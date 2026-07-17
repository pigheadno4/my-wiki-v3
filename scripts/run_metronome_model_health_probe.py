#!/usr/bin/env python3
"""Run the bounded Luna health probe that gates enterprise diagnostics."""
from __future__ import annotations

import argparse
import json
import os
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Dict, Optional, TypeVar

from metronome_model_runtime import (
    AttemptExecution,
    append_progress_event,
    job_lock,
    normalized_output_path,
    raw_output_path,
    run_streaming_process,
    validate_run_id,
    write_json_atomic,
)
from run_metronome_model_worker import (
    build_codex_command,
    build_runtime_metadata,
    common_git_dir,
    prepare_minimal_codex_home,
)


ROOT = Path(__file__).resolve().parent.parent
PROBE_ROOT = Path("tracking/ingest/metronome/pilot/diagnostics/health-probes")
SCHEMA_PATH = Path(
    "tracking/ingest/metronome/pilot/schemas/model-health-probe.schema.json"
)
PROMPT_PATH = Path(
    "tracking/ingest/metronome/pilot/prompts/model-health-probe.md"
)
MODEL = "gpt-5.6-luna"
REASONING_EFFORT = "high"
TOTAL_TIMEOUT_SECONDS = 60
FIRST_MODEL_EVENT_LIMIT_SECONDS = 30
PROCESS_CLEANUP_BUDGET_SECONDS = 6.0
RUNTIME_HASH_KEYS = frozenset(
    (
        "raw_text",
        "prompt_template",
        "rendered_prompt",
        "output_schema",
        "codex_executable",
    )
)
T = TypeVar("T")


class HealthProbeGateError(RuntimeError):
    """Raised when enterprise diagnostics are attempted without a passing probe."""


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _metadata_is_complete(metadata: Optional[Dict[str, Any]], timeout: float) -> bool:
    if not isinstance(metadata, dict):
        return False
    hashes = metadata.get("sha256")
    if not isinstance(hashes, dict) or set(hashes) != RUNTIME_HASH_KEYS:
        return False
    if not all(
        isinstance(hashes[key], str)
        and len(hashes[key]) == 64
        and all(character in "0123456789abcdef" for character in hashes[key])
        for key in RUNTIME_HASH_KEYS
    ):
        return False
    return (
        isinstance(metadata.get("codex_executable"), str)
        and bool(metadata["codex_executable"])
        and isinstance(metadata.get("codex_cli_version"), str)
        and bool(metadata["codex_cli_version"])
        and metadata.get("timeout_seconds") == timeout
    )


def _terminal_json_is_valid(path: Path) -> bool:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    return payload == {"status": "ok"}


def _process_cleanup_passed(execution: Optional[AttemptExecution]) -> bool:
    if execution is None:
        return True
    termination = execution.termination
    if termination is None:
        return True
    return (
        termination.get("grace_outcome")
        in {"already_exited", "terminated", "killed"}
        and termination.get("final_return_code") is not None
    )


