import json
import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from github_work_items import (  # noqa: E402
    ChangeSignals,
    PackageChange,
    WorkItemStateError,
    build_work_item,
    load_work_items,
    recommend_ingest_mode,
    record_collection_failure,
    render_status,
    save_work_items,
    transition_work_item,
    upsert_discovered_work_item,
)


class GitHubWorkItemTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.path = self.root / "tracking/github/work-items.json"
        self.snapshot_manifest = (
            "raw/github/paypal/paypal-js/snapshots/2026-07-20-3caece5/manifest.json"
        )
        self.paypal_change = self.change(
            package="@paypal/paypal-js",
            from_version="9.4.0",
            to_version="10.0.0",
            recommended_mode="full",
            reasons=("major-version-transition",),
        )
        self.react_change = self.change(
            package="@paypal/react-paypal-js",
            from_version="9.1.1",
            to_version="10.0.0",
            recommended_mode="full",
            reasons=("major-version-transition",),
        )
        self.awaiting_item = replace(
            build_work_item(
                "paypal/paypal-js",
                "3caece5" * 5 + "3caec",
                "2026-07-20",
                (self.paypal_change,),
                self.snapshot_manifest,
            ),
            state="awaiting_approval",
        )

    def signals(self, **overrides):
        values = {
            "package": "@paypal/paypal-js",
            "from_version": "10.0.2",
            "to_version": "10.0.3",
            "changed_paths": (),
            "public_exports_changed": False,
            "release_notes": "Routine maintenance.",
        }
        values.update(overrides)
        return ChangeSignals(**values)

    def change(
        self,
        package="@paypal/paypal-js",
        from_version="10.0.2",
        to_version="10.0.3",
        recommended_mode="delta",
        reasons=("contained-patch-release",),
    ):
        slug = package.rsplit("/", 1)[-1]
        return PackageChange(
            package=package,
            from_version=from_version,
            to_version=to_version,
            release_id=package + "@" + to_version,
            release_manifest=(
                "raw/github/paypal/paypal-js/releases/"
                + slug
                + "/"
                + to_version
                + "/2026-07-20/manifest.json"
            ),
            comparison_manifest=(
                "tracking/github/repos/paypal/paypal-js/comparisons/"
                + slug
                + "/"
                + (from_version or "baseline")
                + "--"
                + to_version
                + "/comparison.json"
            ),
            recommended_mode=recommended_mode,
            reasons=reasons,
        )

    def test_baseline_and_major_upgrade_require_full_ingest(self):
        baseline = self.signals(from_version="", to_version="8.9.2")
        major = self.signals(from_version="9.3.0", to_version="10.0.0")

        self.assertEqual("full", recommend_ingest_mode(baseline)[0])
        self.assertEqual("full", recommend_ingest_mode(major)[0])

    def test_small_patch_defaults_to_delta(self):
        signals = self.signals(
            from_version="10.0.2",
            to_version="10.0.3",
            changed_paths=("packages/paypal-js/src/types.ts",),
        )

        mode, reasons = recommend_ingest_mode(signals)

        self.assertEqual("delta", mode)
        self.assertIn("contained-patch-release", reasons)

    def test_public_export_change_escalates_patch_to_full(self):
        signals = self.signals(
            from_version="10.0.2",
            to_version="10.0.3",
            public_exports_changed=True,
        )

        mode, reasons = recommend_ingest_mode(signals)

        self.assertEqual("full", mode)
        self.assertIn("public-exports-changed", reasons)

    def test_same_sha_package_changes_form_one_work_item(self):
        item = build_work_item(
            "paypal/paypal-js",
            "3caece5" * 5 + "3caec",
            "2026-07-20",
            (self.paypal_change, self.react_change),
            self.snapshot_manifest,
        )

        self.assertEqual(2, len(item.package_changes))
        self.assertEqual("full", item.recommended_mode)

    def test_user_approval_is_required_before_ingesting(self):
        save_work_items(self.path, (self.awaiting_item,))

        with self.assertRaises(WorkItemStateError):
            transition_work_item(
                self.path,
                self.awaiting_item.work_item_id,
                "awaiting_approval",
                "ingesting",
            )

        approved = transition_work_item(
            self.path,
            self.awaiting_item.work_item_id,
            "awaiting_approval",
            "approved",
            approved_mode="delta",
        )[0]
        self.assertEqual("approved", approved.state)
        self.assertEqual("delta", approved.approved_mode)

    def test_three_attempts_in_one_run_record_collection_failure(self):
        item = build_work_item(
            "paypal/paypal-js",
            "a" * 40,
            "2026-07-20",
            (self.paypal_change,),
            self.snapshot_manifest,
        )

        saved = record_collection_failure(
            self.path, item, "temporary Git failure", "2026-07-20", 3
        )[0]

        self.assertEqual("collection_failed", saved.state)
        self.assertEqual(3, saved.attempts_in_run)
        self.assertEqual(1, saved.consecutive_failed_runs)

    def test_three_consecutive_failed_runs_require_manual_review(self):
        item = build_work_item(
            "paypal/paypal-js",
            "b" * 40,
            "2026-07-20",
            (self.paypal_change,),
            self.snapshot_manifest,
        )

        for attempted_date in ("2026-07-20", "2026-07-21", "2026-07-22"):
            item = record_collection_failure(
                self.path, item, "temporary Git failure", attempted_date, 3
            )[0]

        self.assertEqual("needs_manual_review", item.state)
        self.assertEqual(3, item.consecutive_failed_runs)

    def test_explicit_retry_preserves_last_successful_evidence_paths(self):
        failed = replace(
            self.awaiting_item,
            state="collection_failed",
            attempts_in_run=3,
            consecutive_failed_runs=1,
            last_error="temporary Git failure",
            last_attempted_date="2026-07-20",
        )
        save_work_items(self.path, (failed,))

        retried = transition_work_item(
            self.path, failed.work_item_id, "collection_failed", "discovered"
        )[0]

        self.assertEqual("discovered", retried.state)
        self.assertEqual(0, retried.attempts_in_run)
        self.assertEqual(failed.snapshot_manifest, retried.snapshot_manifest)
        self.assertEqual(
            failed.package_changes[0].release_manifest,
            retried.package_changes[0].release_manifest,
        )

    def test_upsert_is_idempotent_and_does_not_reset_progress(self):
        save_work_items(self.path, (self.awaiting_item,))
        repeated = upsert_discovered_work_item(
            self.path, replace(self.awaiting_item, state="discovered")
        )

        self.assertEqual((self.awaiting_item,), repeated)
        self.assertEqual("awaiting_approval", repeated[0].state)

    def test_discovered_retry_can_complete_missing_evidence_without_new_id(self):
        incomplete = replace(
            self.awaiting_item,
            state="discovered",
            snapshot_manifest="",
            package_changes=(
                replace(
                    self.awaiting_item.package_changes[0],
                    release_manifest="",
                    comparison_manifest="",
                ),
            ),
        )
        save_work_items(self.path, (incomplete,))

        merged = upsert_discovered_work_item(
            self.path, replace(self.awaiting_item, state="discovered")
        )[0]

        self.assertEqual(incomplete.work_item_id, merged.work_item_id)
        self.assertEqual(self.snapshot_manifest, merged.snapshot_manifest)
        self.assertTrue(merged.package_changes[0].release_manifest)

    def test_loader_rejects_duplicate_keys_and_unknown_fields(self):
        self.path.parent.mkdir(parents=True)
        self.path.write_text(
            '{"format_version":1,"format_version":1,"work_items":[]}',
            encoding="utf-8",
        )
        with self.assertRaises(ValueError):
            load_work_items(self.path)

        self.path.write_text(
            json.dumps({"format_version": 1, "work_items": [], "extra": True}),
            encoding="utf-8",
        )
        with self.assertRaises(ValueError):
            load_work_items(self.path)

    def test_status_is_generated_from_work_items(self):
        status = render_status((self.awaiting_item,))

        self.assertIn("paypal/paypal-js", status)
        self.assertIn("@paypal/paypal-js@10.0.0", status)
        self.assertIn("awaiting_approval", status)
        self.assertIn(self.snapshot_manifest, status)

    def test_approval_states_require_published_evidence(self):
        incomplete = replace(self.awaiting_item, snapshot_manifest="")

        with self.assertRaises(ValueError):
            save_work_items(self.path, (incomplete,))


if __name__ == "__main__":
    unittest.main()
