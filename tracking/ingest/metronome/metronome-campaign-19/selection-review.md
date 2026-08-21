# Metronome Campaign 19 Selection Review

- Status: **awaiting exact-manifest approval**
- Purpose: validate Campaign 18 throughput against a more representative
  five-page mix without changing the scheduler, reviewer policy, or close gate.
- Scheduler mode: `dry_run`; no campaign state, worker order, raw read, or
  canonical wiki write exists until this exact manifest is approved.
- Selection method: metadata only — raw path, source URL header, first heading,
  line count, SHA-256, prior-manifest membership, and source-target existence.
  Raw bodies were not read completely during selection and support no facts.
- Selection boundary: every remaining guide belongs to a Campaign 13–15
  non-promotion calibration manifest. Reusing one could blur the prohibition on
  resuming those jobs, so this campaign substitutes the unused 424-line
  `search-events` API page as its medium-complexity sample. No old candidate or
  suggestion is reused.
- Runtime: one coordinator plus at most three repository-read-only native
  agents in the existing dynamic pool; no worktrees and no batch barrier.

| # | Job | Lines | Worker tier | Metadata-visible risk |
| ---: | --- | ---: | --- | --- |
| 1 | `list-account-level-billing-providers` | 225 | standard | read-only provider and delivery-method configuration enumeration |
| 2 | `disable-trueup-for-commit` | 190 | strong | true-up suppression and invoice, balance, timing, and reversibility boundaries |
| 3 | `get-subscription-quantity-history` | 222 | standard | historical quantities and prices versus future scheduled changes |
| 4 | `archive-a-contract` | 229 | strong | permanent contract, invoice, balance, ledger, and visibility effects |
| 5 | `search-events` | 424 | strong | sampling-only observability, 34-day history, matching, duplicates, and rate limits |

## Model routing

- `standard`: GPT-5.6 Sol at medium effort.
- `strong`: GPT-5.6 Sol at high effort.
- Every first attempt: a different GPT-5.6 Sol reviewer at high effort.
- A reviewer cannot review its own worker output. Workers and reviewers remain
  repository-read-only; only the coordinator writes canonical files.

The manifest records only existing `standard` and `strong` routing metadata.
Native-agent identities and model assignments remain coordinator-owned runtime
inputs and must match emitted orders exactly.

## Worker pre-submit gate

After the complete one-page read and before handoff, each worker must:

1. Validate against the current Campaign v2 worker-result contract, including
   schema, enum, canonical URL, raw hash, backlink, and exact quote substrings.
   Do not invoke the legacy `validate_metronome_ingest.py`, whose older trusted
   order schema is incompatible with Campaign v2.
2. Preserve required fields, response limits, lifecycle and propagation
   effects, failure behavior, rate-limit or historical-window boundaries, and
   contradictions; explicitly retain undocumented behavior.
3. Ground every proposed durable fact or contradiction in submitted quote
   indexes that contain the asserted evidence.
4. Rehearse factual retrieval, boundary/contradiction handling, and exact raw
   deep-dive navigation against the candidate.

This changes only the worker instruction. It adds no validator, state field,
retry class, agent, or monitoring layer.

## Review and retry gate

Every first attempt receives an independent complete-source Sol-high review.
An unchanged-hash correction limited to links, frontmatter, wording, or an
already-identified evidence omission may use targeted diff review. Factual,
uncertain, lifecycle, schema, or cross-source corrections require another full
review. Maximum attempts remain three.

## Coordinator close

Only approved candidates may be promoted. The coordinator applies grouped
reviewer-approved concept updates once before canonical sources, then derives
company, provider-index, provider-log, and count changes mechanically. It runs
fact-link, touched-page, capsule, raw-hash, duplicate catalog, and count checks
once. It does not perform a default third full-source read.

## Immutable query audit

- Standard page: `list-account-level-billing-providers`
- Longest/schema page: `search-events`
- Ordinary sample: `get-subscription-quantity-history`

Each receives exactly three future-query tests: factual retrieval,
boundary/contradiction handling, and exact raw deep dive. A material partial or
fail expands the audit to all five pages. Mechanical link defects are corrected
before the query audit and do not create an extra audit framework.

## Throughput gate

Campaign 19 uses only existing `started_at` and `completed_at` timing fields.
Success signals are intentionally small:

- At least four of five pages approved on attempt 1.
- No more than one full semantic retry.
- No audit expansion caused by a mechanical link omission.
- Approximately 35 minutes or less of visible active work is desirable, not a
  correctness gate.

If these pass on the more representative mix, a separately approved Campaign
20 may expand to 8–10 pages while retaining three dynamic slots and the same
fixed three-page audit. This manifest does not authorize that expansion.

## Authorization boundary

Approval of this exact manifest authorizes initialization, complete reads of
only these five raw pages, independent per-page review, bounded retries, the
fixed/expanded audit rule, and coordinator promotion of reviewer-approved jobs
after all close gates pass. It does not authorize any other page, reuse or
promotion of Campaign 13–15 candidates, routing reclassification, another
model comparison, bulk ingestion, cross-provider rollout, or remote push.
