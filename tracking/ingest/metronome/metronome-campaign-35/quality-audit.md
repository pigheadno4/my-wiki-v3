# Metronome Campaign 35 quality audit

## Outcome

- Final approval: 5/5 new source pages.
- First-pass approval: 0/5 pages.
- Worker attempts: 11; full independent reviews: 10; targeted reviews: 0.
- One Product attempt was rejected mechanically before review because it used an unsupported shared-update kind; attempt 3 changed only that contract field.
- Rejected terminal jobs: 0; coordinator semantic repairs: 0.
- Fixed query audit: 9/9 PASS; expansion beyond the three immutable sample pages was not required.

Final content quality passed. The campaign missed the first-pass and eight-attempt throughput gates, while meeting the 45-minute observational target by completing in 2,657 seconds (44 minutes 17 seconds). No retry was caused by omitting or misstating the provider-wide execution-admission boundary, and the legacy GET negative control did not import POST idempotency semantics.

## Mechanical close checks

- All five manifest raw SHA-256 values matched the immutable files.
- All five canonical source targets were byte-identical to their approved final candidates.
- Twenty-eight reviewer-approved shared updates appeared exactly once across fourteen existing concepts.
- Each new source appeared exactly once in the company catalog and provider index.
- Nineteen touched source, concept, and company files passed targeted `validate_wiki.py` checks.
- The Metronome capsule validator passed with 310 raw snapshots, 177 source summaries, and 115 raw snapshots without source summaries.
- Campaign-owned `git diff --check` passed.

## Fixed query audit

**Verdict: PASS (9/9 cells).**

Audit scope was limited to the immutable manifest-selected sample:

- `add-a-manual-balance-entry-new-source`
- `get-batched-usage-data-new-source`
- `archive-a-threshold-notification-new-source`

For each page, the full promoted canonical source, full assigned raw file, approved final candidate and full review, and all relevant primary-concept/shared-update routes were checked. The promoted source is byte-identical to its approved candidate in all three cases. Every approved shared update for the sample appears exactly once in its target (manual 10/10, usage 5/5, alert 4/4), and every primary concept named by each source links back to that source.

## 1. Add a manual balance entry

### Cell 1 — Query-critical factual answer: PASS

The source correctly answers that bearer-authenticated `POST /v1/contracts/addManualBalanceLedgerEntry` appends a manual event to one commit-or-credit segment. For a supplied payload, `customer_id`, balance `id`, `segment_id`, `amount`, and `reason` are required; a negative amount draws balance down. It also correctly limits requiredness: the OpenAPI `requestBody` wrapper itself is not marked required. These statements match the assigned raw and do not claim invoice recalculation, read-after-write visibility, or response-body data that the endpoint does not establish.

### Cell 2 — Material boundary/contradiction and reciprocal concept route: PASS

The source preserves the correction boundary: a manual balance event addresses a balance discrepancy but does not by itself correct underlying usage or pricing or prove invoice regeneration, refund, payment, tax, revenue, or external A/R reconciliation. The raw explicitly distinguishes the manual ledger route from upstream contract/rate actions that cause invoice recalculation. `[[metronome-invoicing]]` carries the same fact-bearing boundary and links back to `[[source-metronome-api-reference-credits-and-commits-add-a-manual-balance-entry]]`; the corresponding Sources entry is also present. All four primary concepts named by the source link back: credits-and-commits, customers-and-contracts, invoicing, and API idempotency. The approved secondary subscriptions updates are also present exactly once.

### Cell 3 — Exact raw deep dive, SHA, and candidate identity: PASS

The source uses the exact path-qualified backlink `[[raw/metronome/api-reference/credits-and-commits/add-a-manual-balance-entry-2026-08-28|...]]`, which resolves to the assigned raw file. Its SHA-256 is `fd35fca71a4b446a30ae6eabe3bcd0c424566ac21b9efa9bbe482bb8923bcd55`, exactly matching the manifest. The promoted source is byte-identical to approved attempt-2 `candidate.md`.

## 2. Get batched usage data

### Cell 4 — Query-critical factual answer: PASS

The source correctly answers that bearer-authenticated `POST /v1/usage` reads multi-customer, multi-metric aggregates. Within a supplied body, `window_size`, `starting_on`, and `ending_before` are required; HTTP `200` places required `data` and nullable `next_page` as siblings in the top-level response envelope. It correctly preserves the unmarked request-body wrapper and does not infer a limit, stable snapshot, freshness, billing completeness, or raw-event acceptance.

### Cell 5 — Material boundary/contradiction and reciprocal concept route: PASS

The source preserves the raw narrative-versus-schema cursor contradiction: the narrative lists `next_page` with aggregate fields, but the response schema and example place a single nullable cursor beside top-level `data`. `[[metronome-reporting-and-analytics]]` records the same fact-bearing integration boundary and links back to `[[source-metronome-api-reference-usage-get-batched-usage-data]]`. All five primary concepts named by the source link back: billable metrics, reporting and analytics, usage-based billing, event ingestion, and API idempotency. The source also avoids the rejected overreach that `window_size: none` implies one total response row; it limits this to one full-period time window.

### Cell 6 — Exact raw deep dive, SHA, and candidate identity: PASS

The source uses the exact path-qualified backlink `[[raw/metronome/api-reference/usage/get-batched-usage-data-2026-07-13|...]]`, which resolves to the assigned raw file. Its SHA-256 is `c3124c5620213df5cb392f335be431a240d5be42e9f955312017d2432c3be924`, exactly matching the manifest. The promoted source is byte-identical to approved attempt-2 `candidate.md`.

## 3. Archive a threshold notification

### Cell 7 — Query-critical factual answer: PASS

The source correctly answers that bearer-authenticated `POST /v1/alerts/archive` archives one threshold-notification configuration. Within a supplied payload, UUID `id` is required; optional `release_uniqueness_key: true` resets the resource key for reuse. HTTP `200` returns required top-level `data` containing required UUID `id`. It correctly preserves that the request-body wrapper is not marked required and does not invent omitted/false release behavior, completion markers, per-customer results, or propagation status.

### Cell 8 — Material boundary/contradiction and reciprocal concept route: PASS

The source preserves the lifecycle/transport boundary: the raw says evaluation stops immediately, but that does not establish cancellation, retraction, or delivery suppression for a webhook already emitted, queued, retrying, or in flight. `[[metronome-webhooks]]` records this fact-bearing boundary and links back to `[[source-metronome-api-reference-alerts-archive-a-threshold-notification]]`. All four primary concepts named by the source link back: alerts and notifications, API idempotency, webhooks, and reporting and analytics. The separate archive state, resource-key release, request replay, export visibility, and webhook delivery surfaces remain distinct.

### Cell 9 — Exact raw deep dive, SHA, and candidate identity: PASS

The source uses the exact path-qualified backlink `[[raw/metronome/api-reference/alerts/archive-a-threshold-notification-2026-07-13|...]]`, which resolves to the assigned raw file. Its SHA-256 is `dbe2678c59b5b3471905149e8aa329b476e12f6d32a2cb290b74372c6e69d467`, exactly matching the manifest. The promoted source is byte-identical to approved attempt-2 `candidate.md`.

## Blockers

None. No material partial result requires expanding this fixed audit beyond the three immutable sample jobs.
