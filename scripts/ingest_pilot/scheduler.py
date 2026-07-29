"""Pure work-order projections for the minimum ingest pilot."""

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
            "result_contract": {
                "top_level_keys": WORKER_RESULT_KEYS,
                "quote_required_keys": ["text", "location"],
            },
            "preflight": [
                "Copy canonical_url exactly into source_page frontmatter.",
                "Return exactly result_contract.top_level_keys and no other top-level keys.",
                "Ensure every quote has non-empty text and location.",
            ],
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
    }
