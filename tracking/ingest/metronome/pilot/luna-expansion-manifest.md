# Metronome Luna Expansion Pilot Manifest

## Purpose

Evaluate GPT-5.6 Luna with high reasoning as the evidence-extraction tier on five new heterogeneous English-canonical Metronome pages. GPT-5.6 Sol remains the sole canonical editor, concept synthesizer, contradiction reviewer, and final approver.

## Fixed Run Order

| Cycle | Page type | Job | Raw page | Canonical source target |
| ---: | --- | --- | --- | --- |
| 1 | Long conceptual/financial guide | `pilot-luna-asc-606-revenue-recognition` | `raw/metronome/guides/reporting-insights/financial-reporting/asc-606-revenue-recognition-2026-07-13.md` | `wiki/sources/metronome/source-metronome-guides-reporting-insights-financial-reporting-asc-606-revenue-recognition.md` |
| 2 | Pricing concept guide | `pilot-luna-enterprise-commit` | `raw/metronome/guides/pricing-packaging/billing-model-guides/enterprise-commit-2026-07-13.md` | `wiki/sources/metronome/source-metronome-guides-pricing-packaging-billing-model-guides-enterprise-commit.md` |
| 3 | Integration workflow | `pilot-luna-stripe-invoice-integration` | `raw/metronome/integrations/invoice-integrations/stripe-2026-07-13.md` | `wiki/sources/metronome/source-metronome-integrations-invoice-integrations-stripe.md` |
| 4 | API reference | `pilot-luna-create-billable-metric` | `raw/metronome/api-reference/billable-metrics/create-a-billable-metric-2026-07-13.md` | `wiki/sources/metronome/source-metronome-api-reference-billable-metrics-create-a-billable-metric.md` |
| 5 | Long schema-heavy API reference | `pilot-luna-edit-contract` | `raw/metronome/api-reference/contracts/edit-a-contract-2026-07-13.md` | `wiki/sources/metronome/source-metronome-api-reference-contracts-edit-a-contract.md` |

Every job uses schema version 3, mode `real_ingest`, model `gpt-5.6-luna`, and reasoning effort `high`.

## Isolation and Serial Execution

- A Luna worker may write only to `tracking/ingest/metronome/pilot/runs/<job-id>/` for its assigned job.
- Every job forbids the shared files `wiki/companies/metronome.md`, `wiki/metronome-index.md`, `wiki/metronome-log.md`, `wiki/index.md`, and `wiki/log.md`, and forbids all writes under `raw/` and `wiki/`.
- Sol alone may edit canonical wiki pages and final receipts after reading the complete assigned raw file and completing the concept audit.
- Run the cycles in the fixed order above. Do not start a later cycle until the current cycle has passed all acceptance gates and its canonical changes have been committed.
- Apply a 900-second fail-fast limit to each Luna worker run. If the worker reaches the limit, stop that job, preserve its attempt and failure artifacts, and do not start the next cycle until the failure is reviewed and explicitly resolved.

## Acceptance Gates

A cycle may be canonically committed only when all of the following are true:

- The complete raw file was read and the concept audit was completed before canonical source creation or editing.
- The Luna artifacts preserve 3-5 exact grounding quotes, every attempt, failure reason, elapsed time, deterministic repair count, and available cumulative token usage.
- The promoted source has no critical omission, unsupported claim, unresolved contradiction, invalid raw link, failed validator, or unreviewed taxonomy recommendation.
- Tags are unique lowercase kebab-case values that include `metronome`; existing concept suggestions match the current `wiki/concepts/metronome/` inventory, while unknown concepts remain recommendations for Sol.
- The canonical source includes the dated raw snapshot in `raw_files:` and a path-qualified backlink under `## Raw Sources`.
- Deterministic defects such as tag normalization, raw-link formatting, and uniquely locatable quote bounds are repaired locally; ambiguous or semantic defects require Sol review.
- The job, worker artifacts, final receipt, touched wiki pages, and capsule reconciliation pass their applicable deterministic validators.

Failure of any gate blocks canonical promotion, the current cycle's commit, and every later cycle.
