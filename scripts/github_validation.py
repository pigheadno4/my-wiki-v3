"""Deterministic validation for GitHub collection artifacts."""

from __future__ import annotations

from dataclasses import dataclass
import json
import os
from pathlib import Path
import re
import stat
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

from collect_github_repos import is_valid_packet_id
from github_git import ResolvedRef
from github_packets import (
    PacketError,
    PacketRecord,
    VersionEntry,
    VersionIndex,
    _changed_evidence_paths,
    _entry_from_json,
    _evidence_root_from_packet_root,
    _render_packet_markdown,
    _required_reading,
    load_version_index,
)
from github_registry import RepoConfig, VersionTrack, load_registry
from github_reporting import (
    COLLECTION_TERMINAL,
    CollectionReconciliationError,
    StateTransitionError,
    packet_state_key,
    render_collection_status,
    render_ingest_status,
    validate_collection_run,
    validate_packet_history,
)
from github_snapshot import (
    SnapshotFile,
    SnapshotRecord,
    _read_metadata,
    _validate_metadata_schema,
    validate_staged_snapshot,
)
from github_versions import SemanticVersion, matches_semver, parse_package_tag, parse_semver
from validate_wiki import WIKILINK_RE, parse_frontmatter, split_frontmatter


_PACKET_FILES = {
    "changed-files.txt",
    "ingest-packet.md",
    "packet.json",
    "source-diff.patch",
    "state-events.jsonl",
}
_PACKET_KEYS = {
    "changed_files",
    "from",
    "from_snapshot",
    "initial_state",
    "packet_id",
    "packet_type",
    "repo_id",
    "required_reading",
    "to",
    "to_snapshot",
}
_SUPPLEMENT_SUFFIX = re.compile(r"-r([0-9]+)$")
_CHANGED_STATUS = re.compile(r"^(?:[ADMTUXB]|[RC][0-9]{0,3})$")
_PACKET_TYPES = {"baseline", "comparison", "delta"}


@dataclass(frozen=True)
class RegistryTrackRecord:
    repo_id: str
    company: str
    selector: str
    include_prerelease: bool
    track: VersionTrack


@dataclass(frozen=True)
class SnapshotInspection:
    path: Path
    relative_path: str
    repo_id: str
    company: str
    aliases: Tuple[str, ...]
    ref_name: str
    package: str
    version: str
    sha: str
    ref_kind: str
    capture_kind: str
    capture_revision: int
    collection_date: str
    changelog_paths: Tuple[str, ...]
    release_notes_path: str


@dataclass(frozen=True)
class ReleaseEvidenceRecord:
    snapshot_path: str
    repo_id: str
    version: str
    changelog_paths: Tuple[str, ...]
    release_notes_path: str
    changelog_absence_explicit: bool
    release_notes_explicit: bool


@dataclass(frozen=True)
class VersionIndexRecord:
    path: Path
    repo: RepoConfig
    index: VersionIndex


@dataclass(frozen=True)
class PacketInspection:
    path: Path
    record: PacketRecord
    current_state: str
    from_entry: Optional[VersionEntry]
    to_entry: VersionEntry
    to_sha: str
    to_version: str


@dataclass(frozen=True)
class ReleaseLedgerRow:
    version: str
    snapshot_link: str
    changelog_links: Tuple[str, ...]
    release_notes_links: Tuple[str, ...]
    changelog_absent: bool
    release_notes_absent: bool


@dataclass(frozen=True)
class SourceRecord:
    path: Path
    repo_id: str
    raw_files: Tuple[str, ...]
    evidence_links: Tuple[str, ...]
    release_ledger: Tuple[ReleaseLedgerRow, ...]


@dataclass(frozen=True)
class DashboardRecord:
    path: Path
    kind: str
    content: object


@dataclass(frozen=True)
class CollectionRunInspection:
    path: Path
    events: Tuple[Mapping[str, object], ...]


@dataclass(frozen=True)
class GitHubReport:
    root: Path
    registry_tracks: Tuple[RegistryTrackRecord, ...]
    snapshot_paths: Tuple[Path, ...]
    release_evidence_records: Tuple[ReleaseEvidenceRecord, ...]
    packet_paths: Tuple[Path, ...]
    pending_packets: Tuple[str, ...]
    source_records: Tuple[SourceRecord, ...]
    version_indexes: Tuple[VersionIndexRecord, ...]
    dashboard_records: Tuple[DashboardRecord, ...]
    inspection_errors: Tuple[str, ...]
    repositories: Tuple[RepoConfig, ...]
    snapshots: Tuple[SnapshotInspection, ...]
    packets: Tuple[PacketInspection, ...]
    collection_runs: Tuple[CollectionRunInspection, ...]
    collection_events: Tuple[Mapping[str, object], ...]


def inspect_github(root: Path) -> GitHubReport:
    """Inspect local GitHub collection state without network access."""
    root = root.resolve()
    errors: List[str] = []
    repositories = _inspect_registry(root, errors)
    configs_by_namespace = {
        (repo.company, Path(repo.id).name): repo for repo in repositories
    }
    registry_tracks = tuple(
        RegistryTrackRecord(
            repo_id=repo.id,
            company=repo.company,
            selector=track.selector,
            include_prerelease=track.include_prerelease,
            track=track,
        )
        for repo in repositories
        for track in repo.version_tracks
    )

    snapshots, release_records = _inspect_snapshots(
        root, configs_by_namespace, errors
    )
    _inspect_tracking_repository_namespaces(root, repositories, errors)
    version_indexes = _inspect_version_indexes(root, repositories, errors)
    packets = _inspect_packets(root, repositories, errors)
    collection_runs = _inspect_collection_runs(root, errors)
    collection_events = tuple(
        event for run in collection_runs for event in run.events
    )
    sources = _inspect_sources(root, snapshots, release_records, errors)
    dashboards = _inspect_dashboards(root, errors)
    pending = tuple(
        packet.record.packet_id
        for packet in packets
        if packet.current_state == "awaiting-review"
    )
    return GitHubReport(
        root=root,
        registry_tracks=registry_tracks,
        snapshot_paths=tuple(item.path for item in snapshots),
        release_evidence_records=release_records,
        packet_paths=tuple(item.path for item in packets),
        pending_packets=pending,
        source_records=sources,
        version_indexes=version_indexes,
        dashboard_records=dashboards,
        inspection_errors=tuple(errors),
        repositories=repositories,
        snapshots=snapshots,
        packets=packets,
        collection_runs=collection_runs,
        collection_events=collection_events,
    )


def validate_github(report: GitHubReport) -> List[str]:
    """Return all structural and release-retention errors in one report."""
    errors = list(report.inspection_errors)
    _validate_snapshot_identities(report, errors)
    _validate_collection_runs(report, errors)
    _validate_version_indexes(report, errors)
    _validate_packets(report, errors)
    _validate_sources(report, errors)
    _validate_release_collection_packets(report, errors)
    _validate_dashboards(report, errors)
    return _deduplicated(errors)


