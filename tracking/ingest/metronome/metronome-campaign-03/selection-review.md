# Metronome Campaign 03 Selection Review

Status: `proposed_awaiting_approval`

Manifest: [manifest.json](manifest.json)

This proposal tests portable worker-tier routing on five new English canonical pages. Selection used only `inventory-current.json`, raw paths, byte hashes, line counts, and existing source coverage. No raw body was read by the coordinator, no campaign state was initialized, and no worker was started.

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

## Approval boundary

Approval of this selection would authorize campaign initialization and native worker launch for these five jobs. Until then, this directory contains proposal files only: no `campaign.json`, `jobs.json`, `events.jsonl`, `monitor.md`, or `attempts/`.
