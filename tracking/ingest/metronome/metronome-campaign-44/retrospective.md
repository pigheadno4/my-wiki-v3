# Campaign 44 retrospective

Status: COMPLETE. Exact five-page selection approved. Runtime 2026-09-11T13:52:46Z–2026-09-11T14:10:47Z: 1,081 seconds (18m01s). No commit or push.

## Execution notes

- Native live-agent list initially contained only the coordinator. Three actual Sol medium worker dispatches succeeded (rates, schedule, grant); no capacity probe or assumption based on historical Done entries.
- Pinned raw hashes verified and all five source targets absent. Capsule baseline: 310 raw snapshots, 217 sources, 75 unreferenced snapshots; frozen inventory has 15 uncovered canonical identities.
- Prior scheduler/rule changes remain uncommitted. Full unit suite launched once concurrently with initial work; no per-page repeats. Unrelated PayPal work and CLAUDE copy.md are out of scope.
- Current scheduler prioritizes targeted corrections within each role, preserves review-first allocation and worker reserve, and does not preempt active jobs.

## Role timing

UTC start/end observations will be recorded from role handoffs; overlapping windows are not additive. No new tracking schema.

| Role | UTC interval | Duration |
| --- | --- | --- |
| Add rates worker 1 | 13:53:21–13:55:22 | 2m01s |
| Rate schedule worker 1 | 13:54:10–13:56:37 | 2m27s |
| Credit grant worker 1 | 13:54:22–13:55:38 | 1m16s |
| Add rates full reviewer | 13:56:09–13:58:05 | 1m56s |
| Credit grant full reviewer | 13:56:42–13:58:34 | 1m52s |
| Customer Plan worker 1 | 13:57:36–14:00:31 | 2m55s |
| Rate schedule full reviewer | 13:58:50–14:01:03 | 2m13s |
| Package worker 1 | 13:59:57–14:02:02 | 2m05s |
| Customer Plan full reviewer | 14:01:22–14:03:59 | 2m37s |
| Package full reviewer | 14:02:22–14:04:51 | 2m29s |
| Audit A reported analysis | 14:02:25–14:05:53 | 3m28s |
| Audit B analysis | 14:06:32–14:08:39 | 2m07s |
| Audit B report/handoff | 14:08:39–14:09:38 | 59s |

Audit A report labels handoff 14:05:57 (3m32s from its start); coordinator received/read the completion around 14:07. Reported timestamps do not eliminate message-delivery/coordination overhead. Six answers passed, exact assigned object/action matched, no extra raw reads or query repair. Coordinator checked the report, not a duplicate raw audit.

Add rates promoted by 13:58:49; credit grant promoted by 13:59:21. Both first attempts approved with one navigation-only concept suggestion each; no coordinator semantic repair. Source and concept writes were serial. Credit grant's compound Sources anchor was applied at the start of the existing Sources section near its legacy grant entries.

Rate schedule promoted by 14:01:43 with one approved factual concept paragraph, distinguished from the existing point-in-time getRates and contract-specific schedule routes. Group A query audit dispatched immediately afterward for the first three promoted pages, overlapping remaining jobs. Its slot is subtracted from subsequent runtime dispatch capacity.

Customer Plan promoted by 14:04:21 with one reciprocal source route. First four sources passed their initial full reviews; no retry or coordinator semantic repair so far.

Package promoted by 14:05:21, adding its approved archival subsection at the end of Cohort pricing, without moving existing prose under the new subsection. All five initial reviews approved. Group B audit dispatched after this last promotion. Company/provider-index/log aggregation completed by 14:06:13, overlapping both query groups.

One aggregate mechanical/capsule check passed after aggregation: 11 typed pages, candidate/receipt equality, approved shared-update IDs and exact placement, pinned hashes, source/raw provenance, reciprocal routes, unique catalogs and counts. Runtime 0.488s. Capsule: 310 raw snapshots, 222 total source pages (216 official-document records), 70 unreferenced snapshots. Source words: add-rates 286, schedule 300, grant 258, Plan 435, package 210; total 1,489. Diff whitespace check passed. No per-page validation loop or additional full suite.

The full unit suite passed: 773 tests in 121.773s, overlapping initial worker execution. All five selected files are their latest local snapshots. At 13:56:37 the schedule candidate completed while both other slots held initial reviewers; the existing worker reserve dispatched the Plan worker next, leaving schedule review queued. This is unchanged cross-role policy, not a targeted-priority failure.

## Outcome

All five sources promoted on attempt 1; 5/5 first-pass approvals, five full initial reviews, zero full rereviews, targeted reviews, failed/rejected jobs or coordinator semantic repairs. Five shared updates across four concepts: three navigation entries and two factual additions. Final audit passed 10/10, with no extra full raw reads or query repair. Both audit reports were checked against the assigned objects/actions and preserved in quality-audit.md.

| Stage | UTC window | Elapsed |
| --- | --- | --- |
| Initialization to first worker start | 13:52:46–13:53:21 | 35s |
| Five initial workers | 13:53:21–14:02:02 | 8m41s window; 10m44s summed role intervals |
| Five independent initial reviews | 13:56:09–14:04:51 | 8m42s window; 11m07s summed role intervals |
| Promotions | first by 13:58:49, final by 14:05:21 | overlapped reviews and audit A |
| Final promotion to aggregate validation confirmed | 14:05:21–14:07:00 | at most 1m39s; validator itself 0.488s |
| Two query audit groups | 14:02:25–14:09:38 | 7m13s reported window; overlaps other stages |
| Final audit handoff to runtime close | 14:09:38–14:10:47 | 1m09s |
| Operational total | 13:52:46–14:10:47 | 18m01s |

Stage windows overlap and must not be added. Compared with C43's 39m44s, this is 21m43s shorter (~54.7%). First-pass and 35-minute observation targets both met. Source words fell from 1,609 to 1,489 (~7.5%). This is not a controlled benchmark: pages differ, three child slots succeeded versus two used in C43, all first attempts passed, and audit/promotion overlapped. No targeted correction arose, so this run provides no runtime evidence of the new targeted queue priority itself.

Keep the current process for the next separately approved sample; no new scheduler knobs, shorter-source rewrite pass, or extra reviewer layer is justified by this run. Some candidates still retain optional schema qualifiers and hypothetical-unknown phrasing; record this as a drafting-efficiency observation rather than reopening accurate approved pages. Remaining ten frozen-inventory canonical identities include several much longer package/contract references, so do not extrapolate 18 minutes to those pages.

All changes remain local/uncommitted, including C43 and approved scheduler/rule edits. Unrelated PayPal work and CLAUDE copy.md preserved. No collection, further campaign, commit or push performed. Final retrospective prose after runtime closure is excluded from operational elapsed time.
