"""Deterministic ingest recommendations and queue state for the GitHub pilot."""

from dataclasses import asdict, dataclass, replace
from contextlib import contextmanager
import fcntl
import json
import os
from pathlib import Path
import re
import tempfile
import threading
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple

from github_canonical import (
    canonical_json_bytes,
    canonical_sha256,
    safe_policy_path,
    validate_npm_package_name,
)
from github_versions import parse_semver


FULL_SIGNAL_ORDER = (
    "initial-package-baseline",
    "major-version-transition",
    "public-exports-changed",
    "security-signal",
    "sdk-initialization-signal",
    "payment-behavior-signal",
    "broad-change-set",
)
BROAD_CHANGE_FILE_LIMIT = 25
INGEST_MODES = ("full", "delta")
STATES = (
    "discovered",
    "collected",
    "awaiting_approval",
    "approved",
    "ingesting",
    "ingested",
    "collection_failed",
    "needs_manual_review",
)
TRANSITIONS = {
    "discovered": ("collected", "collection_failed", "needs_manual_review"),
    "collected": ("awaiting_approval",),
    "awaiting_approval": ("approved",),
    "approved": ("ingesting",),
    "ingesting": ("ingested", "needs_manual_review"),
    "collection_failed": ("discovered", "needs_manual_review"),
    "needs_manual_review": ("discovered",),
}

_DATE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")
_OBJECT_ID = re.compile(r"^(?:[0-9a-f]{40}|[0-9a-f]{64})$")
_WORK_ITEM_ID = re.compile(r"^github-[0-9a-f]{20}$")
_DOCUMENT_FIELDS = {"format_version", "work_items"}
_PACKAGE_CHANGE_FIELDS = {
    "package",
    "from_version",
    "to_version",
    "release_id",
    "release_manifest",
    "comparison_manifest",
    "recommended_mode",
    "reasons",
}
_WORK_ITEM_FIELDS = {
    "work_item_id",
    "repo_id",
    "sha",
    "collection_date",
    "package_changes",
    "snapshot_manifest",
    "recommended_mode",
    "approved_mode",
    "state",
    "attempts_in_run",
    "consecutive_failed_runs",
    "last_error",
    "last_attempted_date",
    "evidence_revision",
    "ingest_packet",
}
_WORK_ITEM_FIELD_SETS = (
    _WORK_ITEM_FIELDS,
    _WORK_ITEM_FIELDS - {"ingest_packet"},
    _WORK_ITEM_FIELDS - {"evidence_revision"},
    _WORK_ITEM_FIELDS - {"evidence_revision", "ingest_packet"},
)
_QUEUE_THREAD_LOCK = threading.RLock()


class WorkItemStateError(ValueError):
    """A requested ingest queue transition is invalid."""


@dataclass(frozen=True)
class ChangeSignals:
    package: str
    from_version: str
    to_version: str
    changed_paths: Tuple[str, ...]
    public_exports_changed: bool
    release_notes: str


@dataclass(frozen=True)
class PackageChange:
    package: str
    from_version: str
    to_version: str
    release_id: str
    release_manifest: str
    comparison_manifest: str
    recommended_mode: str
    reasons: Tuple[str, ...]


@dataclass(frozen=True)
class PacketStatusSummary:
    packet_path: str
    priority: str
    required_reading_count: int
    unclassified_count: int
    evidence_gap_count: int


@dataclass(frozen=True)
class WorkItem:
    work_item_id: str
    repo_id: str
    sha: str
    collection_date: str
    package_changes: Tuple[PackageChange, ...]
    snapshot_manifest: str
    recommended_mode: str
    evidence_revision: str = ""
    ingest_packet: str = ""
    approved_mode: Optional[str] = None
    state: str = "discovered"
    attempts_in_run: int = 0
    consecutive_failed_runs: int = 0
    last_error: str = ""
    last_attempted_date: str = ""


