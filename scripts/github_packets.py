"""Deterministic version indexes and review-only GitHub ingest packets."""

from contextlib import contextmanager
from dataclasses import dataclass, replace
from datetime import datetime
import fcntl
from functools import cmp_to_key
import fnmatch
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import tempfile
from typing import Dict, Iterable, Iterator, List, Optional, Sequence, Tuple

from github_git import ResolvedRef
from github_registry import RepoConfig
from github_snapshot import SnapshotRecord, SnapshotReleaseEvidence
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
_SHA = re.compile(r"^(?:[0-9a-f]{40}|[0-9a-f]{64})$")
_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_INDEX_KEYS = {"branch_observations", "capture_order", "repo_id", "versions"}
_CAPTURE_ORDER_INDEX_KEYS = {"capture_order", "repo_id", "versions"}
_LEGACY_INDEX_KEYS = {"repo_id", "versions"}
_ENTRY_KEYS = {
    "aliases",
    "capture_kind",
    "changelog_paths",
    "collection_date",
    "package",
    "ref_kind",
    "ref_name",
    "release_notes_path",
    "sha",
    "snapshot_path",
    "version",
}
_REF_KINDS = {"branch", "commit", "package-version", "tag"}
_PACKET_FILES = {
    "packet.json",
    "ingest-packet.md",
    "changed-files.txt",
    "source-diff.patch",
    "state-events.jsonl",
}
_PACKET_LOCK = ".packet.lock"


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
class BranchObservation:
    ref_name: str
    sha: str


@dataclass(frozen=True)
class VersionIndex:
    repo_id: str
    versions: Tuple[VersionEntry, ...]
    capture_order: Tuple[str, ...] = ()
    branch_observations: Tuple[BranchObservation, ...] = ()


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


def load_version_index(path: Path, config: RepoConfig) -> VersionIndex:
    """Load one repository's generated index or return its empty initial state."""
    repo_id = config.id
    if not path.exists():
        return VersionIndex(repo_id, ())
    try:
        data = _load_json(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, ValueError, json.JSONDecodeError) as error:
        raise PacketError("invalid version index " + str(path)) from error
    if type(data) is not dict or set(data) not in (
        _INDEX_KEYS,
        _CAPTURE_ORDER_INDEX_KEYS,
        _LEGACY_INDEX_KEYS,
    ):
        raise PacketError("version index has an invalid schema")
    if type(data["repo_id"]) is not str or data["repo_id"] != repo_id:
        raise PacketError("version index repository does not match " + repo_id)
    versions_data = data["versions"]
    if type(versions_data) is not list:
        raise PacketError("version index versions must be a list")
    evidence_root = _evidence_root_from_index(path, config)
    entries = tuple(_entry_from_json(item, evidence_root) for item in versions_data)
    _validate_index_entry_identities(entries)
    if tuple(sorted(entries, key=_entry_key)) != entries:
        raise PacketError("version index entries are not in deterministic order")
    capture_order = data.get("capture_order", list(_legacy_capture_order(entries)))
    if (
        type(capture_order) is not list
        or any(type(sha) is not str for sha in capture_order)
        or len(set(capture_order)) != len(capture_order)
        or set(capture_order) != {entry.sha for entry in entries}
    ):
        raise PacketError("version index capture_order must contain every SHA exactly once")
    observations = (
        _branch_observations_from_json(data["branch_observations"], entries)
        if "branch_observations" in data
        else _infer_legacy_branch_observations(entries)
    )
    return VersionIndex(repo_id, entries, tuple(capture_order), observations)


def save_version_index(path: Path, index: VersionIndex) -> None:
    """Atomically replace deterministic JSON generated state for one repository."""
    _validate_index_entry_identities(index.versions)
    _validate_branch_observations(index.branch_observations, index.versions)
    data = {
        "branch_observations": [
            {"ref_name": item.ref_name, "sha": item.sha}
            for item in index.branch_observations
        ],
        "capture_order": list(_capture_order(index)),
        "repo_id": index.repo_id,
        "versions": [_entry_to_json(entry) for entry in sorted(index.versions, key=_entry_key)],
    }
    _write_json_atomic(path, data)


