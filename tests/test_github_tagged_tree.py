import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from github_capsule_policy import CapsuleConfig, PackageOverride  # noqa: E402
from github_git_tree import GitTree  # noqa: E402
from github_npm_workspace import WorkspacePackage  # noqa: E402
from github_tagged_tree import resolve_tagged_workspace  # noqa: E402
from tests.github_test_support import commit_files, create_git_repo  # noqa: E402


class TaggedWorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.repo = create_git_repo(Path(self.directory.name))
        self.sha = commit_files(
            self.repo,
            {
                "CHANGELOG.md": "# Changes\n",
                "Package.swift": "// package\n",
                "StripePaymentSheet/Source/PaymentSheet.swift": "public struct PaymentSheet {}\n",
                "src/typings/notification/amount.ts": "export class Amount {}\n",
                "src/typings/notification/models.ts": "export * from './amount';\n",
                "src/typings/notification/notification.ts": "export class Notification {}\n",
                "src/typings/notification/notificationItem.ts": "export class NotificationItem {}\n",
                "src/typings/notification/notificationRequestItem.ts": "export class NotificationRequestItem {}\n",
                "src/typings/notification/future.ts": "export class FutureNotification {}\n",
                "unrelated/private.swift": "internal struct Private {}\n",
            },
            "add tagged tree fixture",
        )

    def capsule(self, **overrides):
        values = {
            "id": "stripe-ios-source",
            "adapter": "tagged-tree-v1",
            "focus_packages": ("stripe-ios",),
            "dependency_scope": "configured-repository-paths",
            "changed_path_policy": "policy-bounded",
            "default_required_roots": ("StripePaymentSheet/Source",),
            "include_paths": ("CHANGELOG.md", "Package.swift"),
        }
        values.update(overrides)
        return CapsuleConfig(**values)

    def tree(self):
        return GitTree(self.repo, self.sha)

    def test_resolves_one_deterministic_synthetic_root_package(self):
        workspace = resolve_tagged_workspace(
            self.tree(),
            self.capsule(),
            {"stripe-ios": "26.4.1"},
        )

        self.assertEqual(
            (
                WorkspacePackage(
                    name="stripe-ios",
                    path="",
                    version="26.4.1",
                    reason="focus",
                    owned_paths=(
                        "CHANGELOG.md",
                        "Package.swift",
                        "StripePaymentSheet/Source/PaymentSheet.swift",
                    ),
                ),
            ),
            workspace.packages,
        )
        self.assertEqual((), workspace.dependency_edges)
        self.assertEqual((), workspace.external_dependencies)
        self.assertEqual((), workspace.declared_targets)

    def test_exact_notification_includes_retain_only_the_approved_files(self):
        approved_paths = (
            "src/typings/notification/amount.ts",
            "src/typings/notification/models.ts",
            "src/typings/notification/notification.ts",
            "src/typings/notification/notificationItem.ts",
            "src/typings/notification/notificationRequestItem.ts",
        )
        workspace = resolve_tagged_workspace(
            self.tree(),
            self.capsule(include_paths=approved_paths),
            {"stripe-ios": "26.4.1"},
        )

        owned_paths = set(workspace.packages[0].owned_paths)
        self.assertTrue(set(approved_paths).issubset(owned_paths))
        self.assertNotIn("src/typings/notification/future.ts", owned_paths)

    def test_rejects_version_identity_mismatch(self):
        with self.assertRaisesRegex(
            ValueError,
            "versions must contain exactly the focus package",
        ):
            resolve_tagged_workspace(
                self.tree(),
                self.capsule(),
                {"stripe-android": "23.13.1"},
            )

    def test_rejects_missing_required_root_and_include(self):
        for capsule, expected in (
            (
                self.capsule(default_required_roots=("Missing/Source",)),
                "missing-required-root",
            ),
            (
                self.capsule(include_paths=("MISSING.md",)),
                "missing-required-include",
            ),
        ):
            with self.subTest(expected=expected):
                with self.assertRaisesRegex(ValueError, expected):
                    resolve_tagged_workspace(
                        self.tree(),
                        capsule,
                        {"stripe-ios": "26.4.1"},
                    )

    def test_rejects_npm_only_policy_fields(self):
        for capsule in (
            self.capsule(default_generated_target_paths=("dist/",)),
            self.capsule(
                package_overrides=(
                    PackageOverride(
                        "stripe-ios",
                        ("StripePaymentSheet/Source",),
                        (),
                        (),
                    ),
                ),
            ),
        ):
            with self.subTest(capsule=capsule):
                with self.assertRaisesRegex(
                    ValueError,
                    "unsupported-tagged-policy",
                ):
                    resolve_tagged_workspace(
                        self.tree(),
                        capsule,
                        {"stripe-ios": "26.4.1"},
                    )


if __name__ == "__main__":
    unittest.main()
