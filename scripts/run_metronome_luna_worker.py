#!/usr/bin/env python3
"""Run one structured GPT-5.6 Luna Metronome draft job with one retry."""
from __future__ import annotations

import argparse
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

from metronome_ingest_pilot import (
    LUNA_MODEL,
    LUNA_REASONING_EFFORT,
    load_json,
    render_luna_draft,
    validate_job,
    validate_luna_output,
)


ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = Path("tracking/ingest/metronome/pilot/schemas/luna-output.schema.json")
PROMPT_PATH = Path("tracking/ingest/metronome/pilot/prompts/source-summary-benchmark.md")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def build_prompt(
    template: str,
    job: Dict[str, Any],
    validation_errors: Optional[List[str]] = None,
) -> str:
    assignment = (
        "\n\n## Assigned job\n\n"
        f"- job_id: `{job['job_id']}`\n"
        f"- raw_path: `{job['raw_path']}`\n"
        f"- canonical_url: `{job['canonical_url']}`\n"
        "\nRead the complete assigned raw file directly from the repository before responding."
    )
    if validation_errors:
        errors = "\n".join(f"- {error}" for error in validation_errors)
        assignment += f"\n\n## Deterministic validation errors from the prior attempt\n\n{errors}"
    return template.rstrip() + assignment + "\n"


def build_codex_command(
    root: Path, schema_path: Path, output_path: Path, prompt: str
) -> List[str]:
    return [
        "codex",
        "-a",
        "never",
        "exec",
        "-m",
        LUNA_MODEL,
        "-c",
        f'model_reasoning_effort="{LUNA_REASONING_EFFORT}"',
        "-s",
        "read-only",
        "--ephemeral",
        "--output-schema",
        str(schema_path),
        "--json",
        "-o",
        str(output_path),
        "-C",
        str(root),
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


def _write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


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

    artifact_dir = root / str(job["artifact_dir"])
    artifact_dir.mkdir(parents=True, exist_ok=True)
    template = (root / PROMPT_PATH).read_text(encoding="utf-8")
    schema_path = root / SCHEMA_PATH
    started_at = utc_now()
    started_clock = time.monotonic()
    validation_errors: Optional[List[str]] = None
    last_result: Any = None
    last_output: Optional[Dict[str, Any]] = None
    last_attempt_dir: Optional[Path] = None
    combined_usage: Optional[Dict[str, Any]] = None

    for attempt in (1, 2):
        attempt_dir = artifact_dir / f"attempt-{attempt}"
        attempt_dir.mkdir(parents=True, exist_ok=True)
        output_path = attempt_dir / "output.json"
        prompt = build_prompt(template, job, validation_errors)
        command = build_codex_command(root, schema_path, output_path, prompt)
        result = runner(command, capture_output=True, text=True, cwd=root)
        last_result = result
        last_attempt_dir = attempt_dir
        (attempt_dir / "events.jsonl").write_text(result.stdout or "", encoding="utf-8")
        (attempt_dir / "stderr.log").write_text(result.stderr or "", encoding="utf-8")
        usage = extract_token_usage(result.stdout or "")
        if usage is not None:
            combined_usage = usage

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
                    errors.append("Luna output must be one JSON object")
                else:
                    output = loaded
                    errors.extend(validate_luna_output(root, job, output))
            except json.JSONDecodeError as exc:
                errors.append(f"Luna output is invalid JSON: {exc.msg}")

        if not errors and output is not None:
            last_output = output
            accepted_output = artifact_dir / "luna-output.json"
            draft_path = artifact_dir / "luna-source-draft.md"
            _write_json(accepted_output, output)
            draft_path.write_text(
                render_luna_draft(job, output, ingest_date), encoding="utf-8"
            )
            finished_at = utc_now()
            receipt = {
                "schema_version": 2,
                "job_id": job["job_id"],
                "provider": job["provider"],
                "canonical_url": job["canonical_url"],
                "raw_path": job["raw_path"],
                "source_page": job["source_page"],
                "status": "success",
                "model_provider": "openai",
                "model": LUNA_MODEL,
                "reasoning_effort": LUNA_REASONING_EFFORT,
                "attempt_count": attempt,
                "started_at": started_at,
                "finished_at": finished_at,
                "elapsed_seconds": round(time.monotonic() - started_clock, 3),
                "process_exit_code": result.returncode,
                "output_path": accepted_output.relative_to(root).as_posix(),
                "draft_path": draft_path.relative_to(root).as_posix(),
                "events_path": (attempt_dir / "events.jsonl").relative_to(root).as_posix(),
                "stderr_path": (attempt_dir / "stderr.log").relative_to(root).as_posix(),
                "grounding_quotes": output["grounding_quotes"],
                "validation": [{"command": "validate_luna_output", "passed": True}],
                "token_usage": combined_usage,
                "token_usage_unavailable_reason": (
                    None if combined_usage is not None else "Codex event stream omitted usage."
                ),
            }
            _write_json(artifact_dir / "luna-worker-receipt.json", receipt)
            return 0
        validation_errors = errors

    finished_at = utc_now()
    assert last_result is not None and last_attempt_dir is not None
    failed_receipt = {
        "schema_version": 2,
        "job_id": job["job_id"],
        "provider": job["provider"],
        "canonical_url": job["canonical_url"],
        "raw_path": job["raw_path"],
        "source_page": job["source_page"],
        "status": "failed",
        "model_provider": "openai",
        "model": LUNA_MODEL,
        "reasoning_effort": LUNA_REASONING_EFFORT,
        "attempt_count": 2,
        "started_at": started_at,
        "finished_at": finished_at,
        "elapsed_seconds": round(time.monotonic() - started_clock, 3),
        "process_exit_code": last_result.returncode,
        "output_path": (last_attempt_dir / "output.json").relative_to(root).as_posix(),
        "draft_path": None,
        "events_path": (last_attempt_dir / "events.jsonl").relative_to(root).as_posix(),
        "stderr_path": (last_attempt_dir / "stderr.log").relative_to(root).as_posix(),
        "grounding_quotes": (
            last_output.get("grounding_quotes", []) if last_output is not None else []
        ),
        "validation": [
            {
                "command": "validate_luna_output",
                "passed": False,
                "errors": validation_errors or ["unknown Luna worker failure"],
            }
        ],
        "token_usage": combined_usage,
        "token_usage_unavailable_reason": (
            None if combined_usage is not None else "Codex event stream omitted usage."
        ),
    }
    _write_json(artifact_dir / "luna-worker-receipt.json", failed_receipt)
    return 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--job", required=True)
    parser.add_argument("--ingest-date", required=True)
    args = parser.parse_args()
    return run_worker(ROOT, Path(args.job), args.ingest_date)


if __name__ == "__main__":
    raise SystemExit(main())
