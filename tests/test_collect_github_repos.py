"""Tests for the public GitHub collection CLI and orchestration."""

from concurrent.futures import ThreadPoolExecutor
from dataclasses import replace
import fcntl
import json
import os
from pathlib import Path
import sys
import tempfile
import threading
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import collect_github_repos  # noqa: E402
from collect_github_repos import CollectionResult, collect_one, main  # noqa: E402
from github_git import RepoInspection, ResolvedRef  # noqa: E402
from github_packets import PacketError, PacketRecord, VersionEntry, VersionIndex  # noqa: E402
from github_registry import RepoConfig, VersionTrack  # noqa: E402
from github_releases import ReleaseCandidate, ReleaseNotesEvidence  # noqa: E402
from github_snapshot import (  # noqa: E402
    SnapshotPromotionResult,
    SnapshotPromotionToken,
    SnapshotRecord,
)


class CollectGitHubReposTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        registry = self.root / "tracking" / "github" / "repo-registry.toml"
        registry.parent.mkdir(parents=True)
        registry.write_text(
            self.registry_row("paypal/paypal-js", "paypal", True)
            + self.registry_row("paypal/paypal-ios", "paypal", False)
            + self.registry_row("stripe/stripe-ios", "stripe", True),
            encoding="utf-8",
        )

    def registry_row(self, repo_id, company, enabled):
        return (
            "[[repos]]\n"
            + 'id="' + repo_id + '"\n'
            + 'company="' + company + '"\n'
            + 'url="https://github.com/' + repo_id + '"\n'
            + "enabled=" + str(enabled).lower() + "\n"
            + 'repo_type="sdk"\n'
            + 'priority="tier1"\n'
            + 'track="releases-and-default-branch"\n'
            + 'version_strategy="semver-tags"\n'
        )

    def config(self, **overrides):
        values = {
            "id": "paypal/paypal-js",
            "company": "paypal",
            "url": "https://github.com/paypal/paypal-js",
            "enabled": True,
            "repo_type": "sdk",
            "priority": "tier1",
            "track": "releases-and-default-branch",
            "version_strategy": "semver-tags",
        }
        values.update(overrides)
        return RepoConfig(**values)

    def result(self, config, state="unchanged", versions=(), packet_ids=(), events=()):
        return CollectionResult(
            repo_id=config.id,
            state=state,
            versions=tuple(versions),
            packet_ids=tuple(packet_ids),
            events=tuple(events),
        )

    def run_main(self, argv, side_effect=None):
        selected = []

        def fake_collect(root, config, selectors=(), release_mode=None, dry_run=False):
            selected.append((config, tuple(selectors), release_mode, dry_run))
            if side_effect is not None:
                return side_effect(root, config, selectors, release_mode, dry_run)
            target = (selectors[0] if selectors else "release-mode:" + str(release_mode))
            events = (
                {"repo_id": config.id, "selector": target, "selected": True, "state": "selected"},
                {"repo_id": config.id, "selector": target, "state": "unchanged"},
            )
            return self.result(config, events=events)

        with mock.patch.object(collect_github_repos, "PROJECT_ROOT", self.root), mock.patch.object(
            collect_github_repos, "collect_one", side_effect=fake_collect
        ):
            code = main(argv)
        return code, selected

    def test_collect_all_and_company_select_enabled_rows_by_default(self):
        code, selected = self.run_main(("collect", "--all", "--dry-run"))
        self.assertEqual(0, code)
        self.assertEqual(("paypal/paypal-js", "stripe/stripe-ios"), tuple(item[0].id for item in selected))
        self.assertTrue(all(item[3] for item in selected))

        code, selected = self.run_main(("collect", "--company", "paypal", "--dry-run"))
        self.assertEqual(0, code)
        self.assertEqual(("paypal/paypal-js",), tuple(item[0].id for item in selected))

    def test_include_disabled_is_required_for_disabled_batch_rows(self):
        code, selected = self.run_main(
            ("collect", "--company", "paypal", "--include-disabled", "--dry-run")
        )

        self.assertEqual(0, code)
        self.assertEqual(("paypal/paypal-js", "paypal/paypal-ios"), tuple(item[0].id for item in selected))

    def test_explicit_repo_can_select_a_disabled_row(self):
        code, selected = self.run_main(
            ("collect", "--repo", "paypal/paypal-ios", "--ref", "default-branch")
        )

        self.assertEqual(0, code)
        self.assertEqual("paypal/paypal-ios", selected[0][0].id)
        self.assertEqual(("default-branch",), selected[0][1])

    def test_release_mode_backfill_and_future_are_forwarded(self):
        for mode in ("backfill", "future"):
            with self.subTest(mode=mode):
                code, selected = self.run_main(
                    ("collect", "--repo", "paypal/paypal-js", "--release-mode", mode, "--dry-run")
                )
                self.assertEqual(0, code)
                self.assertEqual(mode, selected[0][2])
                self.assertTrue(selected[0][3])

    def test_ref_and_release_mode_are_mutually_exclusive(self):
        code = main(
            (
                "collect",
                "--repo",
                "paypal/paypal-js",
                "--ref",
                "default-branch",
                "--release-mode",
                "future",
            )
        )
        self.assertEqual(2, code)

    def test_unknown_or_empty_selection_is_cli_misuse(self):
        with mock.patch.object(collect_github_repos, "PROJECT_ROOT", self.root):
            self.assertEqual(2, main(("collect", "--repo", "missing/repo")))
            self.assertEqual(2, main(("collect", "--company", "missing")))

    def test_generated_state_validation_error_returns_one_not_cli_misuse(self):
        with mock.patch.object(collect_github_repos, "PROJECT_ROOT", self.root), mock.patch.object(
            collect_github_repos,
            "regenerate_status",
            side_effect=PacketError("invalid generated state"),
        ):
            self.assertEqual(1, main(("status",)))

    def test_compare_prepare_status_and_packet_state_cli_forms(self):
        packet = self.packet()
        with mock.patch.object(collect_github_repos, "PROJECT_ROOT", self.root), mock.patch.object(
            collect_github_repos, "compare_one", return_value=packet
        ) as compare, mock.patch.object(
            collect_github_repos, "prepare_one", return_value=packet
        ) as prepare, mock.patch.object(
            collect_github_repos, "regenerate_status", return_value={"repositories": [], "packets": []}
        ) as status:
            self.assertEqual(
                0,
                main(
                    (
                        "compare",
                        "--repo",
                        "paypal/paypal-js",
                        "--from",
                        "package:@paypal/react-paypal-js@8",
                        "--to",
                        "package:@paypal/react-paypal-js@10",
                    )
                ),
            )
            self.assertEqual(
                0,
                main(("prepare", "--repo", "paypal/paypal-js", "--ref", "default-branch")),
            )
            self.assertEqual(0, main(("status",)))

        compare.assert_called_once()
        prepare.assert_called_once()
        self.assertEqual(3, status.call_count)

        self.write_packet(packet)
        contract_before = (packet.directory / "packet.json").read_bytes()
        with mock.patch.object(collect_github_repos, "PROJECT_ROOT", self.root):
            self.assertEqual(
                0,
                main(
                    (
                        "packet-state",
                        "--repo",
                        "paypal/paypal-js",
                        "--packet",
                        packet.packet_id,
                        "--from",
                        "awaiting-review",
                        "--to",
                        "approved",
                    )
                ),
            )
        self.assertEqual(contract_before, (packet.directory / "packet.json").read_bytes())
        events = [json.loads(line) for line in (packet.directory / "state-events.jsonl").read_text().splitlines()]
        self.assertEqual(("awaiting-review", "approved"), tuple(event["state"] for event in events))

    def test_collect_cli_returns_one_for_failed_or_unreconciled_result(self):
        def failed(root, config, selectors, release_mode, dry_run):
            target = selectors[0] if selectors else "default-branch"
            events = (
                {"repo_id": config.id, "selector": target, "selected": True, "state": "selected"},
                {"repo_id": config.id, "selector": target, "state": "failed"},
            )
            return self.result(config, state="failed", events=events)

        code, _ = self.run_main(
            ("collect", "--repo", "paypal/paypal-js", "--ref", "default-branch"), failed
        )
        self.assertEqual(1, code)

        def unreconciled(root, config, selectors, release_mode, dry_run):
            return self.result(
                config,
                events=(
                    {"repo_id": config.id, "selector": "default-branch", "selected": True, "state": "selected"},
                ),
            )

        code, _ = self.run_main(
            ("collect", "--repo", "paypal/paypal-js", "--ref", "default-branch"), unreconciled
        )
        self.assertEqual(1, code)

    def test_release_dry_run_enumerates_policy_without_raw_or_generated_state(self):
        track = VersionTrack("v10", "all-stable", "all-stable")
        config = self.config(version_tracks=(track,))
        candidates = (
            self.candidate("10.0.0"),
            self.candidate("10.1.0"),
            self.candidate("10.2.0-beta.1", prerelease=True),
        )
        inspection = RepoInspection("main", tuple(self.ref(item) for item in candidates), (), False, False)

        with mock.patch("collect_github_repos.clone_repository", side_effect=self.fake_clone), mock.patch(
            "collect_github_repos.discover_release_candidates", return_value=candidates
        ), mock.patch("collect_github_repos.fetch_required_refs"), mock.patch(
            "collect_github_repos.inspect_repository", return_value=inspection
        ), mock.patch("collect_github_repos.resolve_ref", side_effect=lambda config, inspection, selector: next(ref for ref in inspection.refs if ref.ref_name == selector[4:])), mock.patch(
            "collect_github_repos.build_snapshot"
        ) as build:
            result = collect_one(self.root, config, release_mode="backfill", dry_run=True)

        self.assertEqual(("10.0.0", "10.1.0"), result.versions)
        self.assertEqual((), result.packet_ids)
        self.assertFalse((self.root / "raw").exists())
        self.assertFalse((self.root / "tracking" / "github" / "runs").exists())
        build.assert_not_called()

    def test_release_selection_filters_existing_versions_to_each_track(self):
        tracks = (
            VersionTrack("v9", "minor-baselines", "all-stable"),
            VersionTrack("v10", "minor-baselines", "all-stable"),
        )
        config = self.config(version_tracks=tracks)
        index = VersionIndex(
            config.id,
            (
                self.entry("9.0.0", "a" * 40),
                self.entry("10.0.0", "b" * 40),
            ),
        )

        def candidates(config, clone_path, track):
            major = track.selector[1:]
            return (self.candidate(major + ".0.0"), self.candidate(major + ".1.0"))

        with mock.patch(
            "collect_github_repos.discover_release_candidates", side_effect=candidates
        ):
            selected, failures = collect_github_repos._select_releases(
                config, self.root, index, "backfill"
            )

        self.assertEqual([], failures)
        self.assertEqual(
            ("9.0.0", "9.1.0", "10.0.0", "10.1.0"),
            tuple(candidate.version for candidate, _ in selected),
        )

    def test_future_discovery_recognizes_matching_canonical_refs_and_aliases(self):
        package_track = VersionTrack("package:@scope/widgets@10", "none", "all-stable")
        plain_track = VersionTrack("v10", "none", "all-stable")
        index = VersionIndex(
            "acme/widgets",
            (
                VersionEntry(
                    "tag", "v10.1.0", "10.1.0", "a" * 40,
                    ("@scope/widgets@10.1.0", "v10.1.0"),
                    "raw/github/acme/widgets/snapshots/10.1.0", "2026-07-16",
                    "@scope/widgets", "canonical", "", (),
                ),
                VersionEntry(
                    "package-version", "@scope/widgets@10.2.0", "10.2.0", "b" * 40,
                    ("@scope/widgets@10.2.0", "v10.2.0"),
                    "raw/github/acme/widgets/snapshots/10.2.0", "2026-07-16",
                    "@scope/widgets", "canonical", "", (),
                ),
                VersionEntry(
                    "package-version", "@other/widgets@10.3.0", "10.3.0", "c" * 40,
                    ("@other/widgets@10.3.0",),
                    "raw/github/acme/widgets/snapshots/10.3.0", "2026-07-16",
                    "@other/widgets", "canonical", "", (),
                ),
                VersionEntry(
                    "tag", "v9.9.0", "9.9.0", "d" * 40,
                    ("@scope/widgets@9.9.0", "v9.9.0"),
                    "raw/github/acme/widgets/snapshots/9.9.0", "2026-07-16",
                    "@scope/widgets", "canonical", "", (),
                ),
            ),
        )

        self.assertEqual(
            ("10.1.0", "10.2.0"),
            collect_github_repos._existing_versions_for_track(index, package_track),
        )
        self.assertEqual(
            ("10.1.0", "10.2.0"),
            collect_github_repos._existing_versions_for_track(index, plain_track),
        )

    def test_release_mode_creates_at_most_one_packet_and_terminal_event_per_release(self):
        track = VersionTrack("v10", "all-stable", "all-stable")
        config = self.config(version_tracks=(track,))
        candidates = (self.candidate("10.0.0"), self.candidate("10.1.0"))
        refs = tuple(self.ref(item) for item in candidates)
        inspection = RepoInspection("main", refs, (), False, False)
        index = VersionIndex(config.id, ())

        def fake_build(config, ref, repo_root, raw_root, staging_root, collection_date, **kwargs):
            target = raw_root / "paypal" / "paypal-js" / "snapshots" / (ref.version + "-" + ref.sha[:7])
            staging = staging_root / ("stage-" + ref.version)
            staging.mkdir(parents=True)
            return SnapshotRecord(
                config.id,
                ref,
                "canonical",
                0,
                collection_date,
                staging,
                target,
                (),
                repository_url=config.url,
                company=config.company,
                repo_type=config.repo_type,
            )

        packet_calls = []

        def fake_packet(config, current, packet_root):
            packet = self.packet("baseline-" + current.ref.version)
            packet_calls.append(packet)
            return replace(packet, directory=packet_root / packet.packet_id)

        with mock.patch("collect_github_repos.clone_repository", side_effect=self.fake_clone), mock.patch(
            "collect_github_repos.discover_release_candidates", return_value=candidates
        ), mock.patch("collect_github_repos.fetch_required_refs"), mock.patch(
            "collect_github_repos.inspect_repository", return_value=inspection
        ), mock.patch("collect_github_repos.resolve_ref", side_effect=lambda config, inspection, selector: next(ref for ref in refs if ref.ref_name == selector[4:])), mock.patch(
            "collect_github_repos.fetch_release_notes", return_value=None
        ), mock.patch("collect_github_repos.run_git"), mock.patch(
            "collect_github_repos.load_version_index", return_value=index
        ), mock.patch("collect_github_repos.build_snapshot", side_effect=fake_build), mock.patch(
            "collect_github_repos.promote_snapshot_with_result",
            side_effect=lambda record: SnapshotPromotionResult(record.target_path, False, None),
        ), mock.patch("collect_github_repos.build_baseline_packet", side_effect=fake_packet), mock.patch(
            "collect_github_repos.build_delta_packet",
            side_effect=lambda config, prior, current, repo_root, packet_root: fake_packet(
                config, current, packet_root
            ),
        ), mock.patch(
            "collect_github_repos.save_version_index"
        ):
            result = collect_one(self.root, config, release_mode="backfill")

        terminals = [event for event in result.events if event.get("state") in collect_github_repos.COLLECTION_TERMINAL]
        self.assertEqual(2, len(packet_calls))
        self.assertEqual(2, len(result.packet_ids))
        self.assertEqual(2, len(terminals))
        self.assertEqual(2, len({event["selector"] for event in terminals}))

    def test_failure_cleans_temporary_snapshot_staging_and_records_terminal_event(self):
        config = self.config()
        ref = ResolvedRef(config.id, "branch", "main", "a" * 40, "main", (), "2026-07-16T00:00:00Z", None)
        inspection = RepoInspection("main", (ref,), (), False, False)
        staging = self.root / "raw" / "github" / ".staging" / "injected"

        def fake_build(*args, **kwargs):
            staging.mkdir(parents=True)
            return SnapshotRecord(config.id, ref, "canonical", 0, "2026-07-16", staging, self.root / "target", ())

        with mock.patch("collect_github_repos.clone_repository", side_effect=self.fake_clone), mock.patch(
            "collect_github_repos.fetch_required_refs"
        ), mock.patch("collect_github_repos.inspect_repository", return_value=inspection), mock.patch(
            "collect_github_repos.resolve_ref", return_value=ref
        ), mock.patch("collect_github_repos.run_git"), mock.patch(
            "collect_github_repos.load_version_index", return_value=VersionIndex(config.id, ())
        ), mock.patch("collect_github_repos.build_snapshot", side_effect=fake_build), mock.patch(
            "collect_github_repos.promote_snapshot_with_result",
            side_effect=ValueError("injected promotion failure"),
        ):
            result = collect_one(self.root, config, ("default-branch",))

        self.assertEqual("failed", result.state)
        self.assertFalse(staging.exists())
        terminals = [event for event in result.events if event.get("state") == "failed"]
        self.assertEqual(1, len(terminals))
        self.assertIn("injected promotion failure", terminals[0]["error"])

    def test_packet_failure_rolls_back_owned_snapshot_after_index_and_under_collection_lock(self):
        config = self.config()
        ref = ResolvedRef(config.id, "branch", "main", "a" * 40, "main", (), "2026-07-16T00:00:00Z", None)
        inspection = RepoInspection("main", (ref,), (), False, False)
        target = (
            self.root
            / "raw"
            / "github"
            / "paypal"
            / "paypal-js"
            / "snapshots"
            / "main-aaaaaaa"
        ).resolve()

        def fake_build(*args, **kwargs):
            staging = self.root / "raw" / "github" / ".staging" / "injected"
            staging.mkdir(parents=True)
            return SnapshotRecord(
                config.id,
                ref,
                "canonical",
                0,
                "2026-07-16",
                staging,
                target,
                (),
                repository_url=config.url,
                company=config.company,
                repo_type=config.repo_type,
            )

        lock_checks = []

        def assert_collection_lock(label):
            lock = (
                self.root
                / "tracking"
                / "github"
                / "repos"
                / "paypal"
                / "paypal-js"
                / ".collection.lock"
            )
            descriptor = os.open(str(lock), os.O_RDWR)
            try:
                with self.assertRaises(BlockingIOError):
                    fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
            finally:
                os.close(descriptor)
            lock_checks.append(label)

        def load_index(*args):
            assert_collection_lock("index-load")
            return VersionIndex(config.id, ())

        def fail_packet(*args):
            assert_collection_lock("packet")
            raise PacketError("injected packet failure")

        real_rollback = collect_github_repos.rollback_promoted_snapshot

        def rollback(token):
            assert_collection_lock("rollback")
            return real_rollback(token)

        with mock.patch("collect_github_repos.clone_repository", side_effect=self.fake_clone), mock.patch(
            "collect_github_repos.fetch_required_refs"
        ), mock.patch("collect_github_repos.inspect_repository", return_value=inspection), mock.patch(
            "collect_github_repos.resolve_ref", return_value=ref
        ), mock.patch("collect_github_repos.run_git"), mock.patch(
            "collect_github_repos.load_version_index", side_effect=load_index
        ), mock.patch("collect_github_repos.build_snapshot", side_effect=fake_build), mock.patch(
            "collect_github_repos.promote_snapshot_with_result", side_effect=self.fake_owned_promotion
        ), mock.patch(
            "collect_github_repos.build_baseline_packet",
            side_effect=fail_packet,
        ), mock.patch(
            "collect_github_repos.rollback_promoted_snapshot", side_effect=rollback
        ):
            result = collect_one(self.root, config, ("default-branch",))

        index_path = (
            self.root
            / "tracking"
            / "github"
            / "repos"
            / "paypal"
            / "paypal-js"
            / "version-index.json"
        ).resolve()
        self.assertEqual("failed", result.state)
        self.assertFalse(target.exists())
        self.assertFalse(index_path.exists())
        self.assertEqual(["index-load", "packet", "rollback"], lock_checks)

    def test_index_rollback_failure_preserves_snapshot_and_referencing_index(self):
        config = self.config()
        ref = ResolvedRef(config.id, "branch", "main", "a" * 40, "main", (), "2026-07-16T00:00:00Z", None)
        inspection = RepoInspection("main", (ref,), (), False, False)
        target = (
            self.root
            / "raw"
            / "github"
            / "paypal"
            / "paypal-js"
            / "snapshots"
            / "main-aaaaaaa"
        ).resolve()
        index_path = (
            self.root
            / "tracking"
            / "github"
            / "repos"
            / "paypal"
            / "paypal-js"
            / "version-index.json"
        ).resolve()

        def fake_build(*args, **kwargs):
            staging = self.root / "raw" / "github" / ".staging" / "rollback-failure"
            staging.mkdir(parents=True)
            return SnapshotRecord(
                config.id,
                ref,
                "canonical",
                0,
                "2026-07-16",
                staging,
                target,
                (),
                repository_url=config.url,
                company=config.company,
                repo_type=config.repo_type,
            )

        real_unlink = Path.unlink

        def fail_index_removal(path, *args, **kwargs):
            if path == index_path:
                raise OSError("injected index rollback failure")
            return real_unlink(path, *args, **kwargs)

        with mock.patch("collect_github_repos.clone_repository", side_effect=self.fake_clone), mock.patch(
            "collect_github_repos.fetch_required_refs"
        ), mock.patch("collect_github_repos.inspect_repository", return_value=inspection), mock.patch(
            "collect_github_repos.resolve_ref", return_value=ref
        ), mock.patch("collect_github_repos.run_git"), mock.patch(
            "collect_github_repos.build_snapshot", side_effect=fake_build
        ), mock.patch(
            "collect_github_repos.promote_snapshot_with_result", side_effect=self.fake_owned_promotion
        ), mock.patch(
            "collect_github_repos.build_baseline_packet",
            side_effect=PacketError("injected packet failure"),
        ), mock.patch.object(Path, "unlink", new=fail_index_removal):
            result = collect_one(self.root, config, ("default-branch",))

        index = collect_github_repos.load_version_index(index_path, config)
        failures = [event for event in result.events if event.get("state") == "failed"]
        self.assertEqual("failed", result.state)
        self.assertTrue(target.is_dir())
        self.assertEqual(1, len(index.versions))
        self.assertTrue(index.versions[0].snapshot_path.endswith("/main-aaaaaaa"))
        self.assertIn("version index rollback failed", failures[0]["error"])

    def test_new_release_alias_on_existing_sha_archives_notes_in_one_supplement_and_packet(self):
        track = VersionTrack("v1", "all-stable", "all-stable")
        config = self.config(version_tracks=(track,))
        first = self.candidate("1.0.0")
        second = self.candidate("1.1.0")
        second = replace(second, object_sha=first.object_sha, commit_sha=first.commit_sha)
        first_ref = self.ref(first)
        second_ref = replace(
            self.ref(second),
            sha=first_ref.sha,
            aliases=(second.tag,),
        )
        notes = ReleaseNotesEvidence(
            "https://api.github.test/releases/v1.1.0",
            "2026-07-16T00:00:00Z",
            b"# Exact 1.1.0 notes\n",
        )

        with mock.patch("collect_github_repos.clone_repository", side_effect=self.fake_clone), mock.patch(
            "collect_github_repos.discover_release_candidates", return_value=(first,)
        ), mock.patch("collect_github_repos.fetch_required_refs"), mock.patch(
            "collect_github_repos.inspect_repository", return_value=RepoInspection("main", (first_ref,), (), False, False)
        ), mock.patch("collect_github_repos.resolve_ref", return_value=first_ref), mock.patch(
            "collect_github_repos.fetch_release_notes", return_value=None
        ), mock.patch("collect_github_repos.run_git"):
            initial = collect_one(self.root, config, release_mode="backfill")

        self.assertEqual(1, len(initial.packet_ids))
        canonical = next(
            path for path in (self.root / "raw" / "github" / "paypal" / "paypal-js" / "snapshots").iterdir()
            if path.name != ".promotion.lock"
        )
        canonical_manifest = (canonical / "snapshot.md").read_bytes()

        with mock.patch("collect_github_repos.clone_repository", side_effect=self.fake_clone), mock.patch(
            "collect_github_repos.discover_release_candidates", return_value=(first, second)
        ), mock.patch("collect_github_repos.fetch_required_refs"), mock.patch(
            "collect_github_repos.inspect_repository", return_value=RepoInspection("main", (first_ref, second_ref), (), False, False)
        ), mock.patch("collect_github_repos.resolve_ref", return_value=second_ref), mock.patch(
            "collect_github_repos.fetch_release_notes", return_value=notes
        ), mock.patch("collect_github_repos.run_git"):
            collected = collect_one(self.root, config, release_mode="future")

        snapshots = sorted(
            path for path in canonical.parent.iterdir() if path.name != ".promotion.lock"
        )
        self.assertEqual("collected-baseline", collected.state)
        self.assertEqual(1, len(collected.packet_ids))
        self.assertEqual(2, len(snapshots))
        self.assertEqual(canonical_manifest, (canonical / "snapshot.md").read_bytes())
        supplement = next(path for path in snapshots if path != canonical)
        self.assertEqual(notes.content, (supplement / "release-notes.md").read_bytes())
        index = collect_github_repos.load_version_index(
            collect_github_repos._version_index_path(self.root, config), config
        )
        self.assertEqual(1, len(index.versions))
        self.assertEqual(("v1.0.0", "v1.1.0"), index.versions[0].aliases)
        self.assertTrue(index.versions[0].release_notes_path.endswith("/release-notes.md"))

    def test_enabled_owner_company_split_collects_raw_and_tracking_namespaces(self):
        config = self.config(
            id="paypal-examples/example-checkout",
            company="paypal",
            url="https://github.com/paypal-examples/example-checkout",
            enabled=True,
        )
        ref = ResolvedRef(
            config.id, "branch", "main", "a" * 40, "main", (),
            "2026-07-16T00:00:00Z", None,
        )

        with mock.patch("collect_github_repos.clone_repository", side_effect=self.fake_clone), mock.patch(
            "collect_github_repos.fetch_required_refs"
        ), mock.patch(
            "collect_github_repos.inspect_repository", return_value=RepoInspection("main", (ref,), (), False, False)
        ), mock.patch("collect_github_repos.resolve_ref", return_value=ref), mock.patch(
            "collect_github_repos.run_git"
        ):
            result = collect_one(self.root, config, ("default-branch",))

        self.assertEqual("collected-baseline", result.state)
        self.assertEqual(1, len(result.packet_ids))
        self.assertTrue(
            any((self.root / "raw" / "github" / "paypal" / "example-checkout" / "snapshots").iterdir())
        )
        self.assertTrue(
            (self.root / "tracking" / "github" / "repos" / "paypal-examples" / "example-checkout" / "packets" / result.packet_ids[0]).is_dir()
        )

    def test_index_load_failure_still_records_one_terminal_event_for_explicit_ref(self):
        config = self.config()

        with mock.patch(
            "collect_github_repos.load_version_index",
            side_effect=PacketError("invalid version index"),
        ):
            result = collect_one(self.root, config, ("default-branch",))

        self.assertEqual("failed", result.state)
        selected = [event for event in result.events if event.get("selected")]
        terminal = [event for event in result.events if event.get("state") == "failed"]
        self.assertEqual(1, len(selected))
        self.assertEqual(1, len(terminal))
        self.assertIn("invalid version index", terminal[0]["error"])

    def test_packet_state_rejects_corrupted_history_without_appending(self):
        packet = self.packet()
        self.write_packet(packet)
        events_path = packet.directory / "state-events.jsonl"
        append = json.dumps({"packet_id": packet.packet_id, "state": "ingesting"}, sort_keys=True) + "\n"
        events_path.write_text(events_path.read_text(encoding="utf-8") + append, encoding="utf-8")
        before = events_path.read_bytes()

        with mock.patch.object(collect_github_repos, "PROJECT_ROOT", self.root):
            code = main(
                (
                    "packet-state",
                    "--repo",
                    "paypal/paypal-js",
                    "--packet",
                    packet.packet_id,
                    "--from",
                    "ingesting",
                    "--to",
                    "ingested",
                )
            )

        self.assertEqual(1, code)
        self.assertEqual(before, events_path.read_bytes())

    def test_packet_state_serializes_identical_concurrent_transitions(self):
        packet = self.packet()
        self.write_packet(packet)
        barrier = threading.Barrier(2)
        real_append = collect_github_repos.append_event

        def racing_append(path, event):
            barrier.wait(timeout=5)
            real_append(path, event)

        def transition():
            try:
                collect_github_repos._change_packet_state(
                    self.root, self.config(), packet.packet_id, "awaiting-review", "approved"
                )
            except Exception as error:
                return type(error).__name__
            return "ok"

        with mock.patch.object(collect_github_repos, "append_event", side_effect=racing_append):
            with ThreadPoolExecutor(max_workers=2) as executor:
                outcomes = tuple(executor.map(lambda _: transition(), range(2)))

        self.assertEqual(1, outcomes.count("ok"))
        self.assertEqual(2, len((packet.directory / "state-events.jsonl").read_text().splitlines()))

    def test_packet_state_rejects_symlink_escape_without_writing(self):
        packet = self.packet()
        outside = self.root / "outside-packet"
        escaped = replace(packet, directory=outside)
        self.write_packet(escaped)
        packet.directory.parent.mkdir(parents=True, exist_ok=True)
        packet.directory.symlink_to(outside, target_is_directory=True)
        events = outside / "state-events.jsonl"
        before = events.read_bytes()

        with self.assertRaises(Exception):
            collect_github_repos._change_packet_state(
                self.root, self.config(), packet.packet_id, "awaiting-review", "approved"
            )

        self.assertEqual(before, events.read_bytes())

    def test_status_rejects_foreign_packet_history_instead_of_projecting_it(self):
        packet = self.packet()
        self.write_packet(packet)
        events = packet.directory / "state-events.jsonl"
        events.write_text(
            events.read_text(encoding="utf-8")
            + json.dumps(
                {"from_state": "awaiting-review", "packet_id": "foreign", "state": "approved"},
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )

        with self.assertRaises(Exception):
            collect_github_repos.regenerate_status(self.root)

    def test_status_regeneration_writes_json_and_both_markdown_dashboards(self):
        with mock.patch.object(collect_github_repos, "PROJECT_ROOT", self.root):
            self.assertEqual(0, main(("status",)))

        tracking = self.root / "tracking" / "github"
        status = json.loads((tracking / "status.json").read_text(encoding="utf-8"))
        self.assertEqual(3, len(status["repositories"]))
        self.assertTrue((tracking / "collection-status.md").is_file())
        self.assertTrue((tracking / "ingest-status.md").is_file())

    def test_status_allows_repository_local_duplicate_packet_ids_with_distinct_states(self):
        paypal = self.packet("baseline-shared")
        stripe = replace(
            paypal,
            repo_id="stripe/stripe-ios",
            directory=(
                self.root
                / "tracking"
                / "github"
                / "repos"
                / "stripe"
                / "stripe-ios"
                / "packets"
                / paypal.packet_id
            ),
        )
        self.write_packet(paypal)
        self.write_packet(stripe)
        for packet, state in ((paypal, "approved"), (stripe, "rejected")):
            (packet.directory / "state-events.jsonl").write_text(
                json.dumps(
                    {"packet_id": packet.packet_id, "state": "awaiting-review"},
                    sort_keys=True,
                )
                + "\n"
                + json.dumps(
                    {
                        "from_state": "awaiting-review",
                        "packet_id": packet.packet_id,
                        "state": state,
                    },
                    sort_keys=True,
                )
                + "\n",
                encoding="utf-8",
            )

        status = collect_github_repos.regenerate_status(self.root)

        packet_states = {
            (row["repo_id"], row["packet_id"]): row["state"] for row in status["packets"]
        }
        self.assertEqual("approved", packet_states[(paypal.repo_id, paypal.packet_id)])
        self.assertEqual("rejected", packet_states[(stripe.repo_id, stripe.packet_id)])
        markdown = (self.root / "tracking" / "github" / "ingest-status.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("| paypal/paypal-js | baseline-shared | baseline |", markdown)
        self.assertIn("| stripe/stripe-ios | baseline-shared | baseline |", markdown)

    def packet(self, packet_id="baseline-1.0.0-aaaaaaa"):
        directory = self.root / "tracking" / "github" / "repos" / "paypal" / "paypal-js" / "packets" / packet_id
        return PacketRecord(
            packet_id,
            "paypal/paypal-js",
            "baseline",
            "",
            "raw/github/paypal/paypal-js/snapshots/v1",
            ("raw/github/paypal/paypal-js/snapshots/v1/snapshot.md",),
            (),
            "awaiting-review",
            directory,
        )

    def write_packet(self, packet):
        packet.directory.mkdir(parents=True)
        (packet.directory / "packet.json").write_text(
            json.dumps(
                {
                    "packet_id": packet.packet_id,
                    "repo_id": packet.repo_id,
                    "packet_type": packet.packet_type,
                    "from_snapshot": packet.from_snapshot,
                    "to_snapshot": packet.to_snapshot,
                    "required_reading": list(packet.required_reading),
                    "changed_files": list(packet.changed_files),
                    "initial_state": packet.initial_state,
                    "from": None,
                    "to": {},
                },
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )
        (packet.directory / "state-events.jsonl").write_text(
            json.dumps({"packet_id": packet.packet_id, "state": "awaiting-review"}, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    def candidate(self, version, prerelease=False):
        tag = "v" + version
        fill = str(sum(ord(character) for character in version) % 10)
        return ReleaseCandidate("", version, tag, fill * 40, fill * 40, prerelease)

    def entry(self, version, sha):
        return VersionEntry(
            "tag",
            "v" + version,
            version,
            sha,
            ("v" + version,),
            "raw/github/paypal/paypal-js/snapshots/" + version,
            "2026-07-16",
            "",
            "canonical",
            "",
            (),
        )

    def ref(self, candidate):
        return ResolvedRef(
            "paypal/paypal-js",
            "tag",
            candidate.tag,
            candidate.commit_sha,
            candidate.version,
            (candidate.tag,),
            "2026-07-16T00:00:00Z",
            None,
        )

    def fake_clone(self, config, destination):
        destination.mkdir(parents=True)

    def fake_owned_promotion(self, record):
        record.target_path.mkdir(parents=True)
        record.staging_path.rmdir()
        target_stat = record.target_path.stat()
        return SnapshotPromotionResult(
            record.target_path,
            True,
            SnapshotPromotionToken(
                record.target_path,
                target_stat.st_dev,
                target_stat.st_ino,
            ),
        )


if __name__ == "__main__":
    unittest.main()