def _validate_index_entry_identities(entries: Sequence[VersionEntry]) -> None:
    snapshots: Dict[str, set] = {}
    immutable_owners: Dict[str, Tuple[str, Tuple[str, str]]] = {}
    release_identities = set()
    branch_identities = set()
    commit_identities = set()
    for entry in entries:
        snapshots.setdefault(entry.sha, set()).add(entry.snapshot_path)
        if len(snapshots[entry.sha]) > 1:
            raise PacketError("version index maps one SHA to multiple canonical snapshots")
        if entry.ref_kind == "branch":
            identity = (entry.ref_name, entry.sha)
            if identity in branch_identities:
                raise PacketError("version index contains duplicate branch capture entries")
            branch_identities.add(identity)
            continue
        if entry.ref_kind in ("package-version", "tag"):
            semantic = _semantic_release_identity(entry)
            identity = (semantic, entry.sha)
            if identity in release_identities:
                raise PacketError("version index contains duplicate retained release identities")
            release_identities.add(identity)
        else:
            identity = (entry.ref_kind, entry.ref_name)
            if identity in commit_identities:
                raise PacketError("version index contains conflicting reference entries")
            commit_identities.add(identity)
            semantic = (entry.ref_kind, entry.ref_name)
        for name in sorted(_immutable_names(entry)):
            owner = immutable_owners.get(name)
            current = (entry.sha, semantic)
            if owner is not None and owner != current:
                raise PacketError("version index contains conflicting reference entries")
            immutable_owners[name] = current


def _legacy_capture_order(entries: Sequence[VersionEntry]) -> Tuple[str, ...]:
    order = []
    seen = set()
    for entry in entries:
        if entry.sha not in seen:
            seen.add(entry.sha)
            order.append(entry.sha)
    return tuple(order)


def _branch_observations_from_json(
    value: object, entries: Sequence[VersionEntry]
) -> Tuple[BranchObservation, ...]:
    if type(value) is not list:
        raise PacketError("version index branch_observations must be a list")
    branch_entries = {
        (entry.ref_name, entry.sha)
        for entry in entries
        if entry.ref_kind == "branch"
    }
    observations = []
    heads: Dict[str, str] = {}
    for item in value:
        if (
            type(item) is not dict
            or set(item) != {"ref_name", "sha"}
            or type(item["ref_name"]) is not str
            or type(item["sha"]) is not str
            or not _valid_ref_name(item["ref_name"])
            or _SHA.fullmatch(item["sha"]) is None
        ):
            raise PacketError("version index branch observation has an invalid schema")
        identity = (item["ref_name"], item["sha"])
        if identity not in branch_entries:
            raise PacketError("version index branch observation has no matching capture")
        if heads.get(item["ref_name"]) == item["sha"]:
            raise PacketError("version index branch observations contain a redundant head")
        heads[item["ref_name"]] = item["sha"]
        observations.append(BranchObservation(*identity))
    if branch_entries - {(item.ref_name, item.sha) for item in observations}:
        raise PacketError("version index branch capture has no observation")
    return tuple(observations)


def _validate_branch_observations(
    observations: Sequence[BranchObservation], entries: Sequence[VersionEntry]
) -> None:
    _branch_observations_from_json(
        [
            {"ref_name": item.ref_name, "sha": item.sha}
            for item in observations
        ],
        entries,
    )


def _infer_legacy_branch_observations(
    entries: Sequence[VersionEntry],
) -> Tuple[BranchObservation, ...]:
    by_branch: Dict[str, List[VersionEntry]] = {}
    for entry in entries:
        if entry.ref_kind == "branch":
            by_branch.setdefault(entry.ref_name, []).append(entry)
    ordered = []
    for ref_name, history in sorted(by_branch.items()):
        dates = [entry.collection_date for entry in history]
        if len(history) > 1 and len(set(dates)) != len(dates):
            raise PacketError(
                "ambiguous legacy branch history for "
                + ref_name
                + "; explicit migration is required"
            )
        ordered.extend(
            (entry.collection_date, ref_name, entry.sha)
            for entry in sorted(history, key=lambda item: item.collection_date)
        )
    return tuple(
        BranchObservation(ref_name, sha)
        for _, ref_name, sha in sorted(ordered)
    )


def record_snapshot(index: VersionIndex, snapshot: SnapshotRecord) -> VersionIndex:
    """Record one capture, retained ref identity, and changed branch head."""
    if index.repo_id != snapshot.repo_id or snapshot.ref.repo_id != snapshot.repo_id:
        raise PacketError("snapshot repository does not match version index")

    updated = index
    for incoming in _entries_from_snapshot(snapshot):
        updated = _record_snapshot_entry(updated, snapshot, incoming)
    return updated


