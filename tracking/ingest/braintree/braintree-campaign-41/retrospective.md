# Braintree C41 timing and observations

Complete:2026-10-06T14:39:50Z–15:42:29Z,62m39s. Fifty pages and ten shared rolling child slots. No commit/push or next-campaign execution.

## Stage windows

Overlapping wall-clock windows, not additive per-agent CPU or token costs. Receipt/review acceptance endpoints are local artifact mtimes, not exact reasoning completion times. Initial attempt-1 receipt endpoint excludes the two mechanically rejected initial handoffs.

| Window | Elapsed |
| --- | --- |
| Start → last accepted attempt-1 receipt15:30:17Z |50m27s|
| Remaining first-review and targeted-correction acceptance tail →15:37:11Z |6m54s|
| Remaining promotion/catalog and fixed-query handoff tail →15:40:32Z |3m21s|
| Report persistence, shared logs, mechanical checks and runtime close →15:42:29Z |1m57s|
| Total |62m39s|

- First canonical source promotion at14:56:36Z; last at15:37:11Z. Query A completed15:05:55Z while later workers/reviewers were active. Approved concept routes preceded sources; company/provider catalogs and counts were aggregated once. No observed thread-limit failure. Completed agents are not proof of host-level thread release; the available interface exposes status, not a close operation.
- Query analysis/handoff UTC: A15:05:55/15:05:55; B15:12:14/15:12:14; C15:12:43/15:12:43; D15:14:30/15:14:30; E15:16:57/15:16:57; F15:18:45/15:19:57; G analysis15:22:11; H15:22:28/15:22:28; I15:23:59/15:25:23; J15:32:55/15:34:12; K15:38:43/15:39:11; L15:39:10/15:40:32; M15:39:14/15:39:58. Equal timestamps mean no separately recorded report interval, not zero report cost.
- End-to-end first pass41/50(82percent), versus C40's35/50(70percent). Independent initial-review pass43/50(86percent). Seven bounded corrections used targeted review, zero repeated full review. They preserved prompt-specific input/enablement, offline provider-provisioning and transaction-field scope, Fastlane locator ranges, historical iPhone/environment qualification, ping prose/example and variable-consumption inconsistencies, account-model labeling conflict, and Function-selector versus token semantics.
- Two mechanical initial handoff failures involved quotes normalized away from raw: inline Markdown links in Partners Overview, and multiline spacing in M400. Both were repaired in attempt2 before their first independent full review; neither was a semantic reviewer retry. Original artifacts and failure events remain available.
- Raw64522words,3.5percent less than C40's66844. Sources32542words,50.4percent of raw, versus C40's47.7percent. No hard length cap or post-approval source-shortening pass. New In-Person and Custom Prompts concepts provide retrieval routes without forcing detail replication across all sources.

## Why elapsed time did not improve

C41 took4m43s more than C40's57m56s, about8.1percent longer. The main initial receipt window was almost unchanged:50m27s versus50m20s. The late review/correction tail grew from2m44s to6m54s. Fewer review corrections therefore did not translate directly into shorter wall time: two late mechanical handoff fixes still needed their first full independent reviews, the final Functions correction needed targeted review, and ready work/handoffs were coordinated serially. Different content and endpoint definitions prevent assigning the entire difference to any one cause or claiming a controlled concurrency/model benchmark.

The final accepted review→runtime close interval was5m18s, compared with C40's4m52s. Early query overlap kept the close tail bounded, but full audit reads and verbose report drafting still have a visible cost: F,I,J,L each separately reported more than one minute between analysis and handoff. These intervals are observed, not inferred token costs.

## Small next optimization

Keep the current rolling pool, bounded retries and early ready-query overlap; do not add another scheduler, registry or validator. Use the existing worker pre-handoff check to compare retained quote strings literally, including inline links and whitespace, before returning the receipt. Avoid copying a large multiline passage when an exact single-line quote supports the same retained claim. For retained facts, inspect subject/qualifier/action and raw internal labels before handoff; do not demand every navigation label be quoted.

Refill ready roles before report narration, and keep query reports to one actual route plus two concise answers with locators per page, shared checks once. Do not infer that fewer retries justify dropping approved full first reads or independent review. These findings are suggestions for a separately approved future campaign, not new rules or execution authority.
