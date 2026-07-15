"""Deterministic GitHub release discovery and release-note evidence retrieval."""

from dataclasses import dataclass
from functools import cmp_to_key
import json
from pathlib import Path
from typing import Callable, Dict, Optional, Sequence, Tuple
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

import github_git
from github_registry import RepoConfig, VersionTrack
from github_versions import SemanticVersion, compare_semver, matches_semver, parse_package_tag, parse_semver


class ReleaseSelectionError(ValueError):
    """A version track cannot deterministically select retained releases."""


class ReleaseEvidenceError(RuntimeError):
    """GitHub release evidence could not be retrieved or validated."""


@dataclass(frozen=True)
class ReleaseCandidate:
    package: str
    version: str
    tag: str
    object_sha: str
    commit_sha: str
    prerelease: bool


@dataclass(frozen=True)
class ReleaseNotesEvidence:
    source_url: str
    published_at: str
    content: bytes


def discover_release_candidates(
    config: RepoConfig, clone_path: Path, track: VersionTrack
) -> Tuple[ReleaseCandidate, ...]:
    """List matching remote tags without fetching their objects into the clone."""
    package_name, target = _track_scope(track)
    tag_objects, peeled_commits = _remote_tag_metadata(clone_path)
    matching_packages = set()
    candidates = []

    for tag in sorted(tag_objects):
        parsed_package = parse_package_tag(tag)
        if parsed_package is not None:
            package, raw_version = parsed_package
            version = parse_semver(raw_version)
            if package_name is None and _matches(version, target, track.include_prerelease):
                matching_packages.add(package)
            if package_name is None or package != package_name:
                continue
        else:
            if package_name is not None:
                continue
            raw_version = tag
            version = parse_semver(raw_version)

        if version is None:
            continue
        if not version.is_exact:
            if _matches_incomplete(version, target, track.include_prerelease):
                raise ReleaseSelectionError(
                    "incomplete release tag " + tag + " matching selector " + track.selector
                )
            continue
        if not _matches(version, target, track.include_prerelease):
            continue
        candidates.append(
            ReleaseCandidate(
                package=parsed_package[0] if parsed_package is not None else "",
                version=_normalized_version(raw_version),
                tag=tag,
                object_sha=tag_objects[tag],
                commit_sha=peeled_commits.get(tag, tag_objects[tag]),
                prerelease=version.prerelease is not None,
            )
        )

    if package_name is None and len(matching_packages) > 1:
        raise ReleaseSelectionError(
            "plain selector " + track.selector
            + " matches multiple package namespaces; use a package-scoped track"
        )
    return tuple(sorted(candidates, key=cmp_to_key(_compare_candidates)))


def select_release_candidates(
    track: VersionTrack,
    candidates: Sequence[ReleaseCandidate],
    existing_versions: Sequence[str] = (),
    mode: str = "backfill",
) -> Tuple[ReleaseCandidate, ...]:
    """Apply a network-free, deterministic retention policy to release candidates."""
    if mode not in ("backfill", "future"):
        raise ReleaseSelectionError("unknown release selection mode " + mode)
    package_name, target = _track_scope(track)
    eligible = _deduplicated_candidates(
        candidate
        for candidate in candidates
        if _candidate_matches_track(candidate, package_name, target, track.include_prerelease)
    )
    pinned = _pinned_candidates(track, eligible)

    if mode == "future":
        if track.future == "none":
            return ()
        if track.future != "all-stable":
            raise ReleaseSelectionError("unknown future policy " + track.future)
        existing = _version_keys(existing_versions)
        return tuple(candidate for candidate in eligible if _version_key(candidate.version) not in existing)

    if track.backfill == "none":
        return ()
    if track.backfill == "all-stable":
        return eligible
    if track.backfill != "minor-baselines":
        raise ReleaseSelectionError("unknown backfill policy " + track.backfill)
    if not eligible:
        return ()

    selected: Dict[Tuple[object, ...], ReleaseCandidate] = {
        _version_key(eligible[0].version): eligible[0],
        _version_key(eligible[-1].version): eligible[-1],
    }
    latest_by_minor: Dict[Tuple[int, int], ReleaseCandidate] = {}
    for candidate in eligible:
        version = _parsed_version(candidate.version)
        latest_by_minor[(version.major, version.minor or 0)] = candidate
    for candidate in latest_by_minor.values():
        selected[_version_key(candidate.version)] = candidate
    for candidate in pinned:
        selected[_version_key(candidate.version)] = candidate
    return tuple(sorted(selected.values(), key=cmp_to_key(_compare_candidates)))


