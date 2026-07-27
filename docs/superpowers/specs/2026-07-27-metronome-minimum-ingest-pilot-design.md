# Metronome Minimum Parallel Ingest Pilot Design

**Date:** 2026-07-27  
**Status:** Approved design, awaiting written-spec review  
**Scope:** Five-page Metronome dry-run followed by an explicitly approved serial promotion

## Purpose

Build the smallest platform-neutral coordinator that can generate five source-page candidates in parallel, review them serially with Sol, preserve a filesystem audit trail, and promote one complete source cycle at a time.

This design replaces the unmerged safety-first coordinator experiment. That experiment remains frozen as a reference, but none of its coordinator, recovery, journal-proof, or operation-receipt implementation will be cherry-picked.

## Pilot Trust Model

The campaign filesystem is local, trusted, and coordinator-owned.

- Terra and Sol workers never write repository files.
- The coordinator is the only writer of campaign tracking, attempt evidence, canonical wiki pages, and Git commits.
- The pilot detects missing, malformed, unreadable, or internally inconsistent coordinator files.
- The pilot does not defend against a person deliberately rewriting coordinator-owned files into a different but schema-valid history.
- Raw files remain immutable and are verified by SHA-256 before and after processing.

## YAGNI Constraints

The pilot must not introduce:

- automatic crash reconciliation;
- exact replay of partially completed operations;
- cross-file transactions;
- operation receipts or generation binding;
- hostile-journal validation;
- automatic rollback;
- concurrent canonical promotion;
- a pluggable backend framework;
- per-worker Git worktrees;
- recovery behavior for a failure that has not occurred in a real pilot.

One occurrence of an unusual failure is recorded and handled manually. Automation is considered only when the same failure recurs in separate pilots or campaigns.

## Architecture

The implementation has four responsibilities and one thin CLI:

```text
scripts/
├── manage_ingest_pilot.py
└── ingest_pilot/
    ├── coordinator.py
    ├── state.py
    ├── scheduler.py
    └── validator.py
```

- `scheduler.py` selects queued jobs until `worker_concurrency` is filled.
- `coordinator.py` dispatches workers, persists returned candidates, invokes Sol serially, and owns canonical promotion.
- `state.py` atomically replaces the current job projection and appends audit events.
- `validator.py` checks worker output, candidate structure, grounding quotes, raw links, and raw hashes.
- `manage_ingest_pilot.py` exposes only `init`, `run`, `status`, `retry`, `reject`, and `resume`.

No implementation file may import code from the frozen safety-first branch. Small standalone behavior may be reimplemented after reviewing its contract, but the new pilot remains independent of the old coordinator architecture.

## Worker Contract

Workers are pure readers and return structured data to the coordinator. They do not receive repository write authority.

### Terra input

```json
{
  "campaign_id": "metronome-five-page-pilot",
  "job_id": "job-001",
  "attempt": 1,
  "raw_path": "raw/metronome/example/page-2026-07-19.md",
  "raw_sha256": "<sha256>",
  "source_target": "wiki/sources/metronome/source-example-page.md"
}
```

Terra must read the complete raw file and return one source-page candidate.

### Terra output

```json
{
  "source_page": "<complete Markdown candidate>",
  "quotes": [
    {
      "text": "<verbatim quote>",
      "location": "<raw heading or line location>"
    }
  ],
  "suggestions": {
    "company": [],
    "concepts": [],
    "index": [],
    "log": []
  },
  "raw_path": "raw/metronome/example/page-2026-07-19.md",
  "raw_sha256": "<sha256>",
  "status": "candidate_ready"
}
```

The output must include three to five verbatim quotes, the canonical raw link, the original raw hash, a complete source-page candidate, and structured suggestions for shared pages.

### Sol contract

Sol reads:

- the complete raw file;
- the Terra candidate;
- the grounding quotes;
- the relevant current source, company, concept, index, and log pages.

Sol returns exactly one verdict:

