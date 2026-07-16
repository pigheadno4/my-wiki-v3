"""Deterministic version indexes and review-only GitHub ingest packets."""

from dataclasses import dataclass, replace
from functools import cmp_to_key
import fnmatch
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

from github_git import ResolvedRef
from github_registry import RepoConfig
from github_snapshot import SnapshotRecord
from github_versions import compare_semver, parse_package_tag, parse_semver


_DEFAULT_HIGH_CHURN_PARTS = {
    ".git",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "vendor",
}
_LOCK_FILENAMES = {
    "cargo.lock",
    "composer.lock",
    "gemfile.lock",
    "package-lock.json",
    "pnpm-lock.yaml",
    "podfile.lock",
    "yarn.lock",
}
_SAFE_PART = re.compile(r"[^A-Za-z0-9._-]+")


class PacketError(ValueError):
    """A version index or generated packet cannot be made safely."""


@dataclass(frozen=True)
class VersionEntry:
    ref_kind: str
    ref_name: str
    version: str
    sha: str
    aliases: Tuple[str, ...]
    snapshot_path: str
    collection_date: str
    package: str
    capture_kind: str
    release_notes_path: str
    changelog_paths: Tuple[str, ...]


@dataclass(frozen=True)
class VersionIndex:
    repo_id: str
    versions: Tuple[VersionEntry, ...]


@dataclass(frozen=True)
class PacketRecord:
    packet_id: str
    repo_id: str
    packet_type: str
    from_snapshot: str
    to_snapshot: str
    required_reading: Tuple[str, ...]
    changed_files: Tuple[str, ...]
    initial_state: str
    directory: Path


def load_version_index(path: Path, repo_id: str) -> VersionIndex:
    """Load one repository's generated index or return its empty initial state."""
    if not path.exists():
        return VersionIndex(repo_id, ())
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise PacketError("invalid version index " + str(path)) from error
    if not isinstance(data, dict) or data.get("repo_id") != repo_id:
        raise PacketError("version index repository does not match " + repo_id)
    versions_data = data.get("versions")
    if not isinstance(versions_data, list):
        raise PacketError("version index versions must be a list")
    entries = tuple(_entry_from_json(item) for item in versions_data)
    if len({entry.sha for entry in entries}) != len(entries):
        raise PacketError("version index contains more than one entry for a SHA")
    return VersionIndex(repo_id, tuple(sorted(entries, key=_entry_key)))


def save_version_index(path: Path, index: VersionIndex) -> None:
    """Atomically replace deterministic JSON generated state for one repository."""
    data = {
        "repo_id": index.repo_id,
        "versions": [_entry_to_json(entry) for entry in sorted(index.versions, key=_entry_key)],
    }
    _write_json_atomic(path, data)


def record_snapshot(index: VersionIndex, snapshot: SnapshotRecord) -> VersionIndex:
    """Record one canonical SHA, merging aliases and supplemental evidence in place."""
    if index.repo_id != snapshot.repo_id or snapshot.ref.repo_id != snapshot.repo_id:
        raise PacketError("snapshot repository does not match version index")

    existing = next((entry for entry in index.versions if entry.sha == snapshot.ref.sha), None)
    if snapshot.capture_kind == "supplement":
        if existing is None:
            return index
        merged = _merge_snapshot_evidence(existing, snapshot)
        return _replace_entry(index, existing.sha, merged)
    if snapshot.capture_kind != "canonical":
        raise PacketError("snapshot capture_kind must be canonical or supplement")
    if existing is not None:
        return _replace_entry(index, existing.sha, _merge_snapshot_evidence(existing, snapshot))

    entry = _entry_from_snapshot(snapshot)
    return VersionIndex(index.repo_id, tuple(sorted(index.versions + (entry,), key=_entry_key)))


def select_prior(index: VersionIndex, ref: ResolvedRef) -> Optional[VersionEntry]:
    """Choose the latest compatible prior evidence entry for an exact resolved ref."""
    if index.repo_id != ref.repo_id:
        raise PacketError("resolved reference repository does not match version index")
    candidates = [entry for entry in index.versions if entry.sha != ref.sha]
    package = _package_for_ref(ref)
    if package:
        compatible = [entry for entry in candidates if entry.package == package]
        return _latest_version_before(compatible, ref.version)
    if ref.ref_kind == "branch":
        compatible = [
            entry
            for entry in candidates
            if entry.ref_kind == "branch" and entry.ref_name == ref.ref_name
        ]
        return _latest_capture(compatible)

    compatible = [entry for entry in candidates if entry.ref_kind == ref.ref_kind]
    prior = _latest_version_before(compatible, ref.version)
    if prior is not None:
        return prior
    aliases = set(ref.aliases)
    if aliases:
        return _latest_capture([entry for entry in compatible if aliases.intersection(entry.aliases)])
    return None


