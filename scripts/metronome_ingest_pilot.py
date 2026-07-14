#!/usr/bin/env python3
"""Deterministic job and receipt validation for Metronome ingest pilots."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, List


COMMIT_RE = re.compile(r"^[0-9a-f]{7,40}$")


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _missing(data: Dict[str, Any], fields: List[str], prefix: str) -> List[str]:
    return [f"{prefix}: {field} is required" for field in fields if data.get(field) in (None, "", [])]


def validate_job(root: Path, job: Dict[str, Any]) -> List[str]:
    errors = _missing(
        job,
        [
            "schema_version",
            "job_id",
            "provider",
            "canonical_url",
            "raw_path",
            "source_page",
            "concept_leases",
            "role",
            "allowed_write_paths",
            "forbidden_write_paths",
            "forbidden_write_prefixes",
        ],
        "job",
    )
    if job.get("provider") != "metronome":
        errors.append("job: provider must be metronome")

    raw_path = str(job.get("raw_path", ""))
    if raw_path and not raw_path.startswith("raw/metronome/"):
        errors.append("job: raw_path must stay inside raw/metronome/")
    if raw_path and not (root / raw_path).is_file():
        errors.append(f"job: raw_path does not exist: {raw_path}")

    source_page = str(job.get("source_page", ""))
    if source_page and not source_page.startswith("wiki/sources/metronome/"):
        errors.append("job: source_page must stay inside wiki/sources/metronome/")

    concepts = job.get("concept_leases", [])
    if isinstance(concepts, list):
        for concept in concepts:
            if not str(concept).startswith("wiki/concepts/metronome/"):
                errors.append(f"job: concept lease is outside Metronome concepts: {concept}")

    allowed = set(job.get("allowed_write_paths", []))
    forbidden = set(job.get("forbidden_write_paths", []))
    overlap = sorted(allowed & forbidden)
    if overlap:
        errors.append(f"job: allowed and forbidden write paths overlap: {overlap}")

    expected_allowed = {source_page} | set(concepts if isinstance(concepts, list) else [])
    if source_page and allowed != expected_allowed:
        errors.append("job: allowed_write_paths must equal source_page plus concept_leases")

    prefixes = job.get("forbidden_write_prefixes", [])
    for path in sorted(allowed):
        if any(path.startswith(str(prefix)) for prefix in prefixes):
            errors.append(f"job: allowed path is under a forbidden prefix: {path}")
    return errors


def validate_receipt(
    root: Path, job: Dict[str, Any], receipt: Dict[str, Any]
) -> List[str]:
    errors = _missing(
        receipt,
        [
            "schema_version",
            "job_id",
            "provider",
            "canonical_url",
            "raw_path",
            "source_page",
            "status",
            "grounding_quotes",
            "files_changed",
            "validation",
            "worker",
            "review",
        ],
        "receipt",
    )
    for field in ("job_id", "provider", "canonical_url", "raw_path", "source_page"):
        if receipt.get(field) != job.get(field):
            errors.append(f"receipt: {field} does not match job")

    changed = set(receipt.get("files_changed", []))
    allowed = set(job.get("allowed_write_paths", []))
    outside = sorted(changed - allowed)
    if outside:
        errors.append(f"receipt: files_changed outside allowed_write_paths: {outside}")

    quotes = receipt.get("grounding_quotes", [])
    if not isinstance(quotes, list) or not 3 <= len(quotes) <= 5:
        errors.append("receipt: grounding_quotes must contain 3 to 5 entries")
        quotes = []
    raw_path = root / str(job.get("raw_path", ""))
    raw_lines = raw_path.read_text(encoding="utf-8").splitlines() if raw_path.is_file() else []
    for index, quote in enumerate(quotes, 1):
        start = quote.get("line_start") if isinstance(quote, dict) else None
        end = quote.get("line_end") if isinstance(quote, dict) else None
        text = quote.get("text") if isinstance(quote, dict) else None
        if not isinstance(start, int) or not isinstance(end, int) or start < 1 or end < start or end > len(raw_lines):
            errors.append(f"receipt: grounding quote {index} has invalid line bounds")
            continue
        expected = "\n".join(raw_lines[start - 1:end])
        if text != expected:
            errors.append(
                f"receipt: grounding quote {index} does not match raw lines {start}-{end}"
            )

    if receipt.get("status") == "success":
        worker_commit = str(receipt.get("worker_commit", ""))
        if not COMMIT_RE.match(worker_commit):
            errors.append("receipt: successful status requires a valid worker_commit")

        validation = receipt.get("validation", [])
        if not isinstance(validation, list) or not validation:
            errors.append("receipt: successful status requires validation commands")
        else:
            for item in validation:
                if not isinstance(item, dict) or not item.get("command"):
                    errors.append("receipt: validation command is required")
                if not isinstance(item, dict) or item.get("passed") is not True:
                    errors.append("receipt: validation command did not pass")

        worker = receipt.get("worker", {})
        if not isinstance(worker, dict):
            worker = {}
        if worker.get("role") != job.get("role"):
            errors.append("receipt: worker role does not match job")
        if not worker.get("model_provider"):
            errors.append("receipt: worker model_provider is required")
        if not worker.get("model"):
            errors.append("receipt: worker model is required")
        if worker.get("token_usage") is None and not worker.get(
            "token_usage_unavailable_reason"
        ):
            errors.append(
                "receipt: null token_usage requires token_usage_unavailable_reason"
            )

        review = receipt.get("review", {})
        if not isinstance(review, dict) or review.get("status") != "approved":
            errors.append("receipt: review status must be approved")
        if not isinstance(review, dict) or not review.get("reviewer"):
            errors.append("receipt: review reviewer is required")
    return errors
