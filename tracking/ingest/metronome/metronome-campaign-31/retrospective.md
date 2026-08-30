# Metronome Campaign 31 retrospective

## Result

- Started: `2026-08-30T11:28:09Z`
- Completed: `2026-08-30T12:12:08Z`
- Elapsed: 2,639 seconds (43 minutes 59 seconds)
- Final approval: 5/5
- First-pass approval: 3/5
- Worker attempts: 8
- Full reviews: 8
- Targeted reviews: 0
- Coordinator semantic repairs: 0

Final quality and the 9/9 fixed query audit passed. Campaign 31 was 244
seconds faster than Campaign 30, but remained too slow for five pages and
missed both throughput gates.

## What worked

- All five selections were previously never-ingested canonical pages, so every approved task increased current coverage instead of refreshing an already-covered source.
- ASC 606, billing-provider configuration, and custom-field deletion passed on the first attempt across three different page shapes.
- Dynamic slots allowed independent tasks and reviews to continue without a batch barrier.
- The coordinator applied approved shared updates once per target, performed no semantic source repair, and did not add a third full-source review.
- The fixed audit confirmed efficient source-to-raw and concept-to-source routing without expanding beyond the three planned pages.

## What cost time

- Create Custom Field Key needed a complete retry because the first candidate did not preserve the endpoint-enum, Customer-specific prose, and overview-list tension or separate their uniqueness authority precisely.
- Create Threshold Notification needed two complete retries. The first omitted conditional-field, response, uniqueness, and quote-coverage boundaries; the second still omitted the distinct Plan-or-Contract `/alerts/create` surface.
- Those were material semantic omissions, so targeted diff review was not safe.
- The final fixed audit and close checks were bounded and passed once; repeated mechanical testing was not the main cost.

## Recommendation

Keep prioritizing never-ingested canonical pages, because this produces new
query coverage. Keep the current Minimum Sufficient Source and independent
semantic review for complex mutation pages. Do not add process machinery.
For the next campaign, select fewer conflict-dense mutation pages in one group
or reduce the campaign to three pages when the sample contains a known
cross-surface API conflict; the evidence here does not justify weakening
semantic review.