def _inspect_registry(root: Path, errors: List[str]) -> Tuple[RepoConfig, ...]:
    path = root / "tracking/github/repo-registry.toml"
    if not _safe_regular_file(root, path):
        errors.append("tracking/github/repo-registry.toml: registry is missing or unsafe")
        return ()
    try:
        return load_registry(path)
    except (OSError, UnicodeDecodeError, ValueError) as error:
        errors.append("tracking/github/repo-registry.toml: " + str(error))
        return ()


def _inspect_snapshots(
    root: Path,
    configs: Mapping[Tuple[str, str], RepoConfig],
    errors: List[str],
) -> Tuple[Tuple[SnapshotInspection, ...], Tuple[ReleaseEvidenceRecord, ...]]:
    raw_root = root / "raw/github"
    if not raw_root.exists() and not raw_root.is_symlink():
        return (), ()
    _scan_raw_tree(root, raw_root, errors)
    snapshots: List[SnapshotInspection] = []
    releases: List[ReleaseEvidenceRecord] = []
    for company in _safe_directories(raw_root, root, errors):
        if company.name == ".staging":
            continue
        for repository in _safe_directories(company, root, errors):
            snapshot_root = repository / "snapshots"
            if not snapshot_root.exists() and not snapshot_root.is_symlink():
                continue
            if not _safe_directory(root, snapshot_root):
                errors.append(_rel(root, snapshot_root) + ": unsafe snapshot namespace")
                continue
            config = configs.get((company.name, repository.name))
            for snapshot_path in _safe_directories(snapshot_root, root, errors):
                inspected = _inspect_snapshot(root, snapshot_path, config, errors)
                if inspected is None:
                    continue
                snapshots.append(inspected[0])
                releases.append(inspected[1])
    snapshots.sort(key=lambda item: item.relative_path)
    releases.sort(key=lambda item: item.snapshot_path)
    return tuple(snapshots), tuple(releases)


def _inspect_snapshot(
    root: Path,
    snapshot_path: Path,
    config: Optional[RepoConfig],
    errors: List[str],
) -> Optional[Tuple[SnapshotInspection, ReleaseEvidenceRecord]]:
    manifest_path = snapshot_path / "snapshot.md"
    label = _rel(root, manifest_path)
    try:
        text = _safe_read_text(root, manifest_path)
    except ValueError as error:
        errors.append(label + ": " + str(error))
        return None
    metadata, metadata_error = _read_metadata(text)
    if metadata_error is not None or metadata is None:
        errors.append(label + ": " + str(metadata_error))
        return None
    schema_errors: List[str] = []
    _validate_metadata_schema(metadata, schema_errors)
    if "release_notes" not in metadata:
        errors.append(label + ": release evidence is not explicit in manifest")
    errors.extend(label + ": " + error for error in schema_errors)
    if schema_errors:
        return None

    repository = metadata["repository"]
    ref = metadata["ref"]
    release_notes = metadata["release_notes"]
    snapshot_stat = os.stat(snapshot_path, follow_symlinks=False)
    files = tuple(
        SnapshotFile(
            path=item["path"],
            sha256=item["sha256"],
            size=item["size"],
            purpose=item["purpose"],
        )
        for item in metadata["files"]
    )
    record = SnapshotRecord(
        repo_id=repository["id"],
        ref=ResolvedRef(
            repo_id=repository["id"],
            ref_kind=ref["kind"],
            ref_name=ref["name"],
            sha=ref["sha"],
            version=ref["version"],
            aliases=tuple(ref["aliases"]),
            upstream_commit_time=ref["upstream_commit_time"],
            release_published_at=ref["release_published_at"],
        ),
        capture_kind=metadata["capture_kind"],
        capture_revision=metadata["capture_revision"],
        collection_date=metadata["collection_date"],
        staging_path=snapshot_path,
        target_path=snapshot_path,
        files=files,
        repository_url=repository["url"],
        company=repository["company"],
        repo_type=repository["type"],
        release_notes_source_url=(
            release_notes["source_url"] if release_notes is not None else None
        ),
        release_notes_published_at=(
            release_notes["published_at"] if release_notes is not None else None
        ),
        release_notes_sha256=(
            release_notes["sha256"] if release_notes is not None else None
        ),
        release_notes_size=(release_notes["size"] if release_notes is not None else None),
        staging_device=snapshot_stat.st_dev,
        staging_inode=snapshot_stat.st_ino,
    )
    errors.extend(label + ": " + error for error in validate_staged_snapshot(record))

    relative_snapshot = _rel(root, snapshot_path)
    if config is None:
        errors.append(relative_snapshot + ": snapshot repository is not registered")
    else:
        expected = {
            "repository id": config.id,
            "company": config.company,
            "repository URL": config.url,
            "repository type": config.repo_type,
        }
        actual = {
            "repository id": repository["id"],
            "company": repository["company"],
            "repository URL": repository["url"],
            "repository type": repository["type"],
        }
        for field in expected:
            if actual[field] != expected[field]:
                errors.append(relative_snapshot + ": manifest " + field + " disagrees with registry")

    changelogs = tuple(
        relative_snapshot + "/files/" + item.path
        for item in files
        if Path(item.path).name.lower().startswith("changelog")
    )
    release_path = (
        relative_snapshot + "/release-notes.md" if release_notes is not None else ""
    )
    explicit_changelog_absence = any(
        isinstance(item, dict)
        and isinstance(item.get("path"), str)
        and Path(str(item["path"])).name.lower().startswith("changelog")
        and bool(item.get("reason"))
        for item in metadata["excluded"]
    )
    is_release = ref["kind"] in ("package-version", "tag")
    if is_release and not changelogs and not explicit_changelog_absence:
        errors.append(label + ": release evidence is not explicit for changelog absence")
    return (
        SnapshotInspection(
            path=snapshot_path,
            relative_path=relative_snapshot,
            repo_id=repository["id"],
            company=repository["company"],
            aliases=tuple(ref["aliases"]),
            ref_name=ref["name"],
            package=_snapshot_package(ref["name"], ref["aliases"]),
            version=ref["version"],
            sha=ref["sha"],
            ref_kind=ref["kind"],
            capture_kind=metadata["capture_kind"],
            capture_revision=metadata["capture_revision"],
            collection_date=metadata["collection_date"],
            changelog_paths=changelogs,
            release_notes_path=release_path,
        ),
        ReleaseEvidenceRecord(
            snapshot_path=relative_snapshot,
            repo_id=repository["id"],
            version=ref["version"],
            changelog_paths=changelogs,
            release_notes_path=release_path,
            changelog_absence_explicit=bool(changelogs or explicit_changelog_absence),
            release_notes_explicit="release_notes" in metadata,
        ),
    )


