"""Tests for deterministic GitHub version indexes and ingest packets."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from github_git import ResolvedRef  # noqa: E402
from github_packets import (  # noqa: E402
    PacketError,
    VersionIndex,
    build_baseline_packet,
    build_comparison_packet,
    build_delta_packet,
    load_version_index,
    record_snapshot,
    save_version_index,
    select_prior,
)
from github_registry import RepoConfig  # noqa: E402
from github_releases import ReleaseNotesEvidence  # noqa: E402
from github_snapshot import SnapshotFile, SnapshotRecord, build_snapshot, promote_snapshot  # noqa: E402
from tests.github_test_support import commit_file, create_git_repo, tag  # noqa: E402


def git(repo, *args):
    return subprocess.run(
        ["git"] + list(args),
        cwd=str(repo),
        check=True,
        text=True,
        capture_output=True,
    ).stdout.strip()


class GitHubPacketTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.repo = create_git_repo(self.root)
        self.raw_root = self.root / "raw" / "github"
        self.staging_root = self.raw_root / ".staging"
        self.packet_root = self.root / "tracking" / "github" / "repos" / "acme" / "widgets" / "packets"
        self.config = RepoConfig(
            id="acme/widgets",
            company="acme",
            url="https://github.com/acme/widgets",
            enabled=True,
            repo_type="sdk",
            priority="tier1",
            track="releases-and-default-branch",
            version_strategy="monorepo-packages",
            key_paths=("CHANGELOG.md", "docs", "examples", "src"),
        )

    def tearDown(self):
        self.temporary.cleanup()

    def snapshot(self, sha, version="1.0.0", aliases=(), package="@scope/widgets", **overrides):
        ref_name = package + "@" + version if package else "v" + version
        ref = ResolvedRef(
            repo_id="acme/widgets",
            ref_kind="package-version" if package else "tag",
            ref_name=ref_name,
            sha=sha,
            version=version,
            aliases=aliases,
            upstream_commit_time="2026-07-15T00:00:00+00:00",
            release_published_at="2026-07-15T00:00:00+00:00",
        )
        values = {
            "repo_id": "acme/widgets",
            "ref": ref,
            "capture_kind": "canonical",
            "capture_revision": 0,
            "collection_date": "2026-07-15",
            "staging_path": self.root / "staging",
            "target_path": self.raw_root / "acme" / "widgets" / "snapshots" / (version + "-" + sha[:7]),
            "files": (SnapshotFile("CHANGELOG.md", "f" * 64, 1, "repository changelog"),),
            "repository_url": "https://github.com/acme/widgets",
            "company": "acme",
            "repo_type": "sdk",
            "release_notes_source_url": "https://api.github.test/releases/" + version,
            "release_notes_published_at": "2026-07-15T00:00:00Z",
            "release_notes_sha256": "e" * 64,
            "release_notes_size": 1,
        }
        values.update(overrides)
        return SnapshotRecord(**values)

    def empty_index(self):
        return VersionIndex("acme/widgets", ())

    def test_aliases_share_one_canonical_version_entry(self):
        first = record_snapshot(self.empty_index(), self.snapshot("a" * 40, aliases=("v1",)))
        second = record_snapshot(
            first, self.snapshot("a" * 40, aliases=("stable", "v1"))
        )

        self.assertEqual(1, len(second.versions))
        self.assertEqual(("stable", "v1"), second.versions[0].aliases)

    def test_package_namespace_prior_selection_uses_highest_compatible_version(self):
        index = record_snapshot(self.empty_index(), self.snapshot("a" * 40, "1.0.0"))
        index = record_snapshot(index, self.snapshot("b" * 40, "1.2.0"))
        index = record_snapshot(index, self.snapshot("c" * 40, "1.9.0", package="@other/widgets"))
        current = self.snapshot("d" * 40, "2.0.0").ref

        prior = select_prior(index, current)

        self.assertIsNotNone(prior)
        self.assertEqual("1.2.0", prior.version)
        self.assertEqual("@scope/widgets", prior.package)

    def test_package_alias_on_a_plain_tag_keeps_prior_selection_in_its_namespace(self):
        index = record_snapshot(self.empty_index(), self.snapshot("a" * 40, "1.0.0"))
        current = ResolvedRef(
            "acme/widgets",
            "tag",
            "v2.0.0",
            "b" * 40,
            "2.0.0",
            ("@scope/widgets@2.0.0", "v2.0.0"),
            "2026-07-16T00:00:00+00:00",
            None,
        )

        prior = select_prior(index, current)

        self.assertIsNotNone(prior)
        self.assertEqual("@scope/widgets", prior.package)
        self.assertEqual("1.0.0", prior.version)

    def test_multi_package_sha_retains_each_alias_namespace_for_prior_selection(self):
        first = self.snapshot(
            "a" * 40,
            "1.0.0",
            aliases=("@scope-a/widgets@1.0.0", "@scope-b/widgets@1.0.0"),
            package="@scope-a/widgets",
        )
        index = record_snapshot(self.empty_index(), first)
        current = self.snapshot("b" * 40, "2.0.0", package="@scope-b/widgets").ref

        prior = select_prior(index, current)

        self.assertIsNotNone(prior)
        self.assertEqual("a" * 40, prior.sha)

    def test_load_version_index_rejects_unknown_or_malformed_schema(self):
        path = self.version_index_path()
        valid = self.version_index_json()
        cases = {
            "unknown top-level key": {**valid, "unexpected": True},
            "missing versions": {"repo_id": "acme/widgets"},
            "boolean version list": {"repo_id": "acme/widgets", "versions": True},
            "unknown entry key": self.entry_with(valid, unexpected="value"),
            "missing entry key": self.entry_without(valid, "version"),
            "boolean scalar": self.entry_with(valid, capture_revision=True),
            "malformed sha": self.entry_with(valid, sha="a" * 39),
            "malformed ref": self.entry_with(valid, ref_kind="package-version", ref_name="bad tag"),
            "malformed branch ref": self.entry_with(
                valid, ref_kind="branch", ref_name="@", version="@", package=""
            ),
            "malformed version": self.entry_with(valid, version="not-a-version"),
            "duplicate aliases": self.entry_with(
                valid, aliases=["@scope/widgets@1.0.0", "@scope/widgets@1.0.0"]
            ),
            "unsorted aliases": self.entry_with(
                valid, aliases=["z", "@scope/widgets@1.0.0"]
            ),
            "malformed alias": self.entry_with(valid, aliases=["@"]),
            "duplicate changelog": self.entry_with(
                valid,
                changelog_paths=[
                    "raw/github/acme/widgets/snapshots/v1/files/CHANGELOG.md",
                    "raw/github/acme/widgets/snapshots/v1/files/CHANGELOG.md",
                ],
            ),
            "conflicting sha entries": {
                "repo_id": "acme/widgets",
                "versions": [valid["versions"][0], valid["versions"][0]],
            },
            "repo mismatch": {**valid, "repo_id": "other/widgets"},
        }

        for label, document in cases.items():
            with self.subTest(label=label):
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(json.dumps(document), encoding="utf-8")
                with self.assertRaises(PacketError):
                    load_version_index(path, self.config)

        path.write_text(
            '{"repo_id":"acme/widgets","repo_id":"other/widgets","versions":[]}',
            encoding="utf-8",
        )
        with self.assertRaises(PacketError):
            load_version_index(path, self.config)

    def test_load_version_index_rejects_evidence_paths_outside_or_through_symlink(self):
        path = self.version_index_path()
        valid = self.version_index_json()
        unsafe_paths = (
            "/tmp/outside",
            "../raw/github/acme/widgets/snapshots/v1",
            "raw/github/acme/other/snapshots/v1",
        )
        for field in ("snapshot_path", "release_notes_path", "changelog_paths"):
            for unsafe_path in unsafe_paths:
                with self.subTest(field=field, path=unsafe_path):
                    updates = {field: unsafe_path}
                    if field == "changelog_paths":
                        updates[field] = [unsafe_path]
                    document = self.entry_with(valid, **updates)
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text(json.dumps(document), encoding="utf-8")
                    with self.assertRaises(PacketError):
                        load_version_index(path, self.config)

        evidence_root = self.root / "raw" / "github" / "acme" / "widgets"
        evidence_root.mkdir(parents=True)
        outside = self.root / "outside"
        outside.mkdir()
        (evidence_root / "snapshots").symlink_to(outside, target_is_directory=True)
        document = self.entry_with(
            valid, snapshot_path="raw/github/acme/widgets/snapshots/v1"
        )
        path.write_text(json.dumps(document), encoding="utf-8")
        with self.assertRaises(PacketError):
            load_version_index(path, self.config)

    def test_load_version_index_rejects_duplicate_immutable_ref_identity(self):
        document = self.version_index_json()
        duplicate = dict(
            document["versions"][0],
            sha="b" * 40,
            snapshot_path="raw/github/acme/widgets/snapshots/v2",
            release_notes_path="raw/github/acme/widgets/snapshots/v2/release-notes.md",
            changelog_paths=[
                "raw/github/acme/widgets/snapshots/v2/files/CHANGELOG.md"
            ],
        )
        document["versions"].append(duplicate)
        path = self.version_index_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(document), encoding="utf-8")

        with self.assertRaisesRegex(PacketError, "conflicting reference entries"):
            load_version_index(path, self.config)

    def test_version_index_capture_order_is_complete_unique_and_legacy_compatible(self):
        path = self.version_index_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        legacy = self.version_index_json()
        path.write_text(json.dumps(legacy), encoding="utf-8")

        loaded = load_version_index(path, self.config)

        self.assertEqual(("a" * 40,), loaded.capture_order)
        save_version_index(path, loaded)
        self.assertEqual(loaded, load_version_index(path, self.config))
        for invalid in ([], ["a" * 40, "a" * 40], ["b" * 40]):
            with self.subTest(capture_order=invalid):
                current = dict(legacy, capture_order=invalid)
                path.write_text(json.dumps(current), encoding="utf-8")
                with self.assertRaisesRegex(PacketError, "capture_order"):
                    load_version_index(path, self.config)

    def test_packet_root_must_be_tracking_github_without_raw_or_symlink_escape(self):
        raw_packet_root = self.root / "raw" / "github" / "packets"
        with self.assertRaises(PacketError):
            build_baseline_packet(self.config, self.snapshot("a" * 40), raw_packet_root)
        self.assertFalse(raw_packet_root.exists())

        outside = self.root / "outside"
        outside.mkdir()
        symlink_root = self.root / "tracking" / "github"
        symlink_root.parent.mkdir(parents=True)
        symlink_root.symlink_to(outside, target_is_directory=True)
        escaped_packet_root = symlink_root / "repos" / "acme" / "widgets" / "packets"
        with self.assertRaises(PacketError):
            build_baseline_packet(self.config, self.snapshot("b" * 40), escaped_packet_root)
        self.assertFalse(any(outside.iterdir()))

    def test_packet_root_must_match_configured_repository_namespace(self):
        invalid_roots = (
            self.root / "tracking" / "github" / "repos" / "other-company" / "other-repo" / "packets",
            self.root / "tracking" / "github" / "repos" / "acme" / "other-repo" / "packets",
            self.root / "tracking" / "github" / "acme" / "widgets" / "packets",
            self.root / "tracking" / "github" / "repos" / "acme" / "widgets" / "repos" / "acme" / "widgets" / "packets",
            self.root / "tracking" / "github" / "repos" / "acme" / "widgets" / "tracking" / "github" / "repos" / "acme" / "widgets" / "packets",
        )
        invalid_shas = ("a", "b", "c", "d", "e")
        for sha_prefix, packet_root in zip(invalid_shas, invalid_roots):
            with self.subTest(packet_root=packet_root):
                with self.assertRaises(PacketError):
                    build_baseline_packet(
                        self.config,
                        self.snapshot(sha_prefix * 40),
                        packet_root,
                    )

        valid_roots = (
            self.root / "tracking" / "github" / "repos" / "acme" / "widgets",
            self.root / "tracking" / "github" / "repos" / "acme" / "widgets" / "packets",
            self.root / "tracking" / "github" / "repos" / "acme" / "widgets" / "packets" / "review",
        )
        valid_shas = ("f", "0", "1")
        for sha_prefix, packet_root in zip(valid_shas, valid_roots):
            with self.subTest(packet_root=packet_root):
                packet = build_baseline_packet(
                    self.config,
                    self.snapshot(sha_prefix * 40),
                    packet_root,
                )
                self.assertTrue(packet.directory.is_dir())
                self.assertTrue(
                    all(path.startswith("raw/github/acme/widgets/") for path in packet.required_reading)
                )

    def test_packet_evidence_uses_raw_company_and_repo_name_not_tracking_owner(self):
        config = RepoConfig(
            id="paypal-examples/example-checkout",
            company="paypal",
            url="https://github.com/paypal-examples/example-checkout",
            enabled=True,
            repo_type="sample-app",
            priority="tier1",
            track="default-branch",
            version_strategy="commit",
        )
        ref = ResolvedRef(
            config.id, "branch", "main", "a" * 40, "main", (),
            "2026-07-16T00:00:00Z", None,
        )
        snapshot = self.snapshot(
            "a" * 40,
            package="",
            repo_id=config.id,
            ref=ref,
            company=config.company,
            repository_url=config.url,
            target_path=self.root / "raw" / "github" / "paypal" / "example-checkout" / "snapshots" / "main-aaaaaaa",
            release_notes_source_url=None,
            release_notes_published_at=None,
            release_notes_sha256=None,
            release_notes_size=None,
        )
        packet_root = (
            self.root / "tracking" / "github" / "repos" / "paypal-examples"
            / "example-checkout" / "packets"
        )

        packet = build_baseline_packet(config, snapshot, packet_root)

        self.assertTrue(packet.directory.is_dir())
        self.assertTrue(
            all(path.startswith("raw/github/paypal/example-checkout/") for path in packet.required_reading)
        )

    def test_packet_retry_reuses_valid_artifacts_without_resetting_state_events(self):
        record = self.snapshot("a" * 40)
        packet = build_baseline_packet(self.config, record, self.packet_root)
        events = packet.directory / "state-events.jsonl"
        approved = json.dumps({"packet_id": packet.packet_id, "state": "approved"}) + "\n"
        events.write_text(events.read_text(encoding="utf-8") + approved, encoding="utf-8")

        retried = build_baseline_packet(self.config, record, self.packet_root)

        self.assertEqual(packet, retried)
        self.assertTrue(events.read_text(encoding="utf-8").endswith(approved))

    def test_packet_write_failure_cleans_temporary_sibling_without_publishing_packet(self):
        record = self.snapshot("a" * 40)

        with mock.patch("github_packets._write_text_atomic", side_effect=OSError("injected")):
            with self.assertRaises(OSError):
                build_baseline_packet(self.config, record, self.packet_root)

        self.assertFalse((self.packet_root / "baseline-1.0.0-aaaaaaa").exists())
        if self.packet_root.exists():
            self.assertEqual((".packet.lock",), tuple(sorted(path.name for path in self.packet_root.iterdir())))

    def test_conflicting_existing_packet_fails_without_overwrite(self):
        record = self.snapshot("a" * 40)
        packet = build_baseline_packet(self.config, record, self.packet_root)
        packet_json = packet.directory / "packet.json"
        packet_json.write_text("{}\n", encoding="utf-8")

        with self.assertRaises(PacketError):
            build_baseline_packet(self.config, record, self.packet_root)

        self.assertEqual("{}\n", packet_json.read_text(encoding="utf-8"))

    def test_branch_prior_selection_uses_previous_capture_on_the_same_branch(self):
        first = self.snapshot("a" * 40, package="")
        first = SnapshotRecord(
            **dict(
                vars(first),
                ref=ResolvedRef(
                    "acme/widgets", "branch", "main", "a" * 40, "main", (), "2026-07-14T00:00:00+00:00", None
                ),
                collection_date="2026-07-14",
            )
        )
        index = record_snapshot(self.empty_index(), first)
        current = ResolvedRef(
            "acme/widgets", "branch", "main", "b" * 40, "main", (), "2026-07-15T00:00:00+00:00", None
        )

        prior = select_prior(index, current)

        self.assertIsNotNone(prior)
        self.assertEqual("a" * 40, prior.sha)

    def test_branch_prior_selection_uses_immediately_preceding_same_day_capture(self):
        def branch_snapshot(sha):
            record = self.snapshot(sha, package="")
            return SnapshotRecord(
                **dict(
                    vars(record),
                    ref=ResolvedRef(
                        "acme/widgets",
                        "branch",
                        "main",
                        sha,
                        "main",
                        (),
                        "2026-07-15T00:00:00+00:00",
                        None,
                    ),
                    collection_date="2026-07-15",
                    target_path=(
                        self.raw_root
                        / "acme/widgets/snapshots"
                        / ("2026-07-15-main-" + sha[:7])
                    ),
                )
            )

        index = record_snapshot(self.empty_index(), branch_snapshot("f" * 40))
        index = record_snapshot(index, branch_snapshot("a" * 40))
        current_record = branch_snapshot("b" * 40)

        prior = select_prior(index, current_record.ref)
        with mock.patch("github_packets._git_delta", return_value=((), "")):
            packet = build_delta_packet(
                self.config, prior, current_record, self.repo, self.packet_root
            )
        contract = json.loads(
            (packet.directory / "packet.json").read_text(encoding="utf-8")
        )

        self.assertIsNotNone(prior)
        self.assertEqual("a" * 40, prior.sha)
        self.assertEqual(prior.snapshot_path, packet.from_snapshot)
        self.assertEqual("a" * 40, contract["from"]["sha"])
        self.assertEqual("b" * 40, contract["to"]["sha"])

    def test_supplement_updates_evidence_without_creating_another_version(self):
        canonical = self.snapshot("a" * 40, aliases=("v1.0.0",))
        index = record_snapshot(self.empty_index(), canonical)
        supplement = self.snapshot(
            "a" * 40,
            aliases=("stable",),
            capture_kind="supplement",
            capture_revision=1,
            target_path=self.raw_root / "acme" / "widgets" / "snapshots" / "1.0.0-aaaaaaa-r1",
            files=(
                SnapshotFile("CHANGELOG.md", "f" * 64, 1, "repository changelog"),
                SnapshotFile("docs/CHANGELOG-v1.md", "d" * 64, 1, "repository changelog"),
            ),
            release_notes_source_url=None,
            release_notes_published_at=None,
            release_notes_sha256=None,
            release_notes_size=None,
        )

        updated = record_snapshot(index, supplement)

        self.assertEqual(1, len(updated.versions))
        self.assertEqual(("stable", "v1.0.0"), updated.versions[0].aliases)
        self.assertEqual(3, len(updated.versions[0].changelog_paths))
        path = self.version_index_path()
        save_version_index(path, updated)
        self.assertEqual(updated, load_version_index(path, self.config))

    def test_version_index_json_round_trips_with_stable_order_and_newline(self):
        index = record_snapshot(self.empty_index(), self.snapshot("b" * 40, "1.2.0"))
        index = record_snapshot(index, self.snapshot("a" * 40, "1.0.0"))
        path = self.root / "tracking" / "github" / "repos" / "acme" / "widgets" / "version-index.json"

        save_version_index(path, index)

        text = path.read_text(encoding="utf-8")
        self.assertTrue(text.endswith("\n"))
        self.assertEqual(["capture_order", "repo_id", "versions"], list(json.loads(text)))
        self.assertEqual(index, load_version_index(path, self.config))

    def test_delta_packet_records_add_modify_rename_and_deletion_with_raw_evidence(self):
        prior_record, current_record = self.release_snapshots()
        index = record_snapshot(self.empty_index(), prior_record)
        prior = select_prior(index, current_record.ref)

        packet = build_delta_packet(self.config, prior, current_record, self.repo, self.packet_root)

        self.assertIn("D\tdocs/removed.md", packet.changed_files)
        self.assertTrue(any(line.startswith("R") for line in packet.changed_files))
        self.assertIn("A\texamples/new-demo.js", packet.changed_files)
        self.assertIn("M\tCHANGELOG.md", packet.changed_files)
        self.assertEqual("awaiting-review", packet.initial_state)
        self.assertTrue((packet.directory / "packet.json").is_file())
        self.assertTrue((packet.directory / "ingest-packet.md").is_file())
        self.assertTrue((packet.directory / "changed-files.txt").is_file())
        self.assertTrue((packet.directory / "source-diff.patch").is_file())
        self.assertFalse(any(path.suffix == ".patch" for path in self.raw_root.rglob("*")))
        self.assertIn("raw/github/acme/widgets/snapshots", packet.required_reading[0])
        self.assertTrue(any(path.endswith("release-notes.md") for path in packet.required_reading))
        self.assertTrue(any(path.endswith("files/CHANGELOG.md") for path in packet.required_reading))
        self.assertTrue(any(path.endswith("files/examples/new-demo.js") for path in packet.required_reading))
        packet_json = json.loads((packet.directory / "packet.json").read_text(encoding="utf-8"))
        self.assertEqual("awaiting-review", packet_json["initial_state"])

    def test_baseline_and_comparison_packets_stay_in_awaiting_review(self):
        prior_record, current_record = self.release_snapshots()
        index = record_snapshot(self.empty_index(), prior_record)
        prior = select_prior(index, current_record.ref)

        baseline = build_baseline_packet(self.config, prior_record, self.packet_root)
        current_entry = next(
            item
            for item in record_snapshot(index, current_record).versions
            if item.sha == current_record.ref.sha
        )
        comparison = build_comparison_packet(
            self.config, prior, current_entry, self.repo, self.packet_root
        )

        self.assertEqual("awaiting-review", baseline.initial_state)
        self.assertEqual("awaiting-review", comparison.initial_state)
        self.assertTrue((baseline.directory / "source-diff.patch").is_file())
        self.assertTrue((comparison.directory / "source-diff.patch").is_file())

    def release_snapshots(self):
        first_sha = commit_file(self.repo, "README.md", "first\n", "initial readme")
        commit_file(self.repo, "CHANGELOG.md", "# 1.0.0\n", "add changelog")
        commit_file(self.repo, "docs/removed.md", "remove later\n", "add removed document")
        commit_file(self.repo, "docs/renamed.md", "rename without rewriting\n", "add renamed document")
        commit_file(self.repo, "src/public.js", "export const value = 1;\n", "add source")
        tag(self.repo, "@scope/widgets@1.0.0")
        prior_sha = git(self.repo, "rev-parse", "HEAD")
        git(self.repo, "checkout", prior_sha)
        prior_record = self.build_promoted_snapshot(prior_sha, "1.0.0", "# Notes 1.0.0\n")

        git(self.repo, "checkout", "main")
        (self.repo / "docs" / "removed.md").unlink()
        git(self.repo, "rm", "docs/removed.md")
        git(self.repo, "mv", "docs/renamed.md", "docs/new-name.md")
        (self.repo / "src" / "public.js").write_text("export const value = 2;\n", encoding="utf-8")
        git(self.repo, "add", "src/public.js")
        commit_file(self.repo, "CHANGELOG.md", "# 1.1.0\n", "update changelog")
        commit_file(self.repo, "examples/new-demo.js", "newName();\n", "add example")
        current_sha = git(self.repo, "rev-parse", "HEAD")
        tag(self.repo, "@scope/widgets@1.1.0")
        current_record = self.build_promoted_snapshot(current_sha, "1.1.0", "# Notes 1.1.0\n")
        return prior_record, current_record

    def version_index_path(self):
        return self.root / "tracking" / "github" / "repos" / "acme" / "widgets" / "version-index.json"

    def version_index_json(self):
        return {
            "repo_id": "acme/widgets",
            "versions": [
                {
                    "aliases": ["@scope/widgets@1.0.0"],
                    "capture_kind": "canonical",
                    "changelog_paths": [
                        "raw/github/acme/widgets/snapshots/v1/files/CHANGELOG.md"
                    ],
                    "collection_date": "2026-07-15",
                    "package": "@scope/widgets",
                    "ref_kind": "package-version",
                    "ref_name": "@scope/widgets@1.0.0",
                    "release_notes_path": "raw/github/acme/widgets/snapshots/v1/release-notes.md",
                    "sha": "a" * 40,
                    "snapshot_path": "raw/github/acme/widgets/snapshots/v1",
                    "version": "1.0.0",
                }
            ],
        }

    def entry_with(self, document, **updates):
        result = dict(document)
        result["versions"] = [dict(document["versions"][0], **updates)]
        return result

    def entry_without(self, document, field):
        entry = dict(document["versions"][0])
        del entry[field]
        return {"repo_id": document["repo_id"], "versions": [entry]}

    def build_promoted_snapshot(self, sha, version, release_notes):
        ref = ResolvedRef(
            "acme/widgets",
            "package-version",
            "@scope/widgets@" + version,
            sha,
            version,
            ("@scope/widgets@" + version,),
            "2026-07-15T00:00:00+00:00",
            "2026-07-15T00:00:00Z",
        )
        record = build_snapshot(
            self.config,
            ref,
            self.repo,
            self.raw_root,
            self.staging_root,
            "2026-07-15",
            release_notes=ReleaseNotesEvidence(
                "https://api.github.test/releases/" + version,
                "2026-07-15T00:00:00Z",
                release_notes.encode("utf-8"),
            ),
        )
        self.assertEqual(record.target_path, promote_snapshot(record))
        return record


if __name__ == "__main__":
    unittest.main()
