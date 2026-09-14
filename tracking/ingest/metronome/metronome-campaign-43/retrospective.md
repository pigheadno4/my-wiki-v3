# Campaign 43 execution notes

Status: COMPLETE; exact manifest approved 2026-09-10. Closed at `2026-09-10T10:23:50Z`, 2,384 seconds (39m44s) after initialization. All five sources promoted, 10/10 query questions passed, one aggregate mechanical/capsule check passed. No commit or push authorized.

## Timing and capacity

Times are UTC on 2026-09-10. Runtime started at `09:44:06Z`. First two native workers (`c43_w_rate`, `c43_w_card`) successfully launched. Scheduling uses two child slots based on the previously observed working capacity, under the manifest's maximum of three. No capacity test agent or extra failed dispatch was issued; three-slot availability was not retested in this campaign.

## Controls

Five pinned raw hashes/latest snapshots and absent source targets checked. Adopted current assertion-retention, question-needed historical evidence, and paired-question audit reporting rules. Full initial raw reads, independent initial review and reciprocal links remain required. Prior rule-change test run passed 770 tests; documentation-only execution will use one aggregate scoped mechanical/capsule check, without another full unit run unless changes require it.

## Stage observations

Agent self-reported intervals and coordinator dispatch/promotion observations will be recorded here. These overlap and are not additive; earliest clock observation is not necessarily inference start.

- Add-rate worker: `09:44:43Z`–`09:48:31Z` (3m48s), accepted; independent reviewer launched.
- Update-card worker: `09:44:44Z`–`09:48:51Z` (4m07s), accepted and awaiting review. Archive-offset worker launched in the freed slot, retaining one active worker while ready reviews wait. No dispatch failures or retries.
- Archive-offset worker: `09:49:43Z`–`09:53:06Z` (3m23s), accepted; Plan-adjustment worker launched in the freed slot while add-rate review continues.
- Add-rate initial full review: `09:49:17Z`–`09:57:02Z` (7m45s), changes requested for one missing consequential MinimumConfig warning: configured minimums suppress commit-specific overrides, with percentage-rate scope. Existing concept route approved; retry review is targeted. The reviewer was asked once for remaining required work because this review was slow.
- Plan-adjustment worker: `09:54:42Z`–`09:57:26Z` (2m44s), accepted. Update-card reviewer and delete-values worker launched next under the existing scheduler's order; add-rate retry remains queued.
- Dispatch reconciliation: an initial review-result command supplied a worker assignment while the scheduler emitted a ready review; the CLI rejected it before persisting. The corrected command supplied `c43_r_card`. A subsequent worker assignment label `c43_w_rate` was attached by the scheduler to the next queued delete-values job, not the add-rate retry. That trusted order was dispatched to fresh isolated native agent `c43_w_delete` (Sol medium); the earlier add-rate worker was not reused for deletion. This native-name/runtime-label mapping is explicit; no trusted order was rewritten and no duplicate attempt was created.
- Delete-values worker: `09:59:27Z`–`10:03:54Z` (4m27s), accepted. All five first-attempt workers handed off. The scheduler then emitted add-rate attempt 2, assigned to the original worker for the bounded MinimumConfig correction; raw hash and affected context only, no full reread requested.
- Update-card full review: `09:58:14Z`–`10:05:25Z` (7m11s), approved first pass with precise shared-edit placement. Two extraneous reviewer identity fields in the draft artifact were removed by the reviewer before runtime intake; no semantic rereview. Archive-offset review dispatched next.
- Add-rate bounded worker correction: `10:04:45Z`–`10:06:01Z` (1m16s), accepted; unchanged raw hash, narrow warning/quote correction, approved shared meaning retained. Existing queue order selected Plan-adjustment full review next; the corrected add-rate candidate waits for targeted review, not another full review.
- Update-card approved concept paragraph and exact source promoted by `10:06:52Z`. Only the ambiguous metadata clause was replaced; adjacent guide-backed rate-addition, future-effective price-change and existing unknown-boundary guidance was preserved as the reviewer required.
- Archive-offset full review: `10:07:03Z`–`10:09:40Z` (2m37s), approved first pass. Its concept route and exact candidate promoted by `10:10:31Z`; delete-values initial reviewer launched in the freed slot.
- Plan-adjustment review requested a bounded correction: remove unsupported response-array cardinality (`one or more` without minItems) and an unsupported start_period gloss, using the reviewer's exact schema-locator rewrite. Both concept routes approved, targeted retry. Reviewer clock observations `10:10:29Z`–`10:11:24Z` cover only its late observed interval: native dispatch occurred before `10:06:52Z`, so do not present this as a 55-second full review. Original worker dispatched for attempt 2 with unchanged quotes/suggestions requested.
- Delete-values initial full review: `10:10:57Z`–`10:13:13Z` (2m16s), approved first pass. Exact durable concept paragraph added after the existing removeKey paragraph, then exact source promoted by `10:13:59Z`. Original add-rate reviewer dispatched for targeted attempt-2 review.
- Plan-adjustment bounded worker correction: `10:12:33Z`–`10:13:56Z` (1m23s), accepted with unchanged raw hash, quotes and approved suggestions. Original reviewer dispatched for targeted attempt-2 review. First-pass outcome is 3/5; no full rereview was requested.
- Add-rate targeted review: `10:14:06Z`–`10:15:55Z` (1m49s), approved. Its concept route and exact attempt-2 source promoted by `10:16:43Z`; first three pages' query audit dispatched.
- Plan-adjustment targeted review: `10:15:00Z`–`10:16:16Z` (1m16s), approved; its two concept routes and exact source promoted by `10:17:18Z`. Final two pages' query audit dispatched in the freed slot. All five jobs approved; query audits run as disjoint groups under the same two-child capacity.
- Shared company/index/log aggregation completed by `10:18:44Z`. One scoped mechanical/capsule check completed by `10:19:33Z`, validator runtime 0.448s. Checked 11 typed files plus frontmatter-free provider router; final candidate/receipt equality, pinned hashes, six approved shared updates and intended placement, preserved adjacent guide guidance, reciprocal links, catalog uniqueness, and counts all passed. Coverage: 310 raw snapshots, 217 total sources, 211 official-document sources, 75 orphan raw snapshots, 15 remaining frozen-inventory canonical identities. `git diff --check` passed.