def recommend_ingest_mode(signals: ChangeSignals) -> Tuple[str, Tuple[str, ...]]:
    """Recommend full or delta ingest from ordered mechanical signals."""
    if not isinstance(signals, ChangeSignals):
        raise TypeError("signals must be ChangeSignals")
    _require_package(signals.package)
    current = parse_semver(signals.to_version)
    prior = parse_semver(signals.from_version) if signals.from_version else None
    if current is None or not current.is_exact:
        raise ValueError("to_version must be an exact semantic version")
    if signals.from_version and (prior is None or not prior.is_exact):
        raise ValueError("from_version must be an exact semantic version")
    if not isinstance(signals.public_exports_changed, bool):
        raise TypeError("public_exports_changed must be boolean")
    if not isinstance(signals.release_notes, str):
        raise TypeError("release_notes must be text")
    changed_paths = _paths(signals.changed_paths, "changed_paths")

    reasons: List[str] = []
    if prior is None:
        reasons.append("initial-package-baseline")
    elif prior.major != current.major:
        reasons.append("major-version-transition")
    if signals.public_exports_changed:
        reasons.append("public-exports-changed")
    lowered = signals.release_notes.lower()
    if "security" in lowered or "cve-" in lowered:
        reasons.append("security-signal")
    if "initialization" in lowered or "load script" in lowered:
        reasons.append("sdk-initialization-signal")
    if any(word in lowered for word in ("payment", "checkout", "vault", "venmo")):
        reasons.append("payment-behavior-signal")
    if len(changed_paths) > BROAD_CHANGE_FILE_LIMIT:
        reasons.append("broad-change-set")
    ordered = tuple(code for code in FULL_SIGNAL_ORDER if code in reasons)
    if ordered:
        return "full", ordered
    if prior is not None and prior.major == current.major:
        reason = (
            "contained-patch-release"
            if prior.minor == current.minor
            else "contained-minor-release"
        )
        return "delta", (reason,)
    return "full", ("ambiguous-version-transition",)


def build_work_item_id(
    repo_id: str,
    sha: str,
    release_ids: Sequence[str],
    evidence_revision: str = "",
) -> str:
    """Build the stable identity for one SHA-grouped release set."""
    _require_repo_id(repo_id)
    _require_sha(sha)
    normalized = tuple(sorted(set(_strings(release_ids, "release_ids"))))
    if not normalized:
        raise ValueError("release_ids must not be empty")
    payload = {"release_ids": list(normalized), "repository": repo_id, "sha": sha}
    if evidence_revision:
        if re.fullmatch(r"[0-9a-f]{64}", evidence_revision) is None:
            raise ValueError("evidence_revision must be a SHA-256 hash")
        payload["evidence_revision"] = evidence_revision
    return "github-" + canonical_sha256(payload)[:20]


def build_work_item(
    repo_id: str,
    sha: str,
    collection_date: str,
    package_changes: Sequence[PackageChange],
    snapshot_manifest: str,
    evidence_revision: str = "",
    ingest_packet: str = "",
) -> WorkItem:
    """Build one discovered work item from same-SHA package changes."""
    _require_repo_id(repo_id)
    _require_sha(sha)
    _require_date(collection_date, "collection_date")
    changes = tuple(sorted(package_changes, key=lambda item: item.release_id))
    if not changes:
        raise ValueError("package_changes must not be empty")
    if len({item.release_id for item in changes}) != len(changes):
        raise ValueError("package_changes contain duplicate release IDs")
    for change in changes:
        _validate_package_change(change)
    if snapshot_manifest:
        _require_path(snapshot_manifest, "snapshot_manifest")
    mode = "full" if any(item.recommended_mode == "full" for item in changes) else "delta"
    release_ids = tuple(item.release_id for item in changes)
    item = WorkItem(
        build_work_item_id(repo_id, sha, release_ids, evidence_revision),
        repo_id,
        sha,
        collection_date,
        changes,
        snapshot_manifest,
        mode,
        evidence_revision,
        ingest_packet,
    )
    _validate_work_item(item)
    return item


def load_work_items(path: Path) -> Tuple[WorkItem, ...]:
    """Load and strictly validate the machine-readable queue."""
    path = Path(path)
    if not path.exists():
        return ()
    try:
        document = json.loads(
            path.read_text(encoding="utf-8"), object_pairs_hook=_reject_duplicate_keys
        )
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise ValueError("work-item queue is unreadable") from error
    if not isinstance(document, dict) or set(document) != _DOCUMENT_FIELDS:
        raise ValueError("work-item queue has unknown or missing fields")
    if document["format_version"] != 1 or not isinstance(document["work_items"], list):
        raise ValueError("work-item queue format is invalid")
    items = tuple(_work_item_from_dict(row) for row in document["work_items"])
    if len({item.work_item_id for item in items}) != len(items):
        raise ValueError("work-item queue contains duplicate IDs")
    if items != tuple(sorted(items, key=lambda item: item.work_item_id)):
        raise ValueError("work-item queue is not sorted")
    return items


