"""Immutable configuration records for GitHub repository collection."""

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Dict, List, Optional, Sequence, Tuple
from urllib.parse import urlsplit

from github_capsule_policy import CapsuleConfig, SecretAllowlist, parse_capsules, parse_secret_allowlist
from github_versions import parse_package_tag, parse_semver
from toml_compat import load_toml


PRIORITIES = {"tier1", "tier2", "tier3"}
TRACKS = {"default-branch", "releases-and-default-branch"}
VERSION_STRATEGIES = {"monorepo-packages", "semver-tags", "github-release", "commit"}
BACKFILL_POLICIES = {"all-stable", "latest-stable", "minor-baselines", "none"}
FUTURE_POLICIES = {"all-stable", "none"}
MUTABLE_STATE_KEYS = {
    "latest_version",
    "latest_sha",
    "last_collected_at",
    "last_collected_date",
    "collection_date",
    "collected_date",
    "collected_versions",
    "ingest_progress",
    "progress",
    "run_results",
    "policy_hash",
}
REQUIRED_KEYS = {
    "id",
    "company",
    "url",
    "enabled",
    "repo_type",
    "priority",
    "track",
    "version_strategy",
}
OPTIONAL_KEYS = {
    "collection_frequency",
    "requested_refs",
    "key_paths",
    "exclude_paths",
    "max_file_bytes",
    "max_snapshot_bytes",
    "version_tracks",
    "capsules",
    "secret_allowlist",
}
VERSION_TRACK_REQUIRED_KEYS = {"selector", "backfill", "future"}
VERSION_TRACK_OPTIONAL_KEYS = {"include_prerelease", "pinned_versions"}
_PATH_COMPONENT = re.compile(r"[a-z0-9][a-z0-9._-]*\Z")


@dataclass(frozen=True)
class VersionTrack:
    selector: str
    backfill: str
    future: str
    include_prerelease: bool = False
    pinned_versions: Tuple[str, ...] = ()


@dataclass(frozen=True)
class RepoConfig:
    id: str
    company: str
    url: str
    enabled: bool
    repo_type: str
    priority: str
    track: str
    version_strategy: str
    collection_frequency: str = "on-demand"
    requested_refs: Tuple[str, ...] = ()
    key_paths: Tuple[str, ...] = ()
    exclude_paths: Tuple[str, ...] = ()
    max_file_bytes: int = 1048576
    max_snapshot_bytes: int = 10485760
    version_tracks: Tuple[VersionTrack, ...] = ()
    capsules: Tuple[CapsuleConfig, ...] = ()
    secret_allowlist: Tuple[SecretAllowlist, ...] = ()


def load_registry(path: Path) -> Tuple[RepoConfig, ...]:
    data = load_toml(path)
    rows = data.get("repos", [])
    if not isinstance(rows, list):
        raise ValueError("registry repos must be an array of tables")

    repos = []
    for index, row in enumerate(rows, 1):
        if not isinstance(row, dict):
            raise ValueError("registry row " + str(index) + " must be a table")
        _validate_row_keys(row, index)
        missing = sorted(REQUIRED_KEYS - set(row))
        if missing:
            raise ValueError("registry row " + str(index) + " missing required key " + missing[0])
        repos.append(_config_from_row(row, index))

    errors = validate_registry(repos)
    if errors:
        raise ValueError("invalid repository registry:\n- " + "\n- ".join(errors))
    return tuple(repos)


def validate_registry(repos: Sequence[RepoConfig]) -> List[str]:
    errors = []
    ids = set()
    urls = set()
    allowed_attributes = set(RepoConfig.__dataclass_fields__)

    for index, repo in enumerate(repos, 1):
        prefix = "repository " + str(index)
        unexpected = sorted(set(vars(repo)) - allowed_attributes)
        for key in unexpected:
            if key in MUTABLE_STATE_KEYS:
                errors.append(prefix + " contains forbidden mutable-state key " + key)
            else:
                errors.append(prefix + " contains unknown key " + key)

        if repo.id in ids:
            errors.append(prefix + " has duplicate id " + repo.id)
        ids.add(repo.id)

        url_key = repo.url.lower()
        if url_key in urls:
            errors.append(prefix + " has duplicate URL " + repo.url)
        urls.add(url_key)

        if repo.priority not in PRIORITIES:
            errors.append(prefix + " has unknown priority " + repo.priority)
        if repo.track not in TRACKS:
            errors.append(prefix + " has unknown track " + repo.track)
        if repo.version_strategy not in VERSION_STRATEGIES:
            errors.append(prefix + " has unknown version_strategy " + repo.version_strategy)

        expected_id = _github_repository_id(repo.url)
        if expected_id is None:
            errors.append(prefix + " must use an HTTPS GitHub URL")
        elif repo.id != expected_id:
            errors.append(prefix + " id must equal lowercased URL owner/repository " + expected_id)
        if not _safe_path_component(repo.company):
            errors.append(prefix + " company must be a safe lowercase path component")
        id_parts = repo.id.split("/")
        if len(id_parts) != 2 or any(not _safe_path_component(part) for part in id_parts):
            errors.append(prefix + " id must contain safe lowercase path components")

        if not isinstance(repo.enabled, bool):
            errors.append(prefix + " enabled must be a boolean")
        if not repo.collection_frequency:
            errors.append(prefix + " collection_frequency must not be empty")
        if repo.max_file_bytes <= 0 or repo.max_snapshot_bytes <= 0:
            errors.append(prefix + " byte limits must be positive")
        errors.extend(_version_track_errors(repo.version_tracks, prefix))

    return errors


