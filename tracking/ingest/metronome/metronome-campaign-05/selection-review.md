# Metronome Campaign 05 Selection Review

Status: `complete`

Manifest: [manifest.json](manifest.json)

This bounded follow-up tests the Campaign 04 worker-handoff preflight on short, medium, schema-heavy, and unusually long pages. Selection used only `inventory-current.json`, raw paths, byte hashes, line counts, and existing source coverage. No raw body was read while preparing this proposal.

## Proposed jobs

| Order | Job | Page shape | Lines | Recommended tier | Routing reason |
| ---: | --- | --- | ---: | --- | --- |
| 1 | `idempotency` | API-wide convention | 86 | `standard` | Short idempotency convention without a resource schema. |
| 2 | `status-codes` | API-wide convention | 48 | `standard` | Short response convention without a resource lifecycle. |
| 3 | `create-billable-metrics` | Core metering guide | 130 | `strong` | Metering configuration semantics affect downstream aggregation and pricing. |
| 4 | `create-a-customer` | Customer API reference | 393 | `strong` | Schema-heavy provisioning with identity and billing configuration fields. |
| 5 | `amend-a-contract` | Contract API reference | 1,133 | `strong` | Long contract mutation schema with financial lifecycle and timing implications. |

Total selected raw lines: 1,790.

## Deterministic selection checks

- All five entries are selected English `page` records in `tracking/collections/metronome/inventory-current.json`.
- Every raw file exists and its SHA-256 matches the manifest.
- Every canonical URL matches the inventory.
- None of the five raw paths is referenced by an existing canonical Metronome source page.
- All five source targets are unique and do not exist.
- Routing metadata uses only `standard` or `strong`, with a non-empty reason.
- The proposal contains two standard jobs and three strong jobs.

## Proposed execution boundary

- Keep the current portable `standard` and `strong` routing; do not add another classifier.
- Start at most three native workers concurrently because the Sol coordinator occupies the fourth agent slot.
- Refill each available slot immediately; do not wait for a batch barrier.
- Each worker receives the generated self-contained order, reads exactly one complete raw file, and returns only its isolated fixed-schema candidate.
- Every worker runs the order's canonical URL, top-level-key, and quote-field preflight before submission.
- The Sol coordinator performs serial full-raw review, concept audit, promotion, reverse-link reconciliation, contradiction checks, and deterministic validation.
- Invalid results retain evidence and may retry up to three total attempts without pausing unrelated jobs.
- Shared company, concept, index, log, and campaign tracking files remain coordinator-owned.

## Success measure

Content quality still requires full Sol review. The handoff correction is considered useful if this campaign completes with fewer than Campaign 04's five mechanical validator failures, especially zero canonical-URL, extra-key, or missing-quote-location failures.

The user approved this exact proposal on 2026-07-30 before campaign initialization and worker launch.

## Execution result

- Routing: the two `standard` jobs ran on native GPT-5.6 Terra; the three `strong` jobs ran on native GPT-5.6 Sol.
- Scheduling: at most three workers ran concurrently, and freed slots were refilled immediately without a batch barrier.
- Worker boundary: every worker read exactly one complete raw page and wrote only an isolated fixed-schema result under `/private/tmp`.
- Review: the Sol coordinator reread all five raw pages in full, performed concept-first promotion, reconciled forward and reverse links, checked contradictions, and validated every promoted source.
- Final result: 5 approved jobs, 0 failed attempts, 0 retries, and 0 rejected jobs. Every job completed on attempt 1.
- Coverage after promotion: 30 Metronome source summaries ingested and 195 documentation pages pending.

## Preflight conclusion

Campaign 04 recorded five mechanical validator failures; Campaign 05 recorded zero across short, medium, schema-heavy, and 1,133-line inputs. The self-contained canonical URL, exact top-level-key, and quote-field handoff is therefore retained.

This does not reduce the Sol content-review gate. Full rereads still added or repaired a platform idempotency concept, two reciprocal documentation tensions, request-body and response-ID boundaries, customer-configuration caveats, credit-selector ambiguity, and legacy amendment atomicity/error-cache unknowns.
