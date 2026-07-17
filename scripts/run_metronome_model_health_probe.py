#!/usr/bin/env python3
"""Run the bounded Luna health probe that gates enterprise diagnostics."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Dict, Optional, TypeVar

from metronome_model_runtime import (
    AttemptExecution,
    analyze_event_stream,
    append_progress_event,
    job_lock,
    normalized_output_path,
    raw_output_path,
    run_streaming_process,
    validate_run_id,
    write_json_atomic,
)
from run_metronome_model_worker import (
    _git_provenance,
    _write_bytes_atomic,
    _write_terminal_manifest,
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
TERMINAL_MANIFEST_NAME = "terminal-artifact-manifest.json"
RUNNER_SCRIPT_PATHS = (
    Path(__file__).resolve(),
    Path(__file__).resolve().with_name("metronome_model_runtime.py"),
    Path(__file__).resolve().with_name("run_metronome_model_worker.py"),
)
T = TypeVar("T")


class HealthProbeGateError(RuntimeError):
    """Raised when enterprise diagnostics are attempted without a passing probe."""


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def is_model_activity_event(event: Dict[str, Any]) -> bool:
    """Classify model-produced items while excluding runtime lifecycle chatter."""
    if event.get("type") not in {"item.started", "item.updated", "item.completed"}:
        return False
    item = event.get("item")
    return isinstance(item, dict) and item.get("type") not in (None, "error")


def _read_jsonl(path: Path) -> list:
    records = []
    try:
        lines = path.read_bytes().splitlines()
    except OSError:
        return records
    for line in lines:
        try:
            record = json.loads(line.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
        if isinstance(record, dict):
            records.append(record)
    return records


def _events_contain_model_activity(path: Path) -> bool:
    return any(is_model_activity_event(record) for record in _read_jsonl(path))


def _sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


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


def _snapshot_probe_provenance(
    root: Path, probe_dir: Path, prompt_path: Path, schema_path: Path
) -> Dict[str, Any]:
    """Snapshot the probe's exact prompt and schema before model setup begins."""
    provenance_dir = probe_dir / "provenance"
    prompt_snapshot = provenance_dir / "prompt-template.md"
    schema_snapshot = provenance_dir / "output-schema.json"
    _write_bytes_atomic(prompt_snapshot, prompt_path.read_bytes())
    _write_bytes_atomic(schema_snapshot, schema_path.read_bytes())
    return {
        "prompt_template_snapshot_path": _relative(prompt_snapshot, root),
        "output_schema_snapshot_path": _relative(schema_snapshot, root),
        "rendered_prompt_snapshot_path": None,
        "runner_script_sha256": {
            path.relative_to(ROOT).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in RUNNER_SCRIPT_PATHS
        },
        "git": _git_provenance(root),
    }


def _snapshot_rendered_probe_prompt(
    root: Path, probe_dir: Path, provenance: Dict[str, Any], prompt: str
) -> str:
    path = probe_dir / "provenance" / "rendered-prompt.md"
    _write_bytes_atomic(path, prompt.encode("utf-8"))
    relative_path = _relative(path, root)
    provenance["rendered_prompt_snapshot_path"] = relative_path
    return relative_path


def _publish_probe_receipt(
    root: Path,
    probe_dir: Path,
    receipt_path: Path,
    receipt: Dict[str, Any],
    progress_path: Optional[Path],
) -> None:
    manifest_path = probe_dir / TERMINAL_MANIFEST_NAME
    receipt["terminal_manifest"] = {
        "path": _relative(manifest_path, root),
        "integrity_model": (
            "The terminal manifest hashes the final receipt and all other terminal artifacts; "
            "it intentionally does not hash itself."
        ),
    }
    if progress_path is not None:
        append_progress_event(progress_path, "receipt_published")
    write_json_atomic(receipt_path, receipt)
    _write_terminal_manifest(root, probe_dir, receipt_path.name)


