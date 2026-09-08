# Campaign 39 retrospective

Status: complete. Five approved sources, 4/5 first-pass approvals, five full initial reviews, one targeted correction/review, zero full rereviews and zero coordinator semantic repairs. Final retrieval audit: 10/10 PASS.

Operational elapsed: **1,750 seconds / 29m10s**, from 10:04:07 to 10:33:17 UTC on 2026-09-08. This excludes subsequent retrospective finalization and local commit, consistently with Campaign 38.

## Timing method

Campaign started_at/completed_at provide overall operational elapsed time. Existing events.jsonl records event order but has no timestamps; do not present it as a timestamped event log. The observations below are coordinator UTC wall-clock readings at dispatch/result/promotion/audit boundaries. They include tool, scheduling and handoff latency and are not model inference times. Parallel intervals overlap and must not be summed into campaign wall time. No runtime fields or new monitoring system were added.

## Coordinator observations (UTC, 2026-09-08)

- 10:04:07 — campaign initialized (runtime started_at).
- 10:05:04 — first three native worker dispatches confirmed: discounting guide, billing configuration read, legacy plan-charge list. This observation bounds their dispatch-confirmation time; it is not an exact per-agent start timestamp.
- 10:09:02 — discount worker result received/accepted; independent discount reviewer dispatched immediately afterward.
- 10:09:28 — plan-charge worker result received/accepted; independent plan-charge reviewer dispatched immediately afterward.
- 10:09:59 — billing-configuration worker result received/accepted; candidate queued for review. End-date worker dispatched immediately afterward to retain an active worker while two reviewers run.
- 10:13:14 — discount reviewer approved attempt 1; billing-configuration reviewer dispatched immediately afterward (candidate queue interval about 3m15s).
- 10:13:48 — discount source and its two approved reciprocal concept entries promoted; coordinator promotion interval from reviewer result about 34s, including next-review dispatch.
- 10:14:20 — plan-charge reviewer approved attempt 1; final Anrok worker dispatched immediately afterward.
- 10:14:47 — plan-charge source and its two approved reciprocal concept entries promoted; coordinator interval about 27s, including next-worker dispatch.
- 10:15:10 — end-date worker result received/accepted; independent end-date reviewer dispatched immediately afterward.
- 10:18:08 — billing-configuration reviewer approved attempt 1.
- 10:18:09 — billing-configuration source and its approved concept entry promoted. Final audit Group A (six questions for the first three promoted sources) dispatched immediately afterward, overlapping remaining worker/reviewer tasks.
- 10:19:11 — Anrok worker result received/accepted; independent Anrok reviewer dispatched immediately afterward. All five worker attempts have returned. The runtime was given two available campaign slots because Group A occupied the third native slot; this is a per-call capacity bound, not a configuration change.
- 10:24:00 — Anrok reviewer approved attempt 1; Group A report received (6/6 PASS). Group A records a self-timed audit interval of 10:18:48–10:21:53; coordinator dispatch-to-receipt is longer and includes startup, artifact checking and handoff.
- 10:24:13 — Anrok source and two approved concept updates promoted.
- 10:24:44 — end-date full review result read: two bounded blockers, targeted retry. The first result-consumption call lacked the worker assignment required by the existing immediate-retry scheduler and failed before persistence; no duplicate attempt was created.
- 10:25:05 — end-date review recorded and attempt 2 dispatched to the same worker. Correction scope is only can-versus-must wording (source plus main concept suggestion) and the request-example locator; no new full analysis requested.
- Immediately after attempt-2 dispatch — Group B auditor dispatched for the already-promoted Anrok pair; end-date pair will be added after its promotion, without duplicating either pair.
- 10:26:55 — bounded worker correction received/accepted; original end-date reviewer resumed for targeted review only (worker correction interval about 1m50s).
- 10:28:37 — targeted end-date review approved (about 1m42s); all five sources approved, 4/5 on first attempt.
- 10:28:39 — corrected end-date source and its three approved shared updates promoted; remaining Group B pair sent to the existing auditor.
- 10:29:26–10:29:27 — consolidated company/provider-index/provider-log updates applied after preparation; coverage counts updated once.
- 10:30:00 — main close checks passed approval, candidate equality, hashes, ten exact approved updates, reciprocal section placement and catalogs, then the ad hoc count assertion mistakenly expected 197 official records instead of 191.
- 10:31:10 — corrected count and 13-file typed wiki checks passed, capsule has no errors. An unnecessary diagnostic comprehension rebuilt the full link index for each link; it was stopped. This coordinator mistake added roughly a minute of diagnostic work; existing validators and runtime were not changed. The original once-built index-link check had already passed.
- 10:32:44 — Group B final 4/4 report received and read. Its self-timed pairs were 10:25:56–10:28:11 (Anrok) and 10:29:29–10:31:10 (end date); delivery includes additional report and handoff latency.
- 10:33:17 — single combined quality audit persisted and runtime marked complete.

## Stage cost

These are overlapping wall-clock windows, not additive accounting buckets. Work starts and completions are coordinator observations unless explicitly labelled auditor self-timing.

