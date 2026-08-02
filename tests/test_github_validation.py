import hashlib
import json
import shutil
import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from github_canonical import canonical_json_bytes  # noqa: E402
from github_ingest_packets import (  # noqa: E402
    PackagePacketInput,
    build_ingest_packet,
    load_packet_summary,
    publish_queued_packet,
)
from github_registry import load_registry  # noqa: E402
from github_validation import inspect_github, validate_github  # noqa: E402
from github_work_items import (  # noqa: E402
    PacketStatusSummary,
    PackageChange,
    build_work_item,
    render_status,
    save_work_items,
)


class GitHubValidationTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.write_registry()
        self.sha = "a" * 40
        self.snapshot_directory = (
            self.root
            / "raw/github/paypal/paypal-js/snapshots/2026-07-20-aaaaaaa"
        )
        self.snapshot_manifest_path = self.snapshot_directory / "manifest.json"
        source_content = b'{"name":"@paypal/paypal-js","version":"10.0.0"}\n'
        source_path = self.snapshot_directory / "files/packages/paypal-js/package.json"
        source_path.parent.mkdir(parents=True)
        source_path.write_bytes(source_content)
        self.snapshot_manifest = {
            "collected_date": "2026-07-20",
            "excluded": [],
            "files": [
                {
                    "classification_reason": "package-manifest",
                    "git_blob_oid": "b" * 40,
                    "git_mode": "100644",
                    "package": "@paypal/paypal-js",
                    "path": "packages/paypal-js/package.json",
                    "purpose": "package-manifest",
                    "sha256": hashlib.sha256(source_content).hexdigest(),
                    "size": len(source_content),
                }
            ],
            "format_version": 1,
            "repository": "paypal/paypal-js",
            "sha": self.sha,
            "triggering_refs": ["@paypal/paypal-js@10.0.0"],
        }
        self.write_json(self.snapshot_manifest_path, self.snapshot_manifest)

        self.release_directory = (
            self.root
            / "raw/github/paypal/paypal-js/releases/paypal-js/10.0.0/2026-07-20"
        )
        self.release_notes = b"Initial v10 release.\n"
        self.release_directory.mkdir(parents=True)
        (self.release_directory / "release-notes.md").write_bytes(self.release_notes)
        self.release_manifest_path = self.release_directory / "manifest.json"
        self.release_manifest = {
            "collected_date": "2026-07-20",
            "format_version": 1,
            "notes_available": True,
            "notes_sha256": hashlib.sha256(self.release_notes).hexdigest(),
            "package": "@paypal/paypal-js",
            "release_date": "2026-07-07T12:00:00Z",
            "repository": "paypal/paypal-js",
            "sha": self.sha,
            "source_url": "https://api.github.test/releases/1",
            "tag": "@paypal/paypal-js@10.0.0",
            "version": "10.0.0",
        }
        self.write_release_manifest()

        self.snapshot_relative = self.relative(self.snapshot_manifest_path)
        self.release_relative = self.relative(self.release_manifest_path)
        self.change = PackageChange(
            "@paypal/paypal-js",
            "",
            "10.0.0",
            "@paypal/paypal-js@10.0.0",
            self.release_relative,
            "",
            "full",
            ("initial-package-baseline",),
        )
        self.work_item = replace(
            build_work_item(
                "paypal/paypal-js",
                self.sha,
                "2026-07-20",
                (self.change,),
                self.snapshot_relative,
            ),
            state="awaiting_approval",
        )
        self.save_work_items()

    @property
    def queue_path(self):
        return self.root / "tracking/github/work-items.json"

    @property
    def status_path(self):
        return self.root / "tracking/github/status.md"

    @property
    def source_path(self):
        return self.root / "wiki/sources/paypal/github/source-github-paypal-js.md"

    @property
    def changelog_path(self):
        return self.root / "wiki/sources/paypal/github/changelog-github-paypal-js.md"

    def write_registry(self, historical_policy_hashes=(), default_required_roots=("src",)):
        path = self.root / "tracking/github/repo-registry.toml"
        path.parent.mkdir(parents=True, exist_ok=True)
        historical_policy = (
            "historical_policy_hashes=["
            + ",".join(json.dumps(value) for value in historical_policy_hashes)
            + "]\n"
            if historical_policy_hashes
            else ""
        )
        roots = ",".join(json.dumps(value) for value in default_required_roots)
        path.write_text(
            """[[repos]]
id="paypal/paypal-js"
company="paypal"
url="https://github.com/paypal/paypal-js"
enabled=true
repo_type="sdk"
priority="tier1"
track="releases-and-default-branch"
version_strategy="monorepo-packages"

[[repos.version_tracks]]
selector="package:@paypal/paypal-js@10"
backfill="all-stable"
future="all-stable"
include_prerelease=false

[[repos.capsules]]
id="paypal-js-source"
adapter="npm-tracked-source-v1"
focus_packages=["@paypal/paypal-js"]
default_required_roots=[""" + roots + "]\n" + historical_policy + """default_generated_target_paths=[]
""",
            encoding="utf-8",
        )

    def write_json(self, path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(canonical_json_bytes(value) + b"\n")

    def write_release_manifest(self):
        self.write_json(self.release_manifest_path, self.release_manifest)

    def write_comparison(
        self,
        package="@paypal/paypal-js",
        from_version="9.0.0",
        to_version="10.0.0",
        from_sha=None,
        to_sha=None,
        format_version=1,
        upstream_changes=None,
    ):
        slug = package.rsplit("/", 1)[-1]
        directory = (
            self.root
            / "tracking/github/repos/paypal/paypal-js/comparisons"
            / slug
            / (from_version + "--" + to_version)
        )
        directory.mkdir(parents=True)
        patch = b""
        markdown = b"# Comparison\n"
        manifest = directory / "comparison.json"
        changes = upstream_changes or []
        changed_paths = sorted(
            {
                path
                for row in changes
                for path in (row.get("old_path"), row.get("new_path"))
                if path
            }
        )
        document = {
            "changed_paths": changed_paths,
            "format_version": format_version,
            "from_sha": from_sha or ("f" * 40),
            "from_version": from_version,
            "markdown_sha256": hashlib.sha256(markdown).hexdigest(),
            "package": package,
            "patch_sha256": hashlib.sha256(patch).hexdigest(),
            "pathspecs": ["packages/" + slug],
            "repository": "paypal/paypal-js",
            "to_sha": to_sha or self.sha,
            "to_version": to_version,
        }
        if format_version == 2:
            document["upstream_changes"] = changes
        self.write_json(manifest, document)
        (directory / "diff.patch").write_bytes(patch)
        (directory / "comparison.md").write_bytes(markdown)
        return manifest

    def save_work_items(self):
        save_work_items(self.queue_path, (self.work_item,))
        summaries = {}
        if self.work_item.ingest_packet:
            packet = load_packet_summary(
                self.root, self.work_item.ingest_packet
            )
            summaries[self.work_item.work_item_id] = PacketStatusSummary(
                packet.packet_path,
                packet.priority,
                packet.required_reading_count,
                packet.unclassified_count,
                packet.evidence_gap_count,
            )
        self.status_path.parent.mkdir(parents=True, exist_ok=True)
        self.status_path.write_text(
            render_status((self.work_item,), summaries), encoding="utf-8"
        )

    def relative(self, path):
        return path.resolve().relative_to(self.root.resolve()).as_posix()

    def enable_packet(self):
        config = load_registry(
            self.root / "tracking/github/repo-registry.toml"
        )[0]
        packet = build_ingest_packet(
            self.root,
            config,
            self.work_item.work_item_id,
            self.snapshot_relative,
            (
                PackagePacketInput(
                    package="@paypal/paypal-js",
                    from_version="",
                    to_version="10.0.0",
                    from_sha="",
                    to_sha=self.sha,
                    release_manifest=self.release_relative,
                    comparison_manifest="",
                    prior_snapshot_manifest="",
                    upstream_changes=(),
                ),
            ),
            "queued",
        )
        packet_path = publish_queued_packet(self.root, config, packet)
        self.work_item = replace(
            self.work_item,
            ingest_packet=self.relative(packet_path),
        )
        self.save_work_items()
        return packet_path

    def write_ingested_pages(self, changelog_body=None):
        self.source_path.parent.mkdir(parents=True, exist_ok=True)
        self.source_path.write_text(
            "# PayPal JS\n\n"
            + "Raw snapshot: `"
            + self.snapshot_relative
            + "`\n",
            encoding="utf-8",
        )
        body = changelog_body
        if body is None:
            body = (
                "# PayPal JS changelog\n\n"
                + "@paypal/paypal-js@10.0.0\n\n"
                + self.snapshot_relative
                + "\n\n"
                + self.release_relative
                + "\n"
            )
        self.changelog_path.write_text(body, encoding="utf-8")

    def test_valid_historical_packetless_work_item_has_no_errors(self):
        report = inspect_github(self.root)

        self.assertEqual([], validate_github(report))

    def test_valid_packet_enabled_work_item_has_no_errors(self):
        self.enable_packet()

        self.assertEqual([], validate_github(inspect_github(self.root)))

    def test_packet_json_must_be_canonical(self):
        packet_path = self.enable_packet()
        document = json.loads(packet_path.read_text(encoding="utf-8"))
        packet_path.write_text(
            json.dumps(document, indent=2) + "\n",
            encoding="utf-8",
        )

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("packet JSON is not canonical" in item for item in errors))

    def test_packet_markdown_hash_mismatch_is_rejected(self):
        packet_path = self.enable_packet()
        (packet_path.parent / "packet.md").write_text(
            "tampered\n", encoding="utf-8"
        )

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("packet Markdown hash mismatch" in item for item in errors))

    def test_packet_required_reading_must_still_exist(self):
        self.enable_packet()
        (
            self.snapshot_directory
            / "files/packages/paypal-js/package.json"
        ).unlink()

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("packet rebuild failed" in item for item in errors))

    def test_packet_deterministic_content_mismatch_is_rejected(self):
        packet_path = self.enable_packet()
        document = json.loads(packet_path.read_text(encoding="utf-8"))
        document["packages"][0]["retained_evidence"]["counts"]["added"] += 1
        self.write_json(packet_path, document)

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(
            any("packet deterministic content mismatch" in item for item in errors)
        )

    def test_packet_rebuild_uses_registered_historical_policy(self):
        packet_path = self.enable_packet()
        document = json.loads(packet_path.read_text(encoding="utf-8"))

        self.write_registry(
            historical_policy_hashes=(document["capsule_policy_sha256"],),
            default_required_roots=("src", "types"),
        )

        self.assertEqual([], validate_github(inspect_github(self.root)))

    def test_packet_path_and_work_item_identity_mismatch_is_rejected(self):
        packet_path = self.enable_packet()
        document = json.loads(packet_path.read_text(encoding="utf-8"))
        document["work_item_id"] = "github-" + ("f" * 20)
        self.write_json(packet_path, document)

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(
            any("packet path/work-item identity mismatch" in item for item in errors)
        )

    def test_packet_validation_remains_stable_after_expected_wiki_pages_exist(self):
        self.enable_packet()
        self.source_path.parent.mkdir(parents=True, exist_ok=True)
        self.source_path.write_text("# Source\n", encoding="utf-8")
        self.changelog_path.write_text("# Changelog\n", encoding="utf-8")

        self.assertEqual([], validate_github(inspect_github(self.root)))

    def test_release_record_must_link_an_existing_sha_snapshot(self):
        self.release_manifest["sha"] = "f" * 40
        self.write_release_manifest()

        errors = validate_github(inspect_github(self.root))

        self.assertIn("release record links missing SHA snapshot", "\n".join(errors))

    def test_work_item_release_must_match_repository_and_sha(self):
        other_sha = "f" * 40
        other_snapshot = self.root / "raw/github/paypal/paypal-js/snapshots/2026-07-21-fffffff"
        shutil.copytree(self.snapshot_directory, other_snapshot)
        other_manifest = dict(self.snapshot_manifest)
        other_manifest["sha"] = other_sha
        self.write_json(other_snapshot / "manifest.json", other_manifest)
        self.release_manifest["sha"] = other_sha
        self.write_release_manifest()

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("work-item release SHA mismatch" in item for item in errors))

    def test_work_item_comparison_must_match_package_versions_and_target_sha(self):
        prior_sha = "f" * 40
        prior_snapshot = self.root / "raw/github/paypal/paypal-js/snapshots/2026-07-19-fffffff"
        shutil.copytree(self.snapshot_directory, prior_snapshot)
        prior_manifest = dict(self.snapshot_manifest)
        prior_manifest["sha"] = prior_sha
        self.write_json(prior_snapshot / "manifest.json", prior_manifest)
        comparison_manifest = self.write_comparison(
            package="@paypal/react-paypal-js",
            from_sha=prior_sha,
        )
        changed = replace(
            self.change,
            from_version="9.0.0",
            comparison_manifest=self.relative(comparison_manifest),
            reasons=("major-version-transition",),
        )
        self.work_item = replace(
            build_work_item(
                "paypal/paypal-js",
                self.sha,
                "2026-07-20",
                (changed,),
                self.snapshot_relative,
            ),
            state="awaiting_approval",
        )
        self.save_work_items()

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("work-item comparison identity mismatch" in item for item in errors))

    def test_comparison_file_hash_mismatch_is_rejected(self):
        prior_sha = "f" * 40
        prior_snapshot = self.root / "raw/github/paypal/paypal-js/snapshots/2026-07-19-fffffff"
        shutil.copytree(self.snapshot_directory, prior_snapshot)
        prior_manifest = dict(self.snapshot_manifest)
        prior_manifest["sha"] = prior_sha
        self.write_json(prior_snapshot / "manifest.json", prior_manifest)
        comparison_manifest = self.write_comparison(from_sha=prior_sha)
        (comparison_manifest.parent / "diff.patch").write_text("tampered\n", encoding="utf-8")

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("comparison patch hash mismatch" in item for item in errors))

    def test_comparison_validator_accepts_v1_and_v2_manifests(self):
        self.write_comparison(from_sha=self.sha)
        errors = validate_github(inspect_github(self.root))
        self.assertEqual([], errors)

        shutil.rmtree(self.root / "tracking/github/repos")
        self.write_comparison(
            from_sha=self.sha,
            format_version=2,
            upstream_changes=[
                {
                    "status": "modified",
                    "old_path": "packages/paypal-js/package.json",
                    "new_path": "packages/paypal-js/package.json",
                }
            ],
        )

        self.assertEqual([], validate_github(inspect_github(self.root)))

    def test_comparison_validator_rejects_malformed_v2_rename(self):
        manifest = self.write_comparison(
            from_sha=self.sha,
            format_version=2,
            upstream_changes=[
                {
                    "status": "renamed",
                    "old_path": "packages/paypal-js/old.ts",
                    "new_path": "",
                }
            ],
        )
        document = json.loads(manifest.read_text(encoding="utf-8"))
        document["changed_paths"] = ["packages/paypal-js/old.ts"]
        self.write_json(manifest, document)

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("comparison upstream change row is invalid" in item for item in errors))

    def test_comparison_validator_rejects_changed_path_union_mismatch(self):
        manifest = self.write_comparison(
            from_sha=self.sha,
            format_version=2,
            upstream_changes=[
                {
                    "status": "added",
                    "old_path": "",
                    "new_path": "packages/paypal-js/new.ts",
                }
            ],
        )
        document = json.loads(manifest.read_text(encoding="utf-8"))
        document["changed_paths"] = []
        self.write_json(manifest, document)

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("comparison changed path union mismatch" in item for item in errors))

    def test_release_record_accepts_plain_upstream_tag_for_exact_package_version(self):
        self.release_manifest["tag"] = "v10.0.0"
        self.write_release_manifest()

        errors = validate_github(inspect_github(self.root))

        self.assertEqual([], errors)

    def test_release_record_rejects_plain_upstream_tag_for_different_version(self):
        self.release_manifest["tag"] = "v10.0.1"
        self.write_release_manifest()

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("release tag does not match package version" in item for item in errors))

    def test_status_markdown_must_match_work_items_json(self):
        self.status_path.write_text("stale\n", encoding="utf-8")

        errors = validate_github(inspect_github(self.root))

        self.assertIn("tracking/github/status.md is stale", errors)

    def test_source_and_changelog_are_both_required_after_ingest(self):
        self.work_item = replace(
            self.work_item,
            state="ingested",
            approved_mode="full",
        )
        self.save_work_items()

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("source-github-paypal-js.md" in item for item in errors))
        self.assertTrue(any("changelog-github-paypal-js.md" in item for item in errors))

    def test_snapshot_hash_mismatch_is_rejected(self):
        source_path = self.snapshot_directory / "files/packages/paypal-js/package.json"
        source_path.write_text("tampered\n", encoding="utf-8")

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("snapshot file hash mismatch" in item for item in errors))

    def test_supplement_hash_mismatch_is_rejected(self):
        directory = (
            self.root
            / "raw/github/paypal/paypal-js/supplements/2026-07-21-aaaaaaa-12345678"
        )
        source = b"export const value = 1;\n"
        source_path = directory / "files/packages/paypal-js/src/index.ts"
        source_path.parent.mkdir(parents=True)
        source_path.write_bytes(source)
        files = [
            {
                "classification_reason": "explicit-query-path",
                "git_blob_oid": "c" * 40,
                "git_mode": "100644",
                "package": "",
                "path": "packages/paypal-js/src/index.ts",
                "purpose": "query-supplement",
                "sha256": hashlib.sha256(source).hexdigest(),
                "size": len(source),
            }
        ]
        identity = hashlib.sha256(
            canonical_json_bytes(
                {
                    "files": [
                        {
                            "path": files[0]["path"],
                            "sha256": files[0]["sha256"],
                        }
                    ],
                    "repository": "paypal/paypal-js",
                    "sha": self.sha,
                }
            )
        ).hexdigest()
        self.write_json(
            directory / "manifest.json",
            {
                "collected_date": "2026-07-21",
                "files": files,
                "format_version": 1,
                "identity_sha256": identity,
                "repository": "paypal/paypal-js",
                "sha": self.sha,
            },
        )
        source_path.write_text("tampered\n", encoding="utf-8")

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("supplement file hash mismatch" in item for item in errors))

    def test_unsafe_snapshot_paths_are_rejected(self):
        self.snapshot_manifest["files"][0]["path"] = "../escape.md"
        self.write_json(self.snapshot_manifest_path, self.snapshot_manifest)

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("unsafe snapshot file path" in item for item in errors))

    def test_duplicate_release_identity_requires_revision_naming(self):
        duplicate = self.release_directory.parent / "2026-07-21"
        shutil.copytree(self.release_directory, duplicate)

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("duplicate release identity without revision" in item for item in errors))

    def test_missing_comparison_link_is_rejected(self):
        changed = replace(
            self.change,
            from_version="9.0.0",
            comparison_manifest=(
                "tracking/github/repos/paypal/paypal-js/comparisons/"
                "paypal-js/9.0.0--10.0.0/comparison.json"
            ),
            reasons=("major-version-transition",),
        )
        self.work_item = replace(
            build_work_item(
                "paypal/paypal-js",
                self.sha,
                "2026-07-20",
                (changed,),
                self.snapshot_relative,
            ),
            state="awaiting_approval",
        )
        self.save_work_items()

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("missing comparison manifest" in item for item in errors))

    def test_invalid_work_item_state_is_rejected(self):
        document = json.loads(self.queue_path.read_text(encoding="utf-8"))
        document["work_items"][0]["state"] = "auto_ingesting"
        self.write_json(self.queue_path, document)

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("work-item queue" in item for item in errors))

    def test_changelog_requires_package_version_and_raw_links(self):
        self.work_item = replace(
            self.work_item,
            state="ingested",
            approved_mode="full",
        )
        self.save_work_items()
        self.write_ingested_pages("# PayPal JS changelog\n\nVersion 10 shipped.\n")

        errors = validate_github(inspect_github(self.root))

        self.assertTrue(any("package-qualified release" in item for item in errors))
        self.assertTrue(any("raw evidence link" in item for item in errors))

    def test_valid_ingested_pages_link_cumulative_evidence(self):
        self.work_item = replace(
            self.work_item,
            state="ingested",
            approved_mode="full",
        )
        self.save_work_items()
        self.write_ingested_pages()

        self.assertEqual([], validate_github(inspect_github(self.root)))


if __name__ == "__main__":
    unittest.main()
