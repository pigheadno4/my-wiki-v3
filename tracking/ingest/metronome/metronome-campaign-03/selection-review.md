# Metronome Campaign 03 Selection Review

Status: `complete`

Manifest: [manifest.json](manifest.json)

The user approved this routing pilot on 2026-07-29. Selection used only `inventory-current.json`, raw paths, byte hashes, line counts, and existing source coverage; no raw body was read before approval. All five jobs then passed deterministic worker-result validation and serial full-raw Sol review on attempt 1 before canonical promotion.

## Proposed jobs

| Order | Job | Page shape | Lines | Recommended tier | Routing reason |
| ---: | --- | --- | ---: | --- | --- |
| 1 | `metronome-dashboard-quickstart` | Getting-started dashboard guide | 248 | `standard` | Bounded dashboard workflow without an API schema or financial lifecycle. |
| 2 | `data-export-overview` | Reporting overview | 134 | `standard` | Short descriptive overview supplementing an existing reporting concept. |
| 3 | `create-pre-paid-commit` | Commitment implementation guide | 459 | `strong` | Financial schedules, invoicing behavior, and commitment lifecycle conditions. |
| 4 | `edit-a-commit` | API reference | 457 | `strong` | Structured schema for changing financial commitment state. |
| 5 | `stripe-tax` | Cross-provider integration guide | 184 | `strong` | Stripe Tax and Metronome invoice responsibility boundary. |

Total selected raw lines: 1,482. Campaign 02 contained 1,442 raw lines, so this is a bounded comparison rather than a larger-volume run.

## Deterministic selection checks

- All five entries are selected English `page` records in `tracking/collections/metronome/inventory-current.json`.
- Every raw file exists and its SHA-256 matches the manifest.
- Every canonical URL matches the inventory.
- None of the five raw paths is referenced by an existing canonical Metronome source page.
- All five source targets are unique and do not exist.
- Routing metadata uses only `standard` or `strong`, with a non-empty reason.
- The proposal contains two standard jobs and three strong jobs.

## Proposed evaluation

- Map `standard` to the configured lower-cost ingestion worker and `strong` to the configured high-judgment worker; concrete model names remain outside the manifest.
- Preserve serial canonical promotion and coordinator ownership of company, concept, index, log, and link reconciliation.
- Check forward links, reverse links, semantic link relevance, and duplicate raw/source/index/company/log links for every promoted page.
- Record coordinator full-raw rereads, canonical repairs, link findings, and final hard/partial/pass results.

## Execution result

- Routing: the two `standard` jobs ran on native GPT-5.6 Terra; the three `strong` jobs ran on native GPT-5.6 Sol.
- Scheduling: three workers started initially, and the remaining jobs entered as slots freed; no batch barrier was used.
- Worker boundary: every worker read one complete raw page and wrote only a fixed-schema candidate result outside the repository. Shared and canonical files remained coordinator-owned.
- Review: Sol reread all five raw pages in full, performed concept-first promotion, checked contradictions, and reconciled forward, reverse, semantic, and duplicate links.
- Result: 5 approved, 0 failed, 0 retried, and 0 rejected. All approvals occurred on attempt 1.
- Canonical repair: standard-tier source candidates required no material source-body repair. The prepaid guide's warning was classified as a formal contradiction and mirrored onto the create-contract API source; other strong-tier candidates were promoted without material source-body repair.
- Findings preserved: no stated data-export retention period; dashboard-only and Sandbox-only boundaries; prepaid example amount, JSON, date, and rollover inconsistencies; edit-API response and mutation unknowns; and Stripe Tax's `Product` versus `ContractProduct` ambiguity and provider-scope caution.
- Coverage after promotion: 20 Metronome source summaries ingested and 205 documentation pages pending.

## Routing conclusion

The metadata correctly separated bounded operational pages from financial, schema-heavy, and cross-provider pages in this sample. It is suitable for another bounded campaign without adding a classifier, risk score, or automatic escalation state.

This pilot does not demonstrate lower Sol review-token volume because the coordinator still reread all five raw pages in full. Any future token-saving review policy should be proposed and approved separately rather than inferred from these results.
