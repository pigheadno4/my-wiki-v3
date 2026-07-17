#!/usr/bin/env python3
"""Deterministic job and receipt validation for Metronome ingest pilots."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple


COMMIT_RE = re.compile(r"^[0-9a-f]{7,40}$")
JOB_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
RAW_LINK_RE = re.compile(r"^\[\[([^|\]]+)\|[^\]]+\]\]$")
TAG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
LUNA_MODEL = "gpt-5.6-luna"
SOL_MODEL = "gpt-5.6-sol"
TERRA_MODEL = "gpt-5.6-terra"
LUNA_REASONING_EFFORT = "high"
TERRA_REASONING_EFFORT = "medium"
LUNA_RUN_ROOT = "tracking/ingest/metronome/pilot/runs/"
DIAGNOSTIC_INPUT_MODES = frozenset(("staged-file", "inline-stdin"))
DIAGNOSTIC_ACCOUNTING_FIELDS = (
    "attempt_started_at",
    "attempt_finished_at",
    "attempt_elapsed_seconds",
    "time_to_first_stdout_event_seconds",
    "time_to_first_stderr_byte_seconds",
    "streamed_stdout_bytes",
    "streamed_stderr_bytes",
    "parsed_event_count",
    "truncated_line_count",
)
MODEL_PROFILES = {
    LUNA_MODEL: LUNA_REASONING_EFFORT,
    TERRA_MODEL: TERRA_REASONING_EFFORT,
}


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _missing(data: Dict[str, Any], fields: List[str], prefix: str) -> List[str]:
    return [f"{prefix}: {field} is required" for field in fields if data.get(field) in (None, "", [])]


def _is_relative_to(path: Path, directory: Path) -> bool:
    try:
        path.relative_to(directory)
    except ValueError:
        return False
    return True


def _path_has_traversal(value: str) -> bool:
    return any(part in (".", "..") for part in value.replace("\\", "/").split("/"))


def _resolve_contained_path(
    root: Path,
    value: Any,
    directory: Path,
    *,
    prefix: str,
    field: str,
    directory_label: str,
) -> Tuple[Optional[Path], List[str]]:
    """Resolve one repository-relative path and prove it remains in its container."""
    errors: List[str] = []
    if value in (None, ""):
        return None, errors
    if not isinstance(value, str):
        return None, [f"{prefix}: {field} must be a safe repository-relative path"]
    candidate = Path(value)
    if candidate.is_absolute() or value.startswith("/") or "\\" in value:
        return None, [f"{prefix}: {field} must be a safe repository-relative path"]
    if _path_has_traversal(value):
        return None, [f"{prefix}: {field} must not contain traversal"]
    resolved_directory = directory.resolve()
    resolved_parent = directory.parent.resolve()
    resolved = (root / candidate).resolve()
    if (
        not _is_relative_to(resolved_directory, root.resolve())
        or not _is_relative_to(resolved_directory, resolved_parent)
        or not _is_relative_to(resolved, resolved_directory)
    ):
        errors.append(f"{prefix}: {field} resolves outside {directory_label}")
    return resolved, errors


def _validate_job_id(job: Dict[str, Any]) -> List[str]:
    job_id = job.get("job_id")
    if not isinstance(job_id, str) or not JOB_ID_RE.fullmatch(job_id):
        return ["job: job_id must use lowercase kebab-case letters and digits"]
    return []


def _validate_raw_path(root: Path, job: Dict[str, Any]) -> List[str]:
    raw_path = job.get("raw_path")
    resolved, errors = _resolve_contained_path(
        root,
        raw_path,
        root / "raw" / "metronome",
        prefix="job",
        field="raw_path",
        directory_label="raw/metronome",
    )
    if raw_path and resolved is not None and not errors and not resolved.is_file():
        errors.append(f"job: raw_path does not exist: {raw_path}")
    return errors


def _validate_model_artifact_dir(root: Path, job: Dict[str, Any], label: str) -> List[str]:
    artifact_dir = job.get("artifact_dir")
    expected_dir = f"{LUNA_RUN_ROOT}{job.get('job_id', '')}"
    errors: List[str] = []
    if artifact_dir and artifact_dir != expected_dir:
        errors.append(f"job: artifact_dir must match the job ID under the {label} run root")
    _, containment_errors = _resolve_contained_path(
        root,
        artifact_dir,
        root / LUNA_RUN_ROOT,
        prefix="job",
        field="artifact_dir",
        directory_label=f"the {label} run root",
    )
    errors.extend(containment_errors)
    return errors


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
    errors = _validate_job_id(job)
    errors.extend(_validate_raw_path(root, job))
    if job.get("schema_version") == 3:
        return errors + _validate_model_job(root, job)
    if job.get("schema_version") == 2:
        return errors + _validate_luna_job(root, job)
    errors.extend(_missing(
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
    ))
    if job.get("provider") != "metronome":
        errors.append("job: provider must be metronome")

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

    source_page = str(job.get("source_page", ""))
    if source_page and not source_page.startswith("wiki/sources/metronome/"):
        errors.append("job: source_page must stay inside wiki/sources/metronome/")

    artifact_dir = str(job.get("artifact_dir", ""))
    errors.extend(_validate_model_artifact_dir(root, job, "model"))
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

    source_page = str(job.get("source_page", ""))
    if source_page and not source_page.startswith("wiki/sources/metronome/"):
        errors.append("job: source_page must stay inside wiki/sources/metronome/")

    artifact_dir = str(job.get("artifact_dir", ""))
    errors.extend(_validate_model_artifact_dir(root, job, "Luna"))

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
    if isinstance(tags, list):
        if any(not isinstance(tag, str) or not TAG_RE.fullmatch(tag) for tag in tags):
            errors.append("model output: suggested_tags must use lowercase kebab-case")
        if any(not tag for tag in tags) or len(tags) != len(set(tags)):
            errors.append("model output: suggested_tags must be unique nonempty values")
    concepts = output.get("suggested_metronome_concepts", [])
    if not isinstance(concepts, list) or any(
        not str(item).startswith("metronome-") for item in concepts
    ):
        errors.append("model output: concepts must use metronome-prefixed slugs")
    if isinstance(concepts, list):
        concept_dir = root / "wiki/concepts/metronome"
        existing_concepts = {
            path.stem for path in concept_dir.glob("*.md") if path.is_file()
        }
        for concept in sorted(set(str(item) for item in concepts) - existing_concepts):
            errors.append(
                "model output: unknown existing Metronome concept for Sol review: "
                f"{concept}"
            )
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
    root: Path,
    receipt: Dict[str, Any],
    fields: Sequence[str],
    artifact_dir: str,
    prefix: str,
    *,
    require_existing_files: bool = False,
    directory_label: str = "artifact_dir",
) -> List[str]:
    errors: List[str] = []
    directory = root / artifact_dir
    for field in fields:
        value = receipt.get(field)
        if not value:
            continue
        resolved, path_errors = _resolve_contained_path(
            root,
            value,
            directory,
            prefix=prefix,
            field=field,
            directory_label=directory_label,
        )
        errors.extend(path_errors)
        if resolved is None or path_errors or not require_existing_files:
            continue
        lexical = root / str(value)
        if lexical.is_symlink():
            errors.append(f"{prefix}: {field} must not reference a symlink")
        elif not resolved.is_file():
            errors.append(f"{prefix}: {field} must reference an existing regular file")
    return errors


def _is_nonnegative_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and value >= 0


def _validate_runtime_metadata(
    root: Path, job: Dict[str, Any], metadata: Any, prefix: str
) -> List[str]:
    if not isinstance(metadata, dict):
        return [f"{prefix}: runtime_metadata must be an object"]
    errors: List[str] = []
    hashes = metadata.get("sha256")
    required_hashes = (
        "raw_text",
        "prompt_template",
        "rendered_prompt",
        "output_schema",
        "codex_executable",
    )
    if not isinstance(hashes, dict):
        return [f"{prefix}: runtime_metadata.sha256 is required"]
    unavailable = metadata.get("metadata_unavailable_reason")
    for name in required_hashes:
        value = hashes.get(name)
        if name == "codex_executable" and value is None and unavailable:
            continue
        if not isinstance(value, str) or not SHA256_RE.fullmatch(value):
            errors.append(f"{prefix}: runtime_metadata.sha256.{name} must be a SHA-256 hex digest")
    raw_hash = hashes.get("raw_text")
    if isinstance(raw_hash, str) and SHA256_RE.fullmatch(raw_hash):
        raw_path, raw_path_errors = _resolve_contained_path(
            root,
            job.get("raw_path"),
            root / "raw" / "metronome",
            prefix=prefix,
            field="raw_path",
            directory_label="raw/metronome",
        )
        if raw_path is not None and not raw_path_errors and raw_path.is_file():
            expected_raw_hash = hashlib.sha256(raw_path.read_bytes()).hexdigest()
            if raw_hash != expected_raw_hash:
                errors.append(f"{prefix}: runtime_metadata raw_text hash does not match raw_path")
    executable = metadata.get("codex_executable")
    cli_version = metadata.get("codex_cli_version")
    if unavailable:
        if not isinstance(unavailable, str):
            errors.append(f"{prefix}: runtime_metadata unavailable reason must be text")
        if executable is not None or cli_version is not None:
            errors.append(
                f"{prefix}: runtime_metadata unavailable provenance must use null executable and CLI version"
            )
    elif not isinstance(executable, str) or not executable or not isinstance(cli_version, str) or not cli_version:
        errors.append(f"{prefix}: runtime_metadata requires Codex executable and CLI version provenance")
    timeout = metadata.get("timeout_seconds")
    if not isinstance(timeout, int) or isinstance(timeout, bool) or timeout <= 0:
        errors.append(f"{prefix}: runtime_metadata timeout_seconds must be a positive integer")
    return errors


def _validate_diagnostic_accounting(record: Dict[str, Any], prefix: str) -> List[str]:
    errors: List[str] = []
    for field in DIAGNOSTIC_ACCOUNTING_FIELDS:
        if field not in record:
            errors.append(f"{prefix}: {field} is required")
    elapsed = record.get("attempt_elapsed_seconds")
    if "attempt_elapsed_seconds" in record and not _is_nonnegative_number(elapsed):
        errors.append(f"{prefix}: attempt_elapsed_seconds must be nonnegative")
    for field in ("attempt_started_at", "attempt_finished_at"):
        if field in record and (not isinstance(record.get(field), str) or not record.get(field)):
            errors.append(f"{prefix}: {field} must be a timestamp")
    for field in (
        "time_to_first_stdout_event_seconds",
        "time_to_first_stderr_byte_seconds",
    ):
        value = record.get(field)
        if field in record and value is not None and not _is_nonnegative_number(value):
            errors.append(f"{prefix}: {field} must be null or nonnegative")
        if _is_nonnegative_number(value) and _is_nonnegative_number(elapsed) and value > elapsed:
            errors.append(f"{prefix}: {field} cannot exceed attempt_elapsed_seconds")
    for field in (
        "streamed_stdout_bytes",
        "streamed_stderr_bytes",
        "parsed_event_count",
        "truncated_line_count",
    ):
        value = record.get(field)
        if field in record and (
            not isinstance(value, int) or isinstance(value, bool) or value < 0
        ):
            errors.append(f"{prefix}: {field} must be a nonnegative integer")
    return errors


def _validate_streaming_files(
    root: Path, record: Dict[str, Any], artifact_dir: str, prefix: str
) -> List[str]:
    errors: List[str] = []
    events_value = record.get("events_path")
    stderr_value = record.get("stderr_path")
    events_path, event_path_errors = _resolve_contained_path(
        root,
        events_value,
        root / artifact_dir,
        prefix=prefix,
        field="events_path",
        directory_label="diagnostic run directory",
    )
    stderr_path, stderr_path_errors = _resolve_contained_path(
        root,
        stderr_value,
        root / artifact_dir,
        prefix=prefix,
        field="stderr_path",
        directory_label="diagnostic run directory",
    )
    if events_path is not None and not event_path_errors and events_path.is_file():
        events = events_path.read_bytes()
        if record.get("streamed_stdout_bytes") != len(events):
            errors.append(f"{prefix}: streamed_stdout_bytes does not match events_path")
        lines = events.split(b"\n")
        tail = lines.pop()
        parsed_count = 0
        for line in lines:
            if not line.strip():
                continue
            try:
                json.loads(line.decode("utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError):
                continue
            parsed_count += 1
        if record.get("parsed_event_count") != parsed_count:
            errors.append(f"{prefix}: parsed_event_count does not match events_path")
        if record.get("truncated_line_count") != (1 if tail else 0):
            errors.append(f"{prefix}: truncated_line_count does not match events_path")
    if stderr_path is not None and not stderr_path_errors and stderr_path.is_file():
        if record.get("streamed_stderr_bytes") != stderr_path.stat().st_size:
            errors.append(f"{prefix}: streamed_stderr_bytes does not match stderr_path")
    return errors


def _validate_progress_file(root: Path, progress_path: str, artifact_dir: str, prefix: str) -> List[str]:
    path, path_errors = _resolve_contained_path(
        root,
        progress_path,
        root / artifact_dir,
        prefix=prefix,
        field="progress_path",
        directory_label="diagnostic run directory",
    )
    if path is None or path_errors or not path.is_file():
        return []
    events = set()
    errors: List[str] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        try:
            item = json.loads(line)
        except json.JSONDecodeError:
            errors.append(f"{prefix}: progress_path has invalid JSONL at line {line_number}")
            continue
        if not isinstance(item, dict) or not item.get("timestamp") or not item.get("event"):
            errors.append(f"{prefix}: progress_path event at line {line_number} is incomplete")
            continue
        events.add(item["event"])
    for required in ("lock_acquired", "process_started", "validation_completed", "receipt_published"):
        if required not in events:
            errors.append(f"{prefix}: progress_path is missing {required} evidence")
    return errors


def _validate_diagnostic_artifact_tree(run_dir: Path, prefix: str) -> List[str]:
    if not run_dir.is_dir():
        return [f"{prefix}: diagnostic run directory must exist"]
    errors: List[str] = []
    if run_dir.is_symlink():
        errors.append(f"{prefix}: diagnostic run directory must not be a symlink")
    for path in run_dir.rglob("*"):
        if path.is_symlink():
            errors.append(f"{prefix}: diagnostic artifact must not be a symlink: {path.name}")
        if path.name.endswith(".tmp"):
            errors.append(f"{prefix}: temporary artifact remains: {path.name}")
    return errors


def _validate_termination(termination: Any, process_exit_code: Any, prefix: str) -> List[str]:
    if termination is None:
        return (
            [f"{prefix}: timeout requires termination and cleanup evidence"]
            if process_exit_code == 124
            else []
        )
    if not isinstance(termination, dict):
        return [f"{prefix}: termination must be null or an object"]
    errors: List[str] = []
    for field in ("signal", "grace_seconds", "grace_outcome", "escalation_signal", "final_return_code"):
        if field not in termination:
            errors.append(f"{prefix}: termination.{field} is required")
    if termination.get("signal") not in (None, "SIGTERM"):
        errors.append(f"{prefix}: termination.signal must be SIGTERM or null")
    if termination.get("grace_seconds") is not None and not _is_nonnegative_number(
        termination.get("grace_seconds")
    ):
        errors.append(f"{prefix}: termination.grace_seconds must be null or nonnegative")
    if termination.get("grace_outcome") not in (
        "already_exited",
        "terminated",
        "killed",
        "runner_timeout",
    ):
        errors.append(f"{prefix}: termination.grace_outcome is invalid")
    final_code = termination.get("final_return_code")
    if final_code is not None and (
        not isinstance(final_code, int) or isinstance(final_code, bool)
    ):
        errors.append(f"{prefix}: termination.final_return_code must be an integer or null")
    if termination.get("signal") == "SIGTERM" and termination.get("grace_outcome") != "runner_timeout":
        if termination.get("pipe_cleanup_outcome") not in ("eof", "forced_close"):
            errors.append(f"{prefix}: termination requires pipe cleanup outcome")
    return errors


def _validate_diagnostic_worker_receipt(
    root: Path, job: Dict[str, Any], receipt: Dict[str, Any]
) -> List[str]:
    """Validate immutable on-disk evidence for a run-id diagnostic receipt."""
    errors: List[str] = []
    if receipt.get("schema_version") != 3 or job.get("schema_version") != 3:
        errors.append("worker receipt: diagnostic receipts require schema_version 3")
    run_id = receipt.get("run_id")
    if not isinstance(run_id, str) or not JOB_ID_RE.fullmatch(run_id):
        errors.append("worker receipt: diagnostic run_id must use lowercase kebab-case letters and digits")
        return errors
    errors.extend(_validate_model_artifact_dir(root, job, "model"))
    artifact_dir = str(job.get("artifact_dir", ""))
    diagnostic_dir = f"{artifact_dir}/{run_id}"
    run_dir, run_errors = _resolve_contained_path(
        root,
        diagnostic_dir,
        root / artifact_dir,
        prefix="worker receipt",
        field="diagnostic run directory",
        directory_label="artifact_dir",
    )
    errors.extend(run_errors)
    if run_dir is None:
        return errors
    errors.extend(_validate_diagnostic_artifact_tree(run_dir, "worker receipt"))

    for field in (
        "input_mode",
        "progress_path",
        "runtime_metadata",
        "termination",
        "normalized_output_path",
    ):
        if field not in receipt:
            errors.append(f"worker receipt: diagnostic {field} is required")
    if receipt.get("input_mode") not in DIAGNOSTIC_INPUT_MODES:
        errors.append("worker receipt: diagnostic input_mode must be staged-file or inline-stdin")
    errors.extend(_validate_diagnostic_accounting(receipt, "worker receipt"))
    errors.extend(_validate_termination(
        receipt.get("termination"), receipt.get("process_exit_code"), "worker receipt"
    ))
    errors.extend(_validate_runtime_metadata(
        root, job, receipt.get("runtime_metadata"), "worker receipt"
    ))
    errors.extend(
        _validate_artifact_paths(
            root,
            receipt,
            (
                "output_path",
                "normalized_output_path",
                "draft_path",
                "events_path",
                "stderr_path",
                "progress_path",
            ),
            diagnostic_dir,
            "worker receipt",
            require_existing_files=True,
            directory_label="diagnostic run directory",
        )
    )
    errors.extend(_validate_streaming_files(
        root, receipt, diagnostic_dir, "worker receipt"
    ))
    if isinstance(receipt.get("progress_path"), str):
        errors.extend(_validate_progress_file(
            root, receipt["progress_path"], diagnostic_dir, "worker receipt"
        ))

    attempts = receipt.get("attempts")
    if not isinstance(attempts, list) or not attempts:
        return errors
    expected_run_prefix = f"{diagnostic_dir}/"
    for index, attempt in enumerate(attempts, 1):
        if not isinstance(attempt, dict):
            continue
        attempt_prefix = f"worker receipt: attempt {index}"
        for field in (
            "input_mode",
            "progress_path",
            "runtime_metadata",
            "termination",
            "normalized_output_path",
        ):
            if field not in attempt:
                errors.append(f"{attempt_prefix}: diagnostic {field} is required")
        if attempt.get("input_mode") != receipt.get("input_mode"):
            errors.append(f"{attempt_prefix}: input_mode does not match receipt")
        expected_attempt_prefix = f"{expected_run_prefix}attempt-{index}"
        expected_paths = {
            "events_path": f"{expected_attempt_prefix}/events.jsonl",
            "stderr_path": f"{expected_attempt_prefix}/stderr.log",
            "progress_path": f"{expected_attempt_prefix}/progress.jsonl",
        }
        for field, expected in expected_paths.items():
            if attempt.get(field) != expected:
                errors.append(f"{attempt_prefix}: {field} does not match diagnostic attempt path")
        output_path = attempt.get("output_path")
        normalized_path = attempt.get("normalized_output_path")
        if output_path is not None:
            expected_raw = f"{expected_attempt_prefix}/model-output.raw.json"
            if output_path != expected_raw:
                errors.append(f"{attempt_prefix}: diagnostic output_path must reference model-output.raw.json")
        if normalized_path is not None:
            expected_normalized = f"{expected_attempt_prefix}/model-output.normalized.json"
            if normalized_path != expected_normalized:
                errors.append(
                    f"{attempt_prefix}: normalized_output_path must reference model-output.normalized.json"
                )
        if normalized_path is not None and output_path is None:
            errors.append(f"{attempt_prefix}: normalized_output_path requires raw output_path")
        if normalized_path is not None and normalized_path == output_path:
            errors.append(f"{attempt_prefix}: raw and normalized output paths must differ")
        if output_path is not None and normalized_path is not None:
            raw_artifact, raw_artifact_errors = _resolve_contained_path(
                root,
                output_path,
                root / diagnostic_dir,
                prefix=attempt_prefix,
                field="output_path",
                directory_label="diagnostic run directory",
            )
            normalized_artifact, normalized_artifact_errors = _resolve_contained_path(
                root,
                normalized_path,
                root / diagnostic_dir,
                prefix=attempt_prefix,
                field="normalized_output_path",
                directory_label="diagnostic run directory",
            )
            if (
                raw_artifact is not None
                and normalized_artifact is not None
                and not raw_artifact_errors
                and not normalized_artifact_errors
                and raw_artifact.is_file()
                and normalized_artifact.is_file()
                and raw_artifact.samefile(normalized_artifact)
            ):
                errors.append(f"{attempt_prefix}: raw and normalized output artifacts must be distinct")
        errors.extend(
            _validate_artifact_paths(
                root,
                attempt,
                (
                    "output_path",
                    "normalized_output_path",
                    "events_path",
                    "stderr_path",
                    "progress_path",
                ),
                diagnostic_dir,
                attempt_prefix,
                require_existing_files=True,
                directory_label="diagnostic run directory",
            )
        )
        errors.extend(_validate_diagnostic_accounting(attempt, attempt_prefix))
        errors.extend(_validate_termination(
            attempt.get("termination"), attempt.get("process_exit_code"), attempt_prefix
        ))
        errors.extend(_validate_runtime_metadata(
            root, job, attempt.get("runtime_metadata"), attempt_prefix
        ))
        errors.extend(_validate_streaming_files(root, attempt, diagnostic_dir, attempt_prefix))

    last_attempt = attempts[-1] if isinstance(attempts[-1], dict) else {}
    for field in (
        "input_mode",
        "events_path",
        "stderr_path",
        "progress_path",
        "runtime_metadata",
        "termination",
        *DIAGNOSTIC_ACCOUNTING_FIELDS,
    ):
        if receipt.get(field) != last_attempt.get(field):
            errors.append(f"worker receipt: {field} does not reconcile with final attempt")
    if receipt.get("status") == "success":
        accepted_path = f"{diagnostic_dir}/model-output.normalized.json"
        if receipt.get("output_path") != accepted_path:
            errors.append("worker receipt: successful diagnostic output_path must be normalized output")
        if receipt.get("normalized_output_path") != accepted_path:
            errors.append("worker receipt: successful diagnostic normalized_output_path is invalid")
        if receipt.get("draft_path") != f"{diagnostic_dir}/model-source-draft.md":
            errors.append("worker receipt: successful diagnostic draft_path is invalid")
    else:
        for field in ("output_path", "normalized_output_path"):
            if receipt.get(field) != last_attempt.get(field):
                errors.append(f"worker receipt: failed diagnostic {field} does not reconcile with final attempt")
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
            "events_path",
            "stderr_path",
            "validation",
        ],
        "worker receipt",
    )
    diagnostic = "run_id" in receipt
    diagnostic_failure = diagnostic and receipt.get("status") != "success"
    if not diagnostic and any(
        field in receipt
        for field in ("progress_path", "runtime_metadata", "termination", "normalized_output_path")
    ):
        errors.append("worker receipt: diagnostic runtime fields require run_id")
    if "output_path" not in receipt or (
        receipt.get("output_path") in (None, "") and not diagnostic_failure
    ):
        errors.append("worker receipt: output_path is required")
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
            root,
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
                    "events_path",
                    "stderr_path",
                ):
                    if field not in attempt:
                        errors.append(f"worker receipt: attempt {index} {field} is required")
                if "output_path" not in attempt or (
                    attempt.get("output_path") in (None, "")
                    and receipt.get("run_id") is None
                ):
                    errors.append(f"worker receipt: attempt {index} output_path is required")
                if receipt.get("run_id") is not None and "normalized_output_path" not in attempt:
                    errors.append(
                        f"worker receipt: attempt {index} normalized_output_path is required"
                    )
                errors.extend(
                    _validate_artifact_paths(
                        root,
                        attempt,
                        ("output_path", "events_path", "stderr_path"),
                        artifact_dir,
                        f"worker receipt: attempt {index}",
                    )
                )
                if receipt.get("run_id") is not None:
                    normalized_path = attempt.get("normalized_output_path")
                    if attempt.get("output_path") is not None and not str(
                        attempt.get("output_path")
                    ).endswith("model-output.raw.json"):
                        errors.append(
                            f"worker receipt: attempt {index} diagnostic output_path must reference model-output.raw.json"
                        )
                    if normalized_path is not None and normalized_path == attempt.get("output_path"):
                        errors.append(
                            f"worker receipt: attempt {index} raw and normalized output paths must differ"
                        )
                    elif normalized_path is not None:
                        if attempt.get("output_path") is None:
                            errors.append(
                                f"worker receipt: attempt {index} normalized_output_path requires raw output_path"
                            )
                        if not str(normalized_path).endswith("model-output.normalized.json"):
                            errors.append(
                                f"worker receipt: attempt {index} normalized_output_path must reference model-output.normalized.json"
                            )
                        errors.extend(
                            _validate_artifact_paths(
                                root,
                                attempt,
                                ("normalized_output_path",),
                                artifact_dir,
                                f"worker receipt: attempt {index}",
                            )
                        )
        if receipt.get("run_id") is not None:
            if "normalized_output_path" not in receipt:
                errors.append("worker receipt: diagnostic normalized_output_path is required")
            normalized_path = receipt.get("normalized_output_path")
            if normalized_path is not None:
                errors.extend(
                    _validate_artifact_paths(
                        root,
                        receipt,
                        ("normalized_output_path",),
                        artifact_dir,
                        "worker receipt",
                    )
                )
                if not str(normalized_path).endswith("model-output.normalized.json"):
                    errors.append(
                        "worker receipt: diagnostic normalized_output_path must reference model-output.normalized.json"
                    )
            if receipt.get("status") != "success" and receipt.get(
                "output_path"
            ) is not None and not str(receipt.get("output_path")).endswith(
                "model-output.raw.json"
            ):
                errors.append(
                    "worker receipt: failed diagnostic output_path must reference model-output.raw.json"
                )
        if receipt.get("cumulative_token_usage") is None and not receipt.get(
            "token_usage_unavailable_reason"
        ):
            errors.append(
                "worker receipt: null cumulative_token_usage requires token_usage_unavailable_reason"
            )
    if diagnostic:
        errors.extend(_validate_diagnostic_worker_receipt(root, job, receipt))
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
            root,
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
