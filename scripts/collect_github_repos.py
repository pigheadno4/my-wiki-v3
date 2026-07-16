"""Public CLI and orchestration for registry-driven GitHub collection."""

import argparse
from dataclasses import dataclass, replace
from datetime import date, datetime, timezone
import json
import os
from pathlib import Path
import re
import shutil
import stat
import sys
import tempfile
from typing import Dict, List, Mapping, Optional, Sequence, Tuple
import uuid

from github_git import (
    ResolvedRef,
    clone_repository,
    fetch_required_refs,
    inspect_repository,
    resolve_ref,
    run_git,
)
from github_packets import (
    PacketRecord,
    VersionEntry,
    VersionIndex,
    build_baseline_packet,
    build_comparison_packet,
    build_delta_packet,
    load_version_index,
    packet_transaction,
    record_snapshot,
    save_version_index,
    select_prior,
)
from github_registry import RepoConfig, VersionTrack, load_registry, select_repos
from github_releases import (
    ReleaseCandidate,
    discover_release_candidates,
    fetch_release_notes,
    select_release_candidates,
)
from github_reporting import (
    COLLECTION_TERMINAL,
    CollectionReconciliationError,
    StateTransitionError,
    append_event,
    render_collection_status,
    render_ingest_status,
    transition_packet,
    validate_collection_run,
    validate_packet_history,
)
from github_snapshot import SnapshotFile, SnapshotRecord, build_snapshot, promote_snapshot
from github_versions import matches_semver, parse_package_tag, parse_semver


PROJECT_ROOT = Path(__file__).resolve().parents[1]
_SAFE_PACKET_ID = re.compile(r"^[A-Za-z0-9._-]+$")
_FULL_SHA = re.compile(r"^(?:[0-9A-Fa-f]{40}|[0-9A-Fa-f]{64})$")


class CollectionUsageError(ValueError):
    """The CLI or direct orchestration request is not well formed."""


class CollectionCommandError(RuntimeError):
    """A collection operation reached a reconciled terminal failure."""


@dataclass(frozen=True)
class CollectionResult:
    repo_id: str
    state: str
    versions: Tuple[str, ...]
    packet_ids: Tuple[str, ...]
    events: Tuple[Mapping[str, object], ...]


