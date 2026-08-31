# Metronome Campaign 32 retrospective

## Result

- Started: `2026-08-31T11:05:26Z`
- Completed: `2026-08-31T12:09:53Z`
- Elapsed: 3,867 seconds (1 hour 4 minutes 27 seconds)
- Final approval: 5/5
- First-pass approval: 2/5
- Worker attempts: 8
- Full reviews: 7
- Targeted reviews: 1
- Coordinator semantic repairs: 0

Final quality and the 9/9 fixed query audit passed. Campaign 32 was 1,228
seconds slower than Campaign 31 and missed both throughput gates.

## What worked

- All five selections were previously never-ingested canonical pages, so every approved task increased current query coverage.
- Invoice Breakdowns and Embeddable Customer Dashboard passed their first complete reviews, including the 1,150-line schema-heavy control.
- The alias correction qualified only for targeted review: its source candidate and evidence stayed byte-identical while three shared-proposal sentences were corrected.
- Dynamic slots kept unrelated work and review moving without a batch barrier.
- The coordinator promoted only approved candidates and shared proposals, performed no semantic source repair, and did not repeat full-source review.
- The fixed audit confirmed source-to-raw and concept-to-source-to-raw navigation without expanding beyond the three planned pages.

## What cost time

- The alias attempt overstated the undocumented HTTP 200 response as empty rather than saying no response content schema or example is provided.
- Archive Billable Metric needed a full retry to narrow the generic response ID, ground the operation with exact quotes, attribute Product effective dating correctly, and retain the archive-versus-Get metering conflict.
- Guarantee Zero Overages needed a full retry to add the usage-based-billing route, directly ground the literal `price: 100` versus `100 USD/unit` conflict, and link the exact currency and invoice authorities.
- Those two latter defects were material authority or evidence gaps, so targeted review was not safe.
- The bounded promotion, 9/9 fixed audit, and single close validation were not repeated; the dominant cost remained complete semantic retries and their independent reviews.

## Recommendation

Continue prioritizing never-ingested canonical pages, but do not interpret the
mixed-page selection as a throughput improvement. Retain targeted diff review
for unchanged-hash wording or metadata corrections and full review for factual,
authority, contradiction, or material-omission repairs. For the next campaign,
use five pages only if breadth is more important than elapsed time; the current
evidence says a three-page campaign is the safer way to shorten wall-clock time
without weakening semantic review.
