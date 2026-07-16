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

from github_packets import PacketRecord  # noqa: E402
from github_registry import load_registry  # noqa: E402
from github_reporting import (  # noqa: E402
    packet_state_key,
    render_collection_status,
    render_ingest_status,
)
from github_validation import inspect_github, validate_github  # noqa: E402


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

    def write_packet(self, version, sha, snapshot, state):
        packet_id = "baseline-" + version + "-" + sha[:7]
        directory = (
            self.root
            / "tracking/github/repos/paypal/paypal-js/packets"
            / packet_id
        )
        directory.mkdir(parents=True, exist_ok=True)
        snapshot_path = snapshot.as_posix()
        required = (
            snapshot_path + "/snapshot.md",
            snapshot_path + "/release-notes.md",
            snapshot_path + "/files/CHANGELOG.md",
        )
        entry = self.version_entry(version, sha, snapshot)
        contract = {
            "changed_files": [],
            "from": None,
            "from_snapshot": "",
            "initial_state": "awaiting-review",
            "packet_id": packet_id,
            "packet_type": "baseline",
            "repo_id": "paypal/paypal-js",
            "required_reading": list(required),
            "to": entry,
            "to_snapshot": snapshot_path,
        }
        (directory / "packet.json").write_text(
            json.dumps(contract, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        (directory / "ingest-packet.md").write_text("# GitHub ingest packet\n", encoding="utf-8")
        (directory / "changed-files.txt").write_text("\n", encoding="utf-8")
        (directory / "source-diff.patch").write_text("\n", encoding="utf-8")
        history = [{"packet_id": packet_id, "state": "awaiting-review"}]
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
                {"from_state": from_state, "packet_id": packet_id, "state": to_state}
            )
        (directory / "state-events.jsonl").write_text(
            "".join(json.dumps(event, sort_keys=True) + "\n" for event in history),
            encoding="utf-8",
        )
        return PacketRecord(
            packet_id=packet_id,
            repo_id="paypal/paypal-js",
            packet_type="baseline",
            from_snapshot="",
            to_snapshot=snapshot_path,
            required_reading=required,
            changed_files=(),
            initial_state="awaiting-review",
            directory=directory,
        )

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
        self.write_snapshot(
            "10.1.5",
            "a" * 40,
            "2026-07-16",
            capture_kind="supplement",
            capture_revision=1,
            suffix="-r1",
        )

        report = inspect_github(self.root)

        self.assertEqual(2, len(report.snapshot_paths))
        self.assertEqual([], validate_github(report))

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
        packet = next(self.root.glob("tracking/github/repos/*/*/packets/*"))
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
