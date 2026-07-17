# Diagnostic Task 1 Report: Immutable Run Layout and Atomic Artifacts

## Scope

Implemented only Diagnostic Task 1 from the approved diagnostics plan. No
cross-worktree locking, process-group cleanup, live streaming, input modes, or
health-probe code was added. No canonical coverage workflow was run.

## RED evidence

After adding the Task 1 tests, this command was run:

```text
python3 -m unittest tests.test_run_metronome_model_worker tests.test_metronome_ingest_pilot -v
```

It failed as expected before implementation:

- `ModuleNotFoundError: No module named 'metronome_model_runtime'` for the new
  immutable-run API tests.
- `test_diagnostic_worker_receipt_requires_distinct_raw_and_normalized_outputs`
  failed because receipt validation did not yet reject identical raw and
  normalized output paths.

The remaining existing pilot tests passed in that RED run.

## Implementation

- Added `scripts/metronome_model_runtime.py` with lower-case kebab-case run-ID
  validation, nested run-directory resolution, named raw/normalized output
  paths, and an atomic JSON writer using flush, `os.fsync`, and `os.replace`.
- Extended `run_worker(..., runner=...)` with an optional `run_id` while
  preserving the existing no-run-ID legacy path. Diagnostic runs reject an
  already-existing directory before the injected runner/Codex is invoked.
- Diagnostic attempts write Codex output only to
  `model-output.raw.json`; repairs operate on a copied in-memory object and
  write `model-output.normalized.json`. The accepted run-level output is copied
  from the normalized file.
- Diagnostic terminal receipts are atomically published. Legacy receipts remain
  on their prior direct job-artifact path and retain the legacy writer.
- Added receipt validation that requires distinct raw and normalized attempt
  paths for diagnostic receipts.

## GREEN evidence

Focused suite and compilation:

```text
PYTHONPYCACHEPREFIX=/tmp/wiki-v2-pycache python3 -m unittest \
  tests.test_run_metronome_model_worker tests.test_metronome_ingest_pilot -v
PYTHONPYCACHEPREFIX=/tmp/wiki-v2-pycache python3 -m py_compile \
  scripts/metronome_model_runtime.py \
  scripts/run_metronome_model_worker.py \
  scripts/metronome_ingest_pilot.py
```

Result: 37 tests passed; compilation succeeded. The redirected bytecode cache
is necessary in this sandbox because the default macOS cache directory is not
writable.

Full suite:

```text
PYTHONPYCACHEPREFIX=/tmp/wiki-v2-pycache python3 -m unittest discover -s tests -v
```

Result: 67 tests passed.

CLI guard:

```text
python3 scripts/run_metronome_model_worker.py --job missing --ingest-date 2026-07-17
```

Result: exits 2 and reports `--run-id is required for live diagnostic
execution` before worker launch.

## Files changed

- `scripts/metronome_model_runtime.py` (new)
- `scripts/run_metronome_model_worker.py`
- `scripts/metronome_ingest_pilot.py`
- `tests/test_run_metronome_model_worker.py`
- `tests/test_metronome_ingest_pilot.py`

## Self-review

- Legacy `run_worker(root, job_path, ingest_date, runner=...)` remains valid
  and is explicitly covered by a direct-job-artifact test.
- A pre-existing diagnostic run directory returns before `runner` invocation.
- Raw model-output bytes are never rewritten after Codex produces them;
  normalization writes a separate file.
- Receipt publication test observes `model-worker-receipt.json.tmp` before
  replacement and only the final filename after it.
- `git diff --name-only -- raw/metronome wiki` produced no paths, confirming
  this task did not alter raw evidence or canonical wiki content.

## Concerns

None for Task 1. Later-task facilities (locking, Popen streaming, input modes,
and health probing) are intentionally absent and must remain separate changes.
