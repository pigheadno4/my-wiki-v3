# Campaign 40 retrospective

Status: complete. Five sources promoted; 10/10 final retrieval questions passed after correcting one audit-agent object-selection error. First-pass approvals: 3/5. Runtime closure: 1,931 seconds (32m11s), from 13:22:55 to 13:55:06 UTC. The 35-minute observation target was met, but the 4/5 first-pass target was not. This was 3m01s longer than C39 (29m10s), not a demonstrated speed improvement.

## Timing method

Use runtime started_at/completed_at for operational elapsed time, coordinator UTC observations for dispatch/result/promotion boundaries, and agent-reported UTC intervals when available. Existing events.jsonl has event order, not timestamps. Intervals include tool and handoff latency, overlap across agents, and cannot be summed into total wall time. Post-close report/commit time is separate. No runtime fields or monitoring system were added.

## Coordinator observations (UTC, 2026-09-08)

- 13:22:55 — runtime initialized and trusted first-three worker orders returned; native dispatches immediately followed in manifest order (rates, archive, threshold).
- 13:27:44 — threshold worker result accepted and independent reviewer dispatched. Worker-reported interval: 13:24:04–13:27:31 (3m27s); result-to-review handoff approximately 13 seconds plus native dispatch latency.
- 13:28:20 — archive worker result accepted and independent reviewer dispatched. Worker-reported interval: 13:23:41–13:27:54 (4m13s).
- 13:28:40 — rates worker result accepted; reviewer queued while the final slot starts the Plan-customers worker, preserving one active worker. Rates worker-reported interval: 13:23:28–13:28:12 (4m44s).
- 13:32:49 — archive first review accepted; rates reviewer dispatched after approximately 4m09s persisted queue time. Archive reviewer-reported interval: 13:28:47–13:32:36 (3m49s).
- 13:33 — threshold first review accepted and Avalara worker dispatched. Threshold reviewer-reported interval: 13:28:14–13:32:28 (4m14s); minute precision for this coordinator boundary.
- 13:33:44 — archive and threshold approved concept updates and exact candidates promoted. This approximately 55-second window overlaps rates-review and Avalara-worker dispatch, and is not pure file-write time.
- 13:34:15 — Plan-customers result accepted and reviewer dispatched. Worker-reported recorded interval: 13:31:23–13:33:32 (2m09s); this start was recorded well after its 13:28:40 dispatch, so it does not measure the full worker occupancy window.
- 13:37:28 — rates first review accepted and approved concepts/source promoted; Group A's six-question query audit dispatched immediately afterward. Rates reviewer-reported interval: 13:33:32–13:36:59 (3m27s).
- 13:38:03 — Avalara worker result accepted and reviewer dispatched, with the runtime capacity reduced to two because the third slot is occupied by the query auditor. Worker-reported interval: 13:34:06–13:37:24 (3m18s). All five first worker results have now been received.
- 13:39:06 — Plan-customers first review requested a bounded correction for the retained comma-separated status claim versus the scalar enum. Same worker dispatched for attempt 2 and targeted rereview planned. Reviewer-reported interval: 13:35:02–13:38:38 (3m36s); no full rereview requested.
- 13:41:50 — Plan-customers attempt 2 accepted and same reviewer dispatched for targeted diff review. Worker-reported correction interval: 13:39:36–13:41:31 (1m55s).
- 13:44:01 — Plan-customers targeted review accepted and approved concept/source promoted. Reviewer-reported interval: 13:42:20–13:43:29 (1m09s). End-to-end correction-to-promotion window: 4m55s, with no full rereview.
- 13:44 — Group B query auditor dispatched to begin the two Plan questions while awaiting Avalara promotion; minute-precision coordinator boundary.
- 13:44:59 — Avalara first review requested one bounded Error-schema locator correction; same worker dispatched for attempt 2 with runtime capacity one because both auditors occupy slots. Reviewer-reported interval: 13:38:58–13:44:33 (5m35s). Both shared suggestions were approved unchanged. Final first-pass count is 3/5; both retries are targeted.
- 13:47:18 — Avalara attempt 2 accepted and same reviewer dispatched for targeted review. Worker-reported correction interval: 13:45:27–13:46:52 (1m25s). Group B reported its two Plan questions passed and was waiting for Avalara promotion.
- 13:47–13:48 — coordinator inspected Group A report (agent interval 13:38:22–13:46:58) and found Q3/Q4 had silently substituted CREDIT for the assigned COMMIT. Those two passes are invalid; the auditor was reactivated to correct only those two questions and associated evidence/routes. Four valid rate/threshold answers remain retained. This is an audit-agent scope error, not a source defect; extra time is reported separately.
- 13:49:35 — Avalara targeted review accepted and approved concepts/source promoted; all five sources now promoted. Reviewer-reported interval: 13:47:42–13:49:06 (1m24s). Correction-to-promotion window: 4m36s. Group B notified to resume its two Avalara questions; coordinator begins one aggregate shared close and mechanical verification.
- 13:51:27 — aggregate shared close and single combined mechanical/capsule verification finished, approximately 1m52s after final promotion, overlapping both query auditors.
- 13:52:08 — Group A corrected audit completed (agent-reported); coordinator subsequently checked and preserved the report. Six valid questions pass, including the correct commit object. Auditor correction occupied 3m59s, overlapping Group B and final mechanical checks rather than adding its full duration to wall time.
- 13:53:52 — Group B completed (agent-reported), 4/4 pass, including the needed account-level provider-list raw read. Its 8m47s interval includes an unmeasured wait for Avalara promotion; do not treat the whole interval as active query analysis.
- 13:55:06 — both audit reports checked and preserved; aggregate quality report recorded; runtime marked complete. Audit-end to close overhead was 1m14s. Final report/staging/commit time is post-close overhead, not included in the 32m11s runtime.

