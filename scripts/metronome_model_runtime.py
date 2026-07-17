"""Immutable artifact helpers for Metronome model-worker diagnostics."""
from __future__ import annotations

import contextlib
from dataclasses import dataclass
from datetime import datetime, timezone
import fcntl
import hashlib
import json
import os
import re
import selectors
import signal
import subprocess
import time
from pathlib import Path
from typing import Any, Callable, Dict, Iterator, List, Optional, Tuple


RUN_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LOCK_KEY_RE = re.compile(r"[^a-z0-9]+")


@dataclass
class AttemptExecution:
    """Bounded accounting returned by one incrementally streamed process."""

    returncode: int
    started_at: str
    finished_at: str
    elapsed_seconds: float
    time_to_first_stdout_event_seconds: Optional[float]
    time_to_first_stderr_byte_seconds: Optional[float]
    streamed_stdout_bytes: int
    streamed_stderr_bytes: int
    parsed_event_count: int
    truncated_line_count: int
    token_usage: Optional[Dict[str, Any]]
    termination: Optional[Dict[str, Any]]


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def append_progress_event(path: Path, event: str, **details: Any) -> None:
    """Append and flush one timestamped lifecycle event."""
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {"timestamp": _utc_now(), "event": event}
    payload.update(details)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False) + "\n")
        handle.flush()