def build_baseline_packet(
    config: RepoConfig, current: SnapshotRecord, packet_root: Path
) -> PacketRecord:
    """Generate an awaiting-review baseline packet for one immutable snapshot."""
    _require_snapshot_config(config, current)
    entry = _entry_from_snapshot(current)
    packet_id = "baseline-" + _safe_part(entry.version) + "-" + entry.sha[:7]
    required_reading = _required_reading((entry,), ())
    return _write_packet(
        config,
        packet_root,
        packet_id,
        "baseline",
        None,
        entry,
        required_reading,
        (),
        "",
    )


def build_delta_packet(
    config: RepoConfig,
    prior: VersionEntry,
    current: SnapshotRecord,
    repo_root: Path,
    packet_root: Path,
) -> PacketRecord:
    """Generate an awaiting-review delta packet from a local Git checkout."""
    _require_snapshot_config(config, current)
    _require_entry_config(config, prior)
    current_entry = _entry_from_snapshot(current)
    selected_paths = _selected_paths(config, _entry_file_paths(prior, packet_root), _snapshot_file_paths(current))
    changed_files, source_diff = _git_delta(repo_root, prior.sha, current.ref.sha, selected_paths)
    reading = _required_reading(
        (prior, current_entry),
        _changed_evidence_paths(prior, current_entry, changed_files),
    )
    packet_id = _packet_id("delta", prior, current_entry)
    return _write_packet(
        config,
        packet_root,
        packet_id,
        "delta",
        prior,
        current_entry,
        reading,
        changed_files,
        source_diff,
    )


def build_comparison_packet(
    config: RepoConfig,
    prior: VersionEntry,
    current: VersionEntry,
    repo_root: Path,
    packet_root: Path,
) -> PacketRecord:
    """Generate an explicit, review-only comparison packet between two snapshots."""
    _require_entry_config(config, prior)
    _require_entry_config(config, current)
    selected_paths = _selected_paths(
        config, _entry_file_paths(prior, packet_root), _entry_file_paths(current, packet_root)
    )
    changed_files, source_diff = _git_delta(repo_root, prior.sha, current.sha, selected_paths)
    reading = _required_reading(
        (prior, current), _changed_evidence_paths(prior, current, changed_files)
    )
    packet_id = _packet_id("comparison", prior, current)
    return _write_packet(
        config,
        packet_root,
        packet_id,
        "comparison",
        prior,
        current,
        reading,
        changed_files,
        source_diff,
    )


def _entry_from_snapshot(snapshot: SnapshotRecord) -> VersionEntry:
    snapshot_path = _evidence_path(snapshot.target_path)
    changelogs = tuple(
        sorted(
            _evidence_path(snapshot.target_path / "files" / item.path)
            for item in snapshot.files
            if Path(item.path).name.lower().startswith("changelog")
        )
    )
    release_notes_path = ""
    if snapshot.release_notes_source_url is not None:
        release_notes_path = _evidence_path(snapshot.target_path / "release-notes.md")
    return VersionEntry(
        ref_kind=snapshot.ref.ref_kind,
        ref_name=snapshot.ref.ref_name,
        version=snapshot.ref.version,
        sha=snapshot.ref.sha,
        aliases=tuple(sorted(set(snapshot.ref.aliases))),
        snapshot_path=snapshot_path,
        collection_date=snapshot.collection_date,
        package=_package_for_ref(snapshot.ref),
        capture_kind=snapshot.capture_kind,
        release_notes_path=release_notes_path,
        changelog_paths=changelogs,
    )


def _merge_snapshot_evidence(entry: VersionEntry, snapshot: SnapshotRecord) -> VersionEntry:
    supplement = _entry_from_snapshot(snapshot)
    return replace(
        entry,
        aliases=tuple(sorted(set(entry.aliases).union(supplement.aliases))),
        release_notes_path=entry.release_notes_path or supplement.release_notes_path,
        changelog_paths=tuple(sorted(set(entry.changelog_paths).union(supplement.changelog_paths))),
    )


