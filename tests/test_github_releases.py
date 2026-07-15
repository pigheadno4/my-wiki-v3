"""Tests for deterministic GitHub release discovery and evidence retrieval."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from urllib.error import HTTPError


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from github_registry import RepoConfig, VersionTrack  # noqa: E402
from github_releases import (  # noqa: E402
    ReleaseCandidate,
    ReleaseEvidenceError,
    ReleaseNotesEvidence,
    ReleaseSelectionError,
    discover_release_candidates,
    fetch_release_notes,
    select_release_candidates,
)


def git(path, *args):
    return subprocess.run(
        ["git"] + list(args), cwd=str(path), check=True, text=True, capture_output=True
    ).stdout.strip()


def commit_file(path, relative_path, content, message):
    target = path / relative_path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")
    git(path, "add", relative_path)
    git(path, "commit", "-m", message)
    return git(path, "rev-parse", "HEAD")


def tag(path, name):
    git(path, "tag", name)


def annotated_tag(path, name):
    git(path, "tag", "-a", name, "-m", "release " + name)


class FakeResponse:
    def __init__(self, content, status=200):
        self.content = content
        self.status = status

    def read(self):
        return self.content

    def getcode(self):
        return self.status


class GitHubReleasesTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        self.repo = self.root / "source"
        self.remote = self.root / "remote.git"
        self.clone = self.root / "clone"
        self.repo.mkdir()
        git(self.repo, "init", "--initial-branch=main")
        git(self.repo, "config", "user.email", "tests@example.com")
        git(self.repo, "config", "user.name", "Tests")
        self.config = self._config()

    def tearDown(self):
        shutil.rmtree(self.root)

    def _config(self, **overrides):
        values = {
            "id": "acme/widgets",
            "company": "acme",
            "url": "https://github.com/acme/widgets",
            "enabled": True,
            "repo_type": "sdk",
            "priority": "tier1",
            "track": "releases-and-default-branch",
            "version_strategy": "semver-tags",
        }
        values.update(overrides)
        return RepoConfig(**values)

    def _track(self, **overrides):
        values = {
            "selector": "v9",
            "backfill": "all-stable",
            "future": "all-stable",
        }
        values.update(overrides)
        return VersionTrack(**values)

    def _candidates(self, *versions):
        return tuple(
            ReleaseCandidate("", version, "v" + version, "object-" + version, "commit-" + version, "-" in version)
            for version in versions
        )

    def _publish_and_clone(self):
        git(self.root, "init", "--bare", str(self.remote))
        git(self.repo, "remote", "add", "origin", str(self.remote))
        git(self.repo, "push", "--tags", "origin", "main")
        git(self.root, "clone", "--no-checkout", str(self.remote), str(self.clone))

    def test_all_stable_selects_every_stable_candidate_in_semantic_order(self):
        selected = select_release_candidates(
            self._track(), self._candidates("9.1.0", "9.0.0-rc.1", "9.0.1", "9.0.0")
        )

        self.assertEqual(("9.0.0", "9.0.1", "9.1.0"), tuple(item.version for item in selected))

    def test_minor_baselines_include_first_latest_per_minor_and_pins(self):
        selected = select_release_candidates(
            self._track(backfill="minor-baselines", pinned_versions=("9.0.1",)),
            self._candidates("9.0.0", "9.0.1", "9.1.0", "9.1.3", "9.2.0-beta.1"),
        )

        self.assertEqual(("9.0.0", "9.0.1", "9.1.3"), tuple(item.version for item in selected))

    def test_future_all_stable_selects_only_versions_absent_from_index(self):
        selected = select_release_candidates(
            self._track(), self._candidates("9.0.0", "9.0.1", "9.1.0-rc.1"), ("9.0.0",), "future"
        )

        self.assertEqual(("9.0.1",), tuple(item.version for item in selected))

    def test_future_none_selects_no_candidates(self):
        selected = select_release_candidates(
            self._track(future="none"), self._candidates("9.0.0"), mode="future"
        )

        self.assertEqual((), selected)

    def test_invalid_mode_and_missing_pin_fail_without_weakening_retention(self):
        with self.assertRaisesRegex(ReleaseSelectionError, "mode"):
            select_release_candidates(self._track(), self._candidates("9.0.0"), mode="other")
        with self.assertRaisesRegex(ReleaseSelectionError, "9.0.1"):
            select_release_candidates(
                self._track(pinned_versions=("9.0.1",)), self._candidates("9.0.0")
            )

    def test_discovery_keeps_annotated_object_and_peeled_commit_for_exact_package_major(self):
        annotated_commit = commit_file(self.repo, "README.md", "one\n", "initial")
        annotated_tag(self.repo, "@scope/widget@9.0.0")
        annotated_object = git(self.repo, "rev-parse", "@scope/widget@9.0.0")
        lightweight_commit = commit_file(self.repo, "README.md", "two\n", "next")
        tag(self.repo, "@scope/widget@9.1.0")
        tag(self.repo, "@scope/other@9.1.0")
        tag(self.repo, "v9.1.0")
        self._publish_and_clone()

        candidates = discover_release_candidates(
            self.config, self.clone, self._track(selector="package:@scope/widget@9")
        )

        self.assertEqual(("9.0.0", "9.1.0"), tuple(item.version for item in candidates))
        self.assertEqual("@scope/widget", candidates[0].package)
        self.assertEqual(annotated_object, candidates[0].object_sha)
        self.assertEqual(annotated_commit, candidates[0].commit_sha)
        self.assertEqual(lightweight_commit, candidates[1].object_sha)
        self.assertEqual(lightweight_commit, candidates[1].commit_sha)

    def test_plain_track_rejects_ambiguous_matching_package_namespaces(self):
        commit_file(self.repo, "README.md", "one\n", "initial")
        tag(self.repo, "@scope/one@9.0.0")
        tag(self.repo, "@scope/two@9.0.0")
        self._publish_and_clone()

        with self.assertRaisesRegex(ReleaseSelectionError, "package-scoped"):
            discover_release_candidates(self.config, self.clone, self._track())

    def test_discovery_ignores_incomplete_semantic_tags(self):
        commit_file(self.repo, "README.md", "one\n", "initial")
        tag(self.repo, "v9")
        tag(self.repo, "v9.0")
        tag(self.repo, "v9.0.0")
        self._publish_and_clone()

        candidates = discover_release_candidates(self.config, self.clone, self._track())

        self.assertEqual(("9.0.0",), tuple(item.version for item in candidates))

    def test_fetch_release_notes_preserves_utf8_body_and_required_headers(self):
        candidate = self._candidates("9.0.0")[0]
        received = []

        def opener(request):
            received.append(request)
            return FakeResponse(json.dumps({"published_at": "2026-07-15T12:00:00Z", "body": "A cafe \u2615"}).encode("utf-8"))

        evidence = fetch_release_notes(self.config, candidate, token="secret", opener=opener)

        self.assertEqual(
            ReleaseNotesEvidence(
                "https://api.github.com/repos/acme/widgets/releases/tags/v9.0.0",
                "2026-07-15T12:00:00Z",
                b"A cafe \xe2\x98\x95",
            ),
            evidence,
        )
        self.assertEqual("application/vnd.github+json", received[0].get_header("Accept"))
        self.assertEqual("Bearer secret", received[0].get_header("Authorization"))
        self.assertIn("github", received[0].get_header("User-agent").lower())

    def test_fetch_release_notes_returns_none_for_404(self):
        candidate = self._candidates("9.0.0")[0]

        def opener(request):
            raise HTTPError(request.full_url, 404, "not found", None, None)

        self.assertIsNone(fetch_release_notes(self.config, candidate, opener=opener))

    def test_fetch_release_notes_surfaces_context_for_http_and_payload_failures(self):
        candidate = self._candidates("9.0.0")[0]

        def rate_limited(request):
            raise HTTPError(request.full_url, 429, "rate limited", None, None)

        with self.assertRaisesRegex(ReleaseEvidenceError, "acme/widgets.*v9.0.0"):
            fetch_release_notes(self.config, candidate, opener=rate_limited)
        with self.assertRaisesRegex(ReleaseEvidenceError, "malformed"):
            fetch_release_notes(self.config, candidate, opener=lambda request: FakeResponse(b"{"))
        with self.assertRaisesRegex(ReleaseEvidenceError, "body"):
            fetch_release_notes(
                self.config,
                candidate,
                opener=lambda request: FakeResponse(b'{"published_at":"2026-07-15T12:00:00Z","body":null}'),
            )


if __name__ == "__main__":
    unittest.main()
