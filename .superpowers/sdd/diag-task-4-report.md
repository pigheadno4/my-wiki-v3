# Diagnostic Task 4 Report — Equivalent Input Modes

## Scope completed

- Added `staged-file` and `inline-stdin` worker input modes.
- Kept the job identity, deterministic page profile (including concept inventory), schema instructions, and extraction requirements in one shared prompt prefix.
- Kept staged delivery backward-compatible: the isolated worker directory contains `raw.md`, and the command receives the rendered prompt as its final argument.
- Added inline delivery through `codex exec -`: the complete rendered prompt, including the raw evidence between `<<<UNTRUSTED_RAW_EVIDENCE_START>>>` and `<<<UNTRUSTED_RAW_EVIDENCE_END>>>`, is delivered on stdin. The raw text is not placed in command arguments.
- Recorded `input_mode` in each attempt and terminal receipt. Existing runtime metadata continues to hash the raw bytes, prompt template, rendered prompt, output schema, and Codex executable; rendering occurs before the same metadata path for both modes.
- Extended the streaming executor with selector-driven stdin writing so inline input preserves existing stdout/stderr streaming and process-group lifecycle behavior.

## Test-first evidence

The new focused tests were added before the implementation. Their first run failed at import with:

```text
ImportError: cannot import name 'INLINE_RAW_END_DELIMITER' from 'run_metronome_model_worker'
```

That was the expected missing-input-mode interface. After implementation, the focused worker suite passed: 34 tests, 0 failures.

## Constraints observed

- No health probe or live model call was run.
- No canonical file below `raw/` or `wiki/` was changed.
- Historical artifacts were not modified.

## Follow-up concern

The health-probe gate and any enterprise A/B execution remain explicitly out of scope for this task.

## Fix Review — Inline Delimiter Collisions

Review identified that a raw page containing either fixed inline delimiter could forge an apparent evidence boundary. Inline rendering now rejects either `<<<UNTRUSTED_RAW_EVIDENCE_START>>>` or `<<<UNTRUSTED_RAW_EVIDENCE_END>>>` before diagnostic run-directory creation and before a runner/Codex launch. The renderer applies the same validation for direct callers. Staged-file delivery is unchanged.

Two test-first cases, one for each delimiter, initially failed because the injected runner was reached. They now pass while proving that the runner receives no call and the requested diagnostic run directory does not exist. The deterministic rejection is: `inline-stdin raw evidence contains a reserved delimiter`.