def save_work_items(path: Path, items: Sequence[WorkItem]) -> Tuple[WorkItem, ...]:
    """Validate and atomically replace the work-item queue."""
    with _queue_lock(path):
        return _save_work_items_unlocked(path, items)


def _save_work_items_unlocked(path: Path, items: Sequence[WorkItem]) -> Tuple[WorkItem, ...]:
    normalized = tuple(sorted(items, key=lambda item: item.work_item_id))
    if len({item.work_item_id for item in normalized}) != len(normalized):
        raise ValueError("work-item queue contains duplicate IDs")
    for item in normalized:
        _validate_work_item(item)
    document = {
        "format_version": 1,
        "work_items": [_work_item_to_dict(item) for item in normalized],
    }
    _write_atomic(Path(path), canonical_json_bytes(document) + b"\n")
    return normalized


def upsert_discovered_work_item(path: Path, item: WorkItem) -> Tuple[WorkItem, ...]:
    """Insert a discovered item without resetting an existing lifecycle."""
    _validate_work_item(item)
    with _queue_lock(path):
        items = list(load_work_items(path))
        for index, existing in enumerate(items):
            if existing.work_item_id == item.work_item_id:
                _require_same_identity(existing, item)
                if existing.state == "discovered":
                    evidence = _merge_evidence(existing, item)
                    merged = replace(
                        evidence,
                        collection_date=existing.collection_date,
                        consecutive_failed_runs=existing.consecutive_failed_runs,
                        last_error=existing.last_error,
                        last_attempted_date=existing.last_attempted_date,
                    )
                    items[index] = merged
                    return _save_work_items_unlocked(path, items)
                _require_same_evidence(existing, item)
                return tuple(items)
        if item.state != "discovered":
            raise WorkItemStateError("new work item must start in discovered state")
        items.append(item)
        return _save_work_items_unlocked(path, items)


def finalize_collected_work_item(
    path: Path,
    item: WorkItem,
) -> Tuple[WorkItem, ...]:
    """Atomically publish complete collection evidence at the approval gate."""
    _validate_work_item(item)
    if not item.ingest_packet:
        raise WorkItemStateError(
            "collection finalization requires a published ingest packet"
        )
    if item.state != "discovered":
        raise WorkItemStateError(
            "collection finalization requires discovered input"
        )
    if item.approved_mode is not None:
        raise WorkItemStateError(
            "collection finalization approved_mode must be null"
        )
    finalized_input = replace(
        item,
        state="awaiting_approval",
        approved_mode=None,
        attempts_in_run=0,
        consecutive_failed_runs=0,
        last_error="",
        last_attempted_date="",
    )
    _validate_work_item(finalized_input)

    with _queue_lock(path):
        items = list(load_work_items(path))
        matches = [
            index
            for index, value in enumerate(items)
            if value.work_item_id == item.work_item_id
        ]
        if not matches:
            items.append(finalized_input)
            return _save_work_items_unlocked(path, items)

        index = matches[0]
        existing = items[index]
        _require_same_identity(existing, item)
        if existing.approved_mode is not None:
            if existing.state == "needs_manual_review":
                raise WorkItemStateError(
                    "collection finalization cannot resume an ingest-failed work item"
                )
            raise WorkItemStateError(
                "collection finalization requires approved_mode null"
            )
        if existing.state == "awaiting_approval":
            _require_same_evidence(existing, finalized_input)
            return tuple(items)
        if existing.state not in (
            "discovered",
            "collection_failed",
            "needs_manual_review",
        ):
            raise WorkItemStateError(
                "collection finalization cannot replace state " + existing.state
            )

        evidence = _merge_evidence(existing, item)
        finalized = replace(
            evidence,
            collection_date=existing.collection_date,
            state="awaiting_approval",
            approved_mode=None,
            attempts_in_run=0,
            consecutive_failed_runs=0,
            last_error="",
            last_attempted_date="",
        )
        _validate_work_item(finalized)
        items[index] = finalized
        return _save_work_items_unlocked(path, items)


