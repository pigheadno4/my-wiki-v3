"""Deterministic ingest recommendations and queue state for the GitHub pilot."""

from dataclasses import asdict, dataclass, replace
import json
import os
from pathlib import Path
import re
import tempfile
from typing import Any, Dict, List, Optional, Sequence, Tuple

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
}


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
class WorkItem:
    work_item_id: str
    repo_id: str
    sha: str
    collection_date: str
    package_changes: Tuple[PackageChange, ...]
    snapshot_manifest: str
    recommended_mode: str
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


def build_work_item_id(repo_id: str, sha: str, release_ids: Sequence[str]) -> str:
    """Build the stable identity for one SHA-grouped release set."""
    _require_repo_id(repo_id)
    _require_sha(sha)
    normalized = tuple(sorted(set(_strings(release_ids, "release_ids"))))
    if not normalized:
        raise ValueError("release_ids must not be empty")
    payload = {"release_ids": list(normalized), "repository": repo_id, "sha": sha}
    return "github-" + canonical_sha256(payload)[:20]


def build_work_item(
    repo_id: str,
    sha: str,
    collection_date: str,
    package_changes: Sequence[PackageChange],
    snapshot_manifest: str,
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
    _require_path(snapshot_manifest, "snapshot_manifest")
    mode = "full" if any(item.recommended_mode == "full" for item in changes) else "delta"
    release_ids = tuple(item.release_id for item in changes)
    item = WorkItem(
        build_work_item_id(repo_id, sha, release_ids),
        repo_id,
        sha,
        collection_date,
        changes,
        snapshot_manifest,
        mode,
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
    items = list(load_work_items(path))
    for existing in items:
        if existing.work_item_id == item.work_item_id:
            _require_same_evidence(existing, item)
            return tuple(items)
    if item.state != "discovered":
        raise WorkItemStateError("new work item must start in discovered state")
    items.append(item)
    return save_work_items(path, items)


def transition_work_item(
    path: Path,
    work_item_id: str,
    expected: str,
    requested: str,
    approved_mode: Optional[str] = None,
) -> Tuple[WorkItem, ...]:
    """Apply one explicit compare-and-set lifecycle transition."""
    items = list(load_work_items(path))
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
    if requested == "approved":
        if approved_mode not in INGEST_MODES:
            raise WorkItemStateError("approval requires full or delta mode")
    elif approved_mode is not None:
        raise WorkItemStateError("approved_mode is only valid during approval")
    if requested == "ingesting" and current.approved_mode not in INGEST_MODES:
        raise WorkItemStateError("ingest cannot start without an approved mode")
    updates: Dict[str, Any] = {"state": requested}
    if requested == "approved":
        updates["approved_mode"] = approved_mode
    if requested == "discovered" and expected in (
        "collection_failed",
        "needs_manual_review",
    ):
        updates["attempts_in_run"] = 0
    items[index] = replace(current, **updates)
    return save_work_items(path, items)


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
    if attempts_in_run != 3:
        raise ValueError("collection failure requires exactly three attempts in run")
    if not isinstance(error, str) or not error or len(error) > 1000:
        raise ValueError("collection failure error must be 1 to 1000 characters")
    items = list(load_work_items(path))
    matches = [index for index, value in enumerate(items) if value.work_item_id == item.work_item_id]
    if matches:
        index = matches[0]
        current = items[index]
        _require_same_evidence(current, item)
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
    return save_work_items(path, items)


def render_status(items: Sequence[WorkItem]) -> str:
    """Render generated operator status from validated queue items."""
    normalized = tuple(sorted(items, key=lambda item: item.work_item_id))
    for item in normalized:
        _validate_work_item(item)
    lines = ["# GitHub repository ingest status", ""]
    if not normalized:
        return "\n".join(lines + ["No work items.", ""])
    for item in normalized:
        lines.extend(
            [
                "## `" + item.work_item_id + "`",
                "",
                "- Repository: `" + item.repo_id + "`",
                "- SHA: `" + item.sha + "`",
                "- Collection date: `" + item.collection_date + "`",
                "- State: `" + item.state + "`",
                "- Recommended mode: `" + item.recommended_mode + "`",
                "- Approved mode: `" + (item.approved_mode or "not approved") + "`",
                "- Attempts in run: `" + str(item.attempts_in_run) + "`",
                "- Consecutive failed runs: `" + str(item.consecutive_failed_runs) + "`",
                "- Last error: " + (item.last_error or "None"),
                "- Snapshot: [manifest](" + item.snapshot_manifest + ")",
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
                    "  Comparison: [manifest](" + change.comparison_manifest + ")",
                ]
            )
        lines.append("")
    return "\n".join(lines)


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
    _require_path(change.release_manifest, "release_manifest")
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
    _require_path(item.snapshot_manifest, "snapshot_manifest")
    if item.state not in STATES:
        raise ValueError("work-item state is invalid")
    if item.recommended_mode not in INGEST_MODES:
        raise ValueError("work-item recommended mode is invalid")
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
        item.repo_id, item.sha, tuple(change.release_id for change in changes)
    )
    if item.work_item_id != expected_id or not _WORK_ITEM_ID.fullmatch(item.work_item_id):
        raise ValueError("work-item ID is invalid")


def _work_item_to_dict(item: WorkItem) -> dict:
    value = asdict(item)
    value["package_changes"] = [asdict(change) for change in item.package_changes]
    for change in value["package_changes"]:
        change["reasons"] = list(change["reasons"])
    return value


def _work_item_from_dict(value: Any) -> WorkItem:
    if not isinstance(value, dict) or set(value) != _WORK_ITEM_FIELDS:
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
    values["package_changes"] = tuple(changes)
    item = WorkItem(**values)
    _validate_work_item(item)
    return item


def _require_same_evidence(existing: WorkItem, incoming: WorkItem) -> None:
    fields = (
        "work_item_id",
        "repo_id",
        "sha",
        "collection_date",
        "package_changes",
        "snapshot_manifest",
        "recommended_mode",
    )
    if any(getattr(existing, field) != getattr(incoming, field) for field in fields):
        raise ValueError("existing work item conflicts with discovered evidence")


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
    "TRANSITIONS",
    "WorkItem",
    "WorkItemStateError",
    "build_work_item",
    "build_work_item_id",
    "load_work_items",
    "recommend_ingest_mode",
    "record_collection_failure",
    "render_status",
    "save_work_items",
    "transition_work_item",
    "upsert_discovered_work_item",
]
