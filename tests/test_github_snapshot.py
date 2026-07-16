from dataclasses import replace
import fcntl
import hashlib
import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from github_git import ResolvedRef  # noqa: E402
from github_releases import ReleaseNotesEvidence  # noqa: E402
from github_registry import RepoConfig  # noqa: E402
import github_snapshot  # noqa: E402
from github_snapshot import (  # noqa: E402
    SnapshotError,
    build_snapshot,
    promote_snapshot,
    select_key_files,
    validate_staged_snapshot,
)


class GitHubSnapshotTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name).resolve()
        self.repo = self.root / "checkout"
        self.repo.mkdir()
        self.raw_root = self.root / "raw" / "github"
        self.staging_root = self.raw_root / ".staging"
        self.ref = ResolvedRef(
            repo_id="paypal/paypal-js",
            ref_kind="package-version",
            ref_name="@paypal/paypal-js@10.1.0",
            sha="a1b2c3d" * 5 + "a1b2c3d"[:5],
            version="10.1.0",
            aliases=("v10.1.0", "stable"),
            upstream_commit_time="2026-07-13T12:30:00+00:00",
            release_published_at="2026-07-14T08:00:00+00:00",
        )

    def tearDown(self):
        self.temporary.cleanup()

    def config(self, **overrides):
        values = {
            "id": "paypal/paypal-js",
            "company": "paypal",
            "url": "https://github.com/paypal/paypal-js",
            "enabled": True,
            "repo_type": "web-sdk",
            "priority": "tier1",
            "track": "releases-and-default-branch",
            "version_strategy": "monorepo-packages",
            "key_paths": (),
            "exclude_paths": (),
            "max_file_bytes": 1024,
            "max_snapshot_bytes": 4096,
        }
        values.update(overrides)
        return RepoConfig(**values)

    def write(self, relative, content):
        path = self.repo / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)

    def manifest_metadata(self, record):
        manifest = (record.staging_path / "snapshot.md").read_text(encoding="utf-8")
        start = manifest.index("```json\n") + len("```json\n")
        end = manifest.index("\n```", start)
        return json.loads(manifest[start:end])

    def promotion_lock(self, record):
        return record.target_path.parent / ".promotion.lock"

    def write_manifest_metadata(self, record, metadata):
        manifest_path = record.staging_path / "snapshot.md"
        manifest = manifest_path.read_text(encoding="utf-8")
        original = json.dumps(self.manifest_metadata(record), indent=2, sort_keys=True)
        manifest_path.write_text(
            manifest.replace(original, json.dumps(metadata, indent=2, sort_keys=True)),
            encoding="utf-8",
        )

    def test_select_key_files_uses_sorted_policy_and_excludes_unreadable_candidates(self):
        self.write("README.md", b"readme\n")
        self.write("CHANGELOG.md", b"changes\n")
        self.write("docs/migrations/v2.md", b"migration\n")
        self.write("package.json", b"{}\n")
        self.write("openapi.yaml", b"openapi: 3.0.0\n")
        self.write("docs/guide.md", b"guide\n")
        self.write("src/index.ts", b"export {};\n")
        self.write("examples/demo.js", b"demo();\n")
        self.write("internal/private.py", b"private\n")
        self.write("vendor/sdk.py", b"vendor\n")
        self.write("build/output.js", b"build\n")
        self.write("package-lock.json", b"lock\n")
        self.write("assets/logo.bin", b"text\x00binary")
        self.write("docs/oversize.md", b"x" * 1025)

        result = select_key_files(
            self.config(
                key_paths=(
                    "assets/logo.bin",
                    "build",
                    "docs/guide.md",
                    "docs/oversize.md",
                    "package-lock.json",
                    "vendor",
                ),
                exclude_paths=("vendor",),
            ),
            self.repo,
            changed_paths=("examples/demo.js", "internal/private.py", "src/index.ts"),
        )

        self.assertEqual(
            (
                "CHANGELOG.md",
                "README.md",
                "docs/guide.md",
                "docs/migrations/v2.md",
                "examples/demo.js",
                "openapi.yaml",
                "package.json",
                "src/index.ts",
            ),
            tuple(path.relative_to(self.repo).as_posix() for path in result.selected),
        )
        self.assertEqual(sum(path.stat().st_size for path in result.selected), result.total_bytes)
        excluded = dict(result.excluded)
        self.assertIn("vendor/sdk.py", excluded)
        self.assertIn("build/output.js", excluded)
        self.assertIn("package-lock.json", excluded)
        self.assertIn("assets/logo.bin", excluded)
        self.assertIn("docs/oversize.md", excluded)

    def test_selection_stops_before_total_limit(self):
        self.write("README.md", b"r" * 8)
        self.write("CHANGELOG.md", b"c" * 8)

        result = select_key_files(self.config(max_snapshot_bytes=12), self.repo)

        self.assertEqual(("CHANGELOG.md",), tuple(path.name for path in result.selected))
        self.assertIn("README.md", dict(result.excluded))
        self.assertEqual(8, result.total_bytes)

    def test_selection_does_not_apply_vendor_exclusion_from_checkout_ancestors(self):
        repo = self.root / "vendor" / "checkout"
        repo.mkdir(parents=True)
        (repo / "README.md").write_text("readme\n", encoding="utf-8")

        result = select_key_files(self.config(), repo)

        self.assertEqual(("README.md",), tuple(path.name for path in result.selected))

    def test_snapshot_copies_exact_bytes_renders_complete_manifest_and_keeps_diffs_outside_raw(self):
        selected = b"# README\n"
        self.write("README.md", selected)

        record = build_snapshot(
            self.config(), self.ref, self.repo, self.raw_root, self.staging_root, "2026-07-14"
        )

        copied = record.staging_path / "files" / "README.md"
        manifest = (record.staging_path / "snapshot.md").read_text(encoding="utf-8")
        self.assertEqual(selected, copied.read_bytes())
        self.assertEqual(hashlib.sha256(selected).hexdigest(), record.files[0].sha256)
        self.assertIn("| Repository URL | https://github.com/paypal/paypal-js |", manifest)
        self.assertIn("| Full SHA | " + self.ref.sha + " |", manifest)
        self.assertIn("| Capture kind | canonical |", manifest)
        self.assertIn("| Path | SHA-256 | Bytes | Purpose |", manifest)
        self.assertIn("| Path | Reason |", manifest)
        self.assertFalse(any(path.suffix == ".patch" for path in record.staging_path.rglob("*")))
        self.assertEqual([], validate_staged_snapshot(record))

    def test_validation_detects_unlisted_or_changed_snapshot_files(self):
        self.write("README.md", b"original\n")
        record = build_snapshot(
            self.config(), self.ref, self.repo, self.raw_root, self.staging_root, "2026-07-14"
        )
        (record.staging_path / "files" / "README.md").write_bytes(b"changed\n")
        (record.staging_path / "files" / "unlisted.md").write_text("unlisted\n", encoding="utf-8")

        errors = validate_staged_snapshot(record)

        self.assertTrue(any("hash mismatch" in error for error in errors))
        self.assertTrue(any("not listed" in error for error in errors))

    def test_validation_requires_complete_snapshot_identity_metadata(self):
        self.write("README.md", b"original\n")
        record = build_snapshot(
            self.config(), self.ref, self.repo, self.raw_root, self.staging_root, "2026-07-14"
        )
        manifest_path = record.staging_path / "snapshot.md"
        manifest_path.write_text(
            manifest_path.read_text(encoding="utf-8").replace(
                '"url": "https://github.com/paypal/paypal-js"', '"url": ""'
            ),
            encoding="utf-8",
        )

        errors = validate_staged_snapshot(record)

        self.assertTrue(any("metadata mismatch" in error for error in errors))

    def test_existing_target_without_matching_accepted_snapshot_is_rejected(self):
        self.write("README.md", b"snapshot\n")
        record = build_snapshot(
            self.config(), self.ref, self.repo, self.raw_root, self.staging_root, "2026-07-14"
        )
        record.target_path.mkdir(parents=True)

        with self.assertRaisesRegex(SnapshotError, "already exists"):
            promote_snapshot(record)

    def test_canonical_recollection_returns_existing_snapshot_and_supplements_get_revisions(self):
        self.write("README.md", b"snapshot\n")
        canonical = build_snapshot(
            self.config(), self.ref, self.repo, self.raw_root, self.staging_root, "2026-07-14"
        )
        promoted = promote_snapshot(canonical)
        recollection = build_snapshot(
            self.config(), self.ref, self.repo, self.raw_root, self.staging_root, "2026-07-14"
        )
        supplement = build_snapshot(
            self.config(),
            self.ref,
            self.repo,
            self.raw_root,
            self.staging_root,
            "2026-07-14",
            prior_snapshot="raw/github/paypal/paypal-js/snapshots/prior",
            capture_kind="supplement",
        )

        self.assertEqual(promoted, promote_snapshot(recollection))
        self.assertEqual("supplement", supplement.capture_kind)
        self.assertEqual(1, supplement.capture_revision)
        self.assertTrue(supplement.target_path.name.endswith("-r1"))
        self.assertEqual(supplement.target_path, promote_snapshot(supplement))

    def test_build_rejects_staging_outside_raw_github_staging(self):
        self.write("README.md", b"snapshot\n")

        with self.assertRaisesRegex(SnapshotError, "raw/github/.staging"):
            build_snapshot(
                self.config(),
                self.ref,
                self.repo,
                self.raw_root,
                self.root / "staging",
                "2026-07-14",
            )

    def test_changed_public_path_reaches_built_snapshot(self):
        self.write("src/public.js", b"export const value = 1;\n")

        record = build_snapshot(
            self.config(),
            self.ref,
            self.repo,
            self.raw_root,
            self.staging_root,
            "2026-07-14",
            changed_paths=("src/public.js",),
        )

        self.assertTrue((record.staging_path / "files/src/public.js").exists())

    def test_symlink_and_parent_traversal_never_leave_checkout(self):
        outside = self.repo.parent / "secret.txt"
        outside.write_text("secret", encoding="utf-8")
        (self.repo / "README.md").symlink_to(outside)

        result = select_key_files(
            self.config(key_paths=("../secret.txt",)),
            self.repo,
            changed_paths=("/tmp/secret.txt", "../secret.txt"),
        )

        self.assertEqual((), result.selected)
        self.assertTrue(any(reason == "outside-checkout" for _, reason in result.excluded))
        self.assertTrue(any(reason == "symlink is not allowed" for _, reason in result.excluded))

    def test_release_notes_are_exact_top_level_evidence(self):
        evidence = ReleaseNotesEvidence(
            "https://api.github.test/release", "2026-07-14T00:00:00Z", b"# Exact notes\n"
        )
        self.write("README.md", b"snapshot\n")

        record = build_snapshot(
            self.config(),
            self.ref,
            self.repo,
            self.raw_root,
            self.staging_root,
            "2026-07-14",
            release_notes=evidence,
        )

        self.assertEqual(b"# Exact notes\n", (record.staging_path / "release-notes.md").read_bytes())
        metadata = self.manifest_metadata(record)
        self.assertEqual("https://api.github.test/release", metadata["release_notes"]["source_url"])
        self.assertEqual([], validate_staged_snapshot(record))

    def test_empty_selection_creates_files_directory_and_promotes(self):
        record = build_snapshot(
            self.config(key_paths=("missing.md",)),
            self.ref,
            self.repo,
            self.raw_root,
            self.staging_root,
            "2026-07-14",
        )

        self.assertEqual((), record.files)
        self.assertTrue((record.staging_path / "files").is_dir())
        self.assertEqual([], validate_staged_snapshot(record))
        promoted = promote_snapshot(record)
        self.assertTrue((promoted / "files").is_dir())
        self.assertEqual([], list((promoted / "files").iterdir()))

    def test_release_notes_only_capture_validates_promotes_and_preserves_exact_bytes(self):
        evidence = ReleaseNotesEvidence(
            "https://api.github.test/release", "2026-07-14T00:00:00Z", b"# Exact notes\n| raw |\n"
        )
        record = build_snapshot(
            self.config(key_paths=("missing.md",)),
            self.ref,
            self.repo,
            self.raw_root,
            self.staging_root,
            "2026-07-14",
            release_notes=evidence,
        )

        self.assertEqual((), record.files)
        self.assertTrue((record.staging_path / "files").is_dir())
        self.assertEqual(evidence.content, (record.staging_path / "release-notes.md").read_bytes())
        self.assertEqual([], validate_staged_snapshot(record))
        promoted = promote_snapshot(record)
        self.assertEqual(evidence.content, (promoted / "release-notes.md").read_bytes())
        self.assertTrue((promoted / "files").is_dir())

    def test_manifest_json_is_authoritative_and_escapes_pipe_filename_for_markdown(self):
        self.write("docs/a|b.md", b"content\n")

        record = build_snapshot(
            self.config(key_paths=("docs/a|b.md",)),
            self.ref,
            self.repo,
            self.raw_root,
            self.staging_root,
            "2026-07-14",
        )

        manifest = (record.staging_path / "snapshot.md").read_text(encoding="utf-8")
        self.assertEqual("docs/a|b.md", self.manifest_metadata(record)["files"][0]["path"])
        self.assertIn("docs/a\\|b.md", manifest)
        self.assertEqual([], validate_staged_snapshot(record))

    def test_validation_rejects_manifest_metadata_tampering(self):
        self.write("README.md", b"snapshot\n")
        record = build_snapshot(
            self.config(), self.ref, self.repo, self.raw_root, self.staging_root, "2026-07-14"
        )
        manifest_path = record.staging_path / "snapshot.md"
        manifest_path.write_text(
            manifest_path.read_text(encoding="utf-8").replace(self.ref.sha, "f" * len(self.ref.sha)),
            encoding="utf-8",
        )

        errors = validate_staged_snapshot(record)

        self.assertTrue(any("metadata mismatch" in error for error in errors))

    def test_validation_requires_format_version_with_an_exact_integer_type(self):
        self.write("README.md", b"snapshot\n")
        record = build_snapshot(
            self.config(), self.ref, self.repo, self.raw_root, self.staging_root, "2026-07-14"
        )

        missing = self.manifest_metadata(record)
        missing.pop("format_version")
        self.write_manifest_metadata(record, missing)

        errors = validate_staged_snapshot(record)

        self.assertTrue(any("format_version" in error for error in errors))

        boolean = self.manifest_metadata(record)
        boolean["format_version"] = True
        self.write_manifest_metadata(record, boolean)

        errors = validate_staged_snapshot(record)

        self.assertTrue(any("format_version" in error for error in errors))

    def test_validation_rejects_malformed_or_duplicate_excluded_entries(self):
        self.write("README.md", b"snapshot\n")
        record = build_snapshot(
            self.config(key_paths=("missing.md",)),
            self.ref,
            self.repo,
            self.raw_root,
            self.staging_root,
            "2026-07-14",
        )

        malformed = self.manifest_metadata(record)
        malformed["excluded"] = [{"path": "missing.md", "reason": True}]
        self.write_manifest_metadata(record, malformed)

        errors = validate_staged_snapshot(record)

        self.assertTrue(any("excluded" in error and "malformed" in error for error in errors))

        record = build_snapshot(
            self.config(key_paths=("missing.md",)),
            self.ref,
            self.repo,
            self.raw_root,
            self.staging_root,
            "2026-07-14",
        )
        duplicate = self.manifest_metadata(record)
        duplicate["excluded"].append(dict(duplicate["excluded"][0]))
        self.write_manifest_metadata(record, duplicate)

        errors = validate_staged_snapshot(record)

        self.assertTrue(any("excluded entry listed more than once" in error for error in errors))

    def test_validation_rejects_boolean_sizes_and_wrong_identity_or_release_types(self):
        self.write("README.md", b"snapshot\n")
        evidence = ReleaseNotesEvidence(
            "https://api.github.test/release", "2026-07-14T00:00:00Z", b"notes\n"
        )
        cases = (
            (lambda metadata: metadata["files"][0].update(size=True), "saved file metadata"),
            (lambda metadata: metadata["release_notes"].update(size=True), "release notes metadata"),
            (lambda metadata: metadata["repository"].pop("id"), "repository.id"),
            (lambda metadata: metadata["ref"].update(sha=7), "ref.sha"),
            (lambda metadata: metadata["release_notes"].update(published_at=None), "release_notes"),
        )

        for mutate, expected in cases:
            with self.subTest(expected=expected):
                record = build_snapshot(
                    self.config(),
                    self.ref,
                    self.repo,
                    self.raw_root,
                    self.staging_root,
                    "2026-07-14",
                    release_notes=evidence,
                )
                metadata = self.manifest_metadata(record)
                mutate(metadata)
                self.write_manifest_metadata(record, metadata)

                errors = validate_staged_snapshot(record)

                self.assertTrue(any(expected in error for error in errors))

    def test_validation_rejects_unexpected_top_level_entries_and_diffs(self):
        self.write("README.md", b"snapshot\n")
        record = build_snapshot(
            self.config(), self.ref, self.repo, self.raw_root, self.staging_root, "2026-07-14"
        )
        (record.staging_path / "unexpected.txt").write_text("unexpected\n", encoding="utf-8")
        (record.staging_path / "files" / "generated.diff").write_text("diff\n", encoding="utf-8")

        errors = validate_staged_snapshot(record)

        self.assertTrue(any("unexpected top-level entry" in error for error in errors))
        self.assertTrue(any(".diff" in error for error in errors))

    def test_validation_rejects_duplicate_metadata_and_tampered_release_notes(self):
        evidence = ReleaseNotesEvidence("https://api.github.test/release", "2026-07-14T00:00:00Z", b"notes\n")
        self.write("README.md", b"snapshot\n")
        record = build_snapshot(
            self.config(),
            self.ref,
            self.repo,
            self.raw_root,
            self.staging_root,
            "2026-07-14",
            release_notes=evidence,
        )
        (record.staging_path / "release-notes.md").write_bytes(b"changed\n")
        manifest_path = record.staging_path / "snapshot.md"
        metadata = self.manifest_metadata(record)
        metadata["files"].append(metadata["files"][0])
        manifest_path.write_text(
            manifest_path.read_text(encoding="utf-8").replace(
                json.dumps(self.manifest_metadata(record), indent=2, sort_keys=True),
                json.dumps(metadata, indent=2, sort_keys=True),
            ),
            encoding="utf-8",
        )

        errors = validate_staged_snapshot(record)

        self.assertTrue(any("listed more than once" in error for error in errors))
        self.assertTrue(any("release notes hash mismatch" in error for error in errors))

    def test_validation_rejects_release_note_bytes_and_manifest_changed_together(self):
        evidence = ReleaseNotesEvidence(
            "https://api.github.test/release", "2026-07-14T00:00:00Z", b"notes\n"
        )
        self.write("README.md", b"snapshot\n")
        record = build_snapshot(
            self.config(),
            self.ref,
            self.repo,
            self.raw_root,
            self.staging_root,
            "2026-07-14",
            release_notes=evidence,
        )
        changed = b"attacker-controlled notes\n"
        (record.staging_path / "release-notes.md").write_bytes(changed)
        metadata = self.manifest_metadata(record)
        metadata["release_notes"]["sha256"] = hashlib.sha256(changed).hexdigest()
        metadata["release_notes"]["size"] = len(changed)
        self.write_manifest_metadata(record, metadata)

        errors = validate_staged_snapshot(record)

        self.assertTrue(any("release_notes.sha256" in error for error in errors))
        self.assertTrue(any("release_notes.size" in error for error in errors))

    def test_build_enforces_limits_against_copied_bytes(self):
        self.write("README.md", b"small\n")
        original_select = github_snapshot.select_key_files

        def select_then_grow(*args, **kwargs):
            selection = original_select(*args, **kwargs)
            self.write("README.md", b"x" * 9)
            return selection

        with mock.patch("github_snapshot.select_key_files", side_effect=select_then_grow):
            with self.assertRaisesRegex(SnapshotError, "per-file byte limit"):
                build_snapshot(
                    self.config(max_file_bytes=8),
                    self.ref,
                    self.repo,
                    self.raw_root,
                    self.staging_root,
                    "2026-07-14",
                )
        self.assertEqual([], list(self.staging_root.glob("snapshot-*")))

    def test_build_rejects_selected_file_swapped_to_outside_symlink(self):
        self.write("README.md", b"checkout evidence\n")
        outside = self.root / "outside.txt"
        outside.write_bytes(b"outside evidence\n")
        original_select = github_snapshot.select_key_files

        def select_then_swap(*args, **kwargs):
            selection = original_select(*args, **kwargs)
            (self.repo / "README.md").unlink()
            (self.repo / "README.md").symlink_to(outside)
            return selection

        with mock.patch("github_snapshot.select_key_files", side_effect=select_then_swap):
            with self.assertRaisesRegex(SnapshotError, "contained|symlink|no-follow"):
                build_snapshot(
                    self.config(), self.ref, self.repo, self.raw_root, self.staging_root, "2026-07-14"
                )

        self.assertEqual([], list(self.staging_root.glob("snapshot-*")))

    def test_selection_rejects_leaf_swap_after_containment_before_reading_outside_bytes(self):
        self.write("README.md", b"checkout evidence\n")
        outside = self.root / "outside.txt"
        outside.write_bytes(b"outside evidence\n")
        original_exclusion = github_snapshot._exclusion_reason

        def swap_after_containment(*args, **kwargs):
            (self.repo / "README.md").unlink()
            (self.repo / "README.md").symlink_to(outside)
            return original_exclusion(*args, **kwargs)

        with mock.patch("github_snapshot._exclusion_reason", side_effect=swap_after_containment):
            result = select_key_files(self.config(), self.repo)

        self.assertEqual((), result.selected)
        self.assertTrue(any(path == "README.md" for path, _ in result.excluded))

    def test_selection_rejects_parent_swap_after_containment_before_reading_outside_bytes(self):
        self.write("docs/README.md", b"checkout evidence\n")
        outside = self.root / "outside"
        outside.mkdir()
        (outside / "README.md").write_bytes(b"outside evidence\n")
        original_exclusion = github_snapshot._exclusion_reason

        def swap_parent_after_containment(*args, **kwargs):
            docs = self.repo / "docs"
            docs.rename(self.repo / "docs-original")
            docs.symlink_to(outside, target_is_directory=True)
            return original_exclusion(*args, **kwargs)

        with mock.patch("github_snapshot._exclusion_reason", side_effect=swap_parent_after_containment):
            result = select_key_files(self.config(), self.repo)

        self.assertEqual((), result.selected)
        self.assertTrue(any(path == "docs/README.md" for path, _ in result.excluded))

    def test_promotion_rejects_staging_path_swapped_after_validation(self):
        self.write("README.md", b"snapshot\n")
        record = build_snapshot(
            self.config(), self.ref, self.repo, self.raw_root, self.staging_root, "2026-07-14"
        )
        original_staging = record.staging_path.with_name(record.staging_path.name + "-original")
        outside_staging = self.root / "outside-staging"
        shutil.copytree(record.staging_path, outside_staging)
        original_validate = github_snapshot.validate_staged_snapshot

        def validate_then_swap(active_record):
            errors = original_validate(active_record)
            active_record.staging_path.rename(original_staging)
            active_record.staging_path.symlink_to(outside_staging, target_is_directory=True)
            return errors

        with mock.patch("github_snapshot.validate_staged_snapshot", side_effect=validate_then_swap):
            with self.assertRaisesRegex(SnapshotError, "staged directory"):
                promote_snapshot(record)

        self.assertTrue(record.staging_path.is_symlink())
        self.assertTrue(original_staging.is_dir())
        self.assertFalse(record.target_path.exists())

    def test_validation_rejects_repository_provenance_tampering(self):
        self.write("README.md", b"snapshot\n")
        replacements = (
            ('"url": "https://github.com/paypal/paypal-js"', '"url": "https://github.com/attacker/repo"', "repository.url"),
            ('"company": "paypal"', '"company": "attacker"', "repository.company"),
            ('"type": "web-sdk"', '"type": "malicious-sdk"', "repository.type"),
        )

        for original, tampered, field in replacements:
            with self.subTest(field=field):
                record = build_snapshot(
                    self.config(), self.ref, self.repo, self.raw_root, self.staging_root, "2026-07-14"
                )
                manifest_path = record.staging_path / "snapshot.md"
                manifest_path.write_text(
                    manifest_path.read_text(encoding="utf-8").replace(original, tampered, 1),
                    encoding="utf-8",
                )

                errors = validate_staged_snapshot(record)

                self.assertTrue(any("metadata mismatch for " + field in error for error in errors))

    def test_validation_rejects_release_note_provenance_tampering(self):
        self.write("README.md", b"snapshot\n")
        evidence = ReleaseNotesEvidence(
            "https://api.github.test/release", "2026-07-14T00:00:00Z", b"notes\n"
        )
        replacements = (
            ('"source_url": "https://api.github.test/release"', '"source_url": "https://attacker.test/release"', "release_notes.source_url"),
            ('"published_at": "2026-07-14T00:00:00Z"', '"published_at": "2020-01-01T00:00:00Z"', "release_notes.published_at"),
        )

        for original, tampered, field in replacements:
            with self.subTest(field=field):
                record = build_snapshot(
                    self.config(),
                    self.ref,
                    self.repo,
                    self.raw_root,
                    self.staging_root,
                    "2026-07-14",
                    release_notes=evidence,
                )
                manifest_path = record.staging_path / "snapshot.md"
                manifest_path.write_text(
                    manifest_path.read_text(encoding="utf-8").replace(original, tampered, 1),
                    encoding="utf-8",
                )

                errors = validate_staged_snapshot(record)

                self.assertTrue(any("metadata mismatch for " + field in error for error in errors))

    def test_stable_lock_is_retained_and_reused_after_success(self):
        self.write("README.md", b"snapshot\n")
        record = build_snapshot(
            self.config(), self.ref, self.repo, self.raw_root, self.staging_root, "2026-07-14"
        )

        promoted = promote_snapshot(record)
        lock = self.promotion_lock(record)
        recollection = build_snapshot(
            self.config(), self.ref, self.repo, self.raw_root, self.staging_root, "2026-07-14"
        )

        self.assertTrue(lock.is_file())
        self.assertFalse(lock.is_symlink())
        self.assertEqual(promoted, promote_snapshot(recollection))
        self.assertTrue(lock.exists())

    def test_promotion_rejects_lock_file_symlink_and_cleans_staging(self):
        self.write("README.md", b"snapshot\n")
        record = build_snapshot(
            self.config(), self.ref, self.repo, self.raw_root, self.staging_root, "2026-07-14"
        )
        lock = self.promotion_lock(record)
        outside = self.root / "outside-lock"
        outside.write_text("foreign", encoding="utf-8")
        lock.parent.mkdir(parents=True)
        lock.symlink_to(outside)

        with self.assertRaisesRegex(SnapshotError, "lock file.*symlink"):
            promote_snapshot(record)

        self.assertTrue(lock.is_symlink())
        self.assertEqual("foreign", outside.read_text(encoding="utf-8"))
        self.assertFalse(record.staging_path.exists())

    def test_lock_contention_preserves_stable_lock_and_cleans_staging(self):
        self.write("README.md", b"snapshot\n")
        record = build_snapshot(
            self.config(), self.ref, self.repo, self.raw_root, self.staging_root, "2026-07-14"
        )
        lock = self.promotion_lock(record)
        lock.parent.mkdir(parents=True)
        descriptor = os.open(str(lock), os.O_RDWR | os.O_CREAT, 0o600)
        fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
        try:
            with self.assertRaisesRegex(SnapshotError, "promotion lock is already held"):
                promote_snapshot(record)
        finally:
            fcntl.flock(descriptor, fcntl.LOCK_UN)
            os.close(descriptor)

        self.assertTrue(lock.exists())
        self.assertFalse(record.staging_path.exists())

    def test_promotion_rejects_group_writable_staging_parent(self):
        self.write("README.md", b"snapshot\n")
        record = build_snapshot(
            self.config(), self.ref, self.repo, self.raw_root, self.staging_root, "2026-07-14"
        )
        record.staging_path.parent.chmod(0o770)
        try:
            with self.assertRaisesRegex(SnapshotError, "staging parent is not collector-private"):
                promote_snapshot(record)
        finally:
            record.staging_path.parent.chmod(0o700)

        self.assertFalse(record.staging_path.exists())

    def test_promotion_rejects_world_writable_snapshot_parent(self):
        self.write("README.md", b"snapshot\n")
        record = build_snapshot(
            self.config(), self.ref, self.repo, self.raw_root, self.staging_root, "2026-07-14"
        )
        record.target_path.parent.mkdir(parents=True)
        record.target_path.parent.chmod(0o777)
        try:
            with self.assertRaisesRegex(SnapshotError, "snapshot parent is not collector-private"):
                promote_snapshot(record)
        finally:
            record.target_path.parent.chmod(0o700)

        self.assertFalse(record.staging_path.exists())

    def test_concurrent_supplements_allocate_distinct_revisions_while_locked(self):
        self.write("README.md", b"snapshot\n")
        first = build_snapshot(
            self.config(),
            self.ref,
            self.repo,
            self.raw_root,
            self.staging_root,
            "2026-07-14",
            capture_kind="supplement",
        )
        second = build_snapshot(
            self.config(),
            self.ref,
            self.repo,
            self.raw_root,
            self.staging_root,
            "2026-07-14",
            capture_kind="supplement",
        )

        first_path = promote_snapshot(first)
        second_path = promote_snapshot(second)

        self.assertTrue(first_path.name.endswith("-r1"))
        self.assertTrue(second_path.name.endswith("-r2"))
        second_manifest = (second_path / "snapshot.md").read_text(encoding="utf-8")
        self.assertIn('"capture_revision": 2', second_manifest)

    def test_failed_validation_or_target_collision_cleans_current_staging_and_keeps_lock(self):
        self.write("README.md", b"snapshot\n")
        invalid = build_snapshot(
            self.config(), self.ref, self.repo, self.raw_root, self.staging_root, "2026-07-14"
        )
        (invalid.staging_path / "files" / "README.md").write_bytes(b"tampered\n")

        with self.assertRaisesRegex(SnapshotError, "invalid staged snapshot"):
            promote_snapshot(invalid)

        self.assertFalse(invalid.staging_path.exists())
        self.assertTrue(self.promotion_lock(invalid).exists())

        collision = build_snapshot(
            self.config(), self.ref, self.repo, self.raw_root, self.staging_root, "2026-07-14"
        )
        collision.target_path.mkdir(parents=True)
        with self.assertRaisesRegex(SnapshotError, "target already exists"):
            promote_snapshot(collision)
        self.assertFalse(collision.staging_path.exists())

    def test_stable_lock_is_reusable_after_failed_promotion(self):
        self.write("README.md", b"snapshot\n")
        invalid = build_snapshot(
            self.config(), self.ref, self.repo, self.raw_root, self.staging_root, "2026-07-14"
        )
        (invalid.staging_path / "files" / "README.md").write_bytes(b"tampered\n")

        with self.assertRaisesRegex(SnapshotError, "invalid staged snapshot"):
            promote_snapshot(invalid)

        retry = build_snapshot(
            self.config(), self.ref, self.repo, self.raw_root, self.staging_root, "2026-07-14"
        )

        self.assertEqual(retry.target_path, promote_snapshot(retry))
        self.assertTrue(self.promotion_lock(retry).is_file())

    def test_descriptor_relative_replace_failure_cleans_current_staging_and_keeps_lock(self):
        self.write("README.md", b"snapshot\n")
        record = build_snapshot(
            self.config(), self.ref, self.repo, self.raw_root, self.staging_root, "2026-07-14"
        )

        with mock.patch("github_snapshot.os.replace", side_effect=OSError("cross-device failure")):
            with self.assertRaisesRegex(SnapshotError, "could not promote snapshot"):
                promote_snapshot(record)

        self.assertFalse(record.staging_path.exists())
        self.assertTrue(self.promotion_lock(record).exists())

    def test_promotion_rejects_staged_identity_mismatch_without_removing_replacement(self):
        self.write("README.md", b"snapshot\n")
        record = build_snapshot(
            self.config(), self.ref, self.repo, self.raw_root, self.staging_root, "2026-07-14"
        )
        replacement = replace(record, staging_inode=record.staging_inode + 1)

        with self.assertRaisesRegex(SnapshotError, "staged directory"):
            promote_snapshot(replacement)

        self.assertTrue(record.staging_path.exists())
        self.assertFalse(record.target_path.exists())


if __name__ == "__main__":
    unittest.main()