def fetch_release_notes(
    config: RepoConfig,
    candidate: ReleaseCandidate,
    token: Optional[str] = None,
    opener: Optional[Callable[[Request], object]] = None,
) -> Optional[ReleaseNotesEvidence]:
    """Fetch an exact GitHub release body, returning ``None`` only for a 404."""
    source_url = _release_url(config, candidate.tag)
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "payment-industry-wiki-github-collector",
    }
    if token:
        headers["Authorization"] = "Bearer " + token
    request = Request(source_url, headers=headers)
    open_request = opener or urlopen

    try:
        response = open_request(request)
    except HTTPError as error:
        try:
            if error.code == 404:
                return None
            raise _evidence_error(config, candidate, "GitHub HTTP " + str(error.code)) from error
        finally:
            error.close()
    except (URLError, OSError) as error:
        raise _evidence_error(config, candidate, "GitHub request failed: " + str(error)) from error

    try:
        with response as opened_response:
            status = opened_response.getcode() if hasattr(opened_response, "getcode") else None
            if status == 404:
                return None
            if status is not None and status >= 400:
                raise _evidence_error(config, candidate, "GitHub HTTP " + str(status))
            payload = opened_response.read()
    except ReleaseEvidenceError:
        raise
    except (OSError, ValueError) as error:
        raise _evidence_error(config, candidate, "could not read GitHub response: " + str(error)) from error

    if not isinstance(payload, bytes):
        raise _evidence_error(config, candidate, "GitHub response body was not bytes")
    try:
        document = json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise _evidence_error(config, candidate, "malformed GitHub release JSON") from error
    if not isinstance(document, dict):
        raise _evidence_error(config, candidate, "malformed GitHub release JSON")
    body = document.get("body")
    published_at = document.get("published_at")
    if not isinstance(body, str):
        raise _evidence_error(config, candidate, "GitHub release body was not a string")
    if not isinstance(published_at, str):
        raise _evidence_error(config, candidate, "GitHub release published_at was not a string")
    return ReleaseNotesEvidence(source_url, published_at, body.encode("utf-8"))


def _track_scope(track: VersionTrack) -> Tuple[Optional[str], SemanticVersion]:
    if track.selector.startswith("package:"):
        package = parse_package_tag(track.selector[8:])
        if package is None:
            raise ReleaseSelectionError("invalid package release selector " + track.selector)
        target = parse_semver(package[1])
        return package[0], _required_version(target, track.selector)
    return None, _required_version(parse_semver(track.selector), track.selector)


def _remote_tag_metadata(clone_path: Path) -> Tuple[Dict[str, str], Dict[str, str]]:
    object_rows: Dict[str, list] = {}
    peeled_rows: Dict[str, list] = {}
    output = github_git.run_git(["ls-remote", "--tags", "origin"], clone_path)
    for line in output.splitlines():
        sha, separator, ref = line.partition("\t")
        if not separator or not ref.startswith("refs/tags/"):
            continue
        name = ref[len("refs/tags/"):]
        if name.endswith("^{}"):
            peeled_rows.setdefault(name[:-3], []).append(sha)
        else:
            object_rows.setdefault(name, []).append(sha)

    errors = []
    for tag, rows in sorted(object_rows.items()):
        if len(rows) > 1:
            ref = "refs/tags/" + tag
            if len(set(rows)) == 1:
                errors.append("duplicate direct row for " + ref)
            else:
                errors.append("conflicting direct rows for " + ref)
    for tag, rows in sorted(peeled_rows.items()):
        ref = "refs/tags/" + tag + "^{}"
        if tag not in object_rows:
            errors.append("orphan peeled row for " + ref)
        elif len(rows) > 1:
            if len(set(rows)) == 1:
                errors.append("duplicate peeled row for " + ref)
            else:
                errors.append("conflicting peeled rows for " + ref)
    if errors:
        raise ReleaseSelectionError("malformed ls-remote tag metadata: " + "; ".join(sorted(errors)))

    return (
        {tag: rows[0] for tag, rows in object_rows.items()},
        {tag: rows[0] for tag, rows in peeled_rows.items()},
    )