| Stage | Observed UTC interval | Cost and interpretation |
| --- | --- | --- |
| Initialize and first dispatch confirmation | 10:04:07–10:05:04 | 57s |
| First-attempt worker delivery window | 10:05:04–10:19:11 | 14m07s; includes later workers waiting for a slot and overlaps reviews |
| Independent review window, including targeted review | 10:09:02–10:28:37 | 19m35s; overlapping reviewer jobs, not serial time |
| End-date correction loop | 10:24:44–10:28:37 | 3m53s: about 21s coordination, 1m50s worker fix, 1m42s targeted review |
| Incremental promotion | 10:13:14–10:28:39, intermittently | Five recorded approval-to-promotion intervals total about 1m17s, including adjacent dispatch/reading work; not 15 minutes of active writing |
| Final audit window | dispatch after 10:18:09 to receipt 10:32:44 | About 14m35s with overlap, delayed page availability and handoff; auditor self-timed task blocks total 7m01s |
| All sources promoted to operational close | 10:28:39–10:33:17 | 4m38s: catalog/log aggregation, mechanical checks and diagnostic correction, remaining audit/report handoff |

### Per-page first-attempt observations

The first three worker orders were persisted at approximately 10:04:17 (observed input-file mtimes before review overwrote input.json), while all three native dispatches were confirmed by 10:05:04. Their worker durations below use the latter common observation point and may understate startup by up to 47s. Later dispatches immediately followed their recorded observation. Review durations include startup, tool calls, artifact checks and delivery, not just inference.

| Page | Worker observed interval | Full initial review | Review queue |
| --- | ---: | ---: | ---: |
| Discounting guide | 3m58s (+ up to 47s startup) | 4m12s | approximately immediate |
| Billing configuration lookup | 4m55s (+ up to 47s startup) | 4m54s | 3m15s |
| Legacy Plan charges | 4m24s (+ up to 47s startup) | 4m52s | approximately immediate |
| Contract end date | 5m11s | 9m34s | approximately immediate |
| Anrok token | 4m51s | 4m49s | approximately immediate |

The end-date reviewer reported full raw/candidate checking plus shared-context and reciprocal-route checking before finding two bounded blockers. There is no finer instrumentation proving how the 9m34s divided among those activities. Do not attribute all of it to concept reading or all to model speed. Independent full-review intervals total 28m21s across agents; they overlap, so this is not campaign elapsed time.

## Quality and comparison

- Source scope remained small: five final sources average 292.2 whitespace-delimited words including frontmatter/navigation (discount 353, fetch 317, Plans 241, end-date 337, Anrok 213). Raw input totals 1,364 lines.
- Ten shared updates across six existing concepts: eight navigation entries and two supported factual additions. Concept prose was not mandatory for every page; important lifecycle and credential-scope facts remained allowed.
- One first attempt overstated raw's available action (`can`) as a requirement (`must/requires`) and pointed to the wrong request-example node. Both were corrected narrowly without a full rereview. This is an accuracy/locator defect, not evidence that more implementation detail is needed.
- Query routes passed 10/10. Both auditors also ran supplementary gap sweeps under existing query rules; do not label this a zero-search audit. No additional raw became answer evidence and no broken route needed repair.
- C37: 27m52s, 3/5 first-pass, 1,989 raw lines. C38: 22m59s, 5/5, 1,111 lines. C39: 29m10s, 4/5, 1,364 lines. C39 is 6m11s slower than C38; different page mix, one correction loop, longer end-date initial review, queueing and coordinator diagnostic overhead limit causal conclusions. No token-saving percentage is measured.

## Small next improvements, not a new framework

1. The required per-agent instruction chain contains approximately 10,157 whitespace-delimited words across CLAUDE.md, ingest rules, provider rules, and C37–C39/retrieval contracts, before raw. This is a fixed context/reading cost, not a measured token bill or proven latency cause. A separately approved cleanup could make the current contract the direct entry and move historical campaign exceptions out of the hot path while preserving every active quality gate. Do not add another layered playbook.
2. Make approved manifest order match the intended advisory dispatch order before execution; the existing scheduler already supports dynamic slots. No scheduler feature is needed.
3. Preserve modal strength in retained claims and verify the exact raw locator when writing it. These are focused checks within the existing worker contract, not a new provider invariant list or another reviewer stage.
4. For a bounded retrieval audit whose indexed route already answers the question, consider separately approving a narrower gap-sweep policy; this run followed the current query rule and must not be reported as search-free. Do not silently weaken the rule in a running campaign.
5. Reuse correct capsule count fields and compute the link index once in coordinator checks. This fixes our verification procedure, not ingestion logic or the repository validator.

## Closure evidence

All five final sources equal approved candidates modulo final newline. Raw hashes, approved suggestion presence/placement, reciprocal links and catalogs passed. Thirteen typed wiki files passed validation, capsule validation reported no errors, and counts reconcile to 197 total sources, 191 official documentation source records, 95 raw snapshots without source summaries, and 35 uncovered canonical identities in the frozen inventory. Raw and unrelated files were not edited. This campaign extends only the existing provider-specific documentation authorization; it adds no executable rules, runtime schema, tests, model routing or monitoring feature. No bulk rollout or push is authorized.

The runtime dispatched in approved manifest order. The selection note recommended starting the end-date mutation early, but it remains fourth in that order. Preserve the manifest rather than silently rewriting it during execution; evaluate any resulting tail latency in this retrospective.
