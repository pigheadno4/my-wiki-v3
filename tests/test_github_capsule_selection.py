import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from dataclasses import FrozenInstanceError
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from github_capsule_policy import (  # noqa: E402
    CapsuleConfig,
    PackageOverride,
    SecretAllowlist,
)
from github_capsule_selection import (  # noqa: E402
    CapsuleFile,
    CapsuleResolution,
    SecretFinding,
    classify_excluded_categories,
    resolve_capsule,
    resolve_capsule_workspace,
    resolve_npm_capsule,
    scan_evidence_files,
)
import github_capsule_selection  # noqa: E402
from github_git_tree import GitObjectReadError, GitTree  # noqa: E402
from github_registry import load_registry  # noqa: E402
from tests.github_test_support import (  # noqa: E402
    add_submodule_marker,
    commit_files,
    commit_symlink,
    create_git_repo,
)


def manifest(name="example", version="1.0.0", **values):
    result = {"name": name, "version": version}
    result.update(values)
    return json.dumps(result, separators=(",", ":")) + "\n"


def run_git(repo, *args):
    return subprocess.run(
        ["git"] + list(args),
        cwd=str(repo),
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


class CapsuleSelectionTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.repo_number = 0

    def tree(self, files, max_blob_bytes=2000000):
        repo = self.new_repo()
        sha = commit_files(repo, files, "add capsule fixture")
        return GitTree(repo, sha, max_blob_bytes=max_blob_bytes)

    def new_repo(self):
        parent = self.root / ("repo-" + str(self.repo_number))
        parent.mkdir()
        self.repo_number += 1
        return create_git_repo(parent)

    def capsule(self, **values):
        defaults = {
            "id": "selection-test",
            "adapter": "npm-tracked-source-v1",
            "focus_packages": ("example",),
            "default_generated_target_paths": (),
        }
        defaults.update(values)
        return CapsuleConfig(**defaults)

    def commit_capsule(self, **values):
        defaults = {
            "id": "commit-selection-test",
            "adapter": "commit-tree-v1",
            "source_id": "sample-integration",
            "dependency_scope": "configured-repository-paths",
            "changed_path_policy": "policy-bounded",
            "default_required_roots": ("client/components", "server/node/src"),
            "include_paths": (".env.sample", "README.md", "client/package.json"),
            "excluded_categories": ("tests", "fixtures"),
        }
        defaults.update(values)
        return CapsuleConfig(**defaults)

    def blob(self, tree, path):
        return next(item for item in tree.blobs() if item.path == path)

    def allow(self, tree, path, detector_code):
        blob = self.blob(tree, path)
        return SecretAllowlist(path, blob.oid, detector_code)

    def assert_policy_review(self, code, tree, capsule=None, allowlist=()):
        with self.assertRaisesRegex(
            ValueError,
            r"^needs-policy-review:" + code + r":",
        ):
            resolve_npm_capsule(tree, capsule or self.capsule(), allowlist)

    def test_public_records_are_frozen_and_resolution_is_deeply_tuple_based(self):
        tree = self.tree(
            {
                "package.json": manifest(),
                "src/index.js": "export const value = 1;\n",
            }
        )

        result = resolve_npm_capsule(tree, self.capsule(), ())

        self.assertIsInstance(result, CapsuleResolution)
        self.assertIsInstance(result.files[0], CapsuleFile)
        self.assertIsInstance(result.secret_findings, tuple)
        self.assertIsInstance(result.excluded, tuple)
        self.assertIsInstance(result.required_roots, tuple)
        self.assertIsInstance(result.generated_target_paths, tuple)
        self.assertIsInstance(result.include_paths, tuple)
        with self.assertRaises((FrozenInstanceError, AttributeError)):
            result.files[0].path = "changed"

    def test_tagged_dispatch_selects_only_configured_nonexcluded_evidence(self):
        tree = self.tree(
            {
                "README.md": "# SDK\n",
                "SDK/Source/Checkout.swift": "public struct Checkout {}\n",
                "SDK/Source/Tests/Checkout.swift": "test checkout\n",
                "SDK/Source/tests/Fixture.swift": "test fixture\n",
                "SDK/Source/snapshots/checkout.txt": "snapshot\n",
                "SDK/Source/stories/Checkout.story.swift": "public let story = true\n",
                "docs/outside.md": "outside\n",
            }
        )
        capsule = CapsuleConfig(
            id="tagged-selection",
            adapter="tagged-tree-v1",
            focus_packages=("stripe-ios",),
            dependency_scope="configured-repository-paths",
            changed_path_policy="policy-bounded",
            default_required_roots=("SDK/Source",),
            include_paths=("README.md",),
            excluded_categories=("tests", "fixtures"),
        )

        workspace = resolve_capsule_workspace(
            tree,
            capsule,
            {"stripe-ios": "26.4.1"},
        )
        result = resolve_capsule(
            tree,
            capsule,
            (),
            changed_paths=(
                "SDK/Source/Checkout.swift",
                "docs/outside.md",
            ),
            versions={"stripe-ios": "26.4.1"},
        )

        self.assertEqual(workspace, result.workspace)
        selected = {
            item.path: item.classification_reason for item in result.files
        }
        self.assertEqual("include-path", selected["README.md"])
        self.assertEqual(
            "required-root",
            selected["SDK/Source/Checkout.swift"],
        )
        self.assertEqual(
            "required-root",
            selected["SDK/Source/stories/Checkout.story.swift"],
        )
        self.assertNotIn("SDK/Source/Tests/Checkout.swift", selected)
        self.assertNotIn("SDK/Source/tests/Fixture.swift", selected)
        self.assertNotIn("SDK/Source/snapshots/checkout.txt", selected)
        self.assertNotIn("docs/outside.md", selected)
        self.assertEqual(
            {"stripe-ios"},
            {item.package for item in result.files},
        )
        self.assertEqual(
            "tagged-tree-v1",
            result.effective_policy.capsule.adapter,
        )

    def test_tagged_dispatch_batches_selected_blob_reads(self):
        tree = self.tree(
            {
                "README.md": "# SDK\n",
                "lib/Checkout.php": "<?php final class Checkout {}\n",
                "lib/PaymentIntent.php": "<?php final class PaymentIntent {}\n",
            }
        )
        capsule = CapsuleConfig(
            id="tagged-batch-read",
            adapter="tagged-tree-v1",
            focus_packages=("stripe-php",),
            dependency_scope="configured-repository-paths",
            changed_path_policy="policy-bounded",
            default_required_roots=("lib",),
            include_paths=("README.md",),
        )
        tree.blobs()

        with mock.patch("github_git_tree.subprocess.run", wraps=subprocess.run) as run:
            result = resolve_capsule(
                tree,
                capsule,
                (),
                versions={"stripe-php": "21.2.0"},
            )

        self.assertEqual(3, len(result.files))
        cat_file_commands = [
            tuple(call.args[0])
            for call in run.call_args_list
            if call.args[0][:2] == ["git", "cat-file"]
        ]
        self.assertEqual(
            [
                ("git", "cat-file", "--batch-check"),
                ("git", "cat-file", "--batch"),
            ],
            cat_file_commands,
        )

    def test_tagged_dispatch_rejects_aggregate_budget_before_content_batch(self):
        tree = self.tree(
            {
                "README.md": "# SDK\n",
                "lib/Checkout.php": "<?php final class Checkout {}\n",
                "lib/PaymentIntent.php": "<?php final class PaymentIntent {}\n",
            }
        )
        capsule = CapsuleConfig(
            id="tagged-batch-budget",
            adapter="tagged-tree-v1",
            focus_packages=("stripe-php",),
            dependency_scope="configured-repository-paths",
            changed_path_policy="policy-bounded",
            default_required_roots=("lib",),
            include_paths=("README.md",),
            max_capsule_utf8_bytes=50,
        )
        tree.blobs()

        with mock.patch("github_git_tree.subprocess.run", wraps=subprocess.run) as run:
            with self.assertRaisesRegex(ValueError, "capsule-budget-exceeded"):
                resolve_capsule(
                    tree,
                    capsule,
                    (),
                    versions={"stripe-php": "21.2.0"},
                )

        cat_file_commands = [
            tuple(call.args[0])
            for call in run.call_args_list
            if call.args[0][:2] == ["git", "cat-file"]
        ]
        self.assertEqual([("git", "cat-file", "--batch-check")], cat_file_commands)

    def test_tagged_dispatch_reuses_secret_and_budget_guards(self):
        def capsule(**overrides):
            values = {
                "id": "tagged-guards",
                "adapter": "tagged-tree-v1",
                "focus_packages": ("stripe-ios",),
                "dependency_scope": "configured-repository-paths",
                "changed_path_policy": "policy-bounded",
                "default_required_roots": ("SDK/Source",),
                "include_paths": ("README.md",),
            }
            values.update(overrides)
            return CapsuleConfig(**values)

        secret_tree = self.tree(
            {
                "README.md": "# SDK\n",
                "SDK/Source/Checkout.swift": (
                    'let token = "ghp_' + ("a" * 36) + '"\n'
                ),
            }
        )
        with self.assertRaisesRegex(ValueError, "secret-finding"):
            resolve_capsule(
                secret_tree,
                capsule(),
                (),
                versions={"stripe-ios": "26.4.1"},
            )

        budget_tree = self.tree(
            {
                "README.md": "# SDK\n",
                "SDK/Source/Checkout.swift": "public struct Checkout {}\n",
            }
        )
        with self.assertRaisesRegex(ValueError, "capsule-budget-exceeded"):
            resolve_capsule(
                budget_tree,
                capsule(max_capsule_files=1),
                (),
                versions={"stripe-ios": "26.4.1"},
            )
        with self.assertRaisesRegex(ValueError, "capsule-budget-exceeded"):
            resolve_capsule(
                budget_tree,
                capsule(max_capsule_utf8_bytes=10),
                (),
                versions={"stripe-ios": "26.4.1"},
            )

    def test_commit_dispatch_selects_payment_source_and_excludes_repository_noise(self):
        tree = self.tree(
            {
                ".env.sample": "PAYPAL_CLIENT_ID=replace-me\n",
                "README.md": "# Sample\n",
                "client/package.json": manifest(),
                "client/components/paypal/checkout.js": "export const checkout = true;\n",
                "client/components/venmo/app-switch.ts": "export const venmo = true;\n",
                "client/components/local-payments/ideal.js": "export const ideal = true;\n",
                "client/components/paypal/checkout.test.js": "test checkout\n",
                "client/components/jest.config.js": "module.exports = {};\n",
                "client/components/package-lock.json": "{}\n",
                "client/components/logo.png": b"\x89PNG\x00",
                "client/components/.github/workflows/ci.yml": "name: CI\n",
                "client/components/deploy/fly.toml": "app = 'sample'\n",
                "client/components/node_modules/sdk/index.js": "generated dependency\n",
                "client/components/dist/bundle.js": "generated output\n",
                "client/components/.env": "PAYPAL_CLIENT_SECRET=real\n",
                "server/node/src/orders.ts": "export const orders = true;\n",
            }
        )

        workspace = resolve_capsule_workspace(tree, self.commit_capsule())
        result = resolve_capsule(tree, self.commit_capsule(), ())
        selected = {item.path: item for item in result.files}

        self.assertEqual(workspace, result.workspace)
        self.assertEqual(
            {
                ".env.sample",
                "README.md",
                "client/package.json",
                "client/components/local-payments/ideal.js",
                "client/components/paypal/checkout.js",
                "client/components/venmo/app-switch.ts",
                "server/node/src/orders.ts",
            },
            set(selected),
        )
        self.assertEqual(
            {"sample-integration"},
            {item.package for item in result.files},
        )
        self.assertTrue(
            all(item.classification_reason in {"include-path", "required-root"} for item in result.files)
        )
        excluded_paths = {path for path, _ in result.excluded}
        self.assertTrue(
            {
                "client/components/.env",
                "client/components/.github/workflows/ci.yml",
                "client/components/deploy/fly.toml",
                "client/components/dist/bundle.js",
                "client/components/jest.config.js",
                "client/components/logo.png",
                "client/components/node_modules/sdk/index.js",
                "client/components/package-lock.json",
                "client/components/paypal/checkout.test.js",
            }.issubset(excluded_paths)
        )

    def test_commit_dispatch_selects_exact_root_file(self):
        tree = self.tree(
            {
                "CHANGELOG.md": "# Changes\n",
                "README.md": "# GraphQL API\n",
                "schema.graphql": "type Query { ping: String }\n",
            }
        )
        capsule = self.commit_capsule(
            source_id="braintree-graphql-api",
            default_required_roots=("schema.graphql",),
            include_paths=("CHANGELOG.md", "README.md"),
        )

        result = resolve_capsule(tree, capsule, ())

        self.assertEqual(
            {"CHANGELOG.md", "README.md", "schema.graphql"},
            {item.path for item in result.files},
        )
        schema = next(item for item in result.files if item.path == "schema.graphql")
        self.assertEqual("required-root", schema.classification_reason)

    def test_commit_dispatch_reuses_secret_binary_and_budget_guards(self):
        secret_tree = self.tree(
            {
                ".env.sample": "PAYPAL_CLIENT_ID=replace-me\n",
                "README.md": "# Sample\n",
                "client/package.json": manifest(),
                "client/components/paypal/checkout.js": 'const token = "ghp_' + ("a" * 36) + '";\n',
                "server/node/src/orders.ts": "export const orders = true;\n",
            }
        )
        with self.assertRaisesRegex(ValueError, "secret-finding"):
            resolve_capsule(secret_tree, self.commit_capsule(), ())

        binary_tree = self.tree(
            {
                ".env.sample": "PAYPAL_CLIENT_ID=replace-me\n",
                "README.md": "# Sample\n",
                "client/package.json": manifest(),
                "client/components/logo.png": b"\x89PNG\x00",
                "server/node/src/orders.ts": "export const orders = true;\n",
            }
        )
        with self.assertRaisesRegex(ValueError, "unsafe-required-file"):
            resolve_capsule(
                binary_tree,
                self.commit_capsule(include_paths=("client/components/logo.png",)),
                (),
            )

        budget_tree = self.tree(
            {
                ".env.sample": "PAYPAL_CLIENT_ID=replace-me\n",
                "README.md": "# Sample\n",
                "client/package.json": manifest(),
                "client/components/paypal/checkout.js": "export const checkout = true;\n",
                "server/node/src/orders.ts": "export const orders = true;\n",
            }
        )
        with self.assertRaisesRegex(ValueError, "capsule-budget-exceeded"):
            resolve_capsule(
                budget_tree,
                self.commit_capsule(max_capsule_files=1),
                (),
            )

    def test_braintree_android_policy_excludes_binary_ui_asset(self):
        repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
        repo = next(
            item for item in repos if item.id == "braintree/braintree_android"
        )
        self.assertEqual(1, len(repo.capsules))
        capsule = repo.capsules[0]
        files = {
            root + "/Evidence.kt": "public class Evidence\n"
            for root in capsule.default_required_roots
        }
        files.update({path: "evidence\n" for path in capsule.include_paths})
        files[
            "UIComponents/src/main/res/drawable/paypal_logo.xml"
        ] = "<vector />\n"
        files[
            "UIComponents/src/main/res/drawable-xxhdpi/"
            "card_fields_cc_discover.png"
        ] = b"\x89PNG\x00binary"
        files["Demo/src/main/java/Demo.kt"] = "class Demo\n"
        files["TestUtils/src/main/java/TestHelper.kt"] = "class TestHelper\n"

        result = resolve_capsule(
            self.tree(files),
            capsule,
            (),
            versions={"braintree-android": "5.30.0"},
        )
        selected = {item.path for item in result.files}

        self.assertIn(
            "UIComponents/src/main/res/drawable/paypal_logo.xml",
            selected,
        )
        self.assertIn("UIComponents/src/main/AndroidManifest.xml", selected)
        self.assertNotIn(
            "UIComponents/src/main/res/drawable-xxhdpi/"
            "card_fields_cc_discover.png",
            selected,
        )
        self.assertNotIn("Demo/src/main/java/Demo.kt", selected)
        self.assertNotIn("TestUtils/src/main/java/TestHelper.kt", selected)

    def test_braintree_ios_policy_excludes_binary_ui_asset(self):
        repos = load_registry(ROOT / "tracking/github/repo-registry.toml")
        repo = next(
            item for item in repos if item.id == "braintree/braintree_ios"
        )
        capsule = repo.capsules[0]
        files = {
            root + "/Evidence.swift": "public struct Evidence {}\n"
            for root in capsule.default_required_roots
        }
        files.update({path: "evidence\n" for path in capsule.include_paths})
        files[
            "Sources/BraintreeUIComponents/Resources/Assets.xcassets/"
            "CardBrandImages/AmericanExpressLogo.imageset/AmericanExpressLogo.pdf"
        ] = b"%PDF-1.4\x00binary"

        result = resolve_capsule(
            self.tree(files),
            capsule,
            (),
            versions={"braintree-ios": "7.9.0"},
        )
        selected = {item.path for item in result.files}

        self.assertIn(
            "Sources/BraintreeUIComponents/CardFields/Evidence.swift",
            selected,
        )
        self.assertIn(
            "Sources/BraintreeUIComponents/VenmoButton.swift",
            selected,
        )
        self.assertNotIn(
            "Sources/BraintreeUIComponents/Resources/Assets.xcassets/"
            "CardBrandImages/AmericanExpressLogo.imageset/AmericanExpressLogo.pdf",
            selected,
        )

    def test_exact_classification_precedence_exclusions_and_file_metadata(self):
        package = manifest(
            main="./main.js",
            module="./module.js",
            types="./types/index.d.ts",
            bin={"example": "./bin/cli.js"},
            exports={
                ".": {
                    "types": "./types/conditional.d.ts",
                    "default": "./lib/export.js",
                },
                "./feature/*": "./lib/features/*.js",
                "./typed/*": {"types": "./types/features/*.d.ts"},
                "./root": "./src/index.js",
                "./generated": "./dist/generated.js",
                "./generated/*": "./dist/*.js",
                "./blocked": None,
            },
        )
        files = {
            "package.json": package,
            "main.js": "main\n",
            "module.js": "module\n",
            "manual.js": "manual\n",
            "bin/cli.js": "cli\n",
            "lib/export.js": "export\n",
            "lib/features/a.js": "feature\n",
            "types/index.d.ts": "export declare const value: number;\n",
            "types/conditional.d.ts": "export declare const conditional: number;\n",
            "types/features/a.d.ts": "export declare const feature: number;\n",
            "types/sibling.d.ts": "export declare const sibling: number;\n",
            "types/fixtures/kept.d.ts": "export declare const kept: number;\n",
            "src/index.js": "source\n",
            "src/main.test.js": "test\n",
            "src/specs/item.spec.js": "spec\n",
            "src/stories/item.js": "story\n",
            "src/component.stories.js": "story\n",
            "src/fixtures/data.js": "fixture\n",
            "src/tests/fixtures/both.js": "both\n",
            "docs/readme.md": "optional\n",
        }
        repo = self.new_repo()
        sha = commit_files(repo, files, "add classification fixture")
        executable = repo / "bin/cli.js"
        executable.chmod(0o755)
        run_git(repo, "add", "--", "bin/cli.js")
        run_git(repo, "commit", "-m", "make bin executable")
        sha = run_git(repo, "rev-parse", "HEAD")
        tree = GitTree(repo, sha, max_blob_bytes=2000000)
        capsule = self.capsule(
            include_paths=("manual.js", "main.js", "src/index.js"),
            default_generated_target_paths=("dist/",),
        )

        result = resolve_npm_capsule(tree, capsule, ())

        reasons = {item.path: item.classification_reason for item in result.files}
        self.assertEqual("package-manifest", reasons["package.json"])
        self.assertEqual("include-path", reasons["main.js"])
        self.assertEqual("include-path", reasons["manual.js"])
        self.assertEqual("tracked-module-target", reasons["module.js"])
        self.assertEqual("tracked-bin-target", reasons["bin/cli.js"])
        self.assertEqual("tracked-export-target", reasons["lib/export.js"])
        self.assertEqual("tracked-export-pattern", reasons["lib/features/a.js"])
        self.assertEqual("tracked-export-target", reasons["types/conditional.d.ts"])
        self.assertEqual("tracked-export-pattern", reasons["types/features/a.d.ts"])
        self.assertEqual("tracked-types-target", reasons["types/index.d.ts"])
        self.assertEqual(
            "tracked-declaration-directory",
            reasons["types/sibling.d.ts"],
        )
        self.assertNotIn("types/fixtures/kept.d.ts", reasons)
        self.assertEqual("required-root", reasons["src/index.js"])
        self.assertNotIn("docs/readme.md", reasons)
        self.assertNotIn("src/main.test.js", reasons)
        self.assertEqual(
            (
                ("src/component.stories.js", "excluded-category:stories"),
                ("src/fixtures/data.js", "excluded-category:fixtures"),
                ("src/main.test.js", "excluded-category:tests"),
                ("src/specs/item.spec.js", "excluded-category:tests"),
                ("src/stories/item.js", "excluded-category:stories"),
                ("src/tests/fixtures/both.js", "excluded-category:fixtures"),
                ("src/tests/fixtures/both.js", "excluded-category:tests"),
                ("types/fixtures/kept.d.ts", "excluded-category:fixtures"),
            ),
            result.excluded,
        )
        cli = next(item for item in result.files if item.path == "bin/cli.js")
        self.assertEqual("100755", cli.git_mode)
        self.assertEqual(b"cli\n", cli.content)
        self.assertEqual(len(cli.content), cli.size)
        self.assertEqual(hashlib.sha256(cli.content).hexdigest(), cli.sha256)
        self.assertEqual(self.blob(tree, "bin/cli.js").oid, cli.git_blob_oid)
        self.assertEqual("example", cli.package)
        self.assertEqual("source-capsule", cli.purpose)
        self.assertEqual(tuple(sorted(reasons)), tuple(item.path for item in result.files))

    def test_changed_release_evidence_respects_exclusions_and_keeps_stories(self):
        tree = self.tree(
            {
                "package.json": manifest(),
                "src/index.ts": "export const value = 1;\n",
                "test/public-api.test.ts": "test('public api', () => {});\n",
                "stories/new-option.stories.tsx": "export const NewOption = {};\n",
                "fixtures/new-option.json": "{}\n",
                "docs/new-option.md": "# New option\n",
            }
        )

        result = resolve_npm_capsule(
            tree,
            self.capsule(excluded_categories=("tests", "fixtures")),
            (),
            changed_paths=(
                "test/public-api.test.ts",
                "stories/new-option.stories.tsx",
                "fixtures/new-option.json",
                "docs/new-option.md",
            ),
        )

        selected = {item.path: item.classification_reason for item in result.files}
        self.assertEqual(
            "changed-release-evidence", selected["stories/new-option.stories.tsx"]
        )
        self.assertEqual("changed-release-evidence", selected["docs/new-option.md"])
        self.assertNotIn("test/public-api.test.ts", selected)
        self.assertNotIn("fixtures/new-option.json", selected)
        self.assertEqual(
            (
                ("fixtures/new-option.json", "excluded-category:fixtures"),
                ("test/public-api.test.ts", "excluded-category:tests"),
            ),
            result.excluded,
        )

    def test_changed_path_outside_included_packages_is_not_collected(self):
        tree = self.tree(
            {
                "package.json": manifest("root", workspaces=["packages/*"]),
                "packages/example/package.json": manifest("example"),
                "packages/example/src/index.ts": "export const value = 1;\n",
                "packages/unrelated/package.json": manifest("unrelated"),
                "packages/unrelated/src/private.ts": "export const privateValue = 1;\n",
            }
        )

        result = resolve_npm_capsule(
            tree,
            self.capsule(),
            (),
            changed_paths=("packages/unrelated/src/private.ts",),
        )

        self.assertNotIn(
            "packages/unrelated/src/private.ts", {item.path for item in result.files}
        )

    def test_policy_bounded_changed_paths_cannot_expand_base_selection(self):
        tree = self.tree(
            {
                "package.json": manifest(),
                "src/index.ts": "export const checkout = 1;\n",
                "src/core/checkout.ts": "export const core = 1;\n",
                "src/core/checkout.test.ts": "test('checkout', () => {});\n",
                "src/components/Wallet.ts": "export const Wallet = 1;\n",
                "fixtures/wallet.json": "{}\n",
            }
        )

        result = resolve_npm_capsule(
            tree,
            self.capsule(
                changed_path_policy="policy-bounded",
                default_required_roots=("src/core",),
                include_paths=("src/index.ts",),
                excluded_categories=("tests", "fixtures"),
            ),
            (),
            changed_paths=(
                "src/index.ts",
                "src/core/checkout.ts",
                "src/core/checkout.test.ts",
                "src/components/Wallet.ts",
                "fixtures/wallet.json",
            ),
        )

        selected = {item.path for item in result.files}
        self.assertIn("src/index.ts", selected)
        self.assertIn("src/core/checkout.ts", selected)
        self.assertNotIn("src/core/checkout.test.ts", selected)
        self.assertNotIn("src/components/Wallet.ts", selected)
        self.assertNotIn("fixtures/wallet.json", selected)

    def test_changed_release_evidence_keeps_secret_and_file_budget_guards(self):
        secret = "ghp_" + ("a" * 36) + "\n"
        secret_tree = self.tree(
            {
                "package.json": manifest(),
                "src/index.ts": "export const value = 1;\n",
                "docs/secret.md": secret,
            }
        )

        with self.assertRaisesRegex(ValueError, "secret-finding"):
            resolve_npm_capsule(
                secret_tree,
                self.capsule(),
                (),
                changed_paths=("docs/secret.md",),
            )

        oversized_tree = self.tree(
            {
                "package.json": manifest(),
                "src/index.ts": "x\n",
                "docs/large.md": "x" * 101,
            }
        )
        with self.assertRaisesRegex(ValueError, "capsule-budget-exceeded"):
            resolve_npm_capsule(
                oversized_tree,
                self.capsule(max_file_bytes=100),
                (),
                changed_paths=("docs/large.md",),
            )

    def test_public_evidence_scanner_reuses_exact_secret_allowlist_contract(self):
        secret = ("ghp_" + ("a" * 36) + "\n").encode("utf-8")
        tree = self.tree(
            {
                "package.json": manifest(),
                "README.md": secret,
                "src/index.ts": "export const value = 1;\n",
            }
        )
        blob = self.blob(tree, "README.md")
        evidence = CapsuleFile(
            path="README.md",
            content=secret,
            sha256=hashlib.sha256(secret).hexdigest(),
            size=len(secret),
            purpose="repository-context",
            git_blob_oid=blob.oid,
            git_mode=blob.mode,
            package="",
            classification_reason="repository-context",
        )

        with self.assertRaises(github_capsule_selection.SecretFindingsBlocked):
            scan_evidence_files((evidence,), ())

        findings = scan_evidence_files(
            (evidence,),
            (SecretAllowlist("README.md", blob.oid, "github-token-v1"),),
        )

        self.assertEqual(("github-token-v1",), tuple(item.detector_code for item in findings))

    def test_public_evidence_scanner_blocks_psp_and_modern_registry_tokens(self):
        secrets = (
            "sk_live_" + ("a" * 24),
            "github_pat_" + ("a" * 40),
            "npm_" + ("a" * 36),
            "access_token$production$merchant$" + ("a" * 32),
        )

        for index, secret in enumerate(secrets):
            with self.subTest(secret=index):
                content = (secret + "\n").encode("utf-8")
                evidence = CapsuleFile(
                    path="secret-" + str(index) + ".txt",
                    content=content,
                    sha256=hashlib.sha256(content).hexdigest(),
                    size=len(content),
                    purpose="test",
                    git_blob_oid=("a" * 39) + str(index),
                    git_mode="100644",
                    package="",
                    classification_reason="test",
                )
                with self.assertRaisesRegex(ValueError, "secret-finding"):
                    scan_evidence_files((evidence,), ())

    def test_package_overrides_and_resolved_policy_rows_are_exact(self):
        tree = self.tree(
            {
                "package.json": manifest(
                    "root",
                    workspaces=["packages/*"],
                ),
                "packages/app/package.json": manifest(
                    "app",
                    dependencies={"dep": "workspace:*"},
                    main="./entry.js",
                ),
                "packages/app/src/index.js": "app source\n",
                "packages/app/entry.js": "app entry\n",
                "packages/app/shared.cfg": "shared app\n",
                "packages/dep/package.json": manifest("dep"),
                "packages/dep/src/not-selected.js": "not selected\n",
                "packages/dep/types/index.d.ts": "export declare const dep: number;\n",
                "packages/dep/shared.cfg": "shared dep\n",
                "packages/dep/dep.cfg": "dep config\n",
            }
        )
        capsule = CapsuleConfig(
            id="override-test",
            adapter="npm-tracked-source-v1",
            focus_packages=("app",),
            default_required_roots=("src",),
            default_generated_target_paths=("build.js",),
            include_paths=("shared.cfg",),
            package_overrides=(
                PackageOverride(
                    "dep",
                    ("types",),
                    ("dist/",),
                    ("dep.cfg", "shared.cfg"),
                ),
            ),
        )

        result = resolve_npm_capsule(tree, capsule, ())

        self.assertEqual(
            (
                ("app", "src", "default"),
                ("dep", "types", "package-override"),
            ),
            result.required_roots,
        )
        self.assertEqual(
            (
                ("app", "build.js", "file", "default"),
                ("dep", "dist/", "directory", "package-override"),
            ),
            result.generated_target_paths,
        )
        self.assertEqual(
            (
                ("app", "entry.js", "declared-target"),
                ("app", "shared.cfg", "capsule-policy"),
                ("dep", "dep.cfg", "package-override"),
                ("dep", "shared.cfg", "capsule-policy"),
            ),
            result.include_paths,
        )
        paths = tuple(item.path for item in result.files)
        self.assertIn("packages/app/src/index.js", paths)
        self.assertIn("packages/dep/types/index.d.ts", paths)
        self.assertNotIn("packages/dep/src/not-selected.js", paths)

    def test_resolved_rows_preserve_distinct_policy_and_declaration_provenance(self):
        tree = self.tree(
            {
                "package.json": manifest(
                    main="./main.js",
                    types="./types/index.d.ts",
                ),
                "main.js": "main\n",
                "types/index.d.ts": "export declare const value: number;\n",
                "types/sibling.d.ts": "export declare const sibling: number;\n",
            }
        )
        capsule = self.capsule(
            default_required_roots=("types",),
            include_paths=("main.js",),
        )

        result = resolve_npm_capsule(tree, capsule, ())

        self.assertEqual(
            (
                ("example", "types", "default"),
                ("example", "types", "tracked-declaration-target"),
            ),
            result.required_roots,
        )
        self.assertEqual(
            (
                ("example", "main.js", "capsule-policy"),
                ("example", "main.js", "declared-target"),
                ("example", "types/index.d.ts", "declared-target"),
            ),
            result.include_paths,
        )
        reasons = {item.path: item.classification_reason for item in result.files}
        self.assertEqual("include-path", reasons["main.js"])
        self.assertEqual("required-root", reasons["types/index.d.ts"])

    def test_generated_target_results_are_preserved_without_inference(self):
        tree = self.tree(
            {
                "package.json": manifest(
                    exports={
                        "./generated": "./dist/generated.js",
                        "./generated/*": "./dist/*.js",
                        "./blocked": None,
                    }
                ),
                "src/index.js": "source\n",
            }
        )

        result = resolve_npm_capsule(
            tree,
            self.capsule(default_generated_target_paths=("dist/",)),
            (),
        )

        self.assertEqual(
            (
                ("blocked-export", "", ""),
                ("generated-target-not-tracked", "dist/", "./dist/generated.js"),
                ("generated-pattern-not-tracked", "dist/", "./dist/*.js"),
            ),
            tuple(
                (target.status, target.generated_policy_path, target.target)
                for target in result.workspace.declared_targets
            ),
        )
        self.assertNotIn("dist/generated.js", tuple(item.path for item in result.files))

    def test_selection_uses_owned_paths_without_absorbing_nonclosure_workspaces(self):
        tree = self.tree(
            {
                "package.json": manifest(
                    workspaces=["src/*"],
                ),
                "src/root.js": "root source\n",
                "src/child/package.json": manifest("child"),
                "src/child/index.js": "child source\n",
            }
        )

        result = resolve_npm_capsule(tree, self.capsule(), ())

        self.assertEqual(("example",), tuple(item.name for item in result.workspace.packages))
        self.assertEqual(
            ("package.json", "src/root.js"),
            tuple(item.path for item in result.files),
        )

    def test_explicit_targets_override_exclusions_but_declaration_expansion_does_not(self):
        tree = self.tree(
            {
                "package.json": manifest(
                    main="./tests/main.js",
                    types="./fixtures/types/index.d.ts",
                ),
                "src/tests/excluded.js": "excluded\n",
                "tests/main.js": "main\n",
                "stories/manual.js": "manual\n",
                "fixtures/types/index.d.ts": "export declare const x: number;\n",
                "fixtures/types/more.d.ts": "export declare const y: number;\n",
            }
        )

        result = resolve_npm_capsule(
            tree,
            self.capsule(include_paths=("stories/manual.js",)),
            (),
        )

        reasons = {item.path: item.classification_reason for item in result.files}
        self.assertEqual("tracked-main-target", reasons["tests/main.js"])
        self.assertEqual("include-path", reasons["stories/manual.js"])
        self.assertEqual("tracked-types-target", reasons["fixtures/types/index.d.ts"])
        self.assertNotIn("fixtures/types/more.d.ts", reasons)
        self.assertEqual(
            (
                ("fixtures/types/more.d.ts", "excluded-category:fixtures"),
                ("src/tests/excluded.js", "excluded-category:tests"),
            ),
            result.excluded,
        )

    def test_disabled_categories_remain_required_under_configured_roots(self):
        tree = self.tree(
            {
                "package.json": manifest(),
                "src/value.test.js": "test-shaped production source\n",
            }
        )

        result = resolve_npm_capsule(
            tree,
            self.capsule(excluded_categories=()),
            (),
        )

        self.assertEqual((), result.excluded)
        selected = next(item for item in result.files if item.path == "src/value.test.js")
        self.assertEqual("required-root", selected.classification_reason)

    def test_all_enabled_categories_are_excluded_and_selected_paths_have_no_exclusion_rows(self):
        path = "src/tests/stories/fixtures/value.test.stories.js"
        tree = self.tree(
            {
                "package.json": manifest(),
                path: "multi-category evidence\n",
            }
        )

        excluded = resolve_npm_capsule(tree, self.capsule(), ())

        self.assertEqual(
            (
                (path, "excluded-category:fixtures"),
                (path, "excluded-category:stories"),
                (path, "excluded-category:tests"),
            ),
            excluded.excluded,
        )

        selected = resolve_npm_capsule(
            tree,
            self.capsule(include_paths=(path,)),
            (),
        )
        self.assertEqual((), selected.excluded)
        selected_file = next(item for item in selected.files if item.path == path)
        self.assertEqual("required-root", selected_file.classification_reason)

    def test_category_directory_matching_is_case_insensitive(self):
        path = "ios/Tests/PaymentSheetTests.swift"
        tree = self.tree(
            {
                "package.json": manifest(),
                path: "final class PaymentSheetTests {}\n",
            }
        )

        result = resolve_npm_capsule(tree, self.capsule(default_required_roots=("ios",)), ())

        self.assertEqual(
            ((path, "excluded-category:tests"),),
            result.excluded,
        )
        self.assertNotIn(path, {item.path for item in result.files})

    def test_test_category_excludes_mock_directories_without_excluding_stories(self):
        mock_path = "src/lib/__mocks__/analytics.js"
        story_path = ".storybook/stories/HostedFields.stories.ts"
        tree = self.tree(
            {
                "package.json": manifest(name="braintree-web", version="3.142.0"),
                "src/index.js": "module.exports = {};\n",
                mock_path: "module.exports = {};\n",
                story_path: "export default {};\n",
            }
        )

        result = resolve_npm_capsule(
            tree,
            self.capsule(
                focus_packages=("braintree-web",),
                default_required_roots=("src", ".storybook/stories"),
                excluded_categories=("tests", "fixtures"),
            ),
            (),
        )

        paths = tuple(item.path for item in result.files)
        self.assertIn(story_path, paths)
        self.assertNotIn(mock_path, paths)
        self.assertIn(
            (mock_path, "excluded-category:tests"),
            result.excluded,
        )

    def test_public_category_classifier_matches_capsule_selection(self):
        self.assertEqual(
            ("tests",),
            classify_excluded_categories(
                "src/lib/__mocks__/analytics.js",
                ("tests", "fixtures"),
            ),
        )
        self.assertEqual(
            ("tests",),
            classify_excluded_categories(
                "pkg/config/config_test.go",
                ("tests", "fixtures"),
            ),
        )
        self.assertEqual(
            (),
            classify_excluded_categories(
                ".storybook/stories/HostedFields.stories.ts",
                ("tests", "fixtures"),
            ),
        )

    def test_root_level_type_target_respects_category_exclusions_in_declaration_directory(self):
        tree = self.tree(
            {
                "package.json": manifest(types="./index.d.ts"),
                "index.d.ts": "export declare const value: number;\n",
                "sibling.d.ts": "export declare const sibling: number;\n",
                "docs/readme.md": "package-root evidence\n",
                "src/value.test.js": "category does not override declaration scope\n",
            }
        )

        result = resolve_npm_capsule(tree, self.capsule(), ())

        self.assertEqual(
            (
                ("example", "", "tracked-declaration-target"),
                ("example", "src", "default"),
            ),
            result.required_roots,
        )
        self.assertEqual(
            (("src/value.test.js", "excluded-category:tests"),),
            result.excluded,
        )
        reasons = {item.path: item.classification_reason for item in result.files}
        self.assertEqual("tracked-types-target", reasons["index.d.ts"])
        self.assertEqual("tracked-declaration-directory", reasons["sibling.d.ts"])
        self.assertEqual("tracked-declaration-directory", reasons["docs/readme.md"])
        self.assertNotIn("src/value.test.js", reasons)

    def test_missing_required_root_and_include_need_policy_review(self):
        tree = self.tree({"package.json": manifest(), "other.js": "other\n"})
        self.assert_policy_review("missing-required-root", tree)
        exact_file = self.tree({"package.json": manifest(), "src": "not a directory\n"})
        self.assert_policy_review("missing-required-root", exact_file)
        valid_root = self.tree(
            {
                "package.json": manifest(),
                "other/ok.js": "other\n",
            }
        )
        self.assert_policy_review(
            "missing-required-include",
            valid_root,
            self.capsule(default_required_roots=("other",), include_paths=("missing.js",)),
        )

    def test_selected_unsafe_paths_modes_and_contents_fail_but_excluded_ones_do_not(self):
        cases = {
            "lfs-pointer": (
                b"version https://git-lfs.github.com/spec/v1\noid sha256:abc\n",
                "unsafe-required-file",
            ),
            "non-utf8": (b"\xff", "unsafe-required-file"),
            "nul": (b"before\0after", "unsafe-required-file"),
            "oversize": (b"x" * 100, "capsule-budget-exceeded"),
        }
        for label, (content, error_code) in cases.items():
            with self.subTest(label=label):
                tree = self.tree(
                    {"package.json": manifest(), "src/value.js": content},
                    max_blob_bytes=1000,
                )
                capsule = self.capsule(max_file_bytes=50 if label == "oversize" else 1000)
                self.assert_policy_review(error_code, tree, capsule)

        tree = self.tree(
            {
                "package.json": manifest(),
                "src/bad\\name.js": "unsafe path\n",
            }
        )
        self.assert_policy_review("unsafe-required-file", tree)

        repo = self.new_repo()
        commit_files(repo, {"package.json": manifest(), "src/index.js": "ok\n"}, "base")
        sha = commit_symlink(repo, "src/link.js", "../outside", "add selected symlink")
        self.assert_policy_review("unsafe-required-file", GitTree(repo, sha))

        repo = self.new_repo()
        commit_files(repo, {"package.json": manifest(), "src/index.js": "ok\n"}, "base")
        add_submodule_marker(repo, "src/vendor")
        sha = run_git(repo, "rev-parse", "HEAD")
        self.assert_policy_review("unsafe-required-file", GitTree(repo, sha))

        repo = self.new_repo()
        commit_files(repo, {"package.json": manifest(), "src/index.js": "ok\n"}, "base")
        sha = commit_symlink(repo, "src/tests/link.js", "../outside", "add excluded symlink")
        result = resolve_npm_capsule(GitTree(repo, sha), self.capsule(), ())
        self.assertEqual(
            (("src/tests/link.js", "excluded-category:tests"),),
            result.excluded,
        )

    def test_selected_reads_use_capsule_limit_instead_of_tree_default(self):
        tree = self.tree(
            {
                "package.json": manifest(),
                "src/index.js": "selected source exceeds tiny tree default\n",
            },
            max_blob_bytes=1,
        )
        capsule = self.capsule(max_file_bytes=100)

        with mock.patch.object(tree, "read_blobs", wraps=tree.read_blobs) as read_blobs:
            result = resolve_npm_capsule(tree, capsule, ())

        self.assertEqual(
            ("package.json", "src/index.js"),
            tuple(item.path for item in result.files),
        )
        self.assertEqual(
            mock.call(("package.json", "src/index.js"), max_bytes=100),
            read_blobs.call_args,
        )

    def test_selected_read_preserves_typed_git_object_infrastructure_failure(self):
        tree = self.tree(
            {
                "package.json": manifest(),
                "src/index.js": "source\n",
            }
        )
        sentinel = GitObjectReadError("bounded infrastructure failure")

        with mock.patch.object(tree, "read_blobs", side_effect=sentinel):
            with self.assertRaises(GitObjectReadError) as raised:
                resolve_npm_capsule(tree, self.capsule(), ())

        self.assertIs(sentinel, raised.exception)

    def test_every_secret_detector_positive_variant_and_boundary_is_reported(self):
        positives = {
            "pem-private-key-header-v1": (
                "-----BEGIN " + suffix + "PRIVATE KEY-----" + ending
                for suffix in ("", "RSA ", "EC ", "OPENSSH ", "DSA ")
                for ending in ("", " \t\r\n")
            ),
            "aws-access-key-id-v1": (
                prefix + "A" * 16 for prefix in ("AKIA", "ASIA")
            ),
            "github-token-v1": (
                prefix + "_" + "A" * length
                for prefix in ("ghp", "gho", "ghu", "ghs", "ghr")
                for length in (36, 255)
            ),
        }
        for detector_code, values in positives.items():
            for index, value in enumerate(values):
                with self.subTest(detector=detector_code, index=index):
                    tree = self.tree(
                        {
                            "package.json": manifest(),
                            "src/value.txt": value,
                        }
                    )
                    result = resolve_npm_capsule(
                        tree,
                        self.capsule(),
                        (self.allow(tree, "src/value.txt", detector_code),),
                    )
                    finding = next(
                        item
                        for item in result.secret_findings
                        if item.path == "src/value.txt"
                    )
                    self.assertIsInstance(finding, SecretFinding)
                    self.assertEqual(detector_code, finding.detector_code)
                    self.assertEqual("text-secrets-v1", finding.detector)
                    self.assertEqual(
                        hashlib.sha256(value.encode("utf-8")).hexdigest(),
                        finding.file_sha256,
                    )

    def test_secret_false_positive_boundaries_do_not_match(self):
        pem = "-----BEGIN " + "PRIVATE KEY-----"
        aws = "AKIA" + "A" * 16
        github = "ghp_" + "A" * 36
        values = (
            pem[:-1],
            "x" + pem,
            "-----BEGIN " + "PUBLIC KEY-----",
            aws[:-1],
            "A" + aws,
            aws + "A",
            github[:-1],
            "A" + github,
            "ghp_" + "A" * 256,
            "client_secret",
        )
        for index, value in enumerate(values):
            with self.subTest(index=index):
                tree = self.tree(
                    {"package.json": manifest(), "src/value.txt": value}
                )
                result = resolve_npm_capsule(tree, self.capsule(), ())
                self.assertEqual((), result.secret_findings)

    def test_multiple_findings_are_sorted_unique_and_require_exact_allowlist_triples(self):
        aws = "AKIA" + "A" * 16
        github = "ghp_" + "A" * 36
        secret_text = aws + "\n" + github + "\n" + aws
        tree = self.tree(
            {"package.json": manifest(), "src/secret.txt": secret_text}
        )
        aws_allow = self.allow(tree, "src/secret.txt", "aws-access-key-id-v1")
        github_allow = self.allow(tree, "src/secret.txt", "github-token-v1")

        with self.assertRaisesRegex(ValueError, r"secret-finding") as context:
            resolve_npm_capsule(tree, self.capsule(), (aws_allow,))
        self.assertNotIn(aws, str(context.exception))
        self.assertNotIn(github, str(context.exception))

        wrong_rows = (
            SecretAllowlist("src/secret.txt", "0" * 40, "github-token-v1"),
            SecretAllowlist("src/other.txt", self.blob(tree, "src/secret.txt").oid, "github-token-v1"),
            SecretAllowlist("src/secret.txt", self.blob(tree, "src/secret.txt").oid, "other-detector-v1"),
        )
        for row in wrong_rows:
            with self.subTest(row=row):
                with self.assertRaisesRegex(ValueError, r"secret-finding"):
                    resolve_npm_capsule(tree, self.capsule(), (aws_allow, row))

        result = resolve_npm_capsule(tree, self.capsule(), (github_allow, aws_allow))
        self.assertEqual(
            (
                ("aws-access-key-id-v1", self.blob(tree, "src/secret.txt").oid),
                ("github-token-v1", self.blob(tree, "src/secret.txt").oid),
            ),
            tuple(
                (item.detector_code, item.git_blob_oid)
                for item in result.secret_findings
            ),
        )
        fields = set(SecretFinding.__dataclass_fields__)
        self.assertNotIn("matched_text", fields)
        self.assertNotIn("offset", fields)
        self.assertNotIn(secret_text, repr(result.secret_findings))
        self.assertNotIn(repr(secret_text.encode("utf-8")), repr(result))

    def test_secret_blocking_error_preserves_complete_sorted_structured_findings(self):
        blocked_type = github_capsule_selection.SecretFindingsBlocked
        self.assertTrue(issubclass(blocked_type, ValueError))
        self.assertIn("SecretFindingsBlocked", github_capsule_selection.__all__)

        long_path = (
            "src/"
            + "/".join("long-segment-" + str(index).zfill(2) for index in range(40))
            + "/secret.txt"
        )
        pem = "-----BEGIN " + "PRIVATE KEY-----"
        aws = "AKIA" + "A" * 16
        github = "ghp_" + "A" * 36
        secret_text = pem + "\n" + github + "\n" + aws
        tree = self.tree(
            {
                "package.json": manifest(),
                long_path: secret_text,
            }
        )
        aws_allow = self.allow(tree, long_path, "aws-access-key-id-v1")
        github_allow = self.allow(tree, long_path, "github-token-v1")
        blob = self.blob(tree, long_path)
        digest = hashlib.sha256(secret_text.encode("utf-8")).hexdigest()

        with self.assertRaises(blocked_type) as raised:
            resolve_npm_capsule(
                tree,
                self.capsule(),
                (github_allow, aws_allow),
            )

        error = raised.exception
        self.assertIsInstance(error.findings, tuple)
        self.assertIsInstance(error.unallowlisted_findings, tuple)
        self.assertEqual(
            (
                "aws-access-key-id-v1",
                "github-token-v1",
                "pem-private-key-header-v1",
            ),
            tuple(item.detector_code for item in error.findings),
        )
        self.assertEqual(
            ("pem-private-key-header-v1",),
            tuple(item.detector_code for item in error.unallowlisted_findings),
        )
        for finding in error.findings:
            self.assertEqual(long_path, finding.path)
            self.assertEqual(blob.oid, finding.git_blob_oid)
            self.assertEqual(digest, finding.file_sha256)
            self.assertEqual("text-secrets-v1", finding.detector)
            with self.assertRaises((FrozenInstanceError, AttributeError)):
                finding.path = "changed"
        self.assertGreater(len(long_path), 500)
        self.assertEqual(long_path, error.unallowlisted_findings[0].path)
        with self.assertRaises(AttributeError):
            error.findings = ()
        with self.assertRaises(AttributeError):
            error.unallowlisted_findings = ()
        with self.assertRaises(AttributeError):
            error._evidence = None
        with self.assertRaises(AttributeError):
            error._sealed = False
        with self.assertRaises(AttributeError):
            error.args = ("changed",)
        with self.assertRaises(AttributeError):
            error.new_attribute = "changed"
        with self.assertRaises(AttributeError):
            del error._evidence
        self.assertLessEqual(len(str(error).encode("utf-8")), 200)
        self.assertNotIn(secret_text, str(error))
        self.assertNotIn("offset", str(error).lower())

        try:
            raise error
        except blocked_type as caught:
            self.assertIs(error, caught)

    def test_secret_blocking_error_rejects_duplicate_normative_identities(self):
        blocked_type = github_capsule_selection.SecretFindingsBlocked
        base = SecretFinding(
            "src/secret.txt",
            "a" * 40,
            "github-token-v1",
            "1" * 64,
            "text-secrets-v1",
        )
        conflicts = (
            SecretFinding(
                base.path,
                base.git_blob_oid,
                base.detector_code,
                "2" * 64,
                base.detector,
            ),
            SecretFinding(
                base.path,
                base.git_blob_oid,
                base.detector_code,
                base.file_sha256,
                "different-suite-v1",
            ),
        )

        for conflict in conflicts:
            with self.subTest(conflict=conflict):
                with self.assertRaisesRegex(ValueError, "identity"):
                    blocked_type((base, conflict), (base,))

        with self.assertRaisesRegex(ValueError, "exact finding"):
            blocked_type((base,), (conflicts[0],))

    def test_secret_blocking_error_keeps_complete_triple_sorted_evidence(self):
        blocked_type = github_capsule_selection.SecretFindingsBlocked
        path_a_aws = SecretFinding(
            "src/a.txt",
            "a" * 40,
            "aws-access-key-id-v1",
            "1" * 64,
            "text-secrets-v1",
        )
        path_a_github = SecretFinding(
            "src/a.txt",
            "a" * 40,
            "github-token-v1",
            "1" * 64,
            "text-secrets-v1",
        )
        path_b_pem = SecretFinding(
            "src/b.txt",
            "b" * 40,
            "pem-private-key-header-v1",
            "2" * 64,
            "text-secrets-v1",
        )

        error = blocked_type(
            (path_b_pem, path_a_github, path_a_aws),
            (path_b_pem, path_a_github),
        )

        self.assertEqual(
            (path_a_aws, path_a_github, path_b_pem),
            error.findings,
        )
        self.assertEqual(
            (path_a_github, path_b_pem),
            error.unallowlisted_findings,
        )

    def test_effective_policy_uses_candidate_blobs_not_detector_findings(self):
        tree = self.tree(
            {
                "package.json": manifest(),
                "src/index.js": "ordinary text\n",
                "docs/ignored.md": "ignored\n",
            }
        )
        candidate = self.allow(tree, "src/index.js", "github-token-v1")
        unrelated = self.allow(tree, "docs/ignored.md", "github-token-v1")

        baseline = resolve_npm_capsule(tree, self.capsule(), ())
        result = resolve_npm_capsule(tree, self.capsule(), (unrelated, candidate))

        self.assertEqual((candidate,), result.effective_policy.applicable_secret_allowlist)
        self.assertNotEqual(
            baseline.effective_policy.policy_hash,
            result.effective_policy.policy_hash,
        )
        self.assertEqual((), result.secret_findings)

    def test_effective_policy_preserves_exact_applicable_allowlist_rows_once(self):
        tree = self.tree(
            {
                "package.json": manifest(),
                "src/a.js": "ordinary a\n",
                "src/b.js": "ordinary b\n",
                "docs/ignored.js": "ignored\n",
            }
        )
        expected = (
            self.allow(tree, "src/a.js", "aws-access-key-id-v1"),
            self.allow(tree, "src/a.js", "github-token-v1"),
            self.allow(tree, "src/b.js", "pem-private-key-header-v1"),
        )
        unrelated = self.allow(tree, "docs/ignored.js", "github-token-v1")

        result = resolve_npm_capsule(
            tree,
            self.capsule(),
            tuple(reversed(expected)) + (unrelated,),
        )

        self.assertEqual(expected, result.effective_policy.applicable_secret_allowlist)
        self.assertEqual(len(expected), len(set(result.effective_policy.applicable_secret_allowlist)))

    def test_file_count_and_utf8_byte_budgets_accept_exact_limits_and_reject_one_less(self):
        tree = self.tree(
            {
                "package.json": manifest(),
                "src/a.txt": "é" * 25,
                "src/b.txt": "b",
            }
        )
        candidate_sizes = tuple(
            tree.blob_size(blob.path)
            for blob in tree.blobs()
            if blob.path in ("package.json", "src/a.txt", "src/b.txt")
        )
        total = sum(candidate_sizes)
        maximum = max(candidate_sizes)
        exact = self.capsule(
            max_file_bytes=maximum,
            max_capsule_files=3,
            max_capsule_utf8_bytes=total,
        )

        result = resolve_npm_capsule(tree, exact, ())

        self.assertEqual(3, len(result.files))
        self.assertEqual(total, sum(item.size for item in result.files))
        self.assertEqual(50, next(item.size for item in result.files if item.path == "src/a.txt"))

        self.assert_policy_review(
            "capsule-budget-exceeded",
            tree,
            self.capsule(
                max_file_bytes=maximum - 1,
                max_capsule_files=3,
                max_capsule_utf8_bytes=total,
            ),
        )
        with self.assertRaisesRegex(
            ValueError,
            r"selected file count 3 exceeds max_capsule_files 2$",
        ):
            resolve_npm_capsule(
                tree,
                self.capsule(
                    max_file_bytes=maximum,
                    max_capsule_files=2,
                    max_capsule_utf8_bytes=total,
                ),
                (),
            )
        self.assert_policy_review(
            "capsule-budget-exceeded",
            tree,
            self.capsule(
                max_file_bytes=maximum,
                max_capsule_files=3,
                max_capsule_utf8_bytes=total - 1,
            ),
        )

    def test_package_manifest_limit_is_classified_before_task_five_file_budget(self):
        tree = self.tree(
            {
                "package.json": manifest(),
                "src/a.txt": "a",
            }
        )
        manifest_size = tree.blob_size("package.json")

        exact = resolve_npm_capsule(
            tree,
            self.capsule(max_file_bytes=manifest_size),
            (),
        )
        self.assertEqual(manifest_size, exact.files[0].size)

        self.assert_policy_review(
            "package-manifest-byte-limit",
            tree,
            self.capsule(max_file_bytes=manifest_size - 1),
        )

    def test_results_sort_files_exclusions_findings_and_policy_rows_deterministically(self):
        aws = "ASIA" + "B" * 16
        github = "gho_" + "B" * 36
        tree = self.tree(
            {
                "package.json": manifest(),
                "src/z.js": github,
                "src/a.js": aws,
                "src/z.test.js": "test\n",
                "src/fixtures/a.js": "fixture\n",
            }
        )
        rows = (
            self.allow(tree, "src/z.js", "github-token-v1"),
            self.allow(tree, "src/a.js", "aws-access-key-id-v1"),
        )

        result = resolve_npm_capsule(tree, self.capsule(), tuple(reversed(rows)))

        self.assertEqual(
            tuple(sorted(item.path for item in result.files)),
            tuple(item.path for item in result.files),
        )
        self.assertEqual(tuple(sorted(result.excluded)), result.excluded)
        self.assertEqual(
            tuple(
                sorted(
                    result.secret_findings,
                    key=lambda item: (item.path, item.git_blob_oid, item.detector_code),
                )
            ),
            result.secret_findings,
        )
        self.assertEqual(
            tuple(sorted(rows, key=lambda item: (item.path, item.blob_oid, item.detector_code))),
            result.effective_policy.applicable_secret_allowlist,
        )


if __name__ == "__main__":
    unittest.main()