def _replace_entry(index: VersionIndex, sha: str, updated: VersionEntry) -> VersionIndex:
    return VersionIndex(
        index.repo_id,
        tuple(sorted((updated if entry.sha == sha else entry for entry in index.versions), key=_entry_key)),
    )


def _latest_version_before(entries: Sequence[VersionEntry], version: str) -> Optional[VersionEntry]:
    target = parse_semver(version)
    if target is None:
        return None
    candidates = []
    for entry in entries:
        parsed = parse_semver(entry.version)
        if parsed is not None and compare_semver(parsed, target) < 0:
            candidates.append((parsed, entry))
    if not candidates:
        return None
    candidates.sort(key=cmp_to_key(lambda left, right: compare_semver(left[0], right[0])))
    latest_version = candidates[-1][0]
    return _latest_capture([entry for parsed, entry in candidates if compare_semver(parsed, latest_version) == 0])


def _latest_capture(entries: Sequence[VersionEntry]) -> Optional[VersionEntry]:
    if not entries:
        return None
    return max(entries, key=lambda entry: (entry.collection_date, entry.snapshot_path, entry.sha))


def _package_for_ref(ref: ResolvedRef) -> str:
    package_tags = [parse_package_tag(value) for value in (ref.ref_name,) + ref.aliases]
    packages = {item[0] for item in package_tags if item is not None}
    return next(iter(packages)) if len(packages) == 1 else ""


def _entry_key(entry: VersionEntry) -> Tuple[str, str, str, str, str]:
    return (entry.ref_kind, entry.package, entry.version, entry.ref_name, entry.sha)


def _entry_to_json(entry: VersionEntry) -> dict:
    return {
        "aliases": list(entry.aliases),
        "capture_kind": entry.capture_kind,
        "changelog_paths": list(entry.changelog_paths),
        "collection_date": entry.collection_date,
        "package": entry.package,
        "ref_kind": entry.ref_kind,
        "ref_name": entry.ref_name,
        "release_notes_path": entry.release_notes_path,
        "sha": entry.sha,
        "snapshot_path": entry.snapshot_path,
        "version": entry.version,
    }


def _entry_from_json(value: object) -> VersionEntry:
    if not isinstance(value, dict):
        raise PacketError("version index entry must be an object")
    fields = (
        "ref_kind",
        "ref_name",
        "version",
        "sha",
        "snapshot_path",
        "collection_date",
        "package",
        "capture_kind",
        "release_notes_path",
    )
    if any(not isinstance(value.get(field), str) for field in fields):
        raise PacketError("version index entry has invalid scalar fields")
    aliases = value.get("aliases")
    changelogs = value.get("changelog_paths")
    if (
        not isinstance(aliases, list)
        or not isinstance(changelogs, list)
        or any(not isinstance(item, str) for item in aliases + changelogs)
    ):
        raise PacketError("version index entry has invalid evidence paths")
    return VersionEntry(
        ref_kind=value["ref_kind"],
        ref_name=value["ref_name"],
        version=value["version"],
        sha=value["sha"],
        aliases=tuple(sorted(set(aliases))),
        snapshot_path=value["snapshot_path"],
        collection_date=value["collection_date"],
        package=value["package"],
        capture_kind=value["capture_kind"],
        release_notes_path=value["release_notes_path"],
        changelog_paths=tuple(sorted(set(changelogs))),
    )


def _git_delta(
    repo_root: Path, from_sha: str, to_sha: str, selected_paths: Sequence[str]
) -> Tuple[Tuple[str, ...], str]:
    if not selected_paths:
        return (), ""
    prefix = ["diff", "--find-renames", "--no-ext-diff", "--no-textconv", from_sha, to_sha, "--"]
    changed = _run_git(["diff", "--name-status", "--find-renames", "--no-ext-diff", "--no-textconv", from_sha, to_sha, "--"] + list(selected_paths), repo_root)
    source_diff = _run_git(prefix + list(selected_paths), repo_root)
    return tuple(line for line in changed.splitlines() if line), source_diff


