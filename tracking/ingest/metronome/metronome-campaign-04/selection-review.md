# Metronome Campaign 04 Selection Review

Status: `proposed_awaiting_approval`

Manifest: [manifest.json](manifest.json)

This is a bounded follow-up to Campaign 03. Selection used only `inventory-current.json`, raw paths, byte hashes, line counts, and existing source coverage; no raw body was read while preparing the proposal. Approval of this proposal is a separate gate from initialization or worker launch.

## Proposed jobs

| Order | Job | Page shape | Lines | Recommended tier | Routing reason |
| ---: | --- | --- | ---: | --- | --- |
| 1 | `authentication` | API-wide convention | 112 | `standard` | Short authentication convention without a resource schema or financial lifecycle. |
| 2 | `pagination` | API-wide convention | 61 | `standard` | Short pagination convention without financial state transitions. |
| 3 | `ingest-events` | Usage API reference | 293 | `strong` | Schema-heavy event ingestion with identity and validation semantics. |
| 4 | `prepaid-balance-thresholds` | Customer-balance guide | 269 | `strong` | Financial thresholds, recharge behavior, and balance lifecycle. |
| 5 | `schedule-billing-provider-change` | Billing-provider guide | 137 | `strong` | Provider transition timing and a cross-system responsibility boundary. |

Total selected raw lines: 872. This is smaller than Campaign 03's 1,482 lines while preserving the same two-standard/three-strong routing split.

## Deterministic selection checks

- All five entries are selected English `page` records in `tracking/collections/metronome/inventory-current.json`.
- Every raw file exists and its SHA-256 matches the manifest.
- Every canonical URL matches the inventory.
- None of the five raw paths is referenced by an existing canonical Metronome source page.
- All five source targets are unique and do not exist.
- Routing metadata uses only `standard` or `strong`, with a non-empty reason.
- The proposal contains two standard jobs and three strong jobs.

## Proposed execution boundary

- Map `standard` and `strong` through coordinator configuration; keep concrete model names outside the manifest.
- Each worker reads exactly one full raw page and writes only its isolated candidate result.
- The Sol coordinator performs serial concept-first review and owns all canonical source, company, concept, index, log, contradiction, and link changes.
- Refill an available worker slot immediately rather than waiting for a five-job batch barrier.
- Retry a failed job up to three total attempts; a job-level failure does not pause unrelated jobs.
- Do not initialize or launch this campaign until the user approves this exact proposal.
