import hashlib
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from github_git import ResolvedRef  # noqa: E402
from github_packets import PacketRecord, build_baseline_packet  # noqa: E402
from github_registry import load_registry  # noqa: E402
from github_reporting import (  # noqa: E402
    packet_state_key,
    render_collection_status,
    render_ingest_status,
)
import github_validation  # noqa: E402
from github_validation import inspect_github, validate_github  # noqa: E402
from github_snapshot import SnapshotFile, SnapshotRecord  # noqa: E402


class GitHubValidationTests(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def make_valid_tree(self, packet_state="awaiting-review", index_version="10.1.5"):
        root = self.root
        registry_path = root / "tracking" / "github" / "repo-registry.toml"
        registry_path.parent.mkdir(parents=True)
        registry_path.write_text(
            "[[repos]]\n"
            'id = "paypal/paypal-js"\n'
            'company = "paypal"\n'
            'url = "https://github.com/paypal/paypal-js"\n'
            "enabled = true\n"
            'repo_type = "web-sdk"\n'
            'priority = "tier1"\n'
            'track = "releases-and-default-branch"\n'
            'version_strategy = "monorepo-packages"\n'
            "[[repos.version_tracks]]\n"
            'selector = "package:@paypal/paypal-js@10"\n'
            'backfill = "all-stable"\n'
            'future = "all-stable"\n'
            "include_prerelease = false\n",
            encoding="utf-8",
        )
        sha = "a" * 40
        snapshot = self.write_snapshot(index_version, sha, "2026-07-15")
        self.write_version_index((self.version_entry(index_version, sha, snapshot),))
        packet = self.write_packet(index_version, sha, snapshot, packet_state)
        events = self.write_collection_events(index_version, sha, packet.packet_id)
        self.write_source((snapshot,))
        self.write_dashboards(events, (packet,), {packet.packet_id: packet_state})
        return root

    def write_snapshot(
        self,
        version,
        sha,
        collection_date,
        capture_kind="canonical",
        capture_revision=0,
        suffix="",
    ):
        snapshot_id = (
            collection_date
            + "-"
            + version.replace(".", "-")
            + "-"
            + sha[:7]
            + suffix
        )
        relative = Path("raw/github/paypal/paypal-js/snapshots") / snapshot_id
        directory = self.root / relative
        files = {
            "README.md": b"PayPal JS\n",
            "CHANGELOG.md": ("# " + version + "\n").encode("utf-8"),
        }
        for name, content in files.items():
            path = directory / "files" / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
        release_notes = ("Release " + version + "\n").encode("utf-8")
        (directory / "release-notes.md").write_bytes(release_notes)
        metadata = {
            "format_version": 1,
            "repository": {
                "url": "https://github.com/paypal/paypal-js",
                "id": "paypal/paypal-js",
                "company": "paypal",
                "type": "web-sdk",
            },
            "ref": {
                "kind": "package-version",
                "name": "@paypal/paypal-js@" + version,
                "sha": sha,
                "version": version,
                "aliases": ["paypal-js@" + version],
                "upstream_commit_time": collection_date + "T12:00:00Z",
                "release_published_at": collection_date + "T13:00:00Z",
            },
            "capture_kind": capture_kind,
            "capture_revision": capture_revision,
            "collection_date": collection_date,
            "prior_snapshot": None,
            "files": [
                {
                    "path": name,
                    "sha256": hashlib.sha256(content).hexdigest(),
                    "size": len(content),
                    "purpose": "changelog" if name == "CHANGELOG.md" else "readme",
                }
                for name, content in sorted(files.items())
            ],
            "excluded": [],
            "release_notes": {
                "path": "release-notes.md",
                "source_url": "https://github.com/paypal/paypal-js/releases/tag/" + version,
                "published_at": collection_date + "T13:00:00Z",
                "sha256": hashlib.sha256(release_notes).hexdigest(),
                "size": len(release_notes),
            },
        }
        self.write_manifest(directory, metadata)
        return relative

    def write_manifest(self, directory, metadata):
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "snapshot.md").write_text(
            "# GitHub snapshot\n\n"
            "<!-- github-snapshot-metadata-v1 -->\n"
            "```json\n"
            + json.dumps(metadata, indent=2, sort_keys=True)
            + "\n```\n",
            encoding="utf-8",
        )

    def read_manifest(self, snapshot):
        path = self.root / snapshot / "snapshot.md"
        text = path.read_text(encoding="utf-8")
        start = text.index("```json\n") + len("```json\n")
        end = text.index("\n```", start)
        return path, json.loads(text[start:end])

    def version_entry(self, version, sha, snapshot):
        snapshot_path = snapshot.as_posix()
        return {
            "aliases": ["paypal-js@" + version],
            "capture_kind": "canonical",
            "changelog_paths": [snapshot_path + "/files/CHANGELOG.md"],
            "collection_date": snapshot.parts[-1][:10],
            "package": "@paypal/paypal-js",
            "ref_kind": "package-version",
            "ref_name": "@paypal/paypal-js@" + version,
            "release_notes_path": snapshot_path + "/release-notes.md",
            "sha": sha,
            "snapshot_path": snapshot_path,
            "version": version,
        }

    def write_version_index(self, entries):
        path = (
            self.root
            / "tracking/github/repos/paypal/paypal-js/version-index.json"
        )
        path.parent.mkdir(parents=True, exist_ok=True)
        ordered = sorted(
            entries,
            key=lambda item: (
                item["ref_kind"],
                item["package"],
                item["version"],
                item["ref_name"],
                item["sha"],
            ),
        )
        path.write_text(
            json.dumps(
                {"repo_id": "paypal/paypal-js", "versions": ordered},
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )

    def read_version_entries(self):
        path = self.root / "tracking/github/repos/paypal/paypal-js/version-index.json"
        return path, json.loads(path.read_text(encoding="utf-8"))["versions"]

    def set_version_track(self, selector, include_prerelease):
        path = self.root / "tracking/github/repo-registry.toml"
        text = path.read_text(encoding="utf-8")
        text = text.replace(
            'selector = "package:@paypal/paypal-js@10"',
            'selector = "' + selector + '"',
        )
        text = text.replace(
            "include_prerelease = false",
            "include_prerelease = " + ("true" if include_prerelease else "false"),
        )
        path.write_text(text, encoding="utf-8")

    def write_packet(self, version, sha, snapshot, state):
        snapshot_path = snapshot.as_posix()
        snapshot_directory = self.root / snapshot
        manifest_path, metadata = self.read_manifest(snapshot)
        del manifest_path
        release_notes = metadata["release_notes"]
        snapshot_stat = snapshot_directory.stat()
        record = SnapshotRecord(
            repo_id="paypal/paypal-js",
            ref=ResolvedRef(
                repo_id="paypal/paypal-js",
                ref_kind=metadata["ref"]["kind"],
                ref_name=metadata["ref"]["name"],
                sha=sha,
                version=version,
                aliases=tuple(metadata["ref"]["aliases"]),
                upstream_commit_time=metadata["ref"]["upstream_commit_time"],
                release_published_at=metadata["ref"]["release_published_at"],
            ),
            capture_kind=metadata["capture_kind"],
            capture_revision=metadata["capture_revision"],
            collection_date=metadata["collection_date"],
            staging_path=snapshot_directory,
            target_path=snapshot_directory,
            files=tuple(
                SnapshotFile(
                    path=item["path"],
                    sha256=item["sha256"],
                    size=item["size"],
                    purpose=item["purpose"],
                )
                for item in metadata["files"]
            ),
            repository_url=metadata["repository"]["url"],
            company=metadata["repository"]["company"],
            repo_type=metadata["repository"]["type"],
            release_notes_source_url=release_notes["source_url"],
            release_notes_published_at=release_notes["published_at"],
            release_notes_sha256=release_notes["sha256"],
            release_notes_size=release_notes["size"],
            staging_device=snapshot_stat.st_dev,
            staging_inode=snapshot_stat.st_ino,
        )
        config = load_registry(
            self.root / "tracking/github/repo-registry.toml"
        )[0]
        packet = build_baseline_packet(
            config,
            record,
            self.root / "tracking/github/repos/paypal/paypal-js/packets",
        )
        history = [{"packet_id": packet.packet_id, "state": "awaiting-review"}]
        transitions = {
            "approved": (("awaiting-review", "approved"),),
            "ingesting": (("awaiting-review", "approved"), ("approved", "ingesting")),
            "ingested": (
                ("awaiting-review", "approved"),
                ("approved", "ingesting"),
                ("ingesting", "ingested"),
            ),
            "rejected": (("awaiting-review", "rejected"),),
        }
        for from_state, to_state in transitions.get(state, ()):
            history.append(
                {
                    "from_state": from_state,
                    "packet_id": packet.packet_id,
                    "state": to_state,
                }
            )
        (packet.directory / "state-events.jsonl").write_text(
            "".join(json.dumps(event, sort_keys=True) + "\n" for event in history),
            encoding="utf-8",
        )
        return packet

    def write_collection_events(self, version, sha, packet_id):
        selector = "tag:@paypal/paypal-js@" + version
        events = (
            {
                "dry_run": False,
                "repo_id": "paypal/paypal-js",
                "selected": True,
                "selector": selector,
                "state": "selected",
            },
            {
                "dry_run": False,
                "packet_id": packet_id,
                "ref_name": "@paypal/paypal-js@" + version,
                "repo_id": "paypal/paypal-js",
                "selector": selector,
                "sha": sha,
                "state": "collected-baseline",
                "version": version,
            },
        )
        path = self.root / "tracking/github/runs/test.jsonl"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            "".join(json.dumps(event, sort_keys=True) + "\n" for event in events),
            encoding="utf-8",
        )
        return events

    def write_source(self, snapshots):
        source = (
            self.root
            / "wiki/sources/paypal/github/source-github-paypal-js.md"
        )
        source.parent.mkdir(parents=True, exist_ok=True)
        snapshots = tuple(
            snapshot.relative_to(self.root) if snapshot.is_absolute() else snapshot
            for snapshot in snapshots
        )
        raw_files = "".join(
            '  - "' + snapshot.relative_to("raw").as_posix() + '/snapshot.md"\n'
            for snapshot in snapshots
        )
        latest = snapshots[0]
        source.write_text(
            "---\n"
            'title: "PayPal JS"\n'
            "type: source\n"
            "date_ingested: 2026-07-15\n"
            "original_format: github-repo\n"
            "raw_files:\n"
            + raw_files
            + "tags: [paypal, github]\n"
            "---\n\n"
            "## Release History\n\n"
            "| Version | Snapshot | Changelog | Release notes |\n"
            "| --- | --- | --- | --- |\n"
            "| 10.1.5 | [["
            + latest.as_posix()
            + "/snapshot|snapshot]] | [["
            + latest.as_posix()
            + "/files/CHANGELOG|changelog]] | [["
            + latest.as_posix()
            + "/release-notes|release notes]] |\n\n"
            "## Raw Sources\n\n"
            + "".join(
                "- [[" + snapshot.as_posix() + "/snapshot|snapshot]]\n"
                for snapshot in snapshots
            ),
            encoding="utf-8",
        )
        return source

    def write_dashboards(self, events, packets, states):
        tracking = self.root / "tracking/github"
        registry = load_registry(tracking / "repo-registry.toml")
        index_path, versions = self.read_version_entries()
        del index_path
        latest_event = dict(events[-1])
        status = {
            "packets": [
                {
                    "packet_id": packet.packet_id,
                    "packet_type": packet.packet_type,
                    "repo_id": packet.repo_id,
                    "state": states[packet.packet_id],
                }
                for packet in packets
            ],
            "repositories": [
                {
                    "company": "paypal",
                    "enabled": True,
                    "latest_event": latest_event,
                    "priority": "tier1",
                    "repo_id": "paypal/paypal-js",
                    "track": "releases-and-default-branch",
                    "versions": [entry["version"] for entry in versions],
                }
            ],
        }
        (tracking / "status.json").write_text(
            json.dumps(status, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        (tracking / "collection-status.md").write_text(
            render_collection_status(registry, events), encoding="utf-8"
        )
        keyed_states = {
            packet_state_key(packet.repo_id, packet.packet_id): states[packet.packet_id]
            for packet in packets
        }
        (tracking / "ingest-status.md").write_text(
            render_ingest_status(packets, keyed_states), encoding="utf-8"
        )

    def test_valid_collection_has_no_errors(self):
        report = inspect_github(self.make_valid_tree())

        self.assertEqual(1, len(report.snapshot_paths))
        self.assertEqual(1, len(report.release_evidence_records))
        self.assertEqual([], validate_github(report))

    def test_pending_packet_is_informational_not_error(self):
        report = inspect_github(self.make_valid_tree(packet_state="awaiting-review"))

        self.assertEqual(1, len(report.pending_packets))
        self.assertEqual([], validate_github(report))

    def test_producer_packet_rejects_id_that_packet_state_cannot_transition(self):
        self.make_valid_tree()
        packet_directory = next(
            path
            for path in self.root.glob("tracking/github/repos/*/*/packets/*")
            if path.is_dir()
        )
        contract_path = packet_directory / "packet.json"
        contract = json.loads(contract_path.read_text(encoding="utf-8"))
        original_packet_id = contract["packet_id"]
        invalid_packet_id = "invalid packet id"
        invalid_directory = packet_directory.with_name(invalid_packet_id)
        packet_directory.rename(invalid_directory)
        contract["packet_id"] = invalid_packet_id
        (invalid_directory / "packet.json").write_text(
            json.dumps(contract, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        markdown_path = invalid_directory / "ingest-packet.md"
        markdown_path.write_text(
            markdown_path.read_text(encoding="utf-8").replace(
                original_packet_id, invalid_packet_id
            ),
            encoding="utf-8",
        )

        history_path = invalid_directory / "state-events.jsonl"
        history = [
            dict(json.loads(line), packet_id=invalid_packet_id)
            for line in history_path.read_text(encoding="utf-8").splitlines()
        ]
        history_path.write_text(
            "".join(json.dumps(event, sort_keys=True) + "\n" for event in history),
            encoding="utf-8",
        )
        events_path = self.root / "tracking/github/runs/test.jsonl"
        events = [
            dict(event, packet_id=invalid_packet_id)
            if event.get("packet_id") == original_packet_id
            else event
            for event in (
                json.loads(line) for line in events_path.read_text(encoding="utf-8").splitlines()
            )
        ]
        events_path.write_text(
            "".join(json.dumps(event, sort_keys=True) + "\n" for event in events),
            encoding="utf-8",
        )
        packet = PacketRecord(
            packet_id=invalid_packet_id,
            repo_id=contract["repo_id"],
            packet_type=contract["packet_type"],
            from_snapshot=contract["from_snapshot"],
            to_snapshot=contract["to_snapshot"],
            required_reading=tuple(contract["required_reading"]),
            changed_files=tuple(contract["changed_files"]),
            initial_state=contract["initial_state"],
            directory=invalid_directory,
        )
        self.write_dashboards(events, (packet,), {invalid_packet_id: "awaiting-review"})

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("packet ID is invalid" in error for error in errors), errors)

    def test_validator_packet_id_contract_rejects_directory_navigation_names(self):
        self.assertFalse(github_validation.is_valid_packet_id("."))
        self.assertFalse(github_validation.is_valid_packet_id(".."))

    def test_bad_snapshot_hash_is_rejected(self):
        self.make_valid_tree()
        changelog = next(self.root.glob("raw/github/*/*/snapshots/*/files/CHANGELOG.md"))
        changelog.write_text("tampered\n", encoding="utf-8")

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("hash mismatch" in error for error in errors), errors)

    def test_manifest_and_copied_files_must_agree(self):
        self.make_valid_tree()
        snapshot = next(self.root.glob("raw/github/*/*/snapshots/*"))
        (snapshot / "files/unlisted.md").write_text("unlisted\n", encoding="utf-8")

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("copied file is not listed" in error for error in errors), errors)

    def test_two_canonical_snapshots_for_one_sha_are_rejected(self):
        self.make_valid_tree()
        self.write_snapshot("10.1.5", "a" * 40, "2026-07-16", suffix="-duplicate")

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("more than one canonical snapshot" in error for error in errors), errors)

    def test_supplement_for_existing_canonical_sha_is_valid(self):
        self.make_valid_tree()
        supplement = self.write_snapshot(
            "10.1.5",
            "a" * 40,
            "2026-07-16",
            capture_kind="supplement",
            capture_revision=1,
            suffix="-r1",
        )
        index_path, entries = self.read_version_entries()
        del index_path
        entries[0]["release_notes_path"] = supplement.as_posix() + "/release-notes.md"
        entries[0]["changelog_paths"] = sorted(
            entries[0]["changelog_paths"]
            + [supplement.as_posix() + "/files/CHANGELOG.md"]
        )
        self.write_version_index(tuple(entries))

        report = inspect_github(self.root)

        self.assertEqual(2, len(report.snapshot_paths))
        self.assertEqual([], validate_github(report))

    def test_supplement_directory_requires_matching_revision_suffix(self):
        self.make_valid_tree()
        self.write_snapshot(
            "10.1.5",
            "a" * 40,
            "2026-07-16",
            capture_kind="supplement",
            capture_revision=2,
            suffix="-r1",
        )

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(
            any("supplement revision disagrees with directory suffix" in error for error in errors),
            errors,
        )

    def test_supplement_directory_requires_r_suffix(self):
        self.make_valid_tree()
        self.write_snapshot(
            "10.1.5",
            "a" * 40,
            "2026-07-16",
            capture_kind="supplement",
            capture_revision=1,
            suffix="-supplement",
        )

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(
            any("supplement directory must end in -rN" in error for error in errors),
            errors,
        )

    def test_supplement_revision_is_unique_per_canonical_sha(self):
        self.make_valid_tree()
        self.write_snapshot(
            "10.1.5",
            "a" * 40,
            "2026-07-16",
            capture_kind="supplement",
            capture_revision=1,
            suffix="-r1",
        )
        self.write_snapshot(
            "10.1.5",
            "a" * 40,
            "2026-07-17",
            capture_kind="supplement",
            capture_revision=1,
            suffix="-r1",
        )

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("duplicate supplement revision 1" in error for error in errors), errors)

    def test_missing_required_reading_file_is_rejected(self):
        self.make_valid_tree()
        release_notes = next(self.root.glob("raw/github/*/*/snapshots/*/release-notes.md"))
        release_notes.unlink()

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("required reading is missing" in error for error in errors), errors)

    def test_generated_patch_under_raw_is_rejected(self):
        root = self.make_valid_tree()
        snapshot = next(root.glob("raw/github/*/*/snapshots/*"))
        (snapshot / "source-diff.patch").write_text("diff", encoding="utf-8")

        errors = validate_github(inspect_github(root))

        self.assertTrue(any("generated patch under raw" in error for error in errors), errors)

    def test_generated_diff_under_raw_is_rejected(self):
        root = self.make_valid_tree()
        snapshot = next(root.glob("raw/github/*/*/snapshots/*"))
        (snapshot / "files/change.diff").write_text("diff", encoding="utf-8")

        errors = validate_github(inspect_github(root))

        self.assertTrue(any("generated diff under raw" in error for error in errors), errors)

    def test_invalid_packet_transition_is_rejected(self):
        self.make_valid_tree()
        history = next(self.root.glob("tracking/github/repos/*/*/packets/*/state-events.jsonl"))
        packet_id = history.parent.name
        with history.open("a", encoding="utf-8") as handle:
            handle.write(
                json.dumps(
                    {
                        "from_state": "awaiting-review",
                        "packet_id": packet_id,
                        "state": "ingested",
                    },
                    sort_keys=True,
                )
                + "\n"
            )

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("invalid packet state" in error for error in errors), errors)

    def test_packet_directory_rejects_unexpected_real_directory(self):
        self.make_valid_tree()
        packet = next(
            path
            for path in self.root.glob("tracking/github/repos/*/*/packets/*")
            if path.is_dir()
        )
        (packet / "unexpected").mkdir()

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("packet has an invalid file set" in error for error in errors), errors)

    def test_packet_type_must_be_producer_supported(self):
        self.make_valid_tree()
        contract_path = next(self.root.glob("tracking/github/repos/*/*/packets/*/packet.json"))
        contract = json.loads(contract_path.read_text(encoding="utf-8"))
        contract["packet_type"] = "summary"
        contract_path.write_text(json.dumps(contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("unsupported packet type" in error for error in errors), errors)

    def test_packet_endpoint_must_equal_full_index_entry(self):
        self.make_valid_tree()
        contract_path = next(self.root.glob("tracking/github/repos/*/*/packets/*/packet.json"))
        contract = json.loads(contract_path.read_text(encoding="utf-8"))
        contract["to"]["release_notes_path"] = ""
        contract_path.write_text(json.dumps(contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("packet endpoint disagrees with version index" in error for error in errors), errors)

    def test_source_ledger_distinguishes_package_scopes_sharing_version(self):
        snapshot_path = "raw/github/paypal/paypal-js/snapshots/shared"
        snapshot = github_validation.SnapshotInspection(
            path=self.root / snapshot_path,
            relative_path=snapshot_path,
            repo_id="paypal/paypal-js",
            company="paypal",
            aliases=(),
            ref_name="@scope/one@1.0.0",
            package="@scope/one",
            version="1.0.0",
            sha="a" * 40,
            ref_kind="package-version",
            capture_kind="canonical",
            capture_revision=0,
            collection_date="2026-07-15",
            changelog_paths=(snapshot_path + "/files/CHANGELOG.md",),
            release_notes_path="",
        )

        def release(package):
            return github_validation.ReleaseEvidenceRecord(
                snapshot_path=snapshot_path,
                repo_id="paypal/paypal-js",
                ref_kind="package-version",
                ref_name=package + "@1.0.0",
                aliases=(),
                package=package,
                version="1.0.0",
                sha="a" * 40,
                collection_date="2026-07-15",
                capture_kind="canonical",
                capture_revision=0,
                changelog_paths=(snapshot_path + "/files/CHANGELOG.md",),
                release_notes_path=(
                    snapshot_path
                    + "/release-notes/"
                    + package.replace("/", "-")
                    + ".md"
                ),
                changelog_absence_explicit=True,
                release_notes_explicit=True,
            )

        releases = (release("@scope/one"), release("@scope/two"))
        rows = tuple(
            github_validation.ReleaseLedgerRow(
                version=item.ref_name,
                snapshot_link=snapshot_path + "/snapshot",
                changelog_links=(snapshot_path + "/files/CHANGELOG",),
                release_notes_links=(item.release_notes_path[:-3],),
                changelog_absent=False,
                release_notes_absent=False,
            )
            for item in releases
        )
        errors = []

        github_validation._validate_source_release_ledger(
            "source", (snapshot,), {snapshot_path: releases}, rows, errors
        )

        self.assertEqual([], errors)

    def test_baseline_packet_must_not_have_from_endpoint(self):
        self.make_valid_tree()
        contract_path = next(self.root.glob("tracking/github/repos/*/*/packets/*/packet.json"))
        contract = json.loads(contract_path.read_text(encoding="utf-8"))
        contract["from"] = contract["to"]
        contract["from_snapshot"] = contract["to_snapshot"]
        contract_path.write_text(json.dumps(contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("baseline packet has a from endpoint" in error for error in errors), errors)

    def test_packet_changed_files_must_be_safe_name_status_records(self):
        self.make_valid_tree()
        packet = next(
            path
            for path in self.root.glob("tracking/github/repos/*/*/packets/*")
            if path.is_dir()
        )
        contract_path = packet / "packet.json"
        contract = json.loads(contract_path.read_text(encoding="utf-8"))
        contract["changed_files"] = ["M\t../../outside.md"]
        contract_path.write_text(json.dumps(contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        (packet / "changed-files.txt").write_text("M\t../../outside.md\n", encoding="utf-8")

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("unsafe changed file" in error for error in errors), errors)

    def test_baseline_packet_must_not_have_changed_files(self):
        self.make_valid_tree()
        packet = next(
            path
            for path in self.root.glob("tracking/github/repos/*/*/packets/*")
            if path.is_dir()
        )
        contract_path = packet / "packet.json"
        contract = json.loads(contract_path.read_text(encoding="utf-8"))
        contract["changed_files"] = ["M\tREADME.md"]
        contract_path.write_text(json.dumps(contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        (packet / "changed-files.txt").write_text("M\tREADME.md\n", encoding="utf-8")

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("baseline packet has changed files" in error for error in errors), errors)

    def test_changed_files_text_must_equal_packet_contract(self):
        self.make_valid_tree()
        packet = next(
            path
            for path in self.root.glob("tracking/github/repos/*/*/packets/*")
            if path.is_dir()
        )
        (packet / "changed-files.txt").write_text("M\tREADME.md\n", encoding="utf-8")

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("changed-files.txt disagrees with packet contract" in error for error in errors), errors)

    def test_packet_required_reading_is_exact_and_deterministic(self):
        self.make_valid_tree()
        contract_path = next(self.root.glob("tracking/github/repos/*/*/packets/*/packet.json"))
        contract = json.loads(contract_path.read_text(encoding="utf-8"))
        contract["required_reading"] = list(reversed(contract["required_reading"]))
        contract_path.write_text(json.dumps(contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("required reading disagrees with producer contract" in error for error in errors), errors)

    def test_delta_required_reading_includes_changed_snapshot_evidence(self):
        self.make_valid_tree()
        prior = self.write_snapshot("10.0.0", "b" * 40, "2026-07-01")
        index_path, entries = self.read_version_entries()
        del index_path
        prior_entry = self.version_entry("10.0.0", "b" * 40, prior)
        entries.append(prior_entry)
        self.write_version_index(tuple(entries))
        contract_path = next(self.root.glob("tracking/github/repos/*/*/packets/*/packet.json"))
        contract = json.loads(contract_path.read_text(encoding="utf-8"))
        contract["packet_type"] = "delta"
        contract["from"] = prior_entry
        contract["from_snapshot"] = prior.as_posix()
        contract["changed_files"] = ["M\tREADME.md"]
        contract["required_reading"] = [
            prior.as_posix() + "/snapshot.md",
            contract["to_snapshot"] + "/snapshot.md",
            prior.as_posix() + "/release-notes.md",
            contract["to"]["release_notes_path"],
            prior.as_posix() + "/files/CHANGELOG.md",
            contract["to"]["changelog_paths"][0],
        ]
        contract_path.write_text(json.dumps(contract, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        (contract_path.parent / "changed-files.txt").write_text("M\tREADME.md\n", encoding="utf-8")

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("required reading disagrees with producer contract" in error for error in errors), errors)

    def test_packet_markdown_must_equal_producer_rendering(self):
        self.make_valid_tree()
        packet = next(
            path
            for path in self.root.glob("tracking/github/repos/*/*/packets/*")
            if path.is_dir()
        )
        (packet / "ingest-packet.md").write_text("# GitHub ingest packet\n", encoding="utf-8")

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("ingest-packet.md disagrees with packet contract" in error for error in errors), errors)

    def test_baseline_packet_patch_must_be_empty(self):
        self.make_valid_tree()
        packet = next(
            path
            for path in self.root.glob("tracking/github/repos/*/*/packets/*")
            if path.is_dir()
        )
        (packet / "source-diff.patch").write_text("forged patch\n", encoding="utf-8")

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("baseline source-diff.patch must be empty" in error for error in errors), errors)

    def test_collection_run_missing_terminal_is_rejected(self):
        self.make_valid_tree()
        run = self.root / "tracking/github/runs/test.jsonl"
        events = [
            json.loads(line)
            for line in run.read_text(encoding="utf-8").splitlines()
        ]
        run.write_text(json.dumps(events[0], sort_keys=True) + "\n", encoding="utf-8")

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("must have exactly one terminal event; found 0" in error for error in errors), errors)

    def test_collection_run_duplicate_terminal_is_rejected(self):
        self.make_valid_tree()
        run = self.root / "tracking/github/runs/test.jsonl"
        events = [
            json.loads(line)
            for line in run.read_text(encoding="utf-8").splitlines()
        ]
        run.write_text(
            "".join(json.dumps(event, sort_keys=True) + "\n" for event in events + [events[-1]]),
            encoding="utf-8",
        )

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("must have exactly one terminal event; found 2" in error for error in errors), errors)

    def test_unregistered_tracking_repository_namespace_is_rejected(self):
        self.make_valid_tree()
        orphan = self.root / "tracking/github/repos/acme/widgets/version-index.json"
        orphan.parent.mkdir(parents=True)
        orphan.write_text('{"repo_id":"acme/widgets","versions":[]}\n', encoding="utf-8")

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("tracking repository is not registered" in error for error in errors), errors)

    @unittest.skipUnless(hasattr(os, "symlink"), "symlinks are unavailable")
    def test_symlinked_tracking_repository_namespace_is_rejected(self):
        self.make_valid_tree()
        owner = self.root / "tracking/github/repos/acme"
        outside = self.root / "outside-tracking"
        outside.mkdir()
        owner.parent.mkdir(parents=True, exist_ok=True)
        owner.symlink_to(outside, target_is_directory=True)

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("tracking/github/repos/acme: unsafe symlink" in error for error in errors), errors)

    def test_unsafe_nested_tracking_artifact_is_rejected(self):
        self.make_valid_tree()
        nested = self.root / "tracking/github/repos/paypal/paypal-js/orphan/version-index.json"
        nested.parent.mkdir(parents=True)
        nested.write_text('{"repo_id":"paypal/paypal-js","versions":[]}\n', encoding="utf-8")

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("unexpected tracking repository entry" in error for error in errors), errors)

    def test_source_raw_files_are_newest_first(self):
        self.make_valid_tree()
        older = self.write_snapshot("10.0.0", "b" * 40, "2026-07-01")
        index_path, entries = self.read_version_entries()
        del index_path
        entries.append(self.version_entry("10.0.0", "b" * 40, older))
        self.write_version_index(tuple(entries))
        self.write_source((older, next(self.root.glob("raw/github/*/*/snapshots/2026-07-15-*"))))
        status_path = self.root / "tracking/github/status.json"
        status = json.loads(status_path.read_text(encoding="utf-8"))
        status["repositories"][0]["versions"] = [entry["version"] for entry in sorted(
            entries,
            key=lambda item: (
                item["ref_kind"], item["package"], item["version"], item["ref_name"], item["sha"]
            ),
        )]
        status_path.write_text(json.dumps(status, indent=2, sort_keys=True) + "\n", encoding="utf-8")

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("raw_files are not newest first" in error for error in errors), errors)

    def test_path_qualified_release_ledger_links_are_recorded(self):
        report = inspect_github(self.make_valid_tree())

        self.assertEqual(1, len(report.source_records))
        links = report.source_records[0].evidence_links
        self.assertTrue(any(link.endswith("/snapshot") for link in links), links)
        self.assertTrue(any(link.endswith("/files/CHANGELOG") for link in links), links)
        self.assertTrue(any(link.endswith("/release-notes") for link in links), links)
        self.assertEqual([], validate_github(report))

    def test_source_release_ledger_requires_one_row_per_declared_release(self):
        self.make_valid_tree()
        source = next(self.root.glob("wiki/sources/*/github/*.md"))
        text = source.read_text(encoding="utf-8")
        row = next(line for line in text.splitlines() if line.startswith("| 10.1.5 |"))
        source.write_text(text.replace(row + "\n", ""), encoding="utf-8")

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("release snapshot must have exactly one ledger row" in error for error in errors), errors)

    def test_source_release_ledger_version_must_match_snapshot(self):
        self.make_valid_tree()
        source = next(self.root.glob("wiki/sources/*/github/*.md"))
        source.write_text(
            source.read_text(encoding="utf-8").replace("| 10.1.5 |", "| 10.1.4 |"),
            encoding="utf-8",
        )

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("ledger version disagrees with snapshot" in error for error in errors), errors)

    def test_source_release_ledger_changelog_must_match_manifest(self):
        self.make_valid_tree()
        source = next(self.root.glob("wiki/sources/*/github/*.md"))
        text = source.read_text(encoding="utf-8")
        snapshot = next(self.root.glob("raw/github/*/*/snapshots/*")).relative_to(self.root).as_posix()
        text = text.replace(
            "[[" + snapshot + "/files/CHANGELOG|changelog]]",
            "[[" + snapshot + "/release-notes|changelog]]",
        )
        source.write_text(text, encoding="utf-8")

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("ledger changelog disagrees with snapshot manifest" in error for error in errors), errors)

    def test_source_release_ledger_cannot_claim_available_notes_absent(self):
        self.make_valid_tree()
        source = next(self.root.glob("wiki/sources/*/github/*.md"))
        text = source.read_text(encoding="utf-8")
        snapshot = next(self.root.glob("raw/github/*/*/snapshots/*")).relative_to(self.root).as_posix()
        text = text.replace(
            "[[" + snapshot + "/release-notes|release notes]]",
            "absent from immutable snapshot",
        )
        source.write_text(text, encoding="utf-8")

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("ledger release notes disagree with snapshot manifest" in error for error in errors), errors)

    def test_source_release_notes_absence_is_allowed_when_manifest_is_explicit(self):
        self.make_valid_tree()
        snapshot = next(self.root.glob("raw/github/*/*/snapshots/*"))
        manifest_path, metadata = self.read_manifest(snapshot.relative_to(self.root))
        metadata["release_notes"] = None
        (snapshot / "release-notes.md").unlink()
        self.write_manifest(manifest_path.parent, metadata)
        index_path, entries = self.read_version_entries()
        del index_path
        entries[0]["release_notes_path"] = ""
        self.write_version_index(tuple(entries))
        source = next(self.root.glob("wiki/sources/*/github/*.md"))
        snapshot_path = snapshot.relative_to(self.root).as_posix()
        source.write_text(
            source.read_text(encoding="utf-8").replace(
                "[[" + snapshot_path + "/release-notes|release notes]]",
                "absent from immutable snapshot",
            ),
            encoding="utf-8",
        )

        errors = validate_github(inspect_github(self.root))

        self.assertFalse(
            any("ledger release notes" in error for error in errors),
            errors,
        )

    def test_source_release_ledger_order_must_match_raw_files(self):
        self.make_valid_tree()
        older = self.write_snapshot("10.0.0", "b" * 40, "2026-07-01")
        index_path, entries = self.read_version_entries()
        del index_path
        entries.append(self.version_entry("10.0.0", "b" * 40, older))
        self.write_version_index(tuple(entries))
        latest = next(self.root.glob("raw/github/*/*/snapshots/2026-07-15-*"))
        source = self.write_source((latest, older))
        text = source.read_text(encoding="utf-8")
        older_path = older.as_posix()
        older_row = (
            "| 10.0.0 | [["
            + older_path
            + "/snapshot|snapshot]] | [["
            + older_path
            + "/files/CHANGELOG|changelog]] | [["
            + older_path
            + "/release-notes|release notes]] |\n"
        )
        latest_row = next(line for line in text.splitlines() if line.startswith("| 10.1.5 |")) + "\n"
        text = text.replace(latest_row, older_row + latest_row)
        source.write_text(text, encoding="utf-8")

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("ledger row order disagrees with raw_files" in error for error in errors), errors)

    def test_source_rejects_cross_repository_raw_link(self):
        self.make_valid_tree()
        source = next(self.root.glob("wiki/sources/*/github/*.md"))
        foreign = self.root / "raw/github/paypal/other/snapshots/foreign/snapshot.md"
        foreign.parent.mkdir(parents=True)
        foreign.write_text("foreign\n", encoding="utf-8")
        source.write_text(
            source.read_text(encoding="utf-8")
            + "\n- [[raw/github/paypal/other/snapshots/foreign/snapshot|foreign]]\n",
            encoding="utf-8",
        )

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("cross-repository raw link" in error for error in errors), errors)

    def test_status_disagreement_is_rejected(self):
        self.make_valid_tree()
        path = self.root / "tracking/github/status.json"
        status = json.loads(path.read_text(encoding="utf-8"))
        status["packets"][0]["state"] = "ingested"
        path.write_text(json.dumps(status, indent=2, sort_keys=True) + "\n", encoding="utf-8")

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("status disagreement" in error for error in errors), errors)

    def test_stable_track_rejects_prerelease_version_entry(self):
        report = inspect_github(self.make_valid_tree(index_version="10.2.0-beta.1"))

        self.assertTrue(
            any("prerelease in stable-only track" in error for error in validate_github(report))
        )

    def test_exact_package_prerelease_selector_allows_exact_prerelease(self):
        self.make_valid_tree(index_version="10.2.0-beta.1")
        self.set_version_track(
            "package:@paypal/paypal-js@10.2.0-beta.1", include_prerelease=False
        )

        errors = validate_github(inspect_github(self.root))

        self.assertFalse(any("prerelease in stable-only track" in error for error in errors), errors)

    def test_wrong_package_exact_prerelease_selector_does_not_allow_prerelease(self):
        self.make_valid_tree(index_version="10.2.0-beta.1")
        self.set_version_track(
            "package:@paypal/react-paypal-js@10.2.0-beta.1",
            include_prerelease=False,
        )

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("prerelease in stable-only track" in error for error in errors), errors)

    def test_include_prerelease_track_allows_matching_prerelease(self):
        self.make_valid_tree(index_version="10.2.0-beta.1")
        self.set_version_track(
            "package:@paypal/paypal-js@10", include_prerelease=True
        )

        errors = validate_github(inspect_github(self.root))

        self.assertFalse(any("prerelease in stable-only track" in error for error in errors), errors)

    def test_index_changelog_paths_must_equal_snapshot_manifest_evidence(self):
        self.make_valid_tree()
        index_path, entries = self.read_version_entries()
        entries[0]["changelog_paths"] = []
        self.write_version_index(tuple(entries))

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(
            any("index release evidence disagrees with snapshot manifest" in error for error in errors),
            errors,
        )

    def test_index_release_notes_path_must_equal_explicit_manifest_absence(self):
        self.make_valid_tree()
        snapshot = next(self.root.glob("raw/github/*/*/snapshots/*"))
        manifest_path, metadata = self.read_manifest(snapshot.relative_to(self.root))
        metadata["release_notes"] = None
        (snapshot / "release-notes.md").unlink()
        self.write_manifest(manifest_path.parent, metadata)

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(
            any("index release evidence disagrees with snapshot manifest" in error for error in errors),
            errors,
        )

    def test_index_release_evidence_cannot_point_at_another_snapshot(self):
        self.make_valid_tree()
        other = self.write_snapshot("10.0.0", "b" * 40, "2026-07-01")
        index_path, entries = self.read_version_entries()
        del index_path
        entries[0]["release_notes_path"] = other.as_posix() + "/release-notes.md"
        entries[0]["changelog_paths"] = [other.as_posix() + "/files/CHANGELOG.md"]
        entries.append(self.version_entry("10.0.0", "b" * 40, other))
        self.write_version_index(tuple(entries))

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(
            any("index release evidence disagrees with snapshot manifest" in error for error in errors),
            errors,
        )

    def test_retained_snapshot_missing_from_version_index_is_rejected(self):
        self.make_valid_tree()
        self.write_snapshot("10.0.0", "b" * 40, "2026-07-01")

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("retained version missing from index" in error for error in errors), errors)

    def test_release_evidence_must_not_be_silently_absent_from_manifest(self):
        self.make_valid_tree()
        snapshot = next(self.root.glob("raw/github/*/*/snapshots/*"))
        manifest_path, metadata = self.read_manifest(snapshot.relative_to(self.root))
        del metadata["release_notes"]
        self.write_manifest(manifest_path.parent, metadata)

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("release evidence is not explicit" in error for error in errors), errors)

    def test_newly_collected_release_requires_exactly_one_packet(self):
        self.make_valid_tree()
        packet = next(
            path
            for path in self.root.glob("tracking/github/repos/*/*/packets/*")
            if path.is_dir()
        )
        for child in packet.iterdir():
            child.unlink()
        packet.rmdir()

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("newly collected release must have exactly one packet" in error for error in errors), errors)

    @unittest.skipUnless(hasattr(os, "symlink"), "symlinks are unavailable")
    def test_symlinked_snapshot_is_rejected_without_following_it(self):
        self.make_valid_tree()
        snapshots = self.root / "raw/github/paypal/paypal-js/snapshots"
        outside = self.root / "outside"
        outside.mkdir()
        (outside / "source-diff.patch").write_text("outside\n", encoding="utf-8")
        (snapshots / "escaped").symlink_to(outside, target_is_directory=True)

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("unsafe symlink" in error for error in errors), errors)
        self.assertFalse(any("outside/source-diff.patch" in error for error in errors), errors)

    def test_required_reading_path_traversal_fails_closed(self):
        self.make_valid_tree()
        contract_path = next(self.root.glob("tracking/github/repos/*/*/packets/*/packet.json"))
        contract = json.loads(contract_path.read_text(encoding="utf-8"))
        contract["required_reading"] = ["raw/github/paypal/paypal-js/../../../../outside.md"]
        contract_path.write_text(
            json.dumps(contract, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("unsafe required reading path" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
