import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from github_git import (  # noqa: E402
    GitCommandError,
    RefResolutionError,
    clone_repository,
    inspect_repository,
    resolve_ref,
    run_git,
)
from github_registry import RepoConfig  # noqa: E402
from tests.github_test_support import add_submodule_marker, commit_file, create_git_repo, tag  # noqa: E402


class GitResolutionTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.repo = create_git_repo(self.root)

    def config(self, **overrides):
        values = {
            "id": "example/upstream",
            "company": "example",
            "url": str(self.repo),
            "enabled": True,
            "repo_type": "sdk",
            "priority": "tier1",
            "track": "releases-and-default-branch",
            "version_strategy": "semver-tags",
        }
        values.update(overrides)
        return RepoConfig(**values)

    def inspection(self, **overrides):
        return inspect_repository(self.config(**overrides), self.repo)

    def test_default_branch_resolves_to_its_exact_head(self):
        sha = commit_file(self.repo, "README.md", "one\n", "initial")

        resolved = resolve_ref(self.config(), self.inspection(), "default-branch")

        self.assertEqual("branch", resolved.ref_kind)
        self.assertEqual("main", resolved.ref_name)
        self.assertEqual("main", resolved.version)
        self.assertEqual(sha, resolved.sha)
        self.assertTrue(resolved.upstream_commit_time)

    def test_tag_selector_resolves_a_semver_tag(self):
        sha = commit_file(self.repo, "README.md", "one\n", "initial")
        tag(self.repo, "v1.2.3")

        resolved = resolve_ref(self.config(), self.inspection(), "tag:v1.2.3")

        self.assertEqual("tag", resolved.ref_kind)
        self.assertEqual("v1.2.3", resolved.ref_name)
        self.assertEqual("1.2.3", resolved.version)
        self.assertEqual(sha, resolved.sha)

    def test_same_sha_tags_are_sorted_aliases(self):
        sha = commit_file(self.repo, "README.md", "one\n", "initial")
        tag(self.repo, "v1.0.0")
        tag(self.repo, "release-1")

        resolved = resolve_ref(self.config(), self.inspection(), "tag:v1.0.0")

        self.assertEqual(sha, resolved.sha)
        self.assertEqual(("release-1", "v1.0.0"), resolved.aliases)

    def test_commit_selector_resolves_only_the_requested_commit(self):
        sha = commit_file(self.repo, "README.md", "one\n", "initial")
        commit_file(self.repo, "README.md", "two\n", "next")

        resolved = resolve_ref(self.config(), self.inspection(), "commit:" + sha)

        self.assertEqual("commit", resolved.ref_kind)
        self.assertEqual(sha, resolved.ref_name)
        self.assertEqual(sha, resolved.sha)

    def test_package_selector_resolves_a_namespaced_package_tag(self):
        commit_file(
            self.repo,
            "packages/widget/package.json",
            '{"name": "@scope/widget", "version": "9.0.0"}\n',
            "add package",
        )
        tag(self.repo, "@scope/widget@9.0.0")

        inspection = self.inspection(version_strategy="monorepo-packages")
        resolved = resolve_ref(
            self.config(version_strategy="monorepo-packages"),
            inspection,
            "package:@scope/widget@9",
        )

        self.assertEqual(("@scope/widget",), inspection.packages)
        self.assertEqual("package-version", resolved.ref_kind)
        self.assertEqual("@scope/widget@9.0.0", resolved.ref_name)
        self.assertEqual("9.0.0", resolved.version)

    def test_bare_monorepo_major_is_rejected_when_ambiguous(self):
        commit_file(
            self.repo,
            "packages/one/package.json",
            '{"name": "@scope/one", "version": "9.0.0"}\n',
            "add first package",
        )
        tag(self.repo, "@scope/one@9.0.0")
        commit_file(
            self.repo,
            "packages/two/package.json",
            '{"name": "@scope/two", "version": "9.0.0"}\n',
            "add second package",
        )
        tag(self.repo, "@scope/two@9.0.0")

        with self.assertRaisesRegex(RefResolutionError, "ambiguous"):
            resolve_ref(
                self.config(version_strategy="monorepo-packages"),
                self.inspection(version_strategy="monorepo-packages"),
                "v9",
            )

    def test_missing_selector_raises_without_default_branch_fallback(self):
        sha = commit_file(self.repo, "README.md", "one\n", "initial")

        with self.assertRaisesRegex(RefResolutionError, "missing"):
            resolve_ref(self.config(), self.inspection(), "tag:v9.9.9")

        self.assertEqual(
            sha,
            resolve_ref(self.config(), self.inspection(), "default-branch").sha,
        )

    def test_package_selector_requires_a_scoped_package_namespace(self):
        commit_file(self.repo, "README.md", "one\n", "initial")

        with self.assertRaisesRegex(RefResolutionError, "namespace"):
            resolve_ref(self.config(), self.inspection(), "package:widget@9")

    def test_inspection_detects_submodules(self):
        commit_file(self.repo, "README.md", "one\n", "initial")
        add_submodule_marker(self.repo, "vendor/dependency")

        self.assertTrue(self.inspection().has_submodules)

    def test_inspection_detects_lfs_declarations(self):
        commit_file(
            self.repo,
            ".gitattributes",
            "*.bin filter=lfs diff=lfs merge=lfs -text\n",
            "declare lfs",
        )

        self.assertTrue(self.inspection().has_lfs)

    def test_clone_repository_uses_a_local_no_checkout_clone(self):
        commit_file(self.repo, "README.md", "one\n", "initial")
        destination = self.root / "clone"

        clone_repository(self.config(), destination)

        self.assertEqual("main", run_git(["symbolic-ref", "--short", "HEAD"], destination))
        self.assertFalse((destination / "README.md").exists())

    def test_git_errors_are_actionable_and_bounded(self):
        commit_file(self.repo, "README.md", "one\n", "initial")

        with self.assertRaises(GitCommandError) as raised:
            run_git(["rev-parse", "--verify", "missing-ref"], self.repo)

        message = str(raised.exception)
        self.assertIn("git rev-parse --verify missing-ref", message)
        self.assertIn("exit", message)
        self.assertLess(len(message), 1400)


if __name__ == "__main__":
    unittest.main()
