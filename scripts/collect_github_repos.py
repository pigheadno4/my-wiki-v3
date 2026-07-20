"""Focused release-driven collection for the GitHub repository pilot."""

import argparse
from dataclasses import asdict, dataclass, replace
from datetime import date
import json
import os
from pathlib import Path
import tempfile
from typing import Callable, Dict, List, Optional, Sequence, Tuple
from urllib.error import URLError

from github_capsule_selection import resolve_npm_capsule
from github_git import GitCommandError, clone_repository, fetch_required_refs, run_git
from github_git_tree import GitObjectReadError, GitTree
from github_npm_workspace import WorkspacePackage, resolve_workspace
from github_pilot_store import (
    ComparisonRecord,
    PackageReleaseRecord,
    package_slug,
    publish_release_record,
    publish_source_snapshot,
    write_package_comparison,
)
from github_registry import RepoConfig, VersionTrack, load_registry
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
    PackageChange,
    WorkItem,
    WorkItemStateError,
    build_work_item,
    load_work_items,
    recommend_ingest_mode,
    record_collection_failure,
    render_status,
    transition_work_item,
    upsert_discovered_work_item,
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
class _RetainedRelease:
    package: str
    version: str
    tag: str
    sha: str
    release_manifest: str


@dataclass(frozen=True)
class _PackageContext:
    candidate: ReleaseCandidate
    evidence: Optional[ReleaseNotesEvidence]
    release_record: PackageReleaseRecord
    prior: Optional[_RetainedRelease]
    changed_paths: Tuple[str, ...]
    from_paths: Tuple[str, ...]
    to_paths: Tuple[str, ...]
    public_exports_changed: bool


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
) -> CollectionResult:
    """Collect retained package releases and create approval-gated work items."""
    if release_mode not in (None, "backfill", "future"):
        raise CollectionUsageError("release mode must be backfill or future")
    if (release_mode is None) == (release is None):
        raise CollectionUsageError("choose exactly one release mode or exact package release")
    if not isinstance(max_attempts, int) or not 1 <= max_attempts <= 3:
        raise CollectionUsageError("max_attempts must be between one and three")
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
                root, config, context, error, collected, attempt, manual_review=True
            )
        else:
            if not dry_run:
                regenerate_status(root)
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
    )
    if not dry_run and queue_path.exists():
        regenerate_status(root)
    return result


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
            return CollectionResult(config.id, "unchanged", (), (), (), ())
        release_ids = tuple(_release_id(candidate) for candidate in candidates)
        if dry_run:
            return CollectionResult(config.id, "discovered", release_ids, (), (), ())

        history = _load_retained_history(root, config)
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
        evidence_by_id = {
            _release_id(candidate): release_notes_fetcher(config, candidate)
            for candidate in candidates
        }
        ordered = _sort_candidates(candidates, evidence_by_id)
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
            )
            context["package_contexts"] = package_contexts
            tree = GitTree(clone_path, group[0].commit_sha, config.max_file_bytes)
            capsule = _one_capsule(config)
            changed_paths = tuple(
                sorted({path for item in package_contexts for path in item.changed_paths})
            )
            resolution = resolve_npm_capsule(
                tree, capsule, config.secret_allowlist, changed_paths=changed_paths
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
            changes = tuple(
                _publish_comparison_and_change(root, config, clone_path, item)
                for item in package_contexts
            )
            context["changes"] = changes
            work_item = build_work_item(
                config.id,
                group[0].commit_sha,
                collected_date,
                changes,
                snapshot_manifest,
            )
            current = next(
                (
                    item
                    for item in load_work_items(root / WORK_ITEMS_PATH)
                    if item.work_item_id == work_item.work_item_id
                ),
                None,
            )
            if current is not None and current.state == "collection_failed":
                transition_work_item(
                    root / WORK_ITEMS_PATH,
                    current.work_item_id,
                    "collection_failed",
                    "discovered",
                )
            items = upsert_discovered_work_item(root / WORK_ITEMS_PATH, work_item)
            current = next(item for item in items if item.work_item_id == work_item.work_item_id)
            if current.state == "discovered":
                transition_work_item(
                    root / WORK_ITEMS_PATH,
                    current.work_item_id,
                    "discovered",
                    "collected",
                )
                transition_work_item(
                    root / WORK_ITEMS_PATH,
                    current.work_item_id,
                    "collected",
                    "awaiting_approval",
                )
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
            selected = select_release_candidates(
                track, rows, existing_versions=versions, mode=release_mode or "backfill"
            )
        for candidate in selected:
            identity = _release_id(candidate)
            if identity in existing:
                continue
            prior = discovered.get(identity)
            if prior is not None and prior.commit_sha != candidate.commit_sha:
                raise CollectionUsageError("release identity resolves to conflicting SHAs")
            discovered[identity] = candidate
    if release is not None and release not in discovered and release not in existing:
        raise CollectionUsageError("configured tracks do not contain exact release " + release)
    return tuple(discovered[key] for key in sorted(discovered))


def _prepare_group(
    root: Path,
    config: RepoConfig,
    clone_path: Path,
    group: Sequence[ReleaseCandidate],
    evidence_by_id: Dict[str, Optional[ReleaseNotesEvidence]],
    history: Dict[str, List[_RetainedRelease]],
    collected_date: str,
) -> Tuple[_PackageContext, ...]:
    capsule = _one_capsule(config)
    current_tree = GitTree(clone_path, group[0].commit_sha, config.max_file_bytes)
    current_workspace = resolve_workspace(current_tree, capsule)
    contexts = []
    for candidate in sorted(group, key=lambda item: item.package):
        evidence = evidence_by_id[_release_id(candidate)]
        release_date = (
            evidence.published_at
            if evidence is not None
            else run_git(["show", "-s", "--format=%cI", candidate.commit_sha], clone_path)
        )
        record = publish_release_record(
            root, config, candidate, release_date, evidence, collected_date
        )
        prior = _latest_prior(history.get(candidate.package, ()), candidate.version)
        current_package = _workspace_package(current_workspace.packages, candidate.package)
        if prior is None:
            changed_paths = ()
            from_paths = ()
            exports_changed = False
        else:
            prior_tree = GitTree(clone_path, prior.sha, config.max_file_bytes)
            prior_workspace = resolve_workspace(prior_tree, capsule)
            prior_package = _workspace_package(prior_workspace.packages, candidate.package)
            changed_paths = _package_changed_paths(
                clone_path,
                prior.sha,
                candidate.commit_sha,
                prior_package,
                current_package,
            )
            from_paths = _package_pathspecs(prior_package)
            exports_changed = _public_exports(prior_tree, prior_package) != _public_exports(
                current_tree, current_package
            )
        contexts.append(
            _PackageContext(
                candidate,
                evidence,
                record,
                prior,
                changed_paths,
                from_paths,
                _package_pathspecs(current_package),
                exports_changed,
            )
        )
    return tuple(contexts)


def _publish_comparison_and_change(
    root: Path,
    config: RepoConfig,
    clone_path: Path,
    context: _PackageContext,
) -> PackageChange:
    comparison: Optional[ComparisonRecord] = None
    prior_version = context.prior.version if context.prior is not None else ""
    if context.prior is not None:
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


def _record_failed_collection(
    root: Path,
    config: RepoConfig,
    context: Dict[str, object],
    error: Exception,
    collected_date: str,
    attempts: int,
    manual_review: bool,
) -> CollectionResult:
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
        _relative(root, context.release_record.manifest_path),
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
    items = transition_work_item(
        Path(root).resolve() / WORK_ITEMS_PATH,
        work_item_id,
        "awaiting_approval",
        "approved",
        approved_mode=mode,
    )
    regenerate_status(root)
    return next(item for item in items if item.work_item_id == work_item_id)


def next_ingest(root: Path) -> WorkItem:
    """Return the oldest approved item without changing its state."""
    approved = [
        item
        for item in load_work_items(Path(root).resolve() / WORK_ITEMS_PATH)
        if item.state == "approved"
    ]
    if not approved:
        raise WorkItemStateError("no approved GitHub ingest item is available")
    return min(approved, key=lambda item: (item.collection_date, item.work_item_id))


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
            resolve_workspace(
                GitTree(clone_path, prior.sha, config.max_file_bytes), capsule
            ).packages,
            package,
        )
        current_package = _workspace_package(
            resolve_workspace(
                GitTree(clone_path, current.sha, config.max_file_bytes), capsule
            ).packages,
            package,
        )
        return write_package_comparison(
            Path(root).resolve(),
            config,
            clone_path,
            package,
            from_version,
            prior.sha,
            _package_pathspecs(prior_package),
            to_version,
            current.sha,
            _package_pathspecs(current_package),
        )


