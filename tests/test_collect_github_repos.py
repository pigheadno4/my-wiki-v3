import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from collect_github_repos import (  # noqa: E402
    CollectionUsageError,
    _parser,
    approve_one,
    collect_one,
    next_ingest,
    parse_package_release,
    retry_one,
)
from github_capsule_policy import CapsuleConfig  # noqa: E402
from github_registry import RepoConfig, VersionTrack  # noqa: E402
from github_releases import ReleaseEvidenceError, ReleaseNotesEvidence  # noqa: E402
from github_work_items import load_work_items, transition_work_item  # noqa: E402
from tests.github_test_support import commit_files, create_git_repo, tag  # noqa: E402


def run_git(repo, *args):
    return subprocess.run(
        ["git"] + list(args),
        cwd=str(repo),
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def package_manifest(name, version):
    return json.dumps(
        {"name": name, "version": version, "main": "./src/index.ts"},
        sort_keys=True,
    ) + "\n"


class CollectGitHubReposTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name) / "wiki"
        self.root.mkdir()
        repository_parent = Path(self.directory.name) / "fixture"
        repository_parent.mkdir()
        self.remote = create_git_repo(repository_parent)
        self.sha = commit_files(
            self.remote,
            {
                "README.md": "# PayPal JS fixture\n",
                "LICENSE": "Apache-2.0\n",
                "package.json": json.dumps(
                    {
                        "name": "paypal-js-fixture",
                        "version": "10.0.0",
                        "private": True,
                        "workspaces": ["packages/*"],
                    },
                    sort_keys=True,
                )
                + "\n",
                "packages/paypal-js/package.json": package_manifest(
                    "@paypal/paypal-js", "10.0.0"
                ),
                "packages/paypal-js/src/index.ts": "export const loadScript = 1;\n",
                "packages/react-paypal-js/package.json": package_manifest(
                    "@paypal/react-paypal-js", "10.0.0"
                ),
                "packages/react-paypal-js/src/index.ts": "export const Provider = 1;\n",
            },
            "release both packages",
        )
        tag(self.remote, "@paypal/paypal-js@10.0.0")
        tag(self.remote, "@paypal/react-paypal-js@10.0.0")
        self.config = RepoConfig(
            id="paypal/paypal-js",
            company="paypal",
            url="https://github.com/paypal/paypal-js",
            enabled=True,
            repo_type="sdk",
            priority="tier1",
            track="releases-and-default-branch",
            version_strategy="monorepo-packages",
            max_file_bytes=512000,
            max_snapshot_bytes=2000000,
            version_tracks=(
                VersionTrack(
                    "package:@paypal/paypal-js@10",
                    "all-stable",
                    "all-stable",
                ),
                VersionTrack(
                    "package:@paypal/react-paypal-js@10",
                    "all-stable",
                    "all-stable",
                ),
            ),
            capsules=(
                CapsuleConfig(
                    id="paypal-js-source",
                    adapter="npm-tracked-source-v1",
                    focus_packages=(
                        "@paypal/paypal-js",
                        "@paypal/react-paypal-js",
                    ),
                    default_required_roots=("src",),
                    default_generated_target_paths=(),
                    max_file_bytes=512000,
                    max_capsule_files=50,
                    max_capsule_utf8_bytes=1000000,
                    max_packet_files=60,
                    max_packet_utf8_bytes=1200000,
                ),
            ),
        )

    def release_notes(self, config, candidate):
        return ReleaseNotesEvidence(
            "https://api.github.test/" + candidate.tag,
            "2026-07-07T12:00:00Z",
            ("Release " + candidate.tag + "\n").encode("utf-8"),
        )

    def collect(self, **values):
        defaults = {
            "release_mode": "backfill",
            "clone_source": self.remote,
            "release_notes_fetcher": self.release_notes,
            "collection_date": "2026-07-20",
        }
        defaults.update(values)
        return collect_one(self.root, self.config, **defaults)

    def test_backfill_groups_same_sha_releases_into_one_awaiting_item(self):
        result = self.collect()

        self.assertEqual("awaiting_approval", result.state)
        items = load_work_items(self.root / "tracking/github/work-items.json")
        self.assertEqual(1, len(items))
        self.assertEqual(2, len(items[0].package_changes))
        self.assertEqual(self.sha, items[0].sha)
        self.assertTrue(items[0].snapshot_manifest)

    def test_backfill_orders_same_sha_releases_by_release_date(self):
        def dated_notes(config, candidate):
            day = "07" if candidate.package == "@paypal/react-paypal-js" else "08"
            return ReleaseNotesEvidence(
                "https://api.github.test/" + candidate.tag,
                "2026-07-" + day + "T12:00:00Z",
                b"Routine release.\n",
            )

        result = self.collect(release_notes_fetcher=dated_notes)

        self.assertEqual(
            (
                "@paypal/react-paypal-js@10.0.0",
                "@paypal/paypal-js@10.0.0",
            ),
            result.release_ids,
        )

    def test_dry_run_orders_releases_by_release_date_without_writes(self):
        def dated_notes(config, candidate):
            day = "07" if candidate.package == "@paypal/react-paypal-js" else "08"
            return ReleaseNotesEvidence(
                "https://api.github.test/" + candidate.tag,
                "2026-07-" + day + "T12:00:00Z",
                b"Routine release.\n",
            )

        result = self.collect(release_notes_fetcher=dated_notes, dry_run=True)

        self.assertEqual("discovered", result.state)
        self.assertEqual(
            (
                "@paypal/react-paypal-js@10.0.0",
                "@paypal/paypal-js@10.0.0",
            ),
            result.release_ids,
        )
        self.assertFalse((self.root / "raw").exists())
        self.assertFalse((self.root / "tracking").exists())

    def test_recollection_with_no_new_release_is_unchanged(self):
        self.collect()
        result = self.collect(release_mode="future", collection_date="2026-07-21")

        self.assertEqual("unchanged", result.state)
        self.assertEqual(1, len(load_work_items(self.root / "tracking/github/work-items.json")))

    def test_future_patch_creates_package_scoped_delta_comparison(self):
        self.collect()
        next_sha = commit_files(
            self.remote,
            {
                "packages/paypal-js/package.json": package_manifest(
                    "@paypal/paypal-js", "10.0.1"
                ),
                "packages/paypal-js/src/index.ts": "export const loadScript = 2;\n",
            },
            "paypal js patch",
        )
        tag(self.remote, "@paypal/paypal-js@10.0.1")

        result = self.collect(release_mode="future", collection_date="2026-07-21")

        self.assertEqual("awaiting_approval", result.state)
        items = load_work_items(self.root / "tracking/github/work-items.json")
        patch_item = next(item for item in items if item.sha == next_sha)
        self.assertEqual("delta", patch_item.recommended_mode)
        self.assertEqual(1, len(patch_item.package_changes))
        change = patch_item.package_changes[0]
        self.assertEqual("@paypal/paypal-js@10.0.1", change.release_id)
        comparison = self.root / change.comparison_manifest
        self.assertTrue(comparison.is_file())
        patch = (comparison.parent / "diff.patch").read_text(encoding="utf-8")
        self.assertIn("packages/paypal-js/src/index.ts", patch)
        self.assertNotIn("packages/react-paypal-js", patch)

    def test_collection_failure_does_not_create_an_ingest_item(self):
        with mock.patch(
            "collect_github_repos.publish_source_snapshot",
            side_effect=OSError("disk full"),
        ):
            result = self.collect(max_attempts=1)

        self.assertEqual("collection_failed", result.state)
        items = load_work_items(self.root / "tracking/github/work-items.json")
        self.assertEqual(1, len(items))
        self.assertEqual("collection_failed", items[0].state)
        self.assertEqual("", items[0].snapshot_manifest)
        with self.assertRaises(ValueError):
            transition_work_item(
                self.root / "tracking/github/work-items.json",
                items[0].work_item_id,
                "collection_failed",
                "awaiting_approval",
            )

    def test_release_note_failure_remains_visible_without_raw_evidence_paths(self):
        def fail_notes(config, candidate):
            raise ReleaseEvidenceError("temporary API failure")

        result = self.collect(release_notes_fetcher=fail_notes, max_attempts=1)

        self.assertEqual("collection_failed", result.state)
        item = load_work_items(self.root / "tracking/github/work-items.json")[0]
        self.assertEqual("collection_failed", item.state)
        self.assertEqual("", item.snapshot_manifest)
        self.assertTrue(all(not change.release_manifest for change in item.package_changes))

    def test_next_periodic_run_completes_the_same_failed_work_item(self):
        def fail_notes(config, candidate):
            raise ReleaseEvidenceError("temporary API failure")

        failed_result = self.collect(
            release_notes_fetcher=fail_notes,
            max_attempts=1,
            collection_date="2026-07-20",
        )
        failed = load_work_items(self.root / "tracking/github/work-items.json")[0]

        recovered_result = self.collect(collection_date="2026-07-21")
        recovered_items = load_work_items(self.root / "tracking/github/work-items.json")

        self.assertEqual("collection_failed", failed_result.state)
        self.assertEqual("awaiting_approval", recovered_result.state)
        self.assertEqual(1, len(recovered_items))
        recovered = recovered_items[0]
        self.assertEqual(failed.work_item_id, recovered.work_item_id)
        self.assertEqual("2026-07-20", recovered.collection_date)
        self.assertTrue(recovered.snapshot_manifest)
        self.assertTrue(all(change.release_manifest for change in recovered.package_changes))

    def test_later_retry_failure_retains_newly_valid_release_manifests(self):
        def fail_notes(config, candidate):
            raise ReleaseEvidenceError("temporary API failure")

        self.collect(release_notes_fetcher=fail_notes, max_attempts=1)
        failed = load_work_items(self.root / "tracking/github/work-items.json")[0]
        retry_one(self.root, failed.work_item_id)

        with mock.patch(
            "collect_github_repos.publish_source_snapshot",
            side_effect=OSError("disk full"),
        ):
            result = self.collect(max_attempts=1, collection_date="2026-07-21")

        retained = load_work_items(self.root / "tracking/github/work-items.json")[0]
        self.assertEqual("collection_failed", result.state)
        self.assertEqual(failed.work_item_id, retained.work_item_id)
        self.assertEqual("", retained.snapshot_manifest)
        self.assertTrue(all(change.release_manifest for change in retained.package_changes))

    def test_approve_records_user_selected_mode_before_ingest(self):
        self.collect()
        item = load_work_items(self.root / "tracking/github/work-items.json")[0]

        approve_one(self.root, item.work_item_id, "delta")
        approved = load_work_items(self.root / "tracking/github/work-items.json")[0]

        self.assertEqual("approved", approved.state)
        self.assertEqual("delta", approved.approved_mode)

    def test_next_ingest_selects_oldest_approved_item_without_mutation(self):
        self.collect()
        item = load_work_items(self.root / "tracking/github/work-items.json")[0]
        approve_one(self.root, item.work_item_id, "full")

        selected = next_ingest(self.root)
        unchanged = load_work_items(self.root / "tracking/github/work-items.json")[0]

        self.assertEqual(item.work_item_id, selected.work_item_id)
        self.assertEqual("approved", unchanged.state)

    def test_retry_requires_failure_state_and_returns_to_discovered(self):
        self.collect()
        item = load_work_items(self.root / "tracking/github/work-items.json")[0]
        with self.assertRaises(ValueError):
            retry_one(self.root, item.work_item_id)

        with mock.patch(
            "collect_github_repos.publish_source_snapshot",
            side_effect=OSError("disk full"),
        ):
            other_root = Path(self.directory.name) / "failed-wiki"
            other_root.mkdir()
            collect_one(
                other_root,
                self.config,
                release_mode="backfill",
                clone_source=self.remote,
                release_notes_fetcher=self.release_notes,
                collection_date="2026-07-20",
                max_attempts=1,
            )
        failed = load_work_items(other_root / "tracking/github/work-items.json")[0]
        retried = retry_one(other_root, failed.work_item_id)
        self.assertEqual("discovered", retried.state)

    def test_parser_exposes_only_focused_commands(self):
        parser = _parser()
        collect = parser.parse_args(
            ["collect", "--repo", "paypal/paypal-js", "--mode", "backfill"]
        )
        release = parser.parse_args(
            [
                "collect",
                "--repo",
                "paypal/paypal-js",
                "--release",
                "@paypal/paypal-js@10.0.0",
            ]
        )
        approve = parser.parse_args(
            ["approve", "--item", "github-" + "a" * 20, "--mode", "delta"]
        )

        self.assertEqual("backfill", collect.release_mode)
        self.assertEqual("@paypal/paypal-js@10.0.0", release.release)
        self.assertEqual("delta", approve.mode)
        for retired in ("prepare", "packet" + "-state"):
            with self.assertRaises(SystemExit):
                parser.parse_args([retired])

    def test_parser_requires_repo_and_rejects_collection_plus_ingest(self):
        parser = _parser()
        with self.assertRaises(SystemExit):
            parser.parse_args(["collect", "--mode", "backfill"])
        with self.assertRaises(SystemExit):
            parser.parse_args(
                [
                    "collect",
                    "--repo",
                    "paypal/paypal-js",
                    "--mode",
                    "backfill",
                    "--ingest",
                ]
            )

    def test_release_parser_rejects_ambiguous_and_cross_package_versions(self):
        with self.assertRaises(CollectionUsageError):
            parse_package_release("v10")
        with self.assertRaises(CollectionUsageError):
            parse_package_release("@paypal/paypal-js@10")

        parser = _parser()
        arguments = parser.parse_args(
            [
                "compare",
                "--repo",
                "paypal/paypal-js",
                "--from",
                "@paypal/paypal-js@9.0.0",
                "--to",
                "@paypal/react-paypal-js@10.0.0",
            ]
        )
        with self.assertRaises(CollectionUsageError):
            parse_package_release(arguments.from_release, arguments.to_release)


if __name__ == "__main__":
    unittest.main()
