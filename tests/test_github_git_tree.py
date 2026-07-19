import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from github_git_tree import GitTree  # noqa: E402
from tests.github_test_support import (  # noqa: E402
    add_submodule_marker,
    commit_bytes,
    commit_file,
    commit_symlink,
    create_git_repo,
)


class GitTreeTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.repo = create_git_repo(self.root)
        commit_file(self.repo, "packages/widget/package.json", '{"name":"widget","version":"1.0.0"}\n', "add manifest")
        commit_bytes(self.repo, "src/cli.sh", b"#!/bin/sh\necho exact\n", "add executable", executable=True)
        commit_symlink(self.repo, "docs/current", "../README.md", "add symlink")
        commit_bytes(
            self.repo,
            "assets/lfs.bin",
            b"version https://git-lfs.github.com/spec/v1\noid sha256:abc\nsize 1\n",
            "add lfs pointer",
        )
        commit_bytes(self.repo, "assets/binary.bin", b"\xff\x00\x80", "add binary")
        commit_bytes(self.repo, "src/nul.txt", b"before\0after", "add nul bytes")
        add_submodule_marker(self.repo, "vendor/dependency")
        self.sha = self.git("rev-parse", "HEAD")

    def git(self, *args):
        from subprocess import run

        return run(
            ["git"] + list(args),
            cwd=str(self.repo),
            check=True,
            text=True,
            capture_output=True,
        ).stdout.strip()

    def test_blobs_enumerates_exact_tree_modes_and_sizes(self):
        blobs = {blob.path: blob for blob in GitTree(self.repo, self.sha).blobs()}

        self.assertEqual("100644", blobs["packages/widget/package.json"].mode)
        self.assertEqual("100755", blobs["src/cli.sh"].mode)
        self.assertEqual("120000", blobs["docs/current"].mode)
        self.assertEqual("160000", blobs["vendor/dependency"].mode)
        self.assertEqual(len(b"before\0after"), blobs["src/nul.txt"].size)
        self.assertEqual("blob", self.git("cat-file", "-t", blobs["assets/lfs.bin"].oid))
        self.assertEqual(b"\xff\x00\x80", GitTree(self.repo, self.sha).read_blob("assets/binary.bin"))
        self.assertEqual(b"before\0after", GitTree(self.repo, self.sha).read_blob("src/nul.txt"))

    def test_reads_committed_blob_bytes_not_dirty_worktree_bytes(self):
        committed = b'{"name":"widget","version":"1.0.0"}\n'
        (self.repo / "packages/widget/package.json").write_bytes(b'{"name":"dirty"}\n')

        content = GitTree(self.repo, self.sha).read_blob("packages/widget/package.json")

        self.assertEqual(committed, content)

    def test_uses_ls_tree_and_cat_file_with_the_exact_commit(self):
        tree = GitTree(self.repo, self.sha)

        with mock.patch("github_git_tree.subprocess.run", wraps=subprocess.run) as run:
            tree.blobs()
            tree.read_blob("packages/widget/package.json")

        commands = [tuple(call.args[0]) for call in run.call_args_list]
        self.assertIn(("git", "ls-tree", "-r", "-z", "--long", self.sha), commands)
        self.assertIn(
            ("git", "cat-file", "blob", self.sha + ":packages/widget/package.json"),
            commands,
        )

    def test_read_blob_rejects_unsafe_and_untracked_paths(self):
        tree = GitTree(self.repo, self.sha)

        for path in ("", "/etc/passwd", "src/../nul.txt", "src\\nul.txt", "missing.txt"):
            with self.subTest(path=path):
                with self.assertRaises(ValueError):
                    tree.read_blob(path)

    def test_read_blob_rejects_entries_above_the_configured_bound(self):
        tree = GitTree(self.repo, self.sha, max_blob_bytes=4)

        with self.assertRaisesRegex(ValueError, "byte limit"):
            tree.read_blob("src/cli.sh")

    def test_read_json_rejects_duplicate_keys_without_normalizing_bytes(self):
        duplicate_sha = commit_file(
            self.repo,
            "duplicate.json",
            '{"outer":{"first":1,"first":2}}',
            "add duplicate json",
        )

        with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
            GitTree(self.repo, duplicate_sha).read_json("duplicate.json")

    def test_read_json_reads_the_committed_object_when_the_worktree_is_dirty(self):
        committed = {"name": "widget", "version": "1.0.0"}
        (self.repo / "packages/widget/package.json").write_text('{"name":"dirty"}\n', encoding="utf-8")

        value = GitTree(self.repo, self.sha).read_json("packages/widget/package.json")

        self.assertEqual(committed, value)

    def test_constructor_requires_an_exact_object_id_and_positive_bound(self):
        for sha in ("HEAD", "main", "abc", "g" * 40):
            with self.subTest(sha=sha):
                with self.assertRaises(ValueError):
                    GitTree(self.repo, sha)
        with self.assertRaises(ValueError):
            GitTree(self.repo, self.sha, max_blob_bytes=0)

    def test_blobs_rejects_an_object_id_that_is_not_the_exact_commit(self):
        tree_sha = self.git("rev-parse", self.sha + "^{tree}")

        with self.assertRaisesRegex(ValueError, "exact commit"):
            GitTree(self.repo, tree_sha).blobs()


if __name__ == "__main__":
    unittest.main()