## Final source sizes

Whitespace-delimited words, including frontmatter; not an output target or a completeness measure.

| Source | Words |
| --- | ---: |
| Add a rate, attempt 2 | 250 |
| Update rate card | 326 |
| Archive offset configuration | 360 |
| Plan adjustments, attempt 2 | 380 |
| Delete selected custom-field values | 293 |
| Total | 1,609 |

C42 totaled 1,784 words. This is 175 fewer words (about 9.8%), with different pages and no controlled inference about speed or quality. Four navigation entries and two approved factual edits across four concepts were needed; unlike C42, this campaign was not navigation-only shared work.

## Query observations

- Group B Q7–Q10: 4/4 PASS, no retrieval repair or extra full raw read. UTC `10:18:06Z`–`10:21:26Z` (3m20s): analysis to `10:20:07Z` took 2m01s; analysis-end to report handoff 1m19s. Exact selected raws answered the requested current operation/locator questions; the gap sweep found no conflict requiring extra evidence. Coordinator checked requested and reached objects/actions before accepting these verdicts.
- Group A Q1–Q6: 6/6 PASS, no query repair or extra full raw read. UTC `10:17:38Z`–`10:22:34Z` (4m56s): analysis to `10:21:04Z` took 3m26s; analysis-end to handoff 1m30s. The older update-card snapshot and adjacent operations were discovered but not selected because the current questions and found evidence did not require them; no equivalence of unread versions was asserted. Coordinator checked all six object/action matches and evidence routes.

## Stage timing summary

Times are observed/self-reported wall windows, not isolated inference time. They overlap and must not be added.

| Stage | UTC window | Duration |
| --- | --- | --- |
| Initialization to first worker clock observation | 09:44:06–09:44:43 | 37s |
| Five initial workers | 09:44:43–10:03:54 | 19m11s window; individual intervals sum to 18m29s |
| Five initial reviews | 09:49:17–10:13:13 | 23m56s window, including queue gaps; Plan reviewer lacks a reliable start clock |
| Two bounded worker corrections | 10:04:45–10:13:56 | interleaved window; individual work intervals total 2m39s |
| Two targeted reviews | 10:14:06–10:16:16 | 2m10s overlapping window; individual intervals total 3m05s |
| Final source promotion through shared aggregation/check | 10:17:18–10:19:33 | 2m15s, including audit dispatch/preparation; validator itself 0.448s |
| Query audit groups | 10:17:38–10:22:34 | 4m56s overlapping window |
| Last audit handoff through durable report and close | 10:22:34–10:23:50 | 1m16s |
| Operational total | 09:44:06–10:23:50 | 39m44s |

The add-rate correction loop illustrates queue cost: first review ended at 09:57:02, correction worker ran 10:04:45–10:06:01, and targeted reviewer ran 10:14:06–10:15:55. The loop spans 18m53s, of which the two reported work intervals total 3m05s; the intervening 15m48s combines queue, dispatch and handoff delay. Existing ready-review preference and fresh queued work delayed this bounded retry. This is not 18m53s of raw rereading, nor proof that a priority change would save the whole delay without delaying other jobs.

## Outcome and next-step interpretation

- Coverage and final query quality passed: five approved sources, all raw hashes/provenance and intended reciprocal links checked, 10/10 queries, zero full rereviews and zero coordinator semantic repairs.
- Both observation targets missed: first-pass 3/5 (target at least 4/5); 39m44s closure (target at most 35m), 1m43s longer than C42. Do not report end-to-end speed improvement from the smaller sources.
- Two content failures point in opposite directions: one important pricing warning was omitted; one optional schema sentence added unsupported meaning. The approved retention rule remains appropriate, but this sample does not show reliable first-pass execution of it. No extra invariant catalog or repeated compression pass was introduced.
- Query evidence selection behaved as intended: no extra historical/adjacent full reads versus C42's five extra query reads. Query windows were shorter (Group A 4m56s vs 5m38s; Group B 3m20s vs 5m11s), but different raw questions prevent a causal benchmark claim.
- Report handoff remains 1m19s–1m30s after analysis. Source generation and verification still include unnecessary retained detail in some pages; do not launch a retrospective rewrite merely to reduce words.
- A next optimization worth discussing is bounded-correction scheduling within the existing queue, rather than more writing rules or a new framework. Any priority change needs explicit approval and must preserve reviewer independence, actual capacity and progress for fresh jobs. No such scheduler/rule change was made here.
- Actual capacity used was two children, not a measured maximum for this new campaign; three slots were not retested. No conclusion about historical Done-thread resource release follows from this run.

Final retrospective writing after runtime closure is excluded from 39m44s. All changes remain local and uncommitted, including the preceding approved one-file rule refinement; unrelated CLAUDE copy.md is preserved. No new collection, next campaign, commit or push was performed.
