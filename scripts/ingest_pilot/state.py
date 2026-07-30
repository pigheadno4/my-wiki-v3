"""Trusted local state for the minimum Metronome dry-run pilot."""

import json
import os
from pathlib import Path
from typing import Any, Dict, List, Mapping, Union


SCHEMA_VERSION = 1
WORKER_TIERS = {"standard", "strong"}


class PilotError(Exception):
    """Raised when trusted pilot state cannot be read or written."""


def campaign_paths(root: Path, campaign_id: str) -> Dict[str, Path]:
    campaign_dir = root / "tracking" / "ingest" / "metronome" / campaign_id
    return {
        "campaign_dir": campaign_dir,
        "manifest": campaign_dir / "manifest.json",
        "campaign": campaign_dir / "campaign.json",
        "jobs": campaign_dir / "jobs.json",
        "jobs_tmp": campaign_dir / "jobs.json.tmp",
        "events": campaign_dir / "events.jsonl",
        "monitor": campaign_dir / "monitor.md",
        "attempts": campaign_dir / "attempts",
    }


def _load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise PilotError(f"cannot read {path.name}") from error


def load_campaign(root: Path, campaign_id: str) -> Dict[str, Any]:
    campaign = _load_json(campaign_paths(root, campaign_id)["campaign"])
    if not isinstance(campaign, dict):
        raise PilotError("campaign.json must contain an object")
    return campaign


def load_jobs(root: Path, campaign_id: str) -> List[Dict[str, Any]]:
    jobs = _load_json(campaign_paths(root, campaign_id)["jobs"])
    if not isinstance(jobs, list):
        raise PilotError("jobs.json must contain a list")
    return jobs


def _json_bytes(value: Any) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=False) + "\n").encode("utf-8")


def _replace_jobs(path: Path, jobs: List[Dict[str, Any]]) -> None:
    temporary = path.with_name(path.name + ".tmp")
    if temporary.exists():
        raise PilotError("temporary jobs file already exists")
    try:
        with temporary.open("xb") as output:
            output.write(_json_bytes(jobs))
            output.flush()
            os.fsync(output.fileno())
        os.replace(temporary, path)
    except PilotError:
        raise
    except OSError as error:
        raise PilotError("cannot save jobs.json") from error


