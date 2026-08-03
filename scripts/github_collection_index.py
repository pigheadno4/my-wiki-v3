"""Deterministic repository-level GitHub collection scheduling index."""

from calendar import monthrange
from dataclasses import asdict, dataclass
from datetime import date, timedelta
import json
import os
from pathlib import Path
import tempfile
from typing import Mapping, Sequence, Tuple

from github_canonical import canonical_json_bytes
from github_registry import RepoConfig
from github_work_items import WorkItem


JSON_PATH = Path("tracking/github/collection-index.json")
MARKDOWN_PATH = Path("tracking/github/collection-index.md")
FORMAT_VERSION = 1
ACTIONS = frozenset(
    (
        "disabled",
        "collect-baseline",
        "wait",
        "review-delta",
        "review-full",
        "ingest",
        "retry",
        "manual-review",
    )
)
PRIORITY_ORDER = {"tier1": 1, "tier2": 2, "tier3": 3}
ROW_FIELDS = {
    "repo_id",
    "company",
    "enabled",
    "priority",
    "strategy",
    "adapter",
    "frequency",
    "last_checked_date",
    "last_accepted_ref",
    "latest_discovered_ref",
    "comparison_base",
    "queue_state",
    "next_due_date",
    "next_action",
    "last_error",
}


@dataclass(frozen=True)
class CollectionIndexRow:
    repo_id: str
    company: str
    enabled: bool
    priority: str
    strategy: str
    adapter: str
    frequency: str
    last_checked_date: str
    last_accepted_ref: str
    latest_discovered_ref: str
    comparison_base: str
    queue_state: str
    next_due_date: str
    next_action: str
    last_error: str


def build_collection_index(
    repos: Sequence[RepoConfig],
    items: Sequence[WorkItem],
    checked_state: Mapping[str, Mapping[str, str]],
    today: date,
) -> dict:
    """Build one canonical repository-level scheduling document."""
    if not isinstance(today, date):
        raise TypeError("today must be a date")
    known = {repo.id for repo in repos}
    if set(checked_state) - known:
        raise ValueError("checked state contains unknown repository")
    rows = []
    for repo in sorted(
        repos,
        key=lambda value: (
            value.company,
            PRIORITY_ORDER.get(value.priority, 99),
            value.id,
        ),
    ):
        repository_items = tuple(item for item in items if item.repo_id == repo.id)
        checked = checked_state.get(repo.id, {})
        row = _build_row(repo, repository_items, checked, today)
        rows.append(asdict(row))
    return {
        "format_version": FORMAT_VERSION,
        "generated_date": today.isoformat(),
        "repositories": rows,
    }


