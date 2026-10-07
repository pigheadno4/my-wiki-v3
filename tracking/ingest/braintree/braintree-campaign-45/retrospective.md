# Braintree C45 timing and optimization findings

Runtime13:22:41–14:20:11UTC:57m30s. C44 was56m06s; C45 is1m24s (2.5percent) longer. Earlier overview/migration/deprecated dispatch did not demonstrate overall throughput improvement. The approved scope remains50sources/100queries, ten shared rolling child slots, Sol medium workers and independent Sol high first reviewers.

## Overlapping stage windows

| Stage | UTC window | Measurement |
| --- | --- | --- |
| Worker dispatch/drafting/corrections |13:22:41–14:15:18|57accepted matched artifacts; median103s/max265s from attempt-directory birth to artifact modification, including dispatch overhead|
| Independent review/corrections |13:25:46–14:16:40|50full reviews median118s/max267s;7targeted reviews median48s/max63s from trusted review-input modification to external artifact modification|
| Canonical promotion |13:31:30–14:17:03|Source creation window; overlaps workers/reviewers/queries|
| Final query tail |14:17:58–14:19:21|Group M start/handoff endpoints; two pages, four questions; overlaps closure preparation|
| Shared aggregation/close |Approximately14:17:15–14:20:11|Single catalog/count aggregation, two log entries, one structural close and one62-file typed validation; overlaps final query wait|

Windows overlap and must not be added. Filesystem mtimes/birth times and role timestamps are approximate lifecycle evidence, not isolated model compute or token counts. Accepted handoff wait covers57receipts, median127s/max412s, versus C44 median81s/max179s. No negative intervals were excluded. Failed stale-artifact attempt2 is not an accepted receipt and is not in these median measurements.

Worker median111→103s (-7.2percent), full review116→118s, targeted63→48s (-23.8percent). Faster worker/targeted stages were offset by longer coordinator handoff waits and seven rather than three semantic corrections. The last semantic correction was one landing-page provenance sentence; an avoidable stale-path submission then added an operational attempt before targeted approval. The final query group remained gated by that source's promotion. Earlier overview ordering did not eliminate this ordinary-page tail.

## Quality and practical lessons

First-review pass43/50 (86percent), down from C44's47/50 accepted pass. Seven bounded corrections: Function object versus deployment sharing; generic Client API discoverability and locator; Channel API versus generic webhook retry attribution; checklist ordinary steps versus prerequisites; WeChat listed currencies versus umbrella presentment wording; Node website field spelling versus exact-package camelCase; landing-page positioning versus unread linked-article attribution. No full repeat review or terminal rejection.

Primary raw12,940→6,629words (-48.8percent), but source20,153→20,837words (+3.4percent). Thirteen query reports total13,555words versus C44's13,784 (-1.7percent), saved13:36:27–14:19:59UTC; saving spans are not active model compute. Short raw notices still generated substantial qualification/navigation prose. Smaller input did not yield smaller output or faster completion; page scopes and supporting conflicts differ, so this is not a causal model benchmark. Keep material warnings, but avoid hypothetical non-proof inventories repeated across Overview, takeaways, warnings and reciprocal entries. This is a future drafting instruction, not authority to rewrite approved pages now.

The query-report C correction addressed the auditor's Function/deployment object mismatch, not source quality. The supplemental-quote correction addressed the primary-only handoff contract, not content. The stale-artifact failure was coordinator-owned: serialized-store object-identity filtering retained old active entries and selected the wrong path. Reconciliation now uses role/position/artifact values; no runtime/scheduler/schema change was needed. Original failure and correct unused candidate are retained.

## Next small decisions

1. Prioritize ready receipt acceptance and immediate trusted dispatch using the exact current artifact and attempt. Avoid report-copying/prose work ahead of ready handoffs. This run's median127s handoff is the clearest measurable regression; do not add another queue or monitoring system.
2. In the existing worker check, distinguish the subject carrying a statement (page vs linked article; Function vs deployment; product-specific vs generic contract). A one-line scope check targets these observed failures more directly than denser source summaries or a new invariant registry.
3. Preserve consequential local qualifications once; let precise raw locators carry routine detail. Short pages should not acquire large repeated hypothetical boundary inventories. No hard word cap, blanket review waiver or retrospective shortening pass.
4. Keep existing targeted correction reviews and one close validation. They reduced correction-review median; do not add audits or code tests. Changing the100-query scope needs separate user approval.

Current inventory verification:46successful collected website variants remain unreferenced, including the separately deferred27,225-word validation-errors-all-node page. The next round cannot contain50new primary candidates under the unchanged eligibility rules. Recommend preparing up to45ordinary remaining pages and keeping that heavy page separately approved; do not execute, collect, commit or push without approval.

The dispatching-parallel-agents skill kept delegate outputs isolated and coordinator-owned shared writes; verification-before-completion required the fresh structural/typed checks and completed-state readback. No new framework was introduced.
