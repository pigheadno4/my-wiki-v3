# Metronome Campaign 33 retrospective

## Result

- Started: `2026-08-31T12:55:25Z`
- Completed: `2026-08-31T14:15:50Z`
- Elapsed: 4,825 seconds (1 hour 20 minutes 25 seconds)
- Final approval: 5/5
- First-pass approval: 2/5
- Worker attempts: 9
- Full reviews: 9
- Targeted reviews: 0
- Coordinator semantic repairs: 0

Final quality and the 9/9 fixed query audit passed. Campaign 33 was 958
seconds slower than Campaign 32 and missed every throughput target.

## What worked

- All five selections were previously never-ingested canonical pages, so every approved task increased current query coverage.
- Update a Billable Metric and Get Customer Costs passed on their first complete reviews.
- Dynamic slots kept ready reviews and queued workers moving without a batch barrier.
- The coordinator promoted only approved candidates and shared proposals, performed no semantic source repair, and did not repeat full-source review.
- The fixed audit confirmed source-to-raw and concept-to-source-to-raw navigation without expanding beyond the planned three pages.

## What cost time

- Subscription Seats History needed one complete retry for the missing reporting-and-analytics primary route.
- Historical Invoices needed one complete retry for open-object authority, the migration-guide versus OpenAPI custom-usage-line boundary, and direct operation/response quote grounding.
- Alert Specifiers needed two complete retries. The first restored all-customer/current-and-future promotion scope, uniqueness versus request replay, currency-unit limits, and freshness. The second preserved the guide example's `alert_type`, `status: active`, and missing `updated_at` conflict with the current get schema.
- Two initial reviewer artifacts included provenance fields that belong only in persisted evidence. The same reviewers removed those fields without changing their semantic verdicts; later reviewer dispatches stated the exact eight-key input contract.
- Promotion, the 9/9 fixed audit, and closing validation ran once. Complete semantic retries and full re-reviews remained the dominant cost.

## Recommendation

Keep five pages because that is the chosen production-pressure sample, but do
not claim that the one-high-plus-four-medium mix improves speed. Carry only the
concrete Campaign 33 lessons into worker briefs: audit every primary concept,
compare guide examples against current dedicated schemas, distinguish open
schemas from accepted fields, and ground query-critical response placement.
Keep the existing scheduler and validators unchanged.
