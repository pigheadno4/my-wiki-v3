"""Focused release-driven collection for the GitHub repository pilot."""

import argparse
from dataclasses import asdict, dataclass, replace
from datetime import date
import hashlib
import json
from pathlib import Path
import re
import tempfile
from typing import Callable, Dict, List, Optional, Sequence, Tuple, Union
from urllib.error import URLError

from github_canonical import safe_policy_path
from github_capsule_policy import (
    COMMIT_TREE_ADAPTER,
    TAGGED_TREE_ADAPTER,
    CapsuleConfig,
)
from github_collection_index import (
    checked_state_from_document,
    load_collection_index,
    write_collection_index,
)
from github_capsule_selection import (
    resolve_capsule,
    resolve_capsule_workspace,
)
from github_git import (
    GitCommandError,
    clone_repository,
    fetch_commit_history,
    fetch_required_refs,
    inspect_repository,
    run_git,
)
from github_git_tree import GitObjectReadError, GitTree
from github_npm_workspace import WorkspacePackage
from github_ingest_packets import (
    PackagePacketInput,
    RefPacketInput,
    build_ingest_packet,
    build_ref_ingest_packet,
    load_packet_required_reading,
    load_packet_summary,
    publish_queued_packet,
    publish_review_packet,
)
from github_pilot_store import (
    ComparisonRecord,
    PackageReleaseRecord,
    package_slug,
    publish_release_record,
    publish_source_snapshot,
    publish_source_supplement,
    read_upstream_changes,
    write_package_comparison,
    write_ref_comparison,
)
from github_registry import RepoConfig, VersionTrack, load_registry, validate_enabled_policy
from github_releases import (
    ReleaseCandidate,
    ReleaseEvidenceError,
    ReleaseNotesEvidence,
    discover_release_candidates,
    fetch_release_notes,
    select_release_candidates,
)
from github_versions import compare_semver, parse_package_tag, parse_semver
from github_work_items import (
    ChangeSignals,
    PacketStatusSummary,
    PackageChange,
    RefChange,
    RefChangeSignals,
    WorkItem,
    WorkItemStateError,
    build_work_item,
    build_ref_work_item,
    claim_next_ingest,
    evidence_attachment_required_reading,
    finalize_collected_work_item,
    load_work_items,
    recommend_ingest_mode,
    recommend_ref_ingest_mode,
    record_collection_failure,
    record_ingest_failure,
    transition_work_item,
    write_status_from_queue,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
WORK_ITEMS_PATH = Path("tracking/github/work-items.json")
STATUS_PATH = Path("tracking/github/status.md")
RETRYABLE_ERRORS = (
    ReleaseEvidenceError,
    GitObjectReadError,
    GitCommandError,
    URLError,
    OSError,
)
PUBLIC_EXPORT_FIELDS = ("main", "module", "types", "typings", "exports")
_FULL_SHA = re.compile(r"[0-9a-f]{40}")


class CollectionUsageError(ValueError):
    """A focused collection request is ambiguous or incomplete."""


@dataclass(frozen=True)
class CollectionResult:
    repo_id: str
    state: str
    release_ids: Tuple[str, ...]
    snapshot_paths: Tuple[str, ...]
    work_item_ids: Tuple[str, ...]
    errors: Tuple[str, ...]


@dataclass(frozen=True)
class CommitInventory:
    selected_file_count: int
    selected_utf8_bytes: int
    excluded_file_count: int
    excluded_utf8_bytes: int


@dataclass(frozen=True)
class CommitCollectionResult:
    repo_id: str
    state: str
    ref_ids: Tuple[str, ...]
    snapshot_paths: Tuple[str, ...]
    work_item_ids: Tuple[str, ...]
    errors: Tuple[str, ...]
    inventory: CommitInventory


@dataclass(frozen=True)
class _RetainedRelease:
    package: str
    version: str
    tag: str
    sha: str
    release_manifest: str
    notes_sha256: str


@dataclass(frozen=True)
class _PackageContext:
    candidate: ReleaseCandidate
    evidence: Optional[ReleaseNotesEvidence]
    release_date: str
    prior: Optional[_RetainedRelease]
    changed_paths: Tuple[str, ...]
    from_paths: Tuple[str, ...]
    to_paths: Tuple[str, ...]
    public_exports_changed: bool
    release_record: Optional[PackageReleaseRecord] = None


def collect_one(
    root: Path,
    config: RepoConfig,
    release_mode: Optional[str] = None,
    release: Optional[str] = None,
    dry_run: bool = False,
    clone_source: Optional[Path] = None,
    release_notes_fetcher: Callable[
        [RepoConfig, ReleaseCandidate], Optional[ReleaseNotesEvidence]
    ] = fetch_release_notes,
    collection_date: Optional[str] = None,
    max_attempts: int = 3,
) -> Union[CollectionResult, CommitCollectionResult]:
    """Collect retained package releases and create approval-gated work items."""
    if release_mode not in (None, "backfill", "future"):
        raise CollectionUsageError("release mode must be backfill or future")
    if (release_mode is None) == (release is None):
        raise CollectionUsageError("choose exactly one release mode or exact package release")
    if config.version_strategy == "commit" and release is not None:
        raise CollectionUsageError("commit repository does not support releases")
    if not isinstance(max_attempts, int) or not 1 <= max_attempts <= 3:
        raise CollectionUsageError("max_attempts must be between one and three")
    if not config.enabled and not dry_run:
        raise CollectionUsageError(config.id + ": repository is disabled")
    readiness_config = replace(config, enabled=True) if not config.enabled and dry_run else config
    readiness_errors = validate_enabled_policy(readiness_config)
    if readiness_errors:
        raise CollectionUsageError(config.id + ": " + readiness_errors[0])
    collected = collection_date or date.today().isoformat()
    root = Path(root).resolve()
    queue_path = root / WORK_ITEMS_PATH
    context: Dict[str, object] = {}
    last_error: Optional[Exception] = None

    for attempt in range(1, max_attempts + 1):
        try:
            result = _collect_attempt(
                root,
                config,
                release_mode,
                release,
                dry_run,
                clone_source,
                release_notes_fetcher,
                collected,
                context,
            )
        except RETRYABLE_ERRORS as error:
            last_error = error
            if attempt < max_attempts:
                continue
            break
        except Exception as error:
            last_error = error
            return _record_failed_collection(
                root,
                config,
                context,
                error,
                collected,
                attempt,
                manual_review=True,
                dry_run=dry_run,
            )
        else:
            if not dry_run:
                regenerate_status(root)
                if (root / "tracking/github/repo-registry.toml").exists():
                    regenerate_collection_index(
                        root,
                        _checked_update(config.id, result, collected),
                        collected,
                    )
            return result

    if last_error is None:
        raise RuntimeError("collection attempt ended without a result")
    result = _record_failed_collection(
        root,
        config,
        context,
        last_error,
        collected,
        max_attempts,
        manual_review=False,
        dry_run=dry_run,
    )
    if not dry_run and queue_path.exists():
        regenerate_status(root)
    if not dry_run and (root / "tracking/github/repo-registry.toml").exists():
        regenerate_collection_index(
            root,
            _checked_update(config.id, result, collected),
            collected,
        )
    return result


def collect_ref_boundary(
    root: Path,
    config: RepoConfig,
    from_sha: str,
    to_sha: str,
    dry_run: bool = False,
    clone_source: Optional[Path] = None,
    collection_date: Optional[str] = None,
    max_attempts: int = 3,
) -> CommitCollectionResult:
    """Collect one explicit ancestor-to-descendant repository boundary."""
    from_sha = _require_boundary_sha(from_sha, "from SHA")
    to_sha = _require_boundary_sha(to_sha, "to SHA")
    if from_sha == to_sha:
        raise CollectionUsageError("from SHA and to SHA must differ")
    if not isinstance(max_attempts, int) or not 1 <= max_attempts <= 3:
        raise CollectionUsageError("max_attempts must be between one and three")
    if not config.enabled and not dry_run:
        raise CollectionUsageError(config.id + ": repository is disabled")
    readiness_config = replace(config, enabled=True) if not config.enabled else config
    readiness_errors = validate_enabled_policy(readiness_config)
    if readiness_errors:
        raise CollectionUsageError(config.id + ": " + readiness_errors[0])
    capsule = _one_capsule(config)
    if capsule.adapter not in (COMMIT_TREE_ADAPTER, TAGGED_TREE_ADAPTER):
        raise CollectionUsageError(
            "exact-ref collection requires commit-tree-v1 or tagged-tree-v1"
        )

    root = Path(root).resolve()
    collected = collection_date or date.today().isoformat()
    context: Dict[str, object] = {}
    last_error: Optional[Exception] = None
    for attempt in range(1, max_attempts + 1):
        try:
            result = _collect_ref_boundary_attempt(
                root,
                config,
                from_sha,
                to_sha,
                dry_run,
                clone_source,
                collected,
                context,
            )
        except RETRYABLE_ERRORS as error:
            last_error = error
            if attempt < max_attempts:
                continue
            break
        except CollectionUsageError:
            raise
        except Exception as error:
            last_error = error
            return _record_failed_commit_collection(
                root,
                config,
                context,
                error,
                collected,
                attempt,
                manual_review=True,
                dry_run=dry_run,
            )
        else:
            if not dry_run:
                regenerate_status(root)
                if (root / "tracking/github/repo-registry.toml").exists():
                    regenerate_collection_index(root, generated_date=collected)
            return result

    if last_error is None:
        raise RuntimeError("exact-ref collection attempt ended without a result")
    result = _record_failed_commit_collection(
        root,
        config,
        context,
        last_error,
        collected,
        max_attempts,
        manual_review=False,
        dry_run=dry_run,
    )
    if not dry_run and (root / "tracking/github/repo-registry.toml").exists():
        regenerate_collection_index(root, generated_date=collected)
    return result


def _collect_ref_boundary_attempt(
    root: Path,
    config: RepoConfig,
    from_sha: str,
    to_sha: str,
    dry_run: bool,
    clone_source: Optional[Path],
    collected_date: str,
    context: Dict[str, object],
) -> CommitCollectionResult:
    effective = replace(config, url=str(clone_source)) if clone_source is not None else config
    existing_items = load_work_items(root / WORK_ITEMS_PATH)
    existing = next(
        (
            item
            for item in existing_items
            if item.repo_id == config.id
            and item.sha == to_sha
            and any(
                change.from_sha == from_sha and change.to_sha == to_sha
                for change in item.ref_changes
            )
            and item.state
            not in ("discovered", "collection_failed", "needs_manual_review")
        ),
        None,
    )
    if existing is not None:
        return CommitCollectionResult(
            config.id,
            "unchanged",
            ("default-branch@" + to_sha[:7],),
            (),
            (),
            (),
            CommitInventory(0, 0, 0, 0),
        )

    with tempfile.TemporaryDirectory(prefix="wiki-github-ref-") as temporary:
        clone_path = Path(temporary) / "repository"
        clone_repository(effective, clone_path)
        fetch_required_refs(
            effective,
            clone_path,
            ("commit:" + from_sha, "commit:" + to_sha),
        )
        fetch_commit_history(clone_path, to_sha)
        try:
            run_git(["merge-base", "--is-ancestor", from_sha, to_sha], clone_path)
        except GitCommandError as error:
            if error.returncode == 1:
                raise CollectionUsageError(
                    "from SHA must be an ancestor of to SHA"
                ) from error
            raise

        default_branch = run_git(["symbolic-ref", "--short", "HEAD"], clone_path)
        ref_id = "default-branch@" + to_sha[:7]
        context["commit_ref"] = (default_branch, to_sha, ref_id)
        changes = read_upstream_changes(clone_path, from_sha, to_sha)
        changed_paths = tuple(
            sorted(
                {
                    path
                    for change in changes
                    for path in (change.old_path, change.new_path)
                    if path
                }
            )
        )
        mode, reasons = recommend_ref_ingest_mode(
            RefChangeSignals(from_sha, to_sha, changed_paths)
        )
        preliminary_change = RefChange(
            "default-branch",
            default_branch,
            from_sha,
            to_sha,
            ref_id,
            "",
            mode,
            reasons,
        )
        context["ref_change"] = preliminary_change

        capsule = _one_capsule(config)
        before_tree = GitTree(clone_path, from_sha, config.max_file_bytes)
        after_tree = GitTree(clone_path, to_sha, config.max_file_bytes)
        before_changed = tuple(
            sorted({change.old_path for change in changes if change.old_path})
        )
        after_changed = tuple(
            sorted({change.new_path for change in changes if change.new_path})
        )
        before_resolution = resolve_capsule(
            before_tree,
            capsule,
            config.secret_allowlist,
            changed_paths=before_changed,
            versions=_ref_capsule_versions(capsule, from_sha),
        )
        after_resolution = resolve_capsule(
            after_tree,
            capsule,
            config.secret_allowlist,
            changed_paths=after_changed,
            versions=_ref_capsule_versions(capsule, to_sha),
        )
        inventory = _commit_inventory(after_tree, after_resolution)
        context["inventory"] = inventory
        if dry_run:
            return CommitCollectionResult(
                config.id,
                "discovered",
                (ref_id,),
                (),
                (),
                (),
                inventory,
            )

        before_snapshot = publish_source_snapshot(
            root,
            config,
            before_tree,
            before_resolution,
            collected_date,
            ("default-branch@" + from_sha[:7],),
        )
        after_snapshot = publish_source_snapshot(
            root,
            config,
            after_tree,
            after_resolution,
            collected_date,
            (ref_id,),
        )
        prior_manifest = _relative(root, before_snapshot.manifest_path)
        snapshot_manifest = _relative(root, after_snapshot.manifest_path)
        context["prior_ref"] = _boundary_prior_item(
            config.id, from_sha, collected_date, prior_manifest
        )
        context["snapshot_manifest"] = snapshot_manifest

        before_paths = tuple(item.path for item in before_resolution.files)
        after_paths = tuple(item.path for item in after_resolution.files)
        comparison = write_ref_comparison(
            root,
            config,
            clone_path,
            default_branch,
            from_sha,
            before_paths,
            to_sha,
            after_paths,
        )
        comparison_manifest = _relative(root, comparison.metadata_path)
        selected_changes = comparison.upstream_changes
        excluded_paths = {
            path for path, _ in before_resolution.excluded
        } | {path for path, _ in after_resolution.excluded}
        excluded_changes = tuple(
            change
            for change in changes
            if change not in selected_changes
            and any(
                path in excluded_paths
                for path in (change.old_path, change.new_path)
                if path
            )
        )
        change = replace(
            preliminary_change,
            comparison_manifest=comparison_manifest,
        )
        work_item = build_ref_work_item(
            config.id,
            to_sha,
            collected_date,
            (change,),
            snapshot_manifest,
        )
        packet = build_ref_ingest_packet(
            root,
            config,
            work_item.work_item_id,
            snapshot_manifest,
            RefPacketInput(
                "default-branch",
                default_branch,
                from_sha,
                to_sha,
                comparison_manifest,
                prior_manifest,
                tuple(selected_changes),
                tuple(excluded_changes),
            ),
            "queued",
        )
        if packet.document["evidence_gaps"] or packet.document["unclassified_changes"]:
            raise CollectionUsageError("exact-ref packet requires manual review")
        recommendation = packet.document["recommendation"]
        change = replace(
            change,
            recommended_mode=str(recommendation["mode"]),
            reasons=tuple(str(reason) for reason in recommendation["reasons"]),
        )
        work_item = build_ref_work_item(
            config.id,
            to_sha,
            collected_date,
            (change,),
            snapshot_manifest,
        )
        context["ref_change"] = change
        context["work_item"] = work_item
        packet_path = publish_queued_packet(root, config, packet)
        work_item = replace(work_item, ingest_packet=_relative(root, packet_path))
        finalize_collected_work_item(root / WORK_ITEMS_PATH, work_item)
        return CommitCollectionResult(
            config.id,
            "awaiting_approval",
            (ref_id,),
            (prior_manifest, snapshot_manifest),
            (work_item.work_item_id,),
            (),
            inventory,
        )


def _require_boundary_sha(value: str, label: str) -> str:
    if not isinstance(value, str) or _FULL_SHA.fullmatch(value) is None:
        raise CollectionUsageError(label + " must be a full lowercase Git SHA")
    return value


def _ref_capsule_versions(capsule: CapsuleConfig, sha: str):
    if capsule.adapter == TAGGED_TREE_ADAPTER:
        return {capsule.focus_packages[0]: "unreleased-" + sha[:7]}
    return None


def _boundary_prior_item(
    repo_id: str,
    sha: str,
    collection_date: str,
    snapshot_manifest: str,
) -> WorkItem:
    change = RefChange(
        "default-branch",
        "boundary-base",
        "",
        sha,
        "default-branch@" + sha[:7],
        "",
        "full",
        ("initial-commit-baseline",),
    )
    return build_ref_work_item(
        repo_id,
        sha,
        collection_date,
        (change,),
        snapshot_manifest,
    )


def _collect_attempt(
    root: Path,
    config: RepoConfig,
    release_mode: Optional[str],
    release: Optional[str],
    dry_run: bool,
    clone_source: Optional[Path],
    release_notes_fetcher: Callable[
        [RepoConfig, ReleaseCandidate], Optional[ReleaseNotesEvidence]
    ],
    collected_date: str,
    context: Dict[str, object],
) -> Union[CollectionResult, CommitCollectionResult]:
    if config.version_strategy == "commit":
        return _collect_commit_attempt(
            root,
            config,
            release_mode,
            dry_run,
            clone_source,
            collected_date,
            context,
        )
    return _collect_release_attempt(
        root,
        config,
        release_mode,
        release,
        dry_run,
        clone_source,
        release_notes_fetcher,
        collected_date,
        context,
    )


def _collect_release_attempt(
    root: Path,
    config: RepoConfig,
    release_mode: Optional[str],
    release: Optional[str],
    dry_run: bool,
    clone_source: Optional[Path],
    release_notes_fetcher: Callable[
        [RepoConfig, ReleaseCandidate], Optional[ReleaseNotesEvidence]
    ],
    collected_date: str,
    context: Dict[str, object],
) -> CollectionResult:
    effective = replace(config, url=str(clone_source)) if clone_source is not None else config
    existing_items = load_work_items(root / WORK_ITEMS_PATH)
    with tempfile.TemporaryDirectory(prefix="wiki-github-") as temporary:
        clone_path = Path(temporary) / "repository"
        clone_repository(effective, clone_path)
        candidates = _select_candidates(
            effective, config, clone_path, existing_items, release_mode, release
        )
        context["candidates"] = candidates
        if not candidates:
            state = "not_available" if release is not None else "unchanged"
            return CollectionResult(config.id, state, (), (), (), ())
        history = _load_retained_history(root, config)
        evidence_by_id = {
            _release_id(candidate): release_notes_fetcher(config, candidate)
            for candidate in candidates
        }
        candidates, revised_release_ids = _changed_candidates(
            root, candidates, evidence_by_id, history, existing_items
        )
        context["candidates"] = candidates
        if not candidates:
            return CollectionResult(config.id, "unchanged", (), (), (), ())

        if dry_run:
            fetch_required_refs(
                effective,
                clone_path,
                tuple("tag:" + tag for tag in sorted({item.tag for item in candidates})),
            )
            _verify_fetched_candidates(clone_path, candidates)
            ordered = _sort_candidates(candidates, evidence_by_id, clone_path)
            release_ids = tuple(_release_id(candidate) for candidate in ordered)
            return CollectionResult(config.id, "discovered", release_ids, (), (), ())

        prior_tags = {
            retained.tag
            for candidate in candidates
            for retained in [_latest_prior(history.get(candidate.package, ()), candidate.version)]
            if retained is not None
        }
        fetch_required_refs(
            effective,
            clone_path,
            tuple("tag:" + tag for tag in sorted({item.tag for item in candidates} | prior_tags)),
        )
        _verify_fetched_candidates(clone_path, candidates)
        ordered = _sort_candidates(candidates, evidence_by_id, clone_path)
        groups = _group_by_sha(ordered)
        work_item_ids: List[str] = []
        snapshot_paths: List[str] = []

        for group in groups:
            context["group"] = tuple(group)
            context.pop("package_contexts", None)
            context.pop("snapshot_manifest", None)
            context.pop("changes", None)
            package_contexts = _prepare_group(
                root,
                config,
                clone_path,
                group,
                evidence_by_id,
                history,
                collected_date,
                revised_release_ids,
            )
            context["package_contexts"] = package_contexts
            tree = GitTree(clone_path, group[0].commit_sha, config.max_file_bytes)
            capsule = _one_capsule(config)
            changed_paths = tuple(
                sorted({path for item in package_contexts for path in item.changed_paths})
            )
            resolution = resolve_capsule(
                tree,
                capsule,
                config.secret_allowlist,
                changed_paths=changed_paths,
                versions={
                    candidate.package: candidate.version for candidate in group
                },
            )
            snapshot = publish_source_snapshot(
                root,
                config,
                tree,
                resolution,
                collected_date,
                tuple(_release_id(item) for item in group),
            )
            snapshot_manifest = _relative(root, snapshot.manifest_path)
            context["snapshot_manifest"] = snapshot_manifest
            package_contexts = tuple(
                replace(
                    item,
                    release_record=publish_release_record(
                        root,
                        config,
                        item.candidate,
                        item.release_date,
                        item.evidence,
                        collected_date,
                    ),
                )
                for item in package_contexts
            )
            context["package_contexts"] = package_contexts
            changes = tuple(
                _publish_comparison_and_change(
                    root,
                    config,
                    clone_path,
                    item,
                    _release_id(item.candidate) in revised_release_ids,
                )
                for item in package_contexts
            )
            context["changes"] = changes
            revision_records = tuple(
                item.release_record.notes_sha256
                for item in package_contexts
                if _release_id(item.candidate) in revised_release_ids
            )
            evidence_revision = (
                hashlib.sha256("\n".join(sorted(revision_records)).encode("ascii")).hexdigest()
                if revision_records
                else ""
            )
            work_item = build_work_item(
                config.id,
                group[0].commit_sha,
                collected_date,
                changes,
                snapshot_manifest,
                evidence_revision,
            )
            package_inputs = tuple(
                _package_packet_input(
                    root,
                    config,
                    clone_path,
                    item,
                    change,
                    snapshot_manifest,
                    _release_id(item.candidate) in revised_release_ids,
                )
                for item, change in zip(package_contexts, changes)
            )
            packet = build_ingest_packet(
                root,
                config,
                work_item.work_item_id,
                snapshot_manifest,
                package_inputs,
                "queued",
            )
            packet_packages = {
                row["package"]: row for row in packet.document["packages"]
            }
            changes = tuple(
                replace(
                    change,
                    recommended_mode=packet_packages[change.package][
                        "recommendation"
                    ]["mode"],
                    reasons=tuple(
                        packet_packages[change.package]["recommendation"][
                            "reasons"
                        ]
                    ),
                )
                for change in changes
            )
            work_item = build_work_item(
                config.id,
                group[0].commit_sha,
                collected_date,
                changes,
                snapshot_manifest,
                evidence_revision,
            )
            packet_path = publish_queued_packet(root, config, packet)
            work_item = replace(
                work_item,
                ingest_packet=_relative(root, packet_path),
            )
            finalize_collected_work_item(root / WORK_ITEMS_PATH, work_item)
            work_item_ids.append(work_item.work_item_id)
            snapshot_paths.append(snapshot_manifest)
            for item in package_contexts:
                history.setdefault(item.candidate.package, []).append(
                    _retained_from_record(item.release_record)
                )

        return CollectionResult(
            config.id,
            "awaiting_approval",
            tuple(_release_id(candidate) for candidate in ordered),
            tuple(snapshot_paths),
            tuple(work_item_ids),
            (),
        )


def _collect_commit_attempt(
    root: Path,
    config: RepoConfig,
    release_mode: Optional[str],
    dry_run: bool,
    clone_source: Optional[Path],
    collected_date: str,
    context: Dict[str, object],
) -> CommitCollectionResult:
    for key in (
        "commit_ref",
        "inventory",
        "prior_ref",
        "ref_change",
        "snapshot_manifest",
        "work_item",
    ):
        context.pop(key, None)
    if release_mode not in ("backfill", "future"):
        raise CollectionUsageError("commit collection requires backfill or future mode")
    effective = replace(config, url=str(clone_source)) if clone_source is not None else config
    existing_items = load_work_items(root / WORK_ITEMS_PATH)
    prior = _latest_accepted_ref(existing_items, config.id)
    context["prior_ref"] = prior
    with tempfile.TemporaryDirectory(prefix="wiki-github-commit-") as temporary:
        clone_path = Path(temporary) / "repository"
        clone_repository(effective, clone_path)
        inspection = inspect_repository(effective, clone_path)
        branch = next(
            ref
            for ref in inspection.refs
            if ref.ref_kind == "branch" and ref.ref_name == inspection.default_branch
        )
        tree = GitTree(clone_path, branch.sha, config.max_file_bytes)
        capsule = _one_capsule(config)
        if capsule.adapter != COMMIT_TREE_ADAPTER:
            raise CollectionUsageError("commit repository requires commit-tree-v1")
        resolution = resolve_capsule(tree, capsule, config.secret_allowlist)
        inventory = _commit_inventory(tree, resolution)
        ref_id = "default-branch@" + branch.sha[:7]
        context["commit_ref"] = (branch.ref_name, branch.sha, ref_id)
        context["inventory"] = inventory

        if dry_run:
            return CommitCollectionResult(
                config.id,
                "discovered",
                (ref_id,),
                (),
                (),
                (),
                inventory,
            )
        if prior is not None and release_mode == "backfill":
            return CommitCollectionResult(
                config.id, "unchanged", (ref_id,), (), (), (), inventory
            )
        if prior is not None and prior.sha == branch.sha:
            return CommitCollectionResult(
                config.id, "unchanged", (ref_id,), (), (), (), inventory
            )

        current_fingerprint = _resolution_fingerprint(resolution)
        prior_manifest = ""
        prior_paths: Tuple[str, ...] = ()
        prior_excluded: Tuple[str, ...] = ()
        if prior is not None:
            prior_manifest = prior.snapshot_manifest
            prior_document = _load_snapshot_document(root, prior_manifest, config.id)
            prior_fingerprint = _snapshot_selected_fingerprint(
                prior_document,
                capsule.source_id,
            )
            if prior_fingerprint == current_fingerprint:
                return CommitCollectionResult(
                    config.id, "unchanged", (ref_id,), (), (), (), inventory
                )
            prior_paths = tuple(path for path, _ in prior_fingerprint)
            prior_excluded = tuple(
                sorted({str(row["path"]) for row in prior_document["excluded"]})
            )

        snapshot = publish_source_snapshot(
            root,
            config,
            tree,
            resolution,
            collected_date,
            (ref_id,),
        )
        snapshot_manifest = _relative(root, snapshot.manifest_path)
        context["snapshot_manifest"] = snapshot_manifest
        current_paths = tuple(item.path for item in resolution.files)
        comparison_manifest = ""
        selected_changes = ()
        excluded_changes = ()
        if prior is not None:
            comparison = write_ref_comparison(
                root,
                config,
                clone_path,
                branch.ref_name,
                prior.sha,
                prior_paths,
                branch.sha,
                current_paths,
            )
            comparison_manifest = _relative(root, comparison.metadata_path)
            selected_changes = comparison.upstream_changes
            all_changes = read_upstream_changes(clone_path, prior.sha, branch.sha)
            excluded_paths = set(prior_excluded) | {
                path for path, _ in resolution.excluded
            }
            excluded_changes = tuple(
                change
                for change in all_changes
                if any(
                    path in excluded_paths
                    for path in (change.old_path, change.new_path)
                    if path
                )
                and change not in selected_changes
            )

        mode, reasons = recommend_ref_ingest_mode(
            RefChangeSignals(
                prior.sha if prior is not None else "",
                branch.sha,
                tuple(
                    sorted(
                        {
                            path
                            for change in selected_changes
                            for path in (change.old_path, change.new_path)
                            if path
                        }
                    )
                ),
            )
        )
        change = RefChange(
            ref_kind="default-branch",
            ref_name=branch.ref_name,
            from_sha=prior.sha if prior is not None else "",
            to_sha=branch.sha,
            display_identity=ref_id,
            comparison_manifest=comparison_manifest,
            recommended_mode=mode,
            reasons=reasons,
        )
        work_item = build_ref_work_item(
            config.id,
            branch.sha,
            collected_date,
            (change,),
            snapshot_manifest,
        )
        context["ref_change"] = change
        context["work_item"] = work_item
        packet = build_ref_ingest_packet(
            root,
            config,
            work_item.work_item_id,
            snapshot_manifest,
            RefPacketInput(
                ref_kind="default-branch",
                ref_name=branch.ref_name,
                from_sha=change.from_sha,
                to_sha=change.to_sha,
                comparison_manifest=comparison_manifest,
                prior_snapshot_manifest=prior_manifest,
                upstream_changes=tuple(selected_changes),
                excluded_changes=tuple(excluded_changes),
            ),
            "queued",
        )
        if packet.document["evidence_gaps"] or packet.document["unclassified_changes"]:
            raise CollectionUsageError("commit packet requires manual review")
        packet_recommendation = packet.document["recommendation"]
        change = replace(
            change,
            recommended_mode=str(packet_recommendation["mode"]),
            reasons=tuple(str(reason) for reason in packet_recommendation["reasons"]),
        )
        work_item = build_ref_work_item(
            config.id,
            branch.sha,
            collected_date,
            (change,),
            snapshot_manifest,
        )
        packet_path = publish_queued_packet(root, config, packet)
        work_item = replace(work_item, ingest_packet=_relative(root, packet_path))
        finalize_collected_work_item(root / WORK_ITEMS_PATH, work_item)
        return CommitCollectionResult(
            config.id,
            "awaiting_approval",
            (ref_id,),
            (snapshot_manifest,),
            (work_item.work_item_id,),
            (),
            inventory,
        )


def _latest_accepted_ref(
    items: Sequence[WorkItem],
    repo_id: str,
) -> Optional[WorkItem]:
    accepted = tuple(
        item
        for item in items
        if item.repo_id == repo_id
        and item.ref_changes
        and item.state not in ("discovered", "collection_failed", "needs_manual_review")
    )
    if not accepted:
        return None
    prior_shas = {
        change.from_sha
        for item in accepted
        for change in item.ref_changes
        if change.from_sha
    }
    tips = tuple(item for item in accepted if item.sha not in prior_shas)
    candidates = tips or accepted
    return max(candidates, key=lambda item: (item.collection_date, item.work_item_id))


def _commit_inventory(tree: GitTree, resolution) -> CommitInventory:
    excluded_paths = tuple(sorted({path for path, _ in resolution.excluded}))
    return CommitInventory(
        len(resolution.files),
        sum(item.size for item in resolution.files),
        len(excluded_paths),
        sum(tree.blob_size(path) for path in excluded_paths),
    )


def _resolution_fingerprint(resolution) -> Tuple[Tuple[str, str], ...]:
    return tuple(sorted((item.path, item.sha256) for item in resolution.files))


def _load_snapshot_document(root: Path, relative: str, repo_id: str) -> dict:
    path = root / relative
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        raise CollectionUsageError("accepted commit snapshot is unreadable") from None
    if (
        not isinstance(document, dict)
        or document.get("repository") != repo_id
        or not isinstance(document.get("files"), list)
        or not isinstance(document.get("excluded"), list)
    ):
        raise CollectionUsageError("accepted commit snapshot is invalid")
    return document


def _snapshot_selected_fingerprint(
    document: dict,
    source_id: str,
) -> Tuple[Tuple[str, str], ...]:
    rows = tuple(
        (str(row.get("path", "")), str(row.get("sha256", "")))
        for row in document["files"]
        if isinstance(row, dict) and row.get("package") == source_id
    )
    if (
        not rows
        or len({path for path, _ in rows}) != len(rows)
        or any(
            not safe_policy_path(path)
            or len(digest) != 64
            or any(character not in "0123456789abcdef" for character in digest)
            for path, digest in rows
        )
    ):
        raise CollectionUsageError("accepted commit snapshot has invalid selected evidence")
    return tuple(sorted(rows))


def _select_candidates(
    effective: RepoConfig,
    config: RepoConfig,
    clone_path: Path,
    items: Sequence[WorkItem],
    release_mode: Optional[str],
    release: Optional[str],
) -> Tuple[ReleaseCandidate, ...]:
    existing = _existing_release_ids(items)
    discovered: Dict[str, ReleaseCandidate] = {}
    for track in config.version_tracks:
        rows = discover_release_candidates(effective, clone_path, track)
        if release is not None:
            package, version = parse_package_release(release)
            selected = tuple(
                row for row in rows if row.package == package and row.version == version
            )
        else:
            package = _track_package(track)
            versions = tuple(
                release_id[len(package) + 1 :]
                for release_id in existing
                if package and release_id.startswith(package + "@")
            )
            new_selected = select_release_candidates(
                track, rows, existing_versions=versions, mode=release_mode or "backfill"
            )
            retained = tuple(row for row in rows if _release_id(row) in existing)
            selected = new_selected + retained
        for candidate in selected:
            identity = _release_id(candidate)
            prior = discovered.get(identity)
            if prior is not None and prior.commit_sha != candidate.commit_sha:
                raise CollectionUsageError("release identity resolves to conflicting SHAs")
            discovered[identity] = candidate
    return tuple(discovered[key] for key in sorted(discovered))


def _prepare_group(
    root: Path,
    config: RepoConfig,
    clone_path: Path,
    group: Sequence[ReleaseCandidate],
    evidence_by_id: Dict[str, Optional[ReleaseNotesEvidence]],
    history: Dict[str, List[_RetainedRelease]],
    collected_date: str,
    revised_release_ids: set,
) -> Tuple[_PackageContext, ...]:
    capsule = _one_capsule(config)
    current_tree = GitTree(clone_path, group[0].commit_sha, config.max_file_bytes)
    current_workspace = resolve_capsule_workspace(
        current_tree,
        capsule,
        {candidate.package: candidate.version for candidate in group},
    )
    contexts = []
    for candidate in sorted(group, key=lambda item: item.package):
        current_package = _workspace_package(current_workspace.packages, candidate.package)
        if current_package.version != candidate.version:
            raise CollectionUsageError(
                "release tag version does not match package manifest version for "
                + _release_id(candidate)
            )
        evidence = evidence_by_id[_release_id(candidate)]
        release_date = (
            evidence.published_at
            if evidence is not None
            else run_git(["show", "-s", "--format=%cI", candidate.commit_sha], clone_path)
        )
        prior = _latest_prior(history.get(candidate.package, ()), candidate.version)
        if _release_id(candidate) in revised_release_ids:
            changed_paths = ()
            from_paths = ()
            exports_changed = False
        elif prior is None:
            changed_paths = ()
            from_paths = ()
            exports_changed = False
        else:
            prior_tree = GitTree(clone_path, prior.sha, config.max_file_bytes)
            prior_workspace = resolve_capsule_workspace(
                prior_tree,
                capsule,
                {candidate.package: prior.version},
            )
            prior_package = _workspace_package(prior_workspace.packages, candidate.package)
            if capsule.adapter == TAGGED_TREE_ADAPTER:
                changed_paths = _tagged_changed_paths(
                    clone_path,
                    prior.sha,
                    candidate.commit_sha,
                    prior_package,
                    current_package,
                )
                from_paths = _tagged_pathspecs(prior_package)
                exports_changed = False
            else:
                changed_paths = _package_changed_paths(
                    clone_path,
                    prior.sha,
                    candidate.commit_sha,
                    prior_package,
                    current_package,
                )
                from_paths = _package_pathspecs(prior_package)
                exports_changed = _public_exports(
                    prior_tree,
                    prior_package,
                ) != _public_exports(current_tree, current_package)
        to_paths = (
            _tagged_pathspecs(current_package)
            if capsule.adapter == TAGGED_TREE_ADAPTER
            else _package_pathspecs(current_package)
        )
        contexts.append(
            _PackageContext(
                candidate,
                evidence,
                release_date,
                prior,
                changed_paths,
                from_paths,
                to_paths,
                exports_changed,
            )
        )
    return tuple(contexts)


def _publish_comparison_and_change(
    root: Path,
    config: RepoConfig,
    clone_path: Path,
    context: _PackageContext,
    release_notes_revision: bool = False,
) -> PackageChange:
    if context.release_record is None:
        raise CollectionUsageError("release record must be published before comparison")
    comparison: Optional[ComparisonRecord] = None
    prior_version = context.prior.version if context.prior is not None else ""
    if context.prior is not None and not release_notes_revision:
        comparison = write_package_comparison(
            root,
            config,
            clone_path,
            context.candidate.package,
            context.prior.version,
            context.prior.sha,
            context.from_paths,
            context.candidate.version,
            context.candidate.commit_sha,
            context.to_paths,
        )
    notes = (
        context.evidence.content.decode("utf-8", errors="replace")
        if context.evidence is not None
        else ""
    )
    if release_notes_revision:
        mode, reasons = "delta", ("release-notes-revision",)
    else:
        mode, reasons = recommend_ingest_mode(
            ChangeSignals(
                context.candidate.package,
                prior_version,
                context.candidate.version,
                context.changed_paths,
                context.public_exports_changed,
                notes,
            )
        )
    return PackageChange(
        context.candidate.package,
        prior_version,
        context.candidate.version,
        _release_id(context.candidate),
        _relative(root, context.release_record.manifest_path),
        _relative(root, comparison.metadata_path) if comparison is not None else "",
        mode,
        reasons,
    )


def _package_packet_input(
    root: Path,
    config: RepoConfig,
    clone_path: Path,
    context: _PackageContext,
    change: PackageChange,
    current_snapshot_manifest: str,
    release_notes_revision: bool,
) -> PackagePacketInput:
    if context.release_record is None:
        raise CollectionUsageError("release record must exist before packet build")
    if release_notes_revision:
        return PackagePacketInput(
            context.candidate.package,
            context.candidate.version,
            context.candidate.version,
            context.candidate.commit_sha,
            context.candidate.commit_sha,
            change.release_manifest,
            "",
            current_snapshot_manifest,
            (),
            True,
        )
    prior = context.prior
    return PackagePacketInput(
        context.candidate.package,
        prior.version if prior is not None else "",
        context.candidate.version,
        prior.sha if prior is not None else "",
        context.candidate.commit_sha,
        change.release_manifest,
        change.comparison_manifest,
        (
            _snapshot_manifest_for_sha(root, config, prior.sha)
            if prior is not None
            else ""
        ),
        (
            read_upstream_changes(
                clone_path,
                prior.sha,
                context.candidate.commit_sha,
            )
            if prior is not None
            else ()
        ),
    )


def _record_failed_collection(
    root: Path,
    config: RepoConfig,
    context: Dict[str, object],
    error: Exception,
    collected_date: str,
    attempts: int,
    manual_review: bool,
    dry_run: bool = False,
) -> Union[CollectionResult, CommitCollectionResult]:
    if config.version_strategy == "commit":
        return _record_failed_commit_collection(
            root,
            config,
            context,
            error,
            collected_date,
            attempts,
            manual_review,
            dry_run,
        )
    candidates = tuple(context.get("candidates", ()))
    failed_group = tuple(context.get("group", candidates))
    changes = tuple(context.get("changes", ()))
    if not changes:
        package_contexts = tuple(context.get("package_contexts", ()))
        changes = tuple(_failure_change(root, item) for item in package_contexts)
    if not changes and failed_group:
        history = _load_retained_history(root, config)
        changes = tuple(
            _candidate_failure_change(candidate, history) for candidate in failed_group
        )
    work_ids: Tuple[str, ...] = ()
    state = "needs_manual_review" if manual_review else "collection_failed"
    if failed_group and changes:
        sha = failed_group[0].commit_sha
        same_sha = tuple(candidate for candidate in failed_group if candidate.commit_sha == sha)
        release_ids = {_release_id(candidate) for candidate in same_sha}
        grouped_changes = tuple(
            change for change in changes if change.release_id in release_ids
        )
        item = build_work_item(
            config.id,
            sha,
            collected_date,
            grouped_changes,
            str(context.get("snapshot_manifest", "")),
        )
        saved = record_collection_failure(
            root / WORK_ITEMS_PATH,
            item,
            _bounded_error(error),
            collected_date,
            attempts,
        )
        failed = next(value for value in saved if value.work_item_id == item.work_item_id)
        if manual_review and failed.state == "collection_failed":
            saved = transition_work_item(
                root / WORK_ITEMS_PATH,
                failed.work_item_id,
                "collection_failed",
                "needs_manual_review",
            )
            failed = next(value for value in saved if value.work_item_id == item.work_item_id)
        state = failed.state
        work_ids = (failed.work_item_id,)
        regenerate_status(root)
    return CollectionResult(
        config.id,
        state,
        tuple(_release_id(candidate) for candidate in candidates),
        (),
        work_ids,
        (_bounded_error(error),),
    )


def _record_failed_commit_collection(
    root: Path,
    config: RepoConfig,
    context: Dict[str, object],
    error: Exception,
    collected_date: str,
    attempts: int,
    manual_review: bool,
    dry_run: bool,
) -> CommitCollectionResult:
    ref_context = context.get("commit_ref")
    inventory = context.get("inventory")
    if not isinstance(inventory, CommitInventory):
        inventory = CommitInventory(0, 0, 0, 0)
    state = "needs_manual_review" if manual_review else "collection_failed"
    ref_ids: Tuple[str, ...] = ()
    work_ids: Tuple[str, ...] = ()
    if isinstance(ref_context, tuple) and len(ref_context) == 3:
        ref_name, sha, ref_id = ref_context
        ref_ids = (str(ref_id),)
        if not dry_run:
            change = context.get("ref_change")
            if not isinstance(change, RefChange):
                prior = context.get("prior_ref")
                from_sha = prior.sha if isinstance(prior, WorkItem) else ""
                mode, reasons = recommend_ref_ingest_mode(
                    RefChangeSignals(from_sha, str(sha), ())
                )
                change = RefChange(
                    "default-branch",
                    str(ref_name),
                    from_sha,
                    str(sha),
                    str(ref_id),
                    "",
                    mode,
                    reasons,
                )
            item = build_ref_work_item(
                config.id,
                str(sha),
                collected_date,
                (change,),
                str(context.get("snapshot_manifest", "")),
            )
            saved = record_collection_failure(
                root / WORK_ITEMS_PATH,
                item,
                _bounded_error(error),
                collected_date,
                attempts,
            )
            failed = next(value for value in saved if value.work_item_id == item.work_item_id)
            if manual_review and failed.state == "collection_failed":
                saved = transition_work_item(
                    root / WORK_ITEMS_PATH,
                    failed.work_item_id,
                    "collection_failed",
                    "needs_manual_review",
                )
                failed = next(value for value in saved if value.work_item_id == item.work_item_id)
            state = failed.state
            work_ids = (failed.work_item_id,)
            regenerate_status(root)
    return CommitCollectionResult(
        config.id,
        state,
        ref_ids,
        (),
        work_ids,
        (_bounded_error(error),),
        inventory,
    )


def _failure_change(root: Path, context: _PackageContext) -> PackageChange:
    prior_version = context.prior.version if context.prior is not None else ""
    notes = (
        context.evidence.content.decode("utf-8", errors="replace")
        if context.evidence is not None
        else ""
    )
    mode, reasons = recommend_ingest_mode(
        ChangeSignals(
            context.candidate.package,
            prior_version,
            context.candidate.version,
            context.changed_paths,
            context.public_exports_changed,
            notes,
        )
    )
    return PackageChange(
        context.candidate.package,
        prior_version,
        context.candidate.version,
        _release_id(context.candidate),
        (
            _relative(root, context.release_record.manifest_path)
            if context.release_record is not None
            else ""
        ),
        "",
        mode,
        reasons,
    )


def _candidate_failure_change(
    candidate: ReleaseCandidate,
    history: Dict[str, List[_RetainedRelease]],
) -> PackageChange:
    prior = _latest_prior(history.get(candidate.package, ()), candidate.version)
    prior_version = prior.version if prior is not None else ""
    mode, reasons = recommend_ingest_mode(
        ChangeSignals(
            candidate.package,
            prior_version,
            candidate.version,
            (),
            False,
            "",
        )
    )
    return PackageChange(
        candidate.package,
        prior_version,
        candidate.version,
        _release_id(candidate),
        "",
        "",
        mode,
        reasons,
    )


def approve_one(root: Path, work_item_id: str, mode: str) -> WorkItem:
    """Record explicit user approval without starting ingest."""
    root = Path(root).resolve()
    current = next(
        (
            item
            for item in load_work_items(root / WORK_ITEMS_PATH)
            if item.work_item_id == work_item_id
        ),
        None,
    )
    if current is None:
        raise WorkItemStateError("work item was not found")
    ingest_required_reading(root, current)
    items = transition_work_item(
        root / WORK_ITEMS_PATH,
        work_item_id,
        "awaiting_approval",
        "approved",
        approved_mode=mode,
    )
    regenerate_status(root)
    return next(item for item in items if item.work_item_id == work_item_id)


def next_ingest(root: Path) -> WorkItem:
    """Atomically claim and return the oldest approved ingest item."""
    selected = claim_next_ingest(Path(root).resolve() / WORK_ITEMS_PATH)
    regenerate_status(root)
    return selected


def ingest_required_reading(root: Path, item: WorkItem) -> Tuple[str, ...]:
    """Return the packet and attached evidence required for serial ingest."""
    if not item.ingest_packet:
        raise ValueError("ingest item has no packet")
    reading = (
        *load_packet_required_reading(root, item.ingest_packet),
        *evidence_attachment_required_reading(root, item),
    )
    if len(reading) != len(set(reading)):
        raise ValueError("ingest required reading contains duplicates")
    return tuple(reading)


def complete_ingest(root: Path, work_item_id: str) -> WorkItem:
    """Record successful completion of the currently claimed ingest."""
    items = transition_work_item(
        Path(root).resolve() / WORK_ITEMS_PATH,
        work_item_id,
        "ingesting",
        "ingested",
    )
    regenerate_status(root)
    return next(item for item in items if item.work_item_id == work_item_id)


def fail_ingest(root: Path, work_item_id: str, error: str) -> WorkItem:
    """Stop the claimed ingest and require manual review."""
    items = record_ingest_failure(
        Path(root).resolve() / WORK_ITEMS_PATH,
        work_item_id,
        error,
        date.today().isoformat(),
    )
    regenerate_status(root)
    return next(item for item in items if item.work_item_id == work_item_id)


def retry_one(root: Path, work_item_id: str) -> WorkItem:
    """Return one failed item to discovered for an explicit recollection."""
    path = Path(root).resolve() / WORK_ITEMS_PATH
    items = load_work_items(path)
    current = next((item for item in items if item.work_item_id == work_item_id), None)
    if current is None or current.state not in ("collection_failed", "needs_manual_review"):
        raise WorkItemStateError("retry requires collection_failed or needs_manual_review")
    updated = transition_work_item(
        path, work_item_id, current.state, "discovered"
    )
    regenerate_status(root)
    return next(item for item in updated if item.work_item_id == work_item_id)


def compare_one(
    root: Path,
    config: RepoConfig,
    from_release: str,
    to_release: str,
    clone_source: Optional[Path] = None,
) -> ComparisonRecord:
    """Generate a package-scoped comparison for two collected releases."""
    package, from_version = parse_package_release(from_release, to_release)
    _, to_version = parse_package_release(to_release)
    history = _load_retained_history(Path(root).resolve(), config).get(package, [])
    prior = next((item for item in history if item.version == from_version), None)
    current = next((item for item in history if item.version == to_version), None)
    if prior is None or current is None:
        raise CollectionUsageError("both package releases must already be collected")
    effective = replace(config, url=str(clone_source)) if clone_source is not None else config
    with tempfile.TemporaryDirectory(prefix="wiki-github-compare-") as temporary:
        clone_path = Path(temporary) / "repository"
        clone_repository(effective, clone_path)
        fetch_required_refs(
            effective, clone_path, ("tag:" + prior.tag, "tag:" + current.tag)
        )
        capsule = _one_capsule(config)
        prior_package = _workspace_package(
            resolve_capsule_workspace(
                GitTree(clone_path, prior.sha, config.max_file_bytes),
                capsule,
                {package: from_version},
            ).packages,
            package,
        )
        current_package = _workspace_package(
            resolve_capsule_workspace(
                GitTree(clone_path, current.sha, config.max_file_bytes),
                capsule,
                {package: to_version},
            ).packages,
            package,
        )
        from_paths = (
            _tagged_pathspecs(prior_package)
            if capsule.adapter == TAGGED_TREE_ADAPTER
            else _package_pathspecs(prior_package)
        )
        to_paths = (
            _tagged_pathspecs(current_package)
            if capsule.adapter == TAGGED_TREE_ADAPTER
            else _package_pathspecs(current_package)
        )
        comparison = write_package_comparison(
            Path(root).resolve(),
            config,
            clone_path,
            package,
            from_version,
            prior.sha,
            from_paths,
            to_version,
            current.sha,
            to_paths,
        )
        packet = build_ingest_packet(
            Path(root).resolve(),
            config,
            "",
            _snapshot_manifest_for_sha(Path(root).resolve(), config, current.sha),
            (
                PackagePacketInput(
                    package,
                    from_version,
                    to_version,
                    prior.sha,
                    current.sha,
                    current.release_manifest,
                    _relative(Path(root).resolve(), comparison.metadata_path),
                    _snapshot_manifest_for_sha(
                        Path(root).resolve(), config, prior.sha
                    ),
                    read_upstream_changes(clone_path, prior.sha, current.sha),
                ),
            ),
            "ad-hoc",
        )
        publish_review_packet(comparison.metadata_path.parent, packet)
        return comparison


def supplement_one(
    root: Path,
    config: RepoConfig,
    sha: str,
    paths: Sequence[str],
    clone_source: Optional[Path] = None,
    collection_date: Optional[str] = None,
):
    """Collect explicitly approved text paths from one exact commit."""
    root = Path(root).resolve()
    effective = replace(config, url=str(clone_source)) if clone_source is not None else config
    with tempfile.TemporaryDirectory(prefix="wiki-github-supplement-") as temporary:
        clone_path = Path(temporary) / "repository"
        clone_repository(effective, clone_path)
        fetch_required_refs(effective, clone_path, ("commit:" + sha,))
        tree = GitTree(clone_path, sha, config.max_file_bytes)
        return publish_source_supplement(
            root,
            config,
            tree,
            paths,
            collection_date or date.today().isoformat(),
        )


def regenerate_status(root: Path) -> str:
    """Regenerate operator Markdown from the machine queue."""
    root = Path(root).resolve()
    rendered = write_status_from_queue(
        root / WORK_ITEMS_PATH,
        root / STATUS_PATH,
        _packet_status_summaries(root),
    )
    if (root / "tracking/github/repo-registry.toml").exists():
        regenerate_collection_index(root)
    return rendered


def regenerate_collection_index(
    root: Path,
    checked_update: Optional[Dict[str, Dict[str, str]]] = None,
    generated_date: Optional[str] = None,
) -> dict:
    """Regenerate repository-level scheduling state from registry and queue."""
    root = Path(root).resolve()
    checked = {}
    try:
        checked = checked_state_from_document(load_collection_index(root))
    except (OSError, UnicodeError, ValueError, TypeError, json.JSONDecodeError):
        pass
    for repo_id, values in (checked_update or {}).items():
        checked[repo_id] = {**checked.get(repo_id, {}), **values}
    return write_collection_index(
        root,
        load_registry(root / "tracking/github/repo-registry.toml"),
        load_work_items(root / WORK_ITEMS_PATH),
        checked,
        date.fromisoformat(generated_date) if generated_date else date.today(),
    )


def _checked_update(
    repo_id: str,
    result: Union[CollectionResult, CommitCollectionResult],
    checked_date: str,
) -> Dict[str, Dict[str, str]]:
    identities = result.ref_ids if isinstance(result, CommitCollectionResult) else result.release_ids
    return {
        repo_id: {
            "last_checked_date": checked_date,
            "latest_discovered_ref": ", ".join(identities),
            "last_error": " ".join(result.errors)[:240],
        }
    }


def _packet_status_summaries(
    root: Path,
) -> Dict[str, PacketStatusSummary]:
    summaries = {}
    for item in load_work_items(root / WORK_ITEMS_PATH):
        if not item.ingest_packet:
            continue
        summary = load_packet_summary(root, item.ingest_packet)
        attachment_reading = evidence_attachment_required_reading(root, item)
        summaries[item.work_item_id] = PacketStatusSummary(
            summary.packet_path,
            summary.priority,
            summary.required_reading_count + len(attachment_reading),
            summary.unclassified_count,
            summary.evidence_gap_count,
        )
    return summaries


def parse_package_release(
    value: str, other: Optional[str] = None
) -> Tuple[str, str]:
    """Require an exact package-qualified semantic release identity."""
    parsed = parse_package_tag(value) if isinstance(value, str) else None
    if parsed is None:
        raise CollectionUsageError("release must be package-qualified")
    version = parse_semver(parsed[1])
    if version is None or not version.is_exact:
        raise CollectionUsageError("release must use an exact semantic version")
    if other is not None:
        compared = parse_package_release(other)
        if parsed[0] != compared[0]:
            raise CollectionUsageError("comparison releases must use the same package")
    return parsed


def _sort_candidates(
    candidates: Sequence[ReleaseCandidate],
    evidence: Dict[str, Optional[ReleaseNotesEvidence]],
    clone_path: Path,
) -> Tuple[ReleaseCandidate, ...]:
    commit_dates: Dict[str, str] = {}

    def key(candidate: ReleaseCandidate) -> Tuple[object, ...]:
        notes = evidence[_release_id(candidate)]
        if candidate.commit_sha not in commit_dates:
            commit_dates[candidate.commit_sha] = run_git(
                ["show", "-s", "--format=%cI", candidate.commit_sha], clone_path
            )
        return (
            notes.published_at if notes is not None else commit_dates[candidate.commit_sha],
            candidate.package,
            _semver_key(candidate.version),
            candidate.tag,
        )

    return tuple(sorted(candidates, key=key))


def _group_by_sha(
    candidates: Sequence[ReleaseCandidate],
) -> Tuple[Tuple[ReleaseCandidate, ...], ...]:
    groups: Dict[str, List[ReleaseCandidate]] = {}
    order = []
    for candidate in candidates:
        if candidate.commit_sha not in groups:
            groups[candidate.commit_sha] = []
            order.append(candidate.commit_sha)
        groups[candidate.commit_sha].append(candidate)
    return tuple(tuple(groups[sha]) for sha in order)


def _existing_release_ids(items: Sequence[WorkItem]) -> set:
    return {
        change.release_id
        for item in items
        for change in item.package_changes
        if item.state not in (
            "collection_failed",
            "discovered",
            "needs_manual_review",
        )
    }


def _changed_candidates(
    root: Path,
    candidates: Sequence[ReleaseCandidate],
    evidence_by_id: Dict[str, Optional[ReleaseNotesEvidence]],
    history: Dict[str, List[_RetainedRelease]],
    items: Sequence[WorkItem],
) -> Tuple[Tuple[ReleaseCandidate, ...], set]:
    accepted_paths = {
        change.release_manifest
        for item in items
        for change in item.package_changes
        if item.state not in (
            "collection_failed",
            "discovered",
            "needs_manual_review",
        )
        and change.release_manifest
    }
    accepted: Dict[str, List[_RetainedRelease]] = {}
    for rows in history.values():
        for retained in rows:
            if retained.release_manifest in accepted_paths:
                accepted.setdefault(
                    retained.package + "@" + retained.version, []
                ).append(retained)
    changed = []
    revised = set()
    for candidate in candidates:
        release_id = _release_id(candidate)
        prior = accepted.get(release_id, ())
        if prior and any(item.sha != candidate.commit_sha for item in prior):
            raise CollectionUsageError(
                "release tag moved for " + release_id + "; manual review is required"
            )
        evidence = evidence_by_id[release_id]
        notes = evidence.content if evidence is not None else b""
        notes_hash = hashlib.sha256(notes).hexdigest()
        if prior and any(item.notes_sha256 == notes_hash for item in prior):
            continue
        if prior:
            revised.add(release_id)
        changed.append(candidate)
    return tuple(changed), revised


def _verify_fetched_candidates(
    clone_path: Path, candidates: Sequence[ReleaseCandidate]
) -> None:
    for candidate in candidates:
        reference = "refs/tags/" + candidate.tag
        object_sha = run_git(["rev-parse", reference + "^{object}"], clone_path)
        commit_sha = run_git(["rev-parse", reference + "^{commit}"], clone_path)
        if object_sha != candidate.object_sha or commit_sha != candidate.commit_sha:
            raise CollectionUsageError(
                "release tag moved during collection for " + _release_id(candidate)
            )


def _load_retained_history(
    root: Path, config: RepoConfig
) -> Dict[str, List[_RetainedRelease]]:
    repository = root / "raw" / "github" / config.company / config.id.split("/", 1)[1]
    history: Dict[str, List[_RetainedRelease]] = {}
    for path in sorted((repository / "releases").glob("*/*/*/manifest.json")):
        try:
            document = json.loads(path.read_text(encoding="utf-8"))
            retained = _RetainedRelease(
                str(document["package"]),
                str(document["version"]),
                str(document["tag"]),
                str(document["sha"]),
                _relative(root, path),
                str(document["notes_sha256"]),
            )
        except (OSError, UnicodeError, json.JSONDecodeError, KeyError):
            raise CollectionUsageError("collected release manifest is invalid: " + str(path))
        history.setdefault(retained.package, []).append(retained)
    return {
        package: sorted(
            rows,
            key=lambda item: (_semver_key(item.version), item.release_manifest),
        )
        for package, rows in history.items()
    }


def _latest_prior(
    history: Sequence[_RetainedRelease], version: str
) -> Optional[_RetainedRelease]:
    target = parse_semver(version)
    if target is None:
        return None
    eligible = [
        item
        for item in history
        if parse_semver(item.version) is not None
        and compare_semver(parse_semver(item.version), target) < 0
    ]
    return max(eligible, key=lambda item: _semver_key(item.version)) if eligible else None


def _workspace_package(
    packages: Sequence[WorkspacePackage], package: str
) -> WorkspacePackage:
    matches = [item for item in packages if item.name == package]
    if len(matches) != 1:
        raise CollectionUsageError("package is not uniquely present at release SHA: " + package)
    return matches[0]


def _package_changed_paths(
    clone_path: Path,
    from_sha: str,
    to_sha: str,
    prior: WorkspacePackage,
    current: WorkspacePackage,
) -> Tuple[str, ...]:
    output = run_git(["diff", "--name-only", from_sha, to_sha, "--"], clone_path)
    roots = tuple(path for path in (prior.path, current.path) if path)
    if not roots:
        return tuple(sorted(line for line in output.splitlines() if line))
    return tuple(
        sorted(
            line
            for line in output.splitlines()
            if line and any(line == root or line.startswith(root + "/") for root in roots)
        )
    )


def _package_pathspecs(package: WorkspacePackage) -> Tuple[str, ...]:
    if package.path:
        return (package.path,)
    roots = sorted({path.split("/", 1)[0] for path in package.owned_paths if path})
    if not roots:
        raise CollectionUsageError("root package has no bounded comparison paths")
    return tuple(roots)


def _tagged_changed_paths(
    clone_path: Path,
    from_sha: str,
    to_sha: str,
    prior: WorkspacePackage,
    current: WorkspacePackage,
) -> Tuple[str, ...]:
    output = run_git(["diff", "--name-only", from_sha, to_sha, "--"], clone_path)
    owned = frozenset(prior.owned_paths).union(current.owned_paths)
    return tuple(
        sorted(path for path in output.splitlines() if path and path in owned)
    )


def _tagged_pathspecs(package: WorkspacePackage) -> Tuple[str, ...]:
    if package.path:
        raise CollectionUsageError("tagged tree package must use the repository root")
    if not package.owned_paths:
        raise CollectionUsageError("tagged tree package has no bounded comparison paths")
    return tuple(sorted(package.owned_paths))


def _public_exports(tree: GitTree, package: WorkspacePackage) -> dict:
    path = (package.path + "/" if package.path else "") + "package.json"
    manifest = tree.read_json(path)
    return {field: manifest.get(field) for field in PUBLIC_EXPORT_FIELDS if field in manifest}


def _one_capsule(config: RepoConfig):
    if len(config.capsules) != 1:
        raise CollectionUsageError("focused pilot requires exactly one capsule policy")
    return config.capsules[0]


def _retained_from_record(record: PackageReleaseRecord) -> _RetainedRelease:
    return _RetainedRelease(
        record.package,
        record.version,
        record.tag,
        record.sha,
        record.manifest_path.as_posix(),
        record.notes_sha256,
    )


def _release_id(candidate: ReleaseCandidate) -> str:
    return candidate.package + "@" + candidate.version


def _track_package(track: VersionTrack) -> str:
    if not track.selector.startswith("package:"):
        return ""
    parsed = parse_package_tag(track.selector[8:])
    return parsed[0] if parsed is not None else ""


def _semver_key(value: str) -> Tuple[object, ...]:
    parsed = parse_semver(value)
    if parsed is None:
        raise CollectionUsageError("invalid retained semantic version " + value)
    return (parsed.major, parsed.minor or 0, parsed.patch or 0, parsed.prerelease or ())


def _relative(root: Path, path: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        raise CollectionUsageError("artifact path escapes the wiki root") from None


def _snapshot_manifest_for_sha(
    root: Path,
    config: RepoConfig,
    sha: str,
) -> str:
    repository = config.id.split("/", 1)[1]
    snapshot_root = (
        Path(root)
        / "raw"
        / "github"
        / config.company
        / repository
        / "snapshots"
    )
    matches = []
    for path in sorted(snapshot_root.glob("*/manifest.json")):
        try:
            document = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError):
            continue
        if document.get("repository") == config.id and document.get("sha") == sha:
            matches.append(path)
    if len(matches) != 1:
        raise CollectionUsageError(
            "exactly one retained snapshot is required for SHA " + sha
        )
    return _relative(Path(root).resolve(), matches[0])


def _bounded_error(error: Exception) -> str:
    text = str(error).strip() or error.__class__.__name__
    return text[:1000] + ("..." if len(text) > 1000 else "")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="collect_github_repos.py")
    commands = parser.add_subparsers(dest="command", required=True)

    collect = commands.add_parser("collect")
    collect.add_argument("--repo", required=True)
    selection = collect.add_mutually_exclusive_group(required=True)
    selection.add_argument("--mode", dest="release_mode", choices=("backfill", "future"))
    selection.add_argument("--release")
    collect.add_argument("--dry-run", action="store_true")

    collect_ref = commands.add_parser("collect-ref")
    collect_ref.add_argument("--repo", required=True)
    collect_ref.add_argument("--from", dest="from_sha", required=True)
    collect_ref.add_argument("--to", dest="to_sha", required=True)
    collect_ref.add_argument("--dry-run", action="store_true")

    commands.add_parser("status")

    compare = commands.add_parser("compare")
    compare.add_argument("--repo", required=True)
    compare.add_argument("--from", dest="from_release", required=True)
    compare.add_argument("--to", dest="to_release", required=True)

    supplement = commands.add_parser("supplement")
    supplement.add_argument("--repo", required=True)
    supplement.add_argument("--sha", required=True)
    supplement.add_argument("--path", dest="paths", action="append", required=True)

    approve = commands.add_parser("approve")
    approve.add_argument("--item", required=True)
    approve.add_argument("--mode", choices=("full", "delta"), required=True)

    commands.add_parser("next-ingest")

    complete = commands.add_parser("complete-ingest")
    complete.add_argument("--item", required=True)

    failed = commands.add_parser("fail-ingest")
    failed.add_argument("--item", required=True)
    failed.add_argument("--error", required=True)

    retry = commands.add_parser("retry")
    retry.add_argument("--item", required=True)
    return parser