def _unhandled_failure_receipt(state: Dict[str, Any], exc: BaseException) -> int:
    """Publish the terminal fallback for any failure after this process claimed a run."""
    now = time.monotonic()
    deadline = state["deadline_monotonic"]
    receipt = {
        "schema_version": 1,
        "diagnostic_type": "model_health_probe",
        "run_id": state["run_id"],
        "status": "failed",
        "model_provider": "openai",
        "model": MODEL,
        "reasoning_effort": REASONING_EFFORT,
        "input_mode": "fixed-prompt",
        "started_at": state["started_at"],
        "finished_at": _utc_now(),
        "total_timeout_seconds": state["total_timeout_seconds"],
        "deadline_monotonic": deadline,
        "total_elapsed_seconds": round(now - state["started_clock"], 6),
        "within_total_timeout": now <= deadline,
        "receipt_published_within_deadline": now <= deadline,
        "process_exit_code": None,
        "runtime_metadata": None,
        "artifact_sha256": {},
        "output_path": None,
        "normalized_output_path": None,
        "events_path": None,
        "stderr_path": None,
        "progress_path": None,
        "failures": [f"unhandled post-claim health probe setup failed: {exc}"],
        "canonical_coverage_eligible": False,
        "provenance": state.get("provenance", {"status": "incomplete"}),
    }
    try:
        _publish_probe_receipt(
            state["root"],
            state["probe_dir"],
            state["receipt_path"],
            receipt,
            state.get("progress_path"),
        )
    except Exception:
        write_json_atomic(state["receipt_path"], receipt)
    return 1


def run_health_probe(
    root: Path,
    run_id: str,
    *,
    executor: Callable[..., AttemptExecution] = run_streaming_process,
    runtime_metadata_provider: Callable[..., Dict[str, Any]] = build_runtime_metadata,
    total_timeout_seconds: float = TOTAL_TIMEOUT_SECONDS,
) -> int:
    """Run a probe with one fail-closed boundary around the claimed lifecycle."""
    claim_state: Dict[str, Any] = {}
    try:
        return _run_health_probe_impl(
            root,
            run_id,
            executor=executor,
            runtime_metadata_provider=runtime_metadata_provider,
            total_timeout_seconds=total_timeout_seconds,
            claim_state=claim_state,
        )
    except BaseException as exc:
        if not claim_state.get("claimed"):
            raise
        result = _unhandled_failure_receipt(claim_state, exc)
        if isinstance(exc, (KeyboardInterrupt, SystemExit)):
            raise
        return result


