import json
import io
import subprocess
import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path
from unittest import mock
from contextlib import redirect_stdout


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import github_work_items  # noqa: E402
from collect_github_repos import (  # noqa: E402
    CollectionUsageError,
    _RetainedRelease,
    _parser,
    _prepare_group,
    approve_one,
    collect_one,
    compare_one,
    fail_ingest,
    main,
    next_ingest,
    parse_package_release,
    retry_one,
    regenerate_status,
    supplement_one,
)
from github_capsule_policy import CapsuleConfig  # noqa: E402
from github_registry import RepoConfig, VersionTrack  # noqa: E402
from github_releases import (  # noqa: E402
    ReleaseCandidate,
    ReleaseEvidenceError,
    ReleaseNotesEvidence,
)
from github_work_items import (  # noqa: E402
    load_work_items,
    save_work_items,
    transition_work_item,
)
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
        self.assertTrue(items[0].ingest_packet)
        packet = json.loads(
            (self.root / items[0].ingest_packet).read_text(encoding="utf-8")
        )
        self.assertEqual("full", packet["recommendation"]["mode"])
        self.assertEqual(
            ["@paypal/paypal-js", "@paypal/react-paypal-js"],
            [row["package"] for row in packet["packages"]],
        )
        self.assertFalse((self.root / "wiki").exists())

    def test_collector_publishes_only_the_atomic_awaiting_approval_state(self):
        queue_writes = []
        events = []
        write_atomic = github_work_items._write_atomic
        from collect_github_repos import publish_queued_packet

        def capture_queue_writes(path, content):
            if Path(path).name == "work-items.json":
                events.append("queue")
                document = json.loads(content)
                queue_writes.append(
                    tuple(item["state"] for item in document["work_items"])
                )
            return write_atomic(path, content)

        def capture_packet(*args, **kwargs):
            events.append("packet")
            return publish_queued_packet(*args, **kwargs)

        with mock.patch.object(
            github_work_items,
            "_write_atomic",
            side_effect=capture_queue_writes,
        ), mock.patch(
            "collect_github_repos.publish_queued_packet",
            side_effect=capture_packet,
        ):
            result = self.collect()

        self.assertEqual("awaiting_approval", result.state)
        self.assertEqual([("awaiting_approval",)], queue_writes)
        self.assertEqual(["packet", "queue"], events)

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
        with mock.patch("collect_github_repos.fetch_required_refs") as fetch:
            result = self.collect(release_mode="future", collection_date="2026-07-21")

        self.assertEqual("unchanged", result.state)
        fetch.assert_not_called()
        self.assertEqual(1, len(load_work_items(self.root / "tracking/github/work-items.json")))

    def test_recollection_creates_release_only_item_for_changed_notes(self):
        self.collect()
        queue = self.root / "tracking/github/work-items.json"
        item = load_work_items(queue)[0]
        transition_work_item(queue, item.work_item_id, "awaiting_approval", "approved", "delta")
        transition_work_item(queue, item.work_item_id, "approved", "ingesting")
        transition_work_item(queue, item.work_item_id, "ingesting", "ingested")

        def corrected_notes(config, candidate):
            return ReleaseNotesEvidence(
                "https://api.github.test/" + candidate.tag,
                "2026-07-07T12:00:00Z",
                ("Corrected release " + candidate.tag + "\n").encode("utf-8"),
            )

        result = self.collect(
            release_mode="future",
            collection_date="2026-07-21",
            release_notes_fetcher=corrected_notes,
        )

        self.assertEqual("awaiting_approval", result.state)
        items = load_work_items(queue)
        self.assertEqual(2, len(items))
        revision = next(value for value in items if value.work_item_id != item.work_item_id)
        self.assertEqual("delta", revision.recommended_mode)
        self.assertTrue(revision.evidence_revision)
        self.assertTrue(
            all(change.reasons == ("release-notes-revision",) for change in revision.package_changes)
        )

    def test_recollection_routes_moved_release_tag_to_manual_review(self):
        self.collect()
        moved_sha = commit_files(
            self.remote,
            {"README.md": "# Moved release tag\n"},
            "move release tag",
        )
        run_git(self.remote, "tag", "-f", "@paypal/paypal-js@10.0.0", moved_sha)

        result = self.collect(
            release="@paypal/paypal-js@10.0.0",
            release_mode=None,
            collection_date="2026-07-21",
            max_attempts=1,
        )

        self.assertEqual("needs_manual_review", result.state)
        self.assertIn("moved", result.errors[0])

    def test_release_tag_version_must_match_package_manifest(self):
        mismatched_sha = commit_files(
            self.remote,
            {
                "packages/paypal-js/package.json": package_manifest(
                    "@paypal/paypal-js", "10.0.2"
                ),
            },
            "manifest version differs from tag",
        )
        tag(self.remote, "@paypal/paypal-js@10.0.1")

        result = self.collect(
            release="@paypal/paypal-js@10.0.1",
            release_mode=None,
            collection_date="2026-07-21",
            max_attempts=1,
        )

        self.assertEqual("needs_manual_review", result.state)
        self.assertIn("package manifest version", result.errors[0])
        self.assertFalse(
            (
                self.root
                / "raw/github/paypal/paypal-js/releases/paypal-js/10.0.1"
            ).exists()
        )
        self.assertNotEqual(self.sha, mismatched_sha)

    def test_tagged_prepare_group_uses_release_identity_without_npm_exports(self):
        prior_sha = commit_files(
            self.remote,
            {
                "README.md": "# Native SDK\n",
                "Native/Source/Checkout.swift": "public struct Checkout {}\n",
            },
            "native baseline",
        )
        current_sha = commit_files(
            self.remote,
            {
                "Native/Source/Checkout.swift": (
                    "public struct Checkout { public let enabled = true }\n"
                ),
            },
            "native patch",
        )
        candidate = ReleaseCandidate(
            "stripe-ios",
            "26.4.1",
            "26.4.1",
            current_sha,
            current_sha,
            False,
        )
        config = RepoConfig(
            id="stripe/stripe-ios",
            company="stripe",
            url="https://github.com/stripe/stripe-ios",
            enabled=True,
            repo_type="mobile-sdk",
            priority="tier1",
            track="releases-and-default-branch",
            version_strategy="semver-tags",
            version_tracks=(
                VersionTrack(
                    "package:stripe-ios@26",
                    "latest-stable",
                    "all-stable",
                ),
            ),
            capsules=(
                CapsuleConfig(
                    id="stripe-ios-source",
                    adapter="tagged-tree-v1",
                    focus_packages=("stripe-ios",),
                    dependency_scope="configured-repository-paths",
                    changed_path_policy="policy-bounded",
                    default_required_roots=("Native/Source",),
                    include_paths=("README.md",),
                ),
            ),
        )
        history = {
            "stripe-ios": [
                _RetainedRelease(
                    "stripe-ios",
                    "26.4.0",
                    "26.4.0",
                    prior_sha,
                    "raw/prior/manifest.json",
                    "a" * 64,
                )
            ]
        }

        with mock.patch(
            "collect_github_repos._public_exports",
            side_effect=AssertionError("tagged collection parsed NPM exports"),
        ):
            contexts = _prepare_group(
                self.root,
                config,
                self.remote,
                (candidate,),
                {
                    "stripe-ios@26.4.1": ReleaseNotesEvidence(
                        "https://api.github.test/26.4.1",
                        "2026-07-21T12:00:00Z",
                        b"Native patch.\n",
                    )
                },
                history,
                "2026-07-21",
                set(),
            )

        self.assertEqual(1, len(contexts))
        context = contexts[0]
        self.assertEqual(
            ("Native/Source/Checkout.swift",),
            context.changed_paths,
        )
        self.assertEqual(
            ("Native/Source/Checkout.swift", "README.md"),
            context.from_paths,
        )
        self.assertEqual(
            ("Native/Source/Checkout.swift", "README.md"),
            context.to_paths,
        )
        self.assertFalse(context.public_exports_changed)

    def test_tagged_baseline_collects_without_synthetic_package_manifest(self):
        native_parent = Path(self.directory.name) / "native-fixture"
        native_parent.mkdir()
        native_remote = create_git_repo(native_parent)
        native_sha = commit_files(
            native_remote,
            {
                "README.md": "# Native SDK\n",
                "Package.swift": "// package\n",
                "Native/Source/Checkout.swift": "public struct Checkout {}\n",
                "Native/Tests/CheckoutTests.swift": "test checkout\n",
            },
            "native baseline",
        )
        tag(native_remote, "26.4.1")
        config = RepoConfig(
            id="stripe/stripe-ios",
            company="stripe",
            url="https://github.com/stripe/stripe-ios",
            enabled=True,
            repo_type="mobile-sdk",
            priority="tier1",
            track="releases-and-default-branch",
            version_strategy="semver-tags",
            version_tracks=(
                VersionTrack(
                    "package:stripe-ios@26",
                    "latest-stable",
                    "all-stable",
                    pinned_versions=("26.4.1",),
                ),
            ),
            capsules=(
                CapsuleConfig(
                    id="stripe-ios-source",
                    adapter="tagged-tree-v1",
                    focus_packages=("stripe-ios",),
                    dependency_scope="configured-repository-paths",
                    changed_path_policy="policy-bounded",
                    default_required_roots=("Native/Source",),
                    include_paths=("README.md", "Package.swift"),
                    excluded_categories=("tests", "fixtures"),
                    max_capsule_files=20,
                    max_capsule_utf8_bytes=200000,
                    max_packet_files=30,
                    max_packet_utf8_bytes=300000,
                ),
            ),
        )

        result = collect_one(
            self.root,
            config,
            release="stripe-ios@26.4.1",
            clone_source=native_remote,
            release_notes_fetcher=self.release_notes,
            collection_date="2026-07-21",
        )

        self.assertEqual("awaiting_approval", result.state)
        self.assertEqual((native_sha,), tuple(
            item.sha
            for item in load_work_items(
                self.root / "tracking/github/work-items.json"
            )
        ))
        snapshot = json.loads(
            (self.root / result.snapshot_paths[0]).read_text(encoding="utf-8")
        )
        selected = {row["path"] for row in snapshot["files"]}
        self.assertNotIn("package.json", selected)
        packet_path = load_work_items(
            self.root / "tracking/github/work-items.json"
        )[0].ingest_packet
        packet = json.loads(
            (self.root / packet_path).read_text(encoding="utf-8")
        )
        package = packet["packages"][0]
        self.assertEqual("stripe-ios", package["package"])
        self.assertEqual([], package["dependency_changes"])
        self.assertEqual([], package["public_api_changes"])
        self.assertFalse((self.root / "wiki").exists())

    def test_unavailable_exact_release_is_recorded_without_ingest_item(self):
        result = self.collect(
            release="@paypal/paypal-js@10.99.0",
            release_mode=None,
            collection_date="2026-07-21",
        )

        self.assertEqual("not_available", result.state)
        self.assertEqual((), result.work_item_ids)
        self.assertFalse(
            (self.root / "tracking/github/work-items.json").exists()
        )

    def test_equal_date_release_order_uses_semver_not_tag_lexical_order(self):
        for version in ("10.0.2", "10.0.10"):
            commit_files(
                self.remote,
                {
                    "packages/paypal-js/package.json": package_manifest(
                        "@paypal/paypal-js", version
                    ),
                },
                "release " + version,
            )
            tag(self.remote, "@paypal/paypal-js@" + version)

        result = self.collect(dry_run=True)
        paypal = [
            release_id
            for release_id in result.release_ids
            if release_id.startswith("@paypal/paypal-js@")
        ]

        self.assertLess(paypal.index("@paypal/paypal-js@10.0.2"), paypal.index("@paypal/paypal-js@10.0.10"))

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

    def test_same_major_payment_release_uses_bounded_delta_packet(self):
        self.collect()
        next_sha = commit_files(
            self.remote,
            {
                "packages/paypal-js/package.json": package_manifest(
                    "@paypal/paypal-js", "10.0.1"
                ),
                "packages/paypal-js/src/index.ts": "export const loadScript = 2;\n",
            },
            "paypal js payment patch",
        )
        tag(self.remote, "@paypal/paypal-js@10.0.1")

        def payment_notes(config, candidate):
            return ReleaseNotesEvidence(
                "https://api.github.test/" + candidate.tag,
                "2026-07-21T12:00:00Z",
                b"Fix Venmo payment initialization.\n",
            )

        self.collect(
            release_mode="future",
            collection_date="2026-07-21",
            release_notes_fetcher=payment_notes,
        )

        item = next(
            row
            for row in load_work_items(
                self.root / "tracking/github/work-items.json"
            )
            if row.sha == next_sha
        )
        packet = json.loads(
            (self.root / item.ingest_packet).read_text(encoding="utf-8")
        )
        self.assertEqual("delta", item.recommended_mode)
        self.assertEqual("delta", packet["recommendation"]["mode"])
        self.assertEqual("high", packet["recommendation"]["priority"])

    def test_packet_budget_failure_routes_to_manual_review_without_partial_packet(self):
        constrained = replace(
            self.config,
            capsules=(
                replace(
                    self.config.capsules[0],
                    max_packet_files=1,
                ),
            ),
        )

        result = collect_one(
            self.root,
            constrained,
            release_mode="backfill",
            clone_source=self.remote,
            release_notes_fetcher=self.release_notes,
            collection_date="2026-07-20",
            max_attempts=1,
        )

        self.assertEqual("needs_manual_review", result.state)
        self.assertIn("packet budget", result.errors[0])
        packet_root = (
            self.root
            / "tracking/github/repos/paypal/paypal-js/ingest-packets"
        )
        self.assertEqual(
            [],
            list(packet_root.iterdir()) if packet_root.exists() else [],
        )
        item = load_work_items(
            self.root / "tracking/github/work-items.json"
        )[0]
        self.assertEqual("needs_manual_review", item.state)
        self.assertEqual("", item.ingest_packet)

    def test_ad_hoc_compare_writes_review_packet_without_queue_or_wiki_mutation(self):
        self.collect()
        commit_files(
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
        self.collect(release_mode="future", collection_date="2026-07-21")
        queue_path = self.root / "tracking/github/work-items.json"
        queue_before = queue_path.read_bytes()

        comparison = compare_one(
            self.root,
            self.config,
            "@paypal/paypal-js@10.0.0",
            "@paypal/paypal-js@10.0.1",
            clone_source=self.remote,
        )

        self.assertTrue(
            (comparison.metadata_path.parent / "review-packet.json").is_file()
        )
        self.assertTrue(
            (comparison.metadata_path.parent / "review-packet.md").is_file()
        )
        self.assertEqual(queue_before, queue_path.read_bytes())
        self.assertFalse((self.root / "wiki").exists())

    def test_future_collection_cannot_expand_a_policy_bounded_capsule(self):
        bounded_config = replace(
            self.config,
            capsules=(
                replace(
                    self.config.capsules[0],
                    changed_path_policy="policy-bounded",
                ),
            ),
        )
        collect_one(
            self.root,
            bounded_config,
            release_mode="backfill",
            clone_source=self.remote,
            release_notes_fetcher=self.release_notes,
            collection_date="2026-07-20",
        )
        commit_files(
            self.remote,
            {
                "packages/paypal-js/package.json": package_manifest(
                    "@paypal/paypal-js", "10.0.1"
                ),
                "packages/paypal-js/src/index.ts": "export const loadScript = 2;\n",
                "packages/paypal-js/docs/future-option.md": "# Future option\n",
            },
            "paypal js bounded patch",
        )
        tag(self.remote, "@paypal/paypal-js@10.0.1")

        result = collect_one(
            self.root,
            bounded_config,
            release_mode="future",
            clone_source=self.remote,
            release_notes_fetcher=self.release_notes,
            collection_date="2026-07-21",
        )

        manifest_path = self.root / result.snapshot_paths[0]
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        selected = {item["path"] for item in manifest["files"]}
        self.assertIn("packages/paypal-js/src/index.ts", selected)
        self.assertNotIn("packages/paypal-js/docs/future-option.md", selected)

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
        self.assertFalse(
            (self.root / "raw/github/paypal/paypal-js/releases").exists()
        )
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

    def test_successful_retry_clears_active_collection_failure_fields(self):
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
        self.assertEqual(0, recovered.attempts_in_run)
        self.assertEqual(0, recovered.consecutive_failed_runs)
        self.assertEqual("", recovered.last_error)
        self.assertEqual("", recovered.last_attempted_date)
        self.assertTrue(recovered.snapshot_manifest)
        self.assertTrue(all(change.release_manifest for change in recovered.package_changes))

    def test_later_retry_snapshot_failure_does_not_publish_release_manifests(self):
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
        self.assertTrue(all(not change.release_manifest for change in retained.package_changes))
        self.assertFalse(
            (self.root / "raw/github/paypal/paypal-js/releases").exists()
        )

    def test_retry_completes_manual_review_after_partial_evidence_publication(self):
        with mock.patch(
            "collect_github_repos.build_ingest_packet",
            side_effect=ValueError("unclassified retained evidence"),
        ):
            failed_result = self.collect(max_attempts=1)

        failed = load_work_items(self.root / "tracking/github/work-items.json")[0]
        self.assertEqual("needs_manual_review", failed_result.state)
        self.assertTrue(failed.snapshot_manifest)
        self.assertTrue(all(change.release_manifest for change in failed.package_changes))

        retry_one(self.root, failed.work_item_id)
        recovered_result = self.collect(collection_date="2026-07-21")
        recovered = load_work_items(self.root / "tracking/github/work-items.json")[0]

        self.assertEqual("awaiting_approval", recovered_result.state)
        self.assertEqual(failed.work_item_id, recovered.work_item_id)
        self.assertTrue(recovered.ingest_packet)
        self.assertEqual(0, recovered.consecutive_failed_runs)
        self.assertEqual("", recovered.last_error)

    def test_approve_records_user_selected_mode_before_ingest(self):
        self.collect()
        item = load_work_items(self.root / "tracking/github/work-items.json")[0]

        approve_one(self.root, item.work_item_id, "delta")
        approved = load_work_items(self.root / "tracking/github/work-items.json")[0]

        self.assertEqual("approved", approved.state)
        self.assertEqual("delta", approved.approved_mode)

    def test_next_ingest_claims_oldest_approved_item(self):
        self.collect()
        item = load_work_items(self.root / "tracking/github/work-items.json")[0]
        approve_one(self.root, item.work_item_id, "full")

        selected = next_ingest(self.root)
        claimed = load_work_items(self.root / "tracking/github/work-items.json")[0]

        self.assertEqual(item.work_item_id, selected.work_item_id)
        self.assertEqual("ingesting", selected.state)
        self.assertEqual("ingesting", claimed.state)

    def test_status_approval_and_next_ingest_include_attachment_required_reading(self):
        self.collect()
        item = load_work_items(self.root / "tracking/github/work-items.json")[0]
        supplement = supplement_one(
            self.root,
            self.config,
            self.sha,
            ("packages/paypal-js/src/index.ts",),
            clone_source=self.remote,
            collection_date="2026-07-21",
        )
        attachment = github_work_items.publish_evidence_attachment(
            self.root,
            item,
            supplement.manifest_path.resolve().relative_to(
                self.root.resolve()
            ).as_posix(),
        )
        linked = replace(
            item,
            evidence_attachments=(attachment.relative_path,),
        )
        save_work_items(
            self.root / "tracking/github/work-items.json",
            (linked,),
        )

        status = regenerate_status(self.root)
        packet = json.loads(
            (self.root / linked.ingest_packet).read_text(encoding="utf-8")
        )
        self.assertIn(attachment.relative_path, status)
        self.assertIn(
            "Required reading: `"
            + str(len(packet["required_reading"]) + len(attachment.required_reading))
            + "` files",
            status,
        )

        approve_one(self.root, linked.work_item_id, "full")
        output = io.StringIO()
        with mock.patch("collect_github_repos.PROJECT_ROOT", self.root), redirect_stdout(output):
            self.assertEqual(0, main(["next-ingest"]))
        payload = json.loads(output.getvalue())

        self.assertEqual("ingesting", payload["state"])
        self.assertEqual(
            packet["required_reading"] + list(attachment.required_reading),
            payload["required_reading"],
        )

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

    def test_retry_accepts_manual_review_without_approval(self):
        self.collect()
        queue = self.root / "tracking/github/work-items.json"
        item = load_work_items(queue)[0]
        transition_work_item(
            queue,
            item.work_item_id,
            "awaiting_approval",
            "approved",
            approved_mode="delta",
        )
        transition_work_item(queue, item.work_item_id, "approved", "ingesting")
        ingest_failed = fail_ingest(
            self.root,
            item.work_item_id,
            "grounding validation failed",
        )
        collection_failed = replace(
            ingest_failed,
            approved_mode=None,
            last_error="collection policy needs review",
        )
        save_work_items(queue, (collection_failed,))

        retried = retry_one(self.root, item.work_item_id)

        self.assertEqual("discovered", retried.state)
        self.assertIsNone(retried.approved_mode)
        self.assertEqual("collection policy needs review", retried.last_error)

    def test_retry_rejects_ingest_failure_without_mutation(self):
        self.collect()
        item = load_work_items(self.root / "tracking/github/work-items.json")[0]
        approve_one(self.root, item.work_item_id, "delta")
        next_ingest(self.root)
        ingest_failed = fail_ingest(
            self.root,
            item.work_item_id,
            "grounding validation failed",
        )

        with self.assertRaisesRegex(
            ValueError,
            "collection retry cannot resume an ingest-failed work item",
        ):
            retry_one(self.root, item.work_item_id)

        retained = load_work_items(
            self.root / "tracking/github/work-items.json"
        )[0]
        self.assertEqual(ingest_failed, retained)
        self.assertEqual("delta", retained.approved_mode)
        self.assertEqual("grounding validation failed", retained.last_error)

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
        completed = parser.parse_args(
            ["complete-ingest", "--item", "github-" + "a" * 20]
        )
        failed = parser.parse_args(
            ["fail-ingest", "--item", "github-" + "a" * 20, "--error", "grounding failed"]
        )
        supplement = parser.parse_args(
            [
                "supplement",
                "--repo",
                "paypal/paypal-js",
                "--sha",
                "a" * 40,
                "--path",
                "packages/paypal-js/src/index.ts",
            ]
        )

        self.assertEqual("backfill", collect.release_mode)
        self.assertEqual("@paypal/paypal-js@10.0.0", release.release)
        self.assertEqual("delta", approve.mode)
        self.assertEqual("complete-ingest", completed.command)
        self.assertEqual("grounding failed", failed.error)
        self.assertEqual(("packages/paypal-js/src/index.ts",), tuple(supplement.paths))
        for retired in ("prepare", "packet" + "-state"):
            with self.assertRaises(SystemExit):
                parser.parse_args([retired])

    def test_supplement_collects_requested_path_without_mutating_snapshot(self):
        self.collect()
        snapshot = next(
            (self.root / "raw/github/paypal/paypal-js/snapshots").glob("*/manifest.json")
        )
        before = snapshot.read_bytes()

        supplement = supplement_one(
            self.root,
            self.config,
            self.sha,
            ("packages/paypal-js/src/index.ts",),
            clone_source=self.remote,
            collection_date="2026-07-21",
        )

        self.assertEqual(before, snapshot.read_bytes())
        self.assertEqual(
            ("packages/paypal-js/src/index.ts",),
            supplement.files,
        )

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

class CommitCollectGitHubReposTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        base = Path(self.directory.name)
        self.root = base / "wiki"
        self.root.mkdir()
        parent = base / "fixture"
        parent.mkdir()
        self.remote = create_git_repo(parent)
        self.sha = commit_files(
            self.remote,
            {
                "README.md": "# Sample integration\n",
                "LICENSE": "Apache-2.0\n",
                "client/button.ts": "export const button = 1;\n",
                "client/button.test.ts": "test button\n",
                "server/health.ts": "export const health = true;\n",
            },
            "initial sample",
        )
        self.config = RepoConfig(
            id="paypal-examples/v6-web-sdk-sample-integration",
            company="paypal",
            url="https://github.com/paypal-examples/v6-web-sdk-sample-integration",
            enabled=True,
            repo_type="sample-app",
            priority="tier1",
            track="default-branch",
            version_strategy="commit",
            max_file_bytes=512000,
            max_snapshot_bytes=2000000,
            capsules=(
                CapsuleConfig(
                    id="paypal-v6-sample-source",
                    adapter="commit-tree-v1",
                    source_id="v6-web-sdk-sample-integration",
                    dependency_scope="configured-repository-paths",
                    changed_path_policy="policy-bounded",
                    default_required_roots=("client", "server"),
                    include_paths=("LICENSE", "README.md"),
                    excluded_categories=("tests", "fixtures"),
                    max_capsule_files=100,
                    max_capsule_utf8_bytes=1000000,
                    max_packet_files=150,
                    max_packet_utf8_bytes=1500000,
                ),
            ),
        )

    def collect(self, mode="backfill", **overrides):
        values = {
            "release_mode": mode,
            "clone_source": self.remote,
            "collection_date": "2026-08-03",
        }
        values.update(overrides)
        return collect_one(self.root, self.config, **values)

    def test_commit_dry_run_and_disabled_policy_publish_nothing(self):
        result = self.collect(dry_run=True)

        self.assertEqual("discovered", result.state)
        self.assertEqual(("default-branch@" + self.sha[:7],), result.ref_ids)
        self.assertEqual(4, result.inventory.selected_file_count)
        self.assertEqual(1, result.inventory.excluded_file_count)
        self.assertEqual((), result.snapshot_paths)
        self.assertEqual((), result.work_item_ids)
        self.assertFalse((self.root / "raw").exists())
        self.assertFalse((self.root / "tracking").exists())

        disabled = replace(self.config, enabled=False)
        allowed = collect_one(
            self.root,
            disabled,
            release_mode="backfill",
            dry_run=True,
            clone_source=self.remote,
            collection_date="2026-08-03",
        )
        self.assertEqual("discovered", allowed.state)
        with self.assertRaisesRegex(CollectionUsageError, "disabled"):
            collect_one(
                self.root,
                disabled,
                release_mode="backfill",
                clone_source=self.remote,
                collection_date="2026-08-03",
            )

    def test_commit_collection_handles_baseline_unchanged_excluded_and_delta(self):
        baseline = self.collect()
        baseline_items = load_work_items(self.root / "tracking/github/work-items.json")

        self.assertEqual("awaiting_approval", baseline.state)
        self.assertEqual(1, len(baseline_items))
        self.assertEqual((), baseline_items[0].package_changes)
        self.assertEqual("full", baseline_items[0].ref_changes[0].recommended_mode)
        self.assertEqual("", baseline_items[0].ref_changes[0].from_sha)
        self.assertEqual("unchanged", self.collect().state)
        self.assertEqual("unchanged", self.collect(mode="future").state)

        excluded_sha = commit_files(
            self.remote,
            {"client/button.test.ts": "updated test only\n"},
            "change excluded test",
        )
        excluded = self.collect(mode="future", collection_date="2026-08-04")
        self.assertEqual("unchanged", excluded.state)
        self.assertEqual("default-branch@" + excluded_sha[:7], excluded.ref_ids[0])
        snapshots = self.root / "raw/github/paypal/v6-web-sdk-sample-integration/snapshots"
        self.assertEqual(1, len(list(snapshots.glob("*/manifest.json"))))

        changed_sha = commit_files(
            self.remote,
            {"client/button.ts": "export const button = 2;\n"},
            "change selected client source",
        )
        changed = self.collect(mode="future", collection_date="2026-08-05")
        items = load_work_items(self.root / "tracking/github/work-items.json")
        latest = next(item for item in items if item.sha == changed_sha)

        self.assertEqual("awaiting_approval", changed.state)
        self.assertEqual("delta", latest.ref_changes[0].recommended_mode)
        self.assertTrue(latest.ref_changes[0].comparison_manifest)
        self.assertTrue((self.root / latest.ingest_packet).is_file())

    def test_commit_broad_change_is_full_and_release_selector_is_rejected(self):
        self.collect()
        files = {
            "client/generated-example-" + str(index) + ".ts": "export const value = " + str(index) + ";\n"
            for index in range(github_work_items.BROAD_CHANGE_FILE_LIMIT + 1)
        }
        broad_sha = commit_files(self.remote, files, "add broad selected change")

        result = self.collect(mode="future", collection_date="2026-08-04")
        item = next(
            value
            for value in load_work_items(self.root / "tracking/github/work-items.json")
            if value.sha == broad_sha
        )

        self.assertEqual("awaiting_approval", result.state)
        self.assertEqual("full", item.ref_changes[0].recommended_mode)
        self.assertIn("broad-change-set", item.ref_changes[0].reasons)
        with self.assertRaisesRegex(CollectionUsageError, "does not support releases"):
            collect_one(
                self.root,
                self.config,
                release="fake-package@1.0.0",
                clone_source=self.remote,
                collection_date="2026-08-04",
            )

    def test_commit_failure_records_ref_identity_and_retries_without_partial_snapshot(self):
        with mock.patch(
            "collect_github_repos.publish_source_snapshot",
            side_effect=OSError("injected snapshot failure"),
        ):
            failed = self.collect(max_attempts=1)

        self.assertEqual("collection_failed", failed.state)
        self.assertEqual(("default-branch@" + self.sha[:7],), failed.ref_ids)
        item = load_work_items(self.root / "tracking/github/work-items.json")[0]
        self.assertEqual((), item.package_changes)
        self.assertEqual(self.sha, item.ref_changes[0].to_sha)
        self.assertEqual("", item.snapshot_manifest)
        self.assertFalse(
            (self.root / "raw/github/paypal/v6-web-sdk-sample-integration/snapshots").exists()
        )

        retry_one(self.root, item.work_item_id)
        recovered = self.collect(collection_date="2026-08-04")
        recovered_item = next(
            value
            for value in load_work_items(self.root / "tracking/github/work-items.json")
            if value.work_item_id == item.work_item_id
        )
        self.assertEqual("awaiting_approval", recovered.state)
        self.assertTrue(recovered_item.snapshot_manifest)


if __name__ == "__main__":
    unittest.main()