## Closure verification

One aggregate shared close updated the company and provider catalogs/counts/log and enriched existing concept-index descriptions. One combined mechanical check passed across 13 typed wiki files, all provider-index wikilinks, five exact source/candidate/receipt matches, pinned raw hashes, nine exact-once approved updates in their intended sections, reciprocal source/concept links, and unique company/index catalog entries. Capsule validation returned no errors. Counts reconcile to 202 total source summaries, 196 official-documentation sources, 90 raw snapshots without source summaries, and 30 remaining canonical identities in the frozen inventory. `git diff --check` passed. No code/rules/validators changed in this campaign, so no full unit-suite rerun was needed.

Final source word counts (whitespace-split, including frontmatter): rates 398, archive commit 276, threshold guide 350, Plan customers 356, Avalara 291; total 1,671.

## Stage measurements

These intervals overlap; do not sum them to obtain wall time.

| Stage | Observed duration | Interpretation |
| --- | ---: | --- |
| Initial worker pipeline | 15m08s | Runtime start 13:22:55 to last first-result acceptance 13:38:03, including delayed launches, queueing and handoffs |
| Individual initial workers, self-reported | 2m09s–4m44s | Plan worker start was recorded late; its dispatch-to-completion window was about 4m52s |
| Five initial reviewers, self-reported | 3m27s–5m35s each | Total active intervals 20m41s, overlapping workers and each other |
| Rates ready-review queue | 4m09s | 13:28:40–13:32:49; one slot was used to keep pending worker work moving |
| Plan bounded correction through promotion | 4m55s | Worker 1m55s, targeted review 1m09s, remainder dispatch/handoff/promotion |
| Avalara bounded correction through promotion | 4m36s | Worker 1m25s, targeted review 1m24s, remainder dispatch/handoff/promotion |
| Last source promoted | 26m40s from start | 13:49:35; no full rereview was run |
| Aggregate catalogs/log + mechanical/capsule verification | about 1m52s | 13:49:35–13:51:27, overlapping query audits |
| Group A initial query audit | 8m36s | Six questions attempted; two wrong-object answers were invalidated |
| Group A wrong-object correction | 3m59s | Only commit questions rerun; not a worker/source failure |
| Group B audit including promotion wait | 8m47s | 13:45:05–13:53:52; four questions, one additional full raw authority |
| Final audit report acceptance and runtime close | 1m14s | 13:53:52–13:55:06 |
| Operational total | 32m11s | Runtime timestamps; overlapping stages above are not additive |

## Findings and small next-step suggestions

- First-pass rate is 3/5 (60%), below the 4/5 observation target. Both failures concern retained technical detail: a description-versus-enum conflict and an inline-versus-reference schema locator. Neither required broad semantic reconstruction.
- Bounded corrections worked: two targeted reviews, zero full rereviews, and zero coordinator semantic repairs. Keep this behavior; do not interpret small corrections as reasons to restart whole-page analysis.
- Compact instructions did not guarantee faster end-to-end closure. Five initial full reads/reviews, dynamic-slot queueing, two correction handoffs, and final query audit still dominate. Different raw pages/risks preclude causal comparison with C39 or claiming measured token savings from instruction word counts.
- The approved outputs still carry optional schema requiredness and detailed technical assertions into sources, and three dense factual additions into concepts. A future, separately approved change should first narrow those retained facts and prefer purpose-fit concept routes, rather than adding another playbook, registry, review layer, or timing subsystem.
- The audit error suggests one small dispatch discipline: before answering, echo the requested object and verify the selected source/raw operation is that object (commit versus credit). This is a proposed check, not an implemented classifier or additional full audit.
- Keep the current exact raw provenance and initial independent-review control for now. This sample does not justify a wider rollout or review waiver. No next campaign or push has been started.
