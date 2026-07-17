"""Tests for deterministic GitHub release discovery and evidence retrieval."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
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
        self.entered = False
        self.exited = False
        self.closed = False

    def __enter__(self):
        self.entered = True
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.exited = True
        self.close()

    def close(self):
        self.closed = True

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

    def test_disabled_backfill_skips_unavailable_historical_pins_and_existing_versions(self):
        selected = select_release_candidates(
            self._track(backfill="none", pinned_versions=("9.0.1",)),
            self._candidates("9.0.0"),
            existing_versions=("9.0.2",),
        )

        self.assertEqual((), selected)

    def test_disabled_future_skips_unavailable_historical_pins_and_existing_versions(self):
        selected = select_release_candidates(
            self._track(future="none", pinned_versions=("9.0.1",)),
            self._candidates("9.0.0"),
            existing_versions=("9.0.2",),
            mode="future",
        )

        self.assertEqual((), selected)

    def test_build_metadata_versions_keep_distinct_release_identities(self):
        candidates = self._candidates("9.0.0", "9.0.0+build.1", "9.0.0+build.2")

        retained = select_release_candidates(self._track(), candidates)
        future = select_release_candidates(self._track(), candidates, ("9.0.0",), "future")

        self.assertEqual(
            ("9.0.0", "9.0.0+build.1", "9.0.0+build.2"),
            tuple(item.version for item in retained),
        )
        self.assertEqual(
            ("9.0.0+build.1", "9.0.0+build.2"), tuple(item.version for item in future)
        )

    def test_build_metadata_selectors_require_the_exact_release_identity(self):
        plain_candidates = self._candidates("9.0.0+build.1", "9.0.0+build.2")
        package_candidates = (
            ReleaseCandidate(
                "@scope/widget",
                "9.0.0+build.1",
                "@scope/widget@9.0.0+build.1",
                "object-build.1",
                "commit-build.1",
                False,
            ),
            ReleaseCandidate(
                "@scope/widget",
                "9.0.0+build.2",
                "@scope/widget@9.0.0+build.2",
                "object-build.2",
                "commit-build.2",
                False,
            ),
        )

        plain_selected = select_release_candidates(
            self._track(selector="v9.0.0+build.1"), plain_candidates
        )
        package_selected = select_release_candidates(
            self._track(selector="package:@scope/widget@9.0.0+build.1"), package_candidates
        )

        self.assertEqual(("9.0.0+build.1",), tuple(item.version for item in plain_selected))
        self.assertEqual(("9.0.0+build.1",), tuple(item.version for item in package_selected))

    def test_pins_require_the_exact_build_metadata_identity(self):
        candidates = self._candidates("9.0.0+build.1")

        with self.assertRaisesRegex(ReleaseSelectionError, "9.0.0"):
            select_release_candidates(
                self._track(pinned_versions=("9.0.0",)), candidates
            )

        selected = select_release_candidates(
            self._track(pinned_versions=("9.0.0+build.1",)), candidates
        )
        self.assertEqual(("9.0.0+build.1",), tuple(item.version for item in selected))

    def test_minor_baselines_include_available_existing_versions(self):
        selected = select_release_candidates(
            self._track(backfill="minor-baselines"),
            self._candidates("9.0.0", "9.0.1", "9.0.2"),
            existing_versions=("9.0.1",),
        )

        self.assertEqual(("9.0.0", "9.0.1", "9.0.2"), tuple(item.version for item in selected))

    def test_minor_baselines_reject_unavailable_existing_versions(self):
        with self.assertRaisesRegex(ReleaseSelectionError, "9.0.1"):
            select_release_candidates(
                self._track(backfill="minor-baselines"),
                self._candidates("9.0.0"),
                existing_versions=("9.0.1",),
            )

    def test_semantic_aliases_on_the_same_commit_deduplicate(self):
        aliases = (
            ReleaseCandidate("", "9.0.0", "v9.0.0", "tag-a", "commit-shared", False),
            ReleaseCandidate("", "v9.0.0", "9.0.0", "tag-b", "commit-shared", False),
        )

        selected = select_release_candidates(self._track(selector="v9.0.0"), aliases)

        self.assertEqual(1, len(selected))
        self.assertEqual("9.0.0", selected[0].tag)
        self.assertEqual("commit-shared", selected[0].commit_sha)
        self.assertEqual(("9.0.0", "v9.0.0"), selected[0].aliases)

    def test_semantic_aliases_on_different_commits_raise_release_evidence_conflict(self):
        aliases = (
            ReleaseCandidate("", "9.0.0", "v9.0.0", "tag-a", "commit-a", False),
            ReleaseCandidate("", "v9.0.0", "9.0.0", "tag-b", "commit-b", False),
        )

        with self.assertRaisesRegex(ReleaseSelectionError, "release-evidence conflict.*9.0.0"):
            select_release_candidates(self._track(selector="v9.0.0"), aliases)

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

    def test_discovery_rejects_duplicate_and_conflicting_remote_tag_rows(self):
        rows = {
            "duplicate direct": (
                "a" * 40 + "\trefs/tags/v9.0.0\n"
                + "a" * 40 + "\trefs/tags/v9.0.0\n",
                "duplicate direct row.*refs/tags/v9.0.0",
            ),
            "duplicate peeled": (
                "a" * 40 + "\trefs/tags/v9.0.0\n"
                + "b" * 40 + "\trefs/tags/v9.0.0^{}\n"
                + "b" * 40 + "\trefs/tags/v9.0.0^{}\n",
                "duplicate peeled row.*refs/tags/v9\\.0\\.0\\^\\{\\}",
            ),
            "conflicting direct": (
                "a" * 40 + "\trefs/tags/v9.0.0\n"
                + "b" * 40 + "\trefs/tags/v9.0.0\n",
                "conflicting direct rows.*refs/tags/v9.0.0",
            ),
        }

        for name, (output, message) in rows.items():
            with self.subTest(name=name), mock.patch(
                "github_releases.github_git.run_git", return_value=output
            ):
                with self.assertRaisesRegex(ReleaseSelectionError, message):
                    discover_release_candidates(self.config, self.clone, self._track())

    def test_discovery_rejects_orphan_peeled_remote_tag_rows(self):
        output = "a" * 40 + "\trefs/tags/v9.0.0^{}\n"

        with mock.patch("github_releases.github_git.run_git", return_value=output):
            with self.assertRaisesRegex(
                ReleaseSelectionError, "orphan peeled row.*refs/tags/v9\\.0\\.0\\^\\{\\}"
            ):
                discover_release_candidates(self.config, self.clone, self._track())

    def test_discovery_reports_malformed_remote_rows_independently_of_input_order(self):
        direct = "a" * 40 + "\trefs/tags/v9.0.0\n"
        duplicate = "a" * 40 + "\trefs/tags/v9.0.0\n"
        orphan = "b" * 40 + "\trefs/tags/v8.0.0^{}\n"

        messages = []
        for output in (direct + duplicate + orphan, orphan + duplicate + direct):
            with mock.patch("github_releases.github_git.run_git", return_value=output):
                with self.assertRaises(ReleaseSelectionError) as raised:
                    discover_release_candidates(self.config, self.clone, self._track())
            messages.append(str(raised.exception))

        self.assertEqual(messages[0], messages[1])

    def test_discovery_rejects_malformed_rows_and_invalid_object_ids(self):
        rows = {
            "missing tab": "a" * 40 + " refs/tags/v9.0.0\n",
            "non-tag ref": "a" * 40 + "\trefs/heads/main\n",
            "empty tag": "a" * 40 + "\trefs/tags/\n",
            "empty object ID": "\trefs/tags/v9.0.0\n",
            "invalid object ID": "not-a-sha\trefs/tags/v9.0.0\n",
        }

        for name, output in rows.items():
            with self.subTest(name=name), mock.patch(
                "github_releases.github_git.run_git", return_value=output
            ):
                with self.assertRaisesRegex(ReleaseSelectionError, "malformed ls-remote tag metadata"):
                    discover_release_candidates(self.config, self.clone, self._track())

    def test_discovery_accepts_sha1_and_sha256_object_ids(self):
        output = (
            "a" * 40 + "\trefs/tags/v9.0.0\n"
            + "b" * 64 + "\trefs/tags/v9.1.0\n"
        )

        with mock.patch("github_releases.github_git.run_git", return_value=output):
            candidates = discover_release_candidates(self.config, self.clone, self._track())

        self.assertEqual(("9.0.0", "9.1.0"), tuple(item.version for item in candidates))

    def test_discovery_rejects_incomplete_matching_package_tags(self):
        output = "a" * 40 + "\trefs/tags/@scope/widget@9.0\n"

        with mock.patch("github_releases.github_git.run_git", return_value=output):
            with self.assertRaisesRegex(
                ReleaseSelectionError, "incomplete release tag @scope/widget@9.0"
            ):
                discover_release_candidates(
                    self.config, self.clone, self._track(selector="package:@scope/widget@9")
                )

    def test_discovery_rejects_incomplete_major_plain_tags(self):
        for tag_name in ("v9", "v9.0"):
            output = "a" * 40 + "\trefs/tags/" + tag_name + "\n"

            with self.subTest(tag_name=tag_name), mock.patch(
                "github_releases.github_git.run_git", return_value=output
            ):
                with self.assertRaisesRegex(
                    ReleaseSelectionError, "incomplete release tag " + tag_name
                ):
                    discover_release_candidates(self.config, self.clone, self._track())

    def test_discovery_scopes_incomplete_plain_tags_to_minor_selector(self):
        unrelated = "a" * 40 + "\trefs/tags/v9.0\n"
        matching = "b" * 40 + "\trefs/tags/v9.1\n"

        with mock.patch("github_releases.github_git.run_git", return_value=unrelated):
            self.assertEqual(
                (),
                discover_release_candidates(
                    self.config, self.clone, self._track(selector="v9.1")
                ),
            )
        with mock.patch("github_releases.github_git.run_git", return_value=matching):
            with self.assertRaisesRegex(ReleaseSelectionError, "incomplete release tag v9.1"):
                discover_release_candidates(
                    self.config, self.clone, self._track(selector="v9.1")
                )

    def test_discovery_rejects_incomplete_major_tag_for_minor_plain_selector(self):
        output = "a" * 40 + "\trefs/tags/v9\n"

        with mock.patch("github_releases.github_git.run_git", return_value=output):
            with self.assertRaisesRegex(ReleaseSelectionError, "incomplete release tag v9"):
                discover_release_candidates(
                    self.config, self.clone, self._track(selector="v9.1")
                )

    def test_discovery_incomplete_plain_tag_error_is_input_order_independent(self):
        tags = (
            "a" * 40 + "\trefs/tags/v9.0\n",
            "b" * 40 + "\trefs/tags/v9.1\n",
        )
        messages = []

        for output in ("".join(tags), "".join(reversed(tags))):
            with mock.patch("github_releases.github_git.run_git", return_value=output):
                with self.assertRaises(ReleaseSelectionError) as raised:
                    discover_release_candidates(
                        self.config, self.clone, self._track(selector="v9.1")
                    )
            messages.append(str(raised.exception))

        self.assertEqual(messages, ["incomplete release tag v9.1 matching selector v9.1"] * 2)

    def test_discovery_ignores_incomplete_tags_outside_the_selected_package_namespace(self):
        output = (
            "a" * 40 + "\trefs/tags/@scope/other@9.0\n"
            + "b" * 40 + "\trefs/tags/@scope/widget@9.0.0\n"
        )

        with mock.patch("github_releases.github_git.run_git", return_value=output):
            candidates = discover_release_candidates(
                self.config, self.clone, self._track(selector="package:@scope/widget@9")
            )

        self.assertEqual(("9.0.0",), tuple(item.version for item in candidates))

    def test_discovery_scopes_incomplete_package_tags_to_minor_selector(self):
        output = (
            "a" * 40 + "\trefs/tags/@scope/widget@9.0\n"
            + "b" * 40 + "\trefs/tags/@scope/other@9.1\n"
        )

        with mock.patch("github_releases.github_git.run_git", return_value=output):
            self.assertEqual(
                (),
                discover_release_candidates(
                    self.config,
                    self.clone,
                    self._track(selector="package:@scope/widget@9.1"),
                ),
            )

        matching = "c" * 40 + "\trefs/tags/@scope/widget@9.1\n"
        with mock.patch("github_releases.github_git.run_git", return_value=matching):
            with self.assertRaisesRegex(
                ReleaseSelectionError, "incomplete release tag @scope/widget@9.1"
            ):
                discover_release_candidates(
                    self.config,
                    self.clone,
                    self._track(selector="package:@scope/widget@9.1"),
                )

    def test_discovery_rejects_incomplete_package_major_tag_for_minor_selector(self):
        output = "a" * 40 + "\trefs/tags/@scope/widget@9\n"

        with mock.patch("github_releases.github_git.run_git", return_value=output):
            with self.assertRaisesRegex(
                ReleaseSelectionError, "incomplete release tag @scope/widget@9"
            ):
                discover_release_candidates(
                    self.config,
                    self.clone,
                    self._track(selector="package:@scope/widget@9.1"),
                )

    def test_discovery_incomplete_package_tag_error_is_input_order_independent(self):
        tags = (
            "a" * 40 + "\trefs/tags/@scope/widget@9.0\n",
            "b" * 40 + "\trefs/tags/@scope/other@9.1\n",
            "c" * 40 + "\trefs/tags/@scope/widget@9.1\n",
        )
        messages = []

        for output in ("".join(tags), "".join(reversed(tags))):
            with mock.patch("github_releases.github_git.run_git", return_value=output):
                with self.assertRaises(ReleaseSelectionError) as raised:
                    discover_release_candidates(
                        self.config,
                        self.clone,
                        self._track(selector="package:@scope/widget@9.1"),
                    )
            messages.append(str(raised.exception))

        self.assertEqual(
            messages,
            [
                "incomplete release tag @scope/widget@9.1 matching selector "
                "package:@scope/widget@9.1"
            ]
            * 2,
        )

    def test_fetch_release_notes_preserves_utf8_body_and_required_headers(self):
        candidate = self._candidates("9.0.0")[0]
        received = []
        response = FakeResponse(
            json.dumps({"published_at": "2026-07-15T12:00:00Z", "body": "A cafe \u2615"}).encode("utf-8")
        )

        def opener(request):
            received.append(request)
            return response

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
        self.assertTrue(response.entered)
        self.assertTrue(response.exited)
        self.assertTrue(response.closed)

    def test_fetch_release_notes_returns_none_for_404(self):
        candidate = self._candidates("9.0.0")[0]
        response = FakeResponse(b"")
        error = HTTPError("https://api.github.test", 404, "not found", None, response)

        def opener(request):
            raise error

        with mock.patch.object(error, "close", wraps=error.close) as close:
            self.assertIsNone(fetch_release_notes(self.config, candidate, opener=opener))
        close.assert_called_once_with()
        self.assertTrue(response.closed)

    def test_fetch_release_notes_surfaces_context_for_http_and_payload_failures(self):
        candidate = self._candidates("9.0.0")[0]
        response = FakeResponse(b"")
        error = HTTPError("https://api.github.test", 429, "rate limited", None, response)

        def rate_limited(request):
            raise error

        with mock.patch.object(error, "close", wraps=error.close) as close:
            with self.assertRaisesRegex(ReleaseEvidenceError, "acme/widgets.*v9.0.0"):
                fetch_release_notes(self.config, candidate, opener=rate_limited)
        close.assert_called_once_with()
        self.assertTrue(response.closed)
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
