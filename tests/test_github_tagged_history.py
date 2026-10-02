"""Tagged release comparisons retain the historical capsule's ownership."""

import subprocess
import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from collect_github_repos import collect_one, compare_one
from github_capsule_policy import CapsuleConfig
from github_registry import RepoConfig, VersionTrack
from github_releases import ReleaseNotesEvidence
from tests.github_test_support import commit_files, create_git_repo, tag


class TaggedHistoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "wiki"
        self.root.mkdir()
        self.remote = create_git_repo(Path(self.temp.name))
        self.old_sha = commit_files(self.remote, {
            "src/Stable.swift": "public struct Stable {}\n",
            "Old.swift": "public struct Checkout {}\n",
            "Excluded.swift": "public struct Excluded {}\n",
        }, "old layout")
        tag(self.remote, "1.0.0")
        self.config = RepoConfig(
            id="stripe/native", company="stripe", url="https://github.com/stripe/native",
            enabled=True, repo_type="mobile-sdk", priority="tier1",
            track="releases-and-default-branch", version_strategy="semver-tags",
            version_tracks=(VersionTrack("package:native@1", "latest-stable", "all-stable"),),
            capsules=(CapsuleConfig(
                id="native-source", adapter="tagged-tree-v1", focus_packages=("native",),
                dependency_scope="configured-repository-paths", changed_path_policy="policy-bounded",
                default_required_roots=("src",), default_generated_target_paths=(),
                include_paths=("Old.swift",),
            ),),
        )
        self.baseline = self.collect("1.0.0")
        self.assertEqual("awaiting_approval", self.baseline.state, self.baseline.errors)
        self.manifest = self.root / self.baseline.snapshot_paths[0]
        self.original = self.manifest.read_bytes()
        (self.remote / "Old.swift").unlink()
        subprocess.run(["git", "add", "-u"], cwd=self.remote, check=True, capture_output=True)
        commit_files(self.remote, {
            "New.swift": "public struct Checkout { public let enabled = true }\n",
        }, "move checkout")
        tag(self.remote, "1.1.0")
        self.config = replace(self.config, capsules=(replace(
            self.config.capsules[0], include_paths=("New.swift",)
        ),))

    def collect(self, version):
        return collect_one(
            self.root, self.config, release="native@" + version,
            clone_source=self.remote, collection_date="2026-09-30",
            release_notes_fetcher=lambda config, candidate: ReleaseNotesEvidence(
                "https://api.github.test/" + candidate.tag,
                "2026-09-30T00:00:00Z", b"Native update.\n"
            ),
        )

    def test_move_uses_old_snapshot_and_strict_new_policy(self):
        result = self.collect("1.1.0")
        self.assertEqual("awaiting_approval", result.state, result.errors)
        self.assertEqual(self.original, self.manifest.read_bytes())
        comparison = compare_one(self.root, self.config, "native@1.0.0", "native@1.1.0",
                                 clone_source=self.remote)
        self.assertIsNotNone(comparison)
        packet = next((self.root / "tracking/github/repos/stripe/native/comparisons").rglob("diff.patch"))
        patch = packet.read_text()
        self.assertIn("Old.swift", patch)
        self.assertIn("New.swift", patch)
        self.assertNotIn("Excluded.swift", patch)

    def test_missing_current_required_path_still_blocks(self):
        self.config = replace(self.config, capsules=(replace(
            self.config.capsules[0], include_paths=("Missing.swift",)
        ),))
        result = self.collect("1.1.0")
        self.assertEqual("needs_manual_review", result.state)
        self.assertIn("missing-required-include", " ".join(result.errors))

    def test_tampered_historical_evidence_blocks(self):
        (self.manifest.parent / "files/Old.swift").write_text("tampered\n")
        result = self.collect("1.1.0")
        self.assertEqual("needs_manual_review", result.state)
        self.assertIn("hash mismatch", " ".join(result.errors))


if __name__ == "__main__":
    unittest.main()
