import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from github_capsule_policy import CapsuleConfig, PackageOverride  # noqa: E402
from github_git_tree import GitObjectReadError, GitTree  # noqa: E402
from github_npm_workspace import (  # noqa: E402
    DeclaredTarget,
    DependencyEdge,
    WorkspacePackage,
    WorkspaceResolution,
    resolve_workspace,
)
from tests.github_test_support import commit_files, commit_symlink, create_git_repo  # noqa: E402


def manifest(name, version="1.0.0", **values):
    result = {"name": name, "version": version}
    result.update(values)
    return json.dumps(result, separators=(",", ":")) + "\n"


class NpmWorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.repo_number = 0

    def tree(self, files, max_blob_bytes=None):
        repo_root = self.root / ("repo-" + str(self.repo_number))
        repo_root.mkdir()
        self.repo_number += 1
        repo = create_git_repo(repo_root)
        sha = commit_files(repo, files, "add npm workspace fixture")
        if max_blob_bytes is None:
            return GitTree(repo, sha)
        return GitTree(repo, sha, max_blob_bytes=max_blob_bytes)

    def capsule(self, *focus_packages, generated=("dist/",), max_file_bytes=512000):
        return CapsuleConfig(
            id="workspace-test",
            adapter="npm-tracked-source-v1",
            focus_packages=tuple(focus_packages),
            default_generated_target_paths=tuple(generated),
            max_file_bytes=max_file_bytes,
        )

    def test_public_records_are_frozen_and_resolution_uses_tuples(self):
        tree = self.tree({"package.json": manifest("root")})

        resolution = resolve_workspace(tree, self.capsule("root", generated=()))

        self.assertIsInstance(resolution, WorkspaceResolution)
        self.assertIsInstance(resolution.packages[0], WorkspacePackage)
        self.assertIsInstance(resolution.packages, tuple)
        self.assertIsInstance(resolution.dependency_edges, tuple)
        self.assertIsInstance(resolution.external_dependencies, tuple)
        self.assertIsInstance(resolution.declared_targets, tuple)
        self.assertIsInstance(resolution.packages[0].owned_paths, tuple)
        with self.assertRaises(AttributeError):
            resolution.packages[0].reason = "changed"
        with self.assertRaises(TypeError):
            resolution.packages[0].owned_paths[0] = "changed"

    def test_root_package_is_independent_and_list_and_object_workspaces_are_supported(self):
        fixtures = (
            ({"name": "root", "version": "1", "workspaces": ["packages/*"]}, "child"),
            (
                {
                    "name": "root",
                    "version": "1",
                    "workspaces": {"packages": ["packages/*"], "nohoist": ["**/legacy"]},
                },
                "child",
            ),
            ({"name": "root", "version": "1"}, "root"),
        )
        for root_manifest, focus in fixtures:
            with self.subTest(workspaces=root_manifest.get("workspaces", "absent")):
                files = {"package.json": json.dumps(root_manifest)}
                if focus == "child":
                    files["packages/child/package.json"] = manifest("child")
                resolution = resolve_workspace(self.tree(files), self.capsule(focus, generated=()))
                self.assertEqual((focus,), tuple(item.name for item in resolution.packages))

    def test_private_unversioned_workspace_root_is_a_container_not_a_package(self):
        tree = self.tree(
            {
                "package.json": json.dumps(
                    {
                        "name": "@paypal/paypal-js-root",
                        "private": True,
                        "workspaces": ["packages/*"],
                    }
                ),
                "packages/paypal-js/package.json": manifest("@paypal/paypal-js"),
                "packages/paypal-js/src/index.ts": "export const loadScript = 1;\n",
            }
        )

        resolution = resolve_workspace(
            tree,
            self.capsule("@paypal/paypal-js", generated=()),
        )

        self.assertEqual(("@paypal/paypal-js",), tuple(item.name for item in resolution.packages))
        self.assertEqual(("packages/paypal-js",), tuple(item.path for item in resolution.packages))

    def test_capsule_manifest_limit_overrides_constructor_for_root_and_child(self):
        root_manifest = manifest("root", description="r" * 80)
        child_root_manifest = manifest("root", workspaces=["packages/*"])
        child_manifest = manifest("child", description="c" * 120)
        cases = (
            (
                {"package.json": root_manifest},
                "root",
                len(root_manifest.encode("utf-8")),
            ),
            (
                {
                    "package.json": child_root_manifest,
                    "packages/child/package.json": child_manifest,
                },
                "child",
                max(
                    len(child_root_manifest.encode("utf-8")),
                    len(child_manifest.encode("utf-8")),
                ),
            ),
        )
        for files, focus, policy_limit in cases:
            with self.subTest(focus=focus):
                tree = self.tree(files, max_blob_bytes=1)

                resolution = resolve_workspace(
                    tree,
                    self.capsule(
                        focus,
                        generated=(),
                        max_file_bytes=policy_limit,
                    ),
                )

                self.assertEqual((focus,), tuple(item.name for item in resolution.packages))

    def test_capsule_manifest_limit_rejects_root_and_child_one_byte_over(self):
        root_manifest = manifest("root", description="r" * 80)
        child_root_manifest = manifest("root", workspaces=["packages/*"])
        child_manifest = manifest("child", description="c" * 120)
        cases = (
            (
                {"package.json": root_manifest},
                "root",
                len(root_manifest.encode("utf-8")) - 1,
                "package.json",
            ),
            (
                {
                    "package.json": child_root_manifest,
                    "packages/child/package.json": child_manifest,
                },
                "child",
                len(child_manifest.encode("utf-8")) - 1,
                "packages/child/package.json",
            ),
        )
        for files, focus, policy_limit, expected_path in cases:
            with self.subTest(focus=focus):
                tree = self.tree(files, max_blob_bytes=1000000)

                with self.assertRaisesRegex(
                    ValueError,
                    "^needs-policy-review:package-manifest-byte-limit",
                ) as raised:
                    resolve_workspace(
                        tree,
                        self.capsule(
                            focus,
                            generated=(),
                            max_file_bytes=policy_limit,
                        ),
                    )

                self.assertIn(expected_path, str(raised.exception))
                self.assertLess(len(str(raised.exception)), 600)

    def test_manifest_infrastructure_errors_survive_root_and_child_reads(self):
        root_tree = self.tree({"package.json": manifest("root")})
        root_error = GitObjectReadError("root object read failed")
        with self.subTest(package="root"):
            with mock.patch.object(root_tree, "read_json", side_effect=root_error):
                with self.assertRaises(GitObjectReadError) as raised:
                    resolve_workspace(
                        root_tree,
                        self.capsule("root", generated=()),
                    )

            self.assertIs(root_error, raised.exception)

        child_tree = self.tree(
            {
                "package.json": manifest("root", workspaces=["packages/*"]),
                "packages/child/package.json": manifest("child"),
            }
        )
        child_error = GitObjectReadError("child object read failed")
        original_read_json = child_tree.read_json

        def read_json(path, max_bytes=None):
            if path == "packages/child/package.json":
                raise child_error
            return original_read_json(path, max_bytes=max_bytes)

        with self.subTest(package="child"):
            with mock.patch.object(child_tree, "read_json", side_effect=read_json):
                with self.assertRaises(GitObjectReadError) as raised:
                    resolve_workspace(
                        child_tree,
                        self.capsule("child", generated=()),
                    )

            self.assertIs(child_error, raised.exception)

    def test_single_star_expansion_is_sorted_and_overlaps_deduplicate(self):
        tree = self.tree(
            {
                "package.json": manifest(
                    "root",
                    workspaces=["packages/*", "packages/b", "packages/group/*"],
                ),
                "packages/a/package.json": manifest("a"),
                "packages/b/package.json": manifest("b"),
                "packages/group/package.json": manifest("group"),
                "packages/group/c/package.json": manifest("c"),
            }
        )

        resolution = resolve_workspace(tree, self.capsule("b", "a", "c", generated=()))

        self.assertEqual(("a", "b", "c"), tuple(item.name for item in resolution.packages))
        self.assertEqual(("packages/a", "packages/b", "packages/group/c"), tuple(item.path for item in resolution.packages))

    def test_unsupported_workspace_syntax_needs_policy_review(self):
        invalid_patterns = (
            "packages/**",
            "packages/{a,b}",
            "packages/[ab]",
            "!packages/a",
            "packages\\*",
            "/packages/*",
            "packages/../other/*",
            "packages/a*",
            "packages//a",
        )
        for pattern in invalid_patterns:
            with self.subTest(pattern=pattern):
                tree = self.tree({"package.json": manifest("root", workspaces=[pattern])})
                with self.assertRaisesRegex(ValueError, "^needs-policy-review:unsupported-workspace"):
                    resolve_workspace(tree, self.capsule("root", generated=()))

    def test_workspace_objects_and_discovered_directories_are_strict(self):
        invalid_workspaces = (
            {},
            {"packages": "packages/*"},
            {"packages": [], "nohoist": "legacy"},
            {"packages": ["packages/*"], "unknown": []},
            [""],
        )
        for workspaces in invalid_workspaces:
            with self.subTest(workspaces=workspaces):
                tree = self.tree({"package.json": manifest("root", workspaces=workspaces)})
                with self.assertRaisesRegex(ValueError, "^needs-policy-review:unsupported-workspace"):
                    resolve_workspace(tree, self.capsule("root", generated=()))

        tree = self.tree(
            {
                "package.json": manifest("root", workspaces=["packages/*"]),
                "packages/missing/README.md": "tracked directory without a manifest\n",
            }
        )
        with self.assertRaisesRegex(ValueError, "^needs-policy-review:missing-package-manifest"):
            resolve_workspace(tree, self.capsule("root", generated=()))

    def test_package_identity_and_duplicate_names_are_rejected(self):
        invalid = self.tree({"package.json": manifest("BadName")})
        with self.assertRaisesRegex(ValueError, "^needs-policy-review:invalid-package-identity"):
            resolve_workspace(invalid, self.capsule("BadName", generated=()))

        duplicate = self.tree(
            {
                "package.json": manifest("root", workspaces=["packages/*"]),
                "packages/a/package.json": manifest("same"),
                "packages/b/package.json": manifest("same"),
            }
        )
        with self.assertRaisesRegex(ValueError, "^needs-policy-review:duplicate-package-name"):
            resolve_workspace(duplicate, self.capsule("same", generated=()))

        missing_version = self.tree({"package.json": json.dumps({"name": "root"})})
        with self.assertRaisesRegex(ValueError, "^needs-policy-review:invalid-package-identity"):
            resolve_workspace(missing_version, self.capsule("root", generated=()))

        valid = self.tree({"package.json": manifest("root")})
        with self.assertRaisesRegex(ValueError, "^needs-policy-review:ambiguous-package"):
            resolve_workspace(valid, self.capsule("missing", generated=()))

    def test_dependency_closure_normalizes_precedence_metadata_cycles_and_externals(self):
        tree = self.tree(self.monorepo_files())

        resolution = resolve_workspace(tree, self.capsule("@acme/app"))

        self.assertEqual(
            (
                ("@acme/app", "focus"),
                ("@acme/bridge", "internal-dependency"),
                ("@acme/core", "internal-dependency"),
                ("@acme/peer", "internal-peer-dependency"),
                ("@acme/shared", "internal-optional-dependency"),
            ),
            tuple((item.name, item.reason) for item in resolution.packages),
        )
        self.assertIn(
            DependencyEdge("@acme/app", "@acme/shared", "optional-dependency", "link:../shared", True),
            resolution.dependency_edges,
        )
        self.assertNotIn(
            DependencyEdge("@acme/app", "@acme/shared", "dependency", "^1", False),
            resolution.dependency_edges,
        )
        self.assertIn(
            DependencyEdge("@acme/app", "@acme/core", "peer-dependency", "workspace:^", True),
            resolution.dependency_edges,
        )
        self.assertIn(
            DependencyEdge("@acme/app", "@acme/core", "optional-dependency", "file:../core", True),
            resolution.dependency_edges,
        )
        self.assertIn(
            DependencyEdge("@acme/core", "@acme/app", "dependency", "workspace:*", False),
            resolution.dependency_edges,
        )
        self.assertEqual(
            (
                DependencyEdge("@acme/app", "external-peer", "peer-dependency", "^2", False),
                DependencyEdge("@acme/app", "external-runtime", "dependency", "^3", False),
            ),
            resolution.external_dependencies,
        )
        self.assertNotIn("@acme/dev-only", tuple(item.name for item in resolution.packages))

    def test_dependency_manifests_and_peer_metadata_are_strict(self):
        invalid_values = (
            {"dependencies": []},
            {"optionalDependencies": {"dep": 1}},
            {"peerDependencies": {"dep": "1"}, "peerDependenciesMeta": {"missing": {"optional": True}}},
            {"peerDependencies": {"dep": "1"}, "peerDependenciesMeta": {"dep": {}}},
            {"peerDependencies": {"dep": "1"}, "peerDependenciesMeta": {"dep": {"optional": "yes"}}},
            {"peerDependencies": {"dep": "1"}, "peerDependenciesMeta": {"dep": {"optional": True, "extra": 1}}},
        )
        for values in invalid_values:
            with self.subTest(values=values):
                tree = self.tree({"package.json": manifest("root", **values)})
                with self.assertRaisesRegex(ValueError, "^needs-policy-review:malformed-dependency-metadata"):
                    resolve_workspace(tree, self.capsule("root", generated=()))

    def test_local_file_and_link_protocols_must_resolve_to_the_named_workspace(self):
        fixtures = (
            ("file:../b", "packages/a", "packages/b", "wrong-name"),
            ("link:../../outside", "packages/a", "packages/b", "b"),
            ("file:../missing", "packages/a", "packages/b", "b"),
            ("file:/absolute", "packages/a", "packages/b", "b"),
        )
        for specification, source_path, target_path, target_name in fixtures:
            with self.subTest(specification=specification, target_name=target_name):
                tree = self.tree(
                    {
                        "package.json": manifest("root", workspaces=["packages/*"]),
                        source_path + "/package.json": manifest("a", dependencies={"b": specification}),
                        target_path + "/package.json": manifest(target_name),
                    }
                )
                with self.assertRaisesRegex(ValueError, "^needs-policy-review:unsafe-local-dependency"):
                    resolve_workspace(tree, self.capsule("a", generated=()))

    def test_local_file_protocol_can_identify_the_root_workspace(self):
        tree = self.tree(
            {
                "package.json": manifest("root", workspaces=["packages/*"]),
                "packages/a/package.json": manifest("a", dependencies={"root": "file:../.."}),
            }
        )

        resolution = resolve_workspace(tree, self.capsule("a", generated=()))

        self.assertIn(
            DependencyEdge("a", "root", "dependency", "file:../..", False),
            resolution.dependency_edges,
        )

    def test_declarations_record_files_targets_and_tracked_type_roots(self):
        resolution = resolve_workspace(self.tree(self.monorepo_files()), self.capsule("@acme/app"))
        app = next(item for item in resolution.packages if item.name == "@acme/app")

        self.assertEqual(("dist", "src"), app.files)
        self.assertEqual(("types",), app.tracked_declaration_roots)
        self.assertEqual(
            {
                ("main", "./src/index.js", "tracked-required"),
                ("module", "src/index.mjs", "tracked-required"),
                ("types", "./types/index.d.ts", "tracked-required"),
                ("typings", "types/index.d.ts", "tracked-required"),
                ("bin", "./bin/cli.js", "tracked-required"),
            },
            {
                (target.field, target.target, target.status)
                for target in resolution.declared_targets
                if target.field != "exports" and target.package == "@acme/app"
            },
        )

    def test_exports_preserve_json_pointers_condition_order_and_array_order(self):
        resolution = resolve_workspace(self.tree(self.monorepo_files()), self.capsule("@acme/app"))
        targets = {target.json_pointer: target for target in resolution.declared_targets if target.field == "exports"}

        custom = targets["/exports/./custom~1~0condition"]
        self.assertEqual(("custom/~condition",), custom.condition_chain)
        self.assertEqual((), custom.array_indices)
        development = targets["/exports/./import/1/development"]
        self.assertEqual(("import", "development"), development.condition_chain)
        self.assertEqual((1,), development.array_indices)
        blocked = targets["/exports/.~1feature~1*/default/1"]
        self.assertEqual(("default",), blocked.condition_chain)
        self.assertEqual((1,), blocked.array_indices)
        self.assertEqual("blocked-export", blocked.status)
        self.assertEqual("", blocked.target)

    def test_exports_patterns_use_specificity_and_exact_slash_substitution(self):
        resolution = resolve_workspace(self.tree(self.monorepo_files()), self.capsule("@acme/app"))
        rows = [target for target in resolution.declared_targets if target.field == "exports"]
        general = next(target for target in rows if target.target == "./src/features/*.js")
        specific = next(target for target in rows if target.target == "./src/internal/*.js")

        self.assertEqual(("src/features/plain.js",), general.matched_paths)
        self.assertEqual(("src/internal/tool.js",), specific.matched_paths)
        slash_tree = self.tree(
            {
                "package.json": manifest(
                    "root",
                    exports={"./public/*": "./src/*.js"},
                ),
                "src/deep/path.js": "export const value = 1;\n",
            }
        )
        slash = resolve_workspace(slash_tree, self.capsule("root", generated=())).declared_targets[0]
        self.assertEqual("tracked-pattern-required", slash.status)
        self.assertEqual(("src/deep/path.js",), slash.matched_paths)

    def test_more_specific_generated_or_blocked_patterns_shadow_lower_patterns(self):
        for specific_value, expected_status in (("./dist/internal/*.js", "generated-pattern-not-tracked"), (None, "blocked-export")):
            with self.subTest(specific_value=specific_value):
                tree = self.tree(
                    {
                        "package.json": manifest(
                            "root",
                            exports={
                                "./feature/*": "./src/*.js",
                                "./feature/internal/*": specific_value,
                            },
                        ),
                        "src/plain.js": "export {};\n",
                        "src/internal/tool.js": "export {};\n",
                    }
                )

                resolution = resolve_workspace(tree, self.capsule("root", generated=("dist/",)))
                lower = next(target for target in resolution.declared_targets if target.target == "./src/*.js")

                self.assertEqual(("src/plain.js",), lower.matched_paths)
                self.assertTrue(any(target.status == expected_status for target in resolution.declared_targets))

    def test_subpath_shadowing_requires_a_feasible_nonempty_substitution(self):
        cases = (
            ("./ab*", "ab.js", ("src/ab.js",)),
            ("./ab*bc", "abc.js", ("src/abc.js",)),
            ("./ab*bc", "abXbc.js", ()),
            ("./ab*", "abX.js", ()),
            ("./ab*bc", "ab/deep/bc.js", ()),
        )
        for blocking_pattern, filename, expected_paths in cases:
            with self.subTest(pattern=blocking_pattern, filename=filename):
                tree = self.tree(
                    {
                        "package.json": manifest(
                            "root",
                            exports={
                                "./*": "./src/*.js",
                                blocking_pattern: None,
                            },
                        ),
                        "src/" + filename: "export {};\n",
                    }
                )

                resolution = resolve_workspace(
                    tree,
                    self.capsule("root", generated=()),
                )
                lower = next(
                    target
                    for target in resolution.declared_targets
                    if target.target == "./src/*.js"
                )

                self.assertEqual(expected_paths, lower.matched_paths)

    def test_shadowed_lower_pattern_symlinks_are_not_selected(self):
        for specific_value in ("./dist/internal/*.js", None):
            with self.subTest(specific_value=specific_value):
                repo_root = self.root / ("repo-" + str(self.repo_number))
                repo_root.mkdir()
                self.repo_number += 1
                repo = create_git_repo(repo_root)
                commit_files(
                    repo,
                    {
                        "package.json": manifest(
                            "root",
                            exports={
                                "./feature/*": "./src/*.js",
                                "./feature/internal/*": specific_value,
                            },
                        ),
                        "src/plain.js": "export {};\n",
                    },
                    "add shadow fixture",
                )
                sha = commit_symlink(repo, "src/internal/tool.js", "target.js", "add shadowed symlink")

                resolution = resolve_workspace(
                    GitTree(repo, sha),
                    self.capsule("root", generated=("dist/",)),
                )
                lower = next(target for target in resolution.declared_targets if target.target == "./src/*.js")

                self.assertEqual(("src/plain.js",), lower.matched_paths)

    def test_fully_shadowed_types_pattern_does_not_add_a_declaration_root(self):
        tree = self.tree(
            {
                "package.json": manifest(
                    "root",
                    exports={
                        "./feature/*": {"types": "./types/*.d.ts"},
                        "./feature/internal/*": None,
                    },
                ),
                "types/internal/tool.d.ts": "export {};\n",
            }
        )

        resolution = resolve_workspace(tree, self.capsule("root", generated=()))
        lower = next(target for target in resolution.declared_targets if target.target == "./types/*.d.ts")

        self.assertEqual((), lower.matched_paths)
        self.assertEqual((), resolution.packages[0].tracked_declaration_roots)

    def test_null_in_conditions_and_arrays_blocks_only_its_branch(self):
        tree = self.tree(
            {
                "package.json": manifest(
                    "root",
                    exports={
                        ".": {
                            "import": [None, "./src/index.js"],
                            "browser": None,
                            "default": "./src/index.js",
                        }
                    },
                ),
                "src/index.js": "export {};\n",
            }
        )

        targets = resolve_workspace(tree, self.capsule("root", generated=())).declared_targets

        self.assertEqual(2, sum(target.status == "blocked-export" for target in targets))
        self.assertEqual(2, sum(target.status == "tracked-required" for target in targets))

    def test_export_patterns_fail_when_they_select_non_regular_entries(self):
        repo_root = self.root / ("repo-" + str(self.repo_number))
        repo_root.mkdir()
        self.repo_number += 1
        repo = create_git_repo(repo_root)
        commit_files(repo, {"package.json": manifest("root", exports={"./*": "./src/*.js"})}, "add manifest")
        sha = commit_symlink(repo, "src/link.js", "target.js", "add exported symlink")

        with self.assertRaisesRegex(ValueError, "^needs-policy-review:unsafe-declared-target"):
            resolve_workspace(GitTree(repo, sha), self.capsule("root", generated=()))

    def test_root_exports_sugar_accepts_string_null_array_and_conditions(self):
        exports_values = (
            ("./index.js", "tracked-required"),
            (None, "blocked-export"),
            (["./missing.js", "./index.js"], "tracked-required"),
            ({"types": "./index.d.ts", "default": "./index.js"}, "tracked-required"),
        )
        for exports_value, expected_status in exports_values:
            with self.subTest(exports=exports_value):
                tree = self.tree(
                    {
                        "package.json": manifest("root", exports=exports_value),
                        "index.js": "module.exports = {};\n",
                        "index.d.ts": "export {};\n",
                    }
                )
                generated = ("missing.js",) if isinstance(exports_value, list) else ()
                resolution = resolve_workspace(tree, self.capsule("root", generated=generated))
                self.assertTrue(any(target.status == expected_status for target in resolution.declared_targets))
                self.assertTrue(all(target.json_pointer.startswith("/exports") for target in resolution.declared_targets))

    def test_exports_reject_mixed_unsafe_duplicate_and_unsupported_structures(self):
        invalid_exports = (
            {".": "./index.js", "default": "./index.js"},
            {"./bad/../key": "./index.js"},
            {"./bad%2Fkey": "./index.js"},
            {"./bad\\key": "./index.js"},
            {"0": "./index.js"},
            {"": "./index.js"},
            {"./two**": "./src/*.js"},
            {"./one/*": "./src/no-star.js"},
            {"./literal": "./src/*.js"},
            42,
        )
        for exports_value in invalid_exports:
            with self.subTest(exports=exports_value):
                tree = self.tree({"package.json": manifest("root", exports=exports_value), "index.js": "ok\n"})
                with self.assertRaisesRegex(ValueError, "^needs-policy-review:invalid-exports"):
                    resolve_workspace(tree, self.capsule("root", generated=()))

        duplicate = self.tree({"package.json": '{"name":"root","version":"1","exports":{".":"./a.js",".":"./b.js"}}'})
        with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
            resolve_workspace(duplicate, self.capsule("root", generated=()))

    def test_declared_targets_reject_unsafe_targets_and_malformed_fields(self):
        invalid_values = (
            {"main": 1},
            {"module": "../escape.js"},
            {"types": "././types.d.ts"},
            {"bin": []},
            {"bin": {"cli": 1}},
            {"files": "src"},
            {"files": ["src", 1]},
            {"exports": "../escape.js"},
            {"exports": "/absolute.js"},
            {"exports": "package-name"},
            {"exports": "./node_modules/pkg.js"},
        )
        for values in invalid_values:
            with self.subTest(values=values):
                tree = self.tree({"package.json": manifest("root", **values)})
                with self.assertRaisesRegex(ValueError, "^needs-policy-review:(invalid-declaration|invalid-exports)"):
                    resolve_workspace(tree, self.capsule("root", generated=()))

        empty_bin = self.tree({"package.json": manifest("root", bin={})})
        self.assertEqual((), resolve_workspace(empty_bin, self.capsule("root", generated=())).declared_targets)

    def test_wildcard_expansion_rejects_unsafe_git_paths(self):
        tree = self.tree(
            {
                "package.json": manifest("root", exports={"./*": "./src/*.js"}),
                "src/unsafe\\name.js": "export {};\n",
            }
        )

        with self.assertRaisesRegex(ValueError, "^needs-policy-review:unsafe-declared-target"):
            resolve_workspace(tree, self.capsule("root", generated=()))

    def test_generated_targets_are_explicit_and_unreviewed_missing_targets_fail(self):
        tree = self.tree(
            {
                "package.json": manifest(
                    "root",
                    main="./dist/index.js",
                    exports={"./feature/*": "./dist/features/*.js"},
                )
            }
        )
        resolution = resolve_workspace(tree, self.capsule("root", generated=("dist/",)))
        statuses = {(target.status, target.generated_policy_path) for target in resolution.declared_targets}
        self.assertEqual(
            {
                ("generated-target-not-tracked", "dist/"),
                ("generated-pattern-not-tracked", "dist/"),
            },
            statuses,
        )

        with self.assertRaisesRegex(ValueError, "^needs-policy-review:untracked-declared-target"):
            resolve_workspace(tree, self.capsule("root", generated=()))

        directory_itself = self.tree({"package.json": manifest("root", main="./dist")})
        with self.assertRaisesRegex(ValueError, "^needs-policy-review:untracked-declared-target"):
            resolve_workspace(directory_itself, self.capsule("root", generated=("dist/",)))

    def test_generated_pattern_directory_matching_is_segment_safe(self):
        for target in ("./dist/*.js", "./dist/sub*.js"):
            with self.subTest(target=target):
                tree = self.tree({"package.json": manifest("root", exports={"./*": target})})
                declared = resolve_workspace(
                    tree,
                    self.capsule("root", generated=("dist/",)),
                ).declared_targets[0]
                self.assertEqual("generated-pattern-not-tracked", declared.status)
                self.assertEqual("dist/", declared.generated_policy_path)

        unsafe_boundary = self.tree(
            {"package.json": manifest("root", exports={"./*": "./dist*.js"})}
        )
        with self.assertRaisesRegex(ValueError, "^needs-policy-review:untracked-declared-target"):
            resolve_workspace(
                unsafe_boundary,
                self.capsule("root", generated=("dist/",)),
            )

    def test_each_blob_is_owned_by_the_deepest_root_or_child_package(self):
        tree = self.tree(
            {
                "package.json": manifest(
                    "root",
                    workspaces=["packages/*"],
                    exports={"./child/*": "./packages/child/src/*.js"},
                ),
                "packages/child/package.json": manifest(
                    "child",
                    exports={".": "./package.json", "./source/*": "./src/*.js"},
                ),
                "packages/child/src/index.js": "export {};\n",
            }
        )

        with self.assertRaisesRegex(ValueError, "^needs-policy-review:foreign-package-target"):
            resolve_workspace(tree, self.capsule("root", generated=()))

        child = resolve_workspace(tree, self.capsule("child", generated=()))
        self.assertEqual(("packages/child",), tuple(package.path for package in child.packages))
        self.assertEqual(
            {("package.json",), ("src/index.js",)},
            {target.matched_paths for target in child.declared_targets},
        )

    def test_owned_paths_expose_root_and_child_blobs_without_changing_manifest_files(self):
        tree = self.tree(
            {
                "package.json": manifest(
                    "root",
                    workspaces=["packages/*"],
                    files=["declared-root"],
                ),
                "zeta.txt": "z\n",
                "metadata/space name.json": "{}\n",
                "metadata/unsafe\\name.json": "{}\n",
                "alpha.txt": "a\n",
                "packages/child/package.json": manifest(
                    "child",
                    files=["dist", "src"],
                ),
                "packages/child/src/index.js": "export {};\n",
                "packages/child/.metadata.json": "{}\n",
                "packages/child/unsafe\\metadata.json": "{}\n",
            }
        )

        resolution = resolve_workspace(
            tree,
            self.capsule("root", "child", generated=()),
        )
        root = next(package for package in resolution.packages if package.name == "root")
        child = next(package for package in resolution.packages if package.name == "child")

        self.assertEqual(("declared-root",), root.files)
        self.assertEqual(("dist", "src"), child.files)
        self.assertEqual(
            (
                "alpha.txt",
                "metadata/space name.json",
                "metadata/unsafe\\name.json",
                "package.json",
                "zeta.txt",
            ),
            root.owned_paths,
        )
        self.assertEqual(
            (
                ".metadata.json",
                "package.json",
                "src/index.js",
                "unsafe\\metadata.json",
            ),
            child.owned_paths,
        )
        self.assertFalse(any(path.startswith("packages/child") for path in root.owned_paths))

    def test_owned_paths_expose_parent_and_nested_child_at_their_deepest_boundaries(self):
        tree = self.tree(
            {
                "package.json": manifest(
                    "root",
                    workspaces=["packages/*", "packages/parent/nested/*"],
                ),
                "packages/parent/package.json": manifest("parent"),
                "packages/parent/zeta.txt": "z\n",
                "packages/parent/alpha.txt": "a\n",
                "packages/parent/nested/child/package.json": manifest("nested-child"),
                "packages/parent/nested/child/src/index.js": "export {};\n",
            }
        )

        resolution = resolve_workspace(
            tree,
            self.capsule("parent", "nested-child", generated=()),
        )
        parent = next(package for package in resolution.packages if package.name == "parent")
        child = next(
            package
            for package in resolution.packages
            if package.name == "nested-child"
        )

        self.assertEqual(
            ("alpha.txt", "package.json", "zeta.txt"),
            parent.owned_paths,
        )
        self.assertEqual(
            ("package.json", "src/index.js"),
            child.owned_paths,
        )
        self.assertFalse(
            any(path.startswith("nested/child") for path in parent.owned_paths)
        )

    def test_one_segment_workspace_is_deeper_than_the_repository_root(self):
        tree = self.tree(
            {
                "package.json": manifest(
                    "root",
                    workspaces=["*"],
                    exports={"./child/*": "./child/src/*.js"},
                ),
                "child/package.json": manifest(
                    "child",
                    exports={".": "./package.json", "./source/*": "./src/*.js"},
                ),
                "child/src/index.js": "export {};\n",
            }
        )

        with self.assertRaisesRegex(ValueError, "^needs-policy-review:foreign-package-target"):
            resolve_workspace(tree, self.capsule("root", generated=()))

        child = resolve_workspace(tree, self.capsule("child", generated=()))
        self.assertEqual(
            {("package.json",), ("src/index.js",)},
            {target.matched_paths for target in child.declared_targets},
        )

    def test_each_blob_is_owned_by_the_deepest_parent_or_nested_package(self):
        tree = self.tree(
            {
                "package.json": manifest(
                    "root",
                    workspaces=["packages/*", "packages/parent/nested/*"],
                ),
                "packages/parent/package.json": manifest(
                    "parent",
                    exports={"./child/*": "./nested/child/src/*.js"},
                ),
                "packages/parent/nested/child/package.json": manifest(
                    "nested-child",
                    exports={".": "./package.json", "./source/*": "./src/*.js"},
                ),
                "packages/parent/nested/child/src/index.js": "export {};\n",
            }
        )

        with self.assertRaisesRegex(ValueError, "^needs-policy-review:foreign-package-target"):
            resolve_workspace(tree, self.capsule("parent", generated=()))

        child = resolve_workspace(tree, self.capsule("nested-child", generated=()))
        self.assertEqual(
            ("packages/parent/nested/child",),
            tuple(package.path for package in child.packages),
        )
        self.assertEqual(
            {("package.json",), ("src/index.js",)},
            {target.matched_paths for target in child.declared_targets},
        )

    def test_generated_policy_cannot_reclassify_a_foreign_child_literal(self):
        tree = self.tree(
            {
                "package.json": manifest(
                    "root",
                    workspaces=["packages/*"],
                    main="./packages/child/index.js",
                ),
                "packages/child/package.json": manifest("child"),
                "packages/child/index.js": "module.exports = {};\n",
            }
        )

        with self.assertRaisesRegex(ValueError, "^needs-policy-review:foreign-package-target"):
            resolve_workspace(
                tree,
                self.capsule("root", generated=("packages/child/",)),
            )

    def test_generated_policy_cannot_reclassify_a_foreign_child_pattern(self):
        tree = self.tree(
            {
                "package.json": manifest(
                    "root",
                    workspaces=["packages/*"],
                    exports={"./child/*": "./packages/child/src/*.js"},
                ),
                "packages/child/package.json": manifest("child"),
                "packages/child/src/index.js": "export {};\n",
            }
        )

        with self.assertRaisesRegex(ValueError, "^needs-policy-review:foreign-package-target"):
            resolve_workspace(
                tree,
                self.capsule("root", generated=("packages/child/",)),
            )

    def test_parent_generated_policy_cannot_reclassify_nested_package_targets(self):
        declarations = (
            {"main": "./nested/child/index.js"},
            {"exports": {"./child/*": "./nested/child/src/*.js"}},
        )
        for declaration in declarations:
            with self.subTest(declaration=declaration):
                tree = self.tree(
                    {
                        "package.json": manifest(
                            "root",
                            workspaces=["packages/*", "packages/parent/nested/*"],
                        ),
                        "packages/parent/package.json": manifest("parent", **declaration),
                        "packages/parent/nested/child/package.json": manifest("nested-child"),
                        "packages/parent/nested/child/index.js": "module.exports = {};\n",
                        "packages/parent/nested/child/src/index.js": "export {};\n",
                    }
                )

                with self.assertRaisesRegex(ValueError, "^needs-policy-review:foreign-package-target"):
                    resolve_workspace(
                        tree,
                        self.capsule("parent", generated=("nested/child/",)),
                    )

    def test_owned_pattern_match_cannot_hide_a_foreign_package_match(self):
        tree = self.tree(
            {
                "package.json": manifest(
                    "root",
                    workspaces=["packages/*"],
                    exports={"./all/*": "./*.js"},
                ),
                "root.js": "export {};\n",
                "packages/child/package.json": manifest("child"),
                "packages/child/child.js": "export {};\n",
            }
        )

        with self.assertRaisesRegex(ValueError, "^needs-policy-review:foreign-package-target"):
            resolve_workspace(
                tree,
                self.capsule("root", generated=("packages/child/",)),
            )

    def test_foreign_pattern_failure_preserves_nonregular_mode_metadata(self):
        repo_root = self.root / ("repo-" + str(self.repo_number))
        repo_root.mkdir()
        self.repo_number += 1
        repo = create_git_repo(repo_root)
        commit_files(
            repo,
            {
                "package.json": manifest(
                    "root",
                    workspaces=["packages/*"],
                    exports={"./child/*": "./packages/child/src/*.js"},
                ),
                "packages/child/package.json": manifest("child"),
            },
            "add foreign symlink fixture",
        )
        sha = commit_symlink(
            repo,
            "packages/child/src/link.js",
            "target.js",
            "add foreign symlink",
        )

        with self.assertRaisesRegex(ValueError, "^needs-policy-review:foreign-package-target") as raised:
            resolve_workspace(
                GitTree(repo, sha),
                self.capsule("root", generated=("packages/child/",)),
            )

        self.assertIn("packages/child/src/link.js", str(raised.exception))
        self.assertIn("mode=120000", str(raised.exception))
        self.assertLess(len(str(raised.exception)), 600)

    def test_missing_descendant_literals_cannot_use_generated_policy(self):
        cases = (
            ("./packages/child/dist/missing.js", ("packages/child/",)),
            ("./packages/child", ("packages/child",)),
        )
        for target, generated in cases:
            with self.subTest(target=target):
                tree = self.tree(
                    {
                        "package.json": manifest(
                            "root",
                            workspaces=["packages/*"],
                            main=target,
                        ),
                        "packages/child/package.json": manifest("child"),
                    }
                )

                with self.assertRaisesRegex(
                    ValueError,
                    "^needs-policy-review:descendant-package-target",
                ) as raised:
                    resolve_workspace(tree, self.capsule("root", generated=generated))

                self.assertIn("packages/child", str(raised.exception))
                self.assertLess(len(str(raised.exception)), 600)

    def test_unmatched_descendant_pattern_cannot_use_generated_policy(self):
        tree = self.tree(
            {
                "package.json": manifest(
                    "root",
                    workspaces=["packages/*"],
                    exports={"./child/*": "./packages/child/dist/*.js"},
                ),
                "packages/child/package.json": manifest("child"),
            }
        )

        with self.assertRaisesRegex(
            ValueError,
            "^needs-policy-review:descendant-package-target",
        ):
            resolve_workspace(
                tree,
                self.capsule("root", generated=("packages/child/",)),
            )

    def test_parent_cannot_generate_missing_nested_package_targets(self):
        cases = (
            (
                {"main": "./nested/child/dist/missing.js"},
                ("nested/child/",),
            ),
            (
                {"exports": {"./child/*": "./nested/child/dist/*.js"}},
                ("nested/child/",),
            ),
            ({"main": "./nested/child"}, ("nested/child",)),
        )
        for declaration, generated in cases:
            with self.subTest(declaration=declaration):
                tree = self.tree(
                    {
                        "package.json": manifest(
                            "root",
                            workspaces=["packages/*", "packages/parent/nested/*"],
                        ),
                        "packages/parent/package.json": manifest(
                            "parent",
                            **declaration,
                        ),
                        "packages/parent/nested/child/package.json": manifest(
                            "nested-child"
                        ),
                    }
                )

                with self.assertRaisesRegex(
                    ValueError,
                    "^needs-policy-review:descendant-package-target",
                ):
                    resolve_workspace(
                        tree,
                        self.capsule("parent", generated=generated),
                    )

    def test_descendant_boundary_is_segment_aware_for_generated_targets(self):
        tree = self.tree(
            {
                "package.json": manifest(
                    "root",
                    workspaces=["packages/*"],
                    main="./packages/childish/dist/missing.js",
                    exports={"./neighbor/*": "./packages/childish/dist/*.js"},
                ),
                "packages/child/package.json": manifest("child"),
            }
        )

        resolution = resolve_workspace(
            tree,
            self.capsule("root", generated=("packages/childish/",)),
        )

        self.assertEqual(
            {
                ("generated-target-not-tracked", "packages/childish/"),
                ("generated-pattern-not-tracked", "packages/childish/"),
            },
            {
                (target.status, target.generated_policy_path)
                for target in resolution.declared_targets
            },
        )

    def test_package_does_not_treat_its_own_root_as_a_descendant(self):
        tree = self.tree(
            {
                "package.json": manifest("root", workspaces=["packages/*"]),
                "packages/child/package.json": manifest(
                    "child",
                    main="./dist/missing.js",
                ),
            }
        )

        target = resolve_workspace(
            tree,
            self.capsule("child", generated=("dist/",)),
        ).declared_targets[0]

        self.assertEqual("generated-target-not-tracked", target.status)
        self.assertEqual("dist/", target.generated_policy_path)

    def test_unmatched_pattern_prefixes_cannot_expand_into_a_descendant(self):
        cases = (
            ("./packages/*.js", ("packages/",)),
            ("./packages/ch*.js", ("packages/",)),
            ("./*.js", ("packages/child/",)),
        )
        for target, generated in cases:
            with self.subTest(target=target):
                tree = self.tree(
                    {
                        "package.json": manifest(
                            "root",
                            workspaces=["packages/*"],
                            exports={"./feature/*": target},
                        ),
                        "packages/child/package.json": manifest("child"),
                    }
                )

                with self.assertRaisesRegex(
                    ValueError,
                    "^needs-policy-review:descendant-package-target",
                ):
                    resolve_workspace(tree, self.capsule("root", generated=generated))

    def test_fully_shadowed_tracked_foreign_pattern_remains_unselected(self):
        for specific_value in ("./dist/internal/*.js", None):
            with self.subTest(specific_value=specific_value):
                tree = self.tree(
                    {
                        "package.json": manifest(
                            "root",
                            workspaces=["packages/*"],
                            exports={
                                "./feature/*": "./packages/*.js",
                                "./feature/child/*": specific_value,
                            },
                        ),
                        "packages/child/package.json": manifest("child"),
                        "packages/child/tool.js": "export {};\n",
                    }
                )

                resolution = resolve_workspace(
                    tree,
                    self.capsule("root", generated=("dist/",)),
                )
                lower = next(
                    target
                    for target in resolution.declared_targets
                    if target.target == "./packages/*.js"
                )

                self.assertEqual((), lower.matched_paths)

    def test_export_patterns_reject_braces_and_character_classes_only_when_patterned(self):
        invalid_exports = (
            {"./feature/{literal}/*": "./src/*.js"},
            {"./feature/[ab]/*": "./src/*.js"},
            {"./feature/*": "./src/{literal}/*.js"},
            {"./feature/*": "./src/[ab]/*.js"},
        )
        for exports_value in invalid_exports:
            with self.subTest(exports=exports_value):
                tree = self.tree({"package.json": manifest("root", exports=exports_value)})
                with self.assertRaisesRegex(ValueError, "^needs-policy-review:invalid-exports"):
                    resolve_workspace(tree, self.capsule("root", generated=()))

        literals = self.tree(
            {
                "package.json": manifest(
                    "root",
                    exports={
                        "./{literal}": "./src/{literal}.js",
                        "./[ab]": "./src/[ab].js",
                    },
                ),
                "src/{literal}.js": "export {};\n",
                "src/[ab].js": "export {};\n",
            }
        )
        targets = resolve_workspace(literals, self.capsule("root", generated=())).declared_targets
        self.assertEqual(
            {("src/{literal}.js",), ("src/[ab].js",)},
            {target.matched_paths for target in targets},
        )

    def test_package_override_replaces_default_generated_targets(self):
        tree = self.tree({"package.json": manifest("root", main="./build/index.js")})
        capsule = CapsuleConfig(
            id="workspace-test",
            adapter="npm-tracked-source-v1",
            focus_packages=("root",),
            default_generated_target_paths=("dist/",),
            package_overrides=(PackageOverride("root", ("src",), ("build/",), ()),),
        )

        target = resolve_workspace(tree, capsule).declared_targets[0]

        self.assertEqual("generated-target-not-tracked", target.status)
        self.assertEqual("build/", target.generated_policy_path)

    def test_export_types_add_the_complete_top_level_declaration_root(self):
        tree = self.tree(
            {
                "package.json": manifest("root", exports={".": {"types": "./declarations/index.d.ts"}}),
                "declarations/index.d.ts": "export {};\n",
                "declarations/nested/other.d.ts": "export {};\n",
            }
        )

        package = resolve_workspace(tree, self.capsule("root", generated=())).packages[0]

        self.assertEqual(("declarations",), package.tracked_declaration_roots)

    def test_resolver_never_executes_node_or_package_scripts(self):
        tree = self.tree({"package.json": manifest("root", scripts={"postinstall": "exit 99"})})

        with mock.patch("github_git_tree.subprocess.run", wraps=subprocess.run) as run:
            resolve_workspace(tree, self.capsule("root", generated=()))

        commands = [call.args[0] for call in run.call_args_list]
        self.assertTrue(commands)
        self.assertTrue(all(command[0] == "git" for command in commands))

    def monorepo_files(self):
        root = manifest(
            "@acme/root",
            workspaces={
                "packages": ["packages/*", "packages/app", "packages/group/*"],
                "nohoist": ["**/legacy"],
            },
        )
        app = manifest(
            "@acme/app",
            dependencies={
                "@acme/bridge": "workspace:*",
                "@acme/shared": "^1",
                "external-runtime": "^3",
            },
            optionalDependencies={
                "@acme/core": "file:../core",
                "@acme/shared": "link:../shared",
            },
            peerDependencies={
                "@acme/core": "workspace:^",
                "@acme/peer": "workspace:*",
                "external-peer": "^2",
            },
            peerDependenciesMeta={"@acme/core": {"optional": True}},
            devDependencies={"@acme/dev-only": "workspace:*"},
            main="./src/index.js",
            module="src/index.mjs",
            types="./types/index.d.ts",
            typings="types/index.d.ts",
            bin={"acme": "./bin/cli.js"},
            files=["src", "dist"],
            exports={
                ".": {
                    "types": "./types/index.d.ts",
                    "import": [
                        "./src/index.mjs",
                        {"development": "./src/dev.js", "default": "./dist/index.js"},
                    ],
                    "custom/~condition": "./src/custom.js",
                    "default": "./src/index.js",
                },
                "./feature/internal/*": "./src/internal/*.js",
                "./feature/*": {
                    "types": "./types/features/*.d.ts",
                    "import": "./src/features/*.js",
                    "default": ["./src/fallback/*.js", None],
                },
                "./blocked": None,
                "./generated": "./dist/generated.js",
                "./generated/*": "./dist/features/*.js",
            },
        )
        return {
            "package.json": root,
            "packages/app/package.json": app,
            "packages/app/src/index.js": "module.exports = {};\n",
            "packages/app/src/index.mjs": "export {};\n",
            "packages/app/src/dev.js": "export {};\n",
            "packages/app/src/custom.js": "export {};\n",
            "packages/app/src/features/plain.js": "export {};\n",
            "packages/app/src/features/internal/tool.js": "export {};\n",
            "packages/app/src/internal/tool.js": "export {};\n",
            "packages/app/src/fallback/plain.js": "export {};\n",
            "packages/app/src/fallback/internal/tool.js": "export {};\n",
            "packages/app/types/index.d.ts": "export {};\n",
            "packages/app/types/extra.d.ts": "export {};\n",
            "packages/app/types/features/plain.d.ts": "export {};\n",
            "packages/app/types/features/internal/tool.d.ts": "export {};\n",
            "packages/app/bin/cli.js": "#!/usr/bin/env node\n",
            "packages/bridge/package.json": manifest("@acme/bridge", dependencies={"@acme/core": "workspace:*"}),
            "packages/core/package.json": manifest("@acme/core", dependencies={"@acme/app": "workspace:*"}),
            "packages/shared/package.json": manifest("@acme/shared"),
            "packages/peer/package.json": manifest("@acme/peer"),
            "packages/dev-only/package.json": manifest("@acme/dev-only"),
            "packages/group/package.json": manifest("@acme/group"),
            "packages/group/nested/package.json": manifest("@acme/nested"),
        }


if __name__ == "__main__":
    unittest.main()
