import hashlib
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from github_git import ResolvedRef  # noqa: E402
from github_registry import RepoConfig  # noqa: E402
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
                "| Repository URL | https://github.com/paypal/paypal-js |\n", ""
            ),
            encoding="utf-8",
        )

        errors = validate_staged_snapshot(record)

        self.assertTrue(any("missing required metadata: Repository URL" in error for error in errors))

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


if __name__ == "__main__":
    unittest.main()
