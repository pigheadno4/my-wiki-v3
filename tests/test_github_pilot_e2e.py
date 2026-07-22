import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from collect_github_repos import (  # noqa: E402
    approve_one,
    collect_one,
    next_ingest,
    retry_one,
)
from github_capsule_policy import CapsuleConfig  # noqa: E402
from github_registry import RepoConfig, VersionTrack  # noqa: E402
from github_releases import ReleaseNotesEvidence  # noqa: E402
from github_validation import inspect_github, validate_github  # noqa: E402
from github_work_items import load_work_items  # noqa: E402
from tests.github_test_support import commit_files, create_git_repo, tag  # noqa: E402


EXPECTED_RELEASES = (
    "@paypal/paypal-js@8.1.0",
    "@paypal/react-paypal-js@8.9.2",
    "@paypal/paypal-js@9.8.0",
    "@paypal/react-paypal-js@9.3.0",
    "@paypal/paypal-js@10.0.0",
    "@paypal/react-paypal-js@10.0.0",
    "@paypal/paypal-js@10.0.1",
    "@paypal/react-paypal-js@10.1.0",
    "@paypal/paypal-js@10.0.2",
    "@paypal/react-paypal-js@10.1.1",
)


def package_manifest(name, version):
    return json.dumps(
        {
            "name": name,
            "version": version,
            "main": "./src/index.ts",
            "types": "./src/index.ts",
            "exports": {".": "./src/index.ts"},
        },
        sort_keys=True,
    ) + "\n"


class GitHubPilotEndToEndTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        base = Path(self.directory.name)
        self.wiki = base / "wiki"
        self.wiki.mkdir()
        parent = base / "remote"
        parent.mkdir()
        self.remote = create_git_repo(parent)
        self.release_dates = {}
        self._create_release_history()
        self.config = self._config()
        self._write_registry()

    def _config(self):
        tracks = []
        for package in ("@paypal/paypal-js", "@paypal/react-paypal-js"):
            tracks.extend(
                (
                    VersionTrack(
                        "package:" + package + "@8",
                        "latest-stable",
                        "none",
                    ),
                    VersionTrack(
                        "package:" + package + "@9",
                        "latest-stable",
                        "none",
                    ),
                    VersionTrack(
                        "package:" + package + "@10",
                        "all-stable",
                        "all-stable",
                    ),
                )
            )
        return RepoConfig(
            id="paypal/paypal-js",
            company="paypal",
            url="https://github.com/paypal/paypal-js",
            enabled=True,
            repo_type="web-sdk",
            priority="tier1",
            track="releases-and-default-branch",
            version_strategy="monorepo-packages",
            max_file_bytes=512000,
            max_snapshot_bytes=3000000,
            version_tracks=tuple(tracks),
            capsules=(
                CapsuleConfig(
                    id="paypal-js-public-source",
                    adapter="npm-tracked-source-v1",
                    focus_packages=(
                        "@paypal/paypal-js",
                        "@paypal/react-paypal-js",
                    ),
                    default_required_roots=("src",),
                    default_generated_target_paths=("dist/",),
                    excluded_categories=("tests", "fixtures"),
                    max_file_bytes=512000,
                    max_capsule_files=120,
                    max_capsule_utf8_bytes=1500000,
                    max_packet_files=140,
                    max_packet_utf8_bytes=1800000,
                ),
            ),
        )

    def _create_release_history(self):
        root_manifest = json.dumps(
            {
                "name": "paypal-js-offline-fixture",
                "version": "1.0.0",
                "private": True,
                "workspaces": ["packages/*"],
            },
            sort_keys=True,
        ) + "\n"
        common = {
            "README.md": "# Offline PayPal JS fixture\n",
            "LICENSE": "Apache-2.0\n",
            "package.json": root_manifest,
        }
        releases = (
            ("8.1.0", "8.9.2", "v8 baseline"),
            ("9.8.0", "9.3.0", "v9 major"),
            ("10.0.0", "10.0.0", "v10 major"),
            ("10.0.1", "10.1.0", "v10 contained update"),
            ("10.0.2", "10.1.1", "v10 changed docs and tests"),
        )
        for index, (paypal_version, react_version, message) in enumerate(releases, 1):
            files = dict(common) if index == 1 else {}
            files.update(
                {
                    "packages/paypal-js/package.json": package_manifest(
                        "@paypal/paypal-js", paypal_version
                    ),
                    "packages/paypal-js/src/index.ts": (
                        "export {loadScript} from './internal/load-script';\n"
                    ),
                    "packages/paypal-js/src/internal/load-script.ts": (
                        "export const loadScript = () => '"
                        + paypal_version
                        + "';\n"
                    ),
                    "packages/paypal-js/docs/loading.md": (
                        "# Loading\n\nVersion " + paypal_version + "\n"
                    ),
                    "packages/paypal-js/test/loading.test.ts": (
                        "export const expected = '" + paypal_version + "';\n"
                    ),
                    "packages/react-paypal-js/stories/provider.stories.tsx": (
                        "export const version = '" + react_version + "';\n"
                    ),
                    "packages/react-paypal-js/package.json": package_manifest(
                        "@paypal/react-paypal-js", react_version
                    ),
                    "packages/react-paypal-js/src/index.ts": (
                        "export {PayPalScriptProvider} from './provider';\n"
                    ),
                    "packages/react-paypal-js/src/provider.ts": (
                        "export const PayPalScriptProvider = '"
                        + react_version
                        + "';\n"
                    ),
                    "packages/react-paypal-js/docs/provider.md": (
                        "# Provider\n\nVersion " + react_version + "\n"
                    ),
                    "packages/react-paypal-js/test/provider.test.ts": (
                        "export const expected = '" + react_version + "';\n"
                    ),
                }
            )
            commit_files(self.remote, files, message)
            tags = (
                "@paypal/paypal-js@" + paypal_version,
                "@paypal/react-paypal-js@" + react_version,
            )
            for position, release_tag in enumerate(tags):
                tag(self.remote, release_tag)
                day = (index - 1) * 2 + position + 1
                self.release_dates[release_tag] = (
                    "2026-06-" + str(day).zfill(2) + "T12:00:00Z"
                )

    def _write_registry(self):
        path = self.wiki / "tracking/github/repo-registry.toml"
        path.parent.mkdir(parents=True)
        tracks = []
        for package in ("@paypal/paypal-js", "@paypal/react-paypal-js"):
            for major, backfill, future in (
                ("8", "latest-stable", "none"),
                ("9", "latest-stable", "none"),
                ("10", "all-stable", "all-stable"),
            ):
                tracks.append(
                    "\n[[repos.version_tracks]]\n"
                    + 'selector="package:'
                    + package
                    + "@"
                    + major
                    + '"\nbackfill="'
                    + backfill
                    + '"\nfuture="'
                    + future
                    + '"\ninclude_prerelease=false\n'
                )
        path.write_text(
            """[[repos]]
id="paypal/paypal-js"
company="paypal"
url="https://github.com/paypal/paypal-js"
enabled=true
repo_type="web-sdk"
priority="tier1"
track="releases-and-default-branch"
version_strategy="monorepo-packages"
"""
            + "".join(tracks)
            + """
[[repos.capsules]]
id="paypal-js-public-source"
adapter="npm-tracked-source-v1"
focus_packages=["@paypal/paypal-js", "@paypal/react-paypal-js"]
default_required_roots=["src"]
default_generated_target_paths=["dist/"]
excluded_categories=["tests", "fixtures"]
max_file_bytes=512000
max_capsule_files=120
max_capsule_utf8_bytes=1500000
max_packet_files=140
max_packet_utf8_bytes=1800000
""",
            encoding="utf-8",
        )

    def release_notes(self, config, candidate):
        return ReleaseNotesEvidence(
            "https://api.github.test/" + candidate.tag,
            self.release_dates[candidate.tag],
            ("Routine release " + candidate.version + ".\n").encode("utf-8"),
        )

    def collect(self, mode, collection_date, **values):
        return collect_one(
            self.wiki,
            self.config,
            release_mode=mode,
            clone_source=self.remote,
            release_notes_fetcher=self.release_notes,
            collection_date=collection_date,
            **values,
        )

    def items(self):
        return load_work_items(self.wiki / "tracking/github/work-items.json")

    def mode_for(self, release_id):
        return next(
            change.recommended_mode
            for item in self.items()
            for change in item.package_changes
            if change.release_id == release_id
        )

    def test_offline_release_history_rehearses_collection_retry_and_approval(self):
        backfill = self.collect("backfill", "2026-07-20")

        self.assertEqual(EXPECTED_RELEASES, backfill.release_ids)
        snapshots = tuple(
            self.wiki.glob("raw/github/paypal/paypal-js/snapshots/*/manifest.json")
        )
        releases = tuple(
            self.wiki.glob(
                "raw/github/paypal/paypal-js/releases/*/*/*/manifest.json"
            )
        )
        self.assertLess(len(snapshots), len(releases))
        self.assertEqual(5, len(snapshots))
        self.assertEqual(10, len(releases))
        self.assertEqual("full", self.mode_for("@paypal/react-paypal-js@10.0.0"))
        self.assertEqual("delta", self.mode_for("@paypal/paypal-js@10.0.1"))
        self.assertEqual("delta", self.mode_for("@paypal/react-paypal-js@10.1.0"))

        saved_paths = {
            row["path"]
            for path in snapshots
            for row in json.loads(path.read_text(encoding="utf-8"))["files"]
        }
        self.assertIn("packages/paypal-js/src/internal/load-script.ts", saved_paths)
        self.assertIn("packages/paypal-js/docs/loading.md", saved_paths)
        self.assertNotIn("packages/paypal-js/test/loading.test.ts", saved_paths)
        self.assertIn(
            "packages/react-paypal-js/stories/provider.stories.tsx",
            saved_paths,
        )

        unchanged = self.collect("future", "2026-07-21")
        self.assertEqual("unchanged", unchanged.state)

        oldest = next(
            item
            for item in self.items()
            if "@paypal/paypal-js@8.1.0"
            in {change.release_id for change in item.package_changes}
        )
        approve_one(self.wiki, oldest.work_item_id, "full")
        selected = next_ingest(self.wiki)
        self.assertEqual(oldest.work_item_id, selected.work_item_id)
        self.assertEqual("approved", selected.state)
        self.assertEqual(
            "approved",
            next(item for item in self.items() if item.work_item_id == selected.work_item_id).state,
        )

        commit_files(
            self.remote,
            {
                "packages/paypal-js/package.json": package_manifest(
                    "@paypal/paypal-js", "10.0.3"
                ),
                "packages/paypal-js/src/internal/load-script.ts": (
                    "export const loadScript = () => '10.0.3';\n"
                ),
            },
            "future patch",
        )
        future_tag = "@paypal/paypal-js@10.0.3"
        tag(self.remote, future_tag)
        self.release_dates[future_tag] = "2026-07-22T12:00:00Z"

        with mock.patch(
            "collect_github_repos.publish_source_snapshot",
            side_effect=OSError("injected snapshot failure"),
        ):
            failed = self.collect("future", "2026-07-22", max_attempts=1)
        self.assertEqual("collection_failed", failed.state)
        failed_item = next(
            item for item in self.items() if item.work_item_id in failed.work_item_ids
        )
        self.assertEqual("", failed_item.snapshot_manifest)

        retry_one(self.wiki, failed_item.work_item_id)
        recovered = self.collect("future", "2026-07-23")
        self.assertEqual("awaiting_approval", recovered.state)
        recovered_item = next(
            item for item in self.items() if item.work_item_id == failed_item.work_item_id
        )
        self.assertTrue(recovered_item.snapshot_manifest)
        self.assertEqual("delta", recovered_item.recommended_mode)
        self.assertEqual([], validate_github(inspect_github(self.wiki)))


if __name__ == "__main__":
    unittest.main()