def render_collection_index(document: dict) -> str:
    """Render the deterministic operator view of an index document."""
    _validate_document_shape(document)
    lines = [
        "# GitHub repository collection index",
        "",
        "Generated: `" + document["generated_date"] + "`",
        "",
        "| Company | Repository | Priority | Strategy | Frequency | Last checked | Queue | Next due | Next action |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in document["repositories"]:
        lines.append(
            "| "
            + " | ".join(
                (
                    row["company"],
                    "`" + row["repo_id"] + "`",
                    row["priority"],
                    row["strategy"] + (" / " + row["adapter"] if row["adapter"] else ""),
                    row["frequency"],
                    row["last_checked_date"] or "-",
                    row["queue_state"] or "-",
                    row["next_due_date"] or "-",
                    "`" + row["next_action"] + "`",
                )
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def write_collection_index(
    root: Path,
    repos: Sequence[RepoConfig],
    items: Sequence[WorkItem],
    checked_state: Mapping[str, Mapping[str, str]],
    today: date,
) -> dict:
    """Atomically publish matching canonical JSON and Markdown views."""
    root = Path(root).resolve()
    document = build_collection_index(repos, items, checked_state, today)
    _write_atomic(root / JSON_PATH, canonical_json_bytes(document) + b"\n")
    _write_atomic(
        root / MARKDOWN_PATH,
        render_collection_index(document).encode("utf-8"),
    )
    return document


def load_collection_index(root: Path) -> dict:
    """Load and structurally validate the generated JSON index."""
    path = Path(root).resolve() / JSON_PATH
    document = json.loads(path.read_text(encoding="utf-8"))
    _validate_document_shape(document)
    return document


def checked_state_from_document(document: dict) -> dict:
    """Extract collection-run facts that are not represented by queue items."""
    _validate_document_shape(document)
    return {
        row["repo_id"]: {
            "last_checked_date": row["last_checked_date"],
            "latest_discovered_ref": row["latest_discovered_ref"],
            "comparison_base": row["comparison_base"],
            "last_error": row["last_error"],
        }
        for row in document["repositories"]
        if any(
            row[field]
            for field in (
                "last_checked_date",
                "latest_discovered_ref",
                "comparison_base",
                "last_error",
            )
        )
    }


def validate_collection_index(
    root: Path,
    repos: Sequence[RepoConfig],
    items: Sequence[WorkItem],
) -> list:
    """Validate canonical encoding, registry/queue derivation, and both views."""
    root = Path(root).resolve()
    json_path = root / JSON_PATH
    markdown_path = root / MARKDOWN_PATH
    errors = []
    if not json_path.exists() or not markdown_path.exists():
        return ["tracking/github collection index is missing"]
    try:
        raw = json_path.read_bytes()
        document = json.loads(raw.decode("utf-8"))
        _validate_document_shape(document)
    except (OSError, UnicodeError, json.JSONDecodeError, TypeError, ValueError) as error:
        return ["tracking/github/collection-index.json is invalid: " + _bounded(error)]
    if raw != canonical_json_bytes(document) + b"\n":
        errors.append("tracking/github/collection-index.json is not canonical")
    try:
        generated = date.fromisoformat(document["generated_date"])
        expected = build_collection_index(
            repos,
            items,
            checked_state_from_document(document),
            generated,
        )
    except (TypeError, ValueError) as error:
        errors.append("tracking/github/collection-index.json is inconsistent: " + _bounded(error))
        expected = None
    if expected is not None and document != expected:
        errors.append("tracking/github/collection-index.json does not match registry and queue")
    try:
        markdown = markdown_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        errors.append("tracking/github/collection-index.md is unreadable: " + _bounded(error))
    else:
        if markdown != render_collection_index(document):
            errors.append("tracking/github/collection-index.md is stale")
    return errors


def _build_row(
    repo: RepoConfig,
    items: Sequence[WorkItem],
    checked: Mapping[str, str],
    today: date,
) -> CollectionIndexRow:
    latest = max(items, key=lambda item: (item.collection_date, item.work_item_id), default=None)
    accepted = tuple(
        item
        for item in items
        if item.state not in ("discovered", "collection_failed", "needs_manual_review")
    )
    latest_accepted = max(
        accepted,
        key=lambda item: (item.collection_date, item.work_item_id),
        default=None,
    )
    last_checked = _checked_value(checked, "last_checked_date")
    if not last_checked and latest is not None:
        last_checked = latest.collection_date
    latest_ref = _checked_value(checked, "latest_discovered_ref")
    queue_is_current = latest is not None and (
        not last_checked or latest.collection_date >= last_checked
    )
    if queue_is_current:
        latest_ref = _item_identity(latest)
    comparison_base = _checked_value(checked, "comparison_base")
    if queue_is_current:
        comparison_base = _comparison_base(latest)
    last_error = (
        latest.last_error
        if queue_is_current and latest.last_error
        else _checked_value(checked, "last_error")
    )
    last_error = " ".join(last_error.split())[:240]
    next_due = _next_due(last_checked, repo.collection_frequency)
    action = _next_action(repo, latest, bool(accepted), next_due, today)
    adapter = repo.capsules[0].adapter if len(repo.capsules) == 1 else ""
    return CollectionIndexRow(
        repo.id,
        repo.company,
        repo.enabled,
        repo.priority,
        repo.version_strategy,
        adapter,
        repo.collection_frequency,
        last_checked,
        _item_identity(latest_accepted) if latest_accepted is not None else "",
        latest_ref,
        comparison_base,
        latest.state if latest is not None else "",
        next_due,
        action,
        last_error,
    )


def _next_action(
    repo: RepoConfig,
    latest: WorkItem,
    has_accepted: bool,
    next_due: str,
    today: date,
) -> str:
    if not repo.enabled:
        return "disabled"
    if latest is not None:
        if latest.state == "awaiting_approval":
            return "review-" + latest.recommended_mode
        if latest.state in ("approved", "ingesting"):
            return "ingest"
        if latest.state == "collection_failed":
            return "retry"
        if latest.state == "needs_manual_review":
            return "manual-review"
    if not has_accepted:
        return "collect-baseline"
    if not next_due or date.fromisoformat(next_due) > today:
        return "wait"
    return "collect-baseline"


def _next_due(last_checked: str, frequency: str) -> str:
    if not last_checked or frequency == "on-demand":
        return ""
    checked = date.fromisoformat(last_checked)
    if frequency == "weekly":
        return (checked + timedelta(days=7)).isoformat()
    if frequency == "monthly":
        month = checked.month + 1
        year = checked.year
        if month == 13:
            month = 1
            year += 1
        day = min(checked.day, monthrange(year, month)[1])
        return date(year, month, day).isoformat()
    raise ValueError("unsupported collection frequency " + frequency)


def _item_identity(item: WorkItem) -> str:
    if item is None:
        return ""
    if item.ref_changes:
        return ", ".join(change.display_identity for change in item.ref_changes)
    return ", ".join(change.release_id for change in item.package_changes)


def _comparison_base(item: WorkItem) -> str:
    if item.ref_changes:
        return item.ref_changes[0].from_sha
    bases = tuple(
        change.package + "@" + change.from_version
        for change in item.package_changes
        if change.from_version
    )
    return ", ".join(bases)


def _checked_value(checked: Mapping[str, str], field: str) -> str:
    value = checked.get(field, "")
    if not isinstance(value, str):
        raise ValueError("checked state " + field + " must be text")
    return value


def _validate_document_shape(document: dict) -> None:
    if not isinstance(document, dict) or set(document) != {
        "format_version",
        "generated_date",
        "repositories",
    }:
        raise ValueError("collection index has unknown or missing fields")
    if document["format_version"] != FORMAT_VERSION:
        raise ValueError("collection index format is invalid")
    date.fromisoformat(document["generated_date"])
    rows = document["repositories"]
    if not isinstance(rows, list):
        raise ValueError("collection index repositories must be an array")
    identities = []
    for row in rows:
        if not isinstance(row, dict) or set(row) != ROW_FIELDS:
            raise ValueError("collection index row has unknown or missing fields")
        if not isinstance(row["enabled"], bool):
            raise ValueError("collection index enabled value is invalid")
        if row["next_action"] not in ACTIONS:
            raise ValueError("collection index action is invalid")
        for key, value in row.items():
            if key != "enabled" and not isinstance(value, str):
                raise ValueError("collection index row value is invalid")
        identities.append(row["repo_id"])
    if len(identities) != len(set(identities)):
        raise ValueError("collection index contains duplicate repositories")


def _write_atomic(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=path.name + ".", dir=str(path.parent))
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def _bounded(error: Exception) -> str:
    return " ".join(str(error).split())[:240]


__all__ = [
    "ACTIONS",
    "CollectionIndexRow",
    "build_collection_index",
    "checked_state_from_document",
    "load_collection_index",
    "render_collection_index",
    "validate_collection_index",
    "write_collection_index",
]
