"""One-process dry-run transitions for the minimum ingest pilot."""

import json
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, Mapping, Optional, Sequence, Union

from .scheduler import review_order, shared_slot_orders, worker_orders
from .state import (
    PilotError,
    append_event,
    create_attempt,
    initialize_state,
    load_campaign,
    load_jobs,
    render_monitor,
    save_jobs,
    write_attempt_file,
)
from .validator import ValidationError, validate_worker_result


LEGACY_REVIEW_RESULT_KEYS = {"job_id", "attempt", "verdict", "reason", "required_changes"}
REVIEW_RESULT_KEYS = {
    "job_id", "attempt", "verdict", "reason", "required_changes",
    "review_scope", "retry_review_scope", "shared_update_decisions",
}
REVIEW_VERDICTS = {"approved", "changes_requested", "rejected"}
REVIEW_SCOPES = {"full", "targeted"}
SHARED_UPDATE_DECISION_KEYS = {"update_id", "verdict", "reason"}
SHARED_UPDATE_DECISION_VERDICTS = {"approved", "rejected"}


def _json_bytes(value: Any) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=False) + "\n").encode("utf-8")


def _job(jobs: list, job_id: object) -> Dict[str, Any]:
    matches = [job for job in jobs if job["job_id"] == job_id]
    if len(matches) != 1:
        raise PilotError("unknown job")
    return matches[0]


def _load_result(path: Path) -> Dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise PilotError("cannot read result") from error
    if not isinstance(value, dict):
        raise PilotError("result must contain an object")
    return value


def _campaign_payload(root: Path, campaign_id: str) -> Dict[str, Any]:
    campaign = load_campaign(root, campaign_id)
    return {
        "campaign_id": campaign["campaign_id"],
        "campaign_state": campaign["state"],
        "jobs": load_jobs(root, campaign_id),
        "monitor": render_monitor(root, campaign_id),
    }


def init_campaign(root: Path, manifest: Union[Path, Mapping[str, Any]]) -> Dict[str, Any]:
    """Create a trusted dry-run campaign and return its current state."""
    initialize_state(root, manifest)
    if isinstance(manifest, Path):
        campaign_id = _load_result(manifest)["campaign_id"]
    else:
        campaign_id = manifest["campaign_id"]
    return _campaign_payload(root, str(campaign_id))


def _apply_worker_result(
    root: Path,
    campaign_id: str,
    jobs: list,
    result_path: Path,
    max_attempts: int,
) -> tuple[Dict[str, Any], list[tuple[Path, str, bytes]]]:
    result = _load_result(result_path)
    job = _job(jobs, result.get("job_id"))
    if job["state"] != "running":
        raise PilotError("worker result requires a running job")
    attempt_dir = (
        root
        / "tracking"
        / "ingest"
        / "metronome"
        / campaign_id
        / "attempts"
        / job["job_id"]
        / f"attempt-{job['attempt']}"
    )
    try:
        validated = validate_worker_result(root, job, result)
    except ValidationError as error:
        exhausted = job["attempt"] >= max_attempts
        job["state"] = "rejected" if exhausted else "failed"
        job["last_event"] = "worker_result_rejected" if exhausted else "worker_result_invalid"
        job["failure_reason"] = str(error)
        return (
            {"event": job["last_event"], "job_id": job["job_id"], "reason": str(error)},
            [(attempt_dir, "failure.json", _json_bytes({"reason": str(error)}))],
        )

    job["state"] = "candidate_ready"
    job["last_event"] = "candidate_ready"
    job["failure_reason"] = None
    return (
        {"event": "candidate_ready", "job_id": job["job_id"]},
        [
            (attempt_dir, "candidate.md", validated["source_page"].encode("utf-8")),
            (attempt_dir, "receipt.json", _json_bytes(validated)),
            (attempt_dir, "suggestions.json", _json_bytes(validated["suggestions"])),
        ],
    )


