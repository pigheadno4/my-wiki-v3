# Metronome Model Worker Diagnostics Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make Metronome model-worker diagnostics immutable, live-observable, process-safe across worktrees, and capable of proving whether Luna is healthy before any further page-level experiment.

**Architecture:** Extend the existing schema-version-3 runner without changing legacy artifact validation. Each new execution receives an immutable run ID, holds a common-Git-directory advisory lock, streams process output and lifecycle events, preserves raw and normalized outputs separately, and publishes a hashed runtime receipt atomically. A separate tiny health-probe command uses the same lifecycle machinery and gates all future enterprise A/B work.

**Tech Stack:** Python 3.9 standard library (`fcntl`, `hashlib`, `selectors`, `signal`, `subprocess`, `os.replace`), `unittest`, JSON/JSONL, Codex CLI, Git worktrees.

## Global Constraints

- Follow `docs/superpowers/specs/2026-07-17-metronome-model-worker-diagnostics-design.md` exactly.
- Follow `CLAUDE.md` and `rules/ingest.md`; diagnostics never change canonical coverage.
- Never modify `raw/metronome/` or any canonical file under `wiki/`.
- Existing timeout evidence and all legacy version-2/version-3 artifacts remain byte-for-byte unchanged.
- New executions require an immutable caller-supplied `run_id`; existing run directories fail before Codex launch.
- Lock ownership must be shared across linked worktrees through the repository common Git directory.
- Raw model output is immutable; normalized output is a separate file.
- Terminal receipts are visible only after fsync and atomic rename.
- On timeout or interruption, terminate the entire Codex process group with TERM, five-second grace, then KILL if required.
- Do not run enterprise A/B or resume cycles 3-5 in this plan.
- Run only the 60-second Luna/high health probe after deterministic verification passes.

---

### Task 1: Immutable Run Layout and Atomic Artifacts

**Files:**
- Create: `scripts/metronome_model_runtime.py`
- Modify: `scripts/run_metronome_model_worker.py`
- Modify: `tests/test_run_metronome_model_worker.py`
- Modify: `scripts/metronome_ingest_pilot.py`
- Modify: `tests/test_metronome_ingest_pilot.py`

**Interfaces:**
- Produces in `metronome_model_runtime.py`: `validate_run_id(value: str)`, `resolve_run_dir(root, job, run_id)`, `write_json_atomic(path, payload)`, and separate raw/normalized output paths.
- Preserves: existing `run_worker(root, job_path, ingest_date, runner=...)` compatibility for deterministic legacy tests; live diagnostic CLI execution requires `--run-id`.

- [x] Add failing tests that reject missing/invalid run IDs in diagnostic mode, reject an existing run directory before invoking the runner, and leave legacy artifact paths untouched.
- [x] Add a failing test proving deterministic repair never changes `model-output.raw.json` and writes repaired content only to `model-output.normalized.json`.
- [x] Add a failing test that observes a `.tmp` receipt before publication and only the final receipt after `os.replace`.
- [x] Run `python3 -m unittest tests.test_run_metronome_model_worker tests.test_metronome_ingest_pilot -v`; verify failures are caused by the missing immutable-run APIs.
- [x] Implement the minimal immutable layout and atomic JSON writer using flush, `os.fsync`, and `os.replace`.
- [x] Run focused tests and commit `feat: add immutable diagnostic runs`.

### Task 2: Cross-worktree Lock and Process-group Cleanup

**Files:**
- Modify: `scripts/metronome_model_runtime.py`
- Modify: `scripts/run_metronome_model_worker.py`
- Modify: `tests/test_run_metronome_model_worker.py`

**Interfaces:**
- Produces: `job_lock(common_git_dir, provider, job_id)` and `terminate_process_group(process, grace_seconds=5.0)`.
- Consumes: immutable run directory from Task 1.

- [x] Add a failing test using two different worktree roots that proves the same job lock is rejected while held and an unrelated job lock succeeds.
- [x] Add a failing test proving kernel lock release after normal close without deleting the lock file.
- [x] Add a failing child-process test proving timeout sends TERM to the process group, escalates to KILL when needed, and leaves no descendant alive.
- [x] Run the focused tests and confirm they fail because locking/process-group lifecycle is absent.
- [x] Implement non-blocking `fcntl.flock`, safe lock-key normalization, `start_new_session=True`, TERM/grace/KILL cleanup, and termination metadata.
- [x] Run focused tests and commit `feat: make model workers process safe`.

### Task 3: Live Streaming and Runtime Metadata

**Files:**
- Modify: `scripts/metronome_model_runtime.py`
- Modify: `scripts/run_metronome_model_worker.py`
- Modify: `tests/test_run_metronome_model_worker.py`

**Interfaces:**
- Produces: a Popen-based attempt executor returning return code, timing, byte/event counts, truncation counts, token usage, and termination outcome.
- Writes: `events.jsonl`, `stderr.log`, and `progress.jsonl` incrementally.