def _run_git(args: Sequence[str], repo_root: Path) -> str:
    result = subprocess.run(
        ["git"] + list(args),
        cwd=str(repo_root),
        check=False,
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        detail = result.stderr.strip()
        raise PacketError("git " + " ".join(args) + " failed" + (": " + detail if detail else ""))
    return result.stdout


def _selected_paths(config: RepoConfig, *groups: Iterable[str]) -> Tuple[str, ...]:
    paths = set()
    for group in groups:
        for path in group:
            if _selected_path(config, path):
                paths.add(path)
    return tuple(sorted(paths))


def _selected_path(config: RepoConfig, path: str) -> bool:
    relative = Path(path)
    if relative.is_absolute() or ".." in relative.parts or not path:
        return False
    lowered = {part.lower() for part in relative.parts}
    if lowered.intersection(_DEFAULT_HIGH_CHURN_PARTS):
        return False
    if relative.name.lower() in _LOCK_FILENAMES:
        return False
    return not any(
        fnmatch.fnmatch(path, pattern) or fnmatch.fnmatch(relative.name, pattern)
        for pattern in config.exclude_paths
    )


def _snapshot_file_paths(snapshot: SnapshotRecord) -> Tuple[str, ...]:
    return tuple(item.path for item in snapshot.files)


def _entry_file_paths(entry: VersionEntry, packet_root: Path) -> Tuple[str, ...]:
    manifest = _absolute_evidence_path(entry.snapshot_path + "/snapshot.md", packet_root)
    try:
        text = manifest.read_text(encoding="utf-8")
        start = text.index("```json\n") + len("```json\n")
        end = text.index("\n```", start)
        metadata = json.loads(text[start:end])
    except (OSError, UnicodeDecodeError, ValueError, json.JSONDecodeError):
        return ()
    files = metadata.get("files") if isinstance(metadata, dict) else None
    if not isinstance(files, list):
        return ()
    return tuple(
        item["path"]
        for item in files
        if isinstance(item, dict) and isinstance(item.get("path"), str)
    )


def _changed_evidence_paths(
    prior: VersionEntry, current: VersionEntry, changed_files: Sequence[str]
) -> Tuple[str, ...]:
    paths = []
    for line in changed_files:
        fields = line.split("\t")
        if not fields:
            continue
        status = fields[0]
        if status.startswith("R") or status.startswith("C"):
            if len(fields) >= 3:
                paths.append(_file_evidence_path(prior, fields[1]))
                paths.append(_file_evidence_path(current, fields[2]))
        elif len(fields) >= 2:
            entry = prior if status.startswith("D") else current
            paths.append(_file_evidence_path(entry, fields[1]))
    return tuple(_deduplicated(paths))


def _file_evidence_path(entry: VersionEntry, relative: str) -> str:
    return entry.snapshot_path + "/files/" + relative


def _required_reading(
    entries: Sequence[VersionEntry], changed_evidence: Sequence[str]
) -> Tuple[str, ...]:
    manifests = [entry.snapshot_path + "/snapshot.md" for entry in entries]
    release_notes = [entry.release_notes_path for entry in entries if entry.release_notes_path]
    changelogs = [path for entry in entries for path in entry.changelog_paths]
    return tuple(_deduplicated(manifests + release_notes + changelogs + list(changed_evidence)))


def _write_packet(
    config: RepoConfig,
    packet_root: Path,
    packet_id: str,
    packet_type: str,
    prior: Optional[VersionEntry],
    current: VersionEntry,
    required_reading: Tuple[str, ...],
    changed_files: Sequence[str],
    source_diff: str,
) -> PacketRecord:
    directory = packet_root / packet_id
    record = PacketRecord(
        packet_id=packet_id,
        repo_id=config.id,
        packet_type=packet_type,
        from_snapshot=prior.snapshot_path if prior is not None else "",
        to_snapshot=current.snapshot_path,
        required_reading=required_reading,
        changed_files=tuple(changed_files),
        initial_state="awaiting-review",
        directory=directory,
    )
    packet_data = {
        "changed_files": list(record.changed_files),
        "from": _entry_to_json(prior) if prior is not None else None,
        "from_snapshot": record.from_snapshot,
        "initial_state": record.initial_state,
        "packet_id": record.packet_id,
        "packet_type": record.packet_type,
        "repo_id": record.repo_id,
        "required_reading": list(record.required_reading),
        "to": _entry_to_json(current),
        "to_snapshot": record.to_snapshot,
    }
    _write_json_atomic(directory / "packet.json", packet_data)
    _write_text_atomic(directory / "ingest-packet.md", _render_packet_markdown(record, prior, current))
    _write_text_atomic(
        directory / "changed-files.txt", "\n".join(record.changed_files) + "\n"
    )
    _write_text_atomic(
        directory / "source-diff.patch", source_diff if source_diff.endswith("\n") else source_diff + "\n"
    )
    _write_text_atomic(
        directory / "state-events.jsonl",
        json.dumps(
            {"packet_id": record.packet_id, "state": record.initial_state},
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n",
    )
    return record


def _render_packet_markdown(
    record: PacketRecord, prior: Optional[VersionEntry], current: VersionEntry
) -> str:
    lines = [
        "# GitHub ingest packet",
        "",
        "## Identity",
        "",
        "| Field | Value |",
        "| --- | --- |",
        "| Packet ID | " + record.packet_id + " |",
        "| Repository | " + record.repo_id + " |",
        "| Type | " + record.packet_type + " |",
        "| Initial state | awaiting-review |",
    ]
    for label, entry in (("From", prior), ("To", current)):
        if entry is None:
            lines.append("| " + label + " | No prior snapshot |")
            continue
        release = (entry.package + "@" if entry.package else "") + entry.version
        lines.append("| " + label + " | " + release + " at " + entry.sha + " |")
        lines.append("| " + label + " snapshot | " + entry.snapshot_path + " |")
    lines.extend(["", "## Evidence (immutable raw)", ""])
    for label, entry in (("From", prior), ("To", current)):
        if entry is None:
            continue
        if entry.release_notes_path:
            lines.append("- " + label + " release notes: " + entry.release_notes_path)
        else:
            lines.append("- " + label + " release notes: absent from immutable snapshot")
        if entry.changelog_paths:
            lines.extend("- " + label + " changelog: " + path for path in entry.changelog_paths)
        else:
            lines.append("- " + label + " changelog: absent from immutable snapshot")
    lines.extend(["", "### Required reading (in order)", ""])
    lines.extend(str(index) + ". " + path for index, path in enumerate(record.required_reading, 1))
    lines.extend(
        [
            "",
            "## Generated guidance (tracking only)",
            "",
            "Read every immutable raw path above in full before changing wiki content. "
            "`changed-files.txt` and `source-diff.patch` are generated review aids, not source evidence.",
            "",
            "### Changed files",
            "",
        ]
    )
    if record.changed_files:
        lines.extend("- `" + path + "`" for path in record.changed_files)
    else:
        lines.append("- No source diff applies to this baseline packet.")
    return "\n".join(lines) + "\n"


def _packet_id(packet_type: str, prior: VersionEntry, current: VersionEntry) -> str:
    return (
        packet_type
        + "-"
        + _safe_part(prior.version)
        + "-"
        + prior.sha[:7]
        + "-to-"
        + _safe_part(current.version)
        + "-"
        + current.sha[:7]
    )


def _safe_part(value: str) -> str:
    return _SAFE_PART.sub("-", value).strip("-.") or "ref"


def _evidence_path(path: Path) -> str:
    parts = path.as_posix().split("/")
    for index in range(len(parts) - 1):
        if parts[index] == "raw" and parts[index + 1] == "github":
            return "/".join(parts[index:])
    return path.as_posix()


def _absolute_evidence_path(path: str, packet_root: Path) -> Path:
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    for ancestor in (packet_root,) + tuple(packet_root.parents):
        if ancestor.name == "tracking":
            return ancestor.parent / candidate
    return candidate


def _deduplicated(values: Iterable[str]) -> List[str]:
    result = []
    seen = set()
    for value in values:
        if value and value not in seen:
            seen.add(value)
            result.append(value)
    return result


def _require_snapshot_config(config: RepoConfig, snapshot: SnapshotRecord) -> None:
    if snapshot.repo_id != config.id or snapshot.ref.repo_id != config.id:
        raise PacketError("snapshot repository does not match configuration")


def _require_entry_config(config: RepoConfig, entry: VersionEntry) -> None:
    if not entry.snapshot_path:
        raise PacketError("version entry has no snapshot path for " + config.id)


def _write_json_atomic(path: Path, value: object) -> None:
    _write_text_atomic(path, json.dumps(value, indent=2, sort_keys=True) + "\n")


def _write_text_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=str(path.parent))
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
        os.replace(str(temporary), str(path))
    except Exception:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass
        raise