def _record_snapshot_entry(
    index: VersionIndex, snapshot: SnapshotRecord, incoming: VersionEntry
) -> VersionIndex:

    _require_unmoved_immutable_identity(index, incoming)
    same_sha = tuple(entry for entry in index.versions if entry.sha == snapshot.ref.sha)
    existing = _matching_identity_entry(same_sha, incoming)
    canonical = next((entry for entry in same_sha if entry.capture_kind == "canonical"), None)

    if snapshot.capture_kind == "supplement":
        if canonical is None:
            return index
        if existing is None:
            incoming = replace(
                incoming,
                snapshot_path=canonical.snapshot_path,
                collection_date=canonical.collection_date,
                capture_kind="canonical",
                changelog_paths=tuple(
                    sorted(set(canonical.changelog_paths).union(incoming.changelog_paths))
                ),
            )
            updated = _append_entry(index, incoming)
        else:
            updated = _replace_identity_entry(
                index, existing, _merge_snapshot_evidence(existing, snapshot, incoming)
            )
        return _record_branch_observation(updated, incoming)
    if snapshot.capture_kind != "canonical":
        raise PacketError("snapshot capture_kind must be canonical or supplement")

    if existing is not None:
        updated = _replace_identity_entry(
            index, existing, _merge_snapshot_evidence(existing, snapshot, incoming)
        )
        return _record_branch_observation(updated, incoming)

    if canonical is not None:
        incoming = replace(
            incoming,
            snapshot_path=canonical.snapshot_path,
            collection_date=canonical.collection_date,
            capture_kind="canonical",
            changelog_paths=tuple(
                sorted(set(canonical.changelog_paths).union(incoming.changelog_paths))
            ),
        )

    updated = _append_entry(index, incoming)
    if canonical is None:
        updated = replace(updated, capture_order=_capture_order(index) + (incoming.sha,))
    return _record_branch_observation(updated, incoming)


def select_prior(index: VersionIndex, ref: ResolvedRef) -> Optional[VersionEntry]:
    """Choose the latest compatible prior evidence entry for an exact resolved ref."""
    if index.repo_id != ref.repo_id:
        raise PacketError("resolved reference repository does not match version index")
    candidates = [entry for entry in index.versions if entry.sha != ref.sha]
    if ref.ref_kind == "branch":
        for observation in reversed(index.branch_observations):
            if observation.ref_name != ref.ref_name:
                continue
            return next(
                (
                    entry
                    for entry in index.versions
                    if entry.ref_kind == "branch"
                    and entry.ref_name == observation.ref_name
                    and entry.sha == observation.sha
                ),
                None,
            )
        return None

    packages = _selection_packages(ref)
    if packages:
        compatible = [
            entry
            for entry in candidates
            if packages.intersection(_entry_package_identities(entry))
        ]
        return _latest_version_before(compatible, ref.version)

    compatible = [entry for entry in candidates if entry.ref_kind == ref.ref_kind]
    prior = _latest_version_before(compatible, ref.version)
    if prior is not None:
        return prior
    aliases = set(ref.aliases)
    if aliases:
        return _latest_capture([entry for entry in compatible if aliases.intersection(entry.aliases)])
    return None


