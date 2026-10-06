# Braintree C40 timing and observations

Complete:2026-10-05T00:48:27Z–01:46:23Z,57m56s. Fifty pages, ten shared rolling child slots. No commit/push or next-campaign execution.

## Stage windows

Overlapping wall-clock windows, not additive per-agent CPU costs. Receipt/review acceptance endpoints below are local artifact mtimes, not exact worker reasoning completion times.

| Window | Elapsed |
| --- | --- |
| Start → last initial receipt accepted01:38:47Z |50m20s|
| Remaining full/targeted acceptance tail →01:41:31Z |2m44s|
| Final promotion/catalog milestone observed01:43:14Z |1m43s|
| Remaining fixed-query/report tail →01:45:18Z |2m04s|
| Report persistence, log, typed verification and runtime close →01:46:23Z |1m05s|
| Total |57m56s|

- Incremental promotion began before initial work completed: first canonical group observed00:57:31Z, another set01:01:55Z. GroupA query analysis ended01:06:04Z, handoff01:06:57Z; later workers/reviewers were still running. Query groups continued overlapping ingestion. Aggregate catalogs were updated once. No thread-limit failure was encountered.
- Query analysis/handoffUTC, as reported: A01:06:04/01:06:57; B01:15:35/01:16:35; C01:19:34/01:20:28; D01:23:35/01:24:36; E01:25:59/01:27:12; F01:29:28/01:30:30; G01:30:39/01:30:39; H01:35:59/01:35:59; I01:38:19/01:38:19; J01:43:43/01:43:43; K01:44:18/01:45:18; L01:44:14/01:44:14; M01:44:05/01:44:05. Equal timestamps mean no separately reported interval, not zero report cost.
- First pass35/50 (70percent) versus C39's19/20. Fifteen bounded corrections used targeted reviews, no repeated full rereview. Rejections concerned real cross-source conflicts, actor/region/time qualifications, input-versus-consumption, supplied-ID error conditions, a registration-action condition, overbroad unread-CSV disclaimers and one undiscoverable fee section. One proposed cross-API unknown-consequence requirement was reconsidered and removed before runtime acceptance; no unnecessary source expansion followed.
- Raw66844words versus C39's13604 (4.91times);50pages versus20 (2.5times). Total57m56 versus29m39 (1.95times). Mean wall-clock/page69.5s versus89.0s, about21.8percent lower, but content and page lengths differ, so this is not a controlled concurrency or model benchmark.
- Source31887words,47.7percent of primary raw, versus C39's80.1percent. Long tables/example payloads stayed in raw; exact purpose, qualifications and warnings remained in retrieval entries. No hard cap or accepted-page shortening loop.
- Final review acceptance→close4m52s, compared with C39's roughly8m55s after its last initial-review handoff. Different endpoint definitions prevent an exact causal comparison, but early query overlap removed the previous all-reviews-first audit start. Main rolling orchestration remains serialized and can still delay ready handoffs; total workload and historical conflict discovery dominate this larger round.

## Small next optimization

Keep the current rolling pool and early ready-query overlap; do not add a scheduler, registry or more audits. Reuse compact provider-qualified role prompts. In the existing bounded pre-handoff check, distinguish input from consumption, missing input from missing object, intended registration from prior registration, and navigation-only CSV limits from facts explicitly stated in landing prose. For retained historical release/eligibility claims, inspect the already-routed sibling summary for known conflicts instead of importing every sibling detail. Preserve one discoverable locator per central section, including Fees. These are findings for the next approved campaign, not new rule or code changes in C40.
