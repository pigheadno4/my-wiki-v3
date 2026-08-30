# Metronome Campaign 29 retrospective

## Result

- Started: `2026-08-30T07:30:51Z`
- Completed: `2026-08-30T08:06:52Z`
- Elapsed: 2,161 seconds (36 minutes 1 second)
- Final approval: 5/5
- First-pass approval: 3/5
- Worker attempts: 7
- Full reviews: 6
- Targeted reviews: 1
- Coordinator semantic repairs: 0

The campaign completed 225 seconds slower than Campaign 28 and missed the
non-binding 35-minute observation target by 61 seconds. Final quality and the
9/9 fixed query audit passed. The full-retry limit passed, while the
first-pass-rate gate did not.

## What worked

- Both API controls passed on attempt 1. List Invoices kept fields under their immediate parent schemas and separated response-envelope, top-level invoice, nested-object, List, Get, and mutation authority. Edit Commit retained exact financial names and unknown units while separating commit identity from API-wide POST idempotency.
- Avalara passed on attempt 1 with its cross-system tax, invoice, support, correction, and reconciliation boundaries intact.
- The targeted retry rule avoided another full Reporting review: its candidate and shared prose were already correct, so only five quote ranges were repaired and rechecked.
- Dynamic slots kept work moving without a batch barrier, and three approved sources were promoted while the remaining review loops continued.
- The coordinator performed no semantic source repair and no default third full raw read.

## What cost time

- The 1,144-line List Invoices raw remained the campaign's longest complete read and review, although placing it in the first wave contained its tail latency.
- In-app Reporting required a second worker turn because its excerpts did not cover every retained report, dashboard, and ARR claim. The targeted re-review limited the added cost.
- RBAC required a second complete worker read and complete review because the first candidate preserved permissions but omitted the page's intended actor for each built-in role.
- The fixed three-page closing audit remained an intentional quality cost.

## Recommendation

Keep the five-page campaign size. Retain the two API reminders because their
controls passed first try. Add only two bounded brief reminders for the next
mixed sample: cover every retained shared-file claim with the selected quote
ranges, and preserve source-defined principal actors for guide or security
pages. Do not change the scheduler, result schema, monitoring system, or model
route, and do not add another validation layer.
