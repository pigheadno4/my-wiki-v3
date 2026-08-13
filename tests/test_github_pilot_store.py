import json
import subprocess
import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from github_capsule_policy import CapsuleConfig  # noqa: E402
from github_capsule_selection import resolve_npm_capsule  # noqa: E402
from github_canonical import canonical_json_bytes  # noqa: E402
from github_git_tree import GitTree  # noqa: E402
import github_pilot_store  # noqa: E402
from github_pilot_store import (  # noqa: E402
    PilotStoreError,
    UpstreamChange,
    publish_release_record,
    publish_source_snapshot,
    publish_source_supplement,
    read_upstream_changes,
    write_package_comparison,
    write_ref_comparison,
)
from github_registry import RepoConfig  # noqa: E402
from github_releases import ReleaseCandidate, ReleaseNotesEvidence  # noqa: E402
from tests.github_test_support import commit_files, create_git_repo  # noqa: E402


def package_manifest(version):
    return json.dumps(
        {
            "name": "@scope/widget",
            "version": version,
            "main": "./src/index.ts",
        },
        sort_keys=True,
    ) + "\n"


class GitHubPilotStoreTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        repository_root = self.root / "repository"
        repository_root.mkdir()
        self.repo = create_git_repo(repository_root)
        self.sha = commit_files(
            self.repo,
            {
                "README.md": "# Widget\n",
                "LICENSE": "Apache-2.0\n",
                "package.json": package_manifest("10.0.0"),
                "src/index.ts": "export const value = 1;\n",
            },
            "initial release",
        )
        self.config = RepoConfig(
            id="acme/widgets",
            company="acme",
            url="https://github.com/acme/widgets",
            enabled=True,
            repo_type="sdk",
            priority="tier1",
            track="releases-and-default-branch",
            version_strategy="monorepo-packages",
            capsules=(self.capsule(),),
        )
        self.tree = GitTree(self.repo, self.sha)
        self.resolution = resolve_npm_capsule(self.tree, self.capsule(), ())
        self.candidate = ReleaseCandidate(
            package="@scope/widget",
            version="10.0.0",
            tag="@scope/widget@10.0.0",
            object_sha=self.sha,
            commit_sha=self.sha,
            prerelease=False,
        )
        self.evidence = ReleaseNotesEvidence(
            "https://api.github.test/releases/1",
            "2026-07-07T12:00:00Z",
            b"original release notes\n",
        )

    def capsule(self):
        return CapsuleConfig(
            id="widget-source",
            adapter="npm-tracked-source-v1",
            focus_packages=("@scope/widget",),
            default_required_roots=("src",),
            default_generated_target_paths=(),
        )

    def commit_config(self):
        return RepoConfig(
            id="paypal-examples/v6-web-sdk-sample-integration",
            company="paypal",
            url="https://github.com/paypal-examples/v6-web-sdk-sample-integration",
            enabled=True,
            repo_type="sample-app",
            priority="tier1",
            track="default-branch",
            version_strategy="commit",
            capsules=(
                CapsuleConfig(
                    id="paypal-v6-sample-source",
                    adapter="commit-tree-v1",
                    source_id="v6-web-sdk-sample-integration",
                    dependency_scope="configured-repository-paths",
                    changed_path_policy="policy-bounded",
                    default_required_roots=("client", "server"),
                    max_packet_files=30,
                    max_packet_utf8_bytes=200000,
                ),
            ),
        )

    def tagged_config(self):
        return RepoConfig(
            id="paypal/paypal-messages-ios",
            company="paypal",
            url="https://github.com/paypal/paypal-messages-ios",
            enabled=True,
            repo_type="messaging-sdk",
            priority="tier2",
            track="releases-and-default-branch",
            version_strategy="semver-tags",
            capsules=(
                CapsuleConfig(
                    id="paypal-messages-ios-public-source",
                    adapter="tagged-tree-v1",
                    focus_packages=("paypal-messages-ios",),
                    dependency_scope="configured-repository-paths",
                    changed_path_policy="policy-bounded",
                    default_required_roots=("src",),
                    include_paths=("README.md",),
                    max_packet_files=30,
                    max_packet_utf8_bytes=200000,
                ),
            ),
        )

    def test_same_sha_reuses_one_source_snapshot(self):
        first = publish_source_snapshot(
            self.root,
            self.config,
            self.tree,
            self.resolution,
            "2026-07-20",
            ("@scope/widget@10.0.0",),
        )
        second = publish_source_snapshot(
            self.root,
            self.config,
            self.tree,
            self.resolution,
            "2026-07-21",
            ("@scope/other@10.1.0",),
        )

        self.assertEqual(first.directory, second.directory)
        self.assertEqual(
            first.manifest_path.read_bytes(), second.manifest_path.read_bytes()
        )
        self.assertIn("README.md", first.files)
        self.assertIn("LICENSE", first.files)
        self.assertIn("src/index.ts", first.files)
        manifest = json.loads(first.manifest_path.read_text(encoding="utf-8"))
        self.assertEqual(2, manifest["format_version"])
        self.assertTrue(manifest["author_date"])
        self.assertTrue(manifest["commit_date"])

    def test_root_package_lock_is_not_standard_snapshot_context(self):
        sha = commit_files(
            self.repo,
            {"package-lock.json": "x" * (self.config.max_file_bytes + 1)},
            "add oversized lockfile",
        )
        tree = GitTree(self.repo, sha)
        resolution = resolve_npm_capsule(tree, self.capsule(), ())

        snapshot = publish_source_snapshot(
            self.root,
            self.config,
            tree,
            resolution,
            "2026-07-20",
            ("@scope/widget@10.0.0",),
        )

        self.assertNotIn("package-lock.json", snapshot.files)
        self.assertIn("package.json", snapshot.files)
        self.assertIn("src/index.ts", snapshot.files)

    def test_same_release_note_hash_is_idempotent(self):
        first = publish_release_record(
            self.root,
            self.config,
            self.candidate,
            "2026-07-07T12:00:00Z",
            self.evidence,
            "2026-07-20",
        )
        second = publish_release_record(
            self.root,
            self.config,
            self.candidate,
            "2026-07-07T12:00:00Z",
            self.evidence,
            "2026-07-21",
        )

        self.assertEqual(first.directory, second.directory)

    def test_changed_release_notes_create_an_immutable_revision(self):
        first = publish_release_record(
            self.root,
            self.config,
            self.candidate,
            "2026-07-07T12:00:00Z",
            self.evidence,
            "2026-07-20",
        )
        revised = replace(self.evidence, content=b"corrected release notes\n")
        second = publish_release_record(
            self.root,
            self.config,
            self.candidate,
            "2026-07-07T12:00:00Z",
            revised,
            "2026-07-21",
        )

        self.assertNotEqual(first.directory, second.directory)
        self.assertEqual(b"original release notes\n", first.notes_path.read_bytes())
        self.assertEqual(b"corrected release notes\n", second.notes_path.read_bytes())

    def test_release_notes_are_secret_scanned_before_publication(self):
        secret = replace(
            self.evidence,
            content=("sk_live_" + ("a" * 24) + "\n").encode("utf-8"),
        )

        with self.assertRaisesRegex(ValueError, "secret-finding"):
            publish_release_record(
                self.root,
                self.config,
                self.candidate,
                "2026-07-07T12:00:00Z",
                secret,
                "2026-07-20",
            )

        self.assertFalse(
            (self.root / "raw/github/acme/widgets/releases").exists()
        )

    def test_failed_snapshot_validation_publishes_no_partial_directory(self):
        invalid = replace(
            self.resolution,
            files=(replace(self.resolution.files[0], sha256="0" * 64),),
        )

        with self.assertRaises(PilotStoreError):
            publish_source_snapshot(
                self.root,
                self.config,
                self.tree,
                invalid,
                "2026-07-20",
                ("@scope/widget@10.0.0",),
            )

        snapshots = self.root / "raw/github/acme/widgets/snapshots"
        self.assertEqual([], list(snapshots.iterdir()) if snapshots.exists() else [])

    def test_repository_context_file_count_overflow_requires_policy_review(self):
        capsule = replace(self.capsule(), max_capsule_files=3)
        config = replace(self.config, capsules=(capsule,))
        resolution = resolve_npm_capsule(self.tree, capsule, ())

        with self.assertRaisesRegex(
            PilotStoreError,
            (
                r"^needs-policy-review:capsule-budget-exceeded: "
                r"published file count 4 exceeds max_capsule_files 3$"
            ),
        ):
            publish_source_snapshot(
                self.root,
                config,
                self.tree,
                resolution,
                "2026-07-20",
                ("@scope/widget@10.0.0",),
            )

        snapshots = self.root / "raw/github/acme/widgets/snapshots"
        self.assertEqual([], list(snapshots.iterdir()) if snapshots.exists() else [])

    def test_repository_context_byte_overflow_requires_policy_review(self):
        selected_bytes = len(package_manifest("10.0.0").encode("utf-8")) + len(
            b"export const value = 1;\n"
        )
        context_bytes = len(b"# Widget\n") + len(b"Apache-2.0\n")
        capsule = replace(
            self.capsule(),
            max_capsule_utf8_bytes=selected_bytes + context_bytes - 1,
        )
        config = replace(self.config, capsules=(capsule,))
        resolution = resolve_npm_capsule(self.tree, capsule, ())

        with self.assertRaisesRegex(
            PilotStoreError,
            (
                r"^needs-policy-review:capsule-budget-exceeded: "
                r"published UTF-8 bytes "
                + str(selected_bytes + context_bytes)
                + r" exceeds max_capsule_utf8_bytes "
                + str(selected_bytes + context_bytes - 1)
                + r"$"
            ),
        ):
            publish_source_snapshot(
                self.root,
                config,
                self.tree,
                resolution,
                "2026-07-20",
                ("@scope/widget@10.0.0",),
            )

        snapshots = self.root / "raw/github/acme/widgets/snapshots"
        self.assertEqual([], list(snapshots.iterdir()) if snapshots.exists() else [])

    def test_publication_rejects_repository_root_symlink_escape(self):
        outside = self.root / "outside"
        outside.mkdir()
        company_root = self.root / "raw/github/acme"
        company_root.mkdir(parents=True)
        (company_root / "widgets").symlink_to(outside, target_is_directory=True)

        with self.assertRaisesRegex(PilotStoreError, "repository storage path"):
            publish_source_snapshot(
                self.root,
                self.config,
                self.tree,
                self.resolution,
                "2026-07-20",
                ("@scope/widget@10.0.0",),
            )

        self.assertEqual([], list(outside.iterdir()))

    def test_exact_sha_supplement_is_immutable_and_idempotent(self):
        first = publish_source_supplement(
            self.root,
            self.config,
            self.tree,
            ("src/index.ts",),
            "2026-07-20",
        )
        second = publish_source_supplement(
            self.root,
            self.config,
            self.tree,
            ("src/index.ts",),
            "2026-07-21",
        )

        self.assertEqual(first.directory, second.directory)
        self.assertEqual(("src/index.ts",), first.files)
        self.assertEqual(
            b"export const value = 1;\n",
            (first.directory / "files/src/index.ts").read_bytes(),
        )

    def test_comparison_is_scoped_to_the_requested_package_paths(self):
        next_sha = commit_files(
            self.repo,
            {
                "src/index.ts": "export const value = 2;\n",
                "unrelated.txt": "do not include\n",
            },
            "patch release",
        )

        record = write_package_comparison(
            self.root,
            self.config,
            self.repo,
            "@scope/widget",
            "10.0.0",
            self.sha,
            ("src",),
            "10.0.1",
            next_sha,
            ("src",),
        )

        self.assertEqual(("src/index.ts",), record.changed_paths)
        self.assertIn("src/index.ts", record.patch_path.read_text(encoding="utf-8"))
        self.assertNotIn("unrelated.txt", record.patch_path.read_text(encoding="utf-8"))
        metadata = json.loads(record.metadata_path.read_text(encoding="utf-8"))
        self.assertEqual(self.sha, metadata["from_sha"])
        self.assertEqual(next_sha, metadata["to_sha"])

    def test_comparison_persists_added_modified_deleted_and_renamed_paths(self):
        commit_files(
            self.repo,
            {
                "docs/old.md": "old documentation\n",
                "src/old.ts": "export const renamed = true;\n",
            },
            "add comparison fixtures",
        )
        from_sha = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=self.repo,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        (self.repo / "docs/old.md").unlink()
        (self.repo / "src/old.ts").rename(self.repo / "src/new.ts")
        (self.repo / "src/index.ts").write_text(
            "export const value = 2;\n", encoding="utf-8"
        )
        (self.repo / "src/new.stories.js").write_text(
            "export default {};\n", encoding="utf-8"
        )
        subprocess.run(
            ["git", "add", "-A"],
            cwd=self.repo,
            check=True,
            capture_output=True,
        )
        subprocess.run(
            ["git", "commit", "-m", "exercise comparison statuses"],
            cwd=self.repo,
            check=True,
            capture_output=True,
        )
        to_sha = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=self.repo,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()

        record = write_package_comparison(
            self.root,
            self.config,
            self.repo,
            "@scope/widget",
            "10.0.0",
            from_sha,
            ("docs", "src"),
            "10.0.1",
            to_sha,
            ("docs", "src"),
        )

        self.assertEqual(
            (
                UpstreamChange("deleted", "docs/old.md", ""),
                UpstreamChange("modified", "src/index.ts", "src/index.ts"),
                UpstreamChange("added", "", "src/new.stories.js"),
                UpstreamChange("renamed", "src/old.ts", "src/new.ts"),
            ),
            record.upstream_changes,
        )
        self.assertEqual(
            (
                "docs/old.md",
                "src/index.ts",
                "src/new.stories.js",
                "src/new.ts",
                "src/old.ts",
            ),
            record.changed_paths,
        )
        metadata = json.loads(record.metadata_path.read_text(encoding="utf-8"))
        self.assertEqual(2, metadata["format_version"])
        self.assertEqual(
            [
                {"new_path": "", "old_path": "docs/old.md", "status": "deleted"},
                {
                    "new_path": "src/index.ts",
                    "old_path": "src/index.ts",
                    "status": "modified",
                },
                {
                    "new_path": "src/new.stories.js",
                    "old_path": "",
                    "status": "added",
                },
                {
                    "new_path": "src/new.ts",
                    "old_path": "src/old.ts",
                    "status": "renamed",
                },
            ],
            metadata["upstream_changes"],
        )

    def test_ref_comparison_is_commit_qualified_idempotent_and_conflict_safe(self):
        from_sha = commit_files(
            self.repo,
            {
                "client/checkout.ts": "export const checkout = 1;\n",
                "client/old.ts": "export const renamed = true;\n",
                "server/deleted.ts": "export const removed = true;\n",
                "tests/excluded.test.ts": "old test\n",
            },
            "add commit comparison fixture",
        )
        (self.repo / "client/old.ts").rename(self.repo / "client/new.ts")
        (self.repo / "server/deleted.ts").unlink()
        (self.repo / "client/checkout.ts").write_text(
            "export const checkout = 2;\n", encoding="utf-8"
        )
        (self.repo / "client/added.ts").write_text(
            "export const added = true;\n", encoding="utf-8"
        )
        (self.repo / "tests/excluded.test.ts").write_text(
            "new test\n", encoding="utf-8"
        )
        subprocess.run(["git", "add", "-A"], cwd=self.repo, check=True, capture_output=True)
        subprocess.run(
            ["git", "commit", "-m", "change selected commit evidence"],
            cwd=self.repo,
            check=True,
            capture_output=True,
        )
        to_sha = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=self.repo,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.strip()
        selected_from = ("client/checkout.ts", "client/old.ts", "server/deleted.ts")
        selected_to = ("client/added.ts", "client/checkout.ts", "client/new.ts")

        first = write_ref_comparison(
            self.root,
            self.commit_config(),
            self.repo,
            "main",
            from_sha,
            selected_from,
            to_sha,
            selected_to,
        )
        first_bytes = tuple(
            path.read_bytes()
            for path in (first.patch_path, first.metadata_path, first.markdown_path)
        )
        second = write_ref_comparison(
            self.root,
            self.commit_config(),
            self.repo,
            "main",
            from_sha,
            selected_from,
            to_sha,
            selected_to,
        )
        metadata = json.loads(first.metadata_path.read_text(encoding="utf-8"))

        self.assertEqual("default-branch", metadata["ref_kind"])
        self.assertEqual("main", metadata["ref_name"])
        self.assertNotIn("package", metadata)
        self.assertNotIn("from_version", metadata)
        self.assertNotIn("tests/excluded.test.ts", metadata["changed_paths"])
        self.assertEqual(first.metadata_path.parent, second.metadata_path.parent)
        self.assertEqual(
            first_bytes,
            tuple(path.read_bytes() for path in (second.patch_path, second.metadata_path, second.markdown_path)),
        )
        self.assertIn(
            "comparisons/default-branch/" + from_sha[:7] + "--" + to_sha[:7],
            first.metadata_path.as_posix(),
        )

        metadata["ref_name"] = "trunk"
        write_canonical = canonical_json_bytes(metadata) + b"\n"
        first.metadata_path.write_bytes(write_canonical)
        with self.assertRaisesRegex(PilotStoreError, "conflicts"):
            write_ref_comparison(
                self.root,
                self.commit_config(),
                self.repo,
                "main",
                from_sha,
                selected_from,
                to_sha,
                selected_to,
            )

    def test_ref_comparison_accepts_tagged_tree_capsule(self):
        from_sha = commit_files(
            self.repo,
            {"README.md": "# Before\n", "src/message.swift": "let value = 1\n"},
            "add tagged boundary fixture",
        )
        to_sha = commit_files(
            self.repo,
            {"README.md": "# After\n"},
            "change tagged boundary documentation",
        )

        comparison = write_ref_comparison(
            self.root,
            self.tagged_config(),
            self.repo,
            "develop",
            from_sha,
            ("README.md", "src/message.swift"),
            to_sha,
            ("README.md", "src/message.swift"),
        )

        self.assertTrue(comparison.metadata_path.is_file())
        self.assertTrue(comparison.markdown_path.is_file())
        self.assertTrue(comparison.patch_path.is_file())
        self.assertEqual(
            "paypal-messages-ios",
            github_pilot_store._ref_evidence_owner(
                self.tagged_config().capsules[0]
            ),
        )
        self.assertNotIn("/releases/", comparison.metadata_path.as_posix())

    def test_comparison_accepts_zero_padded_rename_similarity(self):
        output = (
            b"R090\0"
            b"packages/widget/src/old.ts\0"
            b"packages/widget/src/new.ts\0"
        )

        with mock.patch(
            "github_pilot_store._run_git_bytes",
            return_value=output,
        ):
            changes = read_upstream_changes(
                self.repo,
                "a" * 40,
                "b" * 40,
                ("packages/widget",),
            )

        self.assertEqual(
            (
                UpstreamChange(
                    "renamed",
                    "packages/widget/src/old.ts",
                    "packages/widget/src/new.ts",
                ),
            ),
            changes,
        )

    def test_comparison_reuses_immutable_legacy_v1_evidence(self):
        next_sha = commit_files(
            self.repo,
            {"src/index.ts": "export const value = 2;\n"},
            "patch release",
        )
        first = write_package_comparison(
            self.root,
            self.config,
            self.repo,
            "@scope/widget",
            "10.0.0",
            self.sha,
            ("src",),
            "10.0.1",
            next_sha,
            ("src",),
        )
        legacy = json.loads(first.metadata_path.read_text(encoding="utf-8"))
        legacy["format_version"] = 1
        legacy.pop("upstream_changes")
        first.metadata_path.write_bytes(canonical_json_bytes(legacy) + b"\n")
        legacy_bytes = first.metadata_path.read_bytes()

        reused = write_package_comparison(
            self.root,
            self.config,
            self.repo,
            "@scope/widget",
            "10.0.0",
            self.sha,
            ("src",),
            "10.0.1",
            next_sha,
            ("src",),
        )

        self.assertEqual(legacy_bytes, reused.metadata_path.read_bytes())
        self.assertEqual(
            (UpstreamChange("modified", "src/index.ts", "src/index.ts"),),
            reused.upstream_changes,
        )

    def test_comparison_enforces_packet_path_and_byte_budgets(self):
        next_sha = commit_files(
            self.repo,
            {
                "src/index.ts": "export const value = '" + ("x" * 200) + "';\n",
                "src/other.ts": "export const other = 2;\n",
            },
            "large comparison",
        )
        constrained = replace(
            self.config,
            capsules=(
                replace(
                    self.capsule(),
                    max_packet_files=1,
                    max_packet_utf8_bytes=64,
                ),
            ),
        )

        with self.assertRaisesRegex(PilotStoreError, "comparison exceeds"):
            write_package_comparison(
                self.root,
                constrained,
                self.repo,
                "@scope/widget",
                "10.0.0",
                self.sha,
                ("src",),
                "10.0.1",
                next_sha,
                ("src",),
            )

    def test_comparison_publication_failure_leaves_no_partial_directory(self):
        next_sha = commit_files(
            self.repo,
            {"src/index.ts": "export const value = 2;\n"},
            "patch release",
        )
        from github_pilot_store import _write_bytes_atomic

        calls = {"count": 0}

        def fail_second_write(path, content):
            calls["count"] += 1
            if calls["count"] == 2:
                raise OSError("disk full")
            return _write_bytes_atomic(path, content)

        with mock.patch(
            "github_pilot_store._write_bytes_atomic",
            side_effect=fail_second_write,
        ):
            with self.assertRaises(OSError):
                write_package_comparison(
                    self.root,
                    self.config,
                    self.repo,
                    "@scope/widget",
                    "10.0.0",
                    self.sha,
                    ("src",),
                    "10.0.1",
                    next_sha,
                    ("src",),
                )

        comparison = (
            self.root
            / "tracking/github/repos/acme/widgets/comparisons/widget/10.0.0--10.0.1"
        )
        self.assertFalse(comparison.exists())


if __name__ == "__main__":
    unittest.main()
