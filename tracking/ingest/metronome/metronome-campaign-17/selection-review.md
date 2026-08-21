# Metronome Campaign 17 Selection Review

- Status: **completed - 5/5 approved and promoted**
- Purpose: second five-page production campaign and the first use of a compact
  worker self-check intended to reduce avoidable full-review retries without
  adding a scheduler, state schema, model comparison, or additional agent.
- Scheduler mode: `dry_run`; workers and reviewers remain repository-read-only.
  Canonical promotion remains a coordinator close action after terminal reviews
  and the campaign-close quality gate.
- Selection method: metadata only — raw path, canonical URL derived from the
  path, first heading, line count, SHA-256, prior-manifest membership, and
  source-target existence. No raw body was read completely during selection.
- Selection: all five remaining English guide pages that have neither prior
  campaign membership nor a canonical Metronome source page. API references,
  prior-campaign pages, and already-ingested pages are excluded.
- Models: Sol-medium worker and a different Sol-high reviewer for every page.
- Runtime: one coordinator plus at most three repository-read-only native
  agents in the existing dynamic pool. No worktrees and no batch barrier.

| # | Job | Lines | Metadata-visible risk |
| ---: | --- | ---: | --- |
| 1 | `make-a-pricing-change` | 200 | pricing-change workflow; standard audit page |
| 2 | `edit-or-override-a-contract` | 237 | contract edits versus overrides; ordinary audit sample |
| 3 | `data-export-cookbook` | 264 | SQL examples and exported-table grain |
| 4 | `edit-contract` | 329 | contract-edit lifecycle and request examples |
| 5 | `revenue-recognition-examples` | 354 | accounting examples; longest and high-risk audit page |

## Worker pre-submit self-check

This checklist is performed inside the existing worker turn after the complete
raw read and before result submission. It does not add a new agent, file type,
state field, or review round.

1. Preserve every top-level taxonomy, named model, workflow branch, or
   capability list introduced near the beginning of the page.
2. Preserve required fields, durable failure or propagation behavior,
   lifecycle boundaries, and material contradictions found anywhere in the
   page; keep undocumented behavior explicit.
3. Ensure every proposed durable concept fact and contradiction is supported
   by one or more submitted quote indexes.
4. Rehearse three future queries against the candidate: factual retrieval,
   boundary or contradiction handling, and exact raw-backlink deep dive.

The generated worker order remains the authority for job ID, raw path/hash,
canonical URL, source target, result schema, and retry context. The checklist
adds only a same-turn completeness check.

## Per-page review gate

Each worker reads exactly one complete raw page, extracts three to five
byte-exact quotes, and returns one isolated source candidate plus fact-bearing
concept, reciprocal-link, and contradiction suggestions. Company, index, and
log suggestions remain empty.

A different Sol reviewer reads the complete raw page and checks source facts,
important omissions, contradictions, unknowns, quote grounding, raw backlink,
and shared semantic suggestions. Unchanged-hash mechanical or already-bounded
corrections may use targeted review; factual, uncertain, or interpretive
corrections require another full review. Maximum attempts remain three.

## Coordinator close and audit

Only approved jobs are eligible for promotion. The coordinator groups approved
concept updates by exact target, applies each target once before its sources,
then derives company, provider-index, provider-log, and count changes
mechanically. The coordinator does not perform a default full-source reread.

The immutable audit sample is:

- standard page: `make-a-pricing-change`
- longest/high-risk page: `revenue-recognition-examples`
- ordinary sample: `edit-or-override-a-contract`

Each receives the fixed retrieval, boundary/contradiction, and raw-deep-dive
query audit. A material partial or fail expands the audit to all five pages.
Campaign close runs the touched-page validator, Metronome capsule validator,
raw-hash, duplicate catalog, reciprocal fact-link, and count checks once.

## Throughput observation

Campaign 17 records the existing `started_at` and `completed_at` values and the
existing attempt/review counts. It does not add per-event timestamps or a
performance subsystem.

- Quality gate: no material query-audit partial or fail at closure.
- First-pass observation: at least 3/5 pages approved on attempt 1 would support
  increasing the next production campaign to ten pages.
- Elapsed-time observation: approximately 30–35 minutes is desirable but is
  not a hard gate because native-agent runtime can vary independently of the
  content workflow.
- If only one or two pages pass on attempt 1, do not add more workflow
  machinery; the next decision is whether to raise worker reasoning effort.

## Authorization boundary

Approval of this exact manifest authorizes initialization, complete reads of
only these five raw pages, independent per-page review, bounded retries, the
fixed/expanded audit rule, and coordinator promotion of reviewer-approved jobs
after all close gates pass. It does not authorize any API-reference page,
prior-campaign retry or promotion, routing reclassification, another model
comparison, bulk ingestion, cross-provider rollout, or remote push.