def build_baseline_packet(
    config: RepoConfig, current: object, packet_root: Path
) -> PacketRecord:
    """Generate an awaiting-review baseline packet for one immutable snapshot."""
    entry = _current_entry(config, current)
    _require_entry_evidence(config, entry, packet_root, allow_supplement=True)
    packet_id = "baseline-" + _packet_identity_part(entry) + "-" + entry.sha[:7]
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
    current: object,
    repo_root: Path,
    packet_root: Path,
) -> PacketRecord:
    """Generate an awaiting-review delta packet from a local Git checkout."""
    _require_entry_config(config, prior)
    current_entry = _current_entry(config, current)
    _require_entry_evidence(config, prior, packet_root)
    _require_entry_evidence(config, current_entry, packet_root, allow_supplement=True)
    current_paths = (
        _entry_file_paths(config, current_entry, packet_root)
        if isinstance(current, VersionEntry)
        else _snapshot_file_paths(current)
    )
    selected_paths = _selected_paths(
        config, _entry_file_paths(config, prior, packet_root), current_paths
    )
    changed_files, source_diff = _git_delta(repo_root, prior.sha, current_entry.sha, selected_paths)
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
    _require_entry_evidence(config, prior, packet_root)
    _require_entry_evidence(config, current, packet_root)
    selected_paths = _selected_paths(
        config,
        _entry_file_paths(config, prior, packet_root),
        _entry_file_paths(config, current, packet_root),
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
    if snapshot.release_evidence:
        return _entry_from_release_evidence(snapshot, snapshot.release_evidence[0])
    release_notes_path = snapshot.release_notes_path
    if not release_notes_path and snapshot.release_notes_source_url is not None:
        release_notes_path = "release-notes.md"
    return _entry_from_ref(snapshot, snapshot.ref, release_notes_path)


def _current_entry(config: RepoConfig, current: object) -> VersionEntry:
    if isinstance(current, VersionEntry):
        _require_entry_config(config, current)
        return current
    if isinstance(current, SnapshotRecord):
        _require_snapshot_config(config, current)
        return _entry_from_snapshot(current)
    raise PacketError("packet current endpoint has an invalid type")


def _entries_from_snapshot(snapshot: SnapshotRecord) -> Tuple[VersionEntry, ...]:
    if snapshot.release_evidence:
        return tuple(
            _entry_from_release_evidence(snapshot, item)
            for item in snapshot.release_evidence
        )
    return (_entry_from_snapshot(snapshot),)


def _entry_from_release_evidence(
    snapshot: SnapshotRecord, evidence: SnapshotReleaseEvidence
) -> VersionEntry:
    return _entry_from_ref(snapshot, evidence.ref, evidence.path)


def _entry_from_ref(
    snapshot: SnapshotRecord, ref: ResolvedRef, release_notes_relative_path: str
) -> VersionEntry:
    snapshot_path = _evidence_path(snapshot.target_path)
    changelogs = tuple(
        sorted(
            _evidence_path(snapshot.target_path / "files" / item.path)
            for item in snapshot.files
            if Path(item.path).name.lower().startswith("changelog")
        )
    )
    release_notes_path = ""
    if release_notes_relative_path:
        release_notes_path = _evidence_path(
            snapshot.target_path / release_notes_relative_path
        )
    return VersionEntry(
        ref_kind=ref.ref_kind,
        ref_name=ref.ref_name,
        version=ref.version,
        sha=ref.sha,
        aliases=tuple(sorted(set(ref.aliases))),
        snapshot_path=snapshot_path,
        collection_date=snapshot.collection_date,
        package=_package_for_ref(ref),
        capture_kind=snapshot.capture_kind,
        release_notes_path=release_notes_path,
        changelog_paths=changelogs,
    )


def _merge_snapshot_evidence(
    entry: VersionEntry,
    snapshot: SnapshotRecord,
    supplement: Optional[VersionEntry] = None,
) -> VersionEntry:
    supplement = supplement or _entry_from_snapshot(snapshot)
    aliases = set(entry.aliases).union(supplement.aliases)
    if supplement.ref_name != entry.ref_name:
        aliases.add(supplement.ref_name)
    return replace(
        entry,
        aliases=tuple(sorted(aliases)),
        release_notes_path=supplement.release_notes_path or entry.release_notes_path,
        changelog_paths=tuple(sorted(set(entry.changelog_paths).union(supplement.changelog_paths))),
    )


def _append_entry(index: VersionIndex, entry: VersionEntry) -> VersionIndex:
    return VersionIndex(
        index.repo_id,
        tuple(sorted(index.versions + (entry,), key=_entry_key)),
        _capture_order(index),
        index.branch_observations,
    )


def _replace_identity_entry(
    index: VersionIndex, existing: VersionEntry, updated: VersionEntry
) -> VersionIndex:
    return VersionIndex(
        index.repo_id,
        tuple(
            sorted(
                (updated if entry == existing else entry for entry in index.versions),
                key=_entry_key,
            )
        ),
        _capture_order(index),
        index.branch_observations,
    )


def _matching_identity_entry(
    entries: Sequence[VersionEntry], incoming: VersionEntry
) -> Optional[VersionEntry]:
    if incoming.ref_kind == "branch":
        return next(
            (
                entry
                for entry in entries
                if entry.ref_kind == "branch" and entry.ref_name == incoming.ref_name
            ),
            None,
        )
    if incoming.ref_kind in ("package-version", "tag"):
        identity = _semantic_release_identity(incoming)
        return next(
            (
                entry
                for entry in entries
                if entry.ref_kind in ("package-version", "tag")
                and _semantic_release_identity(entry) == identity
            ),
            None,
        )
    return next(
        (
            entry
            for entry in entries
            if entry.ref_kind == incoming.ref_kind
            and entry.ref_name == incoming.ref_name
        ),
        None,
    )


def _semantic_release_identity(entry: VersionEntry) -> Tuple[str, str]:
    return (entry.package, entry.version[1:] if entry.version.startswith("v") else entry.version)


def _immutable_names(entry: VersionEntry) -> set:
    if entry.ref_kind == "branch":
        return set()
    return {entry.ref_name}.union(entry.aliases)


def _require_unmoved_immutable_identity(
    index: VersionIndex, incoming: VersionEntry
) -> None:
    incoming_names = _immutable_names(incoming)
    if not incoming_names:
        return
    for existing in index.versions:
        if existing.sha == incoming.sha or existing.ref_kind == "branch":
            continue
        if (
            incoming.ref_kind in ("package-version", "tag")
            and existing.ref_kind in ("package-version", "tag")
            and _semantic_release_identity(existing)
            == _semantic_release_identity(incoming)
        ):
            raise PacketError(
                "immutable reference or release identity "
                + _packet_release_identity(incoming)
                + " is already owned by SHA "
                + existing.sha
            )
        conflict = sorted(incoming_names.intersection(_immutable_names(existing)))
        if conflict:
            raise PacketError(
                "immutable reference "
                + conflict[0]
                + " is already owned by SHA "
                + existing.sha
            )


def _record_branch_observation(
    index: VersionIndex, entry: VersionEntry
) -> VersionIndex:
    if entry.ref_kind != "branch":
        return index
    current = next(
        (
            item
            for item in reversed(index.branch_observations)
            if item.ref_name == entry.ref_name
        ),
        None,
    )
    if current is not None and current.sha == entry.sha:
        return index
    return replace(
        index,
        branch_observations=index.branch_observations
        + (BranchObservation(entry.ref_name, entry.sha),),
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


def _capture_order(index: VersionIndex) -> Tuple[str, ...]:
    if index.capture_order:
        return index.capture_order
    return _legacy_capture_order(index.versions)


def _package_for_ref(ref: ResolvedRef) -> str:
    direct = parse_package_tag(ref.ref_name)
    if direct is not None:
        return direct[0]
    packages = _package_identities(ref.ref_name, ref.aliases)
    return next(iter(packages)) if len(packages) == 1 else ""


def _selection_packages(ref: ResolvedRef) -> set:
    """Use a direct package ref, or one unambiguous package-tag alias, never both."""
    direct = parse_package_tag(ref.ref_name)
    if direct is not None:
        return {direct[0]}
    packages = _package_identities(ref.ref_name, ref.aliases)
    return packages if len(packages) == 1 else set()


def _entry_package_identities(entry: VersionEntry) -> set:
    identities = _package_identities(entry.ref_name, entry.aliases)
    if entry.package:
        identities.add(entry.package)
    return identities


def _package_identities(ref_name: str, aliases: Sequence[str]) -> set:
    return {
        parsed[0]
        for parsed in (parse_package_tag(value) for value in (ref_name,) + tuple(aliases))
        if parsed is not None
    }


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


def _entry_from_json(value: object, evidence_root: Path) -> VersionEntry:
    if type(value) is not dict or set(value) != _ENTRY_KEYS:
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
    if any(type(value[field]) is not str for field in fields):
        raise PacketError("version index entry has invalid scalar fields")
    aliases = value["aliases"]
    changelogs = value["changelog_paths"]
    if (
        type(aliases) is not list
        or type(changelogs) is not list
        or any(type(item) is not str for item in aliases + changelogs)
    ):
        raise PacketError("version index entry has invalid evidence paths")
    if aliases != sorted(set(aliases)) or changelogs != sorted(set(changelogs)):
        raise PacketError("version index entry has duplicate or unordered aliases or changelog paths")
    entry = VersionEntry(
        ref_kind=value["ref_kind"],
        ref_name=value["ref_name"],
        version=value["version"],
        sha=value["sha"],
        aliases=tuple(aliases),
        snapshot_path=value["snapshot_path"],
        collection_date=value["collection_date"],
        package=value["package"],
        capture_kind=value["capture_kind"],
        release_notes_path=value["release_notes_path"],
        changelog_paths=tuple(changelogs),
    )
    _validate_entry(entry, evidence_root)
    return entry


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


def _entry_file_paths(
    config: RepoConfig, entry: VersionEntry, packet_root: Path
) -> Tuple[str, ...]:
    manifest = _absolute_evidence_path(
        entry.snapshot_path + "/snapshot.md", packet_root, config
    )
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
    packet_root = _require_packet_root(packet_root, config.id)
    packet_root.mkdir(parents=True, exist_ok=True)
    packet_root = _require_packet_root(packet_root, config.id)
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
    contents = {
        "packet.json": json.dumps(packet_data, indent=2, sort_keys=True) + "\n",
        "ingest-packet.md": _render_packet_markdown(record, prior, current),
        "changed-files.txt": "\n".join(record.changed_files) + "\n",
        "source-diff.patch": source_diff if source_diff.endswith("\n") else source_diff + "\n",
        "state-events.jsonl": json.dumps(
            {"packet_id": record.packet_id, "state": record.initial_state},
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n",
    }
    lock_descriptor = _open_packet_lock(packet_root)
    try:
        try:
            fcntl.flock(lock_descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            raise PacketError("packet publication lock is already held") from error
        if _path_exists_or_is_symlink(directory):
            _validate_existing_packet(directory, packet_data, contents, record)
            return record
        temporary = Path(tempfile.mkdtemp(prefix=".packet-", dir=str(packet_root)))
        try:
            for name in sorted(contents):
                _write_text_atomic(temporary / name, contents[name])
            try:
                os.rename(str(temporary), str(directory))
            except FileExistsError as error:
                raise PacketError("packet directory already exists: " + str(directory)) from error
        except Exception:
            shutil.rmtree(temporary, ignore_errors=True)
            raise
    finally:
        os.close(lock_descriptor)
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
        + _packet_identity_part(prior)
        + "-"
        + prior.sha[:7]
        + "-to-"
        + _packet_identity_part(current)
        + "-"
        + current.sha[:7]
    )


def _packet_release_identity(entry: VersionEntry) -> str:
    return (entry.package + "@" if entry.package else "") + entry.version


def _packet_identity_part(entry: VersionEntry) -> str:
    if entry.ref_kind in ("package-version", "tag"):
        identity = ("release",) + _semantic_release_identity(entry)
        label = _packet_release_identity(entry)
    elif entry.ref_kind == "branch":
        identity = ("branch", entry.ref_name)
        label = entry.ref_name
    else:
        identity = (entry.ref_kind, entry.ref_name)
        label = entry.version
    digest = hashlib.sha256(
        json.dumps(identity, ensure_ascii=True, separators=(",", ":")).encode("ascii")
    ).hexdigest()
    return _safe_part(label)[:80].rstrip("-.") + "-" + digest


def _safe_part(value: str) -> str:
    return _SAFE_PART.sub("-", value).strip("-.") or "ref"


def _evidence_path(path: Path) -> str:
    parts = path.as_posix().split("/")
    for index in range(len(parts) - 1):
        if parts[index] == "raw" and parts[index + 1] == "github":
            return "/".join(parts[index:])
    return path.as_posix()


def _absolute_evidence_path(path: str, packet_root: Path, config: RepoConfig) -> Path:
    evidence_root = _evidence_root_from_packet_root(packet_root, config)
    return _safe_evidence_path(path, evidence_root)


def _validate_entry(
    entry: VersionEntry, evidence_root: Path, allow_supplement: bool = False
) -> None:
    if entry.ref_kind not in _REF_KINDS:
        raise PacketError("version index entry has an invalid reference kind")
    if _SHA.fullmatch(entry.sha) is None:
        raise PacketError("version index entry has an invalid SHA")
    if not _valid_ref_name(entry.ref_name):
        raise PacketError("version index entry has an invalid reference name")
    if not _valid_date(entry.collection_date):
        raise PacketError("version index entry has an invalid collection date")
    allowed_capture_kinds = {"canonical", "supplement"} if allow_supplement else {"canonical"}
    if entry.capture_kind not in allowed_capture_kinds:
        raise PacketError("version index entry must retain a canonical snapshot")
    package_from_ref = parse_package_tag(entry.ref_name)
    if entry.ref_kind == "package-version":
        if package_from_ref is None or not _is_exact_semver(package_from_ref[1]):
            raise PacketError("version index entry has an invalid package reference")
        if entry.version != package_from_ref[1]:
            raise PacketError("version index entry package version does not match its reference")
    elif entry.ref_kind == "tag":
        expected_version = entry.ref_name[1:] if entry.ref_name.startswith("v") else entry.ref_name
        if not _is_exact_semver(expected_version) or entry.version != expected_version:
            raise PacketError("version index entry tag version does not match its reference")
    elif entry.ref_kind == "branch":
        if entry.version != entry.ref_name:
            raise PacketError("version index entry branch version does not match its reference")
    elif entry.ref_name != entry.sha or entry.version != entry.sha:
        raise PacketError("version index entry commit does not match its SHA")

    identities = _package_identities(entry.ref_name, entry.aliases)
    if entry.package and (
        parse_package_tag(entry.package + "@1.0.0") is None or entry.package not in identities
    ):
        raise PacketError("version index entry package does not match its reference identities")
    for alias in entry.aliases:
        if not _valid_ref_name(alias):
            raise PacketError("version index entry has an invalid alias")
    snapshot_path = _safe_evidence_path(entry.snapshot_path, evidence_root)
    release_notes = (
        _safe_evidence_path(entry.release_notes_path, evidence_root)
        if entry.release_notes_path
        else None
    )
    changelogs = tuple(_safe_evidence_path(item, evidence_root) for item in entry.changelog_paths)
    expected_snapshot_root = evidence_root / "snapshots"
    _require_contained(snapshot_path, expected_snapshot_root, "snapshot path")
    if release_notes is not None:
        _require_contained(release_notes, expected_snapshot_root, "release notes path")
        relative = release_notes.relative_to(expected_snapshot_root)
        if (
            len(relative.parts) < 2
            or relative.name != "release-notes.md"
            and not (
                len(relative.parts) >= 3
                and relative.parts[1] == "release-notes"
                and relative.suffix == ".md"
            )
        ):
            raise PacketError("version index entry release notes path is invalid")
    for changelog in changelogs:
        _require_contained(changelog, expected_snapshot_root, "changelog path")
        relative = changelog.relative_to(expected_snapshot_root)
        if len(relative.parts) < 3 or relative.parts[1] != "files":
            raise PacketError("version index entry changelog path is invalid")


def _valid_ref_name(value: str) -> bool:
    if (
        not value
        or value == "@"
        or value != value.strip()
        or value.startswith((".", "/"))
        or value.endswith((".", "/", ".lock"))
        or "//" in value
    ):
        return False
    if any(part.startswith(".") or part.endswith(".lock") for part in value.split("/")):
        return False
    return not any(
        character in value for character in (" ", "\t", "\r", "\n", "\x00", "..", "@{", "\\", "~", "^", ":", "?", "*", "[")
    )


def _is_exact_semver(value: str) -> bool:
    parsed = parse_semver(value)
    return parsed is not None and parsed.is_exact


def _valid_date(value: str) -> bool:
    if _DATE.fullmatch(value) is None:
        return False
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        return False
    return True


def _evidence_root_from_index(index_path: Path, config: RepoConfig) -> Path:
    repository_root = _repository_root_from_tracking_path(
        index_path, "version-index.json", config.id
    )
    return repository_root / "raw" / "github" / _raw_repository_namespace(config)


def _evidence_root_from_packet_root(packet_root: Path, config: RepoConfig) -> Path:
    repository_root = _repository_root_from_tracking_path(packet_root, None, config.id)
    return repository_root / "raw" / "github" / _raw_repository_namespace(config)


def _raw_repository_namespace(config: RepoConfig) -> Path:
    repo_id = Path(config.id)
    company = Path(config.company)
    if (
        repo_id.is_absolute()
        or repo_id.as_posix() != config.id
        or len(repo_id.parts) != 2
        or any(part in ("", ".", "..") for part in repo_id.parts)
        or company.is_absolute()
        or company.as_posix() != config.company
        or len(company.parts) != 1
        or company.parts[0] in ("", ".", "..")
    ):
        raise PacketError("repository evidence namespace is invalid")
    return company / repo_id.parts[1]


def _repository_root_from_tracking_path(
    path: Path, required_name: Optional[str], repo_id: str
) -> Path:
    owner_repo = Path(repo_id)
    if len(owner_repo.parts) != 2 or any(not part for part in owner_repo.parts):
        raise PacketError("repository ID is invalid")
    lexical = path.absolute()
    if ".." in lexical.parts:
        raise PacketError("tracking path contains parent traversal")
    if required_name is not None and lexical.name != required_name:
        raise PacketError("version index path has an invalid filename")
    tracking_roots = tuple(
        ancestor
        for ancestor in (lexical,) + tuple(lexical.parents)
        if ancestor.name == "github"
        and ancestor.parent.name == "tracking"
        and ancestor == ancestor.parent.parent / "tracking" / "github"
    )
    if len(tracking_roots) != 1:
        raise PacketError("path must identify one tracking/github workspace")
    ancestor = tracking_roots[0]
    repository_root = ancestor.parent.parent
    expected_namespace = ancestor / "repos" / owner_repo
    if required_name is not None:
        if lexical != expected_namespace / required_name:
            raise PacketError("version index is outside its repository tracking namespace")
    else:
        try:
            relative = lexical.relative_to(expected_namespace)
        except ValueError as error:
            raise PacketError("packet root is outside its repository tracking namespace") from error
        if _repeats_repository_namespace(relative, owner_repo):
            raise PacketError("packet root repeats its repository tracking namespace")
    _require_no_symlink_components(repository_root, lexical)
    try:
        lexical.resolve().relative_to(ancestor.resolve())
    except ValueError as error:
        raise PacketError("tracking path escapes through a symlink") from error
    return repository_root


def _repeats_repository_namespace(relative: Path, owner_repo: Path) -> bool:
    parts = relative.parts
    markers = (owner_repo.parts, ("repos",) + owner_repo.parts)
    return any(
        tuple(parts[index : index + len(marker)]) == marker
        for marker in markers
        for index in range(len(parts) - len(marker) + 1)
    )


def _safe_evidence_path(path: str, evidence_root: Path) -> Path:
    candidate = Path(path)
    if not path or candidate.is_absolute() or ".." in candidate.parts or candidate.as_posix() != path:
        raise PacketError("evidence path is not a safe relative path")
    absolute = evidence_root.parents[3] / candidate
    _require_contained(absolute, evidence_root, "evidence path")
    return absolute


def _require_contained(candidate: Path, root: Path, label: str) -> None:
    try:
        candidate.relative_to(root)
        candidate.resolve().relative_to(root.resolve())
    except ValueError as error:
        raise PacketError(label + " escapes its evidence root") from error


def _require_no_symlink_components(root: Path, candidate: Path) -> None:
    try:
        relative = candidate.relative_to(root)
    except ValueError as error:
        raise PacketError("tracking path is outside its repository root") from error
    current = root
    if current.is_symlink():
        raise PacketError("repository root must not be a symlink")
    for part in relative.parts:
        current = current / part
        if current.is_symlink():
            raise PacketError("tracking path must not traverse a symlink")


def _require_packet_root(packet_root: Path, repo_id: str) -> Path:
    _repository_root_from_tracking_path(packet_root, None, repo_id)
    return packet_root.absolute()


def _require_exact_packet_root(packet_root: Path, config: RepoConfig) -> Path:
    repository_root = _repository_root_from_tracking_path(packet_root, None, config.id)
    expected = (
        repository_root / "tracking" / "github" / "repos" / Path(config.id) / "packets"
    )
    lexical = packet_root.absolute()
    if lexical != expected:
        raise PacketError("packet transaction requires the exact packets namespace")
    if not lexical.is_dir() or lexical.is_symlink():
        raise PacketError("packet root is not a regular directory")
    return lexical


def _require_entry_evidence(
    config: RepoConfig,
    entry: VersionEntry,
    packet_root: Path,
    allow_supplement: bool = False,
) -> None:
    evidence_root = _evidence_root_from_packet_root(packet_root, config)
    _validate_entry(entry, evidence_root, allow_supplement=allow_supplement)


@contextmanager
def packet_transaction(config: RepoConfig, packet_root: Path) -> Iterator[int]:
    """Lock and open the exact packet namespace without following symlinks."""
    packet_root = _require_exact_packet_root(packet_root, config)
    root_descriptor: Optional[int] = None
    lock_descriptor: Optional[int] = None
    try:
        root_descriptor = os.open(
            str(packet_root), os.O_RDONLY | _directory_flag() | _no_follow_flag()
        )
        lock_descriptor = _open_packet_lock_at(root_descriptor)
        fcntl.flock(lock_descriptor, fcntl.LOCK_EX)
        yield root_descriptor
    finally:
        if lock_descriptor is not None:
            os.close(lock_descriptor)
        if root_descriptor is not None:
            os.close(root_descriptor)


def _open_packet_lock(packet_root: Path) -> int:
    flags = os.O_CREAT | os.O_RDWR
    no_follow = getattr(os, "O_NOFOLLOW", None)
    if no_follow is None:
        raise PacketError("no-follow lock opening is unavailable")
    try:
        descriptor = os.open(str(packet_root / _PACKET_LOCK), flags | no_follow, 0o600)
    except OSError as error:
        raise PacketError("could not open packet publication lock") from error
    if not stat.S_ISREG(os.fstat(descriptor).st_mode):
        os.close(descriptor)
        raise PacketError("packet publication lock is not a regular file")
    return descriptor


def _open_packet_lock_at(packet_root_descriptor: int) -> int:
    flags = os.O_CREAT | os.O_RDWR | _no_follow_flag()
    try:
        descriptor = os.open(
            _PACKET_LOCK, flags, 0o600, dir_fd=packet_root_descriptor
        )
    except OSError as error:
        raise PacketError("could not open packet publication lock") from error
    if not stat.S_ISREG(os.fstat(descriptor).st_mode):
        os.close(descriptor)
        raise PacketError("packet publication lock is not a regular file")
    return descriptor


def _directory_flag() -> int:
    flag = getattr(os, "O_DIRECTORY", None)
    if flag is None:
        raise PacketError("directory-only opening is unavailable")
    return flag


def _no_follow_flag() -> int:
    flag = getattr(os, "O_NOFOLLOW", None)
    if flag is None:
        raise PacketError("no-follow opening is unavailable")
    return flag


def _validate_existing_packet(
    directory: Path, packet_data: dict, contents: Dict[str, str], record: PacketRecord
) -> None:
    if not directory.is_dir() or directory.is_symlink():
        raise PacketError("existing packet is not a regular directory")
    if {item.name for item in directory.iterdir()} != _PACKET_FILES:
        raise PacketError("existing packet has an invalid file set")
    for name in _PACKET_FILES:
        path = directory / name
        if not path.is_file() or path.is_symlink():
            raise PacketError("existing packet has an invalid file: " + name)
    try:
        existing_data = _load_json((directory / "packet.json").read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, ValueError, json.JSONDecodeError) as error:
        raise PacketError("existing packet JSON is invalid") from error
    if existing_data != packet_data:
        raise PacketError("existing packet conflicts with deterministic packet content")
    for name in ("ingest-packet.md", "changed-files.txt", "source-diff.patch"):
        if (directory / name).read_text(encoding="utf-8") != contents[name]:
            raise PacketError("existing packet conflicts with deterministic packet content")
    _validate_state_events(directory / "state-events.jsonl", record, contents["state-events.jsonl"])


def _validate_state_events(path: Path, record: PacketRecord, initial: str) -> None:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError) as error:
        raise PacketError("existing packet state events are invalid") from error
    if not lines or lines[0] != initial.rstrip("\n"):
        raise PacketError("existing packet initial state event conflicts")
    for line in lines:
        try:
            event = _load_json(line)
        except (ValueError, json.JSONDecodeError) as error:
            raise PacketError("existing packet state event is invalid") from error
        if (
            type(event) is not dict
            or type(event.get("packet_id")) is not str
            or type(event.get("state")) is not str
            or event["packet_id"] != record.packet_id
            or not event["state"]
        ):
            raise PacketError("existing packet state event is invalid")


def _load_json(text: str) -> object:
    def reject_duplicates(pairs: Sequence[Tuple[str, object]]) -> dict:
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate JSON key " + key)
            result[key] = value
        return result

    return json.loads(text, object_pairs_hook=reject_duplicates)


def _path_exists_or_is_symlink(path: Path) -> bool:
    return path.exists() or path.is_symlink()


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
