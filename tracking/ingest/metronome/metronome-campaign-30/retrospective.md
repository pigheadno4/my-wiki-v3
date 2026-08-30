# Metronome Campaign 30 retrospective

## Result

- Started: `2026-08-30T09:30:10Z`
- Completed: `2026-08-30T10:18:13Z`
- Elapsed: 2,883 seconds (48 minutes 3 seconds)
- Final approval: 5/5
- First-pass approval: 3/5
- Worker attempts: 7
- Full reviews: 7
- Targeted reviews: 0
- Coordinator semantic repairs: 0

Final quality and the 9/9 fixed query audit passed. The campaign took 722
seconds longer than Campaign 29 and missed both throughput gates.

## What worked

- Get Invoice passed on attempt 1 while retaining fields under their immediate parent schemas and separating endpoint-local evidence from broader invoice behavior.
- Customer Controls passed on attempt 1 with explicit actors, actor-to-role mappings, and control boundaries intact.
- Create Billable Metrics passed on attempt 1 while preserving financial-unit and documentation-authority conflicts rather than resolving them by inference.
- Dynamic slots kept independent work moving without a batch barrier.
- The coordinator performed no semantic source repair and no additional complete raw-page review.

## What cost time

- Create Commit required a second complete worker read and complete review after its first candidate misstated conditional schedule requiredness, omitted a material timing ambiguity, and supplied incomplete shared-claim quote coverage.
- Stripe Invoice Integration required a second complete worker read and complete review after its first candidate misattributed the guide to Stripe and proposed webhook claims beyond the quoted evidence.
- Both corrections were material, so neither qualified for an unchanged-semantics targeted review.
- The fixed three-page closing audit remained an intentional quality cost.

## Recommendation

Do not add more reminders, prompt layers, validators, or tracking machinery.
Campaign 30 repeated Campaign 29's 3/5 first-pass result and increased full
semantic retries from one to two, so the extra reminders did not establish a
throughput improvement. Retain Minimum Sufficient Source and the existing
independent semantic-review boundary. Before another five-page campaign,
either pause to evaluate whether further per-page source refreshes justify
their cost, or run a smaller three-page calibration that changes the worker's
method rather than extending the checklist.
