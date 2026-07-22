import json
import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from github_capsule_policy import CapsuleConfig  # noqa: E402
from github_capsule_selection import resolve_npm_capsule  # noqa: E402
from github_git_tree import GitTree  # noqa: E402
from github_pilot_store import (  # noqa: E402
    PilotStoreError,
    publish_release_record,
    publish_source_snapshot,
    write_package_comparison,
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


if __name__ == "__main__":
    unittest.main()