def _validate_review_result(result: dict, expected_scope: str, suggestion_ids: set[str]) -> None:
    if set(result) != REVIEW_RESULT_KEYS:
        raise PilotError("review result must use the fixed schema")
    verdict = result["verdict"]
    reason = result["reason"]
    changes = result["required_changes"]
    review_scope = result["review_scope"]
    retry_scope = result["retry_review_scope"]
    decisions = result["shared_update_decisions"]
    if (
        not isinstance(verdict, str)
        or verdict not in REVIEW_VERDICTS
        or not isinstance(reason, str)
        or not reason.strip()
        or not isinstance(changes, list)
        or not all(isinstance(change, str) and change.strip() for change in changes)
        or not isinstance(review_scope, str)
        or review_scope not in REVIEW_SCOPES
        or review_scope != expected_scope
        or (retry_scope is not None and (
            not isinstance(retry_scope, str) or retry_scope not in REVIEW_SCOPES
        ))
    ):
        raise PilotError("review result is invalid")
    if verdict == "approved" and (changes or retry_scope is not None):
        raise PilotError("review result is invalid")
    if verdict == "changes_requested" and (
        not changes or retry_scope not in REVIEW_SCOPES
    ):
        raise PilotError("review result is invalid")
    if verdict == "rejected" and retry_scope is not None:
        raise PilotError("review result is invalid")
    if not isinstance(decisions, list):
        raise PilotError("review result is invalid")
    decision_ids = []
    for decision in decisions:
        if not isinstance(decision, dict) or set(decision) != SHARED_UPDATE_DECISION_KEYS:
            raise PilotError("review result is invalid")
        update_id = decision["update_id"]
        if (
            not isinstance(update_id, str)
            or not isinstance(decision["verdict"], str)
            or decision["verdict"] not in SHARED_UPDATE_DECISION_VERDICTS
            or not isinstance(decision["reason"], str)
            or not decision["reason"].strip()
        ):
            raise PilotError("review result is invalid")
        decision_ids.append(update_id)
    if len(set(decision_ids)) != len(decision_ids) or set(decision_ids) != suggestion_ids:
        raise PilotError("review result is invalid")


def _apply_review_result(
    root: Path,
    campaign_id: str,
    campaign: Mapping[str, Any],
    jobs: list,
    result_path: Path,
    max_attempts: int,
) -> tuple[Dict[str, Any], list[tuple[Path, str, bytes]]]:
    result = _load_result(result_path)
    review_keys = REVIEW_RESULT_KEYS if campaign.get("schema_version", 1) == 2 else LEGACY_REVIEW_RESULT_KEYS
    if set(result) != review_keys:
        raise PilotError("review result must use the fixed schema")
    job = _job(jobs, result["job_id"])
    if job["state"] != "reviewing" or result["attempt"] != job["attempt"]:
        raise PilotError("review result does not match a reviewing job")
    is_schema_v2 = campaign.get("schema_version", 1) == 2
    if campaign["review_concurrency"] > 1 and (
        not isinstance(job.get("reviewer_identity"), str)
        or not job["reviewer_identity"]
        or not isinstance(job.get("reviewer_model"), str)
        or not job["reviewer_model"]
    ):
        raise PilotError("parallel review requires a reviewer assignment")
    if campaign["review_concurrency"] > 1 and job["reviewer_identity"] == job.get("worker_identity"):
        raise PilotError("reviewer identity must differ from worker identity")
    if is_schema_v2 and (
        not isinstance(job.get("reviewer_identity"), str)
        or not job["reviewer_identity"]
        or not isinstance(job.get("reviewer_model"), str)
        or not job["reviewer_model"]
    ):
        raise PilotError("schema-v2 review requires reviewer provenance")
    verdict = result["verdict"]
    reason = result["reason"]
    changes = result["required_changes"]
    if is_schema_v2:
        attempt_dir = (
            root / "tracking" / "ingest" / "metronome" / campaign_id / "attempts"
            / job["job_id"] / f"attempt-{job['attempt']}"
        )
        suggestions = _load_result(attempt_dir / "suggestions.json")
        suggestion_ids = {
            suggestion["update_id"]
            for category in suggestions.values()
            for suggestion in category
        }
        _validate_review_result(result, job.get("next_review_scope", "full"), suggestion_ids)
    elif (
        not isinstance(verdict, str)
        or verdict not in REVIEW_VERDICTS
        or not isinstance(reason, str)
        or not reason
        or not isinstance(changes, list)
    ):
        raise PilotError("review result is invalid")
    files = []
    attempt_dir = (
        root / "tracking" / "ingest" / "metronome" / campaign_id / "attempts"
        / job["job_id"] / f"attempt-{job['attempt']}"
    )
    if is_schema_v2 or "reviewer_identity" in job:
        files.append(
            (attempt_dir, "review.json", _json_bytes({
                **result,
                "reviewer_identity": job["reviewer_identity"],
                "reviewer_model": job["reviewer_model"],
            }))
        )
    if verdict == "approved":
        job["state"] = "approved"
        job["last_event"] = "review_approved"
        job["failure_reason"] = None
        return {"event": "review_approved", "job_id": job["job_id"]}, files
    if verdict == "rejected" or job["attempt"] >= max_attempts:
        job["state"] = "rejected"
        job["last_event"] = "review_rejected" if verdict == "rejected" else "changes_exhausted"
        job["failure_reason"] = reason
        return {"event": job["last_event"], "job_id": job["job_id"], "reason": reason}, files
    job["state"] = "queued"
    job["queue_position"] = max(item["queue_position"] for item in jobs) + 1
    job["last_event"] = "changes_requested"
    job["failure_reason"] = None
    job["next_review_scope"] = result.get("retry_review_scope", "full")
    return {"event": "changes_requested", "job_id": job["job_id"], "reason": reason}, files


