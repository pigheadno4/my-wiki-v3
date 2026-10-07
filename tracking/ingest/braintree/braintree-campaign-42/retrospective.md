# Braintree C42 timing and next optimization

Runtime execution:00:34:33–01:28:15 UTC,53m42s. C41:62m39s; C42 is8m57s (14.3percent) shorter despite6.9percent more raw words. This is one heterogeneous campaign, not proof of a model or concurrency speedup. Close evidence/report preparation after runtime completion is outside that field.

## Overlapping stage windows

| Stage | Observed UTC window | Measurement |
| --- | --- | --- |
| Worker orders/drafting/corrections |00:34:33–01:22:08|Attempt-directory birth to external artifact modification; valid receipt attempt median92s, maximum399s, includes dispatch/queue overhead rather than pure model time|
| Independent review/corrections |00:37:25–01:25:02|Trusted review input modification to external review artifact modification; full median119s, targeted median43s|
| Promotion |00:39:44–01:25:22|Canonical source file birth window; overlaps drafting/review/audits|
| Query evidence |First report saved00:54:00; final audit completed01:27:44|13groups,100questions; report-save start is not auditor-start time; some self-reported earlier timestamps are unreliable|
| Shared aggregation/structural and typed close |Approximately01:25:25–01:28:15|About2m50s; catalogs/counts once, one completed structural check and one65-file typed validation|

These windows overlap and must not be added. File endpoints are approximate lifecycle evidence, not token usage, CPU time or exact active-model duration. Replaced input files have unsuitable birth times for worker starts; attempt-directory creation was used instead. Review-schema repairs alter external artifact modification times. No new timing schema or monitoring framework was added.

Valid worker artifact-to-receipt wait median118s, maximum303s. This includes coordinator processing and active-slot turnover; it does not establish a model latency problem.67worker starts include one stale-artifact recovery;66valid receipts and66reviews remain. First-review pass34/50 (68percent), versus C41's43/50 (86percent); C41 end-to-end first pass41/50 is a different metric.

## Corrections and cost

Sixteen first reviews requested targeted corrections: quotation locators, repeated-code mapping ambiguity, coupled local conditions, softened claim scope, unresolved captured/support conflicts, and concept-route ownership. No second full review was run. Group D's3source changes were checked only on affected questions and unchanged pins. Group H's2illustrative syntax observations were adjudicated nonblocking; no source expansion or full rerun. Three review JSON shape fixes required only mechanical resubmission. One root stale-object artifact-selection mistake caused an extra worker attempt with identical substantive content, not worker quality failure.

## Small next steps only

1. Prioritize ready artifact acceptance and persisted-order dispatch before narrative or report copying; keep artifact-path keyed logical tracking. The observed handoff wait is comparable to an initial review's active duration, so this is the strongest immediately visible opportunity. Do not build another scheduler or journal.
2. Use a short provider/context reminder for this recurring SDK family: preserve captured version/certificate language and exact operation/subject, keep related-product contrasts out of primary concept evidence, and retain each coupled condition. Reuse existing role guidance; no large invariant registry or new review layer.
3. Continue targeted-only corrections for bounded changes. Require a concrete false claim/material warning/query failure before treating illustrative raw code syntax as a source blocker. Do not make retrieval sources into runnable-code certifications.
4. Do not increase concurrency or sample size based solely on this result. Next manifest preparation/execution and commit/push require separate approval. Keep full initial evidence reads and meaningful reciprocal links; avoid another optimization framework.
