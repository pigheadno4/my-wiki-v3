# Braintree C46 timing and findings

Runtime31m10s, versus C45's57m30s:26m20s shorter (45.8percent). Scope45rather than50pages and90rather than100queries; primary raw2,344rather than6,629words. The corpus is unusually sparse, so this is not a causal throughput/model benchmark or proof that all future campaigns will be this fast.

## Overlapping stage windows

| Stage | UTC window, 2026-10-07 | Measurement |
| --- | --- | --- |
| Worker dispatch/drafting/correction |23:28:35–23:53:24|46accepted artifacts, median63.2s/max118.4s from attempt-directory birth to artifact mtime |
| Independent review/correction |23:30:28–23:55:47|45full reviews median70.4s/max99.5s; one targeted lifecycle159.9s |
| Canonical promotion |23:34:57–23:56:15|Incremental source creation window; overlaps roles and queries |
| Final query tail |After final promotion23:56:15 to final audit receipt around23:59|K/L overlap catalog aggregation; no extra full audit layer |
| Shared aggregation/close |23:56:15–23:59:45|One catalog/count/log aggregation, one structural close, one54-page typed validation; overlaps final query tail |

Windows overlap and must not be added. Filesystem times include dispatch overhead and waiting, not isolated model compute or token cost. Worker handoff wait median76.0s/max268.5s across46receipts, versus C45's127s/max412s across57accepted worker receipts. Review handoff wait median63.7s/max232.2s across46receipts. No negative intervals excluded. The targeted lifecycle includes a persisted-order-to-resume delay and must not be described as160seconds of model review. One reviewer handoff used a timezone-inconsistent prose UTC label; external artifact time was used instead. Audit L's self-reported start precedes its actual dispatch, so that start is excluded from performance interpretation; its content verdict is unaffected. No new timing framework was added.

## Quality and remaining efficiency limits

First review44/45 (97.8percent), versus43/50 (86percent) in C45. One bounded correction: a locator accidentally implied exclusive JavaScript-v3 availability where the raw only names JavaScript v3. No full repeat review, failed artifact handoff, semantic coordinator repair or query-source correction. Full primary reads, independent review and90fixed queries were retained.

Worker median103→63.2s and full-review median118→70.4s; lower raw volume and fewer corrections contribute, while reduced handoff wait is consistent with faster ready-artifact acceptance. Earlier metadata-led ordering cannot be isolated as the cause. Query reports total12,045words versus13,555 in C45; source14,052versus20,837words. Reports and qualification prose remain much larger than these sparse raws. The run is faster but does not demonstrate that the prose overhead is solved.

Keep the existing subject/condition/action check: `available with` is not `only available with`; a native-platform URL is not native implementation evidence. Preserve consequential warnings once rather than repeating absent-outcome inventories. Do not retrospectively shorten approved pages or add another validation system. Changing per-page source policy or90-question coverage needs separate approval.

All ordinary remaining successful website variants are now referenced. Only the separately deferred27,225-word validation-errors page remains. Recommended next action is a scoped commit/push approval, then a separate decision on that heavy page or another PSP. No next campaign has been prepared or started.

The dispatching-parallel-agents skill kept outputs isolated and shared writes coordinator-owned. Verification-before-completion required fresh structural/typed checks and completed-state readback; no new framework was introduced.