def _candidate_matches_track(
    candidate: ReleaseCandidate,
    package_name: Optional[str],
    target: SemanticVersion,
    include_prerelease: bool,
) -> bool:
    if package_name is not None and candidate.package != package_name:
        return False
    if package_name is None and candidate.package:
        return False
    return _matches(parse_semver(candidate.version), target, include_prerelease)


def _matches(
    candidate: Optional[SemanticVersion], target: SemanticVersion, include_prerelease: bool
) -> bool:
    return (
        candidate is not None
        and candidate.is_exact
        and matches_semver(candidate, target, include_prerelease)
    )


def _matches_incomplete(
    candidate: Optional[SemanticVersion], target: SemanticVersion, include_prerelease: bool
) -> bool:
    if candidate is None or candidate.is_exact or candidate.major != target.major:
        return False
    if candidate.minor is not None and target.minor is not None and candidate.minor != target.minor:
        return False
    if candidate.patch is not None and target.patch is not None and candidate.patch != target.patch:
        return False
    if (
        candidate.prerelease is not None
        and target.prerelease is not None
        and candidate.prerelease != target.prerelease
    ):
        return False
    return include_prerelease or candidate.prerelease is None


def _pinned_candidates(
    track: VersionTrack, candidates: Sequence[ReleaseCandidate]
) -> Tuple[ReleaseCandidate, ...]:
    selected = []
    for pinned in track.pinned_versions:
        key = _version_key(pinned)
        match = next((candidate for candidate in candidates if _version_key(candidate.version) == key), None)
        if match is None:
            raise ReleaseSelectionError("missing pinned version " + pinned + " for " + track.selector)
        selected.append(match)
    return tuple(selected)


def _deduplicated_candidates(candidates: Sequence[ReleaseCandidate]) -> Tuple[ReleaseCandidate, ...]:
    selected: Dict[Tuple[object, ...], ReleaseCandidate] = {}
    for candidate in candidates:
        key = _version_key(candidate.version)
        prior = selected.get(key)
        if prior is None or _candidate_identity(candidate) < _candidate_identity(prior):
            selected[key] = candidate
    return tuple(sorted(selected.values(), key=cmp_to_key(_compare_candidates)))


def _version_keys(versions: Sequence[str]) -> set:
    return {_version_key(version) for version in versions if parse_semver(version) is not None}


def _version_key(value: str) -> Tuple[object, ...]:
    normalized = _normalized_version(value)
    version = _parsed_version(normalized)
    return (
        version.major,
        version.minor,
        version.patch,
        version.prerelease is None,
        version.prerelease or (),
        normalized.partition("+")[2],
    )


def _parsed_version(value: str) -> SemanticVersion:
    return _required_version(parse_semver(value), value)


def _required_version(value: Optional[SemanticVersion], selector: str) -> SemanticVersion:
    if value is None:
        raise ReleaseSelectionError("invalid semantic version " + selector)
    return value


def _compare_candidates(left: ReleaseCandidate, right: ReleaseCandidate) -> int:
    comparison = compare_semver(_parsed_version(left.version), _parsed_version(right.version))
    if comparison:
        return comparison
    left_identity = _candidate_identity(left)
    right_identity = _candidate_identity(right)
    if left_identity < right_identity:
        return -1
    if left_identity > right_identity:
        return 1
    return 0


def _candidate_identity(candidate: ReleaseCandidate) -> Tuple[str, str, str, str]:
    return (candidate.tag, candidate.object_sha, candidate.commit_sha, candidate.package)


def _normalized_version(value: str) -> str:
    return value[1:] if value.startswith("v") else value


def _release_url(config: RepoConfig, tag: str) -> str:
    owner, separator, repository = config.id.partition("/")
    if not separator or not owner or not repository:
        raise ReleaseEvidenceError("invalid GitHub repository identity " + config.id)
    return (
        "https://api.github.com/repos/" + quote(owner, safe="") + "/" + quote(repository, safe="")
        + "/releases/tags/" + quote(tag, safe="")
    )


def _evidence_error(config: RepoConfig, candidate: ReleaseCandidate, detail: str) -> ReleaseEvidenceError:
    return ReleaseEvidenceError("release evidence for " + config.id + " tag " + candidate.tag + ": " + detail)
