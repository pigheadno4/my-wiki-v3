# Diagnostic Task 3 Report: Live Streaming and Runtime Metadata

## Scope

Implemented only Diagnostic Task 3. Live worker attempts now stream binary
stdout and stderr incrementally, publish lifecycle progress, account for event
timing and truncation, and attach hashed runtime metadata to immutable
diagnostic receipts. No input-mode interface, health probe, live diagnostic
run, raw evidence, historical artifact, or canonical wiki change was added.

## RED evidence

After adding the Task 3 tests, this focused command failed before production
implementation:

```text
PYTHONPYCACHEPREFIX=/tmp/wiki-v2-pycache python3 -m unittest \
  tests.test_run_metronome_model_worker -v
```

The failure was the expected import error:
`cannot import name 'build_runtime_metadata' from
'run_metronome_model_worker'`. The new tests define and exercise the absent
streaming and metadata interfaces, including a real fake process held open
while its attempt files are inspected and an incomplete final JSONL record.

## Implementation

- Added a selector-based, binary `Popen` executor that writes
  `events.jsonl` and `stderr.log` as bytes arrive and appends flushed,
  timestamped events to `progress.jsonl`.
- Added lifecycle events for process start, first parsed stdout event, first
  stderr byte, timeout/TERM/KILL when applicable, process exit, validation
  completion, and atomic receipt publication. Diagnostic attempts also record
  the already-held job lock.
- Added bounded attempt accounting for elapsed and first-event timing, stdout
  and stderr bytes, complete parsed JSON events, one preserved truncated final
  line, token usage, logical return code, and process-group termination.
- Preserved the incomplete final JSONL bytes exactly in `events.jsonl`; only
  complete lines are parsed for events and usage.
- Added SHA-256 metadata for the exact raw bytes, prompt-template bytes,
  rendered prompt UTF-8 bytes, schema bytes, and resolved Codex executable,
  plus the resolved executable path, CLI version, and configured timeout.
  Every diagnostic attempt and terminal receipt carries this metadata.
- Kept injected deterministic runners compatible by adapting their completed
  output into the same accounting shape. Live timeout cleanup still uses the
  Task 2 process-group TERM/grace/KILL implementation.

## GREEN evidence

Focused worker and receipt-compatibility suite:

```text
PYTHONPYCACHEPREFIX=/tmp/wiki-v2-pycache python3 -m unittest \
  tests.test_run_metronome_model_worker tests.test_metronome_ingest_pilot -v
```

Result: 51 tests passed.

Full suite:

```text
PYTHONPYCACHEPREFIX=/tmp/wiki-v2-pycache python3 -m unittest discover -s tests -v
```

Result: 81 tests passed.

Compilation and diff checks:

```text
PYTHONPYCACHEPREFIX=/tmp/wiki-v2-pycache python3 -m py_compile \
  scripts/metronome_model_runtime.py scripts/run_metronome_model_worker.py
git diff --check
git diff --name-only -- raw/metronome wiki \
  tracking/ingest/metronome/pilot/runs \
  tracking/ingest/metronome/pilot/diagnostics
```

Result: compilation and diff checks passed; the protected path check produced
no paths.

## Files changed

- `scripts/metronome_model_runtime.py`
- `scripts/run_metronome_model_worker.py`
- `tests/test_run_metronome_model_worker.py`
- `.superpowers/sdd/diag-task-3-report.md`

## Concerns

None for Task 3. Runtime metadata intentionally describes the existing fixed
staged-file behavior without adding the Task 4 input-mode interface. The Task
5 health probe and any live Codex diagnostic execution remain unimplemented.