def _scan_raw_tree(root: Path, raw_root: Path, errors: List[str]) -> None:
    if not _safe_directory(root, raw_root):
        errors.append(_rel(root, raw_root) + ": unsafe symlink or non-directory")
        return
    for current, directories, filenames in os.walk(raw_root, followlinks=False):
        current_path = Path(current)
        safe_directories = []
        for name in sorted(directories):
            path = current_path / name
            try:
                mode = path.lstat().st_mode
            except OSError:
                errors.append(_rel(root, path) + ": could not inspect raw entry")
                continue
            if stat.S_ISLNK(mode):
                errors.append(_rel(root, path) + ": unsafe symlink under raw")
                continue
            if stat.S_ISDIR(mode):
                safe_directories.append(name)
            else:
                errors.append(_rel(root, path) + ": raw entry is not a regular directory")
        directories[:] = safe_directories
        for name in sorted(filenames):
            path = current_path / name
            try:
                mode = path.lstat().st_mode
            except OSError:
                errors.append(_rel(root, path) + ": could not inspect raw entry")
                continue
            if stat.S_ISLNK(mode):
                errors.append(_rel(root, path) + ": unsafe symlink under raw")
                continue
            if not stat.S_ISREG(mode):
                errors.append(_rel(root, path) + ": raw entry is not a regular file")
            suffix = path.suffix.lower()
            if suffix == ".patch":
                errors.append(_rel(root, path) + ": generated patch under raw")
            elif suffix == ".diff":
                errors.append(_rel(root, path) + ": generated diff under raw")


def _inspect_version_indexes(
    root: Path, repositories: Sequence[RepoConfig], errors: List[str]
) -> Tuple[VersionIndexRecord, ...]:
    records = []
    for repo in repositories:
        path = root / "tracking/github/repos" / Path(repo.id) / "version-index.json"
        if not path.exists() and not path.is_symlink():
            continue
        if not _safe_regular_file(root, path):
            errors.append(_rel(root, path) + ": version index is unsafe")
            continue
        try:
            index = load_version_index(path, repo)
        except (OSError, UnicodeDecodeError, ValueError) as error:
            errors.append(_rel(root, path) + ": " + str(error))
            continue
        records.append(VersionIndexRecord(path=path, repo=repo, index=index))
    return tuple(records)


def _inspect_tracking_repository_namespaces(
    root: Path, repositories: Sequence[RepoConfig], errors: List[str]
) -> None:
    repos_root = root / "tracking/github/repos"
    if not repos_root.exists() and not repos_root.is_symlink():
        return
    if not _safe_directory(root, repos_root):
        errors.append(_rel(root, repos_root) + ": unsafe symlink or non-directory")
        return
    registered = {tuple(Path(repo.id).parts) for repo in repositories}
    try:
        owners = sorted(os.scandir(repos_root), key=lambda item: item.name)
    except OSError:
        errors.append(_rel(root, repos_root) + ": tracking repositories could not be inspected")
        return
    for owner in owners:
        owner_path = Path(owner.path)
        if owner.is_symlink():
            errors.append(_rel(root, owner_path) + ": unsafe symlink")
            continue
        if not owner.is_dir(follow_symlinks=False):
            errors.append(_rel(root, owner_path) + ": unexpected tracking owner entry")
            continue
        try:
            repo_entries = sorted(os.scandir(owner_path), key=lambda item: item.name)
        except OSError:
            errors.append(_rel(root, owner_path) + ": tracking owner could not be inspected")
            continue
        for repo_entry in repo_entries:
            repo_path = Path(repo_entry.path)
            if repo_entry.is_symlink():
                errors.append(_rel(root, repo_path) + ": unsafe symlink")
                continue
            if not repo_entry.is_dir(follow_symlinks=False):
                errors.append(_rel(root, repo_path) + ": unexpected tracking repository entry")
                continue
            if (owner.name, repo_entry.name) not in registered:
                errors.append(_rel(root, repo_path) + ": tracking repository is not registered")
            _inspect_tracking_repository_entries(root, repo_path, errors)


def _inspect_tracking_repository_entries(
    root: Path, repository: Path, errors: List[str]
) -> None:
    try:
        entries = sorted(os.scandir(repository), key=lambda item: item.name)
    except OSError:
        errors.append(_rel(root, repository) + ": tracking repository could not be inspected")
        return
    for entry in entries:
        path = Path(entry.path)
        if entry.is_symlink():
            errors.append(_rel(root, path) + ": unsafe symlink")
        elif entry.name == "version-index.json" and entry.is_file(follow_symlinks=False):
            continue
        elif entry.name == "packets" and entry.is_dir(follow_symlinks=False):
            _inspect_packet_namespace_entries(root, path, errors)
        else:
            errors.append(_rel(root, path) + ": unexpected tracking repository entry")


def _inspect_packet_namespace_entries(
    root: Path, packet_root: Path, errors: List[str]
) -> None:
    try:
        entries = sorted(os.scandir(packet_root), key=lambda item: item.name)
    except OSError:
        errors.append(_rel(root, packet_root) + ": packet namespace could not be inspected")
        return
    for entry in entries:
        path = Path(entry.path)
        if entry.is_symlink():
            errors.append(_rel(root, path) + ": unsafe symlink")
        elif entry.is_dir(follow_symlinks=False):
            continue
        elif entry.name == ".packet.lock" and entry.is_file(follow_symlinks=False):
            continue
        else:
            errors.append(_rel(root, path) + ": unexpected packet namespace entry")


def _inspect_packets(
    root: Path, repositories: Sequence[RepoConfig], errors: List[str]
) -> Tuple[PacketInspection, ...]:
    packets: List[PacketInspection] = []
    for repo in repositories:
        packet_root = root / "tracking/github/repos" / Path(repo.id) / "packets"
        if not packet_root.exists() and not packet_root.is_symlink():
            continue
        if not _safe_directory(root, packet_root):
            errors.append(_rel(root, packet_root) + ": packet namespace is unsafe")
            continue
        for directory in _safe_directories(packet_root, root, errors):
            inspected = _inspect_packet(root, repo, directory, errors)
            if inspected is not None:
                packets.append(inspected)
    packets.sort(key=lambda item: (item.record.repo_id, item.record.packet_id))
    return tuple(packets)


