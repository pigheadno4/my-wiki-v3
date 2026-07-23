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
from github_validation import inspect_github, validate_github  # noqa: E402
from github_work_items import (  # noqa: E402
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

    def write_registry(self):
        path = self.root / "tracking/github/repo-registry.toml"
        path.parent.mkdir(parents=True)
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
default_required_roots=["src"]
default_generated_target_paths=[]
""",
            encoding="utf-8",
        )

    def write_json(self, path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(canonical_json_bytes(value) + b"\n")

    def write_release_manifest(self):
        self.write_json(self.release_manifest_path, self.release_manifest)

    def save_work_items(self):
        save_work_items(self.queue_path, (self.work_item,))
        self.status_path.parent.mkdir(parents=True, exist_ok=True)
        self.status_path.write_text(
            render_status((self.work_item,)), encoding="utf-8"
        )

    def relative(self, path):
        return path.relative_to(self.root).as_posix()

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

    def test_valid_focused_repository_has_no_errors(self):
        report = inspect_github(self.root)

        self.assertEqual([], validate_github(report))

    def test_release_record_must_link_an_existing_sha_snapshot(self):
        self.release_manifest["sha"] = "f" * 40
        self.write_release_manifest()

        errors = validate_github(inspect_github(self.root))

        self.assertIn("release record links missing SHA snapshot", "\n".join(errors))

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
