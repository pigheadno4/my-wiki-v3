"""Pure work-order projections for the minimum ingest pilot."""

from copy import deepcopy
from typing import Dict, List, Optional


WORKER_RESULT_KEYS = [
    "job_id",
    "attempt",
    "source_page",
    "quotes",
    "suggestions",
    "raw_path",
    "raw_sha256",
    "status",
]


def _queued_jobs(jobs: List[dict], max_attempts: int) -> List[dict]:
    return sorted(
        (
            job
            for job in jobs
            if job["state"] == "queued" and job["attempt"] < max_attempts
        ),
        key=lambda job: job["queue_position"],
    )


def _review_context(job: dict) -> Dict[str, object]:
    retry_context = job.get("retry_context", {})
    review_scope = retry_context.get("review_scope", "full")
    return {
        "review_scope": review_scope,
        "prior_attempt": retry_context.get("prior_attempt"),
        "preferred_reviewer_identity": (
            retry_context.get("prior_reviewer_identity")
            if review_scope == "targeted" else None
        ),
    }


def worker_orders(
    jobs: List[dict],
    worker_concurrency: int,
    max_attempts: int,
    available_worker_slots: int,
) -> List[Dict[str, object]]:
    """Return queued worker orders limited by the host's current capacity."""
    slots = max(0, min(worker_concurrency, available_worker_slots))
    return [
        {
            "action": "spawn_worker",
            "job_id": job["job_id"],
            "attempt": job["attempt"] + 1,
            "raw_path": job["raw_path"],
            "raw_sha256": job["raw_sha256"],
            "source_target": job["source_target"],
            "canonical_url": job["canonical_url"],
            "contract_version": job.get("contract_version", 1),
            "result_contract": {
                "top_level_keys": WORKER_RESULT_KEYS,
                "quote_required_keys": ["text", "location"],
            },
            "preflight": [
                "Copy canonical_url exactly into source_page frontmatter.",
                "Return exactly result_contract.top_level_keys and no other top-level keys.",
                "Ensure every quote has non-empty text and location.",
            ],
            **({"retry_context": deepcopy(job["retry_context"])} if job["attempt"] > 0 and "retry_context" in job else {}),
            **{
                key: job[key]
                for key in ("recommended_worker_tier", "routing_reason")
                if key in job
            },
        }
        for job in _queued_jobs(jobs, max_attempts)[:slots]
    ]


def review_order(jobs: List[dict]) -> Optional[Dict[str, object]]:
    """Return one candidate review order unless another review is underway."""
    if any(job["state"] == "reviewing" for job in jobs):
        return None
    candidates = sorted(
        (job for job in jobs if job["state"] == "candidate_ready"),
        key=lambda job: job["queue_position"],
    )
    if not candidates:
        return None
    job = candidates[0]
    return {
        "action": "review_candidate",
        "job_id": job["job_id"],
        "attempt": job["attempt"],
        "raw_path": job["raw_path"],
        "raw_sha256": job["raw_sha256"],
        "source_target": job["source_target"],
        "contract_version": job.get("contract_version", 1),
        **_review_context(job),
    }


def _review_orders(jobs: List[dict], limit: int) -> List[Dict[str, object]]:
    candidates = sorted(
        (job for job in jobs if job["state"] == "candidate_ready"),
        key=lambda job: job["queue_position"],
    )
    return [
        {
            "action": "review_candidate",
            "job_id": job["job_id"],
            "attempt": job["attempt"],
            "raw_path": job["raw_path"],
            "raw_sha256": job["raw_sha256"],
            "source_target": job["source_target"],
            "contract_version": job.get("contract_version", 1),
            **_review_context(job),
        }
        for job in candidates[:max(0, limit)]
    ]


def shared_slot_orders(
    jobs: List[dict],
    worker_concurrency: int,
    review_concurrency: int,
    max_attempts: int,
    total_subagent_slots: int,
) -> Dict[str, List[Dict[str, object]]]:
    """Project review-first orders within one shared host slot budget."""
    active_workers = sum(job["state"] == "running" for job in jobs)
    active_reviewers = sum(job["state"] == "reviewing" for job in jobs)
    free_slots = max(0, total_subagent_slots - active_workers - active_reviewers)
    queued = _queued_jobs(jobs, max_attempts)
    worker_reserve = 1 if queued and active_workers == 0 else 0
    review_slots = min(
        len([job for job in jobs if job["state"] == "candidate_ready"]),
        max(0, review_concurrency - active_reviewers),
        max(0, free_slots - worker_reserve),
    )
    reviews = _review_orders(jobs, review_slots)
    remaining_slots = free_slots - len(reviews)
    workers = worker_orders(
        jobs,
        max(0, worker_concurrency - active_workers),
        max_attempts,
        remaining_slots,
    )
    return {"worker_orders": workers, "review_orders": reviews}