- `approved`;
- `changes_requested`, with specific corrections;
- `rejected`, with a terminal reason.

Sol does not write files. Sol review concurrency and canonical promotion concurrency are both exactly one.

## Filesystem Model

```text
tracking/ingest/metronome/<campaign-id>/
├── campaign.json
├── jobs.json
├── events.jsonl
├── monitor.md
└── attempts/
    └── <job-id>/
        └── attempt-N/
            ├── input.json
            ├── candidate.md
            ├── receipt.json
            ├── suggestions.json
            └── failure.json
```

- `campaign.json` is immutable campaign configuration, including the provider, five job IDs, and `worker_concurrency`.
- `jobs.json` is the sole current-state authority and is replaced atomically.
- `events.jsonl` is append-only audit history. It is not replayed to reconstruct state.
- `monitor.md` is regenerated from `jobs.json` and is never treated as authoritative.
- Each attempt directory is written only by the coordinator. Existing attempt evidence is never deleted or overwritten.
- Successful attempts contain `candidate.md`, `receipt.json`, and `suggestions.json`.
- Failed attempts contain `failure.json`; partial evidence is retained.

If `jobs.json` is updated but appending `events.jsonl` fails, `jobs.json` remains authoritative and the current command reports a warning. The pilot does not implement a transaction or later reconciliation for those two writes.

## Job and Campaign States

Each job has exactly one of these states:

```text
queued
running
candidate_ready
reviewing
approved
promoting
completed
failed
rejected
```

The campaign has exactly one of:

```text
active
paused
completed
```

Normal execution is:

```text
queued
→ running
→ candidate_ready
→ reviewing
→ approved
→ promoting
→ completed
```

`changes_requested` creates the next attempt and places the job at the queue tail. A job has at most three total attempts.

## Rolling Parallelism and Serial Ingest

The scheduler fills up to five Terra slots. When one worker returns, its result is persisted and the newly free slot is immediately offered to the next queued job.

Candidate generation may be parallel, but canonical ingest remains serial:

1. Sol reviews one complete raw source and its candidate.
2. If approved, the coordinator applies that source's complete ingest cycle.
3. The cycle includes source, concept audit and changes, company, optional comparison, contradiction check, provider index, and log.
4. The coordinator runs scoped `validate_wiki.py`.
5. The coordinator creates one commit for that source.
6. Only then may the next approved source enter promotion.

This preserves the repository rule: one source at a time for canonical ingest.

## Failure and Retry Policy

### Retryable up to three total attempts

- worker timeout;
- worker or model failure;
- empty or invalid worker output;
- candidate validation failure;
- raw-link or raw-hash mismatch;
- Sol `changes_requested`.

Operational failures become `failed`. An operator must explicitly run `retry`; retries are placed at the queue tail. Sol `changes_requested` may be queued directly by the coordinator because it is an explicit review result.

### Terminal job outcomes

- A third unsuccessful attempt becomes `rejected`.
- Sol `rejected` becomes `rejected` immediately.
- A rejected job is never automatically retried.
- Other jobs continue when one job is failed or rejected.

### Campaign pause

Any failure after the job enters `promoting` changes the campaign to `paused`.

- No new Sol review or canonical promotion starts.
- Running Terra workers may finish and their candidates may be saved.
- The coordinator does not guess whether Git or canonical wiki writes completed.
- An operator inspects Git and chooses either `resume --mark-completed` or `resume --mark-failed`.
- `resume --mark-failed` records a terminal `rejected` outcome with reason `promotion_outcome_manually_failed`; it never returns the job to the retry queue.

## Restart Rules

On coordinator startup:

- `queued`, `candidate_ready`, `approved`, `completed`, `failed`, and `rejected` are loaded unchanged.
- `running` and `reviewing` become `failed`, with an `interrupted` event.
- Any `promoting` job changes the campaign to `paused`.

The coordinator does not resume a worker, replay an operation, infer a missing event, or reconstruct state from multiple receipts.