def _run_health_probe_impl(
    root: Path,
    run_id: str,
    *,
    executor: Callable[..., AttemptExecution],
    runtime_metadata_provider: Callable[..., Dict[str, Any]],
    total_timeout_seconds: float,
    claim_state: Dict[str, Any],
) -> int:
    """Run one immutable, diagnostic-only probe and atomically publish its receipt."""
    root = Path(root).resolve()
    run_id = validate_run_id(run_id)
    if total_timeout_seconds <= 0 or total_timeout_seconds > TOTAL_TIMEOUT_SECONDS:
        raise ValueError("health probe timeout must be greater than zero and at most 60 seconds")

    prompt_path = root / PROMPT_PATH
    schema_path = root / SCHEMA_PATH
    probe_dir = root / PROBE_ROOT / run_id

    with job_lock(common_git_dir(root), "metronome", "model-health-probe"):
        try:
            probe_dir.mkdir(parents=True, exist_ok=False)
        except FileExistsError as exc:
            raise RuntimeError(f"health probe run directory already exists: {probe_dir}") from exc

        started_at = _utc_now()
        started_clock = time.monotonic()
        deadline_monotonic = started_clock + total_timeout_seconds
        receipt_path = probe_dir / "model-health-probe-receipt.json"
        claim_state.update(
            {
                "claimed": True,
                "root": root,
                "probe_dir": probe_dir,
                "run_id": run_id,
                "started_at": started_at,
                "started_clock": started_clock,
                "deadline_monotonic": deadline_monotonic,
                "total_timeout_seconds": total_timeout_seconds,
                "receipt_path": receipt_path,
                "progress_path": None,
            }
        )
        provenance = _snapshot_probe_provenance(root, probe_dir, prompt_path, schema_path)
        claim_state["provenance"] = provenance
        prompt_snapshot_path = root / provenance["prompt_template_snapshot_path"]
        schema_snapshot_path = root / provenance["output_schema_snapshot_path"]
        attempt_dir = probe_dir / "attempt-1"
        events_path = attempt_dir / "events.jsonl"
        stderr_path = attempt_dir / "stderr.log"
        progress_path = attempt_dir / "progress.jsonl"
        try:
            attempt_dir.mkdir()
            for path in (events_path, stderr_path, progress_path):
                path.touch()
            append_progress_event(progress_path, "lock_acquired")
            claim_state["progress_path"] = progress_path
        except Exception as exc:
            failure_receipt = {
                "schema_version": 1,
                "diagnostic_type": "model_health_probe",
                "run_id": run_id,
                "status": "failed",
                "model_provider": "openai",
                "model": MODEL,
                "reasoning_effort": REASONING_EFFORT,
                "input_mode": "fixed-prompt",
                "started_at": started_at,
                "finished_at": _utc_now(),
                "total_timeout_seconds": total_timeout_seconds,
                "deadline_monotonic": deadline_monotonic,
                "total_elapsed_seconds": round(time.monotonic() - started_clock, 6),
                "within_total_timeout": time.monotonic() <= deadline_monotonic,
                "receipt_published_within_deadline": time.monotonic()
                <= deadline_monotonic,
                "process_exit_code": None,
                "runtime_metadata": None,
                "artifact_sha256": {},
                "output_path": None,
                "normalized_output_path": None,
                "events_path": None,
                "stderr_path": None,
                "progress_path": None,
                "failures": [f"health probe bootstrap failed: {exc}"],
                "canonical_coverage_eligible": False,
                "provenance": provenance,
            }
            _publish_probe_receipt(root, probe_dir, receipt_path, failure_receipt, None)
            return 1

        execution: Optional[AttemptExecution] = None
        runtime_metadata: Optional[Dict[str, Any]] = None
        preflight_error: Optional[str] = None
        prompt_bytes = b""
        prompt = ""
        raw_path = raw_output_path(attempt_dir)
        normalized_path = normalized_output_path(attempt_dir)

        try:
            prompt_bytes = prompt_snapshot_path.read_bytes()
            prompt = prompt_bytes.decode("utf-8")
            _snapshot_rendered_probe_prompt(root, probe_dir, provenance, prompt)
            prompt = (
                root / provenance["rendered_prompt_snapshot_path"]
            ).read_text(encoding="utf-8")
            schema_snapshot_path.read_bytes()
            with tempfile.TemporaryDirectory(prefix=f"metronome-health-{run_id}-") as tmp:
                staged_cwd = Path(tmp)
                minimal_codex_home = prepare_minimal_codex_home(staged_cwd / "codex-home")
                probe_env = os.environ.copy()
                probe_env["CODEX_HOME"] = str(minimal_codex_home)
                command = build_codex_command(
                    staged_cwd,
                    schema_snapshot_path,
                    raw_path,
                    prompt,
                    MODEL,
                    REASONING_EFFORT,
                )
                runtime_metadata = runtime_metadata_provider(
                    raw_bytes=b"",
                    prompt_template_bytes=prompt_bytes,
                    rendered_prompt=prompt,
                    schema_path=schema_snapshot_path,
                    codex_executable=command[0],
                    timeout_seconds=total_timeout_seconds,
                    env=probe_env,
                    deadline_monotonic=deadline_monotonic,
                )
                cleanup_budget = min(
                    PROCESS_CLEANUP_BUDGET_SECONDS, total_timeout_seconds / 4
                )
                process_timeout = deadline_monotonic - time.monotonic() - cleanup_budget
                if process_timeout <= 0:
                    raise TimeoutError("health probe total cap exhausted before model launch")
                try:
                    execution = executor(
                        command,
                        cwd=staged_cwd,
                        timeout=process_timeout,
                        env=probe_env,
                        attempt_dir=attempt_dir,
                        model_event_classifier=is_model_activity_event,
                        absolute_deadline=deadline_monotonic,
                    )
                except Exception as exc:
                    raise RuntimeError(f"probe process launch failed: {exc}") from exc
        except Exception as exc:
            preflight_error = f"health probe setup failed: {exc}"

        terminal_json_valid = _terminal_json_is_valid(raw_path)
        if terminal_json_valid:
            try:
                write_json_atomic(
                    normalized_path,
                    json.loads(raw_path.read_text(encoding="utf-8")),
                )
            except Exception as exc:
                preflight_error = f"health probe normalization failed: {exc}"
                terminal_json_valid = False
        first_stdout_latency = (
            execution.time_to_first_stdout_event_seconds if execution is not None else None
        )
        first_event_latency = (
            getattr(execution, "time_to_first_model_event_seconds", None)
            if execution is not None and _events_contain_model_activity(events_path)
            else None
        )
        append_progress_event(
            progress_path,
            "model_activity_classified",
            observed=first_event_latency is not None,
            elapsed_seconds=first_event_latency,
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
        within_total_timeout = time.monotonic() <= deadline_monotonic
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
            total_elapsed_seconds=round(total_elapsed, 6),
        )
        artifact_hashes = {
            "events": _sha256_path(events_path),
            "stderr": _sha256_path(stderr_path),
            "raw_output": _sha256_path(raw_path) if raw_path.is_file() else None,
            "normalized_output": (
                _sha256_path(normalized_path) if normalized_path.is_file() else None
            ),
        }
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
            "deadline_monotonic": deadline_monotonic,
            "total_elapsed_seconds": round(total_elapsed, 6),
            "within_total_timeout": within_total_timeout,
            "receipt_published_within_deadline": time.monotonic() <= deadline_monotonic,
            "first_model_event_limit_seconds": FIRST_MODEL_EVENT_LIMIT_SECONDS,
            "first_model_event_latency_seconds": first_event_latency,
            "first_model_event_within_limit": first_event_within_limit,
            "time_to_first_stdout_event_seconds": first_stdout_latency,
            "time_to_first_model_event_seconds": first_event_latency,
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
            "artifact_sha256": artifact_hashes,
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
            "provenance": provenance,
        }
        try:
            _publish_probe_receipt(
                root, probe_dir, receipt_path, receipt, progress_path
            )
        except Exception as exc:
            receipt["status"] = "failed"
            receipt["receipt_published_within_deadline"] = False
            receipt["within_total_timeout"] = False
            receipt["failures"].append(f"initial receipt publication failed: {exc}")
            _publish_probe_receipt(
                root, probe_dir, receipt_path, receipt, None
            )
        if time.monotonic() > deadline_monotonic:
            receipt["status"] = "failed"
            receipt["receipt_published_within_deadline"] = False
            receipt["within_total_timeout"] = False
            if not any("deadline" in failure for failure in receipt["failures"]):
                receipt["failures"].append(
                    "health probe receipt publication exceeded the absolute deadline"
                )
            _publish_probe_receipt(
                root, probe_dir, receipt_path, receipt, None
            )
            passed = False
        return 0 if passed else 1