def _write_pending_files(files: Sequence[tuple[Path, str, bytes]]) -> None:
    for attempt_dir, filename, content in files:
        if not attempt_dir.exists():
            attempt_dir.mkdir(parents=True)
        write_attempt_file(attempt_dir, filename, content)


def _start_workers(
    root: Path,
    campaign_id: str,
    jobs: list,
    campaign: Mapping[str, Any],
    available_worker_slots: Optional[int],
) -> list:
    running = sum(job["state"] == "running" for job in jobs)
    campaign_slots = max(0, campaign["worker_concurrency"] - running)
    host_slots = campaign_slots if available_worker_slots is None else available_worker_slots
    orders = worker_orders(jobs, campaign_slots, campaign["max_attempts"], host_slots)
    for order in orders:
        job = _job(jobs, order["job_id"])
        attempt = order["attempt"]
        attempt_dir = create_attempt(root, campaign_id, job, attempt)
        write_attempt_file(attempt_dir, "input.json", _json_bytes(order))
        job["attempt"] = attempt
        job["state"] = "running"
        job["last_event"] = "worker_started"
        job["failure_reason"] = None
    return orders


def _assignment_by_job(
    assignments: Optional[Union[Mapping[str, Mapping[str, str]], Sequence[Mapping[str, str]]]],
    orders: Sequence[Mapping[str, object]],
    label: str,
) -> Dict[str, Dict[str, str]]:
    if not orders:
        return {}
    if assignments is None:
        raise PilotError(f"{label} assignments are required")
    if isinstance(assignments, Mapping):
        expected_job_ids = {str(order["job_id"]) for order in orders}
        if set(assignments) != expected_job_ids:
            raise PilotError(f"{label} assignments must match emitted orders")
        selected = {str(order["job_id"]): assignments[str(order["job_id"])] for order in orders}
    elif isinstance(assignments, Sequence) and not isinstance(assignments, (str, bytes)):
        if len(assignments) != len(orders):
            raise PilotError(f"{label} assignments must match emitted orders")
        selected = {str(order["job_id"]): assignment for order, assignment in zip(orders, assignments)}
    else:
        raise PilotError(f"{label} assignments must match emitted orders")
    validated = {}
    for job_id, assignment in selected.items():
        if not isinstance(assignment, Mapping) or set(assignment) != {"identity", "model"}:
            raise PilotError(f"{label} assignments require identity and model")
        identity, model = assignment["identity"], assignment["model"]
        if not isinstance(identity, str) or not identity.strip() or not isinstance(model, str) or not model.strip():
            raise PilotError(f"{label} assignments require non-empty identity and model")
        validated[job_id] = {"identity": identity, "model": model}
    return validated