def transition_work_item(
    path: Path,
    work_item_id: str,
    expected: str,
    requested: str,
    approved_mode: Optional[str] = None,
) -> Tuple[WorkItem, ...]:
    """Apply one explicit compare-and-set lifecycle transition."""
    with _queue_lock(path):
        items = list(load_work_items(path))
        return _transition_work_item_unlocked(
            path, items, work_item_id, expected, requested, approved_mode
        )


def claim_next_ingest(path: Path) -> WorkItem:
    """Atomically claim the oldest approved work item for serial ingest."""
    with _queue_lock(path):
        items = list(load_work_items(path))
        if any(item.state == "ingesting" for item in items):
            raise WorkItemStateError("a GitHub ingest item is already in progress")
        approved = [item for item in items if item.state == "approved"]
        if not approved:
            raise WorkItemStateError("no approved GitHub ingest item is available")
        selected = min(approved, key=lambda item: (item.collection_date, item.work_item_id))
        updated = _transition_work_item_unlocked(
            path, items, selected.work_item_id, "approved", "ingesting", None
        )
        return next(item for item in updated if item.work_item_id == selected.work_item_id)


def record_collection_failure(
    path: Path,
    item: WorkItem,
    error: str,
    attempted_date: str,
    attempts_in_run: int,
) -> Tuple[WorkItem, ...]:
    """Record one exhausted collection run and escalate after three runs."""
    _validate_work_item(item)
    _require_date(attempted_date, "attempted_date")
    if not isinstance(attempts_in_run, int) or not 1 <= attempts_in_run <= 3:
        raise ValueError("collection failure requires one to three attempts in run")
    if not isinstance(error, str) or not error or len(error) > 1000:
        raise ValueError("collection failure error must be 1 to 1000 characters")
    with _queue_lock(path):
        items = list(load_work_items(path))
        matches = [index for index, value in enumerate(items) if value.work_item_id == item.work_item_id]
        if matches:
            index = matches[0]
            existing = items[index]
            _require_same_identity(existing, item)
            if existing.state in (
                "collected",
                "awaiting_approval",
                "approved",
                "ingesting",
                "ingested",
            ) or (
                existing.state == "needs_manual_review"
                and existing.approved_mode is not None
            ):
                return tuple(items)
            evidence = _merge_evidence(existing, item)
            current = replace(
                evidence,
                collection_date=existing.collection_date,
                state=existing.state,
                approved_mode=existing.approved_mode,
                attempts_in_run=existing.attempts_in_run,
                consecutive_failed_runs=existing.consecutive_failed_runs,
                last_error=existing.last_error,
                last_attempted_date=existing.last_attempted_date,
            )
        else:
            index = len(items)
            current = item
            items.append(item)
        failed_runs = current.consecutive_failed_runs + 1
        state = "needs_manual_review" if failed_runs >= 3 else "collection_failed"
        items[index] = replace(
            current,
            state=state,
            attempts_in_run=attempts_in_run,
            consecutive_failed_runs=failed_runs,
            last_error=error,
            last_attempted_date=attempted_date,
        )
        return _save_work_items_unlocked(path, items)


def record_ingest_failure(
    path: Path,
    work_item_id: str,
    error: str,
    attempted_date: str,
) -> Tuple[WorkItem, ...]:
    """Move the active ingest to manual review with bounded failure context."""
    _require_date(attempted_date, "attempted_date")
    if not isinstance(error, str) or not error or len(error) > 1000:
        raise ValueError("ingest failure error must be 1 to 1000 characters")
    with _queue_lock(path):
        items = list(load_work_items(path))
        index = _find_index(items, work_item_id)
        current = items[index]
        if current.state != "ingesting":
            raise WorkItemStateError(
                "expected state ingesting but found " + current.state
            )
        items[index] = replace(
            current,
            state="needs_manual_review",
            last_error=error,
            last_attempted_date=attempted_date,
        )
        return _save_work_items_unlocked(path, items)


