# Metronome Terra Comparison Pilot Manifest

## Purpose

Compare GPT-5.6 Terra with the completed GPT-5.6 Luna pilot using five new English-canonical Metronome pages. Terra drafts all five pages; Luna shadows the shortest and longest pages. GPT-5.6 Sol remains the sole canonical promoter and final approver.

## Fixed Run Order

| Order | Job | Mode | Model / reasoning | Raw page | Canonical target |
| ---: | --- | --- | --- | --- | --- |
| 1a | `pilot-luna-design-usage-events-shadow` | shadow | Luna / high | `guides/events/design-usage-events-2026-07-13.md` | evidence only |
| 1b | `pilot-terra-design-usage-events` | real ingest | Terra / medium | `guides/events/design-usage-events-2026-07-13.md` | `source-metronome-guides-events-design-usage-events.md` |
| 2 | `pilot-terra-enterprise-commit` | real ingest | Terra / medium | `guides/pricing-packaging/billing-model-guides/enterprise-commit-2026-07-13.md` | `source-metronome-guides-pricing-packaging-billing-model-guides-enterprise-commit.md` |
| 3 | `pilot-terra-stripe-invoice-integration` | real ingest | Terra / medium | `integrations/invoice-integrations/stripe-2026-07-13.md` | `source-metronome-integrations-invoice-integrations-stripe.md` |
| 4 | `pilot-terra-create-billable-metric` | real ingest | Terra / medium | `api-reference/billable-metrics/create-a-billable-metric-2026-07-13.md` | `source-metronome-api-reference-billable-metrics-create-a-billable-metric.md` |
| 5a | `pilot-luna-edit-contract-shadow` | shadow | Luna / high | `api-reference/contracts/edit-a-contract-2026-07-13.md` | evidence only |
| 5b | `pilot-terra-edit-contract` | real ingest | Terra / medium | `api-reference/contracts/edit-a-contract-2026-07-13.md` | `source-metronome-api-reference-contracts-edit-a-contract.md` |

All raw paths are rooted at `raw/metronome/`. All worker artifacts are rooted at `tracking/ingest/metronome/pilot/runs/<job-id>/`. Workers forbid writes under `raw/` and `wiki/`.

## Execution Rules

- Finish the complete Sol-reviewed canonical cycle for one raw page before starting the next raw page.
- Paired shadows may run before their Terra counterpart but never update wiki coverage.
- Preserve all attempts and use cumulative, not accepted-attempt-only, token accounting.
- Repair uniquely locatable quote bounds deterministically; never rerun the whole model for a quote-location-only defect.
- Every promoted source includes its dated raw snapshot in frontmatter and under `## Raw Sources`.

## Acceptance Gates

- Zero critical omissions or unsupported claims in promoted canonical pages.
- No quote-only full-model regeneration.
- Complete per-attempt validation reasons and cumulative token accounting for all seven jobs.
- No more than 10 total Sol repairs across the five Terra pages (2/page average).
- No more than 41.3 total Sol repair minutes across the five Terra pages (30% below the original Luna pilot's 59 minutes).

If Terra misses a quality gate, the report must recommend page-type routing, retaining Luna, or stopping cheap-model scale rather than making Terra the default.
