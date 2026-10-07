# Braintree C43 timing and next optimization

Runtime execution2026-10-07 10:59:37–11:50:39UTC:51m02s. C42 was53m42s: C43 is2m40s (5.0percent) shorter. Primary raw volume fell from68,960 to22,468words (67.4percent), while first independent-review pass improved34/50→45/50 (68→90percent). This heterogeneous comparison is not proof of a model/concurrency speedup. Post-completion close-report writing is outside the runtime field.

## Overlapping stage windows

| Stage | UTC window | Measurement |
| --- | --- | --- |
| Worker orders/drafting/corrections |10:59:37–11:41:48|55matched valid artifacts: attempt-directory birth to external artifact modification; median103s, maximum186s; includes dispatch/queue overhead|
| Independent review/corrections |11:01:58–11:46:24|Trusted review-input modification to external review modification; full50median99s, maximum177s; targeted6median62s, maximum78s|
| Promotion |11:07:36–11:47:02|Canonical source birth window, overlapping workers/reviews/queries|
| Query evidence |First report saved11:15:25; final report saved11:50:15|13groups/100questions; save window is not active auditor duration|
| Shared aggregation/structural and typed close |Approximately11:47–11:50:39|About3m39s, overlapping final audits; catalogs/counts/logs once, one structural check and one64-file typed validation|

Windows overlap and cannot be added. Existing filesystem endpoints are approximate lifecycle evidence, not token usage or pure model compute. One Apple Pay attempt-2 external worker artifact was unavailable as a separate file; its accepted receipt/review remain, so worker timing covers55of56valid candidates. Some auditor self-reported starts precede observed dispatch, so report timestamps are not used to claim precise active audit duration. No new timing schema or monitor was introduced.

Valid matched worker artifact-to-receipt wait median110s, maximum288s (C42:118s/303s). First review median99s (C42:119s); worker median103s (C42:92s), targeted median62s (C42:43s). These endpoints include orchestration/queue effects and do not isolate model latency. Handoff delay remains comparable to the initial review's entire measured duration.

## Corrections

Five initial reviews requested changes: Apple Pay web/native certificate scope; Node-routed Ruby/Python/PHP migration applicability; Shopper Insights availability and consent subject; customer-delete recurring-subscription cascade; payment-app restart versus device reboot and diagnostics Sandbox/Production version boundary. Apple Pay needed a second narrow phrase fix because version-family documentation was called exact-version evidence. Six targeted reviews total; no repeated full review.

The troubleshooting correction introduced a supporting-release quote into the runtime's primary-only quote list. That handoff failed mechanically; attempt3 removed only the supplemental quote/index, preserved source/concept wording and fully read supporting provenance, then passed targeted review. Seven retry worker starts include this mechanical correction. No query source amendment or reviewer JSON schema repair.

## Small next steps, no new framework

1. Prioritize ready result acceptance and immediate trusted-order dispatch before report copying or narration. The110s median wait is still the strongest measured orchestration opportunity; retain the existing rolling scheduler and artifact-path tracking, not another queue system.
2. Keep reports outcome-first and compact: shared pin/route checks once, two short answers plus exact locators per page, no repeated disclaimer inventory. Retain required evidence reads and all100approved questions; do not add tests or audit layers.
3. Sources still total24,328words against22,468raw words, versus C42's29,999source words. Word count alone is distorted by compact code/raw formatting, but inspection shows repeated non-proof lists and long reciprocal labels. Future approved drafting can use one scope-boundary paragraph and genuinely one-line concept routes, retaining each consequential local condition/warning. Do not rewrite C43's approved content merely for style.
4. For supporting authority, retain full-read path-qualified provenance but keep the three-to-five receipt quotes in the primary raw, as required by the current runtime. Use the existing role reminder, no schema/parser change or invariant registry.

Commit/push and next manifest preparation/execution require separate approval. Deferred heavy validation-errors-all-node remains unchanged;146previously unreferenced successful variants remain after these50new primary sources.