def _relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def run_health_probe(
    root: Path,
    run_id: str,
    *,
    executor: Callable[..., AttemptExecution] = run_streaming_process,
    runtime_metadata_provider: Callable[..., Dict[str, Any]] = build_runtime_metadata,
    total_timeout_seconds: float = TOTAL_TIMEOUT_SECONDS,
) -> int:
    """Run one immutable, diagnostic-only probe and atomically publish its receipt."""
    root = Path(root).resolve()
    run_id = validate_run_id(run_id)
    if total_timeout_seconds <= 0 or total_timeout_seconds > TOTAL_TIMEOUT_SECONDS:
        raise ValueError("health probe timeout must be greater than zero and at most 60 seconds")

    prompt_path = root / PROMPT_PATH
    schema_path = root / SCHEMA_PATH
    prompt_bytes = prompt_path.read_bytes()
    prompt = prompt_bytes.decode("utf-8")
    schema_path.read_bytes()
    probe_dir = root / PROBE_ROOT / run_id

    with job_lock(common_git_dir(root), "metronome", "model-health-probe"):
        try:
            probe_dir.mkdir(parents=True, exist_ok=False)
        except FileExistsError as exc:
            raise RuntimeError(f"health probe run directory already exists: {probe_dir}") from exc

        attempt_dir = probe_dir / "attempt-1"
        attempt_dir.mkdir()
        events_path = attempt_dir / "events.jsonl"
        stderr_path = attempt_dir / "stderr.log"
        progress_path = attempt_dir / "progress.jsonl"
        for path in (events_path, stderr_path, progress_path):
            path.touch()
        append_progress_event(progress_path, "lock_acquired")

        started_at = _utc_now()
        started_clock = time.monotonic()
        execution: Optional[AttemptExecution] = None
        runtime_metadata: Optional[Dict[str, Any]] = None
        preflight_error: Optional[str] = None
        raw_path = raw_output_path(attempt_dir)
        normalized_path = normalized_output_path(attempt_dir)

        with tempfile.TemporaryDirectory(prefix=f"metronome-health-{run_id}-") as tmp:
            staged_cwd = Path(tmp)
            minimal_codex_home = prepare_minimal_codex_home(staged_cwd / "codex-home")
            probe_env = os.environ.copy()
            probe_env["CODEX_HOME"] = str(minimal_codex_home)
            command = build_codex_command(
                staged_cwd,
                schema_path,
                raw_path,
                prompt,
                MODEL,
                REASONING_EFFORT,
            )
            try:
                runtime_metadata = runtime_metadata_provider(
                    raw_bytes=b"",
                    prompt_template_bytes=prompt_bytes,
                    rendered_prompt=prompt,
                    schema_path=schema_path,
                    codex_executable=command[0],
                    timeout_seconds=total_timeout_seconds,
                    env=probe_env,
                )
            except Exception as exc:  # pragma: no cover - host-specific preflight failures
                preflight_error = f"runtime metadata preflight failed: {exc}"

            elapsed_before_process = time.monotonic() - started_clock
            cleanup_budget = min(
                PROCESS_CLEANUP_BUDGET_SECONDS, total_timeout_seconds / 4
            )
            process_timeout = total_timeout_seconds - elapsed_before_process - cleanup_budget
            if preflight_error is None and process_timeout > 0:
                try:
                    execution = executor(
                        command,
                        cwd=staged_cwd,
                        timeout=process_timeout,
                        env=probe_env,
                        attempt_dir=attempt_dir,
                    )
                except Exception as exc:  # pragma: no cover - host-specific launch failures
                    preflight_error = f"probe process launch failed: {exc}"
            elif preflight_error is None:
                preflight_error = "health probe total cap exhausted before model launch"

        terminal_json_valid = _terminal_json_is_valid(raw_path)
        if terminal_json_valid:
            write_json_atomic(
                normalized_path,
                json.loads(raw_path.read_text(encoding="utf-8")),
            )
        first_event_latency = (
            execution.time_to_first_stdout_event_seconds if execution is not None else None
        )
        first_event_within_limit = (
            first_event_latency is not None
            and first_event_latency <= FIRST_MODEL_EVENT_LIMIT_SECONDS
        )
        runtime_metadata_complete = _metadata_is_complete(
            runtime_metadata, total_timeout_seconds
        )
        process_cleanup_passed = _process_cleanup_passed(execution)
        wall_elapsed = time.monotonic() - started_clock
        total_elapsed = max(
            wall_elapsed,
            execution.elapsed_seconds if execution is not None else 0.0,
        )
        within_total_timeout = total_elapsed <= total_timeout_seconds
        process_exit_code = execution.returncode if execution is not None else None

        failures = []
        if preflight_error:
            failures.append(preflight_error)
        if process_exit_code != 0:
            failures.append(f"probe process exited with {process_exit_code}")
        if not first_event_within_limit:
            failures.append("first model event was not observed within 30 seconds")
        if not within_total_timeout:
            failures.append("probe exceeded the 60-second total cap")
        if not terminal_json_valid:
            failures.append("terminal output was not the valid tiny probe JSON")
        if not runtime_metadata_complete:
            failures.append("runtime metadata was incomplete")
        if not process_cleanup_passed:
            failures.append("probe process cleanup was incomplete")

        passed = not failures
        append_progress_event(
            progress_path,
            "validation_completed",
            passed=passed,
            error_count=len(failures),
        )
        receipt = {
            "schema_version": 1,
            "diagnostic_type": "model_health_probe",
            "run_id": run_id,
            "status": "passed" if passed else "failed",
            "model_provider": "openai",
            "model": MODEL,
            "reasoning_effort": REASONING_EFFORT,
            "input_mode": "fixed-prompt",
            "started_at": started_at,
            "finished_at": _utc_now(),
            "attempt_started_at": execution.started_at if execution else None,
            "attempt_finished_at": execution.finished_at if execution else None,
            "attempt_elapsed_seconds": execution.elapsed_seconds if execution else None,
            "total_timeout_seconds": total_timeout_seconds,
            "total_elapsed_seconds": round(total_elapsed, 6),
            "within_total_timeout": within_total_timeout,
            "first_model_event_limit_seconds": FIRST_MODEL_EVENT_LIMIT_SECONDS,
            "first_model_event_latency_seconds": first_event_latency,
            "first_model_event_within_limit": first_event_within_limit,
            "time_to_first_stdout_event_seconds": first_event_latency,
            "time_to_first_stderr_byte_seconds": (
                execution.time_to_first_stderr_byte_seconds if execution else None
            ),
            "terminal_json_valid": terminal_json_valid,
            "runtime_metadata_complete": runtime_metadata_complete,
            "process_cleanup_passed": process_cleanup_passed,
            "process_cleanup": {
                "passed": process_cleanup_passed,
                "termination": execution.termination if execution else None,
            },
            "process_exit_code": process_exit_code,
            "runtime_metadata": runtime_metadata,
            "termination": execution.termination if execution is not None else None,
            "streamed_stdout_bytes": (
                execution.streamed_stdout_bytes if execution is not None else 0
            ),
            "streamed_stderr_bytes": (
                execution.streamed_stderr_bytes if execution is not None else 0
            ),
            "parsed_event_count": execution.parsed_event_count if execution else 0,
            "truncated_line_count": execution.truncated_line_count if execution else 0,
            "token_usage": execution.token_usage if execution else None,
            "output_path": _relative(raw_path, root) if raw_path.is_file() else None,
            "normalized_output_path": (
                _relative(normalized_path, root) if normalized_path.is_file() else None
            ),
            "events_path": _relative(events_path, root),
            "stderr_path": _relative(stderr_path, root),
            "progress_path": _relative(progress_path, root),
            "failures": failures,
            "canonical_coverage_eligible": False,
        }
        receipt_path = probe_dir / "model-health-probe-receipt.json"
        write_json_atomic(receipt_path, receipt)
        append_progress_event(progress_path, "receipt_published")
        return 0 if passed else 1


