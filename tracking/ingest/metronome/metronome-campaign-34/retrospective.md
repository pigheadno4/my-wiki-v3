# Metronome Campaign 34 retrospective

## Result

- Started: `2026-08-31T15:08:01Z`
- Completed: `2026-08-31T16:41:05Z`
- Elapsed: 5,584 seconds (1 hour 33 minutes 4 seconds)
- Final approval: 5/5
- First-pass approval: 1/5
- Worker attempts: 12
- Full reviews: 12
- Targeted reviews: 0
- Coordinator semantic repairs: 0

Final quality and the 9/9 fixed query audit passed. Campaign 34 was 759
seconds slower than Campaign 33 and missed every throughput target.

## What worked

- All five selections were previously never-ingested canonical pages, so every approved task increased current query coverage.
- Archive Product passed its first complete review; Customer Configuration passed on attempt 2.
- Dynamic slots kept independent work moving without waiting for a five-job batch barrier.
- The coordinator promoted only approved candidates and reviewer-approved shared proposals, performed no semantic source repair, and did not repeat full-source review.
- One close validation and the fixed three-page audit confirmed source-to-raw and reciprocal concept navigation without expanding the audit.

## What cost time

- Dashboard, Usage Groupings, and Alert List each needed two complete retries; Customer Configuration needed one.
- A repeated cross-page omission caused avoidable retries: API-wide `Idempotency-Key` result persistence begins only after validation passes and no pre-execution concurrent request prevents execution. The final sources now preserve that admission boundary.
- Dashboard's second review found additional material defaults and response-shape boundaries after an earlier review had already requested changes, so the planned blocker-completeness calibration failed.
- Dashboard also required reconciliation across seven authority clusters; Usage Groupings needed window, `LATEST`, pagination, and event-route corrections; Alert List needed alert-type, example, current-create, cursor, and webhook distinctions.
- The persisted scheduler assigned reviewer identity `c34_r_usage_a3` to two reviewing jobs. Actual reviews were safely serialized or handled by distinct agents, so this was a monitoring-identity defect rather than a content-integrity failure.
- Complete semantic retries and complete re-reviews remained the dominant cost. Promotion, fixed audit, and closing validation ran once.

## Recommendation

Keep the current files and validators unchanged. Add only the concrete
idempotency execution-admission sentence to future Metronome worker briefs and
ensure one reviewer identity is not persisted against two simultaneous review
states. Treat both as small corrections, not a new framework. The campaign
proves final quality but does not justify scaling the present five-page method
for speed; the remaining 60 never-ingested pages need a separate, explicitly
approved throughput decision.