- [x] Add a failing test that sees stdout, stderr, and progress files before a fake process exits.
- [x] Add failing tests for time-to-first-event, streamed bytes, parsed-event count, and truncated-last-line accounting.
- [x] Add failing tests for SHA-256 metadata covering raw text, prompt template, rendered prompt, schema, and Codex executable plus CLI version and timeout.
- [x] Run focused tests and confirm the streaming/metadata assertions fail.
- [x] Implement selector-based binary streaming and timestamped progress events without buffering the whole process output.
- [x] Preserve incomplete final JSONL bytes; parsers skip but count the truncated line.
- [x] Run focused tests and commit `feat: stream model worker diagnostics`.

### Task 4: Equivalent Input Modes

**Files:**
- Modify: `scripts/run_metronome_model_worker.py`
- Modify: `tests/test_run_metronome_model_worker.py`
- Modify: `tracking/ingest/metronome/pilot/prompts/source-summary-v3.md`

**Interfaces:**
- Produces: `render_worker_prompt(..., input_mode)` supporting `staged-file` and `inline-stdin`.
- Requires: inline raw content passed through stdin between fixed untrusted-data delimiters, never as a command argument.

- [x] Add failing tests that reject unknown input modes and prove both supported modes contain identical job identity, schema expectations, page profile, concept inventory, and extraction requirements.
- [x] Add a failing test proving inline raw text is absent from the command arguments and present only in stdin-delivered prompt content.
- [x] Add a failing test proving staged-file mode still creates and references `raw.md`.
- [x] Run focused tests and confirm failures are due to the absent input-mode interface.
- [x] Implement the two modes and their hashes without changing accepted output semantics.
- [x] Run focused tests and commit `feat: add diagnostic input modes`.

### Task 5: Health Probe and Gate

**Files:**
- Create: `scripts/run_metronome_model_health_probe.py`
- Create: `tests/test_run_metronome_model_health_probe.py`
- Create: `tracking/ingest/metronome/pilot/schemas/model-health-probe.schema.json`
- Create: `tracking/ingest/metronome/pilot/prompts/model-health-probe.md`
- Modify: `tracking/ingest/metronome/pilot/luna-expansion-manifest.md`

**Interfaces:**
- Consumes: immutable run lifecycle, lock, streaming, atomic receipt, hashes, and process cleanup from Tasks 1-4.
- Produces: a diagnostic receipt with `status`, first-event latency, elapsed time, terminal JSON validity, runtime metadata completeness, and process cleanup result.

- [x] Add failing tests for the 60-second total cap, 30-second first-event gate, valid tiny JSON, complete metadata, atomic receipt, and no surviving process.
- [x] Add a failing orchestration test proving a failed health probe prevents enterprise A/B launch.
- [x] Run health-probe tests and confirm the command/gate is missing.
- [x] Implement the tiny Luna/high probe and document that enterprise A/B remains suspended unless the probe passes.
- [x] Run health-probe tests, all worker tests, full unit discovery, compilation, `git diff --check`, and capsule validation.
- [x] Commit `feat: add luna health probe gate`.

### Task 6: Live Health Probe Evidence

**Files:**
- Create: one immutable health-probe run under `tracking/ingest/metronome/pilot/diagnostics/health-probes/`
- Create: `tracking/ingest/metronome/pilot/diagnostics/health-probe-decision.md`

- [x] Run exactly one Luna/high health probe with a unique 2026-07-18 run ID and the fixed 60-second cap.
- [x] Validate its terminal receipt, hashes, event stream, progress lifecycle, and process cleanup.
- [x] Record PASS only if first event is within 30 seconds and valid terminal JSON arrives within 60 seconds; otherwise record FAIL and keep enterprise A/B suspended.
- [x] Commit the immutable probe evidence and decision.
- [x] Generate a whole-task diff package and dispatch a GPT-5.6 Sol ultra-effort reviewer with a default-decline mandate.
- [x] Do not run enterprise A/B unless that reviewer returns APPROVE or CONDITIONAL APPROVAL with no Critical or Important finding.

### Final Review Remediation

The first whole-task Sol review returned `DECLINE`. All Critical and Important findings
were treated as blockers; the failed live probe remained immutable and enterprise A/B
remained suspended throughout remediation.

- [x] Enforce resolved containment and reject traversal, symlink, hardlink, and temporary-file receipt escapes (`36764c5`).
- [x] Require and reconcile complete diagnostic receipt evidence (`36764c5`).
- [x] Clean the captured process group after interruption even when its leader already exited (`5815e24`, `d4a843e`).
- [x] Gate the actual enterprise worker API and CLI through an explicit immutable job registry and strict passing-probe verification (`e924ee0`).
- [x] Publish atomic failed worker receipts for all post-claim failures and preserve interrupt propagation (`e924ee0`).
- [x] Snapshot prospective prompt/schema inputs and record runner/Git provenance plus terminal artifact manifests without rewriting historical evidence (`e924ee0`).
- [ ] Obtain a fresh GPT-5.6 Sol ultra-effort default-decline verdict over the remediated branch.
