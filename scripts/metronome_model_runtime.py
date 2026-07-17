"""Immutable artifact helpers for Metronome model-worker diagnostics."""
from __future__ import annotations

import contextlib
import fcntl
import hashlib
import json
import os
import re
import signal
import subprocess
import time
from pathlib import Path
from typing import Any, Dict, Iterator, Tuple


RUN_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LOCK_KEY_RE = re.compile(r"[^a-z0-9]+")


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