def collect_one(
    root: Path,
    config: RepoConfig,
    selectors: Sequence[str] = (),
    release_mode: Optional[str] = None,
    dry_run: bool = False,
) -> CollectionResult:
    """Collect explicit refs or retained releases for one repository."""
    if release_mode not in (None, "backfill", "future"):
        raise CollectionUsageError("release mode must be backfill or future")
    if selectors and release_mode is not None:
        raise CollectionUsageError("explicit refs and release mode are mutually exclusive")
    if release_mode is not None and not config.version_tracks:
        raise CollectionUsageError("release mode requires configured version tracks for " + config.id)

    root = root.resolve()
    event_path = None if dry_run else _new_run_event_path(root, config.id)
    events: List[Mapping[str, object]] = []
    packet_ids: List[str] = []
    versions: List[str] = []
    index_path = _version_index_path(root, config)
    explicit = tuple(_deduplicated(_normalize_selector(item) for item in selectors))
    if not explicit and release_mode is None:
        explicit = tuple(_deduplicated(config.requested_refs or ("default-branch",)))

    def emit(event: Mapping[str, object]) -> None:
        frozen = dict(event)
        events.append(frozen)
        if event_path is not None:
            append_event(event_path, frozen)

    selected_targets: List[str] = []
    if explicit:
        for selector in explicit:
            selected_targets.append(selector)
            emit(_selected_event(config.id, selector, dry_run))

    try:
        index = load_version_index(index_path, config)
        with tempfile.TemporaryDirectory(prefix="wiki-github-") as temporary:
            clone_path = Path(temporary) / "repository"
            clone_repository(config, clone_path)

            release_pairs: List[Tuple[ReleaseCandidate, str]] = []
            if release_mode is not None:
                release_pairs, discovery_failures = _select_releases(
                    config, clone_path, index, release_mode
                )
                for selector, error in discovery_failures:
                    selected_targets.append(selector)
                    emit(_selected_event(config.id, selector, dry_run))
                    emit(_terminal_event(config.id, selector, "failed", error=error, dry_run=dry_run))
                for candidate, selector in release_pairs:
                    selected_targets.append(selector)
                    versions.append(candidate.version)
                    emit(_selected_event(config.id, selector, dry_run))

            requested = explicit or tuple(selector for _, selector in release_pairs)
            if requested:
                fetch_required_refs(config, clone_path, requested)
            inspection = inspect_repository(config, clone_path)

            if explicit:
                work = [(None, selector) for selector in explicit]
            else:
                by_selector = {selector: candidate for candidate, selector in release_pairs}
                work = [(by_selector[selector], selector) for selector in requested]

            for candidate, selector in work:
                try:
                    ref = resolve_ref(config, inspection, selector)
                    evidence = None
                    if candidate is not None and not dry_run:
                        evidence = fetch_release_notes(
                            config, candidate, token=os.environ.get("GITHUB_TOKEN")
                        )
                        if evidence is not None:
                            ref = replace(ref, release_published_at=evidence.published_at)
                    if candidate is None:
                        versions.append(ref.version)
                    state, packet, index = _collect_resolved_ref(
                        root,
                        config,
                        clone_path,
                        ref,
                        selector,
                        index,
                        index_path,
                        evidence,
                        candidate is not None,
                        dry_run,
                    )
                    if packet is not None:
                        packet_ids.append(packet.packet_id)
                    emit(
                        _terminal_event(
                            config.id,
                            selector,
                            state,
                            ref=ref,
                            packet_id=packet.packet_id if packet is not None else "",
                            dry_run=dry_run,
                        )
                    )
                except Exception as error:  # one terminal event per selected ref is mandatory
                    emit(
                        _terminal_event(
                            config.id,
                            selector,
                            "failed",
                            error=_bounded_error(error),
                            dry_run=dry_run,
                        )
                    )
    except Exception as error:
        unresolved = [
            selector
            for selector in selected_targets
            if not _has_terminal(events, config.id, selector)
        ]
        if release_mode is not None and not unresolved and not selected_targets:
            unresolved = [track.selector for track in config.version_tracks]
            for selector in unresolved:
                emit(_selected_event(config.id, selector, dry_run))
                selected_targets.append(selector)
        for selector in unresolved:
            emit(
                _terminal_event(
                    config.id,
                    selector,
                    "failed",
                    error=_bounded_error(error),
                    dry_run=dry_run,
                )
            )

    try:
        validate_collection_run(events)
    except CollectionReconciliationError:
        state = "failed"
    else:
        state = _aggregate_state(events)
    return CollectionResult(
        config.id,
        state,
        tuple(versions),
        tuple(packet_ids),
        tuple(events),
    )


def compare_one(
    root: Path,
    config: RepoConfig,
    from_selector: str,
    to_selector: str,
) -> PacketRecord:
    """Collect missing comparison endpoints and create one directional packet."""
    normalized = (_normalize_selector(from_selector), _normalize_selector(to_selector))
    collection = collect_one(root, config, normalized)
    if collection.state in ("failed", "retry-pending"):
        raise CollectionCommandError("could not collect comparison endpoints for " + config.id)

    index = load_version_index(_version_index_path(root, config), config)
    with tempfile.TemporaryDirectory(prefix="wiki-github-") as temporary:
        clone_path = Path(temporary) / "repository"
        clone_repository(config, clone_path)
        fetch_required_refs(config, clone_path, normalized)
        inspection = inspect_repository(config, clone_path)
        from_ref = resolve_ref(config, inspection, normalized[0])
        to_ref = resolve_ref(config, inspection, normalized[1])
        prior = _entry_for_sha(index, from_ref.sha)
        current = _entry_for_sha(index, to_ref.sha)
        if prior is None or current is None:
            raise CollectionCommandError("comparison endpoints are absent from the version index")
        return build_comparison_packet(
            config, prior, current, clone_path, _packet_root(root, config)
        )


def prepare_one(root: Path, config: RepoConfig, selector: str) -> PacketRecord:
    """Regenerate one packet from an existing indexed snapshot without collection."""
    normalized = _normalize_selector(selector)
    index = load_version_index(_version_index_path(root, config), config)
    with tempfile.TemporaryDirectory(prefix="wiki-github-") as temporary:
        clone_path = Path(temporary) / "repository"
        clone_repository(config, clone_path)
        fetch_required_refs(config, clone_path, (normalized,))
        inspection = inspect_repository(config, clone_path)
        ref = resolve_ref(config, inspection, normalized)
        entry = _entry_for_sha(index, ref.sha)
        if entry is None:
            raise CollectionUsageError("requested ref is not present in the version index")
        current = _snapshot_from_entry(root, config, entry)
        prior = select_prior(index, current.ref)
        if prior is None:
            return build_baseline_packet(config, current, _packet_root(root, config))
        fetch_required_refs(config, clone_path, ("commit:" + prior.sha,))
        return build_delta_packet(
            config, prior, current, clone_path, _packet_root(root, config)
        )


