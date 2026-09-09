# Campaign 41 retrospective

Status: complete. Five sources promoted, 4/5 first-pass approvals, 10/10 final retrieval questions passed. Runtime 12:50:34–13:21:22 UTC: 1,848 seconds (30m48s). Both observation targets (at least 4/5 first-pass, at most 35 minutes) met; this is only 1m23s (about 4.3%) faster than C40, not a substantial or causal speedup claim.

## Timing method

Runtime started_at/completed_at measure operational closure. Coordinator UTC observations record handoffs and promotions; agent self-reported intervals may start after native dispatch. Intervals overlap and must not be summed into wall time. Existing events lack timestamps. Post-close report/commit is separate. No new timing schema or subsystem.

## Coordinator observations (UTC, 2026-09-09)

- 12:50:34 — initialized runtime and first three trusted orders; immediately dispatched grants, credit and offset workers in manifest order.
- 12:55:37 — grants worker accepted and independent reviewer dispatched. Worker completion self-reported 12:55:24; no worker start was captured. Dispatch-to-completion is approximately 4m50s, not measured active processing time.
- 12:56:17 — offset worker accepted and reviewer dispatched; self-reported worker interval 12:51:59–12:55:57 (3m58s).
- 12:56:40 — credit worker accepted and queued for review while prepaid-commit-end worker dispatched to keep queued generation moving. Credit worker self-reported recorded interval 12:52:22–12:56:06 (3m44s), with a late recorded start relative to dispatch.
- 13:01:07 — grants first review approved and credit reviewer dispatched after 4m27s ready-review queue. Grants reviewer interval 12:56:10–13:00:37 (4m27s).
- 13:01:31 — offset first review approved and custom-field-values worker dispatched. Offset reviewer interval 12:56:45–13:00:47 (4m02s).
- 13:01:54 — commit-end worker accepted and reviewer dispatched; worker interval 12:57:37.819–13:00:51.524 (about 3m14s).
- 13:02:33 — grants and offset approved concept routes and exact source candidates promoted; the roughly 1m26s interval since first approval includes three native dispatches, handoffs and both promotions.
- 13:06:16 — credit first review approved and concept/source promoted; Group A six-question audit dispatched. Reviewer interval 13:02:41–13:05:43 (3m02s).
- 13:06:40 — custom-field worker accepted and reviewer dispatched, runtime pool reduced to two for the auditor slot. Worker interval 13:02:02–13:05:37 (3m35s). All five initial worker outputs accepted, 16m06s after runtime start.
- 13:07:49 — prepaid commit-end first review approved and concept/source promoted. Reviewer interval 13:02:30–13:06:38 (4m08s). Group B four-question audit dispatched to start its two commit questions while fields review continues. Both auditor slots count against capacity.
- 13:09:37 — Group B had reported its two prepaid-commit questions passed and was waiting for fields promotion; coordinator observation, not exact start of waiting.
- 13:10:40 — fields first review requested correction of four receipt quote line locators only. Source and shared suggestion meaning approved unchanged. Same worker dispatched for targeted attempt 2 with runtime capacity one. Reviewer interval 13:07:18–13:10:17 (2m59s). First-pass rate: 4/5.
- 13:13:01 — fields attempt 2 accepted and same reviewer dispatched for targeted line-locator check. Worker correction interval 13:11:08–13:12:38 (1m30s); candidate, quote text and shared suggestions unchanged.
- 13:14:57 — fields targeted review approved and final concept/source promoted; Group B notified to resume fields questions. Reviewer interval 13:13:37–13:14:24 (47s). Receipt-only correction-to-promotion window 4m17s, including handoffs; source text was never rewritten.
- 13:15:51 — Group A report inspected and preserved; all six correct objects/routes pass. Agent-reported interval 13:06:54–13:11:37 (4m43s), but final artifact was handed back around 13:14:24. Its reported end therefore does not represent the entire dispatch-to-handoff occupancy; do not silently erase that gap.
- 13:16:26 — one aggregate company/index/log close and combined mechanical/capsule validation complete, 1m29s after final source promotion, overlapping Group B's remaining questions.
- 13:17:45 — Group B reported audit-analysis completion; start 13:08:23, 9m22s including a recorded 5m12s promotion wait (13:09:45–13:14:57). All four requested objects/questions passed.
- 13:20:38 — Group B final artifact handoff after report verification/coordination, 2m53s after its stated audit completion. Coordinator had inspected the substantive report and requested no further wording polish. Total Group B start-to-handoff occupancy: 12m15s, not 9m22s.
- 13:21:22 — reports preserved, quality summary accepted and runtime completed. Final handoff-to-close overhead: 44s. Post-close report and local commit are outside operational elapsed time.

