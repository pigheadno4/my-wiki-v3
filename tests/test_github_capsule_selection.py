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
    resolve_npm_capsule,
    scan_evidence_files,
)
import github_capsule_selection  # noqa: E402
from github_git_tree import GitObjectReadError, GitTree  # noqa: E402
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
        self.assertEqual(
            "tracked-declaration-directory",
            reasons["types/fixtures/kept.d.ts"],
        )
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

    def test_changed_release_evidence_is_collected_outside_the_normal_capsule(self):
        tree = self.tree(
            {
                "package.json": manifest(),
                "src/index.ts": "export const value = 1;\n",
                "test/public-api.test.ts": "test('public api', () => {});\n",
                "docs/new-option.md": "# New option\n",
            }
        )

        result = resolve_npm_capsule(
            tree,
            self.capsule(),
            (),
            changed_paths=("test/public-api.test.ts", "docs/new-option.md"),
        )

        selected = {item.path: item.classification_reason for item in result.files}
        self.assertEqual(
            "changed-release-evidence", selected["test/public-api.test.ts"]
        )
        self.assertEqual("changed-release-evidence", selected["docs/new-option.md"])

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

    def test_exclusions_do_not_override_manifest_include_target_or_declaration_rules(self):
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
        self.assertEqual(
            "tracked-declaration-directory",
            reasons["fixtures/types/more.d.ts"],
        )
        self.assertEqual(
            (("src/tests/excluded.js", "excluded-category:tests"),),
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

    def test_root_level_type_target_requires_the_complete_package_declaration_directory(self):
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
        self.assertEqual((), result.excluded)
        reasons = {item.path: item.classification_reason for item in result.files}
        self.assertEqual("tracked-types-target", reasons["index.d.ts"])
        self.assertEqual("tracked-declaration-directory", reasons["sibling.d.ts"])
        self.assertEqual("tracked-declaration-directory", reasons["docs/readme.md"])
        self.assertEqual("required-root", reasons["src/value.test.js"])

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

        with mock.patch.object(tree, "read_blob", wraps=tree.read_blob) as read_blob:
            result = resolve_npm_capsule(tree, capsule, ())

        self.assertEqual(
            ("package.json", "src/index.js"),
            tuple(item.path for item in result.files),
        )
        self.assertIn(
            mock.call("src/index.js", max_bytes=100),
            read_blob.call_args_list,
        )

    def test_selected_read_preserves_typed_git_object_infrastructure_failure(self):
        tree = self.tree(
            {
                "package.json": manifest(),
                "src/index.js": "source\n",
            }
        )
        original_read = tree.read_blob
        sentinel = GitObjectReadError("bounded infrastructure failure")

        def fail_selected(path, max_bytes=None):
            if path == "src/index.js":
                raise sentinel
            return original_read(path, max_bytes=max_bytes)

        with mock.patch.object(tree, "read_blob", side_effect=fail_selected):
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
