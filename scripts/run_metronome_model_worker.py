#!/usr/bin/env python3
"""Run one schema-v3 Metronome evidence-draft job with deterministic repair."""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

from metronome_ingest_pilot import (
    load_json,
    render_model_draft,
    validate_job,
    validate_model_output,
)


ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = Path("tracking/ingest/metronome/pilot/schemas/model-output-v3.schema.json")
PROMPT_PATH = Path("tracking/ingest/metronome/pilot/prompts/source-summary-v3.md")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$")
METHOD_RE = re.compile(r"\b(GET|POST|PUT|PATCH|DELETE)\s+(/\S+)", re.IGNORECASE)
RAW_LINK_RE = re.compile(r"^\[\[([^|\]]+)\|([^\]]+)\]\]$")
RESPONSE_RE = re.compile(r"\b([1-5][0-9]{2})\b")
CONDITIONAL_RE = re.compile(r"\b(if|when|unless|only if|mutually exclusive|one of)\b", re.IGNORECASE)
GATE_RE = re.compile(r"\b(beta|preview|allowlist|feature flag|enabled for|contact metronome)\b", re.IGNORECASE)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def build_page_profile(raw_text: str) -> Dict[str, Any]:
    headings: List[str] = []
    endpoints: List[Dict[str, Any]] = []
    response_codes: List[Dict[str, Any]] = []
    conditional_lines: List[int] = []
    gate_lines: List[int] = []
    for line_number, line in enumerate(raw_text.splitlines(), 1):
        heading = HEADING_RE.match(line)
        if heading:
            headings.append(heading.group(1))
        for method, path in METHOD_RE.findall(line):
            endpoints.append({"line": line_number, "method": method.upper(), "path": path})
        for code in RESPONSE_RE.findall(line):
            response_codes.append({"line": line_number, "code": code})
        if CONDITIONAL_RE.search(line):
            conditional_lines.append(line_number)
        if GATE_RE.search(line):
            gate_lines.append(line_number)
    return {
        "line_count": len(raw_text.splitlines()),
        "headings": headings,
        "endpoints": endpoints,
        "response_codes": response_codes,
        "conditional_hint_lines": conditional_lines,
        "feature_gate_hint_lines": gate_lines,
    }


def build_prompt(
    template: str,
    job: Dict[str, Any],
    profile: Dict[str, Any],
    validation_errors: Optional[List[str]] = None,
) -> str:
    assignment = (
        "\n\n## Assigned job\n\n"
        f"- job_id: `{job['job_id']}`\n"
        f"- original raw_path identity: `{job['raw_path']}`\n"
        f"- canonical_url: `{job['canonical_url']}`\n"
        "- staged input file: `raw.md`\n\n"
        "## Deterministic page profile\n\n"
        f"```json\n{json.dumps(profile, indent=2, ensure_ascii=False)}\n```"
    )
    if validation_errors:
        errors = "\n".join(f"- {error}" for error in validation_errors)
        assignment += f"\n\n## Prior deterministic validation errors\n\n{errors}"
    return template.rstrip() + assignment + "\n"


def build_codex_command(
    cwd: Path,
    schema_path: Path,
    output_path: Path,
    prompt: str,
    model: str,
    reasoning_effort: str,
) -> List[str]:
    return [
        "codex",
        "-a",
        "never",
        "exec",
        "-m",
        model,
        "-c",
        f'model_reasoning_effort="{reasoning_effort}"',
        "-s",
        "read-only",
        "--ephemeral",
        "--skip-git-repo-check",
        "--disable",
        "plugins",
        "--disable",
        "remote_plugin",
        "--disable",
        "apps",
        "--disable",
        "hooks",
        "--disable",
        "memories",
        "--output-schema",
        str(schema_path),
        "--json",
        "-o",
        str(output_path),
        "-C",
        str(cwd),
        prompt,
    ]


def extract_token_usage(events: str) -> Optional[Dict[str, Any]]:
    usage: Optional[Dict[str, Any]] = None
    for line in events.splitlines():
        try:
            item = json.loads(line)
        except json.JSONDecodeError:
            continue
        candidate = item.get("usage") if isinstance(item, dict) else None
        if isinstance(candidate, dict):
            usage = candidate
    return usage


def sum_token_usage(usages: List[Optional[Dict[str, Any]]]) -> Optional[Dict[str, Any]]:
    available = [usage for usage in usages if isinstance(usage, dict)]
    if not available:
        return None
    totals: Dict[str, Any] = {}
    for usage in available:
        for key, value in usage.items():
            if isinstance(value, (int, float)) and not isinstance(value, bool):
                totals[key] = totals.get(key, 0) + value
    return totals