## Stage measurements

Intervals overlap and are not additive. Agent-reported processing intervals exclude some dispatch/startup and reporting time.

| Stage | Observed time | Interpretation |
| --- | ---: | --- |
| Initial worker pipeline | 16m06s | Runtime start to last initial worker acceptance, including staggered launch and handoff |
| Initial workers, individually | about 3m14s–4m50s | Grants lacks a start timestamp; its figure is approximate dispatch-to-completion, others are self-reported |
| Five initial reviewers | 2m59s–4m27s each | Self-reported total 18m38s, overlapping workers and each other |
| Credit ready-review queue | 4m27s | Dynamic pool kept another worker active |
| Receipt-only correction through promotion | 4m17s | Worker 1m30s, targeted reviewer 47s, remaining 2m00s dispatch/handoff/promotion; no source rewrite |
| All five sources promoted | 24m23s after start | C40: 26m40s |
| Shared aggregate close + mechanical/capsule checks | 1m29s | One pass, overlapped final query audit |
| Group A stated audit analysis | 4m43s | Final handoff occurred later; full occupancy cannot be inferred from this interval alone |
| Group B audit start-to-handoff | 12m15s | Includes 5m12s waiting for promotion and 2m53s post-analysis reporting/coordination |
| Final handoff → operational close | 44s | Report persistence and runtime transition |
| Operational total | 30m48s | Runtime timestamps |

## Findings and next-step restraint

- The narrow-detail contract changed outputs: 1,397 total source words versus C40's 1,671; six navigation-only concept updates versus C40's six navigation plus three factual paragraphs. All ten detail/navigation questions still passed. Different pages and risk profiles mean this does not prove causal token savings or cross-provider generality.
- First-pass improved from 3/5 to 4/5. The only failed first review concerned four quote line locators; candidate and shared meaning required no changes. Five full initial reviews remained, with one 47-second targeted rereview and no full rereview.
- Object/action checks worked for all ten questions; no audit object-selection error or two-question rerun occurred. This is a useful single-sample result, not evidence that such errors are impossible.
- Throughput improvement is modest: 1m23s faster operational close. The dynamic-pool ready-review queue and multi-stage handoffs remain, while detailed audit-report production/verification extended occupancy beyond analysis timestamps. Do not label those windows as full-raw analysis costs.
- Keep this contract for the next explicitly approved sample without another architecture redesign. A small future optimization is to use an exact stable heading/schema locator for quotes, or obtain numeric line positions mechanically rather than estimating them. The existing quote location string needs no new schema; no locator generator was built in this campaign.
- Keep future audit reports focused on the requested answer, actual route, evidence and verdict, rather than extra schema inventory or repeated prose. No new report framework, monitoring system, reviewer waiver, bulk rollout, push or next campaign is authorized here.

## Mechanical closure evidence

One combined check passed for 11 typed wiki files, every provider-index wikilink, five source/candidate/receipt equalities (EOF newline normalized), all pinned raw hashes, six approved exact-once concept suggestions in their intended sections, reciprocal source links and unique company/index catalog entries. Capsule validation returned no errors. The receipt-only retry preserves candidate, quote text and suggestions. `git diff --check` passed.

Coverage: 207 total source summaries, 201 official-document sources, 85 raw snapshots without source summaries, 25 remaining canonical identities in the frozen never-ingested inventory. No raw file was modified.

Whitespace-split source word counts including frontmatter: grants 221, credit 324, offset 382, commit end 260, custom fields 210; total 1,397 (C40: 1,671, about 16.4% fewer). Six shared updates are all reciprocal navigation; zero new concept factual paragraphs (C40: six navigation plus three factual additions). No new schemas, runtime code, tests or monitoring subsystem were introduced.

## Scope and baseline

Five never-ingested API pages, 1,484 raw lines. Start coverage: 196 official-document sources, 202 total sources, 90 orphan raw snapshots and 30 remaining frozen-inventory canonical identities. Approved narrow-detail and audit-object rule refinement is applied; mandatory full initial raw reads/reviews, exact provenance, dynamic three-slot pool and one ten-question audit remain. The rule refinement passed 770 unit tests in the preceding turn; it is unchanged here. Preserve unrelated `CLAUDE copy.md`. No push or subsequent campaign authorized.
