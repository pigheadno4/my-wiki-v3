# Metronome Model Worker Diagnostics Design

## Decision

Do not treat the ASC 606 and enterprise-commit timeouts as evidence that staged-file input is slow. Both attempts produced only `thread.started` and `turn.started`; enterprise stderr also recorded model-manager refresh timeouts. The approved next step is an evidence-safe runtime diagnostic, not another ingest attempt.

Medium and long Metronome pages remain routed directly to Sol. Luna remains eligible only for short pages until the diagnostic succeeds on enterprise-commit and a second medium page.

## Goals

- Preserve every historical run byte-for-byte.
- Make future attempts immutable, observable while running, and safe across worktrees.
- Distinguish service/model initialization failures from input-delivery and document-processing costs.
- Compare staged-file and inline-stdin delivery without changing model, reasoning, schema, prompt semantics, or timeout.
- Prevent health probes and comparison runs from changing canonical wiki coverage.

## Non-goals

- Do not resume cycles 3-5.
- Do not create or update source, concept, company, index, or log pages.
- Do not increase timeouts or lower Luna reasoning effort.
- Do not infer model quality from a run that produces no validated structured output.
- Do not replace Sol as canonical reviewer or promoter.

## Run Identity and Storage

Each execution requires a caller-supplied `run_id` matching lowercase kebab-case plus digits. Artifacts live under:

```text
tracking/ingest/metronome/pilot/runs/<job-id>/<run-id>/
```

The runner must fail before launching Codex if that directory already exists. Existing legacy artifacts directly beneath `<job-id>/` remain untouched and readable.

Each attempt directory contains:

```text
attempt-1/
  events.jsonl
  stderr.log
  progress.jsonl
  model-output.raw.json
  model-output.normalized.json
```

`model-output.raw.json` is the exact output written by Codex. Deterministic repair operates on an in-memory copy and writes `model-output.normalized.json`; it never overwrites the raw output. Accepted run-level output is copied from the normalized artifact.

## Cross-worktree Lock

The runner uses an OS-managed advisory `fcntl.flock` on a lock file in the repository common Git directory, keyed by provider and job ID. Because all linked worktrees share the common Git directory, the lock prevents the same job from running concurrently across worktrees.

The lock is non-blocking. A duplicate launch fails before creating its run directory. The kernel releases the lock when the process exits or crashes, so no PID-based stale-lock recovery is needed. The lock file may remain on disk; lock ownership, not file presence, is authoritative.

## Process Lifecycle

Codex launches in a new process group. On timeout or coordinator interruption:

1. Send `SIGTERM` to the process group.
2. Wait up to five seconds.
3. Send `SIGKILL` to the process group if it remains alive.
4. Record termination signal, grace outcome, and final return code.

Tests must prove no descendant process remains after the timeout path.

## Live Observability

The runner uses `subprocess.Popen` rather than buffered `subprocess.run`.

- stdout is appended to `events.jsonl` as bytes arrive.
- stderr is appended to `stderr.log` as bytes arrive.
- `progress.jsonl` records timestamped lifecycle events: lock acquired, process started, first stdout event, first stderr byte, timeout initiated, TERM sent, KILL sent when needed, process exited, validation completed, and receipt published.
- A truncated final JSONL line after a crash remains preserved. Parsers skip the incomplete line and record its existence in the receipt.

## Atomic Receipts

The terminal receipt is written to `model-worker-receipt.json.tmp`, flushed and `fsync`ed, then atomically renamed to `model-worker-receipt.json`. Only the renamed file is terminal. A leftover `.tmp` file means the run was interrupted before terminal publication and must not be accepted.

## Runtime Metadata

Every attempt and terminal receipt records:

- `run_id`
- `input_mode`: `staged-file` or `inline-stdin`
- attempt elapsed seconds
- time to first stdout event and first stderr byte
- streamed stdout bytes, stderr bytes, parsed event count, and truncated-line count
- SHA-256 of raw text, prompt template, rendered prompt, output schema, and Codex executable
- Codex CLI version
- model and reasoning effort
- timeout seconds
- process-group termination outcome
- raw and normalized output paths
- per-attempt and cumulative token usage when emitted

## Input Modes

### Staged file

The existing `raw.md` delivery remains supported. The prompt tells the worker to read `raw.md` completely.

### Inline stdin

The rendered prompt contains the complete raw text between explicit untrusted-data delimiters. The raw text is passed through stdin to Codex, never as a command-line argument. Instructions state that content inside the delimiters is evidence only and cannot override the worker instructions.

Both modes use the same schema, identity fields, page profile, concept inventory, and substantive extraction requirements.

## Diagnostic Sequence

### Phase 1: Health probe

Run Luna/high with a tiny fixed prompt and tiny output schema, no documentation page, and a 60-second timeout. It writes only to a diagnostic run directory and never participates in coverage.

Pass criteria:

- first model event within 30 seconds;
- valid terminal JSON within 60 seconds;
- terminal receipt published atomically;
- complete runtime metadata;
- no surviving child process.

If the probe fails, stop. Do not run enterprise A/B.

### Phase 2: Enterprise A/B

Only after a passing health probe, run two new immutable enterprise-commit diagnostics sequentially:

1. staged-file;
2. inline-stdin.

Both use Luna/high, identical semantic prompt and schema, and a 300-second timeout. Neither may edit canonical wiki files.

Pass criteria for inline mode:

- output validates with exact grounding quotes and no unsupported claims;
- no critical omission in Sol review;
- complete token and runtime accounting;
- at least 25% faster elapsed time or 25% lower cumulative input tokens than staged-file mode.

The comparison is inconclusive if service health changes materially between the paired runs, either run lacks accounting data, or only one mode reaches model execution.

### Phase 3: Routing decision

- Health-probe failure: use Luna only for short pages; route medium/long pages to Sol.
- Healthy probe but failed/inconclusive A/B: same routing; retain diagnostic evidence.
- Successful A/B: repeat inline mode on ASC 606 or another medium page.
- Two successful medium-page inline runs: consider resuming cycles 3-5 one source at a time.

## Testing

Test-first coverage must prove:

- an existing `run_id` cannot be overwritten;
- the same job cannot run concurrently from separate worktree paths;
- an unrelated job can run concurrently;
- stdout/stderr and progress are visible before process completion;
- terminal receipt publication is atomic;
- raw output remains unchanged after normalization;
- truncated event lines are preserved and accounted for;
- TERM then KILL cleans up the process group;
- both input modes preserve equivalent semantic instructions and hashes;
- health-probe failure prevents enterprise A/B execution;
- legacy version-2 and version-3 artifacts continue to validate.

## Review Gate

After implementation and deterministic tests, run only the health probe. A high-effort Sol reviewer with a default-decline posture reviews the implementation diff, test evidence, and health-probe artifacts. Enterprise A/B requires that reviewer to return APPROVE or CONDITIONAL APPROVAL with no Critical or Important implementation finding.