def regenerate_status(root: Path) -> str:
    """Regenerate operator Markdown from the machine queue."""
    root = Path(root).resolve()
    status = render_status(load_work_items(root / WORK_ITEMS_PATH))
    _write_text_atomic(root / STATUS_PATH, status)
    return status


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
) -> Tuple[ReleaseCandidate, ...]:
    def key(candidate: ReleaseCandidate) -> Tuple[object, ...]:
        version = parse_semver(candidate.version)
        if version is None:
            raise CollectionUsageError("candidate version is not semantic")
        notes = evidence[_release_id(candidate)]
        return (
            version.major,
            version.minor or 0,
            version.patch or 0,
            notes.published_at if notes is not None else "",
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
        if item.state not in ("collection_failed", "discovered")
    }


def _load_retained_history(
    root: Path, config: RepoConfig
) -> Dict[str, List[_RetainedRelease]]:
    repository = root / "raw" / "github" / config.company / config.id.split("/", 1)[1]
    history: Dict[str, Dict[Tuple[str, str], _RetainedRelease]] = {}
    for path in sorted((repository / "releases").glob("*/*/*/manifest.json")):
        try:
            document = json.loads(path.read_text(encoding="utf-8"))
            retained = _RetainedRelease(
                str(document["package"]),
                str(document["version"]),
                str(document["tag"]),
                str(document["sha"]),
                _relative(root, path),
            )
        except (OSError, UnicodeError, json.JSONDecodeError, KeyError):
            raise CollectionUsageError("collected release manifest is invalid: " + str(path))
        history.setdefault(retained.package, {})[(retained.version, retained.sha)] = retained
    return {
        package: sorted(rows.values(), key=lambda item: _semver_key(item.version))
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


def _bounded_error(error: Exception) -> str:
    text = str(error).strip() or error.__class__.__name__
    return text[:1000] + ("..." if len(text) > 1000 else "")


def _write_text_atomic(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=".tmp-", dir=str(path.parent))
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as output:
            output.write(content)
            output.flush()
            os.fsync(output.fileno())
        os.replace(temporary, str(path))
    except Exception:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="collect_github_repos.py")
    commands = parser.add_subparsers(dest="command", required=True)

    collect = commands.add_parser("collect")
    collect.add_argument("--repo", required=True)
    selection = collect.add_mutually_exclusive_group(required=True)
    selection.add_argument("--mode", dest="release_mode", choices=("backfill", "future"))
    selection.add_argument("--release")
    collect.add_argument("--dry-run", action="store_true")

    commands.add_parser("status")

    compare = commands.add_parser("compare")
    compare.add_argument("--repo", required=True)
    compare.add_argument("--from", dest="from_release", required=True)
    compare.add_argument("--to", dest="to_release", required=True)

    approve = commands.add_parser("approve")
    approve.add_argument("--item", required=True)
    approve.add_argument("--mode", choices=("full", "delta"), required=True)

    commands.add_parser("next-ingest")

    retry = commands.add_parser("retry")
    retry.add_argument("--item", required=True)
    return parser