def _start_shared_orders(
    root: Path,
    campaign_id: str,
    jobs: list,
    campaign: Mapping[str, Any],
    total_subagent_slots: int,
    worker_assignments: Optional[Union[Mapping[str, Mapping[str, str]], Sequence[Mapping[str, str]]]],
    reviewer_assignments: Optional[Union[Mapping[str, Mapping[str, str]], Sequence[Mapping[str, str]]]],
) -> Dict[str, list]:
    projected = shared_slot_orders(
        jobs,
        campaign["worker_concurrency"],
        campaign["review_concurrency"],
        campaign["max_attempts"],
        total_subagent_slots,
    )
    worker_assignment_by_job = _assignment_by_job(worker_assignments, projected["worker_orders"], "worker")
    reviewer_assignment_by_job = _assignment_by_job(reviewer_assignments, projected["review_orders"], "reviewer")
    for order in projected["review_orders"]:
        job = _job(jobs, order["job_id"])
        assignment = reviewer_assignment_by_job[job["job_id"]]
        if assignment["identity"] == job.get("worker_identity"):
            raise PilotError("reviewer identity must differ from worker identity")
    for order in projected["worker_orders"]:
        job = _job(jobs, order["job_id"])
        assignment = worker_assignment_by_job[job["job_id"]]
        order["worker_identity"] = assignment["identity"]
        order["worker_model"] = assignment["model"]
        attempt = order["attempt"]
        attempt_dir = create_attempt(root, campaign_id, job, attempt)
        write_attempt_file(attempt_dir, "input.json", _json_bytes(order))
        job.update({
            "attempt": attempt,
            "state": "running",
            "last_event": "worker_started",
            "failure_reason": None,
            "worker_identity": assignment["identity"],
            "worker_model": assignment["model"],
        })
    for order in projected["review_orders"]:
        job = _job(jobs, order["job_id"])
        assignment = reviewer_assignment_by_job[job["job_id"]]
        order["reviewer_identity"] = assignment["identity"]
        order["reviewer_model"] = assignment["model"]
        job.update({
            "state": "reviewing",
            "last_event": "review_started",
            "reviewer_identity": assignment["identity"],
            "reviewer_model": assignment["model"],
        })
    return projected


def _start_review(
    jobs: list,
    campaign: Mapping[str, Any],
    reviewer_assignments: Optional[Union[Mapping[str, Mapping[str, str]], Sequence[Mapping[str, str]]]],
) -> Optional[Dict[str, object]]:
    order = review_order(jobs)
    if order is None:
        return None
    job = _job(jobs, order["job_id"])
    if campaign.get("schema_version", 1) == 2:
        assignment = _assignment_by_job(reviewer_assignments, [order], "reviewer")[job["job_id"]]
        order["reviewer_identity"] = assignment["identity"]
        order["reviewer_model"] = assignment["model"]
        job["reviewer_identity"] = assignment["identity"]
        job["reviewer_model"] = assignment["model"]
    job["state"] = "reviewing"
    job["last_event"] = "review_started"
    return order