## Monitor and Wiki Logs

`monitor.md` shows:

- campaign status;
- counts for every job state;
- each job's current attempt, state, raw path, source target, and last event;
- failure or rejection reason;
- the manual action required when promotion is paused.

Logging responsibilities remain separate:

- `events.jsonl` records technical campaign events.
- `monitor.md` presents current pilot progress.
- `wiki/metronome-log.md` records successful ingests, explicit rejections, and campaign summaries.
- `wiki/metronome-index.md` changes only after a canonical promotion succeeds.

## CLI Surface

The pilot CLI contains only:

```text
init
run
status
retry
reject
resume --mark-completed
resume --mark-failed
```

- `init` creates the fixed five-job campaign.
- `run` fills worker slots, persists returned candidates, and performs at most one serial review or promotion action at a time.
- `status` regenerates and prints the monitor.
- `retry` moves one failed pre-promotion job to the queue tail if fewer than three attempts exist. It rejects promotion-stage failures.
- `reject` marks one failed job terminal.
- `resume` resolves one manually inspected promotion interruption and reactivates the campaign. `--mark-completed` records completion; `--mark-failed` records a terminal rejection.

No generic mutation command, operation-replay command, or automatic-recovery command is included.

## Pilot Gates

### Gate 1: Fake campaign

A deterministic fake campaign proves:

- five worker slots fill;
- a completed worker immediately frees a slot;
- candidates persist without raw or wiki mutation;
- Sol review and promotion never overlap;
- a normal job failure does not block other jobs;
- retry moves to the queue tail and stops after three attempts;
- restart applies the simple failure and pause rules.

### Gate 2: Five-page dry-run

The five selected English canonical Metronome pages cover short, long, schema-heavy, guide, and API-oriented content.

The dry-run:

- uses Terra for full raw reading and candidate production;
- uses Sol for serial review;
- saves candidates, quotes, suggestions, receipts, failures, and monitor state;
- verifies every raw SHA-256 remains unchanged;
- performs no canonical wiki write or promotion commit;
- stops for user review.

### Gate 3: Explicitly approved promotion

Only after the user approves the dry-run:

- the coordinator promotes one complete source cycle at a time;
- scoped wiki validation must pass for each source;
- each source receives its own commit;
- the pilot stops on promotion ambiguity.

Bulk processing of the remaining Metronome corpus is outside this design.

## Test Boundary

Tests cover only user-visible contracts:

- allowed job transitions;
- maximum of three attempts;
- rolling five-slot scheduling;
- strict worker JSON, quote count, raw link, raw hash, and candidate validation;
- one Sol review and one canonical promotion at a time;
- failed jobs do not block unrelated work;
- promotion failure pauses the campaign;
- restart converts `running` and `reviewing` to `failed` and `promoting` to campaign pause;
- one end-to-end fake five-page campaign.

Tests explicitly exclude:

- malicious schema-valid journal rewriting;
- every possible instruction-level crash window;
- exact operation replay;
- concurrent coordinator writers;
- automatic rollback;
- complex recovery matrices.

## Success Criteria

The design is successful when:

- five Terra candidates are generated with rolling concurrency;
- each worker reads exactly one complete raw page;
- each candidate has three to five verified grounding quotes and a raw link;
- Terra and Sol perform no repository writes;
- raw hashes remain unchanged;
- Sol review and canonical promotion remain serial;
- the monitor clearly explains every job's state and required action;
- the dry-run stops for user approval;
- approved pages can be promoted one source at a time;
- no recovery subsystem or hostile-state security model is introduced.

## Branch Strategy

- Base the new design and implementation on the current `main`.
- Keep `codex/metronome-simplified-ingest-orchestration` frozen and unmerged.
- Use a new isolated branch for this minimum pilot.
- Do not cherry-pick implementation commits from the frozen branch.
- Preserve unrelated main-worktree files and other provider work.