def _write_monitor(campaign_dir: Path, campaign: Mapping[str, Any], jobs: List[Dict[str, Any]]) -> str:
    counts = {state: sum(job.get("state") == state for job in jobs) for state in (
        "queued",
        "running",
        "candidate_ready",
        "reviewing",
        "approved",
        "failed",
        "rejected",
    )}
    title = str(campaign["campaign_id"]).replace("-", " ").title()
    lines = [
        f"# {title}",
        "",
        f"- Campaign state: `{campaign['state']}`",
        f"- Worker concurrency: `{campaign['worker_concurrency']}`",
        f"- Queued: {counts['queued']}",
        f"- Running: {counts['running']}",
        f"- Candidate ready: {counts['candidate_ready']}",
        f"- Reviewing: {counts['reviewing']}",
        f"- Approved: {counts['approved']}",
        f"- Failed: {counts['failed']}",
        f"- Rejected: {counts['rejected']}",
        "",
        "| Job | Attempt | State | Raw | Source target | Last event | Failure |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for job in jobs:
        lines.append(
            f"| {job['job_id']} | {job['attempt']} | {job['state']} | {job['raw_path']} "
            f"| {job['source_target']} | {job['last_event']} | {job['failure_reason'] or ''} |"
        )
    monitor = "\n".join(lines) + "\n"
    try:
        (campaign_dir / "monitor.md").write_text(monitor, encoding="utf-8")
    except OSError as error:
        raise PilotError("cannot write monitor.md") from error
    return monitor


def render_monitor(root: Path, campaign_id: str) -> str:
    paths = campaign_paths(root, campaign_id)
    return _write_monitor(paths["campaign_dir"], load_campaign(root, campaign_id), load_jobs(root, campaign_id))


def _manifest_data(manifest: Union[Path, Mapping[str, Any]]) -> Dict[str, Any]:
    if isinstance(manifest, Path):
        data = _load_json(manifest)
    else:
        data = dict(manifest)
    if not isinstance(data, dict):
        raise PilotError("manifest.json must contain an object")
    return data


def _routing_metadata(source: Mapping[str, Any]) -> Dict[str, str]:
    tier_present = "recommended_worker_tier" in source
    reason_present = "routing_reason" in source
    if tier_present != reason_present:
        raise PilotError(
            "worker routing requires both recommended_worker_tier and routing_reason"
        )
    if not tier_present:
        return {}
    tier = source["recommended_worker_tier"]
    reason = source["routing_reason"]
    if not isinstance(tier, str) or tier not in WORKER_TIERS:
        raise PilotError("recommended_worker_tier must be standard or strong")
    if not isinstance(reason, str) or not reason.strip():
        raise PilotError("routing_reason must be non-empty text")
    return {
        "recommended_worker_tier": tier,
        "routing_reason": reason,
    }


def _review_configuration(manifest: Mapping[str, Any]) -> Dict[str, Any]:
    review_concurrency = manifest.get("review_concurrency", 1)
    if isinstance(review_concurrency, bool) or not isinstance(review_concurrency, int) or review_concurrency < 1:
        raise PilotError("review_concurrency must be a positive integer")
    audit_job_ids = manifest.get("audit_job_ids")
    if audit_job_ids is None:
        if review_concurrency > 1:
            raise PilotError("parallel review requires audit_job_ids")
        return {"review_concurrency": review_concurrency}
    job_ids = {source.get("job_id") for source in manifest["jobs"]}
    if (
        not isinstance(audit_job_ids, list)
        or len(audit_job_ids) != 3
        or any(not isinstance(job_id, str) or not job_id for job_id in audit_job_ids)
        or len(set(audit_job_ids)) != 3
        or any(job_id not in job_ids for job_id in audit_job_ids)
    ):
        raise PilotError("audit_job_ids must contain three distinct manifest job IDs")
    return {"review_concurrency": review_concurrency, "audit_job_ids": list(audit_job_ids)}


def initialize_state(root: Path, manifest: Union[Path, Mapping[str, Any]]) -> None:
    manifest_data = _manifest_data(manifest)
    campaign_id = manifest_data["campaign_id"]
    paths = campaign_paths(root, campaign_id)
    campaign_dir = paths["campaign_dir"]
    if paths["campaign"].exists() or paths["jobs"].exists():
        raise PilotError("campaign is already initialized")
    review_configuration = _review_configuration(manifest_data)
    routing_metadata = [
        _routing_metadata(source) for source in manifest_data["jobs"]
    ]
    try:
        campaign_dir.mkdir(parents=True, exist_ok=True)
        if paths["manifest"].exists():
            if _load_json(paths["manifest"]) != manifest_data:
                raise PilotError("destination manifest does not match input")
        else:
            paths["manifest"].write_bytes(_json_bytes(manifest_data))
        campaign = {
            "schema_version": SCHEMA_VERSION,
            "campaign_id": campaign_id,
            "provider": "metronome",
            "state": "active",
            "worker_concurrency": 5,
            "max_attempts": 3,
            **review_configuration,
            "mode": "dry_run",
        }
        paths["campaign"].write_bytes(_json_bytes(campaign))
        jobs = [
            {
                "job_id": source["job_id"],
                "raw_path": source["raw_path"],
                "raw_sha256": source["raw_sha256"],
                "source_target": source["source_target"],
                "canonical_url": source["canonical_url"],
                **routing_metadata[position - 1],
                "state": "queued",
                "attempt": 0,
                "queue_position": position,
                "last_event": "initialized",
                "failure_reason": None,
            }
            for position, source in enumerate(manifest_data["jobs"], start=1)
        ]
        with paths["events"].open("x", encoding="utf-8") as events:
            events.write(
                "".join(
                    json.dumps({"event": "initialized", "job_id": job["job_id"]}, separators=(",", ":"))
                    + "\n"
                    for job in jobs
                )
            )
        _replace_jobs(paths["jobs"], jobs)
        _write_monitor(campaign_dir, campaign, jobs)
    except FileExistsError as error:
        raise PilotError("events.jsonl already exists") from error
    except (KeyError, OSError, TypeError) as error:
        raise PilotError("cannot initialize campaign") from error


def save_jobs(root: Path, campaign_id: str, jobs: List[Dict[str, Any]]) -> None:
    paths = campaign_paths(root, campaign_id)
    _replace_jobs(paths["jobs"], jobs)
    render_monitor(root, campaign_id)


def append_event(root: Path, campaign_id: str, event: Mapping[str, Any]) -> None:
    paths = campaign_paths(root, campaign_id)
    try:
        with paths["events"].open("a", encoding="utf-8") as output:
            output.write(json.dumps(dict(event), separators=(",", ":")) + "\n")
    except (OSError, TypeError) as error:
        raise PilotError("cannot append event") from error
    render_monitor(root, campaign_id)


def create_attempt(root: Path, campaign_id: str, job: Mapping[str, Any], attempt: int) -> Path:
    paths = campaign_paths(root, campaign_id)
    attempt_dir = paths["attempts"] / str(job["job_id"]) / f"attempt-{attempt}"
    if attempt_dir.exists():
        raise PilotError("attempt directory already exists")
    try:
        attempt_dir.mkdir(parents=True)
    except OSError as error:
        raise PilotError("cannot create attempt directory") from error
    render_monitor(root, campaign_id)
    return attempt_dir


def write_attempt_file(attempt_dir: Path, filename: str, content: bytes) -> None:
    destination = attempt_dir / filename
    try:
        with destination.open("xb") as output:
            output.write(content)
    except FileExistsError as error:
        raise PilotError(f"attempt file already exists: {filename}") from error
    except OSError as error:
        raise PilotError(f"cannot write attempt file: {filename}") from error
    campaign_dir = attempt_dir.parent.parent.parent
    campaign = _load_json(campaign_dir / "campaign.json")
    jobs = _load_json(campaign_dir / "jobs.json")
    _write_monitor(campaign_dir, campaign, jobs)


def recover_interrupted(root: Path, campaign_id: str) -> List[Dict[str, Any]]:
    jobs = load_jobs(root, campaign_id)
    interrupted = []
    for job in jobs:
        if job["state"] in ("running", "reviewing"):
            job["state"] = "failed"
            job["last_event"] = "interrupted"
            job["failure_reason"] = "interrupted"
            interrupted.append(job["job_id"])
    if interrupted:
        save_jobs(root, campaign_id, jobs)
        for job_id in interrupted:
            append_event(root, campaign_id, {"event": "interrupted", "job_id": job_id})
    else:
        render_monitor(root, campaign_id)
    return jobs
