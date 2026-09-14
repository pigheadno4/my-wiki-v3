# Campaign 46 retrospective

Status: COMPLETE. Exact five-page list approved. Runtime 2026-09-13T09:09:42Z–2026-09-13T09:31:00Z: 1,278 seconds (21m18s).

## Execution notes

- Existing work includes prior C43–C45/scheduler changes and unrelated PayPal/GitHub work. Preserve all; no commits or push.
- No running child agents at preflight; completed historical entries are not used as capacity proof. Actual launches determine available slots.
- Documentation-only campaign; no new rule or code edits, no repeated full unit suite.
- Three actual worker launches succeeded. Five hashes, latest local snapshots and absent source targets verified; initial capsule check passed (227 sources, 65 unreferenced raw snapshots).

## Role timing

UTC observations below; overlapping windows must not be added.

| Role | UTC interval | Duration |
| --- | --- | --- |
| Contract v1 worker | 09:10:11–09:13:52 | 3m41s |
| Create package worker | 09:10:28–09:13:53 | 3m25s |
| List packages worker | 09:10:46–09:13:48 | 3m02s |
| Get package worker | 09:15:05–09:17:44 | 2m39s |
| List packages initial review | 09:14:29–09:17:22 | 2m53s |
| Contract v1 initial review | 09:14:48–09:18:02 | 3m14s |
| Create package initial review | 09:19:09–09:22:43 | 3m34s |
| Get package initial review | 09:19:38–09:22:29 | 2m51s |
| Product-order worker | 09:19:50–09:21:20 | 1m30s |
| Product-order initial review | 09:22:49–09:25:17 | 2m28s |
| Query audit A analysis | 09:23:47–09:27:13 | 3m26s |
| Query audit A analysis-to-handoff | 09:27:13–09:28:43 | 1m30s |
| Query audit B analysis | 09:26:39–09:28:38 | 1m59s |
| Query audit B analysis-to-handoff | 09:28:38–09:30:18 | 1m40s |

All initial long-page receipts passed. Review-first with one worker reserve dispatched Get package after the first three results, while list/contract reviewers ran; create-package review remained queued. No retry so far.

## Outcome

Contract v1 and list-packages were independently approved and promoted, with their exact reciprocal concept entries first, by 09:19:36Z. Remaining roles continue; no third coordinator raw reread.
Get/create package were likewise approved and promoted by 09:23:36Z. The first four pages passed on attempt one. Query group A (contract v1 and package list) launched while final product-order review remained active. Provider catalogs are deferred to the single close update; concept-led routes are already canonical.

All five sources passed on attempt one. Five full initial reviews, zero retries/targeted reviews, zero coordinator semantic repairs. Final retrieval audit passed 10/10 with no extra raw reads or query repairs. One aggregate mechanical/capsule check passed. No code/rule changes, full-suite repetition, new framework, commit or push.

## Promotion and mechanical close observations

- All five independently approved pages were promoted before company/index/log aggregation finished at 09:26:29Z (combined upper-bound observation). Exact concept entries preceded sources; no semantic repair or new concept prose.
- Single aggregate check passed: 10 typed wiki files, all five source/candidate/receipt equalities, pinned hashes, canonical URLs, raw forward paths, concept reciprocal links, approved update presence and unique catalog entries. Provider capsule and `git diff --check` passed; mechanical check itself took 0.407 seconds. No full unit-suite run.
- Sources total 1,612 whitespace-delimited words: contract v1 276, create package 523, list packages 284, get package 303, product ordering 226. Long raw schemas did not require equivalent source inventories; the create page keeps its material restrictions.
- Canonical reconciliation normalizes historical `.md` URL suffixes for comparison only; it does not rewrite historical source metadata. All 80 frozen-inventory identities now have sources, and all 226 selected English canonical pages in the current local collection inventory have source owners. The 232 total source summaries include 226 official-document sources and six GitHub source-layer pages.
- Of 310 immutable raw snapshots, 60 lack direct source references; these are not 60 never-ingested canonical pages. Separately, 36 current-inventory latest snapshots are absent from their existing source's `raw_files`, representing future refresh candidates. Neither refresh nor collection is authorized here.
- Query group A passed 4/4 with both selected raws read fully and no extra reads or repairs. Coordinator checked requested object/action identity and accepted its routes. Report catalog absence and line numbers describe its initial observation before the aggregate catalog update, not the final catalog state. The aggregate mechanical check independently covers the final catalog.
- Query group A analysis-to-handoff took 1m30s; this reporting interval remains an optimization candidate even with compact-report instructions. Avoid expanding future reports with optional schema inventories; no policy change is made here.

## End-to-end timing and next optimization

| Observed stage window | UTC | Wall window |
| --- | --- | --- |
| Worker execution, including gaps between worker starts | 09:10:11–09:21:20 | 11m09s |
| Independent reviews, overlapping workers | 09:14:29–09:25:17 | 10m48s |
| Query audits, overlapping final review/promotion | 09:23:47–09:30:18 | 6m31s |
| Last audit handoff to operational closure | 09:30:18–09:31:00 | 42s |

Individual worker durations totaled 14m17s; independent-review durations totaled 15m00s. These sums are role time, not end-to-end wall time. Final sources and catalog aggregation were finished by 09:26:29Z, while audits continued. The mechanical check took under a second; it is not the bottleneck. Precise per-job queue accounting is not reconstructed from untimestamped journal events.

C46 is 35 seconds faster than C45 (21m53s) and 3m17s slower than C44 (18m01s). It read 8,760 raw lines and retained 1,612 source words. Different pages, role scheduling and reporting make these observational comparisons, not causal speedup claims. Zero retries removes one known cost but does not make coordinator handoffs and final audit free.

Small next improvement: keep the existing routing/review rules, dispatch ready roles immediately, and make audit reports answer-and-locator led without optional schema catalogs. Group B also spent 1m40s after analysis on reporting; both reports together show 3m10s of role reporting time, partly overlapping and therefore not a guaranteed 3m10s wall saving. Do not add a performance framework or another policy layer.

All current local canonical pages now have source owners. The next substantive ingestion decision is whether any of the 36 latest-snapshot refresh gaps merits a bounded refresh, not another arbitrary five-page never-ingested campaign. No refresh is started here. During this campaign another task committed PayPal JS work as d18ae498 on shared main and requested inclusion in a future authorized push; this campaign did not alter or recommit it and did not push.