def regenerate_status(
    root: Path, repos: Optional[Sequence[RepoConfig]] = None
) -> Mapping[str, object]:
    """Regenerate JSON and Markdown projections from machine-readable contracts."""
    root = root.resolve()
    registry = tuple(repos) if repos is not None else load_registry(_registry_path(root))
    events = _load_collection_events(root)
    packets, states = _load_packet_contracts(root, registry)
    repository_rows = []
    latest_events: Dict[str, Mapping[str, object]] = {}
    for event in events:
        repo_id = event.get("repo_id")
        if isinstance(repo_id, str) and event.get("state") in COLLECTION_TERMINAL:
            latest_events[repo_id] = event
    for config in registry:
        index = load_version_index(_version_index_path(root, config), config)
        repository_rows.append(
            {
                "company": config.company,
                "enabled": config.enabled,
                "latest_event": dict(latest_events.get(config.id, {})),
                "priority": config.priority,
                "repo_id": config.id,
                "track": config.track,
                "versions": [entry.version for entry in index.versions],
            }
        )
    packet_rows = [
        {
            "packet_id": packet.packet_id,
            "packet_type": packet.packet_type,
            "repo_id": packet.repo_id,
            "state": states.get(packet.packet_id, packet.initial_state),
        }
        for packet in sorted(packets, key=lambda item: (item.repo_id, item.packet_id))
    ]
    status = {"packets": packet_rows, "repositories": repository_rows}
    tracking = root / "tracking" / "github"
    _write_text_atomic(
        tracking / "status.json", json.dumps(status, indent=2, sort_keys=True) + "\n"
    )
    _write_text_atomic(
        tracking / "collection-status.md", render_collection_status(registry, events)
    )
    _write_text_atomic(
        tracking / "ingest-status.md", render_ingest_status(packets, states)
    )
    return status


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Run the public CLI and return the documented process status code."""
    parser = _parser()
    try:
        arguments = parser.parse_args(list(argv) if argv is not None else None)
    except SystemExit as error:
        return int(error.code)

    root = PROJECT_ROOT.resolve()
    try:
        repos = load_registry(_registry_path(root))
    except ValueError as error:
        print("error: " + str(error), file=sys.stderr)
        return 2

    try:
        if arguments.command == "collect":
            selected = _select_cli_repos(repos, arguments)
            combined_events: List[Mapping[str, object]] = []
            results = []
            for config in selected:
                result = collect_one(
                    root,
                    config,
                    tuple(arguments.refs or ()),
                    arguments.release_mode,
                    arguments.dry_run,
                )
                results.append(result)
                combined_events.extend(result.events)
                print(_render_result(result, arguments.dry_run))
            try:
                validate_collection_run(combined_events)
            except CollectionReconciliationError:
                return 1
            if not arguments.dry_run:
                regenerate_status(root, repos)
            if any(result.state in ("failed", "retry-pending") for result in results):
                return 1
            return 0

        config = None
        if hasattr(arguments, "repo") and arguments.repo is not None:
            config = _explicit_repo(repos, arguments.repo)
        if arguments.command == "compare":
            packet = compare_one(root, config, arguments.from_selector, arguments.to_selector)
            regenerate_status(root, repos)
            print(packet.packet_id)
            return 0
        if arguments.command == "prepare":
            packet = prepare_one(root, config, arguments.ref)
            regenerate_status(root, repos)
            print(packet.packet_id)
            return 0
        if arguments.command == "packet-state":
            _change_packet_state(
                root,
                config,
                arguments.packet,
                arguments.from_state,
                arguments.to_state,
            )
            regenerate_status(root, repos)
            return 0
        if arguments.command == "status":
            regenerate_status(root, repos)
            return 0
        raise CollectionUsageError("unknown command")
    except (CollectionUsageError, StateTransitionError) as error:
        print("error: " + str(error), file=sys.stderr)
        return 2
    except Exception as error:
        print("error: " + str(error), file=sys.stderr)
        return 1


def _collect_resolved_ref(
    root: Path,
    config: RepoConfig,
    clone_path: Path,
    ref: ResolvedRef,
    selector: str,
    index: VersionIndex,
    index_path: Path,
    release_notes: object,
    release_target: bool,
    dry_run: bool,
) -> Tuple[str, Optional[PacketRecord], VersionIndex]:
    existing = _entry_for_sha(index, ref.sha)
    prior = select_prior(index, ref)
    if dry_run:
        if existing is not None:
            return "unchanged", None, index
        return ("collected-change" if prior is not None else "collected-baseline"), None, index
    if existing is not None:
        release_name = selector[4:] if selector.startswith("tag:") else ""
        known_refs = {existing.ref_name}.union(existing.aliases)
        if release_target and release_name and release_name not in known_refs:
            return _collect_release_alias(
                root,
                config,
                clone_path,
                ref,
                index,
                index_path,
                existing,
                prior,
                release_notes,
            )
        merged = record_snapshot(index, _alias_snapshot(root, config, existing, ref))
        if merged != index:
            save_version_index(index_path, merged)
        return "unchanged", None, merged

    run_git(["checkout", "--detach", ref.sha], clone_path)
    changed_paths: Tuple[str, ...] = ()
    if prior is not None:
        fetch_required_refs(config, clone_path, ("commit:" + prior.sha,))
        changed_paths = tuple(
            line for line in run_git(["diff", "--name-only", prior.sha, ref.sha], clone_path).splitlines() if line
        )
    raw_root = root / "raw" / "github"
    staging_root = raw_root / ".staging"
    record = None
    packet = None
    promoted_new = False
    index_existed = index_path.exists()
    index_saved = False
    try:
        record = build_snapshot(
            config,
            ref,
            clone_path,
            raw_root,
            staging_root,
            date.today().isoformat(),
            prior_snapshot=prior.snapshot_path if prior is not None else None,
            release_notes=release_notes,
            changed_paths=changed_paths,
        )
        target_existed = record.target_path.exists()
        promoted = promote_snapshot(record)
        promoted_new = promoted == record.target_path and not target_existed
        record = replace(record, target_path=promoted)
        updated = record_snapshot(index, record)
        save_version_index(index_path, updated)
        index_saved = True
        packet_root = _packet_root(root, config)
        if prior is None:
            packet = build_baseline_packet(config, record, packet_root)
            state = "collected-baseline"
        else:
            packet = build_delta_packet(config, prior, record, clone_path, packet_root)
            state = "collected-change"
        return state, packet, updated
    except Exception:
        if index_saved:
            try:
                if index_existed:
                    save_version_index(index_path, index)
                else:
                    index_path.unlink()
            except Exception:
                pass
        if promoted_new and record is not None and record.target_path.is_dir():
            shutil.rmtree(record.target_path, ignore_errors=True)
        raise
    finally:
        if record is not None and record.staging_path.exists() and not record.staging_path.is_symlink():
            shutil.rmtree(record.staging_path, ignore_errors=True)


def _select_releases(
    config: RepoConfig,
    clone_path: Path,
    index: VersionIndex,
    mode: str,
) -> Tuple[List[Tuple[ReleaseCandidate, str]], List[Tuple[str, str]]]:
    selected: List[Tuple[ReleaseCandidate, str]] = []
    failures: List[Tuple[str, str]] = []
    seen = set()
    for track in config.version_tracks:
        try:
            candidates = discover_release_candidates(config, clone_path, track)
            retained = select_release_candidates(
                track,
                candidates,
                _existing_versions_for_track(index, track),
                mode,
            )
        except Exception as error:
            failures.append((track.selector, _bounded_error(error)))
            continue
        for candidate in retained:
            selector = "tag:" + candidate.tag
            identity = (candidate.package, candidate.version, candidate.commit_sha)
            if identity in seen:
                continue
            seen.add(identity)
            selected.append((candidate, selector))
    return selected, failures


def _existing_versions_for_track(
    index: VersionIndex, track: VersionTrack
) -> Tuple[str, ...]:
    if track.selector.startswith("package:"):
        package_tag = parse_package_tag(track.selector[8:])
        if package_tag is None:
            return ()
        package_name, selector_version = package_tag
    else:
        package_name = ""
        selector_version = track.selector
    target = parse_semver(selector_version)
    if target is None:
        return ()
    versions = []
    for entry in index.versions:
        references = (entry.ref_name,) + entry.aliases
        if package_name:
            candidates = [
                parsed[1]
                for parsed in (parse_package_tag(reference) for reference in references)
                if parsed is not None and parsed[0] == package_name
            ]
            if entry.package == package_name:
                candidates.append(entry.version)
        else:
            candidates = [
                reference
                for reference in references
                if parse_package_tag(reference) is None
            ]
        for candidate in candidates:
            parsed = parse_semver(candidate)
            if parsed is not None and matches_semver(
                parsed, target, track.include_prerelease
            ):
                normalized = candidate[1:] if candidate.startswith("v") else candidate
                versions.append(normalized)
    return tuple(_deduplicated(versions))


def _collect_release_alias(
    root: Path,
    config: RepoConfig,
    clone_path: Path,
    ref: ResolvedRef,
    index: VersionIndex,
    index_path: Path,
    existing: VersionEntry,
    prior: Optional[VersionEntry],
    release_notes: object,
) -> Tuple[str, Optional[PacketRecord], VersionIndex]:
    record = None
    promoted_new = False
    index_existed = index_path.exists()
    index_saved = False
    try:
        run_git(["checkout", "--detach", ref.sha], clone_path)
        if release_notes is not None:
            raw_root = root / "raw" / "github"
            record = build_snapshot(
                config,
                ref,
                clone_path,
                raw_root,
                raw_root / ".staging",
                date.today().isoformat(),
                prior_snapshot=existing.snapshot_path,
                capture_kind="supplement",
                release_notes=release_notes,
            )
            promoted = promote_snapshot(record)
            promoted_new = True
            record = replace(record, target_path=promoted)
        else:
            record = _alias_snapshot(root, config, existing, ref)

        updated = record_snapshot(index, record)
        save_version_index(index_path, updated)
        index_saved = True
        packet_root = _packet_root(root, config)
        if prior is None:
            packet = build_baseline_packet(config, record, packet_root)
            state = "collected-baseline"
        else:
            fetch_required_refs(config, clone_path, ("commit:" + prior.sha,))
            packet = build_delta_packet(config, prior, record, clone_path, packet_root)
            state = "collected-change"
        return state, packet, updated
    except Exception:
        if index_saved:
            try:
                if index_existed:
                    save_version_index(index_path, index)
                else:
                    index_path.unlink()
            except Exception:
                pass
        if promoted_new and record is not None and record.target_path.is_dir():
            shutil.rmtree(record.target_path, ignore_errors=True)
        raise
    finally:
        if record is not None and record.staging_path.exists() and not record.staging_path.is_symlink():
            shutil.rmtree(record.staging_path, ignore_errors=True)


def _selected_event(repo_id: str, selector: str, dry_run: bool) -> Mapping[str, object]:
    return {
        "dry_run": dry_run,
        "repo_id": repo_id,
        "selected": True,
        "selector": selector,
        "state": "selected",
    }


def _terminal_event(
    repo_id: str,
    selector: str,
    state: str,
    error: str = "",
    ref: Optional[ResolvedRef] = None,
    packet_id: str = "",
    dry_run: bool = False,
) -> Mapping[str, object]:
    event: Dict[str, object] = {
        "dry_run": dry_run,
        "repo_id": repo_id,
        "selector": selector,
        "state": state,
    }
    if error:
        event["error"] = error
    if ref is not None:
        event.update({"ref_name": ref.ref_name, "sha": ref.sha, "version": ref.version})
    if packet_id:
        event["packet_id"] = packet_id
    return event


def _aggregate_state(events: Sequence[Mapping[str, object]]) -> str:
    states = [event.get("state") for event in events if event.get("state") in COLLECTION_TERMINAL]
    for state in ("failed", "retry-pending", "collected-change", "collected-baseline", "unchanged"):
        if state in states:
            return state
    return "unchanged"


def _has_terminal(events: Sequence[Mapping[str, object]], repo_id: str, selector: str) -> bool:
    return any(
        event.get("repo_id") == repo_id
        and event.get("selector") == selector
        and event.get("state") in COLLECTION_TERMINAL
        for event in events
    )


def _entry_for_sha(index: VersionIndex, sha: str) -> Optional[VersionEntry]:
    return next((entry for entry in index.versions if entry.sha == sha), None)


def _alias_snapshot(
    root: Path, config: RepoConfig, entry: VersionEntry, ref: ResolvedRef
) -> SnapshotRecord:
    target = root / entry.snapshot_path
    return SnapshotRecord(
        config.id,
        ref,
        "canonical",
        0,
        entry.collection_date,
        target,
        target,
        (),
        repository_url=config.url,
        company=config.company,
        repo_type=config.repo_type,
    )


def _snapshot_from_entry(root: Path, config: RepoConfig, entry: VersionEntry) -> SnapshotRecord:
    target = root / entry.snapshot_path
    metadata = _snapshot_metadata(target / "snapshot.md")
    ref_data = metadata.get("ref", {})
    files_data = metadata.get("files", [])
    files = tuple(
        SnapshotFile(item["path"], item["sha256"], item["size"], item["purpose"])
        for item in files_data
        if isinstance(item, dict)
        and isinstance(item.get("path"), str)
        and isinstance(item.get("sha256"), str)
        and type(item.get("size")) is int
        and isinstance(item.get("purpose"), str)
    )
    ref = ResolvedRef(
        config.id,
        entry.ref_kind,
        entry.ref_name,
        entry.sha,
        entry.version,
        entry.aliases,
        str(ref_data.get("upstream_commit_time", "")),
        ref_data.get("release_published_at") if isinstance(ref_data.get("release_published_at"), str) else None,
    )
    release = metadata.get("release_notes")
    release = release if isinstance(release, dict) else {}
    return SnapshotRecord(
        config.id,
        ref,
        "canonical",
        0,
        entry.collection_date,
        target,
        target,
        files,
        repository_url=config.url,
        company=config.company,
        repo_type=config.repo_type,
        release_notes_source_url=release.get("source_url"),
        release_notes_published_at=release.get("published_at"),
        release_notes_sha256=release.get("sha256"),
        release_notes_size=release.get("size"),
    )


def _snapshot_metadata(path: Path) -> Mapping[str, object]:
    text = path.read_text(encoding="utf-8")
    start = text.index("```json\n") + len("```json\n")
    end = text.index("\n```", start)
    value = json.loads(text[start:end])
    if not isinstance(value, dict):
        raise CollectionCommandError("snapshot metadata is not an object")
    return value


def _change_packet_state(
    root: Path,
    config: RepoConfig,
    packet_id: str,
    expected: str,
    requested: str,
) -> None:
    if _SAFE_PACKET_ID.fullmatch(packet_id) is None:
        raise CollectionUsageError("packet ID is invalid")
    packet_root = _packet_root(root, config)
    with packet_transaction(config, packet_root) as packet_root_descriptor:
        packet_descriptor = _open_packet_directory(packet_root_descriptor, packet_id)
        try:
            contract = _read_packet_json_object(packet_descriptor, "packet.json")
            if contract.get("packet_id") != packet_id or contract.get("repo_id") != config.id:
                raise CollectionUsageError("packet contract does not match the request")
            initial_state = contract.get("initial_state")
            if not isinstance(initial_state, str):
                raise CollectionCommandError("packet contract has an invalid initial state")
            events = _read_packet_jsonl(packet_descriptor, "state-events.jsonl")
            try:
                latest = validate_packet_history(packet_id, initial_state, events)
            except StateTransitionError as error:
                raise CollectionCommandError("packet state history is invalid: " + str(error)) from error
            if latest != expected:
                raise StateTransitionError(
                    "packet current state is " + latest + ", not requested --from " + expected
                )
            state = transition_packet(expected, requested)
            _append_packet_event(
                packet_descriptor,
                {"from_state": expected, "packet_id": packet_id, "state": state},
            )
        finally:
            os.close(packet_descriptor)


def _load_collection_events(root: Path) -> Tuple[Mapping[str, object], ...]:
    events = []
    runs = root / "tracking" / "github" / "runs"
    if not runs.is_dir():
        return ()
    for path in sorted(runs.glob("*.jsonl")):
        events.extend(_read_jsonl(path, ignore_invalid=True))
    return tuple(events)


def _load_packet_contracts(
    root: Path,
    repos: Sequence[RepoConfig],
) -> Tuple[Tuple[PacketRecord, ...], Mapping[str, str]]:
    packets = []
    states = {}
    for config in repos:
        packet_root = _packet_root(root, config)
        if not packet_root.exists() and not packet_root.is_symlink():
            continue
        with packet_transaction(config, packet_root) as packet_root_descriptor:
            names = sorted(
                name for name in os.listdir(packet_root_descriptor) if name != ".packet.lock"
            )
            for packet_id in names:
                packet_descriptor = _open_packet_directory(packet_root_descriptor, packet_id)
                try:
                    value = _read_packet_json_object(packet_descriptor, "packet.json")
                    packet = _packet_record_from_contract(
                        value, config, packet_id, packet_root / packet_id
                    )
                    events = _read_packet_jsonl(packet_descriptor, "state-events.jsonl")
                    state = validate_packet_history(
                        packet.packet_id, packet.initial_state, events
                    )
                finally:
                    os.close(packet_descriptor)
                if packet.packet_id in states:
                    raise CollectionCommandError("duplicate packet ID " + packet.packet_id)
                packets.append(packet)
                states[packet.packet_id] = state
    return tuple(packets), states


def _packet_record_from_contract(
    value: Mapping[str, object],
    config: RepoConfig,
    packet_id: str,
    directory: Path,
) -> PacketRecord:
    scalar_fields = (
        "packet_id",
        "repo_id",
        "packet_type",
        "from_snapshot",
        "to_snapshot",
        "initial_state",
    )
    if any(type(value.get(field)) is not str for field in scalar_fields):
        raise CollectionCommandError("packet contract has invalid scalar fields")
    required = value.get("required_reading")
    changed = value.get("changed_files")
    if (
        type(required) is not list
        or type(changed) is not list
        or any(type(item) is not str for item in required + changed)
        or value["packet_id"] != packet_id
        or value["repo_id"] != config.id
        or value["initial_state"] != "awaiting-review"
    ):
        raise CollectionCommandError("packet contract does not match its namespace")
    return PacketRecord(
        packet_id=packet_id,
        repo_id=config.id,
        packet_type=str(value["packet_type"]),
        from_snapshot=str(value["from_snapshot"]),
        to_snapshot=str(value["to_snapshot"]),
        required_reading=tuple(required),
        changed_files=tuple(changed),
        initial_state="awaiting-review",
        directory=directory,
    )


def _open_packet_directory(packet_root_descriptor: int, packet_id: str) -> int:
    if _SAFE_PACKET_ID.fullmatch(packet_id) is None:
        raise CollectionCommandError("packet directory name is invalid")
    flags = os.O_RDONLY | _directory_flag() | _no_follow_flag()
    try:
        return os.open(packet_id, flags, dir_fd=packet_root_descriptor)
    except OSError as error:
        raise CollectionCommandError("packet directory is not safe") from error


def _read_packet_json_object(directory_descriptor: int, name: str) -> Mapping[str, object]:
    value = _load_json_strict(_read_packet_text(directory_descriptor, name))
    if type(value) is not dict:
        raise CollectionCommandError(name + " is not a JSON object")
    return value


def _read_packet_jsonl(directory_descriptor: int, name: str) -> List[Mapping[str, object]]:
    events = []
    for line in _read_packet_text(directory_descriptor, name).splitlines():
        value = _load_json_strict(line)
        if type(value) is not dict:
            raise CollectionCommandError(name + " contains a non-object event")
        events.append(value)
    return events


def _read_packet_text(directory_descriptor: int, name: str) -> str:
    try:
        descriptor = os.open(
            name, os.O_RDONLY | _no_follow_flag(), dir_fd=directory_descriptor
        )
    except OSError as error:
        raise CollectionCommandError("packet file is not safe: " + name) from error
    try:
        if not stat.S_ISREG(os.fstat(descriptor).st_mode):
            raise CollectionCommandError("packet file is not regular: " + name)
        with os.fdopen(descriptor, "r", encoding="utf-8") as handle:
            descriptor = -1
            return handle.read()
    except (OSError, UnicodeDecodeError) as error:
        raise CollectionCommandError("packet file could not be read: " + name) from error
    finally:
        if descriptor >= 0:
            os.close(descriptor)


def _append_packet_event(directory_descriptor: int, event: Mapping[str, object]) -> None:
    try:
        descriptor = os.open(
            "state-events.jsonl",
            os.O_WRONLY | os.O_APPEND | _no_follow_flag(),
            dir_fd=directory_descriptor,
        )
    except OSError as error:
        raise CollectionCommandError("packet state history is not safe") from error
    try:
        if not stat.S_ISREG(os.fstat(descriptor).st_mode):
            raise CollectionCommandError("packet state history is not regular")
        payload = (json.dumps(dict(event), sort_keys=True) + "\n").encode("utf-8")
        if os.write(descriptor, payload) != len(payload):
            raise CollectionCommandError("packet state event append was incomplete")
    finally:
        os.close(descriptor)


def _load_json_strict(text: str) -> object:
    def reject_duplicates(pairs: Sequence[Tuple[str, object]]) -> dict:
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate JSON key " + key)
            result[key] = value
        return result

    return json.loads(text, object_pairs_hook=reject_duplicates)


def _directory_flag() -> int:
    flag = getattr(os, "O_DIRECTORY", None)
    if flag is None:
        raise CollectionCommandError("directory-only opening is unavailable")
    return flag


def _no_follow_flag() -> int:
    flag = getattr(os, "O_NOFOLLOW", None)
    if flag is None:
        raise CollectionCommandError("no-follow opening is unavailable")
    return flag


def _read_jsonl(path: Path, ignore_invalid: bool = False) -> List[Mapping[str, object]]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        return []
    result = []
    for line in lines:
        try:
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError("event is not an object")
        except (ValueError, json.JSONDecodeError):
            if ignore_invalid:
                continue
            raise
        result.append(value)
    return result


def _select_cli_repos(repos: Sequence[RepoConfig], arguments: argparse.Namespace) -> Tuple[RepoConfig, ...]:
    if arguments.repo is not None:
        if arguments.include_disabled:
            raise CollectionUsageError("--include-disabled applies only to batch selection")
        return (_explicit_repo(repos, arguments.repo),)
    enabled_only = not arguments.include_disabled
    selected = select_repos(
        repos,
        company=arguments.company,
        enabled_only=enabled_only,
    )
    if not selected:
        raise CollectionUsageError("repository selection is empty")
    return selected


def _explicit_repo(repos: Sequence[RepoConfig], repo_id: str) -> RepoConfig:
    selected = select_repos(repos, repo_id=repo_id, enabled_only=False)
    if len(selected) != 1:
        raise CollectionUsageError("unknown repository " + repo_id)
    return selected[0]


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="collect_github_repos.py")
    subparsers = parser.add_subparsers(dest="command", required=True)

    collect = subparsers.add_parser("collect")
    selection = collect.add_mutually_exclusive_group(required=True)
    selection.add_argument("--all", action="store_true")
    selection.add_argument("--company")
    selection.add_argument("--repo")
    mode = collect.add_mutually_exclusive_group()
    mode.add_argument("--ref", dest="refs", action="append")
    mode.add_argument("--release-mode", choices=("backfill", "future"))
    collect.add_argument("--include-disabled", action="store_true")
    collect.add_argument("--dry-run", action="store_true")

    compare = subparsers.add_parser("compare")
    compare.add_argument("--repo", required=True)
    compare.add_argument("--from", dest="from_selector", required=True)
    compare.add_argument("--to", dest="to_selector", required=True)

    prepare = subparsers.add_parser("prepare")
    prepare.add_argument("--repo", required=True)
    prepare.add_argument("--ref", required=True)

    subparsers.add_parser("status")

    packet_state = subparsers.add_parser("packet-state")
    packet_state.add_argument("--repo", required=True)
    packet_state.add_argument("--packet", required=True)
    packet_state.add_argument("--from", dest="from_state", required=True)
    packet_state.add_argument("--to", dest="to_state", required=True)
    return parser


def _registry_path(root: Path) -> Path:
    return root / "tracking" / "github" / "repo-registry.toml"


def _repo_tracking_root(root: Path, config: RepoConfig) -> Path:
    return root / "tracking" / "github" / "repos" / Path(config.id)


def _version_index_path(root: Path, config: RepoConfig) -> Path:
    return _repo_tracking_root(root, config) / "version-index.json"


def _packet_root(root: Path, config: RepoConfig) -> Path:
    return _repo_tracking_root(root, config) / "packets"


def _new_run_event_path(root: Path, repo_id: str) -> Path:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    slug = repo_id.replace("/", "-")
    return root / "tracking" / "github" / "runs" / (timestamp + "-" + slug + "-" + uuid.uuid4().hex + ".jsonl")


def _normalize_selector(selector: str) -> str:
    if not isinstance(selector, str) or not selector:
        raise CollectionUsageError("ref selector must not be empty")
    return "commit:" + selector if _FULL_SHA.fullmatch(selector) else selector


def _deduplicated(values: Sequence[str]) -> List[str]:
    result = []
    seen = set()
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


def _bounded_error(error: Exception) -> str:
    text = str(error).strip() or error.__class__.__name__
    return text[:1000] + ("..." if len(text) > 1000 else "")


def _render_result(result: CollectionResult, dry_run: bool) -> str:
    prefix = "dry-run " if dry_run else ""
    versions = ",".join(result.versions) if result.versions else "-"
    packets = ",".join(result.packet_ids) if result.packet_ids else "-"
    return prefix + result.repo_id + " state=" + result.state + " versions=" + versions + " packets=" + packets


def _write_text_atomic(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, name = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=str(path.parent))
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
        os.replace(str(temporary), str(path))
    except Exception:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass
        raise


if __name__ == "__main__":
    raise SystemExit(main())
