# Metronome Campaign 04 Selection Review

Status: `complete`

Manifest: [manifest.json](manifest.json)

This bounded follow-up to Campaign 03 was approved and executed on 2026-07-29. Selection used only `inventory-current.json`, raw paths, byte hashes, line counts, and existing source coverage; no raw body was read before approval. Every job later received one complete worker reread and one complete serial Sol reread before canonical approval.

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
- The user approved this exact proposal before initialization and worker launch.

## Execution result

- Routing: the two `standard` jobs ran on native GPT-5.6 Terra; the three `strong` jobs ran on native GPT-5.6 Sol.
- Scheduling: three workers started initially and later jobs or retries entered as slots became available; no batch barrier was used.
- Worker boundary: every attempt read exactly one complete raw page and wrote only an isolated fixed-schema candidate outside the repository. The coordinator alone wrote tracking and canonical wiki files.
- Review: Sol reread all five raw pages in full, performed concept-first promotion, reconciled forward and reverse links, checked contradictions, and ran focused deterministic validation after each source.
- Final result: 5 approved jobs, 0 rejected jobs, and 5 failed attempts preserved as evidence.
- Attempts: `authentication` 2, `pagination` 2, `ingest-events` 2, `prepaid-balance-thresholds` 1, and `schedule-billing-provider-change` 3.
- Deterministic failures: three first attempts used the `.md` fetch URL instead of the canonical URL; the provider-change job then failed once for extra or missing fixed-schema fields and once for missing quote locations.
- Canonical findings: customer-token lifetime remains distinct from 12-hour engineer credentials; pagination leaves ordering and cursor lifetime unspecified; ingest response and partial-batch semantics are absent; prepaid threshold equality and discount semantics conflict internally; provider-selection timing and request examples contain defects.
- Coverage after promotion: 25 Metronome source summaries ingested and 200 documentation pages pending.

## Routing conclusion

The standard-versus-strong metadata still described content complexity correctly, but model tier did not predict fixed-schema compliance in this sample. The existing fail-closed validator and bounded retry loop caught every malformed candidate before Sol review. A future campaign should retain the same simple routing and exact preflight assertions for canonical URL, top-level keys, and quote fields; it does not need a new classifier or more state machinery.
