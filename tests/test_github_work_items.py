import json
import hashlib
import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import github_work_items  # noqa: E402
from github_work_items import (  # noqa: E402
    BROAD_CHANGE_FILE_LIMIT,
    ChangeSignals,
    PackageChange,
    PacketStatusSummary,
    RefChange,
    RefChangeSignals,
    WorkItemStateError,
    build_ref_work_item,
    build_work_item,
    claim_next_ingest,
    load_work_items,
    recommend_ingest_mode,
    recommend_ref_ingest_mode,
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
        item = build_work_item(
            "paypal/paypal-js",
            "3caece5" * 5 + "3caec",
            "2026-07-20",
            (self.paypal_change,),
            self.snapshot_manifest,
        )
        self.ingest_packet = (
            "tracking/github/repos/paypal/paypal-js/ingest-packets/"
            + item.work_item_id
            + "/packet.json"
        )
        self.awaiting_item = replace(
            item,
            ingest_packet=self.ingest_packet,
            state="awaiting_approval",
        )

    def write_attachment_fixture(self):
        snapshot = self.root / self.snapshot_manifest
        snapshot.parent.mkdir(parents=True, exist_ok=True)
        snapshot.write_text(
            json.dumps(
                {
                    "repository": self.awaiting_item.repo_id,
                    "sha": self.awaiting_item.sha,
                },
                sort_keys=True,
                separators=(",", ":"),
            )
            + "\n",
            encoding="utf-8",
        )
        source = b"export const attached = true;\n"
        supplement_directory = (
            self.root
            / "raw/github/paypal/paypal-js/supplements/2026-07-20-3caece5-attachment"
        )
        source_path = supplement_directory / "files/packages/paypal-js/src/attached.ts"
        source_path.parent.mkdir(parents=True, exist_ok=True)
        source_path.write_bytes(source)
        digest = hashlib.sha256(source).hexdigest()
        identity_payload = {
            "files": [
                {
                    "path": "packages/paypal-js/src/attached.ts",
                    "sha256": digest,
                }
            ],
            "repository": self.awaiting_item.repo_id,
            "sha": self.awaiting_item.sha,
        }
        supplement = {
            "collected_date": "2026-07-20",
            "files": [
                {
                    "classification_reason": "explicit-query-path",
                    "git_blob_oid": "b" * 40,
                    "git_mode": "100644",
                    "package": "",
                    "path": "packages/paypal-js/src/attached.ts",
                    "purpose": "query-supplement",
                    "sha256": digest,
                    "size": len(source),
                }
            ],
            "format_version": 1,
            "identity_sha256": hashlib.sha256(
                json.dumps(
                    identity_payload, sort_keys=True, separators=(",", ":")
                ).encode("utf-8")
            ).hexdigest(),
            "repository": self.awaiting_item.repo_id,
            "sha": self.awaiting_item.sha,
        }
        manifest = supplement_directory / "manifest.json"
        manifest.write_text(
            json.dumps(supplement, sort_keys=True, separators=(",", ":")) + "\n",
            encoding="utf-8",
        )
        return manifest, source_path

    def relative(self, path):
        return Path(path).resolve().relative_to(self.root.resolve()).as_posix()

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

    def ref_change(
        self,
        from_sha="",
        to_sha="b" * 40,
        recommended_mode="full",
        reasons=("initial-commit-baseline",),
        comparison_manifest="",
    ):
        return RefChange(
            ref_kind="default-branch",
            ref_name="main",
            from_sha=from_sha,
            to_sha=to_sha,
            display_identity="default-branch@" + to_sha[:7],
            comparison_manifest=comparison_manifest,
            recommended_mode=recommended_mode,
            reasons=reasons,
        )

    def ref_item(self, **overrides):
        values = {
            "repo_id": "paypal-examples/v6-web-sdk-sample-integration",
            "sha": "b" * 40,
            "collection_date": "2026-08-03",
            "ref_changes": (self.ref_change(),),
            "snapshot_manifest": (
                "raw/github/paypal-examples/v6-web-sdk-sample-integration/"
                "snapshots/2026-08-03-bbbbbbb/manifest.json"
            ),
        }
        values.update(overrides)
        return build_ref_work_item(**values)

    def test_commit_work_item_round_trips_without_package_release_fields(self):
        change = self.ref_change()
        item = self.ref_item(ref_changes=(change,))

        self.assertEqual((), item.package_changes)
        self.assertEqual((change,), item.ref_changes)
        save_work_items(self.path, (item,))
        saved = json.loads(self.path.read_text(encoding="utf-8"))["work_items"][0]
        self.assertNotIn("package_changes", saved)
        self.assertIn("ref_changes", saved)
        self.assertEqual((item,), load_work_items(self.path))

        release_payload = github_work_items._work_item_to_dict(self.awaiting_item)
        self.assertIn("package_changes", release_payload)
        self.assertNotIn("ref_changes", release_payload)

    def test_commit_and_package_change_families_are_mutually_exclusive(self):
        mixed = replace(self.ref_item(), package_changes=(self.paypal_change,))

        with self.assertRaisesRegex(ValueError, "exactly one change family"):
            save_work_items(self.path, (mixed,))

    def test_commit_work_item_validates_sha_identity_and_lifecycle(self):
        comparison = (
            "tracking/github/repos/paypal-examples/v6-web-sdk-sample-integration/"
            "comparisons/default-branch/aaaaaaaa--bbbbbbb/comparison.json"
        )
        change = self.ref_change(
            from_sha="a" * 40,
            recommended_mode="delta",
            reasons=("contained-commit-change",),
            comparison_manifest=comparison,
        )
        item = self.ref_item(ref_changes=(change,))
        packet = (
            "tracking/github/repos/paypal-examples/v6-web-sdk-sample-integration/"
            "ingest-packets/" + item.work_item_id + "/packet.json"
        )
        awaiting = replace(item, ingest_packet=packet, state="awaiting_approval")
        save_work_items(self.path, (awaiting,))

        approved = transition_work_item(
            self.path,
            item.work_item_id,
            "awaiting_approval",
            "approved",
            approved_mode="delta",
        )[0]
        claimed = claim_next_ingest(self.path)
        completed = transition_work_item(
            self.path,
            item.work_item_id,
            "ingesting",
            "ingested",
        )[0]

        self.assertEqual("approved", approved.state)
        self.assertEqual("ingesting", claimed.state)
        self.assertEqual("ingested", completed.state)
        status = render_status((completed,))
        self.assertIn("default-branch@bbbbbbb", status)
        self.assertNotIn("### Package releases", status)

        invalid = replace(
            item,
            ref_changes=(
                replace(
                    change,
                    to_sha="c" * 40,
                    display_identity="default-branch@ccccccc",
                ),
            ),
        )
        with self.assertRaisesRegex(ValueError, "to_sha must equal work-item SHA"):
            save_work_items(self.path, (invalid,))

    def test_commit_recommendations_are_mechanical(self):
        cases = (
            (
                RefChangeSignals("", "b" * 40, ()),
                ("full", ("initial-commit-baseline",)),
            ),
            (
                RefChangeSignals("a" * 40, "b" * 40, ("client/components/paypal/button.ts",)),
                ("delta", ("contained-commit-change",)),
            ),
            (
                RefChangeSignals("a" * 40, "b" * 40, ("server/node/src/routes/auth.ts",)),
                ("full", ("server-architecture-signal",)),
            ),
            (
                RefChangeSignals("a" * 40, "b" * 40, ("client/components/vault/capture.ts",)),
                ("full", ("payment-behavior-signal",)),
            ),
            (
                RefChangeSignals(
                    "a" * 40,
                    "b" * 40,
                    tuple("client/components/file-" + str(index) + ".ts" for index in range(BROAD_CHANGE_FILE_LIMIT + 1)),
                ),
                ("full", ("broad-change-set",)),
            ),
        )

        for signals, expected in cases:
            with self.subTest(expected=expected):
                self.assertEqual(expected, recommend_ref_ingest_mode(signals))

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

    def test_work_item_accepts_case_sensitive_tagged_package_identity(self):
        change = self.change(
            package="BraintreeDropIn",
            from_version="",
            to_version="9.14.0",
            recommended_mode="full",
            reasons=("initial-release-baseline",),
        )

        item = build_work_item(
            "braintree/braintree-ios-drop-in",
            "d951d10" * 5 + "d951d",
            "2026-08-13",
            (change,),
            "raw/github/braintree/braintree-ios-drop-in/snapshots/2026-08-13-d951d10/manifest.json",
        )

        self.assertEqual("BraintreeDropIn@9.14.0", item.package_changes[0].release_id)

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

    def test_claim_next_ingest_is_atomic_and_globally_serial(self):
        first = replace(self.awaiting_item, state="approved", approved_mode="full")
        second = replace(
            build_work_item(
                "paypal/paypal-js",
                "4caece5" * 5 + "4caec",
                "2026-07-21",
                (replace(self.paypal_change, to_version="10.0.1", release_id="@paypal/paypal-js@10.0.1"),),
                self.snapshot_manifest.replace("3caece5", "4caece5"),
            ),
            state="approved",
            approved_mode="delta",
        )
        save_work_items(self.path, (first, second))

        claimed = claim_next_ingest(self.path)

        self.assertEqual(first.work_item_id, claimed.work_item_id)
        states = {item.work_item_id: item.state for item in load_work_items(self.path)}
        self.assertEqual("ingesting", states[first.work_item_id])
        self.assertEqual("approved", states[second.work_item_id])
        with self.assertRaisesRegex(WorkItemStateError, "already in progress"):
            claim_next_ingest(self.path)

    def test_transition_rejects_a_second_ingesting_item(self):
        first = replace(self.awaiting_item, state="ingesting", approved_mode="full")
        second = replace(
            build_work_item(
                "paypal/paypal-js",
                "4caece5" * 5 + "4caec",
                "2026-07-21",
                (replace(self.paypal_change, to_version="10.0.1", release_id="@paypal/paypal-js@10.0.1"),),
                self.snapshot_manifest.replace("3caece5", "4caece5"),
            ),
            state="approved",
            approved_mode="delta",
        )
        save_work_items(self.path, (first, second))

        with self.assertRaisesRegex(WorkItemStateError, "already in progress"):
            transition_work_item(
                self.path, second.work_item_id, "approved", "ingesting"
            )

    def test_late_collection_failure_does_not_demote_finalized_or_ingest_states(self):
        for state, approved_mode in (
            ("collected", None),
            ("awaiting_approval", None),
            ("approved", "full"),
            ("ingesting", "full"),
            ("ingested", "full"),
        ):
            with self.subTest(state=state):
                current = replace(
                    self.awaiting_item,
                    state=state,
                    approved_mode=approved_mode,
                )
                save_work_items(self.path, (current,))

                retained = record_collection_failure(
                    self.path,
                    replace(self.awaiting_item, state="discovered"),
                    "late collector failed",
                    "2026-07-21",
                    3,
                )[0]

                self.assertEqual(current, retained)

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

    def test_atomic_finalization_publishes_new_item_directly_to_approval(self):
        discovered = replace(self.awaiting_item, state="discovered")

        finalized = github_work_items.finalize_collected_work_item(
            self.path,
            discovered,
        )[0]

        self.assertEqual("awaiting_approval", finalized.state)
        self.assertIsNone(finalized.approved_mode)
        self.assertEqual((finalized,), load_work_items(self.path))

    def test_new_finalization_requires_packet_but_historical_json_remains_valid(self):
        with self.assertRaisesRegex(
            WorkItemStateError,
            "ingest packet",
        ):
            github_work_items.finalize_collected_work_item(
                self.path,
                replace(
                    self.awaiting_item,
                    state="discovered",
                    ingest_packet="",
                ),
            )

        document = {
            "format_version": 1,
            "work_items": [
                github_work_items._work_item_to_dict(self.awaiting_item)
            ],
        }
        document["work_items"][0].pop("ingest_packet")
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(document), encoding="utf-8")

        loaded = load_work_items(self.path)

        self.assertEqual("", loaded[0].ingest_packet)
        save_work_items(self.path, loaded)
        self.assertEqual("", load_work_items(self.path)[0].ingest_packet)

    def test_packet_pointer_is_immutable_collection_evidence(self):
        save_work_items(self.path, (self.awaiting_item,))
        conflict = replace(
            self.awaiting_item,
            state="discovered",
            ingest_packet=self.ingest_packet.replace(
                "repos/paypal/paypal-js/",
                "repos/paypal/other/",
            ),
        )

        with self.assertRaisesRegex(ValueError, "conflicts with discovered evidence"):
            github_work_items.finalize_collected_work_item(self.path, conflict)

    def test_atomic_finalization_recovers_collection_failures_with_same_identity(self):
        for failed_state in ("collection_failed", "needs_manual_review"):
            with self.subTest(failed_state=failed_state):
                incomplete = replace(
                    self.awaiting_item,
                    state=failed_state,
                    snapshot_manifest="",
                    package_changes=(
                        replace(
                            self.awaiting_item.package_changes[0],
                            release_manifest="",
                            comparison_manifest="",
                        ),
                    ),
                    attempts_in_run=3,
                    consecutive_failed_runs=2,
                    last_error="temporary Git failure",
                    last_attempted_date="2026-07-21",
                )
                save_work_items(self.path, (incomplete,))
                incoming = replace(
                    self.awaiting_item,
                    state="discovered",
                    collection_date="2026-07-22",
                )

                finalized = github_work_items.finalize_collected_work_item(
                    self.path,
                    incoming,
                )[0]

                self.assertEqual(incomplete.work_item_id, finalized.work_item_id)
                self.assertEqual("2026-07-20", finalized.collection_date)
                self.assertEqual("awaiting_approval", finalized.state)
                self.assertIsNone(finalized.approved_mode)
                self.assertEqual(0, finalized.attempts_in_run)
                self.assertEqual(0, finalized.consecutive_failed_runs)
                self.assertEqual("", finalized.last_error)
                self.assertEqual("", finalized.last_attempted_date)
                self.assertEqual(self.snapshot_manifest, finalized.snapshot_manifest)
                self.assertTrue(finalized.package_changes[0].release_manifest)

    def test_atomic_finalization_is_idempotent_for_identical_approval_item(self):
        save_work_items(self.path, (self.awaiting_item,))

        repeated = github_work_items.finalize_collected_work_item(
            self.path,
            replace(self.awaiting_item, state="discovered"),
        )

        self.assertEqual((self.awaiting_item,), repeated)
        self.assertEqual((self.awaiting_item,), load_work_items(self.path))

    def test_atomic_finalization_rejects_conflicting_evidence_without_mutation(self):
        save_work_items(self.path, (self.awaiting_item,))
        conflict = replace(
            self.awaiting_item,
            state="discovered",
            snapshot_manifest=self.snapshot_manifest.replace(
                "2026-07-20",
                "2026-07-21",
            ),
        )

        with self.assertRaisesRegex(ValueError, "conflicts with discovered evidence"):
            github_work_items.finalize_collected_work_item(self.path, conflict)

        self.assertEqual((self.awaiting_item,), load_work_items(self.path))

    def test_atomic_finalization_rejects_stale_or_ingest_approval(self):
        stale = replace(
            self.awaiting_item,
            state="discovered",
            approved_mode="delta",
        )
        with self.assertRaisesRegex(ValueError, "approved_mode must be null"):
            github_work_items.finalize_collected_work_item(self.path, stale)
        self.assertEqual((), load_work_items(self.path))

        ingest_failed = replace(
            self.awaiting_item,
            state="needs_manual_review",
            approved_mode="delta",
            last_error="grounding validation failed",
            last_attempted_date="2026-07-21",
        )
        save_work_items(self.path, (ingest_failed,))

        with self.assertRaisesRegex(
            WorkItemStateError,
            "collection finalization cannot resume an ingest-failed work item",
        ):
            github_work_items.finalize_collected_work_item(
                self.path,
                replace(self.awaiting_item, state="discovered"),
            )

        self.assertEqual((ingest_failed,), load_work_items(self.path))

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
        status = render_status(
            (self.awaiting_item,),
            {
                self.awaiting_item.work_item_id: PacketStatusSummary(
                    self.ingest_packet,
                    "high",
                    8,
                    0,
                    0,
                )
            },
        )

        self.assertIn("paypal/paypal-js", status)
        self.assertIn("@paypal/paypal-js@10.0.0", status)
        self.assertIn("awaiting_approval", status)
        self.assertIn(self.snapshot_manifest, status)
        self.assertIn("Review priority: `high`", status)
        self.assertIn("Required reading: `8` files", status)
        self.assertIn("packet.md", status)

    def test_status_links_resolve_from_tracking_github_directory(self):
        status = render_status((self.awaiting_item,))

        self.assertIn("[manifest](../../" + self.snapshot_manifest + ")", status)
        self.assertIn(
            "[review packet](repos/paypal/paypal-js/ingest-packets/",
            status,
        )
        self.assertIn(
            "Release: [manifest](../../" + self.paypal_change.release_manifest + ")",
            status,
        )
        self.assertIn(
            "Comparison: [manifest](repos/paypal/paypal-js/comparisons/",
            status,
        )

    def test_work_item_attachment_is_loaded_and_rendered_in_status(self):
        attachment = (
            "tracking/github/repos/paypal/paypal-js/evidence-attachments/"
            + self.awaiting_item.work_item_id
            + "/attachment.json"
        )
        document = {
            "format_version": 1,
            "work_items": [github_work_items._work_item_to_dict(self.awaiting_item)],
        }
        document["work_items"][0]["evidence_attachments"] = [attachment]
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(document), encoding="utf-8")

        try:
            loaded = load_work_items(self.path)[0]
        except ValueError as error:
            self.fail("work-item attachment field must load: " + str(error))
        status = render_status(
            (loaded,),
            {
                loaded.work_item_id: PacketStatusSummary(
                    self.ingest_packet,
                    "high",
                    10,
                    0,
                    0,
                )
            },
        )

        self.assertEqual((attachment,), loaded.evidence_attachments)
        self.assertIn(
            "Evidence attachment: [manifest](repos/paypal/paypal-js/evidence-attachments/",
            status,
        )
        self.assertIn("Required reading: `10` files", status)

    def test_attachment_publication_is_deterministic_and_approval_revalidates_hashes(self):
        publisher = getattr(github_work_items, "publish_evidence_attachment", None)
        required_reading = getattr(
            github_work_items, "evidence_attachment_required_reading", None
        )
        if publisher is None or required_reading is None:
            self.fail("evidence attachment publication API is missing")
        supplement, source = self.write_attachment_fixture()
        first = publisher(self.root, self.awaiting_item, self.relative(supplement))
        first_bytes = (self.root / first.relative_path).read_bytes()
        second = publisher(self.root, self.awaiting_item, self.relative(supplement))
        linked = replace(
            self.awaiting_item,
            evidence_attachments=(first.relative_path,),
        )
        save_work_items(self.path, (linked,))

        self.assertEqual(first, second)
        self.assertEqual(first_bytes, (self.root / second.relative_path).read_bytes())
        self.assertEqual(
            (
                first.relative_path,
                self.relative(supplement),
                self.relative(source),
            ),
            required_reading(self.root, linked),
        )

        source.write_bytes(b"export const attached = fals;\n")
        with self.assertRaisesRegex(ValueError, "attachment file hash mismatch"):
            transition_work_item(
                self.path,
                linked.work_item_id,
                "awaiting_approval",
                "approved",
                approved_mode="full",
            )

    def test_approval_rejects_a_missing_linked_attachment(self):
        attachment = (
            "tracking/github/repos/paypal/paypal-js/evidence-attachments/"
            + self.awaiting_item.work_item_id
            + "/attachment.json"
        )
        document = {
            "format_version": 1,
            "work_items": [github_work_items._work_item_to_dict(self.awaiting_item)],
        }
        document["work_items"][0]["evidence_attachments"] = [attachment]
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(document), encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "evidence attachment is missing"):
            transition_work_item(
                self.path,
                self.awaiting_item.work_item_id,
                "awaiting_approval",
                "approved",
                approved_mode="full",
            )

    def test_approval_rejects_a_published_but_unlinked_attachment(self):
        supplement, _ = self.write_attachment_fixture()
        publisher = getattr(github_work_items, "publish_evidence_attachment", None)
        if publisher is None:
            self.fail("evidence attachment publication API is missing")
        publisher(self.root, self.awaiting_item, self.relative(supplement))
        save_work_items(self.path, (self.awaiting_item,))

        with self.assertRaisesRegex(ValueError, "published evidence attachment is not linked"):
            transition_work_item(
                self.path,
                self.awaiting_item.work_item_id,
                "awaiting_approval",
                "approved",
                approved_mode="full",
            )

    def test_work_item_rejects_an_unsafe_attachment_path(self):
        document = {
            "format_version": 1,
            "work_items": [github_work_items._work_item_to_dict(self.awaiting_item)],
        }
        document["work_items"][0]["evidence_attachments"] = ["../attachment.json"]
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(document), encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "unsafe path"):
            load_work_items(self.path)

    def test_approval_states_require_published_evidence(self):
        incomplete = replace(self.awaiting_item, snapshot_manifest="")

        with self.assertRaises(ValueError):
            save_work_items(self.path, (incomplete,))


if __name__ == "__main__":
    unittest.main()
