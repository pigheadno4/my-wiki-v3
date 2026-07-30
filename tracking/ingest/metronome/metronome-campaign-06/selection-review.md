# Metronome Campaign 06 Selection Review

Status: `complete`

Manifest: [manifest.json](manifest.json)

This campaign scales the proven native coordinator flow from five to ten jobs while keeping the content size bounded. Selection used only `inventory-current.json`, raw paths, byte hashes, line counts, and existing source coverage. No raw body was read while preparing this proposal.

## Proposed jobs

| Order | Job | Page shape | Lines | Recommended tier | Routing reason |
| ---: | --- | --- | ---: | --- | --- |
| 1 | `api-introduction` | API foundation | 71 | `standard` | Short convention page without a resource schema or financial lifecycle. |
| 2 | `postman` | Developer tooling | 79 | `standard` | Short, bounded integration setup. |
| 3 | `api-quickstart` | API onboarding | 148 | `standard` | Bounded onboarding flow rather than a schema-heavy reference. |
| 4 | `send-usage-events` | Event operations guide | 118 | `standard` | Focused event-sending flow with existing ingestion concepts. |
| 5 | `provision-customer` | Customer operations guide | 124 | `standard` | Focused provisioning flow backed by established customer concepts. |
| 6 | `how-metronome-works` | Cross-object architecture | 163 | `strong` | Spans metering, pricing, contracts, and invoicing. |
| 7 | `create-products-contracts` | Commercial object guide | 119 | `strong` | Product and contract relationships affect pricing interpretation. |
| 8 | `provision-contract` | Contract lifecycle guide | 213 | `strong` | Carries pricing, effective-time, and billing lifecycle semantics. |
| 9 | `create-manage-rate-cards` | Pricing configuration guide | 264 | `strong` | Pricing and dimensional-rate semantics need cross-concept judgment. |
| 10 | `create-a-billable-metric` | Billable-metric API | 342 | `strong` | Schema-heavy aggregation configuration affects downstream pricing. |

Total selected raw lines: 1,641.

Routing balance: five `standard` jobs and five `strong` jobs.

## Why this ten-page set

- It forms a useful onboarding spine: API entry and tooling, event/customer setup, platform architecture, then products, contracts, rate cards, and billable metrics.
- It doubles job count without simultaneously increasing maximum page size. Campaign 05's only material audit failure occurred in a 1,133-line nested OpenAPI page, so Campaign 06 isolates scheduling scale from extreme-document complexity.
- The largest selected page is 342 lines. The pending 4,532-line `edit-a-contract` reference remains outside this campaign and should receive a later dedicated proposal rather than consume the first ten-job scale test.
- Path and line-count metadata are sufficient for the provisional tier assignments. Workers and the coordinator must still read each selected raw page fully before any content judgment.

## Deterministic selection checks

- All ten entries are selected English `page` records in `tracking/collections/metronome/inventory-current.json`.
- Every raw file exists and its SHA-256 matches the manifest.
- Every canonical URL matches the inventory.
- None of the ten raw paths is referenced by an existing canonical Metronome source page.
- All ten source targets are unique and do not exist.
- Routing metadata uses only `standard` or `strong`, with a non-empty reason.
- The proposal contains five standard jobs and five strong jobs.

## Proposed execution boundary

- Keep the existing portable `standard` and `strong` routing; do not add another classifier.
- Start at most three native workers concurrently because the Sol coordinator occupies the fourth agent slot.
- Refill each available slot immediately after coordinator acceptance or rejection; do not wait for a five-job batch barrier.
- Each worker receives one generated self-contained order, reads exactly one complete raw file, runs the canonical-URL/top-level-key/quote-field preflight, and returns only its isolated fixed-schema candidate.
- The Sol coordinator performs serial full-raw review, concept-first promotion, contradiction review, reverse-link reconciliation, and deterministic validation.
- Invalid results retain evidence and may retry up to three total attempts without pausing unrelated jobs.
- Workers do not edit repository files. Company, concept, index, log, and campaign state remain coordinator-owned.

## Acceptance gates

Before Campaign 06 can be called complete:

1. All ten jobs reach `approved`, `rejected`, or exhausted-attempt terminal state with durable attempt receipts.
2. Every approved source receives serial full-raw Sol review before promotion.
3. Forward and reverse source/concept/company links are reconciled.
4. `validate_wiki.py`, `validate_metronome_capsule.py`, campaign integrity checks, and the full unit suite pass.
5. An independent query-quality audit samples all ten sources with one core, one boundary, and one trap question before any recommendation to increase scale again.

Campaign initialization and worker launch require approval of this exact proposal.

## Execution result

- Routing: five standard jobs used native GPT-5.6 Terra and five strong jobs used native GPT-5.6 Sol.
- Scheduling: no more than three workers ran concurrently; a freed slot started the queued retry without waiting for a batch barrier.
- Worker boundary: workers read one complete raw page and wrote isolated fixed-schema candidates under `/private/tmp`; only the Sol coordinator wrote shared repository files.
- Review: Sol reread all ten raw pages, promoted concept-first, preserved contradictions and unknowns, reconciled links, and validated each source.
- Retry behavior: nine jobs passed on attempt 1. `provision-customer` attempt 1 failed a byte-for-byte quote check; evidence was retained, and a fresh Terra attempt 2 passed and was approved.
- Final result: 10 approved jobs, 1 failed attempt, 1 retry, and 0 rejected jobs.
- Coverage after promotion: 40 Metronome source summaries ingested and 185 documentation pages pending.

## Quality and graduation result

The independent query audit initially produced 29 pass, 1 partial, and 0 fail across 30 tests. A one-sentence creation-time recommendation was restored to the customer source; the final result is 30 pass, 0 partial, and 0 fail.

Every source and raw link resolves, each Campaign 06 source appears exactly once in the company page and provider index, all manifest hashes match, targeted validation passes, the capsule reconciles 225/40/185, and the full suite passed 548 tests.

Concept backlinks use a narrow fact-based rule: company and provider index are exhaustive catalogs, while a concept cites a source only when that source contributes a durable fact. Navigation-only source links do not force mechanical reciprocal citations.

Campaign 06 is complete, but it does not graduate the workflow to reduced testing or parallel review because one first attempt was malformed. Evidence: [quality-audit.md](quality-audit.md).
