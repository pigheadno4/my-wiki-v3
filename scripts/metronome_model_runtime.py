"""Immutable artifact helpers for Metronome model-worker diagnostics."""
from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any, Dict, Tuple


RUN_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


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
