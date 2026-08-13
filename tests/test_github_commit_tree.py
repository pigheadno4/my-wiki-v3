import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from github_capsule_policy import CapsuleConfig  # noqa: E402
from github_commit_tree import resolve_commit_workspace  # noqa: E402
from github_git_tree import GitTree  # noqa: E402
from github_npm_workspace import WorkspacePackage  # noqa: E402
from tests.github_test_support import (  # noqa: E402
    commit_files,
    commit_symlink,
    create_git_repo,
)


class CommitWorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.repo = create_git_repo(Path(self.directory.name))
        self.sha = commit_files(
            self.repo,
            {
                ".env": "PAYPAL_CLIENT_SECRET=real\n",
                ".env.sample": "PAYPAL_CLIENT_SECRET=replace-me\n",
                "README.md": "# PayPal v6 sample\n",
                "client/components/paypal/checkout.js": "export const checkout = true;\n",
                "client/components/paypal/checkout.test.js": "test checkout\n",
                "client/components/venmo/app-switch.ts": "export const venmo = true;\n",
                "client/components/venmo/logo.png": b"\x89PNG\r\n",
                "client/package-lock.json": "{}\n",
                "server/node/src/orders.ts": "export const createOrder = true;\n",
                "server/node/src/oversized.ts": "x" * 100,
                ".github/workflows/ci.yml": "name: CI\n",
            },
            "add commit tree fixture",
        )
        self.sha = commit_symlink(
            self.repo,
            "client/components/paypal/readme-link",
            "../../../README.md",
            "add symlink",
        )

    def capsule(self, **overrides):
        values = {
            "id": "paypal-v6-sample-source",
            "adapter": "commit-tree-v1",
            "source_id": "v6-web-sdk-sample-integration",
            "dependency_scope": "configured-repository-paths",
            "changed_path_policy": "policy-bounded",
            "default_required_roots": (
                "client/components",
                "server/node/src",
            ),
            "include_paths": (".env.sample", "README.md"),
        }
        values.update(overrides)
        return CapsuleConfig(**values)

    def tree(self):
        return GitTree(self.repo, self.sha)

    def test_resolves_one_repository_source_from_exact_regular_blobs(self):
        workspace = resolve_commit_workspace(self.tree(), self.capsule())

        self.assertEqual(
            (
                WorkspacePackage(
                    name="v6-web-sdk-sample-integration",
                    path="",
                    version="",
                    reason="repository-source",
                    owned_paths=(
                        ".env.sample",
                        "README.md",
                        "client/components/paypal/checkout.js",
                        "client/components/paypal/checkout.test.js",
                        "client/components/venmo/app-switch.ts",
                        "client/components/venmo/logo.png",
                        "server/node/src/orders.ts",
                        "server/node/src/oversized.ts",
                    ),
                ),
            ),
            workspace.packages,
        )
        self.assertEqual((), workspace.dependency_edges)
        self.assertEqual((), workspace.external_dependencies)
        self.assertEqual((), workspace.declared_targets)

    def test_resolves_exact_file_as_required_path(self):
        workspace = resolve_commit_workspace(
            self.tree(),
            self.capsule(
                default_required_roots=("README.md",),
                include_paths=(".env.sample",),
            ),
        )

        self.assertEqual(
            (".env.sample", "README.md"),
            workspace.packages[0].owned_paths,
        )

    def test_rejects_missing_required_root_and_include(self):
        for capsule, expected in (
            (
                self.capsule(default_required_roots=("missing/source",)),
                "missing-required-root",
            ),
            (
                self.capsule(default_required_roots=("missing.graphql",)),
                "missing-required-root",
            ),
            (
                self.capsule(include_paths=("MISSING.md",)),
                "missing-required-include",
            ),
        ):
            with self.subTest(expected=expected):
                with self.assertRaisesRegex(ValueError, expected):
                    resolve_commit_workspace(self.tree(), capsule)

    def test_requires_commit_tree_adapter(self):
        with self.assertRaisesRegex(ValueError, "commit-tree-v1"):
            resolve_commit_workspace(
                self.tree(),
                CapsuleConfig(
                    id="release",
                    adapter="npm-tracked-source-v1",
                    focus_packages=("sample",),
                ),
            )


if __name__ == "__main__":
    unittest.main()
