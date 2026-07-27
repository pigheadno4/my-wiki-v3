"""One-process dry-run transitions for the minimum ingest pilot."""

import json
from pathlib import Path
from typing import Any, Dict, Mapping, Optional, Union

from .scheduler import review_order, worker_orders
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


REVIEW_RESULT_KEYS = {"job_id", "attempt", "verdict", "reason", "required_changes"}
REVIEW_VERDICTS = {"approved", "changes_requested", "rejected"}


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


def _apply_worker_result(root: Path, campaign_id: str, jobs: list, result_path: Path) -> Dict[str, Any]:
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
        job["state"] = "failed"
        job["last_event"] = "worker_result_invalid"
        job["failure_reason"] = str(error)
        write_attempt_file(attempt_dir, "failure.json", _json_bytes({"reason": str(error)}))
        return {"event": "worker_result_invalid", "job_id": job["job_id"], "reason": str(error)}

    write_attempt_file(attempt_dir, "candidate.md", validated["source_page"].encode("utf-8"))
    write_attempt_file(attempt_dir, "receipt.json", _json_bytes(validated))
    write_attempt_file(attempt_dir, "suggestions.json", _json_bytes(validated["suggestions"]))
    job["state"] = "candidate_ready"
    job["last_event"] = "candidate_ready"
    job["failure_reason"] = None
    return {"event": "candidate_ready", "job_id": job["job_id"]}


def _apply_review_result(jobs: list, result_path: Path, max_attempts: int) -> Dict[str, Any]:
    result = _load_result(result_path)
    if set(result) != REVIEW_RESULT_KEYS:
        raise PilotError("review result must use the fixed schema")
    job = _job(jobs, result["job_id"])
    if job["state"] != "reviewing" or result["attempt"] != job["attempt"]:
        raise PilotError("review result does not match a reviewing job")
    verdict = result["verdict"]
    reason = result["reason"]
    changes = result["required_changes"]
    if verdict not in REVIEW_VERDICTS or not isinstance(reason, str) or not reason or not isinstance(changes, list):
        raise PilotError("review result is invalid")
    if verdict == "approved":
        job["state"] = "approved"
        job["last_event"] = "review_approved"
        job["failure_reason"] = None
        return {"event": "review_approved", "job_id": job["job_id"]}
    if verdict == "rejected" or job["attempt"] >= max_attempts:
        job["state"] = "rejected"
        job["last_event"] = "review_rejected" if verdict == "rejected" else "changes_exhausted"
        job["failure_reason"] = reason
        return {"event": job["last_event"], "job_id": job["job_id"], "reason": reason}
    job["state"] = "queued"
    job["queue_position"] = max(item["queue_position"] for item in jobs) + 1
    job["last_event"] = "changes_requested"
    job["failure_reason"] = None
    return {"event": "changes_requested", "job_id": job["job_id"], "reason": reason}


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


def _start_review(jobs: list) -> Optional[Dict[str, object]]:
    order = review_order(jobs)
    if order is None:
        return None
    job = _job(jobs, order["job_id"])
    job["state"] = "reviewing"
    job["last_event"] = "review_started"
    return order


def run_once(
    root: Path,
    campaign_id: str,
    worker_result_path: Optional[Path] = None,
    review_result_path: Optional[Path] = None,
    available_worker_slots: Optional[int] = None,
) -> Dict[str, Any]:
    """Apply one result, then publish bounded worker and review orders."""
    if worker_result_path is not None and review_result_path is not None:
        raise PilotError("supply either a worker result or a review result, not both")
    campaign = load_campaign(root, campaign_id)
    jobs = load_jobs(root, campaign_id)
    events = []
    if worker_result_path is not None:
        events.append(_apply_worker_result(root, campaign_id, jobs, Path(worker_result_path)))
    changes_requested = False
    if review_result_path is not None:
        review_event = _apply_review_result(jobs, Path(review_result_path), campaign["max_attempts"])
        events.append(review_event)
        changes_requested = review_event["event"] == "changes_requested"
    orders = [] if changes_requested else _start_workers(
        root, campaign_id, jobs, campaign, available_worker_slots
    )
    events.extend({"event": "worker_started", "job_id": order["job_id"]} for order in orders)
    review = _start_review(jobs)
    if review is not None:
        events.append({"event": "review_started", "job_id": review["job_id"]})
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