def _config(repos: Sequence[RepoConfig], repo_id: str) -> RepoConfig:
    matches = [repo for repo in repos if repo.id == repo_id]
    if len(matches) != 1:
        raise CollectionUsageError("unknown repository " + repo_id)
    return matches[0]


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
            print(json.dumps(asdict(next_ingest(root)), sort_keys=True))
            return 0
        if arguments.command == "retry":
            print(json.dumps(asdict(retry_one(root, arguments.item)), sort_keys=True))
            return 0

        repos = load_registry(root / "tracking/github/repo-registry.toml")
        config = _config(repos, arguments.repo)
        if arguments.command == "compare":
            parse_package_release(arguments.from_release, arguments.to_release)
            record = compare_one(
                root, config, arguments.from_release, arguments.to_release
            )
            print(json.dumps(asdict(record), sort_keys=True, default=str))
            return 0
        result = collect_one(
            root,
            config,
            release_mode=arguments.release_mode,
            release=arguments.release,
            dry_run=arguments.dry_run,
        )
        print(json.dumps(asdict(result), sort_keys=True))
        return 1 if result.state in ("collection_failed", "needs_manual_review") else 0
    except (CollectionUsageError, ValueError, WorkItemStateError) as error:
        parser.error(str(error))
    return 2


__all__ = [
    "CollectionResult",
    "CollectionUsageError",
    "approve_one",
    "collect_one",
    "compare_one",
    "main",
    "next_ingest",
    "parse_package_release",
    "regenerate_status",
    "retry_one",
]


if __name__ == "__main__":
    raise SystemExit(main())