def validate_enabled_policy(repo: RepoConfig) -> List[str]:
    """Return operational-readiness errors for one enabled focused repository."""
    if not repo.enabled:
        return []
    errors = []
    if not repo.version_tracks:
        errors.append("enabled repository requires version tracks")
    if len(repo.capsules) != 1:
        errors.append("enabled repository requires exactly one capsule")
    for track in repo.version_tracks:
        if not track.selector.startswith("package:"):
            errors.append("enabled repository release selectors must be package-qualified")
    return errors


def select_repos(
    repos: Sequence[RepoConfig],
    company: Optional[str] = None,
    repo_id: Optional[str] = None,
    enabled_only: bool = True,
) -> Tuple[RepoConfig, ...]:
    return tuple(
        repo
        for repo in repos
        if (not enabled_only or repo.enabled)
        and (company is None or repo.company == company)
        and (repo_id is None or repo.id == repo_id)
    )


def _validate_row_keys(row: Dict[str, object], index: int) -> None:
    keys = set(row)
    mutable = sorted(keys & MUTABLE_STATE_KEYS)
    if mutable:
        raise ValueError(
            "registry row " + str(index) + " contains forbidden mutable-state key " + mutable[0]
        )
    unexpected = sorted(keys - REQUIRED_KEYS - OPTIONAL_KEYS)
    if unexpected:
        raise ValueError("registry row " + str(index) + " contains unknown key " + unexpected[0])


def _config_from_row(row: Dict[str, object], index: int) -> RepoConfig:
    return RepoConfig(
        id=_required_string(row, "id", index),
        company=_required_string(row, "company", index),
        url=_required_string(row, "url", index),
        enabled=_required_bool(row, "enabled", index),
        repo_type=_required_string(row, "repo_type", index),
        priority=_required_string(row, "priority", index),
        track=_required_string(row, "track", index),
        version_strategy=_required_string(row, "version_strategy", index),
        collection_frequency=_optional_string(row, "collection_frequency", "on-demand", index),
        requested_refs=_optional_strings(row, "requested_refs", index),
        key_paths=_optional_strings(row, "key_paths", index),
        exclude_paths=_optional_strings(row, "exclude_paths", index),
        max_file_bytes=_optional_positive_int(row, "max_file_bytes", 1048576, index),
        max_snapshot_bytes=_optional_positive_int(row, "max_snapshot_bytes", 10485760, index),
        version_tracks=_version_tracks(row.get("version_tracks", []), index),
        capsules=parse_capsules(row.get("capsules", []), index),
        secret_allowlist=parse_secret_allowlist(row.get("secret_allowlist", []), index),
    )


def _version_tracks(value: object, index: int) -> Tuple[VersionTrack, ...]:
    if not isinstance(value, list):
        raise ValueError("registry row " + str(index) + " version_tracks must be an array of tables")
    tracks = []
    for track_index, track in enumerate(value, 1):
        if not isinstance(track, dict):
            raise ValueError(
                "registry row " + str(index) + " version track " + str(track_index) + " must be a table"
            )
        keys = set(track)
        unexpected = sorted(keys - VERSION_TRACK_REQUIRED_KEYS - VERSION_TRACK_OPTIONAL_KEYS)
        if unexpected:
            raise ValueError(
                "registry row " + str(index) + " version track " + str(track_index)
                + " contains unknown key " + unexpected[0]
            )
        missing = sorted(VERSION_TRACK_REQUIRED_KEYS - keys)
        if missing:
            raise ValueError(
                "registry row " + str(index) + " version track " + str(track_index)
                + " missing required key " + missing[0]
            )
        selector = _version_track_selector(track["selector"], index, track_index)
        backfill = _version_track_policy(track["backfill"], BACKFILL_POLICIES, "backfill", index, track_index)
        future = _version_track_policy(track["future"], FUTURE_POLICIES, "future", index, track_index)
        include_prerelease = track.get("include_prerelease", False)
        if not isinstance(include_prerelease, bool):
            raise ValueError(
                "registry row " + str(index) + " version track " + str(track_index)
                + " include_prerelease must be a boolean"
            )
        pinned_versions = _pinned_versions(track.get("pinned_versions", []), index, track_index)
        tracks.append(VersionTrack(selector, backfill, future, include_prerelease, pinned_versions))
    errors = _version_track_errors(tuple(tracks), "registry row " + str(index))
    if errors:
        raise ValueError(errors[0])
    return tuple(tracks)


