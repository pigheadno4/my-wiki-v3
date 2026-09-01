# Metronome Campaign 35 retrospective

## Result

- Started: `2026-09-01T10:54:24Z`
- Completed: `2026-09-01T11:38:41Z`
- Elapsed: 2,657 seconds (44 minutes 17 seconds)
- Final approval: 5/5
- First-pass approval: 0/5
- Worker attempts: 11
- Full reviews: 10
- Targeted reviews: 0
- Coordinator semantic repairs: 0

Final quality, the 9/9 fixed query audit, exact candidate promotion, shared-update, hash, link, count, capsule, and diff checks passed. Campaign 35 finished 2,927 seconds faster than Campaign 34 and met the observational 45-minute target, but missed the first-pass and eight-attempt throughput gates.

## What worked

- The exact Metronome POST execution-admission rule was present on the first attempt for all four POST jobs. No retry was caused by omitting or misstating it.
- The legacy Customer Plans GET remained a clean negative control and did not inherit POST `Idempotency-Key` behavior.
- Each first reviewer returned all material blockers visible to it together. No later complete review discovered a new material blocker from the unchanged raw and authority context.
- Dynamic slots continued without a batch barrier, and the campaign closed within 45 minutes despite five semantic retries and one mechanical recovery.
- The coordinator promoted only approved candidates and reviewer-approved updates, performed no semantic repair, and ran one close validation plus the fixed three-page audit.

## What cost time

- Every first attempt required correction. The remaining blockers were page-specific authority fan-out rather than the calibrated execution-admission sentence: ledger amount and retention boundaries, `window_size: none` and `LATEST` semantics, Product type/composite/SQL/custom-field conflicts, exact Contracts migration routing, and alert export/uniqueness/recovery distinctions.
- Product attempt 2 used unsupported `update_kind: contradiction`. The controller correctly failed closed before review, but attempt 3 was needed solely to map that warning to `durable_fact`; no source semantics changed.
- Complete retries and complete re-reviews remained the dominant cost. The new provider invariant prevented one known defect but did not improve first-pass approval on this sample.

## Gate assessment

- PASS: 5/5 final approval, no terminal rejection, no coordinator semantic repair, no execution-admission retry, GET negative control, blocker completeness, 9/9 fixed audit, exact promotion and reciprocal links, and elapsed time at or below 45 minutes.
- FAIL: 0/5 first-pass approvals versus the 3/5 target; 11 worker attempts versus the maximum of 8.

## Recommendation

Keep the provider invariant and current files; do not add another registry, scheduler, or reviewer layer. Before another campaign, make one small contract clarification so worker suggestions name only the already-supported `durable_fact` or `reciprocal_source_link` kinds. More importantly, treat Campaign 35 as evidence that one provider-wide preflight fixes a repeated rule but cannot solve cross-authority completeness. Do not scale this five-page, full-review method for throughput without a separate user-approved strategy for the remaining 55 never-ingested canonical pages.