def _inspect_packet(
    root: Path, repo: RepoConfig, directory: Path, errors: List[str]
) -> Optional[PacketInspection]:
    label = _rel(root, directory)
    try:
        names = {
            entry.name
            for entry in os.scandir(directory)
        }
    except OSError:
        errors.append(label + ": packet directory could not be inspected")
        return None
    if names != _PACKET_FILES:
        errors.append(label + ": packet has an invalid file set")
    for name in _PACKET_FILES:
        if not _safe_regular_file(root, directory / name):
            errors.append(label + ": packet file is missing or unsafe: " + name)
    try:
        contract = _load_json_strict(_safe_read_text(root, directory / "packet.json"))
    except (ValueError, json.JSONDecodeError) as error:
        errors.append(label + ": invalid packet contract: " + str(error))
        return None
    if type(contract) is not dict or set(contract) != _PACKET_KEYS:
        errors.append(label + ": packet contract has an invalid schema")
        return None
    scalar_fields = (
        "packet_id",
        "repo_id",
        "packet_type",
        "from_snapshot",
        "to_snapshot",
        "initial_state",
    )
    required = contract["required_reading"]
    changed = contract["changed_files"]
    if (
        any(type(contract[field]) is not str for field in scalar_fields)
        or type(required) is not list
        or type(changed) is not list
        or any(type(item) is not str for item in required + changed)
        or contract["packet_id"] != directory.name
        or contract["repo_id"] != repo.id
        or contract["initial_state"] != "awaiting-review"
    ):
        errors.append(label + ": packet contract does not match its namespace")
        return None
    if not is_valid_packet_id(contract["packet_id"]):
        errors.append(label + ": packet ID is invalid")
    packet_type = contract["packet_type"]
    if packet_type not in _PACKET_TYPES:
        errors.append(label + ": unsupported packet type " + packet_type)
    try:
        evidence_root = _evidence_root_from_packet_root(directory.parent, repo)
        from_entry = (
            None
            if contract["from"] is None
            else _entry_from_json(contract["from"], evidence_root)
        )
        to_entry = _entry_from_json(contract["to"], evidence_root)
    except (PacketError, TypeError) as error:
        errors.append(label + ": invalid packet endpoint: " + str(error))
        return None
    if packet_type == "baseline":
        if from_entry is not None or contract["from_snapshot"]:
            errors.append(label + ": baseline packet has a from endpoint")
    elif from_entry is None or not contract["from_snapshot"]:
        errors.append(label + ": non-baseline packet is missing its from endpoint")
    if (
        (from_entry is not None and contract["from_snapshot"] != from_entry.snapshot_path)
        or contract["to_snapshot"] != to_entry.snapshot_path
    ):
        errors.append(label + ": packet endpoint snapshot fields disagree")
    if from_entry is not None and from_entry.sha == to_entry.sha:
        errors.append(label + ": packet endpoints must identify different SHAs")
    record = PacketRecord(
        packet_id=contract["packet_id"],
        repo_id=contract["repo_id"],
        packet_type=contract["packet_type"],
        from_snapshot=contract["from_snapshot"],
        to_snapshot=contract["to_snapshot"],
        required_reading=tuple(required),
        changed_files=tuple(changed),
        initial_state=contract["initial_state"],
        directory=directory,
    )
    for changed_file in record.changed_files:
        if not _valid_changed_file(changed_file):
            errors.append(label + ": unsafe changed file: " + changed_file)
    if len(set(record.changed_files)) != len(record.changed_files):
        errors.append(label + ": changed files contain duplicates")
    if packet_type == "baseline" and record.changed_files:
        errors.append(label + ": baseline packet has changed files")
    endpoint_entries = (
        (to_entry,) if from_entry is None else (from_entry, to_entry)
    )
    changed_evidence = (
        ()
        if from_entry is None
        else _changed_evidence_paths(from_entry, to_entry, record.changed_files)
    )
    expected_reading = _required_reading(endpoint_entries, changed_evidence)
    if record.required_reading != expected_reading:
        errors.append(label + ": required reading disagrees with producer contract")
    try:
        changed_text = _safe_read_text(root, directory / "changed-files.txt")
        packet_markdown = _safe_read_text(root, directory / "ingest-packet.md")
        source_diff = _safe_read_text(root, directory / "source-diff.patch")
    except ValueError as error:
        errors.append(label + ": packet generated file is unsafe: " + str(error))
        changed_text = ""
        packet_markdown = ""
        source_diff = ""
    expected_changed_text = "\n".join(record.changed_files) + "\n"
    if changed_text != expected_changed_text:
        errors.append(label + ": changed-files.txt disagrees with packet contract")
    if packet_markdown != _render_packet_markdown(record, from_entry, to_entry):
        errors.append(label + ": ingest-packet.md disagrees with packet contract")
    if packet_type == "baseline" and source_diff != "\n":
        errors.append(label + ": baseline source-diff.patch must be empty")
    elif source_diff and not source_diff.endswith("\n"):
        errors.append(label + ": source-diff.patch is not newline terminated")
    try:
        events = tuple(
            _require_json_object(_load_json_strict(line), "packet state event")
            for line in _safe_read_text(root, directory / "state-events.jsonl").splitlines()
        )
        current_state = validate_packet_history(
            record.packet_id, record.initial_state, events
        )
    except (ValueError, json.JSONDecodeError, StateTransitionError) as error:
        errors.append(label + ": invalid packet state history: " + str(error))
        current_state = "invalid"

    for path in record.required_reading:
        candidate = _safe_workspace_relative(root, path)
        expected_root = (
            "raw/github/" + repo.company + "/" + Path(repo.id).name + "/snapshots/"
        )
        if candidate is None or not path.startswith(expected_root):
            errors.append(label + ": unsafe required reading path: " + path)
            continue
        if not _safe_regular_file(root, candidate):
            errors.append(label + ": required reading is missing or unsafe: " + path)

    return PacketInspection(
        path=directory,
        record=record,
        current_state=current_state,
        from_entry=from_entry,
        to_entry=to_entry,
        to_sha=to_entry.sha,
        to_version=to_entry.version,
    )


def _inspect_collection_runs(
    root: Path, errors: List[str]
) -> Tuple[CollectionRunInspection, ...]:
    runs = root / "tracking/github/runs"
    if not runs.exists() and not runs.is_symlink():
        return ()
    if not _safe_directory(root, runs):
        errors.append(_rel(root, runs) + ": collection runs namespace is unsafe")
        return ()
    runs_found: List[CollectionRunInspection] = []
    try:
        entries = sorted(os.scandir(runs), key=lambda item: item.name)
    except OSError:
        errors.append(_rel(root, runs) + ": collection runs could not be inspected")
        return ()
    for entry in entries:
        path = Path(entry.path)
        if entry.is_symlink() or not entry.is_file(follow_symlinks=False):
            errors.append(_rel(root, path) + ": collection run is unsafe")
            continue
        if path.suffix != ".jsonl":
            continue
        try:
            events = tuple(
                    _require_json_object(_load_json_strict(line), "collection event")
                    for line in _safe_read_text(root, path).splitlines()
            )
        except (ValueError, json.JSONDecodeError) as error:
            errors.append(_rel(root, path) + ": invalid collection event: " + str(error))
            continue
        runs_found.append(CollectionRunInspection(path=path, events=events))
    return tuple(runs_found)


def _inspect_sources(
    root: Path,
    snapshots: Sequence[SnapshotInspection],
    release_records: Sequence[ReleaseEvidenceRecord],
    errors: List[str],
) -> Tuple[SourceRecord, ...]:
    source_root = root / "wiki/sources"
    if not source_root.is_dir():
        return ()
    snapshot_map = {item.relative_path + "/snapshot.md": item for item in snapshots}
    records = []
    for company in _safe_directories(source_root, root, errors):
        github = company / "github"
        if not github.exists() and not github.is_symlink():
            continue
        if not _safe_directory(root, github):
            errors.append(_rel(root, github) + ": GitHub source namespace is unsafe")
            continue
        try:
            entries = sorted(os.scandir(github), key=lambda item: item.name)
        except OSError:
            errors.append(_rel(root, github) + ": GitHub sources could not be inspected")
            continue
        for entry in entries:
            path = Path(entry.path)
            if entry.is_symlink() or not entry.is_file(follow_symlinks=False):
                errors.append(_rel(root, path) + ": GitHub source is unsafe")
                continue
            if path.suffix != ".md":
                continue
            record = _inspect_source(
                root,
                path,
                company.name,
                snapshot_map,
                {item.snapshot_path: item for item in release_records},
                errors,
            )
            if record is not None:
                records.append(record)
    return tuple(records)