def _transition_work_item_unlocked(
    path: Path,
    items: List[WorkItem],
    work_item_id: str,
    expected: str,
    requested: str,
    approved_mode: Optional[str],
) -> Tuple[WorkItem, ...]:
    index = _find_index(items, work_item_id)
    current = items[index]
    if current.state != expected:
        raise WorkItemStateError(
            "expected state " + expected + " but found " + current.state
        )
    if requested not in TRANSITIONS.get(expected, ()):
        raise WorkItemStateError(
            "invalid work-item transition from " + expected + " to " + requested
        )
    if (
        requested == "discovered"
        and expected in ("collection_failed", "needs_manual_review")
        and current.approved_mode is not None
    ):
        raise WorkItemStateError(
            "collection retry cannot resume an ingest-failed work item"
        )
    if requested == "approved":
        if approved_mode not in INGEST_MODES:
            raise WorkItemStateError("approval requires full or delta mode")
    elif approved_mode is not None:
        raise WorkItemStateError("approved_mode is only valid during approval")
    if requested == "ingesting":
        if current.approved_mode not in INGEST_MODES:
            raise WorkItemStateError("ingest cannot start without an approved mode")
        if any(
            item.work_item_id != work_item_id and item.state == "ingesting"
            for item in items
        ):
            raise WorkItemStateError("a GitHub ingest item is already in progress")
    updates: Dict[str, Any] = {"state": requested}
    if requested == "approved":
        updates["approved_mode"] = approved_mode
    if requested == "collected":
        updates.update(
            attempts_in_run=0,
            consecutive_failed_runs=0,
            last_error="",
            last_attempted_date="",
        )
    if requested == "discovered" and expected in (
        "collection_failed",
        "needs_manual_review",
    ):
        updates["attempts_in_run"] = 0
    items[index] = replace(current, **updates)
    return _save_work_items_unlocked(path, items)


