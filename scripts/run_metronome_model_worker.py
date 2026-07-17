#!/usr/bin/env python3
"""Run one schema-v3 Metronome evidence-draft job with deterministic repair."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import re
import shutil
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
from metronome_model_runtime import (
    AttemptExecution,
    analyze_event_stream,
    append_progress_event,
    job_lock,
    normalized_output_path,
    raw_output_path,
    resolve_run_dir,
    terminate_process_group,
    run_streaming_process,
    validate_run_id,
    write_json_atomic,
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


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def build_runtime_metadata(
    *,
    raw_bytes: bytes,
    prompt_template_bytes: bytes,
    rendered_prompt: str,
    schema_path: Path,
    codex_executable: str,
    timeout_seconds: int,
    env: Dict[str, str],
) -> Dict[str, Any]:
    """Hash the exact runtime inputs and identify the selected CLI executable."""
    resolved = shutil.which(codex_executable, path=env.get("PATH"))
    executable_path = Path(resolved or codex_executable).expanduser().resolve()
    executable_bytes = executable_path.read_bytes()
    version = subprocess.run(
        [str(executable_path), "--version"],
        cwd=executable_path.parent,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True,
        timeout=10,
    ).stdout.strip()
    return {
        "sha256": {
            "raw_text": _sha256_bytes(raw_bytes),
            "prompt_template": _sha256_bytes(prompt_template_bytes),
            "rendered_prompt": _sha256_bytes(rendered_prompt.encode("utf-8")),
            "output_schema": _sha256_bytes(schema_path.read_bytes()),
            "codex_executable": _sha256_bytes(executable_bytes),
        },
        "codex_executable": str(executable_path),
        "codex_cli_version": version,
        "timeout_seconds": timeout_seconds,
    }


def _build_injected_runtime_metadata(
    *,
    raw_bytes: bytes,
    prompt_template_bytes: bytes,
    rendered_prompt: str,
    schema_path: Path,
    timeout_seconds: int,
    **_ignored: Any,
) -> Dict[str, Any]:
    """Describe deterministic injected attempts without inspecting a host CLI."""
    return {
        "sha256": {
            "raw_text": _sha256_bytes(raw_bytes),
            "prompt_template": _sha256_bytes(prompt_template_bytes),
            "rendered_prompt": _sha256_bytes(rendered_prompt.encode("utf-8")),
            "output_schema": _sha256_bytes(schema_path.read_bytes()),
            "codex_executable": None,
        },
        "codex_executable": None,
        "codex_cli_version": None,
        "timeout_seconds": timeout_seconds,
        "metadata_unavailable_reason": "Attempt used an injected deterministic runner.",
    }


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
        value = re.sub(r"[^a-z0-9]+", "-", str(tag).strip().lower()).strip("-")
        if not value or value in seen:
            continue
        seen.add(value)
        normalized.append(value)
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


def common_git_dir(root: Path) -> Path:
    """Resolve the shared Git directory used by every linked worktree."""
    try:
        output = subprocess.check_output(
            ["git", "-C", str(root), "rev-parse", "--git-common-dir"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        # Deterministic unit roots are not Git repositories. Production roots
        # always take the shared-Git path above.
        return root / ".git"
    path = Path(output)
    return path if path.is_absolute() else root / path


def run_process_in_new_group(
    command: List[str],
    *,
    cwd: Path,
    timeout: int,
    env: Dict[str, str],
    attempt_dir: Path,
) -> AttemptExecution:
    """Run one worker command with selector-based binary output streaming."""
    return run_streaming_process(
        command,
        cwd=cwd,
        timeout=timeout,
        env=env,
        attempt_dir=attempt_dir,
    )


def _buffered_attempt_execution(
    result: Any,
    attempt_dir: Path,
    *,
    started_at: str,
    started_clock: float,
    termination: Optional[Dict[str, Any]],
) -> AttemptExecution:
    """Adapt injected deterministic runners to the live-attempt accounting shape."""
    events_path = attempt_dir / "events.jsonl"
    stderr_path = attempt_dir / "stderr.log"
    progress_path = attempt_dir / "progress.jsonl"
    stdout_bytes = _text(result.stdout).encode("utf-8")
    stderr_bytes = _text(result.stderr).encode("utf-8")
    events_path.write_bytes(stdout_bytes)
    stderr_path.write_bytes(stderr_bytes)
    parsed_count, truncated_count, usage = analyze_event_stream(stdout_bytes)
    elapsed = time.monotonic() - started_clock
    if parsed_count:
        append_progress_event(progress_path, "first_stdout_event", elapsed_seconds=0.0)
    if stderr_bytes:
        append_progress_event(progress_path, "first_stderr_byte", elapsed_seconds=0.0)
    append_progress_event(
        progress_path,
        "process_exited",
        process_return_code=result.returncode,
        logical_return_code=result.returncode,
        injected_runner=True,
    )
    return AttemptExecution(
        returncode=int(result.returncode),
        started_at=started_at,
        finished_at=utc_now(),
        elapsed_seconds=round(elapsed, 6),
        time_to_first_stdout_event_seconds=0.0 if parsed_count else None,
        time_to_first_stderr_byte_seconds=0.0 if stderr_bytes else None,
        streamed_stdout_bytes=len(stdout_bytes),
        streamed_stderr_bytes=len(stderr_bytes),
        parsed_event_count=parsed_count,
        truncated_line_count=truncated_count,
        token_usage=usage,
        termination=termination,
    )


def _execution_accounting(execution: AttemptExecution) -> Dict[str, Any]:
    return {
        "attempt_started_at": execution.started_at,
        "attempt_finished_at": execution.finished_at,
        "attempt_elapsed_seconds": execution.elapsed_seconds,
        "time_to_first_stdout_event_seconds": execution.time_to_first_stdout_event_seconds,
        "time_to_first_stderr_byte_seconds": execution.time_to_first_stderr_byte_seconds,
        "streamed_stdout_bytes": execution.streamed_stdout_bytes,
        "streamed_stderr_bytes": execution.streamed_stderr_bytes,
        "parsed_event_count": execution.parsed_event_count,
        "truncated_line_count": execution.truncated_line_count,
    }


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


def _run_worker_unlocked(
    root: Path,
    job_path: Path,
    ingest_date: str,
    runner: Optional[Callable[..., Any]] = None,
    run_id: Optional[str] = None,
    lock_acquired_at: Optional[str] = None,
    runtime_metadata_provider: Optional[Callable[..., Dict[str, Any]]] = None,
) -> int:
    job_file = job_path if job_path.is_absolute() else root / job_path
    job = load_json(job_file)
    job_errors = validate_job(root, job)
    if job_errors:
        for error in job_errors:
            print(error)
        return 1

    raw_bytes = (root / job["raw_path"]).read_bytes()
    raw_text = raw_bytes.decode("utf-8")
    profile = build_page_profile(raw_text)
    concept_dir = root / "wiki/concepts/metronome"
    profile["existing_metronome_concept_slugs"] = sorted(
        path.stem for path in concept_dir.glob("*.md") if path.is_file()
    )
    diagnostic = run_id is not None
    if diagnostic:
        try:
            run_id = validate_run_id(run_id)
        except ValueError as exc:
            print(exc)
            return 1
        (root / job["artifact_dir"]).mkdir(parents=True, exist_ok=True)
        artifact_dir = resolve_run_dir(root, job, run_id)
        try:
            artifact_dir.mkdir(parents=False, exist_ok=False)
        except FileExistsError:
            print(f"diagnostic run directory already exists: {artifact_dir}")
            return 1
    else:
        artifact_dir = root / job["artifact_dir"]
        artifact_dir.mkdir(parents=True, exist_ok=True)
    template_bytes = (root / PROMPT_PATH).read_bytes()
    template = template_bytes.decode("utf-8")
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
    last_raw_output_path: Optional[Path] = None
    last_normalized_path: Optional[Path] = None
    last_termination: Optional[Dict[str, Any]] = None
    last_execution: Optional[AttemptExecution] = None
    last_runtime_metadata: Optional[Dict[str, Any]] = None

    with tempfile.TemporaryDirectory(prefix=f"metronome-{job['job_id']}-") as tmp:
        staged_cwd = Path(tmp)
        (staged_cwd / "raw.md").write_text(raw_text, encoding="utf-8")
        minimal_codex_home = prepare_minimal_codex_home(staged_cwd / "codex-home")
        worker_env = os.environ.copy()
        worker_env["CODEX_HOME"] = str(minimal_codex_home)
        for attempt in (1, 2):
            attempt_dir = artifact_dir / f"attempt-{attempt}"
            attempt_dir.mkdir(parents=True, exist_ok=True)
            if diagnostic:
                output_path = raw_output_path(attempt_dir)
                normalized_path = normalized_output_path(attempt_dir)
            else:
                output_path = attempt_dir / "output.json"
                normalized_path = None
            prompt = build_prompt(template, job, profile, validation_errors)
            timeout_seconds = int(job.get("timeout_seconds", 900))
            command = build_codex_command(
                staged_cwd,
                schema_path,
                output_path,
                prompt,
                job["model"],
                job["reasoning_effort"],
            )
            termination: Optional[Dict[str, Any]] = None
            progress_path = attempt_dir / "progress.jsonl"
            if diagnostic:
                append_progress_event(
                    progress_path,
                    "lock_acquired",
                    acquired_at=lock_acquired_at or started_at,
                )
                metadata_provider = (
                    build_runtime_metadata
                    if runner is None
                    else runtime_metadata_provider or _build_injected_runtime_metadata
                )
                runtime_metadata = metadata_provider(
                    raw_bytes=raw_bytes,
                    prompt_template_bytes=template_bytes,
                    rendered_prompt=prompt,
                    schema_path=schema_path,
                    codex_executable=command[0],
                    timeout_seconds=timeout_seconds,
                    env=worker_env,
                )
            else:
                runtime_metadata = None
            attempt_started_at = utc_now()
            attempt_started_clock = time.monotonic()
            try:
                if runner is None:
                    execution = run_process_in_new_group(
                        command,
                        cwd=staged_cwd,
                        timeout=timeout_seconds,
                        env=worker_env,
                        attempt_dir=attempt_dir,
                    )
                    termination = execution.termination
                else:
                    append_progress_event(
                        progress_path,
                        "process_started",
                        pid=None,
                        injected_runner=True,
                    )
                    buffered_result = runner(
                        command,
                        capture_output=True,
                        text=True,
                        cwd=staged_cwd,
                        timeout=timeout_seconds,
                        env=worker_env,
                    )
            except subprocess.TimeoutExpired as exc:
                buffered_result = subprocess.CompletedProcess(
                    command,
                    124,
                    stdout=_text(exc.stdout),
                    stderr=_text(exc.stderr) + "\nworker attempt timed out",
                )
                termination = {
                    "signal": None,
                    "grace_seconds": None,
                    "grace_outcome": "runner_timeout",
                    "escalation_signal": None,
                    "final_return_code": 124,
                }
            if runner is not None:
                execution = _buffered_attempt_execution(
                    buffered_result,
                    attempt_dir,
                    started_at=attempt_started_at,
                    started_clock=attempt_started_clock,
                    termination=termination,
                )
            result = execution
            last_result = execution
            last_attempt_dir = attempt_dir
            written_raw_output_path = output_path if output_path.is_file() else None
            events_path = attempt_dir / "events.jsonl"
            stderr_path = attempt_dir / "stderr.log"
            usage = execution.token_usage
            usages.append(usage)

            errors: List[str] = []
            output: Optional[Dict[str, Any]] = None
            written_normalized_path: Optional[Path] = None
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
                        output = copy.deepcopy(loaded)
                        total_quote_repairs += repair_quote_bounds(raw_text, output)
                        if repair_raw_link(job, output):
                            total_raw_link_repairs += 1
                        total_tag_repairs += repair_mandatory_tags(output)
                        if normalized_path is None:
                            _write_json(output_path, output)
                        else:
                            write_json_atomic(normalized_path, output)
                            written_normalized_path = normalized_path
                        errors.extend(validate_model_output(root, job, output))
                except json.JSONDecodeError as exc:
                    errors.append(f"model output is invalid JSON: {exc.msg}")

            status = "accepted" if not errors and output is not None else "rejected"
            append_progress_event(
                progress_path,
                "validation_completed",
                passed=not errors and output is not None,
                error_count=len(errors),
            )
            attempt_record = {
                    "attempt": attempt,
                    "status": status,
                    "process_exit_code": result.returncode,
                    "validation_errors": errors,
                    "retry_reason": "; ".join(errors) if errors else None,
                    "output_path": (
                        written_raw_output_path.relative_to(root).as_posix()
                        if diagnostic and written_raw_output_path is not None
                        else (None if diagnostic else output_path.relative_to(root).as_posix())
                    ),
                    "events_path": events_path.relative_to(root).as_posix(),
                    "stderr_path": stderr_path.relative_to(root).as_posix(),
                    "progress_path": progress_path.relative_to(root).as_posix(),
                    "token_usage": usage,
                }
            if normalized_path is not None:
                attempt_record["normalized_output_path"] = (
                    written_normalized_path.relative_to(root).as_posix()
                    if written_normalized_path is not None
                    else None
                )
            if diagnostic:
                attempt_record["termination"] = termination
                attempt_record["runtime_metadata"] = runtime_metadata
                attempt_record.update(_execution_accounting(execution))
            attempt_records.append(attempt_record)
            last_raw_output_path = written_raw_output_path
            last_normalized_path = written_normalized_path
            last_termination = termination
            last_execution = execution
            last_runtime_metadata = runtime_metadata
            if termination is not None or result.returncode == 124:
                validation_errors = errors
                break
            if not errors and output is not None:
                last_output = output
                accepted_output = (
                    artifact_dir / "model-output.normalized.json"
                    if diagnostic
                    else artifact_dir / "model-output.json"
                )
                draft_path = artifact_dir / "model-source-draft.md"
                if normalized_path is None:
                    _write_json(accepted_output, output)
                else:
                    shutil.copyfile(normalized_path, accepted_output)
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
                if run_id is not None:
                    receipt["run_id"] = run_id
                    receipt["normalized_output_path"] = accepted_output.relative_to(root).as_posix()
                    receipt["termination"] = last_termination
                    receipt["progress_path"] = progress_path.relative_to(root).as_posix()
                    receipt["runtime_metadata"] = last_runtime_metadata
                    receipt.update(_execution_accounting(execution))
                    write_json_atomic(artifact_dir / "model-worker-receipt.json", receipt)
                    append_progress_event(progress_path, "receipt_published")
                else:
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
        "output_path": (
            last_raw_output_path.relative_to(root).as_posix()
            if diagnostic and last_raw_output_path is not None
            else (
                None
                if diagnostic
                else (last_attempt_dir / "output.json").relative_to(root).as_posix()
            )
        ),
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
    if run_id is not None:
        assert last_execution is not None
        failed["run_id"] = run_id
        failed["termination"] = last_termination
        failed["progress_path"] = (
            last_attempt_dir / "progress.jsonl"
        ).relative_to(root).as_posix()
        failed["runtime_metadata"] = last_runtime_metadata
        failed.update(_execution_accounting(last_execution))
        failed["normalized_output_path"] = (
            last_normalized_path.relative_to(root).as_posix()
            if last_normalized_path is not None
            else None
        )
        write_json_atomic(artifact_dir / "model-worker-receipt.json", failed)
        append_progress_event(last_attempt_dir / "progress.jsonl", "receipt_published")
    else:
        _write_json(artifact_dir / "model-worker-receipt.json", failed)
    return 1


def run_worker(
    root: Path,
    job_path: Path,
    ingest_date: str,
    runner: Optional[Callable[..., Any]] = None,
    run_id: Optional[str] = None,
    runtime_metadata_provider: Optional[Callable[..., Dict[str, Any]]] = None,
) -> int:
    """Run one job, serializing diagnostic executions across Git worktrees."""
    if run_id is None:
        return _run_worker_unlocked(root, job_path, ingest_date, runner=runner)
    try:
        run_id = validate_run_id(run_id)
        job = load_json(job_path if job_path.is_absolute() else root / job_path)
        provider = str(job["provider"])
        job_id = str(job["job_id"])
    except (KeyError, ValueError) as exc:
        print(exc)
        return 1
    try:
        with job_lock(common_git_dir(root), provider, job_id):
            return _run_worker_unlocked(
                root,
                job_path,
                ingest_date,
                runner=runner,
                run_id=run_id,
                lock_acquired_at=utc_now(),
                runtime_metadata_provider=runtime_metadata_provider,
            )
    except RuntimeError as exc:
        print(exc)
        return 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--job", required=True)
    parser.add_argument("--ingest-date", required=True)
    parser.add_argument("--run-id")
    parser.add_argument("--recover-attempt", type=int)
    args = parser.parse_args()
    if args.recover_attempt:
        return recover_attempt(ROOT, Path(args.job), args.ingest_date, args.recover_attempt)
    if not args.run_id:
        parser.error("--run-id is required for live diagnostic execution")
    return run_worker(ROOT, Path(args.job), args.ingest_date, run_id=args.run_id)


if __name__ == "__main__":
    raise SystemExit(main())
