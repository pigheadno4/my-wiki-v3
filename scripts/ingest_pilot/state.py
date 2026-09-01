"""Trusted local state for the minimum Metronome dry-run pilot."""

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Mapping, Union


SCHEMA_VERSION = 2
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


def _utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


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


def _replace_campaign(path: Path, campaign: Mapping[str, Any]) -> None:
    temporary = path.with_name(path.name + ".tmp")
    if temporary.exists():
        raise PilotError("temporary campaign file already exists")
    try:
        with temporary.open("xb") as output:
            output.write(_json_bytes(campaign))
            output.flush()
            os.fsync(output.fileno())
        os.replace(temporary, path)
    except PilotError:
        raise
    except OSError as error:
        raise PilotError("cannot save campaign.json") from error


def _review_counts(campaign_dir: Path) -> Dict[str, int]:
    counts = {"full": 0, "targeted": 0}
    for review_path in (campaign_dir / "attempts").glob("*/attempt-*/review.json"):
        review = _load_json(review_path)
        scope = review.get("review_scope") if isinstance(review, dict) else None
        if scope in counts:
            counts[scope] += 1
    return counts


def _write_monitor(campaign_dir: Path, campaign: Mapping[str, Any], jobs: List[Dict[str, Any]]) -> str:
    counts = {state: sum(job.get("state") == state for job in jobs) for state in (
        "queued",
        "running",
        "candidate_ready",
        "risk_pending",
        "review_deferred",
        "reviewing",
        "approved",
        "failed",
        "rejected",
    )}
    review_counts = _review_counts(campaign_dir)
    started_at = campaign.get("started_at", "not recorded")
    completed_at = campaign.get("completed_at")
    completed_display = completed_at if completed_at is not None else "incomplete"
    elapsed = "in progress"
    if isinstance(started_at, str) and isinstance(completed_at, str):
        try:
            elapsed_seconds = int(
                (datetime.strptime(completed_at, "%Y-%m-%dT%H:%M:%SZ")
                 - datetime.strptime(started_at, "%Y-%m-%dT%H:%M:%SZ")).total_seconds()
            )
            elapsed = f"{elapsed_seconds} seconds"
        except ValueError:
            elapsed = "unavailable"
    title = str(campaign["campaign_id"]).replace("-", " ").title()
    lines = [
        f"# {title}",
        "",
        f"- Campaign state: `{campaign['state']}`",
        f"- Worker concurrency: `{campaign['worker_concurrency']}`",
        f"- Started at: `{started_at}`",
        f"- Completed at: `{completed_display}`",
        f"- Full reviews: {review_counts['full']}",
        f"- Targeted reviews: {review_counts['targeted']}",
        f"- Coordinator repairs: {campaign.get('coordinator_repairs', 0)}",
        f"- Elapsed: `{elapsed}`",
        f"- Queued: {counts['queued']}",
        f"- Running: {counts['running']}",
        f"- Candidate ready: {counts['candidate_ready']}",
        f"- Risk pending: {counts['risk_pending']}",
        f"- Review deferred: {counts['review_deferred']}",
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
    review_policy = manifest.get("review_policy", "per_page")
    if review_policy == "audit_only":
        raise PilotError("audit_only review_policy is not authorized")
    if review_policy not in {"per_page", "risk_gated"}:
        raise PilotError("review_policy must be per_page or risk_gated")
    review_concurrency = manifest.get("review_concurrency", 1)
    if isinstance(review_concurrency, bool) or not isinstance(review_concurrency, int) or review_concurrency < 1:
        raise PilotError("review_concurrency must be a positive integer")
    job_ids = {source.get("job_id") for source in manifest["jobs"]}
    risk_configuration: Dict[str, Any] = {}
    if review_policy == "risk_gated":
        sample_job_id = manifest.get("risk_sample_job_id")
        routes = [source.get("initial_review_route") for source in manifest["jobs"]]
        if (
            not isinstance(sample_job_id, str)
            or sample_job_id not in job_ids
            or any(route not in {"mandatory", "provisional"} for route in routes)
        ):
            raise PilotError("risk_gated review requires one sample and a route for every job")
        sample = next(source for source in manifest["jobs"] if source["job_id"] == sample_job_id)
        if sample["initial_review_route"] != "provisional":
            raise PilotError("risk_gated sample job must be provisional")
        risk_configuration = {
            "risk_sample_job_id": sample_job_id,
            "risk_gate": "pending",
        }
    elif "risk_sample_job_id" in manifest or any(
        "initial_review_route" in source for source in manifest["jobs"]
    ):
        raise PilotError("risk_gated fields require review_policy risk_gated")
    if "audit_job_ids" not in manifest:
        if review_policy == "risk_gated":
            raise PilotError("risk_gated review requires three audit job IDs")
        if review_concurrency > 1:
            raise PilotError("parallel review requires audit_job_ids")
        configuration = {"review_concurrency": review_concurrency, **risk_configuration}
        if "review_policy" in manifest:
            configuration["review_policy"] = review_policy
        return configuration
    audit_job_ids = manifest["audit_job_ids"]
    if (
        not isinstance(audit_job_ids, list)
        or len(audit_job_ids) != 3
        or any(not isinstance(job_id, str) or not job_id for job_id in audit_job_ids)
        or len(set(audit_job_ids)) != 3
        or any(job_id not in job_ids for job_id in audit_job_ids)
    ):
        raise PilotError("audit_job_ids must contain three distinct manifest job IDs")
    if review_policy == "risk_gated":
        route_by_job = {
            source["job_id"]: source["initial_review_route"] for source in manifest["jobs"]
        }
        sample_job_id = risk_configuration["risk_sample_job_id"]
        if (
            sample_job_id not in audit_job_ids
            or not any(route_by_job[job_id] == "mandatory" for job_id in audit_job_ids)
            or not any(
                job_id != sample_job_id and route_by_job[job_id] == "provisional"
                for job_id in audit_job_ids
            )
        ):
            raise PilotError("risk_gated audit must include mandatory, sample, and provisional jobs")
    configuration = {
        "review_concurrency": review_concurrency,
        "audit_job_ids": list(audit_job_ids),
        **risk_configuration,
    }
    if "review_policy" in manifest:
        configuration["review_policy"] = review_policy
    return configuration


def initialize_state(root: Path, manifest: Union[Path, Mapping[str, Any]]) -> None:
    manifest_data = _manifest_data(manifest)
    campaign_id = manifest_data["campaign_id"]
    paths = campaign_paths(root, campaign_id)
    campaign_dir = paths["campaign_dir"]
    if paths["campaign"].exists() or paths["jobs"].exists():
        raise PilotError("campaign is already initialized")
    review_configuration = _review_configuration(manifest_data)
    worker_concurrency = manifest_data.get("worker_concurrency", 5)
    if (
        isinstance(worker_concurrency, bool)
        or not isinstance(worker_concurrency, int)
        or worker_concurrency < 1
    ):
        raise PilotError("worker_concurrency must be a positive integer")
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
            "worker_concurrency": worker_concurrency,
            "max_attempts": 3,
            **review_configuration,
            "mode": "dry_run",
            "started_at": _utc_now(),
            "completed_at": None,
            "coordinator_repairs": 0,
        }
        _replace_campaign(paths["campaign"], campaign)
        jobs = [
            {
                "job_id": source["job_id"],
                "raw_path": source["raw_path"],
                "raw_sha256": source["raw_sha256"],
                "source_target": source["source_target"],
                "canonical_url": source["canonical_url"],
                "contract_version": 2,
                **routing_metadata[position - 1],
                **(
                    {"initial_review_route": source["initial_review_route"]}
                    if review_configuration.get("review_policy") == "risk_gated"
                    else {}
                ),
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


def save_campaign(root: Path, campaign_id: str, campaign: Mapping[str, Any]) -> None:
    paths = campaign_paths(root, campaign_id)
    _replace_campaign(paths["campaign"], campaign)
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
