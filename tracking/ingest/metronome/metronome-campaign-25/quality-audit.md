# Metronome Campaign 25 Quality Audit

## Outcome

- Fixed audit sample: `edit-a-contract`, `get-a-threshold-notification`, and `sdks`.
- Query result: 3/3 pages and 9/9 checks passed.
- Expansion: not required; factual retrieval, material boundaries, exact raw navigation, and primary reciprocal links all passed.
- Shadow risk-review verdict: `inconclusive`. Every provisional page exposed at least one listed risk trigger during its complete worker read and was correctly escalated to mandatory full review, leaving no eligible simulated unreviewed release.

## Fixed query audit

| Page | Factual retrieval | Boundary or contradiction | Exact raw deep dive |
| --- | --- | --- | --- |
| `edit-a-contract` | Pass — retrieves required customer and contract identity, mixed component edits, finalized-invoice behavior, recurring-grant eligibility, threshold activation, and the response surface. | Pass — preserves undefined mixed-edit atomicity and recovery, charge-initiation versus payment, the `uniqueness_key` runtime-authority conflict, provider-transition conflict, and response-ID contradiction. | Pass — `Raw Sources` links to the exact path-qualified 2026-07-13 contract-edit snapshot. |
| `get-a-threshold-notification` | Pass — retrieves one customer/notification pair's current `ok`, `in_alarm`, `evaluating`, or archived-null state and retained alert configuration. | Pass — separates current state from history, preserves the `updated_at` narrative/schema conflict, and states that same-key POST replay is not proof of a fresh evaluation. | Pass — `Raw Sources` links to the exact path-qualified 2026-07-13 threshold-notification snapshot. |
| `sdks` | Pass — retrieves the four-language route from usage ingest through metrics, customer association, catalog pricing, contracts, and draft invoicing. | Pass — preserves generic retry versus event/API idempotency, the stale August 2024 chronology, the Go contract-start and grouping conflict, currency limits, and unproven propagation or downstream outcomes. | Pass — `Raw Sources` links to the exact path-qualified 2026-07-13 SDK reference snapshot. |

## Mechanical integrity

- All six raw SHA-256 values match the approved manifest.
- All six canonical source files are byte-identical to their reviewer-approved candidates.
- Each promoted source appears exactly once in `wiki/companies/metronome.md` and `wiki/metronome-index.md`.
- All reviewer-approved concept targets contain the required reciprocal source route.
- Targeted wiki validation passed for 27 files; capsule validation reports 225 raw pages, 151 source summaries, and 80 raw pages without source summaries.
- The single final unit suite passed 741 tests in 118.346 seconds, and `git diff --check` passed.

## Verdict

Campaign 25 passes real-source promotion quality for all six pages. Its shadow experiment does not approve reviewer sampling: escalation was safe but too broad to exercise an unreviewed release, so the result is inconclusive rather than pass or fail. No live Metronome sampling policy or cross-provider rollout is authorized.