def _config(repos: Sequence[RepoConfig], repo_id: str) -> RepoConfig:
    matches = [repo for repo in repos if repo.id == repo_id]
    if len(matches) != 1:
        raise CollectionUsageError("unknown repository " + repo_id)
    return matches[0]


def _collection_result_payload(
    result: Union[CollectionResult, CommitCollectionResult]
) -> dict:
    if isinstance(result, CollectionResult):
        return asdict(result)
    if isinstance(result, CommitCollectionResult):
        return asdict(result)
    raise TypeError("result must be a collection result")


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = _parser()
    arguments = parser.parse_args(argv)
    root = PROJECT_ROOT
    try:
        if arguments.command == "status":
            print(regenerate_status(root), end="")
            return 0
        if arguments.command == "approve":
            print(json.dumps(asdict(approve_one(root, arguments.item, arguments.mode)), sort_keys=True))
            return 0
        if arguments.command == "next-ingest":
            item = next_ingest(root)
            payload = asdict(item)
            if item.ingest_packet:
                payload["packet_summary"] = asdict(
                    load_packet_summary(root, item.ingest_packet)
                )
                payload["required_reading"] = list(
                    ingest_required_reading(root, item)
                )
            print(json.dumps(payload, sort_keys=True))
            return 0
        if arguments.command == "complete-ingest":
            print(json.dumps(asdict(complete_ingest(root, arguments.item)), sort_keys=True))
            return 0
        if arguments.command == "fail-ingest":
            print(json.dumps(asdict(fail_ingest(root, arguments.item, arguments.error)), sort_keys=True))
            return 0
        if arguments.command == "retry":
            print(json.dumps(asdict(retry_one(root, arguments.item)), sort_keys=True))
            return 0

        repos = load_registry(root / "tracking/github/repo-registry.toml")
        config = _config(repos, arguments.repo)
        if arguments.command == "supplement":
            record = supplement_one(
                root,
                config,
                arguments.sha,
                tuple(arguments.paths),
            )
            print(json.dumps(asdict(record), sort_keys=True, default=str))
            return 0
        if arguments.command == "compare":
            parse_package_release(arguments.from_release, arguments.to_release)
            record = compare_one(
                root, config, arguments.from_release, arguments.to_release
            )
            print(json.dumps(asdict(record), sort_keys=True, default=str))
            return 0
        if arguments.command == "collect-ref":
            result = collect_ref_boundary(
                root,
                config,
                arguments.from_sha,
                arguments.to_sha,
                dry_run=arguments.dry_run,
            )
            print(json.dumps(_collection_result_payload(result), sort_keys=True))
            return 1 if result.state in ("collection_failed", "needs_manual_review") else 0
        result = collect_one(
            root,
            config,
            release_mode=arguments.release_mode,
            release=arguments.release,
            dry_run=arguments.dry_run,
        )
        print(json.dumps(_collection_result_payload(result), sort_keys=True))
        return 1 if result.state in ("collection_failed", "needs_manual_review") else 0
    except (CollectionUsageError, ValueError, WorkItemStateError) as error:
        parser.error(str(error))
    return 2


__all__ = [
    "CommitCollectionResult",
    "CommitInventory",
    "CollectionResult",
    "CollectionUsageError",
    "approve_one",
    "collect_one",
    "collect_ref_boundary",
    "complete_ingest",
    "compare_one",
    "main",
    "fail_ingest",
    "next_ingest",
    "parse_package_release",
    "regenerate_status",
    "regenerate_collection_index",
    "retry_one",
    "supplement_one",
]


if __name__ == "__main__":
    raise SystemExit(main())
