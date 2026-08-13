import sys
import tempfile
import unittest
from unittest import mock
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from github_git import (  # noqa: E402
    GitCommandError,
    RefResolutionError,
    clone_repository,
    fetch_required_refs,
    inspect_repository,
    resolve_ref,
    run_git,
)
from github_registry import RepoConfig  # noqa: E402
from tests.github_test_support import (  # noqa: E402
    add_submodule_marker,
    annotated_tag,
    commit_file,
    create_git_repo,
    tag,
)


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

    def test_exact_prerelease_selector_does_not_resolve_the_stable_tag(self):
        prerelease_sha = commit_file(self.repo, "README.md", "candidate\n", "candidate")
        tag(self.repo, "v1.0.0-rc.1")
        stable_sha = commit_file(self.repo, "README.md", "stable\n", "stable")
        tag(self.repo, "v1.0.0")

        resolved = resolve_ref(self.config(), self.inspection(), "v1.0.0-rc.1")

        self.assertEqual("v1.0.0-rc.1", resolved.ref_name)
        self.assertEqual(prerelease_sha, resolved.sha)
        self.assertNotEqual(stable_sha, resolved.sha)

    def test_exact_selector_does_not_match_an_incomplete_candidate(self):
        commit_file(self.repo, "README.md", "partial\n", "partial")
        tag(self.repo, "v1.2")

        with self.assertRaisesRegex(RefResolutionError, "missing selector v1.2.0"):
            resolve_ref(self.config(), self.inspection(), "v1.2.0")

    def test_exact_prerelease_selector_does_not_match_an_incomplete_candidate(self):
        commit_file(self.repo, "README.md", "partial prerelease\n", "partial prerelease")
        tag(self.repo, "v1.2-rc.1")

        with self.assertRaisesRegex(RefResolutionError, "missing selector v1.2.0-rc.1"):
            resolve_ref(self.config(), self.inspection(), "v1.2.0-rc.1")

    def test_exact_selector_rejects_ambiguous_build_metadata_tags(self):
        commit_file(self.repo, "README.md", "first build\n", "first build")
        tag(self.repo, "v1.2.3+build.1")
        commit_file(self.repo, "README.md", "second build\n", "second build")
        tag(self.repo, "v1.2.3+build.2")

        with self.assertRaisesRegex(RefResolutionError, "ambiguous selector v1.2.3"):
            resolve_ref(self.config(), self.inspection(), "v1.2.3")

    def test_major_selector_prefers_stable_over_the_same_version_prerelease(self):
        commit_file(self.repo, "README.md", "candidate\n", "candidate")
        tag(self.repo, "v9.2.0-rc.1")
        stable_sha = commit_file(self.repo, "README.md", "stable\n", "stable")
        tag(self.repo, "v9.2.0")

        resolved = resolve_ref(self.config(), self.inspection(), "v9")

        self.assertEqual("v9.2.0", resolved.ref_name)
        self.assertEqual(stable_sha, resolved.sha)

    def test_major_selector_excludes_prereleases_when_no_stable_tag_exists(self):
        commit_file(self.repo, "README.md", "candidate 2\n", "candidate 2")
        tag(self.repo, "v9.2.0-rc.2")
        commit_file(self.repo, "README.md", "candidate 10\n", "candidate 10")
        tag(self.repo, "v9.2.0-rc.10")

        with self.assertRaisesRegex(RefResolutionError, "missing selector v9"):
            resolve_ref(self.config(), self.inspection(), "v9")

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

    def test_package_selector_accepts_an_unscoped_package_namespace(self):
        sha = commit_file(self.repo, "README.md", "one\n", "initial")
        tag(self.repo, "widget@9.0.0")

        resolved = resolve_ref(
            self.config(version_strategy="monorepo-packages"),
            self.inspection(version_strategy="monorepo-packages"),
            "package:widget@9",
        )

        self.assertEqual(sha, resolved.sha)
        self.assertEqual("widget@9.0.0", resolved.ref_name)

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
        promisor = subprocess.run(
            ["git", "config", "--get", "remote.origin.promisor"],
            cwd=str(destination),
            check=False,
            text=True,
            capture_output=True,
        )
        self.assertEqual(1, promisor.returncode)
        self.assertEqual("", promisor.stdout)

    def test_clone_fetch_inspect_and_resolve_selected_local_remote_refs(self):
        historical_sha = commit_file(self.repo, "README.md", "historical\n", "historical")
        annotated_tag(self.repo, "v1.0.0")
        commit_file(
            self.repo,
            "packages/widget/package.json",
            '{"name": "@scope/widget", "version": "9.1.0"}\n',
            "add package",
        )
        commit_file(
            self.repo,
            ".gitattributes",
            "*.bin filter=lfs diff=lfs merge=lfs -text\n",
            "declare lfs",
        )
        add_submodule_marker(self.repo, "vendor/dependency")
        tag(self.repo, "@scope/widget@9.1.0")
        tag(self.repo, "v99.0.0")
        destination = self.root / "clone"
        config = self.config(version_strategy="monorepo-packages")

        clone_repository(config, destination)
        fetch_required_refs(
            config,
            destination,
            ("tag:v1.0.0", "package:@scope/widget@9", "commit:" + historical_sha),
        )
        inspection = inspect_repository(config, destination)

        self.assertFalse((destination / "README.md").exists())
        self.assertEqual("", run_git(["ls-files"], destination))
        self.assertEqual(
            "true", run_git(["rev-parse", "--is-shallow-repository"], destination)
        )
        self.assertEqual(("@scope/widget",), inspection.packages)
        self.assertTrue(inspection.has_submodules)
        self.assertTrue(inspection.has_lfs)
        self.assertEqual(
            ("@scope/widget@9.1.0", "v1.0.0"),
            tuple(
                name
                for name in run_git(
                    ["for-each-ref", "--format=%(refname:strip=2)", "refs/tags"], destination
                ).splitlines()
                if name
            ),
        )
        self.assertEqual(
            historical_sha,
            resolve_ref(config, inspection, "commit:" + historical_sha).sha,
        )
        self.assertEqual("v1.0.0", resolve_ref(config, inspection, "tag:v1.0.0").ref_name)
        self.assertEqual(
            "@scope/widget@9.1.0",
            resolve_ref(config, inspection, "package:@scope/widget@9").ref_name,
        )

    def test_git_errors_are_actionable_and_bounded(self):
        commit_file(self.repo, "README.md", "one\n", "initial")

        with self.assertRaises(GitCommandError) as raised:
            run_git(["rev-parse", "--verify", "missing-ref"], self.repo)

        message = str(raised.exception)
        self.assertIn("git rev-parse --verify missing-ref", message)
        self.assertIn("exit", message)
        self.assertLess(len(message), 1400)

    def test_git_command_error_truncates_stderr_beyond_one_thousand_characters(self):
        stderr = "x" * 1001
        error = subprocess.CalledProcessError(1, ["git", "status"], stderr=stderr)

        with mock.patch("github_git.subprocess.run", side_effect=error):
            with self.assertRaises(GitCommandError) as raised:
                run_git(["status"], self.repo)

        message = str(raised.exception)
        self.assertEqual("x" * 1000 + "...", message.rsplit(": ", 1)[1])
        self.assertNotIn(stderr, message)

    def test_git_timeout_is_reported_as_a_retryable_git_error(self):
        error = subprocess.TimeoutExpired(["git", "fetch"], 120)

        with mock.patch("github_git.subprocess.run", side_effect=error) as run:
            with self.assertRaises(GitCommandError) as raised:
                run_git(["fetch"], self.repo)

        self.assertIn("timed out after 120 seconds", str(raised.exception))
        self.assertEqual(120, run.call_args.kwargs["timeout"])


if __name__ == "__main__":
    unittest.main()