def repair_quote_bounds(raw_text: str, output: Dict[str, Any]) -> int:
    raw_lines = raw_text.splitlines()
    repaired = 0
    for quote in output.get("grounding_quotes", []):
        if not isinstance(quote, dict) or not isinstance(quote.get("text"), str):
            continue
        quote_lines = quote["text"].splitlines()
        if not quote_lines:
            continue
        matches = []
        width = len(quote_lines)
        for offset in range(0, len(raw_lines) - width + 1):
            if raw_lines[offset : offset + width] == quote_lines:
                matches.append(offset + 1)
        if len(matches) != 1:
            continue
        start = matches[0]
        end = start + width - 1
        if quote.get("line_start") != start or quote.get("line_end") != end:
            quote["line_start"] = start
            quote["line_end"] = end
            repaired += 1
    return repaired


def repair_raw_link(job: Dict[str, Any], output: Dict[str, Any]) -> bool:
    raw_link = output.get("proposed_raw_link")
    match = RAW_LINK_RE.match(raw_link) if isinstance(raw_link, str) else None
    if not match:
        return False
    expected_target = str(job["raw_path"])
    if expected_target.endswith(".md"):
        expected_target = expected_target[:-3]
    if match.group(1) == expected_target:
        return False
    output["proposed_raw_link"] = f"[[{expected_target}|{match.group(2)}]]"
    return True


def repair_mandatory_tags(output: Dict[str, Any]) -> int:
    tags = output.get("suggested_tags")
    if not isinstance(tags, list):
        return 0
    normalized: List[str] = []
    seen = set()
    for tag in tags:
        value = str(tag)
        key = value.lower()
        if key in seen:
            continue
        seen.add(key)
        normalized.append("metronome" if key == "metronome" else value)
    if "metronome" not in seen:
        normalized.insert(0, "metronome")
    if normalized == tags:
        return 0
    output["suggested_tags"] = normalized
    return 1


def _text(value: Any) -> str:
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    return value or ""


def _write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def prepare_minimal_codex_home(target: Path) -> Path:
    target.mkdir(parents=True, exist_ok=True)
    source = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex")))
    for name in ("auth.json", "models_cache.json", "installation_id", "version.json"):
        source_path = source / name
        target_path = target / name
        if source_path.is_file() and not target_path.exists():
            target_path.symlink_to(source_path)
    return target


def recover_attempt(
    root: Path, job_path: Path, ingest_date: str, attempt: int
) -> int:
    job_file = job_path if job_path.is_absolute() else root / job_path
    job = load_json(job_file)
    job_errors = validate_job(root, job)
    if job_errors:
        for error in job_errors:
            print(error)
        return 1
    artifact_dir = root / job["artifact_dir"]
    receipt_path = artifact_dir / "model-worker-receipt.json"
    output_path = artifact_dir / f"attempt-{attempt}" / "output.json"
    if not receipt_path.is_file() or not output_path.is_file():
        print("recovery requires an existing worker receipt and attempt output")
        return 1
    receipt = load_json(receipt_path)
    output = load_json(output_path)
    raw_text = (root / job["raw_path"]).read_text(encoding="utf-8")
    quote_repairs = repair_quote_bounds(raw_text, output)
    raw_link_repairs = 1 if repair_raw_link(job, output) else 0
    tag_repairs = repair_mandatory_tags(output)
    errors = validate_model_output(root, job, output)
    if errors:
        for error in errors:
            print(error)
        return 1
    records = receipt.get("attempts", [])
    record = next(
        (item for item in records if isinstance(item, dict) and item.get("attempt") == attempt),
        None,
    )
    if record is None or record.get("process_exit_code") != 0:
        print("recovery requires a completed model attempt with process_exit_code 0")
        return 1
    accepted_output = artifact_dir / "model-output.json"
    draft_path = artifact_dir / "model-source-draft.md"
    _write_json(accepted_output, output)
    draft_path.write_text(render_model_draft(job, output, ingest_date), encoding="utf-8")
    record["validation_errors_before_recovery"] = record.get("validation_errors", [])
    record["retry_reason_before_recovery"] = record.get("retry_reason")
    record["status"] = "accepted_after_deterministic_repair"
    record["validation_errors"] = []
    record["retry_reason"] = None
    receipt.update(
        {
            "status": "success",
            "process_exit_code": 0,
            "output_path": accepted_output.relative_to(root).as_posix(),
            "draft_path": draft_path.relative_to(root).as_posix(),
            "events_path": record["events_path"],
            "stderr_path": record["stderr_path"],
            "grounding_quotes": output["grounding_quotes"],
            "validation": [
                {"command": "recover_attempt_validate_model_output", "passed": True}
            ],
            "token_usage": record.get("token_usage"),
            "token_usage_unavailable_reason": (
                None
                if record.get("token_usage") is not None
                else "Recovered attempt event stream omitted usage."
            ),
            "quote_line_repairs": receipt.get("quote_line_repairs", 0)
            + quote_repairs,
            "raw_link_repairs": receipt.get("raw_link_repairs", 0)
            + raw_link_repairs,
            "mandatory_tag_repairs": receipt.get("mandatory_tag_repairs", 0)
            + tag_repairs,
            "recovered_from_attempt": attempt,
            "recovery_finished_at": utc_now(),
        }
    )
    _write_json(receipt_path, receipt)
    return 0