def run_once(
    root: Path,
    campaign_id: str,
    worker_result_path: Optional[Path] = None,
    review_result_path: Optional[Path] = None,
    available_worker_slots: Optional[int] = None,
    total_subagent_slots: Optional[int] = None,
    worker_assignments: Optional[Union[Mapping[str, Mapping[str, str]], Sequence[Mapping[str, str]]]] = None,
    reviewer_assignments: Optional[Union[Mapping[str, Mapping[str, str]], Sequence[Mapping[str, str]]]] = None,
) -> Dict[str, Any]:
    """Apply one result, then publish bounded worker and review orders."""
    if worker_result_path is not None and review_result_path is not None:
        raise PilotError("supply either a worker result or a review result, not both")
    campaign = load_campaign(root, campaign_id)
    if campaign["review_concurrency"] > 1 and total_subagent_slots is None:
        raise PilotError("parallel review requires total_subagent_slots")
    if total_subagent_slots is not None and (
        isinstance(total_subagent_slots, bool)
        or not isinstance(total_subagent_slots, int)
        or total_subagent_slots < 0
    ):
        raise PilotError("total_subagent_slots must be a non-negative integer")
    jobs = deepcopy(load_jobs(root, campaign_id))
    events = []
    pending_files = []
    if worker_result_path is not None:
        event, files = _apply_worker_result(
            root,
            campaign_id,
            jobs,
            Path(worker_result_path),
            campaign["max_attempts"],
        )
        events.append(event)
        pending_files.extend(files)
    changes_requested = False
    if review_result_path is not None:
        review_event, files = _apply_review_result(
            root, campaign_id, campaign, jobs, Path(review_result_path), campaign["max_attempts"]
        )
        events.append(review_event)
        pending_files.extend(files)
        changes_requested = review_event["event"] == "changes_requested"
    review_orders = []
    if changes_requested and total_subagent_slots is None:
        orders = []
    elif total_subagent_slots is None:
        orders = _start_workers(root, campaign_id, jobs, campaign, available_worker_slots)
    else:
        shared_orders = _start_shared_orders(
            root, campaign_id, jobs, campaign, total_subagent_slots, worker_assignments, reviewer_assignments
        )
        orders, review_orders = shared_orders["worker_orders"], shared_orders["review_orders"]
    events.extend({"event": "worker_started", "job_id": order["job_id"]} for order in orders)
    if total_subagent_slots is None:
        review = _start_review(jobs, campaign, reviewer_assignments)
        if review is not None:
            review_orders = [review]
    else:
        review = review_orders[0] if review_orders else None
    events.extend({"event": "review_started", "job_id": order["job_id"]} for order in review_orders)
    _write_pending_files(pending_files)
    save_jobs(root, campaign_id, jobs)
    warnings = []
    for event in events:
        try:
            append_event(root, campaign_id, event)
        except PilotError as error:
            warnings.append(str(error))
    output = _campaign_payload(root, campaign_id)
    output["worker_orders"] = orders
    output["review_order"] = review
    output["review_orders"] = review_orders
    if warnings:
        output["warnings"] = warnings
    return output


def status(root: Path, campaign_id: str) -> Dict[str, Any]:
    """Regenerate and return the non-authoritative campaign monitor."""
    return _campaign_payload(root, campaign_id)


def retry_job(root: Path, campaign_id: str, job_id: str) -> Dict[str, Any]:
    """Return one failed, non-exhausted job to the tail of the queue."""
    campaign = load_campaign(root, campaign_id)
    jobs = load_jobs(root, campaign_id)
    job = _job(jobs, job_id)
    if job["state"] != "failed" or job["attempt"] >= campaign["max_attempts"]:
        raise PilotError("retry requires a failed job below the attempt limit")
    job["state"] = "queued"
    job["queue_position"] = max(item["queue_position"] for item in jobs) + 1
    job["last_event"] = "retry_queued"
    job["failure_reason"] = None
    save_jobs(root, campaign_id, jobs)
    output = _campaign_payload(root, campaign_id)
    try:
        append_event(root, campaign_id, {"event": "retry_queued", "job_id": job_id})
    except PilotError as error:
        output["warnings"] = [str(error)]
    return output


def reject_job(root: Path, campaign_id: str, job_id: str, reason: str) -> Dict[str, Any]:
    """Record an operator's terminal rejection of one failed job."""
    if not isinstance(reason, str) or not reason.strip():
        raise PilotError("rejection reason is required")
    jobs = load_jobs(root, campaign_id)
    job = _job(jobs, job_id)
    if job["state"] != "failed":
        raise PilotError("reject requires a failed job")
    job["state"] = "rejected"
    job["last_event"] = "operator_rejected"
    job["failure_reason"] = reason
    save_jobs(root, campaign_id, jobs)
    output = _campaign_payload(root, campaign_id)
    try:
        append_event(root, campaign_id, {"event": "operator_rejected", "job_id": job_id, "reason": reason})
    except PilotError as error:
        output["warnings"] = [str(error)]
    return output
