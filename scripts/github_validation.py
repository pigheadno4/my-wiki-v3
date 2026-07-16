"""Deterministic validation for GitHub collection artifacts."""

from __future__ import annotations

from dataclasses import dataclass
import json
import os
from pathlib import Path
import stat
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

from github_git import ResolvedRef
from github_packets import PacketRecord, VersionIndex, load_version_index
from github_registry import RepoConfig, VersionTrack, load_registry
from github_reporting import (
    COLLECTION_TERMINAL,
    StateTransitionError,
    packet_state_key,
    render_collection_status,
    render_ingest_status,
    validate_packet_history,
)
from github_snapshot import (
    SnapshotFile,
    SnapshotRecord,
    _read_metadata,
    _validate_metadata_schema,
    validate_staged_snapshot,
)
from github_versions import matches_semver, parse_package_tag, parse_semver
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
    to_sha: str
    to_version: str


@dataclass(frozen=True)
class SourceRecord:
    path: Path
    repo_id: str
    raw_files: Tuple[str, ...]
    evidence_links: Tuple[str, ...]


@dataclass(frozen=True)
class DashboardRecord:
    path: Path
    kind: str
    content: object


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
    version_indexes = _inspect_version_indexes(root, repositories, errors)
    packets = _inspect_packets(root, repositories, errors)
    collection_events = _inspect_collection_events(root, errors)
    sources = _inspect_sources(root, snapshots, errors)
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
        collection_events=collection_events,
    )


def validate_github(report: GitHubReport) -> List[str]:
    """Return all structural and release-retention errors in one report."""
    errors = list(report.inspection_errors)
    _validate_snapshot_identities(report, errors)
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
            if entry.is_file(follow_symlinks=False) or entry.is_symlink()
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

    target = contract.get("to")
    to_sha = ""
    to_version = ""
    if type(target) is not dict:
        errors.append(label + ": packet target entry is invalid")
    else:
        if type(target.get("sha")) is str:
            to_sha = target["sha"]
        if type(target.get("version")) is str:
            to_version = target["version"]
    return PacketInspection(
        path=directory,
        record=record,
        current_state=current_state,
        to_sha=to_sha,
        to_version=to_version,
    )


def _inspect_collection_events(
    root: Path, errors: List[str]
) -> Tuple[Mapping[str, object], ...]:
    runs = root / "tracking/github/runs"
    if not runs.exists() and not runs.is_symlink():
        return ()
    if not _safe_directory(root, runs):
        errors.append(_rel(root, runs) + ": collection runs namespace is unsafe")
        return ()
    events: List[Mapping[str, object]] = []
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
            for line in _safe_read_text(root, path).splitlines():
                events.append(
                    _require_json_object(_load_json_strict(line), "collection event")
                )
        except (ValueError, json.JSONDecodeError) as error:
            errors.append(_rel(root, path) + ": invalid collection event: " + str(error))
    return tuple(events)


def _inspect_sources(
    root: Path, snapshots: Sequence[SnapshotInspection], errors: List[str]
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
            record = _inspect_source(root, path, company.name, snapshot_map, errors)
            if record is not None:
                records.append(record)
    return tuple(records)


def _inspect_source(
    root: Path,
    path: Path,
    company: str,
    snapshots: Mapping[str, SnapshotInspection],
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
    for target in links:
        if target in ("snapshot", "CHANGELOG", "release-notes") and snapshot_records:
            errors.append(
                label + ": GitHub evidence wikilink is not path-qualified: " + target
            )
        if not target.startswith("raw/github/"):
            continue
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
    return SourceRecord(
        path=path,
        repo_id=next(iter(repo_ids)) if len(repo_ids) == 1 else "",
        raw_files=tuple(item for item in raw_files if isinstance(item, str)),
        evidence_links=links,
    )


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


def _validate_version_indexes(report: GitHubReport, errors: List[str]) -> None:
    indexes = {record.repo.id: record for record in report.version_indexes}
    snapshots_by_path = {item.relative_path: item for item in report.snapshots}
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
            for track in record.repo.version_tracks:
                if _entry_matches_track(entry.package, entry.version, track):
                    parsed = parse_semver(entry.version)
                    if (
                        parsed is not None
                        and parsed.prerelease
                        and not track.include_prerelease
                    ):
                        errors.append(
                            record.repo.id
                            + " "
                            + entry.version
                            + ": prerelease in stable-only track "
                            + track.selector
                        )


def _entry_matches_track(package: str, version: str, track: VersionTrack) -> bool:
    selector = track.selector
    candidate = parse_semver(version)
    if candidate is None:
        return False
    if selector.startswith("package:"):
        parsed = parse_package_tag(selector[8:])
        if parsed is None or parsed[0] != package:
            return False
        target = parse_semver(parsed[1])
    else:
        target = parse_semver(selector)
    return (
        target is not None
        and matches_semver(candidate, target, include_prerelease=True)
    )


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
        target = snapshots.get(record.to_snapshot)
        if target is None:
            errors.append(
                _rel(report.root, packet.path) + ": packet target snapshot is missing"
            )
        elif target.sha != packet.to_sha:
            errors.append(
                _rel(report.root, packet.path)
                + ": packet target disagrees with snapshot"
            )
        if packet.to_sha and (record.repo_id, packet.to_sha) not in indexed:
            errors.append(
                _rel(report.root, packet.path) + ": packet target is missing from index"
            )
        if packet.current_state == "ingested" and target is not None:
            source = sources_by_repo.get(record.repo_id)
            raw_file = target.relative_path[4:] + "/snapshot.md"
            if source is None or raw_file not in source.raw_files:
                errors.append(
                    _rel(report.root, packet.path)
                    + ": ingested packet is absent from source raw_files"
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