def _inspect_source(
    root: Path,
    path: Path,
    company: str,
    snapshots: Mapping[str, SnapshotInspection],
    release_records: Mapping[str, ReleaseEvidenceRecord],
    errors: List[str],
) -> Optional[SourceRecord]:
    label = _rel(root, path)
    try:
        text = _safe_read_text(root, path)
    except ValueError as error:
        errors.append(label + ": " + str(error))
        return None
    frontmatter_text, body = split_frontmatter(text)
    if frontmatter_text is None:
        errors.append(label + ": missing YAML frontmatter")
        return None
    frontmatter = parse_frontmatter(frontmatter_text)
    raw_files = frontmatter.get("raw_files")
    if frontmatter.get("type") != "source" or not isinstance(raw_files, list):
        errors.append(label + ": invalid GitHub source frontmatter")
        return None
    snapshot_records = []
    repo_ids = set()
    for raw_file in raw_files:
        if not isinstance(raw_file, str):
            errors.append(label + ": raw_files entry is not a string")
            continue
        relative = "raw/" + raw_file
        snapshot = snapshots.get(relative)
        if snapshot is None:
            errors.append(
                label + ": raw_files snapshot is missing or unqualified: " + raw_file
            )
            continue
        if snapshot.company != company:
            errors.append(label + ": source company disagrees with raw_files")
        snapshot_records.append(snapshot)
        repo_ids.add(snapshot.repo_id)
    if any(
        snapshot_records[index].collection_date
        < snapshot_records[index + 1].collection_date
        for index in range(len(snapshot_records) - 1)
    ):
        errors.append(label + ": source raw_files are not newest first")
    if len(repo_ids) > 1:
        errors.append(label + ": source raw_files identify more than one repository")
    links = tuple(
        target.strip().rstrip("\\").strip() for target in WIKILINK_RE.findall(body)
    )
    repository_prefix = ""
    if len(repo_ids) == 1:
        repo_id = next(iter(repo_ids))
        repository_prefix = (
            "raw/github/" + company + "/" + Path(repo_id).name + "/"
        )
    for target in links:
        if target in ("snapshot", "CHANGELOG", "release-notes") and snapshot_records:
            errors.append(
                label + ": GitHub evidence wikilink is not path-qualified: " + target
            )
        if not target.startswith("raw/github/"):
            continue
        if repository_prefix and not target.startswith(repository_prefix):
            errors.append(label + ": cross-repository raw link: " + target)
        candidate = _safe_workspace_relative(
            root, target + ("" if target.endswith(".md") else ".md")
        )
        if candidate is None or not _safe_regular_file(root, candidate):
            errors.append(
                label + ": GitHub evidence wikilink does not resolve: " + target
            )
    for raw_file in raw_files:
        expected = (
            "raw/" + raw_file[:-3]
            if isinstance(raw_file, str) and raw_file.endswith(".md")
            else ""
        )
        if expected and expected not in links:
            errors.append(
                label
                + ": raw_files snapshot has no path-qualified wikilink: "
                + raw_file
            )
    ledger = _parse_release_ledger(body, label, errors)
    _validate_source_release_ledger(
        label, snapshot_records, release_records, ledger, errors
    )
    return SourceRecord(
        path=path,
        repo_id=next(iter(repo_ids)) if len(repo_ids) == 1 else "",
        raw_files=tuple(item for item in raw_files if isinstance(item, str)),
        evidence_links=links,
        release_ledger=ledger,
    )


def _parse_release_ledger(
    body: str, label: str, errors: List[str]
) -> Tuple[ReleaseLedgerRow, ...]:
    lines = body.splitlines()
    heading = next(
        (index for index, line in enumerate(lines) if line.strip().lower() == "## release history"),
        None,
    )
    if heading is None:
        return ()
    header_index = next(
        (
            index
            for index in range(heading + 1, len(lines))
            if lines[index].strip()
        ),
        None,
    )
    if header_index is None or not lines[header_index].lstrip().startswith("|"):
        errors.append(label + ": release ledger table is missing")
        return ()
    headers = [cell.strip().lower() for cell in _markdown_table_cells(lines[header_index])]
    required = ("version", "snapshot", "changelog", "release notes")
    if any(name not in headers for name in required):
        errors.append(label + ": release ledger has invalid columns")
        return ()
    indexes = {name: headers.index(name) for name in required}
    rows: List[ReleaseLedgerRow] = []
    for line in lines[header_index + 1 :]:
        stripped = line.strip()
        if not stripped:
            if rows:
                break
            continue
        if not stripped.startswith("|"):
            if rows or stripped.startswith("## "):
                break
            continue
        cells = _markdown_table_cells(line)
        if cells and all(set(cell.strip()) <= {"-", ":"} for cell in cells):
            continue
        if len(cells) <= max(indexes.values()):
            errors.append(label + ": release ledger row is malformed")
            continue
        snapshot_links = _cell_links(cells[indexes["snapshot"]])
        if len(snapshot_links) != 1:
            errors.append(label + ": release ledger row must have one snapshot link")
        changelog_cell = cells[indexes["changelog"]]
        release_notes_cell = cells[indexes["release notes"]]
        rows.append(
            ReleaseLedgerRow(
                version=cells[indexes["version"]].strip().strip("`"),
                snapshot_link=snapshot_links[0] if len(snapshot_links) == 1 else "",
                changelog_links=_cell_links(changelog_cell),
                release_notes_links=_cell_links(release_notes_cell),
                changelog_absent=_explicit_absence(changelog_cell),
                release_notes_absent=_explicit_absence(release_notes_cell),
            )
        )
    return tuple(rows)


def _markdown_table_cells(line: str) -> List[str]:
    content = line.strip()
    if content.startswith("|"):
        content = content[1:]
    if content.endswith("|"):
        content = content[:-1]
    cells = []
    current = []
    link_depth = 0
    index = 0
    while index < len(content):
        pair = content[index : index + 2]
        if pair == "[[":
            link_depth += 1
            current.extend(pair)
            index += 2
            continue
        if pair == "]]" and link_depth:
            link_depth -= 1
            current.extend(pair)
            index += 2
            continue
        if content[index] == "|" and link_depth == 0:
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(content[index])
        index += 1
    cells.append("".join(current).strip())
    return cells


def _cell_links(cell: str) -> Tuple[str, ...]:
    return tuple(
        _normalize_evidence_link(target.strip().rstrip("\\").strip())
        for target in WIKILINK_RE.findall(cell)
    )


def _normalize_evidence_link(target: str) -> str:
    return target[:-3] if target.endswith(".md") else target


def _explicit_absence(cell: str) -> bool:
    return re.search(r"\babsent\b", cell, re.IGNORECASE) is not None


