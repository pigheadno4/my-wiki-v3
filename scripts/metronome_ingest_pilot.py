#!/usr/bin/env python3
"""Deterministic job and receipt validation for Metronome ingest pilots."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, List, Sequence


COMMIT_RE = re.compile(r"^[0-9a-f]{7,40}$")
RAW_LINK_RE = re.compile(r"^\[\[([^|\]]+)\|[^\]]+\]\]$")
LUNA_MODEL = "gpt-5.6-luna"
SOL_MODEL = "gpt-5.6-sol"
TERRA_MODEL = "gpt-5.6-terra"
LUNA_REASONING_EFFORT = "high"
TERRA_REASONING_EFFORT = "medium"
LUNA_RUN_ROOT = "tracking/ingest/metronome/pilot/runs/"
MODEL_PROFILES = {
    LUNA_MODEL: LUNA_REASONING_EFFORT,
    TERRA_MODEL: TERRA_REASONING_EFFORT,
}


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _missing(data: Dict[str, Any], fields: List[str], prefix: str) -> List[str]:
    return [f"{prefix}: {field} is required" for field in fields if data.get(field) in (None, "", [])]


def _is_under(path: str, directory: str) -> bool:
    normalized = directory.rstrip("/")
    return path == normalized or path.startswith(f"{normalized}/")


def _validate_quotes(
    root: Path,
    job: Dict[str, Any],
    quotes: Any,
    prefix: str,
) -> List[str]:
    errors: List[str] = []
    if not isinstance(quotes, list) or not 3 <= len(quotes) <= 5:
        return [f"{prefix}: grounding_quotes must contain 3 to 5 entries"]
    raw_path = root / str(job.get("raw_path", ""))
    raw_lines = raw_path.read_text(encoding="utf-8").splitlines() if raw_path.is_file() else []
    for index, quote in enumerate(quotes, 1):
        start = quote.get("line_start") if isinstance(quote, dict) else None
        end = quote.get("line_end") if isinstance(quote, dict) else None
        text = quote.get("text") if isinstance(quote, dict) else None
        if (
            not isinstance(start, int)
            or not isinstance(end, int)
            or start < 1
            or end < start
            or end > len(raw_lines)
        ):
            errors.append(f"{prefix}: grounding quote {index} has invalid line bounds")
            continue
        expected = "\n".join(raw_lines[start - 1 : end])
        if text != expected:
            errors.append(
                f"{prefix}: grounding quote {index} does not match raw lines {start}-{end}"
            )
    return errors


def _validate_validation_results(validation: Any, prefix: str) -> List[str]:
    if not isinstance(validation, list) or not validation:
        return [f"{prefix}: successful status requires validation commands"]
    errors: List[str] = []
    for item in validation:
        if not isinstance(item, dict) or not item.get("command"):
            errors.append(f"{prefix}: validation command is required")
        if not isinstance(item, dict) or item.get("passed") is not True:
            errors.append(f"{prefix}: validation command did not pass")
    return errors


def validate_job(root: Path, job: Dict[str, Any]) -> List[str]:
    if job.get("schema_version") == 3:
        return _validate_model_job(root, job)
    if job.get("schema_version") == 2:
        return _validate_luna_job(root, job)
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


def _validate_model_job(root: Path, job: Dict[str, Any]) -> List[str]:
    errors = _missing(
        job,
        [
            "schema_version",
            "job_id",
            "provider",
            "mode",
            "canonical_url",
            "raw_path",
            "source_page",
            "artifact_dir",
            "role",
            "model_provider",
            "model",
            "reasoning_effort",
            "allowed_write_paths",
            "forbidden_write_paths",
            "forbidden_write_prefixes",
        ],
        "job",
    )
    if job.get("provider") != "metronome":
        errors.append("job: provider must be metronome")
    if job.get("mode") not in ("real_ingest", "shadow"):
        errors.append("job: mode must be real_ingest or shadow")
    if job.get("role") != "cheap_ingester":
        errors.append("job: role must be cheap_ingester")
    if job.get("model_provider") != "openai":
        errors.append("job: model_provider must be openai")
    model = job.get("model")
    if model not in MODEL_PROFILES or job.get("reasoning_effort") != MODEL_PROFILES.get(model):
        errors.append("job: unsupported model/reasoning pair")

    raw_path = str(job.get("raw_path", ""))
    if raw_path and not raw_path.startswith("raw/metronome/"):
        errors.append("job: raw_path must stay inside raw/metronome/")
    if raw_path and not (root / raw_path).is_file():
        errors.append(f"job: raw_path does not exist: {raw_path}")
    source_page = str(job.get("source_page", ""))
    if source_page and not source_page.startswith("wiki/sources/metronome/"):
        errors.append("job: source_page must stay inside wiki/sources/metronome/")

    artifact_dir = str(job.get("artifact_dir", ""))
    expected_dir = f"{LUNA_RUN_ROOT}{job.get('job_id', '')}"
    if artifact_dir and artifact_dir != expected_dir:
        errors.append("job: artifact_dir must match the job ID under the model run root")
    if job.get("allowed_write_paths", []) != [artifact_dir]:
        errors.append("job: allowed_write_paths must contain only artifact_dir")
    if artifact_dir in set(job.get("forbidden_write_paths", [])):
        errors.append("job: allowed and forbidden write paths overlap")
    prefixes = set(job.get("forbidden_write_prefixes", []))
    if "raw/" not in prefixes or "wiki/" not in prefixes:
        errors.append("job: model jobs must forbid raw/ and wiki/ prefixes")
    return errors


def _validate_luna_job(root: Path, job: Dict[str, Any]) -> List[str]:
    errors = _missing(
        job,
        [
            "schema_version",
            "job_id",
            "provider",
            "mode",
            "canonical_url",
            "raw_path",
            "source_page",
            "artifact_dir",
            "role",
            "model_provider",
            "model",
            "reasoning_effort",
            "allowed_write_paths",
            "forbidden_write_paths",
            "forbidden_write_prefixes",
        ],
        "job",
    )
    if job.get("provider") != "metronome":
        errors.append("job: provider must be metronome")
    if job.get("mode") not in ("real_ingest", "shadow"):
        errors.append("job: mode must be real_ingest or shadow")
    if job.get("role") != "cheap_ingester":
        errors.append("job: role must be cheap_ingester")
    if job.get("model_provider") != "openai":
        errors.append("job: model_provider must be openai")
    if job.get("model") != LUNA_MODEL:
        errors.append(f"job: model must be {LUNA_MODEL}")
    if job.get("reasoning_effort") != LUNA_REASONING_EFFORT:
        errors.append(f"job: reasoning_effort must be {LUNA_REASONING_EFFORT}")

    raw_path = str(job.get("raw_path", ""))
    if raw_path and not raw_path.startswith("raw/metronome/"):
        errors.append("job: raw_path must stay inside raw/metronome/")
    if raw_path and not (root / raw_path).is_file():
        errors.append(f"job: raw_path does not exist: {raw_path}")

    source_page = str(job.get("source_page", ""))
    if source_page and not source_page.startswith("wiki/sources/metronome/"):
        errors.append("job: source_page must stay inside wiki/sources/metronome/")

    artifact_dir = str(job.get("artifact_dir", ""))
    expected_dir = f"{LUNA_RUN_ROOT}{job.get('job_id', '')}"
    if artifact_dir and artifact_dir != expected_dir:
        errors.append("job: artifact_dir must match the job ID under the Luna run root")

    allowed = job.get("allowed_write_paths", [])
    if allowed != [artifact_dir]:
        errors.append("job: allowed_write_paths must contain only artifact_dir")
    forbidden = set(job.get("forbidden_write_paths", []))
    if artifact_dir in forbidden:
        errors.append("job: allowed and forbidden write paths overlap")
    prefixes = set(job.get("forbidden_write_prefixes", []))
    if "raw/" not in prefixes or "wiki/" not in prefixes:
        errors.append("job: Luna jobs must forbid raw/ and wiki/ prefixes")
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

    errors.extend(_validate_quotes(root, job, receipt.get("grounding_quotes", []), "receipt"))

    if receipt.get("status") == "success":
        worker_commit = str(receipt.get("worker_commit", ""))
        if not COMMIT_RE.match(worker_commit):
            errors.append("receipt: successful status requires a valid worker_commit")

        errors.extend(_validate_validation_results(receipt.get("validation", []), "receipt"))

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


def validate_luna_output(
    root: Path, job: Dict[str, Any], output: Dict[str, Any]
) -> List[str]:
    errors = _missing(
        output,
        [
            "job_id",
            "raw_path",
            "canonical_url",
            "title",
            "grounding_quotes",
            "overview",
            "key_takeaways",
            "details",
            "suggested_tags",
            "proposed_raw_link",
        ],
        "luna output",
    )
    for field in ("job_id", "raw_path", "canonical_url"):
        if output.get(field) != job.get(field):
            errors.append(f"luna output: {field} does not match job")
    errors.extend(
        _validate_quotes(root, job, output.get("grounding_quotes", []), "luna output")
    )

    tags = output.get("suggested_tags", [])
    if not isinstance(tags, list) or "metronome" not in tags:
        errors.append("luna output: suggested_tags must include metronome")
    concepts = output.get("suggested_metronome_concepts", [])
    if not isinstance(concepts, list) or any(
        not str(item).startswith("metronome-") for item in concepts
    ):
        errors.append("luna output: concepts must use metronome-prefixed slugs")

    expected_target = str(job.get("raw_path", ""))
    if expected_target.endswith(".md"):
        expected_target = expected_target[:-3]
    raw_link = str(output.get("proposed_raw_link", ""))
    match = RAW_LINK_RE.match(raw_link)
    if not match or match.group(1) != expected_target:
        errors.append(
            "luna output: proposed_raw_link must target the assigned raw file without .md"
        )
    if output.get("unsupported_claim_self_check") not in ([], None):
        errors.append("luna output: unsupported_claim_self_check must be empty for acceptance")
    return errors


def _evidence_errors(items: Any, quote_ids: set, prefix: str) -> List[str]:
    errors: List[str] = []
    if not isinstance(items, list):
        return [f"{prefix}: must be a list"]
    for index, item in enumerate(items, 1):
        if not isinstance(item, dict) or not item.get("text"):
            errors.append(f"{prefix}: item {index} text is required")
            continue
        evidence_ids = item.get("evidence_quote_ids")
        if not isinstance(evidence_ids, list) or not evidence_ids:
            errors.append(f"{prefix}: item {index} requires evidence_quote_ids")
            continue
        for quote_id in evidence_ids:
            if quote_id not in quote_ids:
                errors.append(
                    f"{prefix}: item {index} cites undefined grounding quote {quote_id}"
                )
    return errors


def validate_model_output(
    root: Path, job: Dict[str, Any], output: Dict[str, Any]
) -> List[str]:
    required = [
        "job_id",
        "raw_path",
        "canonical_url",
        "title",
        "grounding_quotes",
        "overview",
        "overview_evidence_quote_ids",
        "key_takeaways",
        "details",
        "sections_covered",
        "scope_boundaries",
        "conditional_requirements",
        "feature_gates",
        "internal_inconsistencies",
        "material_omissions",
        "suggested_tags",
        "suggested_metronome_concepts",
        "proposed_raw_link",
        "unsupported_claim_self_check",
    ]
    errors = [
        f"model output: {field} is required" for field in required if field not in output
    ]
    errors.extend(
        _missing(
            output,
            [
                "job_id",
                "raw_path",
                "canonical_url",
                "title",
                "grounding_quotes",
                "overview",
                "overview_evidence_quote_ids",
                "key_takeaways",
                "details",
                "sections_covered",
                "suggested_tags",
                "proposed_raw_link",
            ],
            "model output",
        )
    )
    for field in ("job_id", "raw_path", "canonical_url"):
        if output.get(field) != job.get(field):
            errors.append(f"model output: {field} does not match job")
    errors.extend(
        _validate_quotes(root, job, output.get("grounding_quotes", []), "model output")
    )

    quote_ids: set = set()
    for index, quote in enumerate(output.get("grounding_quotes", []), 1):
        quote_id = quote.get("id") if isinstance(quote, dict) else None
        if not quote_id:
            errors.append(f"model output: grounding quote {index} id is required")
        elif quote_id in quote_ids:
            errors.append(f"model output: grounding quote id is duplicated: {quote_id}")
        else:
            quote_ids.add(quote_id)

    overview_ids = output.get("overview_evidence_quote_ids")
    if not isinstance(overview_ids, list) or not overview_ids:
        errors.append("model output: overview_evidence_quote_ids is required")
    else:
        for quote_id in overview_ids:
            if quote_id not in quote_ids:
                errors.append(
                    f"model output: overview cites undefined grounding quote {quote_id}"
                )
    errors.extend(
        _evidence_errors(output.get("key_takeaways"), quote_ids, "model output: key_takeaways")
    )
    details = output.get("details")
    if not isinstance(details, list) or not details:
        errors.append("model output: details must be a nonempty list")
    else:
        for index, section in enumerate(details, 1):
            if not isinstance(section, dict) or not section.get("heading"):
                errors.append(f"model output: detail section {index} heading is required")
                continue
            errors.extend(
                _evidence_errors(
                    section.get("facts"), quote_ids, f"model output: detail section {index} facts"
                )
            )
    for field in (
        "scope_boundaries",
        "conditional_requirements",
        "feature_gates",
        "internal_inconsistencies",
    ):
        errors.extend(_evidence_errors(output.get(field), quote_ids, f"model output: {field}"))
    for field in ("sections_covered", "material_omissions"):
        if not isinstance(output.get(field), list):
            errors.append(f"model output: {field} must be a list")

    tags = output.get("suggested_tags", [])
    if not isinstance(tags, list) or "metronome" not in tags:
        errors.append("model output: suggested_tags must include metronome")
    concepts = output.get("suggested_metronome_concepts", [])
    if not isinstance(concepts, list) or any(
        not str(item).startswith("metronome-") for item in concepts
    ):
        errors.append("model output: concepts must use metronome-prefixed slugs")
    expected_target = str(job.get("raw_path", ""))
    if expected_target.endswith(".md"):
        expected_target = expected_target[:-3]
    match = RAW_LINK_RE.match(str(output.get("proposed_raw_link", "")))
    if not match or match.group(1) != expected_target:
        errors.append(
            "model output: proposed_raw_link must target the assigned raw file without .md"
        )
    if output.get("unsupported_claim_self_check") not in ([], None):
        errors.append("model output: unsupported_claim_self_check must be empty for acceptance")
    return errors


def render_luna_draft(
    job: Dict[str, Any], output: Dict[str, Any], ingest_date: str
) -> str:
    tags = ", ".join(str(item) for item in output["suggested_tags"])
    takeaways = "\n".join(f"- {item}" for item in output["key_takeaways"])
    detail_blocks = []
    for section in output["details"]:
        facts = "\n".join(f"- {fact}" for fact in section["facts"])
        detail_blocks.append(f"### {section['heading']}\n\n{facts}")
    details = "\n\n".join(detail_blocks)
    return (
        "---\n"
        f"title: \"{output['title']}\"\n"
        "type: source\n"
        f"date_ingested: {ingest_date}\n"
        f"canonical_url: \"{job['canonical_url']}\"\n"
        "original_format: webpage\n"
        "raw_files:\n"
        f"  - \"{job['raw_path'][4:]}\"\n"
        f"tags: [{tags}]\n"
        "---\n\n"
        f"## Overview\n\n{output['overview']}\n\n"
        f"## Key takeaways\n\n{takeaways}\n\n"
        f"## Details\n\n{details}\n\n"
        "## Change history\n\n"
        f"- {ingest_date}: Luna pilot draft from the assigned raw snapshot.\n\n"
        "## Related\n\n"
        "- Company: [[metronome]]\n"
        "- Concepts: coordinator concept audit required before promotion.\n\n"
        "## Raw Sources\n\n"
        f"- {output['proposed_raw_link']}\n"
    )


def render_model_draft(
    job: Dict[str, Any], output: Dict[str, Any], ingest_date: str
) -> str:
    tags = ", ".join(str(item) for item in output["suggested_tags"])
    takeaways = "\n".join(
        f"- {item['text']} [{', '.join(item['evidence_quote_ids'])}]"
        for item in output["key_takeaways"]
    )
    detail_blocks = []
    for section in output["details"]:
        facts = "\n".join(
            f"- {fact['text']} [{', '.join(fact['evidence_quote_ids'])}]"
            for fact in section["facts"]
        )
        detail_blocks.append(f"### {section['heading']}\n\n{facts}")
    details = "\n\n".join(detail_blocks)
    return (
        "---\n"
        f"title: \"{output['title']}\"\n"
        "type: source\n"
        f"date_ingested: {ingest_date}\n"
        f"canonical_url: \"{job['canonical_url']}\"\n"
        "original_format: webpage\n"
        "raw_files:\n"
        f"  - \"{job['raw_path'][4:]}\"\n"
        f"tags: [{tags}]\n"
        "---\n\n"
        f"## Overview\n\n{output['overview']} "
        f"[{', '.join(output['overview_evidence_quote_ids'])}]\n\n"
        f"## Key takeaways\n\n{takeaways}\n\n"
        f"## Details\n\n{details}\n\n"
        "## Change history\n\n"
        f"- {ingest_date}: {job['model']} comparison-pilot draft from the assigned raw snapshot.\n\n"
        "## Related\n\n"
        "- Company: [[metronome]]\n"
        "- Concepts: coordinator concept audit required before promotion.\n\n"
        "## Raw Sources\n\n"
        f"- {output['proposed_raw_link']}\n"
    )


def _validate_identity(job: Dict[str, Any], receipt: Dict[str, Any], prefix: str) -> List[str]:
    errors: List[str] = []
    for field in ("job_id", "provider", "canonical_url", "raw_path", "source_page"):
        if receipt.get(field) != job.get(field):
            errors.append(f"{prefix}: {field} does not match job")
    return errors


def _validate_artifact_paths(
    receipt: Dict[str, Any], fields: Sequence[str], artifact_dir: str, prefix: str
) -> List[str]:
    errors: List[str] = []
    for field in fields:
        value = receipt.get(field)
        if value and not _is_under(str(value), artifact_dir):
            errors.append(f"{prefix}: {field} must stay inside artifact_dir")
    return errors


def validate_worker_receipt(
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
            "model_provider",
            "model",
            "reasoning_effort",
            "attempt_count",
            "started_at",
            "finished_at",
            "elapsed_seconds",
            "process_exit_code",
            "output_path",
            "events_path",
            "stderr_path",
            "validation",
        ],
        "worker receipt",
    )
    errors.extend(_validate_identity(job, receipt, "worker receipt"))
    if receipt.get("status") not in ("success", "retryable_failure", "failed"):
        errors.append("worker receipt: invalid status")
    if receipt.get("model_provider") != "openai":
        errors.append("worker receipt: model_provider must be openai")
    if job.get("schema_version") == 3:
        if receipt.get("model") != job.get("model"):
            errors.append("worker receipt: model does not match job")
        if receipt.get("reasoning_effort") != job.get("reasoning_effort"):
            errors.append("worker receipt: reasoning_effort does not match job")
    else:
        if receipt.get("model") != LUNA_MODEL:
            errors.append(f"worker receipt: model must be {LUNA_MODEL}")
        if receipt.get("reasoning_effort") != LUNA_REASONING_EFFORT:
            errors.append(f"worker receipt: reasoning_effort must be {LUNA_REASONING_EFFORT}")
    if receipt.get("attempt_count") not in (1, 2):
        errors.append("worker receipt: attempt_count must be 1 or 2")
    artifact_dir = str(job.get("artifact_dir", ""))
    errors.extend(
        _validate_artifact_paths(
            receipt,
            ("output_path", "draft_path", "events_path", "stderr_path"),
            artifact_dir,
            "worker receipt",
        )
    )
    if receipt.get("status") == "success" or receipt.get("grounding_quotes"):
        errors.extend(
            _validate_quotes(
                root, job, receipt.get("grounding_quotes", []), "worker receipt"
            )
        )
    if receipt.get("token_usage") is None and not receipt.get(
        "token_usage_unavailable_reason"
    ):
        errors.append(
            "worker receipt: null token_usage requires token_usage_unavailable_reason"
        )
    if receipt.get("status") == "success":
        if receipt.get("process_exit_code") != 0:
            errors.append("worker receipt: successful status requires process_exit_code 0")
        if not receipt.get("draft_path"):
            errors.append("worker receipt: successful status requires draft_path")
        errors.extend(
            _validate_validation_results(receipt.get("validation", []), "worker receipt")
        )
    if job.get("schema_version") == 3:
        attempts = receipt.get("attempts")
        if not isinstance(attempts, list) or len(attempts) != receipt.get("attempt_count"):
            errors.append("worker receipt: attempts must match attempt_count")
        else:
            for index, attempt in enumerate(attempts, 1):
                if not isinstance(attempt, dict) or attempt.get("attempt") != index:
                    errors.append(f"worker receipt: attempt {index} identity is invalid")
                    continue
                for field in (
                    "status",
                    "process_exit_code",
                    "validation_errors",
                    "output_path",
                    "events_path",
                    "stderr_path",
                ):
                    if field not in attempt:
                        errors.append(f"worker receipt: attempt {index} {field} is required")
                errors.extend(
                    _validate_artifact_paths(
                        attempt,
                        ("output_path", "events_path", "stderr_path"),
                        artifact_dir,
                        f"worker receipt: attempt {index}",
                    )
                )
        if receipt.get("cumulative_token_usage") is None and not receipt.get(
            "token_usage_unavailable_reason"
        ):
            errors.append(
                "worker receipt: null cumulative_token_usage requires token_usage_unavailable_reason"
            )
    return errors


def validate_final_receipt(
    root: Path, job: Dict[str, Any], receipt: Dict[str, Any]
) -> List[str]:
    draft_field = "model_draft" if job.get("schema_version") == 3 else "luna_draft"
    errors = _missing(
        receipt,
        [
            "schema_version",
            "job_id",
            "provider",
            "canonical_url",
            "raw_path",
            "source_page",
            "mode",
            "worker_receipt",
            draft_field,
            "final_status",
            "coordinator_repair_minutes",
            "validation",
            "review",
        ],
        "final receipt",
    )
    errors.extend(_validate_identity(job, receipt, "final receipt"))
    if receipt.get("mode") != job.get("mode"):
        errors.append("final receipt: mode does not match job")
    if receipt.get("final_status") not in (
        "approved",
        "approved_with_repairs",
        "rejected",
    ):
        errors.append("final receipt: invalid final_status")
    repair_minutes = receipt.get("coordinator_repair_minutes")
    if not isinstance(repair_minutes, (int, float)) or repair_minutes < 0:
        errors.append("final receipt: coordinator_repair_minutes must be nonnegative")
    for field in ("repairs", "concepts_updated", "contradictions", "shared_files_updated"):
        if not isinstance(receipt.get(field), list):
            errors.append(f"final receipt: {field} must be a list")
    artifact_dir = str(job.get("artifact_dir", ""))
    errors.extend(
        _validate_artifact_paths(
            receipt,
            ("worker_receipt", draft_field),
            artifact_dir,
            "final receipt",
        )
    )
    review = receipt.get("review", {})
    if not isinstance(review, dict):
        review = {}
    if review.get("model") != SOL_MODEL:
        errors.append(f"final receipt: review model must be {SOL_MODEL}")
    if receipt.get("final_status") in ("approved", "approved_with_repairs"):
        if review.get("status") != "approved":
            errors.append("final receipt: approved final status requires approved review")
        errors.extend(
            _validate_validation_results(receipt.get("validation", []), "final receipt")
        )
    return errors
