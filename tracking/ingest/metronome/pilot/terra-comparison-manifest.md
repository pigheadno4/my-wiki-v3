# Metronome Terra Comparison Pilot Manifest

## Purpose

Compare GPT-5.6 Terra with the completed GPT-5.6 Luna pilot using five new English-canonical Metronome pages. Terra drafts all five pages; Luna shadows the shortest and longest pages. GPT-5.6 Sol remains the sole canonical promoter and final approver.

## Current Execution Status

**BLOCKED after job 1a — job 1b and all later jobs remain unstarted.**

On 2026-07-21, replacement health probe `luna-health-2026-07-21-01` passed the
strict gate. Job 1a then ran once under immutable run ID
`luna-design-usage-events-shadow-20260721-01`. The worker read the complete 88-line raw
file, but Luna produced no model message or terminal JSON after the raw-read tool result.
The worker enforced its 900-second cap, sent `SIGTERM`, observed clean process and pipe
termination without escalation, published a failed receipt, and reconciled the terminal
artifact manifest.

This failure has no model output that can be repaired deterministically. Do not retry job
1a or start job 1b until the failure is explicitly reviewed and a new action is approved.

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

## Health Probe Gate

All seven jobs above are registered by exact manifest path and SHA-256 in the
legacy-named `enterprise-diagnostic-jobs.json` registry. The registry also retains the
historical `pilot-luna-enterprise-commit` job, so it contains eight protected entries in
total. The filename and schema field names remain unchanged to avoid changing the gated
worker code solely for terminology.

Every comparison worker invocation must provide both a unique `--run-id` and
the current passing health-probe run ID. The latest passing probe is
`luna-health-2026-07-21-01`. Before claiming a run directory or
launching a model, the worker reconciles its own immutable registry entry and revalidates
the probe's freshness, runner provenance, artifacts, hashes, timing, and terminal receipt.
A missing, stale, future-dated, tampered, or provenance-mismatched probe blocks that job.

The registry defines protected identity, not permission to batch. This manifest's fixed
order and the one-source-at-a-time canonical review boundary still control execution.

## Execution Rules

- Finish the complete Sol-reviewed canonical cycle for one raw page before starting the next raw page.
- Start only one listed job at a time; never have a coordinator launch all seven jobs automatically.
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