def _load_passing_probe_receipt(receipt_path: Path) -> Dict[str, Any]:
    try:
        receipt = json.loads(Path(receipt_path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise HealthProbeGateError(
            "enterprise A/B remains suspended: health probe receipt is unavailable or invalid"
        ) from exc
    required = {
        "diagnostic_type": "model_health_probe",
        "status": "passed",
        "within_total_timeout": True,
        "terminal_json_valid": True,
        "first_model_event_within_limit": True,
        "runtime_metadata_complete": True,
        "process_cleanup_passed": True,
    }
    if not isinstance(receipt, dict) or any(
        receipt.get(key) != value for key, value in required.items()
    ):
        raise HealthProbeGateError(
            "enterprise A/B remains suspended: a passing health probe is required"
        )
    return receipt


def launch_enterprise_ab_if_probe_passes(
    receipt_path: Path, launcher: Callable[[], T]
) -> T:
    """Enforce the health gate before calling a separately supplied orchestrator."""
    _load_passing_probe_receipt(receipt_path)
    return launcher()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run one immutable, diagnostic-only Luna health probe."
    )
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--run-id", required=True)
    args = parser.parse_args()
    try:
        return run_health_probe(args.root, args.run_id)
    except (OSError, RuntimeError, UnicodeDecodeError, ValueError) as exc:
        print(exc)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
