import hashlib
import json
import shutil
import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path, PurePosixPath
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from github_canonical import canonical_sha256  # noqa: E402
from github_capsule_policy import CapsuleConfig  # noqa: E402
from github_ingest_packets import (  # noqa: E402
    IngestPacket,
    PackagePacketInput,
    PacketBuildError,
    RefPacketInput,
    build_ingest_packet,
    build_ref_ingest_packet,
    publish_queued_packet,
    publish_review_packet,
)
from github_pilot_store import UpstreamChange  # noqa: E402
from github_registry import RepoConfig, load_registry  # noqa: E402
from tests.github_test_support import write_canonical_json  # noqa: E402


class GitHubIngestPacketTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.config = RepoConfig(
            id="acme/widgets",
            company="acme",
            url="https://github.com/acme/widgets",
            enabled=True,
            repo_type="sdk",
            priority="tier1",
            track="releases-and-default-branch",
            version_strategy="monorepo-packages",
            max_file_bytes=512000,
            max_snapshot_bytes=2000000,
            capsules=(
                CapsuleConfig(
                    id="widget-source",
                    adapter="npm-tracked-source-v1",
                    focus_packages=("@scope/widget",),
                    default_required_roots=("src", ".storybook/stories"),
                    default_generated_target_paths=(),
                    include_paths=("CHANGELOG.md", "docs"),
                    excluded_categories=("tests", "fixtures"),
                    max_packet_files=30,
                    max_packet_utf8_bytes=200000,
                ),
            ),
        )
        self.prior_sha = "a" * 40
        self.current_sha = "b" * 40

    def snapshot(self, sha, version, files, excluded=(), date="2026-07-28"):
        directory = (
            self.root
            / "raw/github/acme/widgets/snapshots"
            / (date + "-" + sha[:7])
        )
        rows = []
        for path, value in sorted(files.items()):
            if isinstance(value, tuple):
                if len(value) == 4:
                    content, purpose, classification, package = value
                else:
                    content, purpose, classification = value
                    package = "@scope/widget"
            else:
                content, purpose, classification = value, "public-source", "required-root"
                package = "@scope/widget"
            content = content.encode("utf-8") if isinstance(content, str) else content
            saved = directory / "files" / path
            saved.parent.mkdir(parents=True, exist_ok=True)
            saved.write_bytes(content)
            if path == "README.md":
                package = ""
            rows.append(
                {
                    "classification_reason": classification,
                    "git_blob_oid": hashlib.sha1(content).hexdigest(),
                    "git_mode": "100644",
                    "package": package,
                    "path": path,
                    "purpose": purpose,
                    "sha256": hashlib.sha256(content).hexdigest(),
                    "size": len(content),
                }
            )
        manifest = {
            "author_date": "2026-07-28T00:00:00Z",
            "collected_date": date,
            "commit_date": "2026-07-28T00:00:00Z",
            "excluded": [
                {"path": path, "reason": reason} for path, reason in excluded
            ],
            "files": rows,
            "format_version": 2,
            "repository": "acme/widgets",
            "sha": sha,
            "triggering_refs": ["@scope/widget@" + version],
        }
        path = directory / "manifest.json"
        write_canonical_json(path, manifest)
        return path

    def release(self, version, sha, notes, package="@scope/widget"):
        slug = package.rsplit("/", 1)[-1]
        directory = (
            self.root
            / "raw/github/acme/widgets/releases"
            / slug
            / version
            / "2026-07-28"
        )
        notes_path = directory / "release-notes.md"
        notes_path.parent.mkdir(parents=True, exist_ok=True)
        notes_path.write_text(notes, encoding="utf-8")
        manifest = {
            "collected_date": "2026-07-28",
            "format_version": 1,
            "notes_available": True,
            "notes_sha256": hashlib.sha256(notes.encode("utf-8")).hexdigest(),
            "package": package,
            "release_date": "2026-07-28T00:00:00Z",
            "repository": "acme/widgets",
            "sha": sha,
            "source_url": "https://api.github.test/releases/" + version,
            "tag": package + "@" + version,
            "version": version,
        }
        path = directory / "manifest.json"
        write_canonical_json(path, manifest)
        return path

    def comparison(
        self,
        from_version,
        to_version,
        changes,
        package="@scope/widget",
    ):
        slug = package.rsplit("/", 1)[-1]
        directory = (
            self.root
            / "tracking/github/repos/acme/widgets/comparisons"
            / slug
            / (from_version + "--" + to_version)
        )
        patch = b"diff fixture\n"
        markdown = b"# Comparison\n"
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "diff.patch").write_bytes(patch)
        (directory / "comparison.md").write_bytes(markdown)
        changed_paths = sorted(
            {
                path
                for item in changes
                for path in (item.old_path, item.new_path)
                if path
            }
        )
        manifest = {
            "changed_paths": changed_paths,
            "format_version": 2,
            "from_sha": self.prior_sha,
            "from_version": from_version,
            "markdown_sha256": hashlib.sha256(markdown).hexdigest(),
            "package": package,
            "patch_sha256": hashlib.sha256(patch).hexdigest(),
            "pathspecs": ["src"],
            "repository": "acme/widgets",
            "to_sha": self.current_sha,
            "to_version": to_version,
            "upstream_changes": [
                {
                    "new_path": item.new_path,
                    "old_path": item.old_path,
                    "status": item.status,
                }
                for item in changes
            ],
        }
        path = directory / "comparison.json"
        write_canonical_json(path, manifest)
        return path

    def manifest_content(self, version, **overrides):
        value = {
            "name": "@scope/widget",
            "version": version,
            "main": "./src/index.ts",
        }
        value.update(overrides)
        return json.dumps(value, sort_keys=True) + "\n"

    def relative(self, path):
        return path.relative_to(self.root).as_posix()

    def build(
        self,
        prior_files,
        current_files,
        changes,
        from_version="10.0.0",
        to_version="10.0.1",
        notes="Routine payment update.\n",
        prior_excluded=(),
        current_excluded=(),
        config=None,
        packet_kind="queued",
    ):
        prior = self.snapshot(
            self.prior_sha,
            from_version,
            prior_files,
            prior_excluded,
            date="2026-07-27",
        )
        current = self.snapshot(
            self.current_sha,
            to_version,
            current_files,
            current_excluded,
        )
        release = self.release(to_version, self.current_sha, notes)
        comparison = self.comparison(from_version, to_version, changes)
        package_input = PackagePacketInput(
            package="@scope/widget",
            from_version=from_version,
            to_version=to_version,
            from_sha=self.prior_sha,
            to_sha=self.current_sha,
            release_manifest=self.relative(release),
            comparison_manifest=self.relative(comparison),
            prior_snapshot_manifest=self.relative(prior),
            upstream_changes=tuple(changes),
        )
        return build_ingest_packet(
            self.root,
            config or self.config,
            "github-" + ("1" * 20) if packet_kind == "queued" else "",
            self.relative(current),
            (package_input,),
            packet_kind,
        )

    def commit_config(self):
        return replace(
            self.config,
            track="default-branch",
            version_strategy="commit",
            capsules=(
                CapsuleConfig(
                    id="sample-source",
                    adapter="commit-tree-v1",
                    source_id="sample-integration",
                    dependency_scope="configured-repository-paths",
                    changed_path_policy="policy-bounded",
                    default_required_roots=("client", "server"),
                    max_packet_files=30,
                    max_packet_utf8_bytes=200000,
                ),
            ),
        )

    def tagged_config(self):
        return replace(
            self.config,
            version_strategy="semver-tags",
            capsules=(
                CapsuleConfig(
                    id="widget-tagged-source",
                    adapter="tagged-tree-v1",
                    focus_packages=("@scope/widget",),
                    dependency_scope="configured-repository-paths",
                    changed_path_policy="policy-bounded",
                    default_required_roots=("src",),
                    include_paths=("README.md", "CHANGELOG.md"),
                    max_packet_files=30,
                    max_packet_utf8_bytes=200000,
                ),
            ),
        )

    def ref_comparison(self, changes):
        directory = (
            self.root
            / "tracking/github/repos/acme/widgets/comparisons/default-branch/"
            / (self.prior_sha[:7] + "--" + self.current_sha[:7])
        )
        patch = b"diff fixture\n"
        markdown = b"# Ref comparison\n"
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "diff.patch").write_bytes(patch)
        (directory / "comparison.md").write_bytes(markdown)
        manifest = {
            "changed_paths": sorted(
                {
                    path
                    for item in changes
                    for path in (item.old_path, item.new_path)
                    if path
                }
            ),
            "format_version": 2,
            "from_sha": self.prior_sha,
            "markdown_sha256": hashlib.sha256(markdown).hexdigest(),
            "patch_sha256": hashlib.sha256(patch).hexdigest(),
            "pathspecs": ["client", "server"],
            "ref_kind": "default-branch",
            "ref_name": "main",
            "repository": "acme/widgets",
            "to_sha": self.current_sha,
            "upstream_changes": [
                {
                    "new_path": item.new_path,
                    "old_path": item.old_path,
                    "status": item.status,
                }
                for item in changes
            ],
        }
        path = directory / "comparison.json"
        write_canonical_json(path, manifest)
        return path

    def test_ref_packet_contains_exact_commit_evidence_and_wiki_targets(self):
        prior = self.snapshot(
            self.prior_sha,
            "baseline",
            {
                "client/button.ts": (
                    "export const button = 1;\n",
                    "source-capsule",
                    "required-root",
                    "sample-integration",
                ),
                "server/orders.ts": (
                    "export const orders = 1;\n",
                    "source-capsule",
                    "required-root",
                    "sample-integration",
                ),
            },
            date="2026-07-27",
        )
        current = self.snapshot(
            self.current_sha,
            "current",
            {
                "client/button.ts": (
                    "export const button = 2;\n",
                    "source-capsule",
                    "required-root",
                    "sample-integration",
                ),
                "server/orders.ts": (
                    "export const orders = 1;\n",
                    "source-capsule",
                    "required-root",
                    "sample-integration",
                ),
            },
            excluded=(("client/button.test.ts", "excluded-category:tests"),),
        )
        change = UpstreamChange("modified", "client/button.ts", "client/button.ts")
        excluded_change = UpstreamChange(
            "modified",
            "client/button.test.ts",
            "client/button.test.ts",
        )
        comparison = self.ref_comparison((change,))
        packet = build_ref_ingest_packet(
            self.root,
            self.commit_config(),
            "github-" + ("3" * 20),
            self.relative(current),
            RefPacketInput(
                ref_kind="default-branch",
                ref_name="main",
                from_sha=self.prior_sha,
                to_sha=self.current_sha,
                comparison_manifest=self.relative(comparison),
                prior_snapshot_manifest=self.relative(prior),
                upstream_changes=(change,),
                excluded_changes=(excluded_change,),
            ),
            "queued",
        )

        self.assertNotIn("packages", packet.document)
        self.assertEqual("default-branch@bbbbbbb", packet.document["ref"]["display_identity"])
        self.assertEqual("2026-07-28T00:00:00Z", packet.document["author_date"])
        self.assertEqual("2026-07-28T00:00:00Z", packet.document["commit_date"])
        self.assertEqual("delta", packet.document["recommendation"]["mode"])
        self.assertEqual(["client/button.ts"], [row["path"] for row in packet.document["selected_changes"]])
        self.assertEqual(
            ["client/button.test.ts"],
            [row["path"] for row in packet.document["excluded_changes"]],
        )
        self.assertEqual([], packet.document["evidence_gaps"])
        self.assertEqual([], packet.document["unclassified_changes"])
        required = packet.document["required_reading"]
        self.assertIn(self.relative(current), required)
        self.assertIn(self.relative(comparison), required)
        self.assertIn(self.relative(current.parent / "files/client/button.ts"), required)
        targets = set(packet.document["expected_wiki_targets"])
        self.assertTrue(
            {
                "wiki/sources/acme/github/source-github-widgets.md",
                "wiki/sources/acme/github/changelog-github-widgets.md",
                "wiki/companies/acme.md",
                "wiki/acme-index.md",
                "wiki/acme-log.md",
                "wiki/log.md",
            }.issubset(targets)
        )
        self.assertTrue(packet.document["concept_audit_required"])
        self.assertIn("default-branch@bbbbbbb", packet.markdown.decode("utf-8"))

    def test_ref_packet_accepts_tagged_tree_capsule_without_release_evidence(self):
        prior = self.snapshot(
            self.prior_sha,
            "1.0.0",
            {
                "README.md": ("# Before\n", "repository-context", "include-path"),
                "CHANGELOG.md": ("# Changes\n", "repository-context", "include-path"),
                "src/message.swift": "let value = 1\n",
            },
            date="2026-07-27",
        )
        current = self.snapshot(
            self.current_sha,
            "unreleased-bbbbbbb",
            {
                "README.md": ("# After\n", "repository-context", "include-path"),
                "CHANGELOG.md": ("# Changes\n", "repository-context", "include-path"),
                "src/message.swift": "let value = 1\n",
            },
        )
        change = UpstreamChange("modified", "README.md", "README.md")
        comparison = self.ref_comparison((change,))

        packet = build_ref_ingest_packet(
            self.root,
            self.tagged_config(),
            "github-" + ("5" * 20),
            self.relative(current),
            RefPacketInput(
                ref_kind="default-branch",
                ref_name="main",
                from_sha=self.prior_sha,
                to_sha=self.current_sha,
                comparison_manifest=self.relative(comparison),
                prior_snapshot_manifest=self.relative(prior),
                upstream_changes=(change,),
                excluded_changes=(),
            ),
            "queued",
        )

        self.assertIn("ref", packet.document)
        self.assertNotIn("packages", packet.document)
        self.assertNotIn("release_manifest", json.dumps(packet.document))
        required = packet.document["required_reading"]
        self.assertIn(self.relative(prior), required)
        self.assertIn(self.relative(current), required)
        self.assertIn(self.relative(comparison), required)
        self.assertIn(
            self.relative(comparison.parent / "comparison.md"),
            required,
        )
        self.assertIn(self.relative(comparison.parent / "diff.patch"), required)

    def test_ref_baseline_is_full_and_reads_every_selected_file(self):
        current = self.snapshot(
            self.current_sha,
            "current",
            {
                "client/button.ts": (
                    "export const button = 1;\n",
                    "source-capsule",
                    "required-root",
                    "sample-integration",
                ),
                "server/orders.ts": (
                    "export const orders = 1;\n",
                    "source-capsule",
                    "required-root",
                    "sample-integration",
                ),
            },
        )

        packet = build_ref_ingest_packet(
            self.root,
            self.commit_config(),
            "github-" + ("4" * 20),
            self.relative(current),
            RefPacketInput(
                ref_kind="default-branch",
                ref_name="main",
                from_sha="",
                to_sha=self.current_sha,
                comparison_manifest="",
                prior_snapshot_manifest="",
                upstream_changes=(),
            ),
            "queued",
        )

        self.assertEqual("full", packet.document["recommendation"]["mode"])
        self.assertIn(
            "initial-commit-baseline",
            packet.document["recommendation"]["reasons"],
        )
        for path in ("client/button.ts", "server/orders.ts"):
            self.assertIn(
                self.relative(current.parent / "files" / path),
                packet.document["required_reading"],
            )

    def test_ref_baseline_classifies_nested_license_as_repository_context(self):
        current = self.snapshot(
            self.current_sha,
            "current",
            {
                "server/node/LICENSE": (
                    "MIT\n",
                    "source-capsule",
                    "include-path",
                ),
            },
        )

        packet = build_ref_ingest_packet(
            self.root,
            self.commit_config(),
            "github-" + ("3" * 20),
            self.relative(current),
            RefPacketInput(
                ref_kind="default-branch",
                ref_name="main",
                from_sha="",
                to_sha=self.current_sha,
                comparison_manifest="",
                prior_snapshot_manifest="",
                upstream_changes=(),
                excluded_changes=(),
            ),
            "queued",
        )

        selected = packet.document["selected_changes"]
        self.assertEqual("repository-context", selected[0]["classification"])
        self.assertEqual([], packet.document["unclassified_changes"])

    def test_retained_diff_accounts_for_rename_without_false_add_remove(self):
        prior = {
            "package.json": self.manifest_content("10.0.0"),
            "src/index.ts": "export const value = 1;\n",
            "src/old.ts": "export const same = true;\n",
            "README.md": ("# Widget\n", "repository-context", "repository-context"),
        }
        current = {
            "package.json": self.manifest_content("10.0.1"),
            "src/index.ts": "export const value = 2;\n",
            "src/new.ts": "export const same = true;\n",
            "README.md": ("# Widget\n", "repository-context", "repository-context"),
        }
        packet = self.build(
            prior,
            current,
            (
                UpstreamChange("modified", "package.json", "package.json"),
                UpstreamChange("modified", "src/index.ts", "src/index.ts"),
                UpstreamChange("renamed", "src/old.ts", "src/new.ts"),
            ),
        )

        retained = packet.document["packages"][0]["retained_evidence"]

        self.assertEqual(
            {"added": 0, "modified": 2, "removed": 0, "renamed": 1, "unchanged": 1},
            retained["counts"],
        )
        statuses = {row["path"]: row["status"] for row in retained["files"]}
        self.assertEqual("renamed", statuses["src/new.ts"])
        self.assertNotIn("src/old.ts", statuses)

    def test_tagged_baseline_builds_without_package_manifest(self):
        config = replace(
            self.config,
            version_strategy="semver-tags",
            capsules=(
                CapsuleConfig(
                    id="stripe-ios-source",
                    adapter="tagged-tree-v1",
                    focus_packages=("stripe-ios",),
                    dependency_scope="configured-repository-paths",
                    changed_path_policy="policy-bounded",
                    default_required_roots=("Native/Source",),
                    include_paths=(
                        "README.md",
                        "LICENSE",
                        "VERSION",
                        "Package.swift",
                        "modules.yaml",
                        "settings.gradle",
                        "dependencies.gradle",
                        "go.mod",
                        "composer.json",
                        "pkg/fixtures/triggers/checkout.session.completed.json",
                        "rpc/common.proto",
                        "Native/api/native.api",
                    ),
                    excluded_categories=("tests", "fixtures"),
                    max_packet_files=30,
                    max_packet_utf8_bytes=200000,
                ),
            ),
        )
        current = self.snapshot(
            self.current_sha,
            "26.4.1",
            {
                "README.md": (
                    "# Native SDK\n",
                    "repository-context",
                    "repository-context",
                    "",
                ),
                "Package.swift": (
                    "// package\n",
                    "public-source",
                    "include-path",
                    "stripe-ios",
                ),
                "LICENSE": (
                    "MIT\n",
                    "public-source",
                    "include-path",
                    "stripe-ios",
                ),
                "VERSION": (
                    "26.4.1\n",
                    "public-source",
                    "include-path",
                    "stripe-ios",
                ),
                "modules.yaml": (
                    "modules: []\n",
                    "public-source",
                    "include-path",
                    "stripe-ios",
                ),
                "settings.gradle": (
                    "rootProject.name = 'native'\n",
                    "public-source",
                    "include-path",
                    "stripe-ios",
                ),
                "dependencies.gradle": (
                    "ext.versions = [:]\n",
                    "public-source",
                    "include-path",
                    "stripe-ios",
                ),
                "go.mod": (
                    "module example.com/checkout\n",
                    "public-source",
                    "include-path",
                    "stripe-ios",
                ),
                "composer.json": (
                    '{"name":"stripe/stripe-php"}\n',
                    "public-source",
                    "include-path",
                    "stripe-ios",
                ),
                "pkg/fixtures/triggers/checkout.session.completed.json": (
                    '{"fixtures": []}\n',
                    "source-capsule",
                    "include-path",
                    "stripe-ios",
                ),
                "rpc/common.proto": (
                    "syntax = \"proto3\";\n",
                    "source-capsule",
                    "include-path",
                    "stripe-ios",
                ),
                "PrivacyInfo.xcprivacy": (
                    "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n",
                    "public-source",
                    "include-path",
                    "stripe-ios",
                ),
                "Native/api/native.api": (
                    "public final class Checkout\n",
                    "public-source",
                    "include-path",
                    "stripe-ios",
                ),
                "Native/Source/Checkout.swift": (
                    "public struct Checkout {}\n",
                    "public-source",
                    "required-root",
                    "stripe-ios",
                ),
                "Native/Resources/ar.lproj/Checkout.strings": (
                    '"checkout" = "Checkout";\n',
                    "public-source",
                    "required-root",
                    "stripe-ios",
                ),
            },
        )
        release = self.release(
            "26.4.1",
            self.current_sha,
            "Native baseline.\n",
            package="stripe-ios",
        )

        packet = build_ingest_packet(
            self.root,
            config,
            "github-" + ("2" * 20),
            self.relative(current),
            (
                PackagePacketInput(
                    package="stripe-ios",
                    from_version="",
                    to_version="26.4.1",
                    from_sha="",
                    to_sha=self.current_sha,
                    release_manifest=self.relative(release),
                    comparison_manifest="",
                    prior_snapshot_manifest="",
                    upstream_changes=(),
                ),
            ),
            "queued",
        )

        package = packet.document["packages"][0]
        self.assertEqual("stripe-ios", package["package"])
        self.assertEqual([], package["dependency_changes"])
        self.assertEqual([], package["public_api_changes"])
        classified = {
            row["path"]: row["classification"]
            for row in package["retained_evidence"]["files"]
        }
        self.assertEqual("repository-context", classified["LICENSE"])
        self.assertEqual("package-manifest", classified["composer.json"])
        for path in (
            "VERSION",
            "Package.swift",
            "modules.yaml",
            "settings.gradle",
            "dependencies.gradle",
            "go.mod",
            "PrivacyInfo.xcprivacy",
        ):
            self.assertEqual("build-configuration", classified[path])
        self.assertEqual(
            "public-source",
            classified["Native/api/native.api"],
        )
        self.assertEqual(
            "public-source",
            classified["pkg/fixtures/triggers/checkout.session.completed.json"],
        )
        self.assertEqual("public-source", classified["rpc/common.proto"])
        self.assertEqual(
            "translation",
            classified["Native/Resources/ar.lproj/Checkout.strings"],
        )
        self.assertTrue(
            any(
                path.endswith("/files/Native/Source/Checkout.swift")
                for path in package["required_reading"]
            )
        )
        self.assertTrue(
            all("package.json" not in path for path in package["required_reading"])
        )

    def test_commit_web_and_environment_files_have_stable_classifications(self):
        config = RepoConfig(
            id="acme/widgets",
            company="acme",
            url="https://github.com/acme/widgets",
            enabled=True,
            repo_type="sample-app",
            priority="tier1",
            track="default-branch",
            version_strategy="commit",
            capsules=(
                CapsuleConfig(
                    id="widget-sample",
                    adapter="commit-tree-v1",
                    source_id="widgets",
                    dependency_scope="configured-repository-paths",
                    changed_path_policy="policy-bounded",
                    default_required_roots=("client", "src"),
                    max_packet_files=30,
                    max_packet_utf8_bytes=200000,
                ),
            ),
        )
        snapshot = self.snapshot(
            self.current_sha,
            "",
            {
                ".env.sample": ("CLIENT_ID=example\n", "source-capsule", "include-path", "widgets"),
                "example.env": ("CLIENT_SECRET=example\n", "source-capsule", "include-path", "widgets"),
                "client/.npmrc": ("engine-strict=true\n", "source-capsule", "required-root", "widgets"),
                "client/.nvmrc": ("22\n", "source-capsule", "required-root", "widgets"),
                "client/index.html": ("<main></main>\n", "source-capsule", "required-root", "widgets"),
                "client/styles.css": ("main { display: block; }\n", "source-capsule", "required-root", "widgets"),
                ".github/workflows/sync.yml": (
                    "name: Sync\n",
                    "source-capsule",
                    "include-path",
                    "widgets",
                ),
                "generateAll.sh": (
                    "#!/bin/sh\n",
                    "source-capsule",
                    "include-path",
                    "widgets",
                ),
                "src/data/products.json": ('{"sku":"sample"}\n', "source-capsule", "required-root", "widgets"),
            },
        )

        packet = build_ref_ingest_packet(
            self.root,
            config,
            "github-" + ("4" * 20),
            self.relative(snapshot),
            RefPacketInput(
                "default-branch",
                "main",
                "",
                self.current_sha,
                "",
                "",
                (),
            ),
            "queued",
        )

        classified = {
            row["path"]: row["classification"]
            for row in packet.document["selected_changes"]
        }
        self.assertEqual("runtime-configuration", classified[".env.sample"])
        self.assertEqual("runtime-configuration", classified["example.env"])
        self.assertEqual("build-configuration", classified["client/.npmrc"])
        self.assertEqual("build-configuration", classified["client/.nvmrc"])
        self.assertEqual("public-source", classified["client/index.html"])
        self.assertEqual("public-source", classified["client/styles.css"])
        self.assertEqual(
            "build-configuration",
            classified[".github/workflows/sync.yml"],
        )
        self.assertEqual("public-source", classified["generateAll.sh"])
        self.assertEqual("public-source", classified["src/data/products.json"])
        self.assertEqual([], packet.document["unclassified_changes"])

    def test_typescript_config_is_classified_as_build_configuration(self):
        prior = {
            "package.json": self.manifest_content("10.0.0"),
            "tsconfig.lib.json": '{"compilerOptions":{"target":"ES2020"}}\n',
        }
        current = {
            "package.json": self.manifest_content("10.1.0"),
            "tsconfig.lib.json": '{"compilerOptions":{"target":"ES2022"}}\n',
        }

        packet = self.build(
            prior,
            current,
            (
                UpstreamChange("modified", "package.json", "package.json"),
                UpstreamChange(
                    "modified",
                    "tsconfig.lib.json",
                    "tsconfig.lib.json",
                ),
            ),
            from_version="10.0.0",
            to_version="10.1.0",
        )

        rows = packet.document["packages"][0]["retained_evidence"]["files"]
        classified = {row["path"]: row["classification"] for row in rows}
        self.assertEqual(
            "build-configuration",
            classified["tsconfig.lib.json"],
        )

    def test_agent_plugin_and_mcp_manifests_are_runtime_configuration(self):
        config = RepoConfig(
            id="acme/widgets",
            company="acme",
            url="https://github.com/acme/widgets",
            enabled=True,
            repo_type="developer-tooling",
            priority="tier2",
            track="default-branch",
            version_strategy="commit",
            capsules=(
                CapsuleConfig(
                    id="widget-tools",
                    adapter="commit-tree-v1",
                    source_id="widgets",
                    dependency_scope="configured-repository-paths",
                    changed_path_policy="policy-bounded",
                    default_required_roots=("tools",),
                    max_packet_files=30,
                    max_packet_utf8_bytes=200000,
                ),
            ),
        )
        manifest_paths = (
            "gemini-extension.json",
            "providers/claude/plugin/.claude-plugin/plugin.json",
            "providers/claude/plugin/.mcp.json",
            "providers/codex/plugin/.app.json",
            "providers/codex/plugin/.codex-plugin/plugin.json",
            "providers/cursor/plugin/.cursor-plugin/plugin.json",
            "providers/cursor/plugin/mcp.json",
            "providers/grok/plugin/.grok-plugin/plugin.json",
            "providers/grok/plugin/.mcp.json",
            "tools/modelcontextprotocol/manifest.json",
            "tools/modelcontextprotocol/server.json",
        )
        files = {
            path: ('{"name":"tool"}\n', "source-capsule", "include-path", "widgets")
            for path in manifest_paths
        }
        files["custom.json"] = (
            '{"name":"custom"}\n',
            "source-capsule",
            "include-path",
            "widgets",
        )
        snapshot = self.snapshot(self.current_sha, "", files)

        packet = build_ref_ingest_packet(
            self.root,
            config,
            "github-" + ("5" * 20),
            self.relative(snapshot),
            RefPacketInput(
                "default-branch",
                "main",
                "",
                self.current_sha,
                "",
                "",
                (),
            ),
            "queued",
        )

        classified = {
            row["path"]: row["classification"]
            for row in packet.document["selected_changes"]
        }
        for path in manifest_paths:
            self.assertEqual("runtime-configuration", classified[path])
        self.assertEqual("unclassified", classified["custom.json"])

    def test_codegen_versions_are_classified_as_build_configuration(self):
        prior = {
            "package.json": self.manifest_content("22.3.2"),
            "CODEGEN_VERSION": "1.0.0\n",
            "OPENAPI_VERSION": "2026-07-01\n",
        }
        current = {
            "package.json": self.manifest_content("22.4.0"),
            "CODEGEN_VERSION": "1.1.0\n",
            "OPENAPI_VERSION": "2026-08-01\n",
        }

        packet = self.build(
            prior,
            current,
            (
                UpstreamChange("modified", "CODEGEN_VERSION", "CODEGEN_VERSION"),
                UpstreamChange("modified", "OPENAPI_VERSION", "OPENAPI_VERSION"),
            ),
            from_version="22.3.2",
            to_version="22.4.0",
        )

        rows = packet.document["packages"][0]["retained_evidence"]["files"]
        classified = {row["path"]: row["classification"] for row in rows}
        self.assertEqual("build-configuration", classified["CODEGEN_VERSION"])
        self.assertEqual("build-configuration", classified["OPENAPI_VERSION"])

    def test_terraform_registry_manifest_is_build_configuration(self):
        prior = {
            "package.json": self.manifest_content("1.0.0"),
            "terraform-registry-manifest.json": '{"version":1}\n',
        }
        current = {
            "package.json": self.manifest_content("1.0.1"),
            "terraform-registry-manifest.json": '{"version":1}\n',
        }

        packet = self.build(
            prior,
            current,
            (),
            from_version="1.0.0",
            to_version="1.0.1",
        )

        rows = packet.document["packages"][0]["retained_evidence"]["files"]
        classified = {row["path"]: row["classification"] for row in rows}
        self.assertEqual(
            "build-configuration",
            classified["terraform-registry-manifest.json"],
        )

    def test_pnpm_workspace_is_build_configuration(self):
        prior = {
            "package.json": self.manifest_content("1.0.0"),
            "pnpm-workspace.yaml": "packages:\n  - packages/*\n",
        }
        current = {
            "package.json": self.manifest_content("1.0.1"),
            "pnpm-workspace.yaml": "packages:\n  - packages/*\n",
        }

        packet = self.build(
            prior,
            current,
            (),
            from_version="1.0.0",
            to_version="1.0.1",
        )

        rows = packet.document["packages"][0]["retained_evidence"]["files"]
        classified = {row["path"]: row["classification"] for row in rows}
        self.assertEqual(
            "build-configuration",
            classified["pnpm-workspace.yaml"],
        )

    def test_eslint_configs_are_classified_as_build_configuration(self):
        prior = {
            "package.json": self.manifest_content("10.0.0"),
            "types/.eslintrc.yml": "rules: {}\n",
            "src/eslint.config.mjs": "export default [];\n",
        }
        current = {
            "package.json": self.manifest_content("10.1.0"),
            "types/.eslintrc.yml": "rules:\n  semi: error\n",
            "src/eslint.config.mjs": "export default [{ rules: {} }];\n",
        }

        packet = self.build(
            prior,
            current,
            (
                UpstreamChange("modified", "package.json", "package.json"),
                UpstreamChange(
                    "modified",
                    "types/.eslintrc.yml",
                    "types/.eslintrc.yml",
                ),
                UpstreamChange(
                    "modified",
                    "src/eslint.config.mjs",
                    "src/eslint.config.mjs",
                ),
            ),
            from_version="10.0.0",
            to_version="10.1.0",
        )

        rows = packet.document["packages"][0]["retained_evidence"]["files"]
        classified = {row["path"]: row["classification"] for row in rows}
        self.assertEqual("build-configuration", classified["types/.eslintrc.yml"])
        self.assertEqual("build-configuration", classified["src/eslint.config.mjs"])

    def test_native_package_metadata_is_classified_as_build_configuration(self):
        native_files = {
            "Cartfile": "github \"example/dependency\"\n",
            "android/build.gradle": "dependencies {}\n",
            "android/gradle.properties": "StripeSdkVersion=1\n",
            "android/gradle/libs.versions.toml": "[versions]\nkotlin = '2.0.0'\n",
            "android/src/main/AndroidManifest.xml": "<manifest />\n",
            "ios/Info.plist": "<?xml version=\"1.0\"?><plist />\n",
            "ios/StripeSdk.entitlements": "<?xml version=\"1.0\"?><plist />\n",
            "ios/StripeSdk.xcodeproj/project.pbxproj": "// project\n",
            "ios/StripeSdk.xcodeproj/xcshareddata/xcschemes/Tests.xcscheme": "<Scheme />\n",
            "ios/StripeSdk.xctestplan": "{}\n",
            "widget.podspec": "Pod::Spec.new do |spec|\nend\n",
        }
        prior = {
            "package.json": self.manifest_content("10.0.0"),
            **native_files,
        }
        current = {
            "package.json": self.manifest_content("10.1.0"),
            **native_files,
        }
        changes = tuple(
            UpstreamChange("modified", path, path)
            for path in sorted(native_files)
        )

        packet = self.build(
            prior,
            current,
            changes,
            from_version="10.0.0",
            to_version="10.1.0",
        )

        rows = packet.document["packages"][0]["retained_evidence"]["files"]
        classified = {row["path"]: row["classification"] for row in rows}
        for path in native_files:
            self.assertEqual("build-configuration", classified[path])

    def test_android_proguard_rules_are_build_configuration(self):
        prior = {
            "package.json": self.manifest_content("10.0.0"),
            "android/proguard.pro": "-keep class com.example.** { *; }\n",
        }
        current = {
            "package.json": self.manifest_content("10.1.0"),
            "android/proguard.pro": "-keep class com.example.** { *; }\n",
        }

        packet = self.build(
            prior,
            current,
            (
                UpstreamChange(
                    "modified",
                    "android/proguard.pro",
                    "android/proguard.pro",
                ),
            ),
            from_version="10.0.0",
            to_version="10.1.0",
        )

        rows = packet.document["packages"][0]["retained_evidence"]["files"]
        classified = {row["path"]: row["classification"] for row in rows}
        self.assertEqual(
            "build-configuration",
            classified["android/proguard.pro"],
        )

    def test_objective_c_sources_are_classified_as_public_source(self):
        sources = {
            "ios/WidgetManager.m": "@implementation WidgetManager\n@end\n",
            "ios/WidgetModule.mm": "@implementation WidgetModule\n@end\n",
        }
        prior = {
            "package.json": self.manifest_content("10.0.0"),
            **sources,
        }
        current = {
            "package.json": self.manifest_content("10.1.0"),
            **sources,
        }

        packet = self.build(
            prior,
            current,
            tuple(
                UpstreamChange("modified", path, path)
                for path in sorted(sources)
            ),
            from_version="10.0.0",
            to_version="10.1.0",
        )

        rows = packet.document["packages"][0]["retained_evidence"]["files"]
        classified = {row["path"]: row["classification"] for row in rows}
        for path in sources:
            self.assertEqual("public-source", classified[path])

    def test_graphql_operations_are_classified_as_public_source(self):
        path = "CardPayments/src/main/res/raw/update_setup_token.graphql"
        prior = {
            "package.json": self.manifest_content("10.0.0"),
            path: "mutation UpdateSetupToken { updateSetupToken { id } }\n",
        }
        current = {
            "package.json": self.manifest_content("10.1.0"),
            path: "mutation UpdateSetupToken { updateSetupToken { id status } }\n",
        }

        packet = self.build(
            prior,
            current,
            (UpstreamChange("modified", path, path),),
            from_version="10.0.0",
            to_version="10.1.0",
        )

        rows = packet.document["packages"][0]["retained_evidence"]["files"]
        classified = {row["path"]: row["classification"] for row in rows}
        self.assertEqual("public-source", classified[path])

    def test_typescript_module_sources_are_classified_as_public_source(self):
        prior = {
            "package.json": self.manifest_content("10.0.0"),
            "lib/index.d.mts": "export type Widget = string;\n",
            "lib/index.d.cts": "export type Widget = string;\n",
        }
        current = {
            "package.json": self.manifest_content("10.1.0"),
            "lib/index.d.mts": "export type Widget = string | number;\n",
            "lib/index.d.cts": "export type Widget = string | number;\n",
        }

        packet = self.build(
            prior,
            current,
            (
                UpstreamChange("modified", "package.json", "package.json"),
                UpstreamChange(
                    "modified",
                    "lib/index.d.mts",
                    "lib/index.d.mts",
                ),
                UpstreamChange(
                    "modified",
                    "lib/index.d.cts",
                    "lib/index.d.cts",
                ),
            ),
            from_version="10.0.0",
            to_version="10.1.0",
        )

        rows = packet.document["packages"][0]["retained_evidence"]["files"]
        classified = {row["path"]: row["classification"] for row in rows}
        self.assertEqual("public-source", classified["lib/index.d.mts"])
        self.assertEqual("public-source", classified["lib/index.d.cts"])

    def test_baseline_is_full_and_reads_every_current_snapshot_file(self):
        files = {
            "package.json": self.manifest_content("8.0.0"),
            "src/index.ts": "export const value = 1;\n",
            ".storybook/stories/example.stories.ts": "export default {};\n",
        }
        current = self.snapshot(self.current_sha, "8.0.0", files)
        release = self.release("8.0.0", self.current_sha, "Initial release.\n")
        packet = build_ingest_packet(
            self.root,
            self.config,
            "github-" + ("2" * 20),
            self.relative(current),
            (
                PackagePacketInput(
                    package="@scope/widget",
                    from_version="",
                    to_version="8.0.0",
                    from_sha="",
                    to_sha=self.current_sha,
                    release_manifest=self.relative(release),
                    comparison_manifest="",
                    prior_snapshot_manifest="",
                    upstream_changes=(),
                ),
            ),
            "queued",
        )

        self.assertEqual("full", packet.document["recommendation"]["mode"])
        required = packet.document["required_reading"]
        for path in files:
            self.assertIn(
                self.relative(current.parent / "files" / path),
                required,
            )
        self.assertIn(
            "wiki/sources/acme/github/source-github-widgets.md",
            packet.document["expected_wiki_targets"],
        )

    def test_extensionless_package_bin_target_is_public_source(self):
        files = {
            "package.json": self.manifest_content("8.0.0"),
            "bin/cli": (
                "#!/usr/bin/env node\n",
                "public-source",
                "tracked-bin-target",
            ),
            "src/index.ts": "export const value = 1;\n",
        }
        current = self.snapshot(self.current_sha, "8.0.0", files)
        release = self.release("8.0.0", self.current_sha, "Initial release.\n")

        packet = build_ingest_packet(
            self.root,
            self.config,
            "github-" + ("2" * 20),
            self.relative(current),
            (
                PackagePacketInput(
                    package="@scope/widget",
                    from_version="",
                    to_version="8.0.0",
                    from_sha="",
                    to_sha=self.current_sha,
                    release_manifest=self.relative(release),
                    comparison_manifest="",
                    prior_snapshot_manifest="",
                    upstream_changes=(),
                ),
            ),
            "queued",
        )

        classified = {
            row["path"]: row["classification"]
            for row in packet.document["packages"][0]["retained_evidence"]["files"]
        }
        self.assertEqual("public-source", classified["bin/cli"])

    def test_keep_file_is_documentation(self):
        files = {
            "package.json": self.manifest_content("8.0.0"),
            "src/index.ts": "export const value = 1;\n",
            "src/lib/.keep": "Generated source extension directory.\n",
        }
        current = self.snapshot(self.current_sha, "8.0.0", files)
        release = self.release("8.0.0", self.current_sha, "Initial release.\n")

        packet = build_ingest_packet(
            self.root,
            self.config,
            "github-" + ("2" * 20),
            self.relative(current),
            (
                PackagePacketInput(
                    package="@scope/widget",
                    from_version="",
                    to_version="8.0.0",
                    from_sha="",
                    to_sha=self.current_sha,
                    release_manifest=self.relative(release),
                    comparison_manifest="",
                    prior_snapshot_manifest="",
                    upstream_changes=(),
                ),
            ),
            "queued",
        )

        classified = {
            row["path"]: row["classification"]
            for row in packet.document["packages"][0]["retained_evidence"]["files"]
        }
        self.assertEqual("documentation", classified["src/lib/.keep"])

    def test_same_major_payment_change_is_delta_with_high_priority(self):
        prior = {
            "package.json": self.manifest_content("10.0.0"),
            "src/venmo/client.ts": "export const value = 1;\n",
            "src/unchanged.ts": "export const unchanged = true;\n",
        }
        current = {
            "package.json": self.manifest_content("10.0.1"),
            "src/venmo/client.ts": "export const value = 2;\n",
            "src/unchanged.ts": "export const unchanged = true;\n",
        }

        packet = self.build(
            prior,
            current,
            (
                UpstreamChange("modified", "package.json", "package.json"),
                UpstreamChange(
                    "modified", "src/venmo/client.ts", "src/venmo/client.ts"
                ),
            ),
            notes="Fix Venmo payment initialization.\n",
        )

        self.assertEqual("delta", packet.document["recommendation"]["mode"])
        self.assertEqual("high", packet.document["recommendation"]["priority"])
        self.assertIn("payment-review-signal", packet.document["recommendation"]["reasons"])
        self.assertNotIn(
            str(
                PurePosixPath(packet.document["snapshot_manifest"]).parent
                / "files"
                / "src/unchanged.ts"
            ),
            packet.document["required_reading"],
        )

    def test_dependency_only_change_is_delta(self):
        prior = {
            "package.json": self.manifest_content(
                "10.0.0", dependencies={"dep": "^1.0.0"}
            ),
            "src/index.ts": "export const value = 1;\n",
        }
        current = {
            "package.json": self.manifest_content(
                "10.0.1", dependencies={"dep": "^1.1.0"}
            ),
            "src/index.ts": "export const value = 1;\n",
        }

        packet = self.build(
            prior,
            current,
            (UpstreamChange("modified", "package.json", "package.json"),),
            notes="Dependency maintenance.\n",
        )

        package = packet.document["packages"][0]
        self.assertEqual("delta", package["recommendation"]["mode"])
        self.assertEqual(
            [
                {
                    "field": "dependencies",
                    "from": "^1.0.0",
                    "name": "dep",
                    "status": "changed",
                    "to": "^1.1.0",
                }
            ],
            package["dependency_changes"],
        )

    def test_public_export_addition_is_delta_but_removal_is_full(self):
        prior = {
            "package.json": self.manifest_content(
                "10.0.0", exports={".": "./src/index.ts"}
            ),
            "src/index.ts": "export const value = 1;\n",
        }
        added = {
            "package.json": self.manifest_content(
                "10.0.1",
                exports={".": "./src/index.ts", "./extra": "./src/extra.ts"},
            ),
            "src/index.ts": "export const value = 1;\n",
            "src/extra.ts": "export const extra = 1;\n",
        }
        addition = self.build(
            prior,
            added,
            (
                UpstreamChange("modified", "package.json", "package.json"),
                UpstreamChange("added", "", "src/extra.ts"),
            ),
            notes="Add an export.\n",
        )
        self.assertEqual("delta", addition.document["recommendation"]["mode"])
        self.assertEqual("high", addition.document["recommendation"]["priority"])

        removal_prior = {
            "package.json": self.manifest_content(
                "10.0.0",
                exports={".": "./src/index.ts", "./extra": "./src/extra.ts"},
            ),
            "src/index.ts": "export const value = 1;\n",
            "src/extra.ts": "export const extra = 1;\n",
        }
        removal_current = {
            "package.json": self.manifest_content(
                "10.0.1", exports={".": "./src/index.ts"}
            ),
            "src/index.ts": "export const value = 1;\n",
        }
        removal = self.build(
            removal_prior,
            removal_current,
            (
                UpstreamChange("modified", "package.json", "package.json"),
                UpstreamChange("deleted", "src/extra.ts", ""),
            ),
            notes="Remove an export.\n",
        )
        self.assertEqual("full", removal.document["recommendation"]["mode"])
        self.assertIn(
            "public-api-incompatible-change",
            removal.document["recommendation"]["reasons"],
        )

    def test_major_and_security_recommendations_remain_bounded(self):
        prior = {
            "package.json": self.manifest_content("9.4.0"),
            "src/index.ts": "export const value = 1;\n",
        }
        current = {
            "package.json": self.manifest_content("10.0.0"),
            "src/index.ts": "export const value = 2;\n",
        }
        changes = (
            UpstreamChange("modified", "package.json", "package.json"),
            UpstreamChange("modified", "src/index.ts", "src/index.ts"),
        )

        major = self.build(
            prior,
            current,
            changes,
            from_version="9.4.0",
            to_version="10.0.0",
        )
        self.assertEqual("full", major.document["recommendation"]["mode"])
        self.assertIn(
            "major-version-transition", major.document["recommendation"]["reasons"]
        )

        bounded = self.build(
            {
                "package.json": self.manifest_content("10.0.0"),
                "src/index.ts": "export const value = 1;\n",
            },
            {
                "package.json": self.manifest_content("10.0.1"),
                "src/index.ts": "export const value = 2;\n",
            },
            changes,
            notes="Security fix for a bounded source path.\n",
        )
        self.assertEqual("delta", bounded.document["recommendation"]["mode"])
        self.assertEqual("high", bounded.document["recommendation"]["priority"])

        unbounded = self.build(
            {
                "package.json": self.manifest_content("10.0.0"),
                "src/index.ts": "export const value = 1;\n",
            },
            {
                "package.json": self.manifest_content("10.0.1"),
                "src/index.ts": "export const value = 2;\n",
            },
            changes
            + (UpstreamChange("modified", ".github/workflows/release.yml", ".github/workflows/release.yml"),),
            notes="Security fix with repository-wide impact.\n",
        )
        self.assertEqual("full", unbounded.document["recommendation"]["mode"])
        self.assertIn(
            "unbounded-security-impact",
            unbounded.document["recommendation"]["reasons"],
        )

    def test_release_notes_revision_is_delta_without_comparison(self):
        prior_files = {
            "package.json": self.manifest_content("10.0.0"),
            "src/index.ts": "export const value = 1;\n",
        }
        current_files = {
            "package.json": self.manifest_content("10.0.1"),
            "src/index.ts": "export const value = 2;\n",
        }
        prior = self.snapshot(
            self.prior_sha, "10.0.0", prior_files, date="2026-07-27"
        )
        current = self.snapshot(self.current_sha, "10.0.1", current_files)
        release = self.release(
            "10.0.1", self.current_sha, "Corrected release notes.\n"
        )
        packet = build_ingest_packet(
            self.root,
            self.config,
            "github-" + ("3" * 20),
            self.relative(current),
            (
                PackagePacketInput(
                    package="@scope/widget",
                    from_version="10.0.0",
                    to_version="10.0.1",
                    from_sha=self.prior_sha,
                    to_sha=self.current_sha,
                    release_manifest=self.relative(release),
                    comparison_manifest="",
                    prior_snapshot_manifest=self.relative(prior),
                    upstream_changes=(),
                    release_notes_revision=True,
                ),
            ),
            "queued",
        )

        self.assertEqual("delta", packet.document["recommendation"]["mode"])
        self.assertIn(
            "release-notes-revision", packet.document["recommendation"]["reasons"]
        )
        self.assertIn(
            self.relative(release.parent / "release-notes.md"),
            packet.document["required_reading"],
        )

    def test_nested_package_json_evidence_is_not_the_package_identity_manifest(self):
        nested_manifest = json.dumps(
            {"name": "@scope/widget-auto", "private": True},
            sort_keys=True,
        ) + "\n"
        prior_files = {
            "packages/widget/package.json": (
                self.manifest_content("10.0.0"),
                "package-manifest",
                "package-manifest",
                "@scope/widget",
            ),
            "packages/widget/auto/package.json": (
                nested_manifest,
                "public-source",
                "tracked-declaration-directory",
                "@scope/widget",
            ),
            "packages/widget/src/index.ts": (
                "export const value = 1;\n",
                "public-source",
                "required-root",
                "@scope/widget",
            ),
        }
        current_files = dict(prior_files)
        current_files["packages/widget/package.json"] = (
            self.manifest_content("10.0.1"),
            "package-manifest",
            "package-manifest",
            "@scope/widget",
        )

        packet = self.build(
            prior_files,
            current_files,
            (
                UpstreamChange(
                    "modified",
                    "packages/widget/package.json",
                    "packages/widget/package.json",
                ),
            ),
        )

        self.assertEqual("10.0.1", packet.document["packages"][0]["to_version"])

    def test_unsupported_public_export_structure_blocks_packet(self):
        prior = {
            "package.json": self.manifest_content("10.0.0"),
            "src/index.ts": "export const value = 1;\n",
        }
        current = {
            "package.json": self.manifest_content(
                "10.0.1", exports=["./src/index.ts"]
            ),
            "src/index.ts": "export const value = 1;\n",
        }

        with self.assertRaisesRegex(
            PacketBuildError, "unsupported public API structure"
        ):
            self.build(
                prior,
                current,
                (UpstreamChange("modified", "package.json", "package.json"),),
            )

    def test_shared_sha_multi_package_packet_has_one_snapshot_identity(self):
        other = "@scope/other"
        config = replace(
            self.config,
            capsules=(
                replace(
                    self.config.capsules[0],
                    focus_packages=("@scope/widget", other),
                ),
            ),
        )
        prior_files = {
            "packages/widget/package.json": (
                self.manifest_content("10.0.0"),
                "package-manifest",
                "package-manifest",
                "@scope/widget",
            ),
            "packages/widget/src/index.ts": (
                "export const widget = 1;\n",
                "public-source",
                "required-root",
                "@scope/widget",
            ),
            "packages/other/package.json": (
                json.dumps(
                    {"name": other, "version": "10.0.0", "main": "./src/index.ts"},
                    sort_keys=True,
                )
                + "\n",
                "package-manifest",
                "package-manifest",
                other,
            ),
            "packages/other/src/index.ts": (
                "export const other = 1;\n",
                "public-source",
                "required-root",
                other,
            ),
        }
        current_files = dict(prior_files)
        current_files["packages/widget/package.json"] = (
            self.manifest_content("10.0.1"),
            "package-manifest",
            "package-manifest",
            "@scope/widget",
        )
        current_files["packages/widget/src/index.ts"] = (
            "export const widget = 2;\n",
            "public-source",
            "required-root",
            "@scope/widget",
        )
        current_files["packages/other/package.json"] = (
            json.dumps(
                {"name": other, "version": "10.0.1", "main": "./src/index.ts"},
                sort_keys=True,
            )
            + "\n",
            "package-manifest",
            "package-manifest",
            other,
        )
        current_files["packages/other/src/index.ts"] = (
            "export const other = 2;\n",
            "public-source",
            "required-root",
            other,
        )
        prior = self.snapshot(
            self.prior_sha, "10.0.0", prior_files, date="2026-07-27"
        )
        current = self.snapshot(self.current_sha, "10.0.1", current_files)
        widget_changes = (
            UpstreamChange(
                "modified",
                "packages/widget/package.json",
                "packages/widget/package.json",
            ),
            UpstreamChange(
                "modified",
                "packages/widget/src/index.ts",
                "packages/widget/src/index.ts",
            ),
        )
        other_changes = (
            UpstreamChange(
                "modified",
                "packages/other/package.json",
                "packages/other/package.json",
            ),
            UpstreamChange(
                "modified",
                "packages/other/src/index.ts",
                "packages/other/src/index.ts",
            ),
        )
        widget_release = self.release("10.0.1", self.current_sha, "Widget.\n")
        other_release = self.release(
            "10.0.1", self.current_sha, "Other.\n", package=other
        )
        widget_comparison = self.comparison("10.0.0", "10.0.1", widget_changes)
        other_comparison = self.comparison(
            "10.0.0", "10.0.1", other_changes, package=other
        )
        packet = build_ingest_packet(
            self.root,
            config,
            "github-" + ("4" * 20),
            self.relative(current),
            (
                PackagePacketInput(
                    "@scope/widget",
                    "10.0.0",
                    "10.0.1",
                    self.prior_sha,
                    self.current_sha,
                    self.relative(widget_release),
                    self.relative(widget_comparison),
                    self.relative(prior),
                    widget_changes,
                ),
                PackagePacketInput(
                    other,
                    "10.0.0",
                    "10.0.1",
                    self.prior_sha,
                    self.current_sha,
                    self.relative(other_release),
                    self.relative(other_comparison),
                    self.relative(prior),
                    other_changes,
                ),
            ),
            "queued",
        )

        self.assertEqual(2, len(packet.document["packages"]))
        self.assertEqual(
            ["@scope/other", "@scope/widget"],
            [row["package"] for row in packet.document["packages"]],
        )
        self.assertNotIn("snapshot_manifest", packet.document["packages"][0])

    def test_approved_test_exclusion_is_accounted_for_not_required_reading(self):
        prior = {
            "package.json": self.manifest_content("10.0.0"),
            "src/index.ts": "export const value = 1;\n",
        }
        current = {
            "package.json": self.manifest_content("10.0.1"),
            "src/index.ts": "export const value = 1;\n",
        }
        excluded = (("src/index.test.ts", "excluded-category:tests"),)
        packet = self.build(
            prior,
            current,
            (
                UpstreamChange("modified", "package.json", "package.json"),
                UpstreamChange(
                    "modified", "src/index.test.ts", "src/index.test.ts"
                ),
            ),
            prior_excluded=excluded,
            current_excluded=excluded,
        )

        upstream = packet.document["packages"][0]["upstream_changes"]
        test_row = next(row for row in upstream if row["new_path"].endswith(".test.ts"))
        self.assertEqual("intentional-policy-exclusion", test_row["disposition"])
        self.assertFalse(
            any(path.endswith("src/index.test.ts") for path in packet.document["required_reading"])
        )

    def test_multiple_category_exclusions_for_one_path_are_accepted(self):
        prior = {
            "package.json": self.manifest_content("10.0.0"),
            "src/index.ts": "export const value = 1;\n",
        }
        current = {
            "package.json": self.manifest_content("10.0.1"),
            "src/index.ts": "export const value = 1;\n",
        }
        path = "src/__tests__/fixtures/sample.json"
        excluded = (
            (path, "excluded-category:fixtures"),
            (path, "excluded-category:tests"),
        )

        packet = self.build(
            prior,
            current,
            (UpstreamChange("modified", path, path),),
            prior_excluded=excluded,
            current_excluded=excluded,
        )

        row = packet.document["packages"][0]["upstream_changes"][0]
        self.assertEqual("intentional-policy-exclusion", row["disposition"])
        self.assertEqual("excluded-category:fixtures", row["reason"])

    def test_missing_required_source_and_unclassified_retained_file_block_packet(self):
        prior = {
            "package.json": self.manifest_content("10.0.0"),
            "src/index.ts": "export const value = 1;\n",
        }
        current = {
            "package.json": self.manifest_content("10.0.1"),
            "src/index.ts": "export const value = 1;\n",
        }
        with self.assertRaisesRegex(PacketBuildError, "blocking evidence gap"):
            self.build(
                prior,
                current,
                (
                    UpstreamChange("modified", "package.json", "package.json"),
                    UpstreamChange(
                        "modified", "src/missing.ts", "src/missing.ts"
                    ),
                ),
            )

        unclassified = dict(current)
        unclassified["src/value.weird"] = (
            "unknown\n",
            "public-source",
            "required-root",
        )
        with self.assertRaisesRegex(PacketBuildError, "unclassified"):
            self.build(
                prior,
                unclassified,
                (
                    UpstreamChange("modified", "package.json", "package.json"),
                    UpstreamChange("added", "", "src/value.weird"),
                ),
            )

    def test_packet_json_model_and_markdown_are_deterministic(self):
        prior = {
            "package.json": self.manifest_content("10.0.0"),
            "src/index.ts": "export const value = 1;\n",
        }
        current = {
            "package.json": self.manifest_content("10.0.1"),
            "src/index.ts": "export const value = 2;\n",
        }
        changes = (
            UpstreamChange("modified", "package.json", "package.json"),
            UpstreamChange("modified", "src/index.ts", "src/index.ts"),
        )

        first = self.build(prior, current, changes)
        second = self.build(prior, current, tuple(reversed(changes)))

        self.assertIsInstance(first, IngestPacket)
        self.assertEqual(first.document, second.document)
        self.assertEqual(first.markdown, second.markdown)
        self.assertEqual(
            hashlib.sha256(first.markdown).hexdigest(),
            first.document["markdown_sha256"],
        )

    def test_prior_packet_policy_change_requires_full_ingest(self):
        packet_path = (
            self.root
            / "tracking/github/repos/acme/widgets/ingest-packets"
            / ("github-" + ("9" * 20))
            / "packet.json"
        )
        write_canonical_json(
            packet_path,
            {
                "capsule_policy_sha256": "f" * 64,
                "packages": [
                    {
                        "package": "@scope/widget",
                        "to_sha": self.prior_sha,
                        "to_version": "10.0.0",
                    }
                ],
                "repository": "acme/widgets",
            },
        )
        packet = self.build(
            {
                "package.json": self.manifest_content("10.0.0"),
                "src/index.ts": "export const value = 1;\n",
            },
            {
                "package.json": self.manifest_content("10.0.1"),
                "src/index.ts": "export const value = 2;\n",
            },
            (
                UpstreamChange("modified", "package.json", "package.json"),
                UpstreamChange("modified", "src/index.ts", "src/index.ts"),
            ),
        )

        self.assertEqual("full", packet.document["recommendation"]["mode"])
        self.assertIn(
            "capsule-policy-changed",
            packet.document["recommendation"]["reasons"],
        )

    def test_packet_budget_overflow_blocks_packet(self):
        constrained = replace(
            self.config,
            capsules=(
                replace(
                    self.config.capsules[0],
                    max_packet_files=1,
                ),
            ),
        )
        files = {
            "package.json": self.manifest_content("10.0.0"),
            "src/index.ts": "export const value = 1;\n",
        }

        with self.assertRaisesRegex(PacketBuildError, "packet budget"):
            self.build(
                files,
                {
                    "package.json": self.manifest_content("10.0.1"),
                    "src/index.ts": "export const value = 2;\n",
                },
                (
                    UpstreamChange("modified", "package.json", "package.json"),
                    UpstreamChange("modified", "src/index.ts", "src/index.ts"),
                ),
                config=constrained,
            )

    def test_queued_packet_publication_is_canonical_idempotent_and_conflict_safe(self):
        packet = self.build(
            {
                "package.json": self.manifest_content("10.0.0"),
                "src/index.ts": "export const value = 1;\n",
            },
            {
                "package.json": self.manifest_content("10.0.1"),
                "src/index.ts": "export const value = 2;\n",
            },
            (
                UpstreamChange("modified", "package.json", "package.json"),
                UpstreamChange("modified", "src/index.ts", "src/index.ts"),
            ),
        )

        first = publish_queued_packet(self.root, self.config, packet)
        second = publish_queued_packet(self.root, self.config, packet)

        self.assertEqual(first, second)
        self.assertEqual(
            (
                self.root
                / "tracking/github/repos/acme/widgets/ingest-packets"
                / ("github-" + ("1" * 20))
                / "packet.json"
            ).resolve(),
            first,
        )
        self.assertEqual(
            packet.document,
            json.loads(first.read_text(encoding="utf-8")),
        )
        self.assertEqual(packet.markdown, (first.parent / "packet.md").read_bytes())

        conflicting = IngestPacket(
            dict(packet.document, collection_date="2026-07-29"),
            packet.markdown,
        )
        with self.assertRaisesRegex(PacketBuildError, "conflicts"):
            publish_queued_packet(self.root, self.config, conflicting)

    def test_queued_packet_failure_leaves_no_partial_directory(self):
        packet = self.build(
            {
                "package.json": self.manifest_content("10.0.0"),
                "src/index.ts": "export const value = 1;\n",
            },
            {
                "package.json": self.manifest_content("10.0.1"),
                "src/index.ts": "export const value = 2;\n",
            },
            (
                UpstreamChange("modified", "package.json", "package.json"),
                UpstreamChange("modified", "src/index.ts", "src/index.ts"),
            ),
        )
        from github_ingest_packets import _write_atomic

        calls = {"count": 0}

        def fail_second(path, content):
            calls["count"] += 1
            if calls["count"] == 2:
                raise OSError("disk full")
            return _write_atomic(path, content)

        with mock.patch(
            "github_ingest_packets._write_atomic",
            side_effect=fail_second,
        ):
            with self.assertRaises(OSError):
                publish_queued_packet(self.root, self.config, packet)

        destination = (
            self.root
            / "tracking/github/repos/acme/widgets/ingest-packets"
            / ("github-" + ("1" * 20))
        )
        self.assertFalse(destination.exists())

    def test_review_packet_publication_is_idempotent_and_cleans_partial_files(self):
        packet = self.build(
            {
                "package.json": self.manifest_content("10.0.0"),
                "src/index.ts": "export const value = 1;\n",
            },
            {
                "package.json": self.manifest_content("10.0.1"),
                "src/index.ts": "export const value = 2;\n",
            },
            (
                UpstreamChange("modified", "package.json", "package.json"),
                UpstreamChange("modified", "src/index.ts", "src/index.ts"),
            ),
            packet_kind="ad-hoc",
        )
        comparison = (
            self.root
            / "tracking/github/repos/acme/widgets/comparisons/widget/10.0.0--10.0.1"
        )

        first = publish_review_packet(comparison, packet)
        second = publish_review_packet(comparison, packet)

        self.assertEqual(first, second)
        self.assertEqual(comparison / "review-packet.json", first)
        self.assertEqual(
            packet.markdown, (comparison / "review-packet.md").read_bytes()
        )

        first.unlink()
        (comparison / "review-packet.md").unlink()
        from github_ingest_packets import _write_atomic

        calls = {"count": 0}

        def fail_second(path, content):
            calls["count"] += 1
            if calls["count"] == 2:
                raise OSError("disk full")
            return _write_atomic(path, content)

        with mock.patch(
            "github_ingest_packets._write_atomic",
            side_effect=fail_second,
        ):
            with self.assertRaises(OSError):
                publish_review_packet(comparison, packet)

        self.assertFalse((comparison / "review-packet.json").exists())
        self.assertFalse((comparison / "review-packet.md").exists())

    def test_queued_packet_rejects_repository_symlink_escape(self):
        packet = self.build(
            {
                "package.json": self.manifest_content("10.0.0"),
                "src/index.ts": "export const value = 1;\n",
            },
            {
                "package.json": self.manifest_content("10.0.1"),
                "src/index.ts": "export const value = 2;\n",
            },
            (
                UpstreamChange("modified", "package.json", "package.json"),
                UpstreamChange("modified", "src/index.ts", "src/index.ts"),
            ),
        )
        outside = self.root / "outside"
        outside.mkdir()
        repository_parent = self.root / "tracking/github/repos/acme"
        shutil.rmtree(repository_parent / "widgets")
        (repository_parent / "widgets").symlink_to(
            outside, target_is_directory=True
        )

        with self.assertRaisesRegex(PacketBuildError, "storage path"):
            publish_queued_packet(self.root, self.config, packet)

        self.assertEqual([], list(outside.iterdir()))

    def test_braintree_3_143_0_to_3_144_0_conformance(self):
        fixture_root = (
            ROOT
            / "tests/fixtures/github/braintree-web-3.143.0--3.144.0"
        )
        fixture = json.loads(
            (fixture_root / "fixture.json").read_text(encoding="utf-8")
        )
        comparison_fixture = json.loads(
            (fixture_root / "comparison.json").read_text(encoding="utf-8")
        )
        snapshot_documents = {}
        for label, summary_name, evidence_key in (
            ("prior", "prior-manifest.json", "prior_snapshot"),
            ("current", "current-manifest.json", "current_snapshot"),
        ):
            summary_path = fixture_root / summary_name
            summary = json.loads(summary_path.read_text(encoding="utf-8"))
            evidence_path = ROOT / fixture[evidence_key]
            content = evidence_path.read_bytes()
            document = json.loads(content)
            snapshot_documents[label] = document
            self.assertEqual(summary["repository"], document["repository"])
            self.assertEqual(summary["sha"], document["sha"])
            self.assertEqual(summary["collected_date"], document["collected_date"])
            self.assertEqual(summary["file_count"], len(document["files"]))
            self.assertEqual(
                summary["manifest_sha256"],
                hashlib.sha256(content).hexdigest(),
            )
            self.assertEqual(
                summary["files_sha256"],
                canonical_sha256(document["files"]),
            )

        accepted_comparison_path = ROOT / fixture["comparison"]
        accepted_comparison = json.loads(
            accepted_comparison_path.read_text(encoding="utf-8")
        )
        self.assertEqual(
            comparison_fixture["accepted_manifest_sha256"],
            hashlib.sha256(accepted_comparison_path.read_bytes()).hexdigest(),
        )
        for field in (
            "repository",
            "package",
            "from_version",
            "to_version",
            "from_sha",
            "to_sha",
        ):
            self.assertEqual(comparison_fixture[field], accepted_comparison[field])

        changes = tuple(
            UpstreamChange(
                row["status"],
                row["old_path"],
                row["new_path"],
            )
            for row in comparison_fixture["upstream_changes"]
        )
        config = {
            item.id: item
            for item in load_registry(
                ROOT / "tracking/github/repo-registry.toml"
            )
        }[fixture["repository"]]
        packet = build_ingest_packet(
            ROOT,
            config,
            "",
            fixture["current_snapshot"],
            (
                PackagePacketInput(
                    package=fixture["package"],
                    from_version=comparison_fixture["from_version"],
                    to_version=comparison_fixture["to_version"],
                    from_sha=comparison_fixture["from_sha"],
                    to_sha=comparison_fixture["to_sha"],
                    release_manifest=fixture["release"],
                    comparison_manifest=fixture["comparison"],
                    prior_snapshot_manifest=fixture["prior_snapshot"],
                    upstream_changes=changes,
                ),
            ),
            "ad-hoc",
        )
        document = packet.document
        package = document["packages"][0]
        expected = fixture["expected"]
        self.assertEqual(
            {
                key: expected[key]
                for key in ("added", "modified", "removed", "renamed", "unchanged")
            },
            package["retained_evidence"]["counts"],
        )
        added = [
            row
            for row in package["retained_evidence"]["files"]
            if row["status"] == "added"
        ]
        self.assertEqual(
            [(expected["added_story"], "story")],
            [(row["path"], row["classification"]) for row in added],
        )
        self.assertEqual(expected["evidence_gaps"], len(document["evidence_gaps"]))
        self.assertEqual(
            expected["unclassified_changes"],
            len(document["unclassified_changes"]),
        )
        self.assertEqual(expected["mode"], document["recommendation"]["mode"])
        self.assertEqual(
            expected["priority"], document["recommendation"]["priority"]
        )

        required = set(document["required_reading"])
        current_root = PurePosixPath(fixture["current_snapshot"]).parent
        for row in package["retained_evidence"]["files"]:
            if row["status"] == "unchanged":
                self.assertNotIn(
                    str(current_root / "files" / row["path"]),
                    required,
                )


if __name__ == "__main__":
    unittest.main()