def _validate_source_release_ledger(
    label: str,
    snapshots: Sequence[SnapshotInspection],
    release_records: Mapping[str, ReleaseEvidenceRecord],
    rows: Sequence[ReleaseLedgerRow],
    errors: List[str],
) -> None:
    releases = [
        snapshot
        for snapshot in snapshots
        if snapshot.ref_kind in ("package-version", "tag")
    ]
    expected_order = [
        snapshot.relative_path + "/snapshot" for snapshot in releases
    ]
    actual_order = [row.snapshot_link for row in rows]
    if actual_order != expected_order and set(actual_order) == set(expected_order):
        errors.append(label + ": ledger row order disagrees with raw_files")
    rows_by_snapshot: Dict[str, List[ReleaseLedgerRow]] = {}
    for row in rows:
        rows_by_snapshot.setdefault(row.snapshot_link, []).append(row)
    for snapshot in releases:
        snapshot_link = snapshot.relative_path + "/snapshot"
        matching = rows_by_snapshot.get(snapshot_link, ())
        if len(matching) != 1:
            errors.append(
                label
                + ": release snapshot must have exactly one ledger row: "
                + snapshot.relative_path
            )
            continue
        row = matching[0]
        if row.version != snapshot.version:
            errors.append(label + ": ledger version disagrees with snapshot")
        evidence = release_records.get(snapshot.relative_path)
        if evidence is None:
            continue
        expected_changelogs = tuple(
            _normalize_evidence_link(path) for path in evidence.changelog_paths
        )
        if expected_changelogs:
            if row.changelog_links != expected_changelogs or row.changelog_absent:
                errors.append(
                    label + ": ledger changelog disagrees with snapshot manifest"
                )
        elif (
            row.changelog_links
            or not row.changelog_absent
            or not evidence.changelog_absence_explicit
        ):
            errors.append(label + ": ledger changelog absence is not explicit")
        expected_release_notes = (
            (_normalize_evidence_link(evidence.release_notes_path),)
            if evidence.release_notes_path
            else ()
        )
        if expected_release_notes:
            if (
                row.release_notes_links != expected_release_notes
                or row.release_notes_absent
            ):
                errors.append(
                    label
                    + ": ledger release notes disagree with snapshot manifest"
                )
        elif (
            row.release_notes_links
            or not row.release_notes_absent
            or not evidence.release_notes_explicit
        ):
            errors.append(label + ": ledger release notes absence is not explicit")
    expected_set = set(expected_order)
    for row in rows:
        if row.snapshot_link not in expected_set:
            errors.append(label + ": release ledger row is not declared in raw_files")


def _inspect_dashboards(
    root: Path, errors: List[str]
) -> Tuple[DashboardRecord, ...]:
    records = []
    tracking = root / "tracking/github"
    for name, kind in (
        ("status.json", "status-json"),
        ("collection-status.md", "collection-status"),
        ("ingest-status.md", "ingest-status"),
    ):
        path = tracking / name
        if not path.exists() and not path.is_symlink():
            continue
        try:
            text = _safe_read_text(root, path)
            content = _load_json_strict(text) if kind == "status-json" else text
        except (ValueError, json.JSONDecodeError) as error:
            errors.append(_rel(root, path) + ": invalid dashboard: " + str(error))
            continue
        records.append(DashboardRecord(path=path, kind=kind, content=content))
    return tuple(records)


def _validate_snapshot_identities(report: GitHubReport, errors: List[str]) -> None:
    canonical_by_key: Dict[Tuple[str, str], List[SnapshotInspection]] = {}
    all_by_key: Dict[Tuple[str, str], List[SnapshotInspection]] = {}
    for snapshot in report.snapshots:
        key = (snapshot.repo_id, snapshot.sha)
        all_by_key.setdefault(key, []).append(snapshot)
        if snapshot.capture_kind == "canonical":
            canonical_by_key.setdefault(key, []).append(snapshot)
            if snapshot.capture_revision != 0:
                errors.append(
                    snapshot.relative_path + ": canonical snapshot revision must be zero"
                )
        elif snapshot.capture_kind == "supplement":
            if snapshot.capture_revision <= 0:
                errors.append(
                    snapshot.relative_path + ": supplement revision must be positive"
                )
            suffix = _SUPPLEMENT_SUFFIX.search(snapshot.path.name)
            if suffix is None:
                errors.append(
                    snapshot.relative_path + ": supplement directory must end in -rN"
                )
            elif int(suffix.group(1)) != snapshot.capture_revision:
                errors.append(
                    snapshot.relative_path
                    + ": supplement revision disagrees with directory suffix"
                )
        else:
            errors.append(snapshot.relative_path + ": invalid capture kind")
    for (repo_id, sha), snapshots in sorted(canonical_by_key.items()):
        if len(snapshots) > 1:
            errors.append(
                repo_id + " " + sha + ": more than one canonical snapshot for SHA"
            )
    for key, snapshots in sorted(all_by_key.items()):
        supplements = [
            item for item in snapshots if item.capture_kind == "supplement"
        ]
        if supplements and len(canonical_by_key.get(key, ())) != 1:
            errors.append(
                key[0] + " " + key[1] + ": supplement has no unique canonical snapshot"
            )
        revisions: Dict[int, List[SnapshotInspection]] = {}
        for supplement in supplements:
            revisions.setdefault(supplement.capture_revision, []).append(supplement)
        for revision, captures in sorted(revisions.items()):
            if len(captures) > 1:
                errors.append(
                    key[0]
                    + " "
                    + key[1]
                    + ": duplicate supplement revision "
                    + str(revision)
                )


def _validate_collection_runs(report: GitHubReport, errors: List[str]) -> None:
    for run in report.collection_runs:
        try:
            validate_collection_run(run.events)
        except CollectionReconciliationError as error:
            errors.append(_rel(report.root, run.path) + ": " + str(error))


