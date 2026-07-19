import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import github_git_tree  # noqa: E402
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
        for call in run.call_args_list:
            self.assertEqual("1", call.kwargs["env"]["GIT_NO_REPLACE_OBJECTS"])

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

    def test_reads_the_named_commit_even_when_a_replace_ref_is_installed(self):
        first_sha = commit_bytes(self.repo, "replace-target.txt", b"first\n", "add first")
        commit_bytes(self.repo, "replace-target.txt", b"second\n", "add second")
        self.git("replace", first_sha, "HEAD")

        self.assertEqual(b"first\n", GitTree(self.repo, first_sha).read_blob("replace-target.txt"))

    def test_enumerates_unrelated_unsafe_paths_but_refuses_to_read_them(self):
        sha = commit_bytes(self.repo, "unrelated\\path.txt", b"ignored\n", "add unsafe path")
        tree = GitTree(self.repo, sha)

        self.assertIn("unrelated\\path.txt", {blob.path for blob in tree.blobs()})
        self.assertEqual(b'{"name":"widget","version":"1.0.0"}\n', tree.read_blob("packages/widget/package.json"))
        with self.assertRaisesRegex(ValueError, "safe repository-relative POSIX path"):
            tree.read_blob("unrelated\\path.txt")

    def test_read_json_rejects_non_finite_constants_with_bounded_errors(self):
        for constant in ("NaN", "Infinity", "-Infinity"):
            with self.subTest(constant=constant):
                sha = commit_bytes(self.repo, "constant.json", constant.encode("ascii"), "add " + constant)
                with self.assertRaisesRegex(ValueError, "invalid JSON constant") as raised:
                    GitTree(self.repo, sha).read_json("constant.json")
                self.assertLess(len(str(raised.exception)), 200)

    def test_read_json_rejects_invalid_utf8_with_a_bounded_error(self):
        sha = commit_bytes(self.repo, "invalid-utf8.json", b'{"value":"\xff"}', "add invalid utf8")

        with self.assertRaisesRegex(ValueError, "valid UTF-8") as raised:
            GitTree(self.repo, sha).read_json("invalid-utf8.json")
        self.assertLess(len(str(raised.exception)), 200)

    def test_commit_helpers_preserve_leading_dash_and_control_character_paths(self):
        names = ("-leading.txt", "tab\tname.txt", "newline\nname.txt")
        for name in names:
            with self.subTest(name=repr(name)):
                sha = commit_bytes(self.repo, name, name.encode("utf-8"), "add unusual path")
                tree = GitTree(self.repo, sha)
                self.assertIn(name, {blob.path for blob in tree.blobs()})
                self.assertEqual(name.encode("utf-8"), tree.read_blob(name))
        sha = commit_symlink(self.repo, "-leading-link", "target", "add unusual symlink")
        self.assertEqual(b"target", GitTree(self.repo, sha).read_blob("-leading-link"))

    def test_sha256_repository_reads_full_length_object_ids_when_supported(self):
        sha_root = self.root / "sha256"
        sha_root.mkdir()
        try:
            repo = create_git_repo(sha_root, object_format="sha256")
        except subprocess.CalledProcessError as error:
            detail = (error.stderr or "").lower()
            if (
                "object-format" in detail
                or "unknown option" in detail
                or ("sha256" in detail and ("unsupported" in detail or "unknown" in detail))
            ):
                self.skipTest("Git does not support SHA-256 object format")
            raise
        sha = commit_bytes(repo, "package.json", b'{"name":"sha256"}\n', "add package")

        self.assertEqual(64, len(sha))
        self.assertEqual(b'{"name":"sha256"}\n', GitTree(repo, sha).read_blob("package.json"))

    def test_read_blob_accepts_exact_maximum_and_rejects_one_byte_over(self):
        sha = commit_bytes(self.repo, "boundary.txt", b"12345", "add boundary")

        self.assertEqual(b"12345", GitTree(self.repo, sha, max_blob_bytes=5).read_blob("boundary.txt"))
        with self.assertRaisesRegex(ValueError, "byte limit"):
            GitTree(self.repo, sha, max_blob_bytes=4).read_blob("boundary.txt")

    def test_per_read_limit_overrides_the_constructor_default_in_both_directions(self):
        sha = commit_bytes(self.repo, "per-read.txt", b"12345", "add per-read boundary")

        self.assertEqual(
            b"12345",
            GitTree(self.repo, sha, max_blob_bytes=4).read_blob("per-read.txt", max_bytes=5),
        )
        with self.assertRaisesRegex(ValueError, "byte limit"):
            GitTree(self.repo, sha, max_blob_bytes=10).read_blob("per-read.txt", max_bytes=4)

    def test_per_read_limit_accepts_the_exact_boundary_and_rejects_invalid_values(self):
        sha = commit_bytes(self.repo, "override-boundary.txt", b"12345", "add override boundary")
        tree = GitTree(self.repo, sha, max_blob_bytes=1)

        self.assertEqual(b"12345", tree.read_blob("override-boundary.txt", max_bytes=5))
        for value in (True, False, 0, -1, "5"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError) as raised:
                    tree.read_blob("override-boundary.txt", max_bytes=value)
                self.assertNotIsInstance(
                    raised.exception,
                    github_git_tree.GitObjectReadError,
                )

    def test_deterministic_path_mode_limit_and_commit_errors_are_not_infrastructure_errors(self):
        tree = GitTree(self.repo, self.sha, max_blob_bytes=1)
        calls = (
            lambda: tree.read_blob("src\\nul.txt"),
            lambda: tree.read_blob("vendor/dependency"),
            lambda: tree.read_blob("src/cli.sh"),
        )
        for call in calls:
            with self.subTest(call=call):
                with self.assertRaises(ValueError) as raised:
                    call()
                self.assertNotIsInstance(
                    raised.exception,
                    github_git_tree.GitObjectReadError,
                )

        tree_sha = self.git("rev-parse", self.sha + "^{tree}")
        with self.assertRaises(ValueError) as raised:
            GitTree(self.repo, tree_sha).blobs()
        self.assertNotIsInstance(raised.exception, github_git_tree.GitObjectReadError)

    def test_cat_file_failure_raises_bounded_redacted_infrastructure_error(self):
        tree = GitTree(self.repo, self.sha)
        tree.blobs()
        secret = "sensitive stderr that must not escape"
        failure = subprocess.CalledProcessError(
            128,
            ["git", "cat-file"],
            stderr=secret.encode("utf-8"),
        )

        with mock.patch("github_git_tree.subprocess.run", side_effect=failure) as run:
            with self.assertRaises(github_git_tree.GitObjectReadError) as raised:
                tree.read_blob("packages/widget/package.json")

        message = str(raised.exception)
        self.assertLess(len(message), 200)
        self.assertNotIn(secret, message)
        self.assertNotIn("packages/widget/package.json", message)
        self.assertEqual("1", run.call_args.kwargs["env"]["GIT_NO_REPLACE_OBJECTS"])

    def test_cat_file_os_and_timeout_failures_are_typed_bounded_and_redacted(self):
        tree = GitTree(self.repo, self.sha)
        tree.blobs()
        failures = (
            OSError(2, "sensitive os detail", "sensitive/os/path"),
            subprocess.TimeoutExpired(
                ["git", "cat-file", "sensitive/timeout/path"],
                1,
                stderr=b"sensitive timeout stderr",
            ),
        )

        for failure in failures:
            with self.subTest(failure=type(failure).__name__):
                with mock.patch("github_git_tree.subprocess.run", side_effect=failure):
                    with self.assertRaises(github_git_tree.GitObjectReadError) as raised:
                        tree.read_blob("packages/widget/package.json")

                message = str(raised.exception)
                self.assertLess(len(message), 200)
                self.assertNotIn("sensitive", message)
                self.assertNotIn("packages/widget/package.json", message)
                self.assertIsNone(raised.exception.__cause__)

    def test_commit_verification_os_and_timeout_failures_remain_deterministic_value_errors(self):
        failures = (
            OSError(2, "sensitive os detail", "sensitive/os/path"),
            subprocess.TimeoutExpired(
                ["git", "rev-parse", "sensitive/timeout/path"],
                1,
                stderr=b"sensitive timeout stderr",
            ),
        )

        for failure in failures:
            with self.subTest(failure=type(failure).__name__):
                with mock.patch("github_git_tree.subprocess.run", side_effect=failure):
                    with self.assertRaises(ValueError) as raised:
                        GitTree(self.repo, self.sha).blobs()

                self.assertIs(type(raised.exception), ValueError)
                self.assertEqual("sha must name an exact commit", str(raised.exception))
                self.assertIsNone(raised.exception.__cause__)

    def test_post_read_size_mismatch_raises_infrastructure_error(self):
        tree = GitTree(self.repo, self.sha)
        tree.blobs()

        with mock.patch("github_git_tree._run_git_bytes", return_value=b"short"):
            with self.assertRaises(github_git_tree.GitObjectReadError) as raised:
                tree.read_blob("packages/widget/package.json")

        self.assertLess(len(str(raised.exception)), 200)
        self.assertNotIn("packages/widget/package.json", str(raised.exception))

    def test_git_object_read_error_is_exported(self):
        self.assertIn("GitObjectReadError", github_git_tree.__all__)
        self.assertTrue(issubclass(github_git_tree.GitObjectReadError, ValueError))

    def test_read_json_delegates_exact_boundary_and_validates_per_read_limit(self):
        content = b'{"name":"bounded"}'
        sha = commit_bytes(self.repo, "bounded.json", content, "add bounded json")
        tree = GitTree(self.repo, sha, max_blob_bytes=1)

        self.assertEqual(
            {"name": "bounded"},
            tree.read_json("bounded.json", max_bytes=len(content)),
        )
        with self.assertRaisesRegex(ValueError, "byte limit"):
            tree.read_json("bounded.json", max_bytes=len(content) - 1)
        for value in (True, False, 0, -1, "18"):
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, "positive integer"):
                    tree.read_json("bounded.json", max_bytes=value)


if __name__ == "__main__":
    unittest.main()