@contextmanager
def _queue_lock(path: Path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    lock_path = path.with_name(path.name + ".lock")
    with _QUEUE_THREAD_LOCK:
        with lock_path.open("a+b") as lock:
            fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
            try:
                yield
            finally:
                fcntl.flock(lock.fileno(), fcntl.LOCK_UN)


def render_status(
    items: Sequence[WorkItem],
    packet_summaries: Optional[Mapping[str, PacketStatusSummary]] = None,
) -> str:
    """Render generated operator status from validated queue items."""
    summaries = dict(packet_summaries or {})
    normalized = tuple(sorted(items, key=lambda item: item.work_item_id))
    for item in normalized:
        _validate_work_item(item)
    lines = ["# GitHub repository ingest status", ""]
    if not normalized:
        return "\n".join(lines + ["No work items.", ""])
    for item in normalized:
        summary = summaries.get(item.work_item_id)
        if summary is not None:
            _validate_packet_summary(item, summary)
        packet_markdown = (
            item.ingest_packet[: -len("packet.json")] + "packet.md"
            if item.ingest_packet.endswith("packet.json")
            else item.ingest_packet
        )
        lines.extend(
            [
                "## `" + item.work_item_id + "`",
                "",
                "- Repository: `" + item.repo_id + "`",
                "- SHA: `" + item.sha + "`",
                "- Collection date: `" + item.collection_date + "`",
                "- State: `" + item.state + "`",
                "- Recommended mode: `" + item.recommended_mode + "`",
                "- Evidence revision: `" + (item.evidence_revision or "initial") + "`",
                "- Approved mode: `" + (item.approved_mode or "not approved") + "`",
                "- Attempts in run: `" + str(item.attempts_in_run) + "`",
                "- Consecutive failed runs: `" + str(item.consecutive_failed_runs) + "`",
                "- Last error: " + (item.last_error or "None"),
                "- Snapshot: "
                + (
                    "[manifest](" + item.snapshot_manifest + ")"
                    if item.snapshot_manifest
                    else "Not published"
                ),
                "- Packet: "
                + (
                    "[review packet](" + packet_markdown + ")"
                    if item.ingest_packet
                    else "Historical item without packet"
                ),
                "- Review priority: `"
                + (summary.priority if summary is not None else "not available")
                + "`",
                "- Required reading: `"
                + (
                    str(summary.required_reading_count)
                    if summary is not None
                    else "not available"
                )
                + "` files",
                "- Unclassified changes: `"
                + (
                    str(summary.unclassified_count)
                    if summary is not None
                    else "not available"
                )
                + "`",
                "- Evidence gaps: `"
                + (
                    str(summary.evidence_gap_count)
                    if summary is not None
                    else "not available"
                )
                + "`",
                "",
                "### Package releases",
                "",
            ]
        )
        for change in item.package_changes:
            lines.extend(
                [
                    "- `" + change.release_id + "` (recommended `" + change.recommended_mode + "`)",
                    "  Release: [manifest](" + change.release_manifest + ")",
                    "  Comparison: "
                    + (
                        "[manifest](" + change.comparison_manifest + ")"
                        if change.comparison_manifest
                        else "Not applicable"
                    ),
                ]
            )
        lines.append("")
    return "\n".join(lines)


def write_status_from_queue(
    queue_path: Path,
    status_path: Path,
    packet_summaries: Optional[Mapping[str, PacketStatusSummary]] = None,
) -> str:
    """Render and atomically write status while holding the queue lock."""
    with _queue_lock(queue_path):
        status = render_status(load_work_items(queue_path), packet_summaries)
        _write_atomic(Path(status_path), status.encode("utf-8"))
        return status


def _validate_package_change(change: PackageChange) -> None:
    if not isinstance(change, PackageChange):
        raise TypeError("package change must be PackageChange")
    _require_package(change.package)
    for label, version in (("from_version", change.from_version), ("to_version", change.to_version)):
        if not isinstance(version, str) or (version and parse_semver(version) is None):
            raise ValueError(label + " must be semantic")
    if not change.to_version:
        raise ValueError("to_version is required")
    if change.release_id != change.package + "@" + change.to_version:
        raise ValueError("release_id must be package-qualified")
    if change.release_manifest:
        _require_path(change.release_manifest, "release_manifest")
    if change.comparison_manifest:
        _require_path(change.comparison_manifest, "comparison_manifest")
    if change.recommended_mode not in INGEST_MODES:
        raise ValueError("recommended_mode must be full or delta")
    reasons = _strings(change.reasons, "reasons")
    if not reasons or len(set(reasons)) != len(reasons):
        raise ValueError("reasons must be non-empty and unique")


def _validate_work_item(item: WorkItem) -> None:
    if not isinstance(item, WorkItem):
        raise TypeError("work item must be WorkItem")
    _require_repo_id(item.repo_id)
    _require_sha(item.sha)
    _require_date(item.collection_date, "collection_date")
    if item.snapshot_manifest:
        _require_path(item.snapshot_manifest, "snapshot_manifest")
    elif item.state not in ("discovered", "collection_failed", "needs_manual_review"):
        raise ValueError("work-item state requires a published snapshot")
    if item.state not in ("discovered", "collection_failed", "needs_manual_review"):
        if any(not change.release_manifest for change in item.package_changes):
            raise ValueError("work-item state requires all release manifests")
        if any(change.from_version and not change.comparison_manifest for change in item.package_changes):
            raise ValueError("work-item state requires all applicable comparisons")
    if item.state not in STATES:
        raise ValueError("work-item state is invalid")
    if item.recommended_mode not in INGEST_MODES:
        raise ValueError("work-item recommended mode is invalid")
    if item.evidence_revision and re.fullmatch(r"[0-9a-f]{64}", item.evidence_revision) is None:
        raise ValueError("work-item evidence revision is invalid")
    if item.ingest_packet:
        _require_path(item.ingest_packet, "ingest_packet")
        expected_suffix = (
            "/ingest-packets/" + item.work_item_id + "/packet.json"
        )
        if (
            not item.ingest_packet.startswith("tracking/github/repos/")
            or not item.ingest_packet.endswith(expected_suffix)
        ):
            raise ValueError("work-item ingest packet path is invalid")
    if item.approved_mode is not None and item.approved_mode not in INGEST_MODES:
        raise ValueError("work-item approved mode is invalid")
    if item.state in ("approved", "ingesting", "ingested") and item.approved_mode is None:
        raise ValueError("approved work-item state requires approved mode")
    if not isinstance(item.attempts_in_run, int) or not 0 <= item.attempts_in_run <= 3:
        raise ValueError("attempts_in_run must be between zero and three")
    if not isinstance(item.consecutive_failed_runs, int) or item.consecutive_failed_runs < 0:
        raise ValueError("consecutive_failed_runs must be non-negative")
    if not isinstance(item.last_error, str) or len(item.last_error) > 1000:
        raise ValueError("last_error is invalid")
    if item.last_attempted_date:
        _require_date(item.last_attempted_date, "last_attempted_date")
    changes = tuple(item.package_changes)
    if not changes:
        raise ValueError("package_changes must not be empty")
    if changes != tuple(sorted(changes, key=lambda value: value.release_id)):
        raise ValueError("package_changes must be sorted")
    for change in changes:
        _validate_package_change(change)
    if len({change.release_id for change in changes}) != len(changes):
        raise ValueError("package_changes contain duplicate release IDs")
    expected_mode = "full" if any(change.recommended_mode == "full" for change in changes) else "delta"
    if item.recommended_mode != expected_mode:
        raise ValueError("work-item recommended mode does not match package changes")
    expected_id = build_work_item_id(
        item.repo_id,
        item.sha,
        tuple(change.release_id for change in changes),
        item.evidence_revision,
    )
    if item.work_item_id != expected_id or not _WORK_ITEM_ID.fullmatch(item.work_item_id):
        raise ValueError("work-item ID is invalid")


def _work_item_to_dict(item: WorkItem) -> dict:
    value = asdict(item)
    if not item.ingest_packet:
        value.pop("ingest_packet")
    value["package_changes"] = [asdict(change) for change in item.package_changes]
    for change in value["package_changes"]:
        change["reasons"] = list(change["reasons"])
    return value


def _work_item_from_dict(value: Any) -> WorkItem:
    if not isinstance(value, dict) or set(value) not in _WORK_ITEM_FIELD_SETS:
        raise ValueError("work item has unknown or missing fields")
    rows = value["package_changes"]
    if not isinstance(rows, list):
        raise ValueError("package_changes must be an array")
    changes = []
    for row in rows:
        if not isinstance(row, dict) or set(row) != _PACKAGE_CHANGE_FIELDS:
            raise ValueError("package change has unknown or missing fields")
        reasons = row["reasons"]
        if not isinstance(reasons, list):
            raise ValueError("package change reasons must be an array")
        values = dict(row)
        values["reasons"] = tuple(reasons)
        changes.append(PackageChange(**values))
    values = dict(value)
    values.setdefault("evidence_revision", "")
    values.setdefault("ingest_packet", "")
    values["package_changes"] = tuple(changes)
    item = WorkItem(**values)
    _validate_work_item(item)
    return item


def _require_same_evidence(existing: WorkItem, incoming: WorkItem) -> None:
    fields = (
        "work_item_id",
        "repo_id",
        "sha",
        "package_changes",
        "snapshot_manifest",
        "recommended_mode",
        "ingest_packet",
    )
    if any(getattr(existing, field) != getattr(incoming, field) for field in fields):
        raise ValueError("existing work item conflicts with discovered evidence")


def _require_same_identity(existing: WorkItem, incoming: WorkItem) -> None:
    existing_ids = tuple(change.release_id for change in existing.package_changes)
    incoming_ids = tuple(change.release_id for change in incoming.package_changes)
    if (
        existing.work_item_id != incoming.work_item_id
        or existing.repo_id != incoming.repo_id
        or existing.sha != incoming.sha
        or existing_ids != incoming_ids
    ):
        raise ValueError("existing work item conflicts with discovered identity")


def _require_compatible_paths(existing: WorkItem, incoming: WorkItem) -> None:
    if (
        existing.snapshot_manifest
        and incoming.snapshot_manifest
        and existing.snapshot_manifest != incoming.snapshot_manifest
    ):
        raise ValueError("existing work item conflicts with snapshot evidence")
    if (
        existing.ingest_packet
        and incoming.ingest_packet
        and existing.ingest_packet != incoming.ingest_packet
    ):
        raise ValueError("existing work item conflicts with ingest packet evidence")
    existing_changes = {change.release_id: change for change in existing.package_changes}
    for change in incoming.package_changes:
        prior = existing_changes[change.release_id]
        for field in ("release_manifest", "comparison_manifest"):
            prior_path = getattr(prior, field)
            current_path = getattr(change, field)
            if prior_path and current_path and prior_path != current_path:
                raise ValueError("existing work item conflicts with package evidence")


def _merge_evidence(existing: WorkItem, incoming: WorkItem) -> WorkItem:
    _require_compatible_paths(existing, incoming)
    old_changes = {change.release_id: change for change in existing.package_changes}
    merged_changes = []
    for change in incoming.package_changes:
        prior = old_changes[change.release_id]
        use_incoming_policy = bool(
            change.release_manifest or change.comparison_manifest
        )
        policy = change if use_incoming_policy else prior
        merged_changes.append(
            replace(
                policy,
                release_manifest=change.release_manifest or prior.release_manifest,
                comparison_manifest=(
                    change.comparison_manifest or prior.comparison_manifest
                ),
            )
        )
    mode = "full" if any(change.recommended_mode == "full" for change in merged_changes) else "delta"
    return replace(
        incoming,
        package_changes=tuple(merged_changes),
        snapshot_manifest=incoming.snapshot_manifest or existing.snapshot_manifest,
        ingest_packet=incoming.ingest_packet or existing.ingest_packet,
        recommended_mode=mode,
    )


def _validate_packet_summary(
    item: WorkItem, summary: PacketStatusSummary
) -> None:
    if not isinstance(summary, PacketStatusSummary):
        raise TypeError("packet summary must be PacketStatusSummary")
    if summary.packet_path != item.ingest_packet:
        raise ValueError("packet summary path does not match work item")
    if summary.priority not in ("normal", "high"):
        raise ValueError("packet summary priority is invalid")
    for value in (
        summary.required_reading_count,
        summary.unclassified_count,
        summary.evidence_gap_count,
    ):
        if not isinstance(value, int) or value < 0:
            raise ValueError("packet summary count is invalid")


def _find_index(items: Sequence[WorkItem], work_item_id: str) -> int:
    for index, item in enumerate(items):
        if item.work_item_id == work_item_id:
            return index
    raise WorkItemStateError("work item was not found")


def _require_repo_id(value: str) -> None:
    if not isinstance(value, str) or value.count("/") != 1 or not safe_policy_path(value):
        raise ValueError("repository ID must be owner/name")


def _require_sha(value: str) -> None:
    if not isinstance(value, str) or not _OBJECT_ID.fullmatch(value):
        raise ValueError("SHA must be a full Git object ID")


def _require_date(value: str, label: str) -> None:
    if not isinstance(value, str) or not _DATE.fullmatch(value):
        raise ValueError(label + " must use YYYY-MM-DD")


def _require_path(value: str, label: str) -> None:
    if not safe_policy_path(value):
        raise ValueError(label + " must be a safe relative path")


def _require_package(value: str) -> None:
    if not validate_npm_package_name(value):
        raise ValueError("package name is invalid")


def _paths(values: Sequence[str], label: str) -> Tuple[str, ...]:
    normalized = _strings(values, label)
    if any(not safe_policy_path(value) for value in normalized):
        raise ValueError(label + " contains an unsafe path")
    if len(set(normalized)) != len(normalized):
        raise ValueError(label + " contains duplicates")
    return normalized


def _strings(values: Sequence[str], label: str) -> Tuple[str, ...]:
    if isinstance(values, (str, bytes)):
        raise TypeError(label + " must be a sequence")
    normalized = tuple(values)
    if any(not isinstance(value, str) or not value for value in normalized):
        raise ValueError(label + " must contain non-empty strings")
    return normalized


def _reject_duplicate_keys(pairs: Sequence[Tuple[str, Any]]) -> dict:
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError("duplicate JSON key " + key)
        value[key] = item
    return value


def _write_atomic(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=".tmp-", dir=str(path.parent))
    try:
        with os.fdopen(descriptor, "wb") as output:
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


__all__ = [
    "BROAD_CHANGE_FILE_LIMIT",
    "ChangeSignals",
    "FULL_SIGNAL_ORDER",
    "PackageChange",
    "PacketStatusSummary",
    "TRANSITIONS",
    "WorkItem",
    "WorkItemStateError",
    "build_work_item",
    "build_work_item_id",
    "finalize_collected_work_item",
    "load_work_items",
    "recommend_ingest_mode",
    "record_collection_failure",
    "render_status",
    "save_work_items",
    "transition_work_item",
    "upsert_discovered_work_item",
]