def _validate_version_indexes(report: GitHubReport, errors: List[str]) -> None:
    indexes = {record.repo.id: record for record in report.version_indexes}
    snapshots_by_path = {item.relative_path: item for item in report.snapshots}
    release_records_by_path = {
        item.snapshot_path: item for item in report.release_evidence_records
    }
    snapshots_by_sha: Dict[Tuple[str, str], List[SnapshotInspection]] = {}
    for item in report.snapshots:
        snapshots_by_sha.setdefault((item.repo_id, item.sha), []).append(item)
    canonical = [
        item for item in report.snapshots if item.capture_kind == "canonical"
    ]
    for snapshot in canonical:
        record = indexes.get(snapshot.repo_id)
        entries = () if record is None else record.index.versions
        found = [
            entry
            for entry in entries
            if entry.sha == snapshot.sha
            and entry.snapshot_path == snapshot.relative_path
        ]
        if len(found) != 1:
            errors.append(
                snapshot.repo_id
                + " "
                + snapshot.version
                + ": retained version missing from index"
            )
    for record in report.version_indexes:
        for entry in record.index.versions:
            snapshot = snapshots_by_path.get(entry.snapshot_path)
            if snapshot is None:
                errors.append(
                    record.repo.id + " " + entry.version + ": index snapshot is missing"
                )
                continue
            if snapshot.sha != entry.sha or snapshot.version != entry.version:
                errors.append(
                    record.repo.id
                    + " "
                    + entry.version
                    + ": index disagrees with snapshot"
                )
            related = sorted(
                snapshots_by_sha.get((record.repo.id, entry.sha), ()),
                key=lambda item: item.capture_revision,
            )
            related_evidence = [
                release_records_by_path[item.relative_path]
                for item in related
                if item.relative_path in release_records_by_path
            ]
            expected_release_notes = ""
            expected_changelogs = set()
            for evidence in related_evidence:
                if evidence.release_notes_path:
                    expected_release_notes = evidence.release_notes_path
                expected_changelogs.update(evidence.changelog_paths)
            if (
                entry.release_notes_path != expected_release_notes
                or tuple(entry.changelog_paths) != tuple(sorted(expected_changelogs))
            ):
                errors.append(
                    record.repo.id
                    + " "
                    + entry.version
                    + ": index release evidence disagrees with snapshot manifest"
                )
            for evidence in (entry.release_notes_path,) + tuple(
                entry.changelog_paths
            ):
                if evidence and not _safe_regular_file(
                    report.root, report.root / Path(evidence)
                ):
                    errors.append(
                        record.repo.id
                        + " "
                        + entry.version
                        + ": indexed release evidence is missing"
                    )
            parsed = parse_semver(entry.version)
            if (
                parsed is not None
                and parsed.prerelease
                and not _prerelease_entry_allowed(entry.package, parsed, record.repo.version_tracks)
            ):
                selector = (
                    record.repo.version_tracks[0].selector
                    if record.repo.version_tracks
                    else "<no configured selector>"
                )
                errors.append(
                    record.repo.id
                    + " "
                    + entry.version
                    + ": prerelease in stable-only track "
                    + selector
                )


def _snapshot_package(ref_name: str, aliases: Sequence[str]) -> str:
    direct = parse_package_tag(ref_name)
    if direct is not None:
        return direct[0]
    packages = {
        parsed[0]
        for parsed in (parse_package_tag(value) for value in aliases)
        if parsed is not None
    }
    return next(iter(packages)) if len(packages) == 1 else ""


def _prerelease_entry_allowed(
    package: str, candidate: SemanticVersion, tracks: Sequence[VersionTrack]
) -> bool:
    for track in tracks:
        selector = track.selector
        if selector.startswith("package:"):
            parsed_package = parse_package_tag(selector[8:])
            if parsed_package is None:
                continue
            selector_package, selector_version = parsed_package
            if selector_package != package:
                continue
            target = parse_semver(selector_version)
        else:
            if package:
                continue
            target = parse_semver(selector)
        if target is None:
            continue
        if target.prerelease:
            if target.is_exact and matches_semver(candidate, target, include_prerelease=True):
                return True
            continue
        if track.include_prerelease and matches_semver(
            candidate, target, include_prerelease=True
        ):
            return True
    return False


def _validate_packets(report: GitHubReport, errors: List[str]) -> None:
    snapshots = {item.relative_path: item for item in report.snapshots}
    indexed = {
        (record.repo.id, entry.sha): entry
        for record in report.version_indexes
        for entry in record.index.versions
    }
    sources_by_repo = {
        source.repo_id: source
        for source in report.source_records
        if source.repo_id
    }
    for packet in report.packets:
        record = packet.record
        label = _rel(report.root, packet.path)
        for endpoint in tuple(
            item for item in (packet.from_entry, packet.to_entry) if item is not None
        ):
            indexed_entry = indexed.get((record.repo_id, endpoint.sha))
            if indexed_entry is None:
                errors.append(label + ": packet endpoint is missing from version index")
            elif (
                indexed_entry.ref_kind != endpoint.ref_kind
                or indexed_entry.ref_name != endpoint.ref_name
                or indexed_entry.version != endpoint.version
                or indexed_entry.package != endpoint.package
            ):
                errors.append(label + ": packet endpoint disagrees with version index")
            endpoint_snapshot = snapshots.get(endpoint.snapshot_path)
            if endpoint_snapshot is None:
                errors.append(label + ": packet endpoint snapshot is missing")
            elif (
                endpoint_snapshot.repo_id != record.repo_id
                or endpoint_snapshot.sha != endpoint.sha
                or endpoint_snapshot.version != endpoint.version
                or endpoint_snapshot.ref_kind != endpoint.ref_kind
                or endpoint_snapshot.ref_name != endpoint.ref_name
                or endpoint_snapshot.package != endpoint.package
                or endpoint_snapshot.aliases != endpoint.aliases
                or endpoint_snapshot.collection_date != endpoint.collection_date
                or endpoint_snapshot.capture_kind != endpoint.capture_kind
                or endpoint_snapshot.release_notes_path
                != endpoint.release_notes_path
                or endpoint_snapshot.changelog_paths != endpoint.changelog_paths
            ):
                errors.append(
                    label
                    + ": packet endpoint disagrees with version index or snapshot manifest"
                )
        target = snapshots.get(record.to_snapshot)
        if target is None:
            errors.append(
                label + ": packet target snapshot is missing"
            )
        elif target.sha != packet.to_sha:
            errors.append(
                label + ": packet target disagrees with snapshot"
            )
        if packet.to_sha and (record.repo_id, packet.to_sha) not in indexed:
            errors.append(
                label + ": packet target is missing from index"
            )
        if packet.current_state == "ingested" and target is not None:
            source = sources_by_repo.get(record.repo_id)
            raw_file = target.relative_path[4:] + "/snapshot.md"
            if source is None or raw_file not in source.raw_files:
                errors.append(
                    label + ": ingested packet is absent from source raw_files"
                )


def _validate_sources(report: GitHubReport, errors: List[str]) -> None:
    seen = {}
    for source in report.source_records:
        if not source.repo_id:
            continue
        if source.repo_id in seen:
            errors.append(
                source.repo_id + ": more than one stable GitHub source page"
            )
        seen[source.repo_id] = source.path


def _validate_release_collection_packets(
    report: GitHubReport, errors: List[str]
) -> None:
    for event in report.collection_events:
        if event.get("dry_run") is True or event.get("state") not in (
            "collected-baseline",
            "collected-change",
        ):
            continue
        repo_id = event.get("repo_id")
        version = event.get("version")
        sha = event.get("sha")
        if (
            not isinstance(repo_id, str)
            or not isinstance(version, str)
            or not isinstance(sha, str)
        ):
            continue
        if parse_semver(version) is None:
            continue
        matching = [
            packet
            for packet in report.packets
            if packet.record.repo_id == repo_id
            and packet.to_sha == sha
            and packet.to_version == version
        ]
        if len(matching) != 1:
            errors.append(
                repo_id
                + " "
                + version
                + ": newly collected release must have exactly one packet; found "
                + str(len(matching))
            )
            continue
        packet_id = event.get("packet_id")
        if packet_id != matching[0].record.packet_id:
            errors.append(
                repo_id
                + " "
                + version
                + ": collection event packet disagrees with artifact"
            )