def run_worker(
    root: Path,
    job_path: Path,
    ingest_date: str,
    runner: Callable[..., Any] = subprocess.run,
) -> int:
    job_file = job_path if job_path.is_absolute() else root / job_path
    job = load_json(job_file)
    job_errors = validate_job(root, job)
    if job_errors:
        for error in job_errors:
            print(error)
        return 1

    raw_text = (root / job["raw_path"]).read_text(encoding="utf-8")
    profile = build_page_profile(raw_text)
    artifact_dir = root / job["artifact_dir"]
    artifact_dir.mkdir(parents=True, exist_ok=True)
    template = (root / PROMPT_PATH).read_text(encoding="utf-8")
    schema_path = root / SCHEMA_PATH
    started_at = utc_now()
    started_clock = time.monotonic()
    validation_errors: Optional[List[str]] = None
    attempt_records: List[Dict[str, Any]] = []
    usages: List[Optional[Dict[str, Any]]] = []
    total_quote_repairs = 0
    total_raw_link_repairs = 0
    total_tag_repairs = 0
    last_result: Any = None
    last_attempt_dir: Optional[Path] = None
    last_output: Optional[Dict[str, Any]] = None

    with tempfile.TemporaryDirectory(prefix=f"metronome-{job['job_id']}-") as tmp:
        staged_cwd = Path(tmp)
        (staged_cwd / "raw.md").write_text(raw_text, encoding="utf-8")
        minimal_codex_home = prepare_minimal_codex_home(staged_cwd / "codex-home")
        worker_env = os.environ.copy()
        worker_env["CODEX_HOME"] = str(minimal_codex_home)
        for attempt in (1, 2):
            attempt_dir = artifact_dir / f"attempt-{attempt}"
            attempt_dir.mkdir(parents=True, exist_ok=True)
            output_path = attempt_dir / "output.json"
            prompt = build_prompt(template, job, profile, validation_errors)
            command = build_codex_command(
                staged_cwd,
                schema_path,
                output_path,
                prompt,
                job["model"],
                job["reasoning_effort"],
            )
            try:
                result = runner(
                    command,
                    capture_output=True,
                    text=True,
                    cwd=staged_cwd,
                    timeout=int(job.get("timeout_seconds", 900)),
                    env=worker_env,
                )
            except subprocess.TimeoutExpired as exc:
                result = subprocess.CompletedProcess(
                    command,
                    124,
                    stdout=_text(exc.stdout),
                    stderr=_text(exc.stderr) + "\nworker attempt timed out",
                )
            last_result = result
            last_attempt_dir = attempt_dir
            events_path = attempt_dir / "events.jsonl"
            stderr_path = attempt_dir / "stderr.log"
            events_path.write_text(result.stdout or "", encoding="utf-8")
            stderr_path.write_text(result.stderr or "", encoding="utf-8")
            usage = extract_token_usage(result.stdout or "")
            usages.append(usage)

            errors: List[str] = []
            output: Optional[Dict[str, Any]] = None
            if result.returncode != 0:
                errors.append(f"codex process exited with {result.returncode}")
            if not output_path.is_file():
                errors.append("codex did not write the required output file")
            else:
                try:
                    loaded = json.loads(output_path.read_text(encoding="utf-8"))
                    if not isinstance(loaded, dict):
                        errors.append("model output must be one JSON object")
                    else:
                        output = loaded
                        total_quote_repairs += repair_quote_bounds(raw_text, output)
                        if repair_raw_link(job, output):
                            total_raw_link_repairs += 1
                        total_tag_repairs += repair_mandatory_tags(output)
                        _write_json(output_path, output)
                        errors.extend(validate_model_output(root, job, output))
                except json.JSONDecodeError as exc:
                    errors.append(f"model output is invalid JSON: {exc.msg}")

            status = "accepted" if not errors and output is not None else "rejected"
            attempt_records.append(
                {
                    "attempt": attempt,
                    "status": status,
                    "process_exit_code": result.returncode,
                    "validation_errors": errors,
                    "retry_reason": "; ".join(errors) if errors else None,
                    "output_path": output_path.relative_to(root).as_posix(),
                    "events_path": events_path.relative_to(root).as_posix(),
                    "stderr_path": stderr_path.relative_to(root).as_posix(),
                    "token_usage": usage,
                }
            )
            if result.returncode == 124:
                validation_errors = errors
                break
            if not errors and output is not None:
                last_output = output
                accepted_output = artifact_dir / "model-output.json"
                draft_path = artifact_dir / "model-source-draft.md"
                _write_json(accepted_output, output)
                draft_path.write_text(render_model_draft(job, output, ingest_date), encoding="utf-8")
                cumulative = sum_token_usage(usages)
                receipt = {
                    "schema_version": 3,
                    "job_id": job["job_id"],
                    "provider": job["provider"],
                    "canonical_url": job["canonical_url"],
                    "raw_path": job["raw_path"],
                    "source_page": job["source_page"],
                    "status": "success",
                    "model_provider": job["model_provider"],
                    "model": job["model"],
                    "reasoning_effort": job["reasoning_effort"],
                    "attempt_count": attempt,
                    "attempts": attempt_records,
                    "started_at": started_at,
                    "finished_at": utc_now(),
                    "elapsed_seconds": round(time.monotonic() - started_clock, 3),
                    "process_exit_code": result.returncode,
                    "output_path": accepted_output.relative_to(root).as_posix(),
                    "draft_path": draft_path.relative_to(root).as_posix(),
                    "events_path": events_path.relative_to(root).as_posix(),
                    "stderr_path": stderr_path.relative_to(root).as_posix(),
                    "grounding_quotes": output["grounding_quotes"],
                    "validation": [{"command": "validate_model_output", "passed": True}],
                    "token_usage": usage,
                    "cumulative_token_usage": cumulative,
                    "token_usage_unavailable_reason": None if cumulative is not None else "Codex event stream omitted usage.",
                    "quote_line_repairs": total_quote_repairs,
                    "raw_link_repairs": total_raw_link_repairs,
                    "mandatory_tag_repairs": total_tag_repairs,
                    "page_profile": profile,
                }
                _write_json(artifact_dir / "model-worker-receipt.json", receipt)
                return 0
            validation_errors = errors

    assert last_result is not None and last_attempt_dir is not None
    cumulative = sum_token_usage(usages)
    failed = {
        "schema_version": 3,
        "job_id": job["job_id"],
        "provider": job["provider"],
        "canonical_url": job["canonical_url"],
        "raw_path": job["raw_path"],
        "source_page": job["source_page"],
        "status": "failed",
        "model_provider": job["model_provider"],
        "model": job["model"],
        "reasoning_effort": job["reasoning_effort"],
        "attempt_count": len(attempt_records),
        "attempts": attempt_records,
        "started_at": started_at,
        "finished_at": utc_now(),
        "elapsed_seconds": round(time.monotonic() - started_clock, 3),
        "process_exit_code": last_result.returncode,
        "output_path": (last_attempt_dir / "output.json").relative_to(root).as_posix(),
        "draft_path": None,
        "events_path": (last_attempt_dir / "events.jsonl").relative_to(root).as_posix(),
        "stderr_path": (last_attempt_dir / "stderr.log").relative_to(root).as_posix(),
        "grounding_quotes": last_output.get("grounding_quotes", []) if last_output else [],
        "validation": [{"command": "validate_model_output", "passed": False, "errors": validation_errors or ["unknown failure"]}],
        "token_usage": usages[-1] if usages else None,
        "cumulative_token_usage": cumulative,
        "token_usage_unavailable_reason": None if cumulative is not None else "Codex event stream omitted usage.",
        "quote_line_repairs": total_quote_repairs,
        "raw_link_repairs": total_raw_link_repairs,
        "mandatory_tag_repairs": total_tag_repairs,
        "page_profile": profile,
    }
    _write_json(artifact_dir / "model-worker-receipt.json", failed)
    return 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--job", required=True)
    parser.add_argument("--ingest-date", required=True)
    parser.add_argument("--recover-attempt", type=int)
    args = parser.parse_args()
    if args.recover_attempt:
        return recover_attempt(ROOT, Path(args.job), args.ingest_date, args.recover_attempt)
    return run_worker(ROOT, Path(args.job), args.ingest_date)


if __name__ == "__main__":
    raise SystemExit(main())