def _version_track_selector(value: object, index: int, track_index: int) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError(
            "registry row " + str(index) + " version track " + str(track_index)
            + " selector must be a non-empty semantic selector"
        )
    parsed = parse_package_tag(value[8:]) if value.startswith("package:") else None
    if parsed is None:
        raise ValueError(
            "registry row " + str(index) + " version track " + str(track_index)
            + " selector must be package-qualified"
        )
    return value


def _version_track_policy(
    value: object, policies: set, key: str, index: int, track_index: int
) -> str:
    if not isinstance(value, str) or value not in policies:
        raise ValueError(
            "registry row " + str(index) + " version track " + str(track_index)
            + " has unknown " + key + " policy " + str(value)
        )
    return value


def _pinned_versions(value: object, index: int, track_index: int) -> Tuple[str, ...]:
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValueError(
            "registry row " + str(index) + " version track " + str(track_index)
            + " pinned_versions must be an array of strings"
        )
    if any((parsed := parse_semver(item)) is None or not parsed.is_exact for item in value):
        raise ValueError(
            "registry row " + str(index) + " version track " + str(track_index)
            + " pinned_versions must contain exact semantic versions"
        )
    return tuple(value)


def _version_track_errors(tracks: object, prefix: str) -> List[str]:
    if not isinstance(tracks, tuple):
        return [prefix + " version_tracks must be a tuple"]
    errors = []
    selectors = set()
    for index, track in enumerate(tracks, 1):
        track_prefix = prefix + " version track " + str(index)
        if not isinstance(track, VersionTrack):
            errors.append(track_prefix + " must be a VersionTrack")
            continue
        try:
            _version_track_selector(track.selector, 0, index)
        except ValueError as error:
            errors.append(str(error).replace("registry row 0 ", track_prefix + " "))
        if track.backfill not in BACKFILL_POLICIES:
            errors.append(track_prefix + " has unknown backfill policy " + track.backfill)
        if track.future not in FUTURE_POLICIES:
            errors.append(track_prefix + " has unknown future policy " + track.future)
        if not isinstance(track.include_prerelease, bool):
            errors.append(track_prefix + " include_prerelease must be a boolean")
        if not isinstance(track.pinned_versions, tuple):
            errors.append(track_prefix + " pinned_versions must be a tuple")
        elif any(
            not isinstance(version, str)
            or (parsed := parse_semver(version)) is None
            or not parsed.is_exact
            for version in track.pinned_versions
        ):
            errors.append(track_prefix + " pinned_versions must contain exact semantic versions")
        selector_key = _version_track_key(track.selector)
        if selector_key in selectors:
            errors.append(track_prefix + " has duplicate selector " + track.selector)
        selectors.add(selector_key)
    return errors


def _version_track_key(selector: str) -> Tuple[object, ...]:
    if selector.startswith("package:"):
        package = parse_package_tag(selector[8:])
        if package is not None:
            version = parse_semver(package[1])
            return ("package", package[0], version)
    version = parse_semver(selector)
    return ("tag", version)


def _required_string(row: Dict[str, object], key: str, index: int) -> str:
    value = row[key]
    if not isinstance(value, str) or not value:
        raise ValueError("registry row " + str(index) + " " + key + " must be a non-empty string")
    return value


def _required_bool(row: Dict[str, object], key: str, index: int) -> bool:
    value = row[key]
    if not isinstance(value, bool):
        raise ValueError("registry row " + str(index) + " " + key + " must be a boolean")
    return value


def _optional_string(row: Dict[str, object], key: str, default: str, index: int) -> str:
    value = row.get(key, default)
    if not isinstance(value, str) or not value:
        raise ValueError("registry row " + str(index) + " " + key + " must be a non-empty string")
    return value


def _optional_strings(row: Dict[str, object], key: str, index: int) -> Tuple[str, ...]:
    value = row.get(key, [])
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ValueError("registry row " + str(index) + " " + key + " must be an array of strings")
    return tuple(value)


def _optional_positive_int(row: Dict[str, object], key: str, default: int, index: int) -> int:
    value = row.get(key, default)
    if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
        raise ValueError("registry row " + str(index) + " " + key + " must be a positive integer")
    return value


def _github_repository_id(url: str) -> Optional[str]:
    parsed = urlsplit(url)
    if parsed.scheme != "https" or parsed.netloc.lower() != "github.com":
        return None
    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) != 2 or parsed.query or parsed.fragment:
        return None
    return parts[0].lower() + "/" + parts[1].lower()


def _safe_path_component(value: str) -> bool:
    return (
        isinstance(value, str)
        and value not in {".", ".."}
        and _PATH_COMPONENT.fullmatch(value) is not None
    )