def _validate_dashboards(report: GitHubReport, errors: List[str]) -> None:
    dashboards = {record.kind: record for record in report.dashboard_records}
    has_generated_state = bool(
        report.snapshots
        or report.version_indexes
        or report.packets
        or report.collection_events
    )
    if not dashboards and not has_generated_state:
        return
    for kind in ("status-json", "collection-status", "ingest-status"):
        if kind not in dashboards:
            errors.append("tracking/github: missing generated dashboard " + kind)
    if len(dashboards) != 3:
        return

    latest: Dict[str, Mapping[str, object]] = {}
    for event in report.collection_events:
        repo_id = event.get("repo_id")
        if (
            isinstance(repo_id, str)
            and event.get("state") in COLLECTION_TERMINAL
        ):
            latest[repo_id] = event
    indexes = {record.repo.id: record.index for record in report.version_indexes}
    repository_rows = [
        {
            "company": repo.company,
            "enabled": repo.enabled,
            "latest_event": dict(latest.get(repo.id, {})),
            "priority": repo.priority,
            "repo_id": repo.id,
            "track": repo.track,
            "versions": [
                entry.version
                for entry in indexes.get(repo.id, VersionIndex(repo.id, ())).versions
            ],
        }
        for repo in report.repositories
    ]
    packet_rows = [
        {
            "packet_id": packet.record.packet_id,
            "packet_type": packet.record.packet_type,
            "repo_id": packet.record.repo_id,
            "state": packet.current_state,
        }
        for packet in report.packets
    ]
    expected_status = {"packets": packet_rows, "repositories": repository_rows}
    if dashboards["status-json"].content != expected_status:
        errors.append(
            "tracking/github/status.json: status disagreement with collection artifacts"
        )

    expected_collection = render_collection_status(
        report.repositories, report.collection_events
    )
    if dashboards["collection-status"].content != expected_collection:
        errors.append(
            "tracking/github/collection-status.md: status disagreement with collection artifacts"
        )
    states = {
        packet_state_key(packet.record.repo_id, packet.record.packet_id):
        packet.current_state
        for packet in report.packets
    }
    expected_ingest = render_ingest_status(
        tuple(packet.record for packet in report.packets), states
    )
    if dashboards["ingest-status"].content != expected_ingest:
        errors.append(
            "tracking/github/ingest-status.md: status disagreement with collection artifacts"
        )


def _safe_directories(
    path: Path, root: Path, errors: List[str]
) -> Tuple[Path, ...]:
    if not _safe_directory(root, path):
        errors.append(_rel(root, path) + ": unsafe symlink or non-directory")
        return ()
    result = []
    try:
        entries = sorted(os.scandir(path), key=lambda item: item.name)
    except OSError:
        errors.append(_rel(root, path) + ": directory could not be inspected")
        return ()
    for entry in entries:
        child = Path(entry.path)
        if entry.is_symlink():
            errors.append(_rel(root, child) + ": unsafe symlink")
        elif entry.is_dir(follow_symlinks=False):
            result.append(child)
    return tuple(result)


def _valid_changed_file(value: str) -> bool:
    fields = value.split("\t")
    if not fields or _CHANGED_STATUS.fullmatch(fields[0]) is None:
        return False
    expected_fields = 3 if fields[0].startswith(("R", "C")) else 2
    if len(fields) != expected_fields:
        return False
    return all(_safe_upstream_path(path) for path in fields[1:])


def _safe_upstream_path(value: str) -> bool:
    path = Path(value)
    return (
        bool(value)
        and not path.is_absolute()
        and ".." not in path.parts
        and path.as_posix() == value
    )


def _safe_workspace_relative(root: Path, value: str) -> Optional[Path]:
    relative = Path(value)
    if (
        not value
        or relative.is_absolute()
        or ".." in relative.parts
        or relative.as_posix() != value
    ):
        return None
    return root / relative


def _safe_directory(root: Path, path: Path) -> bool:
    return _safe_path_kind(root, path, stat.S_ISDIR)


def _safe_regular_file(root: Path, path: Path) -> bool:
    return _safe_path_kind(root, path, stat.S_ISREG)


def _safe_path_kind(root: Path, path: Path, predicate: object) -> bool:
    try:
        relative = path.absolute().relative_to(root.absolute())
    except ValueError:
        return False
    current = root.absolute()
    try:
        if current.is_symlink():
            return False
        for part in relative.parts:
            current = current / part
            mode = current.lstat().st_mode
            if stat.S_ISLNK(mode):
                return False
        return bool(predicate(current.lstat().st_mode))  # type: ignore[operator]
    except OSError:
        return False


def _safe_read_text(root: Path, path: Path) -> str:
    try:
        relative = path.absolute().relative_to(root.absolute())
    except ValueError as error:
        raise ValueError("path escapes workspace") from error
    directory_descriptor = os.open(
        root, os.O_RDONLY | _directory_flag() | _no_follow_flag()
    )
    descriptor: Optional[int] = None
    try:
        parts = relative.parts
        if not parts:
            raise ValueError("path does not identify a file")
        for part in parts[:-1]:
            next_descriptor = os.open(
                part,
                os.O_RDONLY | _directory_flag() | _no_follow_flag(),
                dir_fd=directory_descriptor,
            )
            os.close(directory_descriptor)
            directory_descriptor = next_descriptor
        descriptor = os.open(
            parts[-1],
            os.O_RDONLY | _no_follow_flag(),
            dir_fd=directory_descriptor,
        )
        if not stat.S_ISREG(os.fstat(descriptor).st_mode):
            raise ValueError("file is not regular")
        with os.fdopen(descriptor, "r", encoding="utf-8") as handle:
            descriptor = None
            return handle.read()
    except (OSError, UnicodeDecodeError) as error:
        raise ValueError("file is missing, unsafe, or not UTF-8") from error
    finally:
        if descriptor is not None:
            os.close(descriptor)
        os.close(directory_descriptor)


def _load_json_strict(text: str) -> object:
    def reject_duplicates(pairs: Sequence[Tuple[str, object]]) -> dict:
        value = {}
        for key, item in pairs:
            if key in value:
                raise ValueError("duplicate JSON key " + key)
            value[key] = item
        return value

    return json.loads(text, object_pairs_hook=reject_duplicates)


def _require_json_object(
    value: object, label: str
) -> Mapping[str, object]:
    if type(value) is not dict:
        raise ValueError(label + " is not an object")
    return value


def _directory_flag() -> int:
    flag = getattr(os, "O_DIRECTORY", None)
    if flag is None:
        raise ValueError("directory-only opening is unavailable")
    return flag


def _no_follow_flag() -> int:
    flag = getattr(os, "O_NOFOLLOW", None)
    if flag is None:
        raise ValueError("no-follow opening is unavailable")
    return flag


def _rel(root: Path, path: Path) -> str:
    try:
        return path.absolute().relative_to(root.absolute()).as_posix()
    except ValueError:
        return str(path)


def _deduplicated(values: Iterable[str]) -> List[str]:
    result = []
    seen = set()
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result
