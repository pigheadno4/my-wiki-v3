# Metronome Campaign 30 bounded first-pass reminder proposal

**Status:** Awaiting explicit manifest approval; no ingestion authorized
**Mode:** Five-page existing-source refresh
**Collection baseline:** 81 changed, 1 new, and 146 unchanged current targets

## Goal

Test the two small follow-ups from Campaign 29 without changing the ingestion
architecture. Campaign 30 retains five pages, strong Sol workers, independent
complete-source Sol review, dynamic slots, existing retry rules, incremental
promotion, and the mature close path.

The two additional campaign-local reminders are:

1. Every retained factual shared-file claim must be fully covered by the
   selected quote ranges used by that suggestion.
2. When a guide, concept, or security page explicitly defines principal actors
   or actor-to-role relationships, preserve those mappings in the source
   candidate and relevant primary-concept suggestion.

Campaign 29's proven API reminders remain in scope where relevant: assign each
query-critical field to its immediate parent schema, and preserve exact raw
financial units and source authority before paraphrasing.

This proposal adds no registry, schema field, validator, scheduler state,
review tier, model route, or monitoring layer.

## Metadata and collection-evidence selection

Selection used current collection state, raw path, line count, SHA-256, stored
diff size, existing-source presence, archetype, and distance from the source
identity's prior campaign. Raw bodies were not read in full to prepare this
proposal; workers and reviewers must still complete their assigned reads.

Only `collected-changed` pages were selected. An initially considered alert
page was excluded because its current collection state is `unchanged`, which
must not trigger a model task.

The first dispatch wave starts the longest API read, the financial mutation,
and the integration page so their complete reads overlap the shorter guides.

| Job | Raw lines | Diff lines | Archetype | Prior campaign | Selection reason |
| --- | ---: | ---: | --- | --- | --- |
| `get-an-invoice-refresh` | 1,042 | 44 | API Read / Schema | 21 | Longest control for parent-schema placement, envelope and nested-resource boundaries, invoice state, and evidence closure |
| `create-a-commit-refresh` | 626 | 51 | API Mutation / Financial | 02 | Financial-unit, required-field, lifecycle, idempotency-authority, and evidence-closure control |
| `stripe-invoice-integration-refresh` | 331 | 36 | Integration Guide | 02 | Metronome-versus-Stripe actors, invoice and payment authority, failure, reconciliation, and shared-evidence control |
| `customer-controls-refresh` | 185 | 20 | Concept / Customer Guide | 08 | Principal-actor, control ownership, enforcement boundary, and shared-evidence control |
| `create-billable-metrics-refresh` | 132 | 36 | Concept / Implementation Guide | 05 | Short guide control for actors, metric-definition boundaries, lifecycle, and shared-evidence closure |

The five latest raws total 2,316 lines. The fixed close audit uses
`get-an-invoice-refresh`, `create-a-commit-refresh`, and
`customer-controls-refresh` to cover the longest schema page, financial
mutation, and principal-actor reminder.

## Worker and staging contract

Each worker must:

1. Read the complete 2026-08-28 raw and complete current source target. Treat
   the stored diff as navigation only.
2. Return one complete Minimum Sufficient Source candidate with query-critical
   facts, material boundaries or contradictions, a raw-detail coverage map,
   primary concept routes, newest-first immutable history, and an exact
   path-qualified raw backlink.
3. Apply the immediate-parent schema and exact-unit or authority reminders when
   relevant; do not force irrelevant sections onto a page.
4. Preserve every source-defined principal actor or actor-to-role mapping that
   affects a realistic integration or access decision.
5. Ensure every factual claim retained in a shared-file suggestion is directly
   supported by its selected quote indexes. Either broaden the quote range or
   trim the unsupported claim.
6. Return only the fixed result object outside the repository. The controller
   alone writes attempt evidence, campaign state, canonical pages, shared
   files, and the commit.

## Review, success gates, and close

- Use strong Sol workers and different strong Sol complete-source reviewers.
- Keep three dynamic native-agent slots and no batch barrier.
- Every first review reads the complete assigned raw and candidate.
- A bounded unchanged-hash correction may receive targeted review only when it
  changes no factual meaning. Factual, authority, actor, material-omission, or
  contradiction fixes require complete review.
- The coordinator does not perform a default third full raw read or silently
  repair source semantics. It promotes only reviewer-approved candidates and
  shared updates, then performs shared catalogs, links, counts, and mechanical
  close checks once.
- Required close result: five of five finally approved, at least four of five
  approved on the first attempt, no rejected job, no coordinator semantic
  repair, and no more than one full semantic retry.
- The fixed three-page query audit must pass all nine checks. Existing targeted
  wiki checks, capsule validation, raw-hash, link, count, candidate-equality,
  and `git diff --check` checks run once at close.
- Thirty-five minutes remains an observation target, not a quality waiver.
  Only campaign-level `started_at` and `completed_at` are recorded.

## Authorization boundary

This file and `manifest.json` are proposal artifacts only. They do not
initialize Campaign 30 or authorize agent dispatch. Separate approval of this
exact manifest would authorize complete reads of only these five current raw
pages, updates to only the five named existing source targets, distinct
per-page Sol reviews, bounded retries, reviewer-approved shared updates,
canonical promotion, the fixed three-page audit, mature close checks, and one
local campaign commit.

It does not authorize a sixth page, larger campaign, bulk ingestion, reviewer
sampling, Luna or Terra routing, rule or code changes, cross-PSP rollout,
remote push, or unrelated-file modification.
