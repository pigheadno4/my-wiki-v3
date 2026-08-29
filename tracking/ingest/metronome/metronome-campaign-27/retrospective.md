# Metronome Campaign 27 retrospective

## Result

- Started: `2026-08-29T02:47:40Z`
- Completed: `2026-08-29T03:18:27Z`
- Elapsed: 1,847 seconds (30 minutes 47 seconds)
- Final approval: 5/5
- First-pass approval: 4/5
- Worker attempts: 6
- Full reviews: 6
- Targeted reviews: 0
- Coordinator semantic repairs: 0

Compared with Campaign 26's 2,698 seconds and two first-pass approvals,
Campaign 27 finished 851 seconds faster (about 31.5%) and doubled first-pass
approvals to four. It missed the non-binding 30-minute observation target by
47 seconds while meeting every quality gate.

## What improved

- Bounded representative pages avoided another longest-page stress sample
  while retaining one 433-line schema-heavy control.
- Job-specific reminders prevented schema-scope generalization and unsafe
  shared-passage replacement. Get Product correctly kept
  `include_composite_spend` drift source-scoped to the Get snapshot.
- Dynamic slots kept review moving without a batch barrier, and incremental
  promotion let the coordinator apply approved concept updates while unrelated
  jobs continued.
- Review remained useful rather than ceremonial: Authentication caught two
  material conflicts, and one full retry resolved both. The other four pages
  passed on their first attempt.
- The coordinator performed no third full raw read and no semantic repair.

## Remaining cost

The single Authentication retry required a second worker full read and a
second reviewer full read. The fixed three-page close audit also remained an
intentional quality cost. One reviewer result initially included two metadata
keys owned by the coordinator; the same reviewer removed only those keys
without repeating semantic work.

Only campaign-level `started_at` and `completed_at` were recorded, so this
retrospective does not claim precise per-stage timing. No timing registry,
scheduler feature, or additional monitoring layer is warranted from this
five-page result.

## Recommendation

Treat the Campaign 27 brief as a successful Metronome-local first-pass
calibration. Before changing global PSP rules or increasing campaign size,
reuse the same bounded reminders in one more representative Metronome campaign
and compare first-pass rate and elapsed time. Do not remove independent
per-page review on the strength of this sample.
