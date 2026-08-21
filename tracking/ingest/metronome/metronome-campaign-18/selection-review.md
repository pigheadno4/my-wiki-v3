# Metronome Campaign 18 Selection Review

- Status: **awaiting exact-manifest approval**
- Purpose: five-page speed-and-quality campaign using three standard workers and
  two stronger first-pass workers, while retaining independent per-page review.
- Scheduler mode: `dry_run`; no campaign state, worker order, or canonical wiki
  write exists until this exact manifest is approved and initialized.
- Selection method: metadata only — raw path, source URL header, first heading,
  line count, SHA-256, prior-manifest membership, and source-target existence.
  Raw bodies were not read completely during selection and support no facts.
- Selection boundary: the sixteen remaining guide pages all belong to Campaign
  13–15 negative or non-promotion calibration manifests. Campaign 18 therefore
  selects five short API pages with no prior campaign membership instead of
  resuming old jobs or reusing old candidates.
- Runtime: one coordinator plus at most three repository-read-only native
  agents in the existing dynamic pool; no worktrees and no batch barrier.

| # | Job | Lines | Worker tier | Metadata-visible risk |
| ---: | --- | ---: | --- | --- |
| 1 | `list-pricing-units` | 165 | standard | read-only pricing-unit listing and denomination taxonomy |
| 2 | `archive-a-rate-card` | 154 | strong | archival state, future availability, and existing-contract propagation |
| 3 | `list-plans` | 180 | standard | deprecated read-only Plans listing and Contracts migration boundary |
| 4 | `release-external-payment-gate-threshold-commit` | 163 | strong | webhook-correlated payment outcome and pending-commit state transition |
| 5 | `get-an-invoice-pdf` | 198 | standard | binary response, invoice/customer identifiers, and unsupported officiality or compliance implications |

## Model routing

- `standard`: GPT-5.6 Sol at medium effort.
- `strong`: GPT-5.6 Sol at high effort.
- Every first attempt: a different GPT-5.6 Sol reviewer at high effort.
- A reviewer cannot review its own worker output. All workers and reviewers are
  repository-read-only; only the coordinator may write canonical files.

The manifest records only the existing `standard` or `strong` routing metadata.
Actual native-agent identities and model assignments remain coordinator-owned
runtime inputs and must match emitted worker or reviewer orders exactly.

## Worker pre-submit gate

Inside the existing worker turn, after the complete one-page read and before
handoff, the worker must:

1. Run the generated order's authoritative result validator and correct any
   schema, enum, canonical URL, raw hash, backlink, or quote-substring failure
   before returning the result.
2. Preserve required request fields, response-media or response-schema limits,
   lifecycle effects, failure behavior, propagation semantics, deprecation,
   and material contradictions; keep undocumented behavior explicit.
3. Ensure every proposed durable concept fact or contradiction cites submitted
   quote indexes that actually contain the asserted evidence.
4. Rehearse factual retrieval, boundary/contradiction handling, and exact raw
   deep-dive navigation against its candidate.

This is a same-turn checklist using existing validation. It adds no agent,
state field, retry class, validator, or monitoring subsystem.

## Review and retry gate

Every first attempt receives a complete-source independent review. A bounded
unchanged-hash correction limited to links, frontmatter, wording, or an
already-identified evidence omission may use targeted diff review. Factual,
uncertain, lifecycle, schema, or cross-source corrections require another full
complete-source review. Maximum attempts remain three.

## Coordinator close and link preflight

Only approved candidates may be promoted. The coordinator applies grouped
reviewer-approved concept changes once, before canonical sources, and derives
company, provider-index, provider-log, and count changes mechanically.

Before the query audit, the coordinator performs one simple fact-link table:
for every approved fact-bearing concept update, verify source-to-concept and
concept-to-source links each occur exactly once. This uses existing `rg`/wiki
checks and adds no registry or new validator. Mechanical defects are repaired
before the query audit rather than triggering avoidable audit expansion.

## Immutable query audit

- Standard page: `list-pricing-units`
- Schema/state-transition page: `release-external-payment-gate-threshold-commit`
- Ordinary sample: `list-plans`

Each receives exactly three future-query checks: factual retrieval,
boundary/contradiction handling, and exact raw deep dive. A material partial or
fail expands the audit to all five pages. Campaign close runs touched-page,
capsule, raw-hash, duplicate catalog, reciprocal fact-link, and count checks
once. Code and rules are unchanged, so only targeted documentation tests run.

## Throughput observation

Campaign 18 uses the existing campaign `started_at` and `completed_at`. At
close, the coordinator records the time when all page reviews became terminal
in this selection review as one plain observation; it does not change campaign
state schema or introduce per-event performance logging.

Success signals:

- At least three of five pages approved on attempt 1.
- No more than two full semantic retries.
- No audit expansion caused by a mechanical link omission.
- Approximately 35–45 minutes of visible active work is desirable, not a hard
  correctness gate.

## Authorization boundary

Approval of this exact manifest authorizes initialization, complete reads of
only these five raw pages, independent per-page review, bounded retries, the
fixed/expanded audit rule, and coordinator promotion of reviewer-approved jobs
after all close gates pass. It does not authorize any other API or guide page,
reuse or promotion of Campaign 13–15 candidates, routing reclassification,
another model comparison, bulk ingestion, cross-provider rollout, or remote
push.