def analyze_event_stream(data: bytes) -> Tuple[int, int, Optional[Dict[str, Any]]]:
    """Parse complete JSONL records while accounting for an incomplete tail."""
    complete_lines = data.split(b"\n")
    tail = complete_lines.pop()
    parsed_event_count = 0
    usage: Optional[Dict[str, Any]] = None
    for line in complete_lines:
        if not line.strip():
            continue
        try:
            item = json.loads(line.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
        parsed_event_count += 1
        candidate = item.get("usage") if isinstance(item, dict) else None
        if isinstance(candidate, dict):
            usage = candidate
    return parsed_event_count, 1 if tail else 0, usage


def _consume_stdout_lines(
    buffer: bytearray,
) -> Tuple[int, Optional[Dict[str, Any]], bool]:
    """Remove and parse complete lines from a streaming stdout buffer."""
    parsed = 0
    usage: Optional[Dict[str, Any]] = None
    parsed_any = False
    while True:
        newline = buffer.find(b"\n")
        if newline < 0:
            break
        line = bytes(buffer[:newline])
        del buffer[: newline + 1]
        if not line.strip():
            continue
        try:
            item = json.loads(line.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
        parsed += 1
        parsed_any = True
        candidate = item.get("usage") if isinstance(item, dict) else None
        if isinstance(candidate, dict):
            usage = candidate
    return parsed, usage, parsed_any


def run_streaming_process(
    command: List[str],
    *,
    cwd: Path,
    timeout: int,
    env: Dict[str, str],
    attempt_dir: Path,
    terminator: Optional[Callable[[subprocess.Popen[Any]], Dict[str, Any]]] = None,
) -> AttemptExecution:
    """Stream a process's binary output to durable attempt files with bounded memory."""
    attempt_dir.mkdir(parents=True, exist_ok=True)
    events_path = attempt_dir / "events.jsonl"
    stderr_path = attempt_dir / "stderr.log"
    progress_path = attempt_dir / "progress.jsonl"
    events_path.touch()
    stderr_path.touch()
    progress_path.touch()

    started_at = _utc_now()
    started_clock = time.monotonic()
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=False,
        bufsize=0,
        cwd=cwd,
        env=env,
        start_new_session=True,
    )
    append_progress_event(progress_path, "process_started", pid=process.pid)
    assert process.stdout is not None and process.stderr is not None

    selector = selectors.DefaultSelector()
    selector.register(process.stdout, selectors.EVENT_READ, "stdout")
    selector.register(process.stderr, selectors.EVENT_READ, "stderr")
    stdout_buffer = bytearray()
    stdout_bytes = 0
    stderr_bytes = 0
    parsed_event_count = 0
    usage: Optional[Dict[str, Any]] = None
    first_stdout_event: Optional[float] = None
    first_stderr_byte: Optional[float] = None
    termination: Optional[Dict[str, Any]] = None
    timed_out = False
    terminate = terminator or terminate_process_group

    try:
        with events_path.open("ab", buffering=0) as events_handle, stderr_path.open(
            "ab", buffering=0
        ) as stderr_handle:
            while selector.get_map():
                elapsed = time.monotonic() - started_clock
                if not timed_out and process.poll() is None and elapsed >= timeout:
                    timed_out = True
                    append_progress_event(progress_path, "timeout_initiated")
                    append_progress_event(progress_path, "term_sent")
                    termination = terminate(process)
                    if termination.get("escalation_signal") == "SIGKILL":
                        append_progress_event(progress_path, "kill_sent")

                if process.poll() is not None:
                    select_timeout = 0.05
                elif timed_out:
                    select_timeout = 0.05
                else:
                    select_timeout = min(0.05, max(0.0, timeout - elapsed))
                for key, _mask in selector.select(select_timeout):
                    stream = key.fileobj
                    chunk = os.read(stream.fileno(), 65536)
                    if not chunk:
                        selector.unregister(stream)
                        stream.close()
                        continue
                    observed = time.monotonic() - started_clock
                    if key.data == "stdout":
                        events_handle.write(chunk)
                        stdout_bytes += len(chunk)
                        stdout_buffer.extend(chunk)
                        count, candidate_usage, parsed_any = _consume_stdout_lines(stdout_buffer)
                        parsed_event_count += count
                        if candidate_usage is not None:
                            usage = candidate_usage
                        if parsed_any and first_stdout_event is None:
                            first_stdout_event = observed
                            append_progress_event(
                                progress_path,
                                "first_stdout_event",
                                elapsed_seconds=round(observed, 6),
                            )
                    else:
                        stderr_handle.write(chunk)
                        stderr_bytes += len(chunk)
                        if first_stderr_byte is None:
                            first_stderr_byte = observed
                            append_progress_event(
                                progress_path,
                                "first_stderr_byte",
                                elapsed_seconds=round(observed, 6),
                            )
    except BaseException:
        if process.poll() is None:
            append_progress_event(progress_path, "interruption_initiated")
            append_progress_event(progress_path, "term_sent")
            termination = terminate(process)
            if termination.get("escalation_signal") == "SIGKILL":
                append_progress_event(progress_path, "kill_sent")
        raise
    finally:
        selector.close()

    if process.poll() is None:
        process.wait()
    returncode = 124 if timed_out else int(process.returncode)
    finished_at = _utc_now()
    elapsed_seconds = time.monotonic() - started_clock
    append_progress_event(
        progress_path,
        "process_exited",
        process_return_code=process.returncode,
        logical_return_code=returncode,
    )
    return AttemptExecution(
        returncode=returncode,
        started_at=started_at,
        finished_at=finished_at,
        elapsed_seconds=round(elapsed_seconds, 6),
        time_to_first_stdout_event_seconds=(
            round(first_stdout_event, 6) if first_stdout_event is not None else None
        ),
        time_to_first_stderr_byte_seconds=(
            round(first_stderr_byte, 6) if first_stderr_byte is not None else None
        ),
        streamed_stdout_bytes=stdout_bytes,
        streamed_stderr_bytes=stderr_bytes,
        parsed_event_count=parsed_event_count,
        truncated_line_count=1 if stdout_buffer else 0,
        token_usage=usage,
        termination=termination,
    )


def validate_run_id(value: str) -> str:
    """Return a safe caller-provided immutable run ID or raise ValueError."""
    if not isinstance(value, str) or not RUN_ID_RE.fullmatch(value):
        raise ValueError("run_id must use lowercase kebab-case letters and digits")
    return value


def resolve_run_dir(root: Path, job: Dict[str, Any], run_id: str) -> Path:
    """Return the nested diagnostic directory without creating it."""
    return root / str(job["artifact_dir"]) / validate_run_id(run_id)


def raw_output_path(attempt_dir: Path) -> Path:
    return attempt_dir / "model-output.raw.json"


def normalized_output_path(attempt_dir: Path) -> Path:
    return attempt_dir / "model-output.normalized.json"


def output_paths(attempt_dir: Path) -> Tuple[Path, Path]:
    """Return separate immutable raw and deterministic-normalized output paths."""
    return raw_output_path(attempt_dir), normalized_output_path(attempt_dir)


def _lock_key(provider: str, job_id: str) -> str:
    """Return a path-safe, collision-resistant key for one provider job."""
    identity = f"{provider}\0{job_id}"
    label = LOCK_KEY_RE.sub("-", f"{provider}-{job_id}".lower()).strip("-")
    label = label[:80] or "job"
    digest = hashlib.sha256(identity.encode("utf-8")).hexdigest()[:16]
    return f"{label}-{digest}.lock"


@contextlib.contextmanager
def job_lock(common_git_dir: Path, provider: str, job_id: str) -> Iterator[Path]:
    """Hold a non-blocking, kernel-managed lock for a provider job."""
    lock_dir = Path(common_git_dir) / "metronome-model-locks"
    lock_dir.mkdir(parents=True, exist_ok=True)
    lock_path = lock_dir / _lock_key(provider, job_id)
    handle = lock_path.open("a+", encoding="utf-8")
    try:
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise RuntimeError(f"model job already locked: {provider}/{job_id}") from exc
        yield lock_path
    finally:
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        finally:
            handle.close()


def terminate_process_group(
    process: subprocess.Popen[Any], grace_seconds: float = 5.0
) -> Dict[str, Any]:
    """Terminate a session-leading process and every descendant in its group."""
    metadata: Dict[str, Any] = {
        "signal": "SIGTERM",
        "grace_seconds": grace_seconds,
        "grace_outcome": "already_exited",
        "escalation_signal": None,
        "final_return_code": process.poll(),
    }
    if process.poll() is not None:
        return metadata
    try:
        process_group = os.getpgid(process.pid)
    except ProcessLookupError:
        return metadata
    try:
        os.killpg(process_group, signal.SIGTERM)
    except (PermissionError, ProcessLookupError):
        metadata["grace_outcome"] = "already_exited"
    else:
        deadline = time.monotonic() + max(0.0, grace_seconds)
        while True:
            if process.poll() is None:
                try:
                    process.wait(timeout=min(0.05, max(0.0, deadline - time.monotonic())))
                except subprocess.TimeoutExpired:
                    pass
            try:
                os.killpg(process_group, 0)
            except ProcessLookupError:
                metadata["grace_outcome"] = "terminated"
                break
            except PermissionError:
                # Some sandboxes report a dead/reaped group as EPERM. Once the
                # leader is reaped, do not convert that zombie-only state into
                # an inaccurate KILL outcome.
                if process.poll() is not None:
                    metadata["grace_outcome"] = "terminated"
                    break
            if time.monotonic() >= deadline:
                metadata["escalation_signal"] = "SIGKILL"
                try:
                    os.killpg(process_group, signal.SIGKILL)
                except (PermissionError, ProcessLookupError):
                    metadata["grace_outcome"] = "terminated"
                    metadata["escalation_signal"] = None
                else:
                    metadata["grace_outcome"] = "killed"
                break
    if process.poll() is None:
        process.wait()
    metadata["final_return_code"] = process.returncode
    return metadata


def write_json_atomic(path: Path, payload: Dict[str, Any]) -> None:
    """Publish JSON only after its temporary file is flushed and synced."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f"{path.name}.tmp")
    with temporary.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temporary, path)
