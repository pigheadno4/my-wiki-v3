# Braintree C39 timing and observations

Status: complete. Runtime2026-10-04T14:34:14Z–15:03:53Z, total29m39s. No commit/push or C40 authority.

## Observed stage windows

Wall-clock milestone tails, not additive worker/reviewer costs; roles overlap.

| Window | Elapsed |
| --- | --- |
| Initialization → last initial worker handoff14:51:00Z |16m46s|
| Remaining initial-review tail →14:54:58Z |3m58s|
| Context restoration, concept/source promotion, audit dispatch and aggregate catalogs →15:00:12Z observation |5m14s|
| Remaining query-analysis tail →15:01:58Z |1m46s|
| Report-writing/handoff tail →15:02:46Z |48s|
| Coordinator persistence, typed checks and runtime close →15:03:53Z |1m07s|
| Total |29m39s|

- First pass19/20. Twenty full initial reviews, one targeted correction/review, no repeated full review. NAB fee correction approved14:46:43Z while unrelated jobs continued, so it is not an additional final correction tail. No schema-rejected handoff, thread-limit failure, formatter repair or coordinator semantic repair.
- All20 sources promoted unchanged after approved concept updates; seven existing concepts, no new concept. One approved durable fee-outcome qualification is source-cited in disputes; other changes are reciprocal retrieval routes. Catalog452=435website+17GitHub.
- Forty fixed queries passed. Provider-qualified dispatch avoided C38's wrong-provider rework. Auditor-reported analysis/handoffUTC: A15:01:01/15:02:10; B15:00:28/15:01:17; C15:01:58/15:02:46; D15:01:46/15:02:40; E15:01:45/15:01:45. These are report timing notes, not separate per-agent CPU costs or proof of released thread capacity.
- Primary raw1953lines/13604words; source10902words. C38 raw14638/source13458words. Source output decreased2556words (19.0percent), whereas primary raw words decreased7.1percent; output/raw ratio80.1percent versus91.9percent. This is consistent with less repeated caveating, but different content prevents a causal or equal-work performance claim. No accepted page was shortened merely to meet a cap.
- Total29m39s versus C38's30m21s:42seconds faster (2.3percent), not a substantial speedup. Worker handoff was1m47s later; final initial-review tail was58seconds shorter; the post-review promotion/context/catalog interval was longer. Smaller output did not remove orchestration and coordinator latency.

## Small next improvement, not new machinery

Use the already authorized incremental concept-before-source promotion more promptly after a ready review is accepted and available role slots are filled. In this round promotion was deferred until all twenty reviews had finished; five query groups therefore started late rather than overlapping earlier ready groups. Dispatch each ready four-page audit group once its routes exist and a shared slot is free. Keep ten shared rolling slots, exact candidates, independent first review and forty questions unchanged. Avoid rereading already-loaded governance after a handoff when valid context is retained; retain required reads after genuine context loss. Prepare group prompts from pinned selection once and avoid long retrospective prose during live dispatch. No scheduler, timing fields, monitoring system or extra validator is needed.

Preserve the successful scope placement: identity once, central action with local conditions, each unique warning once, raw detail locators, concise concept routes. Some concept suggestions remain long, but do not rewrite accepted suggestions now or introduce another shortening/review loop. Further changes require separate campaign approval.