def _reject_gate(reason: str) -> None:
    raise HealthProbeGateError(f"enterprise A/B remains suspended: {reason}")


def _load_passing_probe_receipt(root: Path, run_id: str) -> Dict[str, Any]:
    root = Path(root).resolve()
    try:
        run_id = validate_run_id(run_id)
    except ValueError as exc:
        raise HealthProbeGateError(
            "enterprise A/B remains suspended: invalid health probe run ID"
        ) from exc
    probe_dir = root / PROBE_ROOT / run_id
    attempt_dir = probe_dir / "attempt-1"
    receipt_path = probe_dir / "model-health-probe-receipt.json"
    receipt_tmp = receipt_path.with_name(f"{receipt_path.name}.tmp")
    if (
        not probe_dir.is_dir()
        or probe_dir.is_symlink()
        or not attempt_dir.is_dir()
        or attempt_dir.is_symlink()
        or not receipt_path.is_file()
        or receipt_path.is_symlink()
        or receipt_tmp.exists()
    ):
        _reject_gate("expected immutable health probe receipt is incomplete")
    try:
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise HealthProbeGateError(
            "enterprise A/B remains suspended: health probe receipt is unavailable or invalid"
        ) from exc
    if not isinstance(receipt, dict):
        _reject_gate("health probe receipt must be one JSON object")

    expected_paths = {
        "output_path": _relative(raw_output_path(attempt_dir), root),
        "normalized_output_path": _relative(normalized_output_path(attempt_dir), root),
        "events_path": _relative(attempt_dir / "events.jsonl", root),
        "stderr_path": _relative(attempt_dir / "stderr.log", root),
        "progress_path": _relative(attempt_dir / "progress.jsonl", root),
    }
    if any(receipt.get(key) != value for key, value in expected_paths.items()):
        _reject_gate("receipt artifact paths do not match the expected immutable run")
    artifact_paths = {
        key: root / value for key, value in expected_paths.items()
    }
    if any(
        not path.is_file() or path.is_symlink() or path.with_name(f"{path.name}.tmp").exists()
        for path in artifact_paths.values()
    ):
        _reject_gate("health probe artifacts are missing, linked, or incomplete")

    raw_path = artifact_paths["output_path"]
    normalized_path = artifact_paths["normalized_output_path"]
    events_path = artifact_paths["events_path"]
    stderr_path = artifact_paths["stderr_path"]
    progress_path = artifact_paths["progress_path"]
    if not _terminal_json_is_valid(raw_path) or not _terminal_json_is_valid(normalized_path):
        _reject_gate("terminal probe JSON is invalid")

    provenance = receipt.get("provenance")
    if not isinstance(provenance, dict):
        _reject_gate("probe provenance is incomplete")
    expected_provenance_paths = {
        "prompt_template_snapshot_path": _relative(
            probe_dir / "provenance" / "prompt-template.md", root
        ),
        "output_schema_snapshot_path": _relative(
            probe_dir / "provenance" / "output-schema.json", root
        ),
        "rendered_prompt_snapshot_path": _relative(
            probe_dir / "provenance" / "rendered-prompt.md", root
        ),
    }
    if any(provenance.get(key) != value for key, value in expected_provenance_paths.items()):
        _reject_gate("probe provenance paths do not match the immutable run")
    provenance_paths = {
        key: root / value for key, value in expected_provenance_paths.items()
    }
    if any(
        not path.is_file() or path.is_symlink() or path.with_name(f"{path.name}.tmp").exists()
        for path in provenance_paths.values()
    ):
        _reject_gate("probe provenance snapshots are missing, linked, or incomplete")
    expected_runner_hashes = {
        path.relative_to(ROOT).as_posix(): _sha256_path(path)
        for path in RUNNER_SCRIPT_PATHS
    }
    if provenance.get("runner_script_sha256") != expected_runner_hashes:
        _reject_gate("probe runner-script provenance does not reconcile")
    git_provenance = provenance.get("git")
    if (
        not isinstance(git_provenance, dict)
        or set(git_provenance)
        != {"commit", "dirty", "dirty_status_sha256", "unavailable_reason"}
    ):
        _reject_gate("probe Git provenance is incomplete")

    manifest_path = probe_dir / TERMINAL_MANIFEST_NAME
    manifest_record = receipt.get("terminal_manifest")
    if (
        not manifest_path.is_file()
        or manifest_path.is_symlink()
        or manifest_path.with_name(f"{manifest_path.name}.tmp").exists()
        or not isinstance(manifest_record, dict)
        or manifest_record.get("path") != _relative(manifest_path, root)
    ):
        _reject_gate("terminal probe manifest is incomplete")
    try:
        terminal_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        _reject_gate("terminal probe manifest is invalid")
    expected_manifest_hashes = {}
    for path in sorted(probe_dir.rglob("*")):
        if (
            not path.is_file()
            or path.is_symlink()
            or path == manifest_path
            or path.name.endswith(".tmp")
        ):
            continue
        expected_manifest_hashes[_relative(path, root)] = _sha256_path(path)
    if terminal_manifest != {
        "schema_version": 1,
        "sha256": expected_manifest_hashes,
        "not_covered_due_to_self_reference": _relative(manifest_path, root),
        "receipt_sha256_covered": True,
    }:
        _reject_gate("terminal probe manifest hashes do not reconcile")

    recorded_hashes = receipt.get("artifact_sha256")
    recomputed_hashes = {
        "events": _sha256_path(events_path),
        "stderr": _sha256_path(stderr_path),
        "raw_output": _sha256_path(raw_path),
        "normalized_output": _sha256_path(normalized_path),
    }
    if recorded_hashes != recomputed_hashes:
        _reject_gate("health probe artifact hashes do not reconcile")

    events_bytes = events_path.read_bytes()
    parsed_count, truncated_count, usage = analyze_event_stream(events_bytes)
    if (
        receipt.get("streamed_stdout_bytes") != len(events_bytes)
        or receipt.get("streamed_stderr_bytes") != stderr_path.stat().st_size
        or receipt.get("parsed_event_count") != parsed_count
        or receipt.get("truncated_line_count") != truncated_count
        or receipt.get("token_usage") != usage
        or not _events_contain_model_activity(events_path)
    ):
        _reject_gate("event-stream accounting or model activity does not reconcile")

    progress = _read_jsonl(progress_path)
    classified = [item for item in progress if item.get("event") == "model_activity_classified"]
    runtime_model_events = [
        item for item in progress if item.get("event") == "first_model_event"
    ]
    process_started = [item for item in progress if item.get("event") == "process_started"]
    process_exited = [item for item in progress if item.get("event") == "process_exited"]
    validations = [
        item for item in progress if item.get("event") == "validation_completed"
    ]
    if (
        not progress
        or progress[-1].get("event") != "receipt_published"
        or len(classified) != 1
        or len(runtime_model_events) != 1
        or len(process_started) != 1
        or len(process_exited) != 1
        or len(validations) != 1
        or classified[0].get("observed") is not True
    ):
        _reject_gate("receipt publication or model-activity progress is incomplete")
    model_latency = classified[0].get("elapsed_seconds")
    runtime_model_latency = runtime_model_events[0].get("elapsed_seconds")
    stdout_latency = receipt.get("time_to_first_stdout_event_seconds")
    total_elapsed = receipt.get("total_elapsed_seconds")
    attempt_elapsed = receipt.get("attempt_elapsed_seconds")
    if not all(
        isinstance(value, (int, float)) and not isinstance(value, bool) and value >= 0
        for value in (
            model_latency,
            runtime_model_latency,
            stdout_latency,
            total_elapsed,
            attempt_elapsed,
        )
    ):
        _reject_gate("probe latency or elapsed accounting is invalid")
    if (
        model_latency > FIRST_MODEL_EVENT_LIMIT_SECONDS
        or runtime_model_latency != model_latency
        or stdout_latency > model_latency
        or attempt_elapsed > total_elapsed
        or total_elapsed > TOTAL_TIMEOUT_SECONDS
        or process_exited[0].get("elapsed_seconds") != attempt_elapsed
        or validations[0].get("total_elapsed_seconds") != total_elapsed
        or process_exited[0].get("logical_return_code") != 0
        or process_exited[0].get("process_return_code") != 0
        or validations[0].get("passed") is not True
        or validations[0].get("error_count") != 0
        or receipt.get("first_model_event_latency_seconds") != model_latency
        or receipt.get("time_to_first_model_event_seconds") != model_latency
    ):
        _reject_gate("probe latency or elapsed gates do not reconcile")

    metadata = receipt.get("runtime_metadata")
    if not _metadata_is_complete(metadata, TOTAL_TIMEOUT_SECONDS):
        _reject_gate("runtime metadata is incomplete")
    assert isinstance(metadata, dict)
    hashes = metadata["sha256"]
    prompt_path = provenance_paths["prompt_template_snapshot_path"]
    rendered_prompt_path = provenance_paths["rendered_prompt_snapshot_path"]
    schema_path = provenance_paths["output_schema_snapshot_path"]
    executable_path = Path(metadata["codex_executable"])
    if not executable_path.is_file():
        _reject_gate("recorded Codex executable is unavailable")
    expected_runtime_hashes = {
        "raw_text": hashlib.sha256(b"").hexdigest(),
        "prompt_template": _sha256_path(prompt_path),
        "rendered_prompt": _sha256_path(rendered_prompt_path),
        "output_schema": _sha256_path(schema_path),
        "codex_executable": _sha256_path(executable_path),
    }
    if hashes != expected_runtime_hashes:
        _reject_gate("runtime input or executable provenance does not reconcile")

    required_values = {
        "schema_version": 1,
        "diagnostic_type": "model_health_probe",
        "run_id": run_id,
        "status": "passed",
        "model_provider": "openai",
        "model": MODEL,
        "reasoning_effort": REASONING_EFFORT,
        "input_mode": "fixed-prompt",
        "total_timeout_seconds": TOTAL_TIMEOUT_SECONDS,
        "first_model_event_limit_seconds": FIRST_MODEL_EVENT_LIMIT_SECONDS,
        "process_exit_code": 0,
        "failures": [],
        "canonical_coverage_eligible": False,
        "termination": None,
        "receipt_published_within_deadline": True,
    }
    if any(receipt.get(key) != value for key, value in required_values.items()):
        _reject_gate("receipt identity, exit, failure, or scope facts do not reconcile")
    cleanup = receipt.get("process_cleanup")
    if cleanup != {"passed": True, "termination": None}:
        _reject_gate("process cleanup facts do not reconcile")
    recomputed_summaries = {
        "within_total_timeout": True,
        "terminal_json_valid": True,
        "first_model_event_within_limit": True,
        "runtime_metadata_complete": True,
        "process_cleanup_passed": True,
    }
    if any(receipt.get(key) != value for key, value in recomputed_summaries.items()):
        _reject_gate("receipt summary fields disagree with recomputed gate facts")
    return receipt


def launch_enterprise_ab_if_probe_passes(
    root: Path, run_id: str, launcher: Callable[[], T]
) -> T:
    """Enforce the health gate before calling a separately supplied orchestrator."""
    _load_passing_probe_receipt(root, run_id)
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
