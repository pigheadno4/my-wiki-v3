# Braintree C10 execution notes

Status: COMPLETE. Ten-page manifest approved2026-09-21. Runtime start11:15:32Z.
All ten hashes/absent targets/canonical owners verified; C09 closed. Baseline61
sources:45 website+16 GitHub. Initial three Sol medium workers confirmed with
persisted orders for Payment Method Create/Update and Subscription Search.
No running prior agents or startup capacity failure. Three dynamic child slots
include audits; different Sol high reviewers; coordinator-only repository writes.
No collection/raw edits, GitHub work, code/rule changes, commit/push or next campaign.

Initial worker observations: Create11:16:30–11:18:45Z; Update11:16:21–11:19:19Z;
Search11:16:48–11:18:54Z. Three receipts accepted first time. Create/Search reviewers
dispatched; Update worker reused for Retry Charge under its new persisted identity.

Retry worker11:20:17–11:21:37Z; Grant worker11:22:09–11:23:05Z. Five receipts
accepted first time, no format correction. Create review11:19:04–11:21:16Z approved.
Search approved, but its reported11:21:29–11:21:34Z is a final-recording observation,
not credible complete role latency; exclude it from reading-speed comparisons.
Create/Search promoted; Update/Retry reviews live and Revoke worker started.

Update first review11:22:10–11:24:09Z requested one bounded material warning fix:
AVS verifyCard transaction/CVV rejection action missing from retained source and
concept route. Targeted retry authorized; no full-analysis retry. Original worker
corrected11:26:55–11:28:23Z: warning, line223 locator, expanded quote5 and reciprocal
vocabulary only; original reviewer will check bounded diff/context.
Revoke worker11:23:34–11:24:28Z; Transaction Webhooks11:25:00–11:26:18Z.
Grant review11:25:27–11:26:31Z approved. Retry review11:22:46–11:23:25Z approved.
Query group B11:24:30 start,11:25:39 analysis end,11:25:47 handoff:4/4 PASS.
Account Updater worker now running; no format retries or thread-cap failures.

Transaction Webhooks review11:27:16–11:28:31Z approved; reviewer additionally fully
read existing overview raw to substantiate scope comparison. This is an actual
extra authority read, not a retry. Update targeted review11:29:19–11:30:17Z approved;
no full rereview. Source promoted, audit A started while remaining jobs continued.
Account worker11:29:07–11:30:05Z; Fraud worker11:30:37–11:31:26Z. Address Find now
running. Revoke review latency longer than other short pages; coordinator requested
blocker/status rather than starting a duplicate review or treating delay as failure.

## Final outcome and timing

Runtime completed2026-09-21T11:42:03Z:26m31s elapsed,159.1seconds per accepted
page. All10 approved and promoted; first worker-format acceptance10/10, first
content review9/10. Ten initial full reviews, one targeted rereview; one bounded
worker correction, zero full-analysis retries, zero full rereviews, zero
coordinator semantic repairs. Query audit20/20 PASS; one mechanical close with
14 typed pages, hashes/candidate equality, reciprocal routes, unique ownership,
catalogs and counts passed.71 sources=55 website+16 GitHub. No new concept.

Remaining observed worker window: Address11:31:58–11:32:48Z. Initial worker
analysis windows overall11:16:21–11:32:48Z (16m27s span, not summed effort).
Update correction11:26:55–11:28:23Z overlapped other jobs. Reviews and promotions
also overlapped workers, so these windows must not be added into elapsed time.

Remaining reviewer observations: Account Updater11:34:35–11:34:44Z, reported
handoff11:35:12Z; Fraud11:37:34–11:38:13Z, handoff11:38:43Z;
Address11:38:05–11:38:22Z, handoff11:38:46Z. Overall reviewer window begins
11:19:04Z and final reported handoff is11:38:46Z (19m42s span including queue,
setup and delivery, not19m42s of model analysis). Very short self-reported
analysis intervals do not establish total role latency.

Revoke reported analysis11:27:11–11:28:24Z but its artifact/result was handed
back around11:34Z. This unexplained roughly5–6minute gap occupied a reviewer
slot; no content blocker or retry was reported. Do not relabel this gap as
raw-reading time or infer a transport root cause without evidence.

Audit reported windows (start → analysis end → handoff):
- A:11:31:27 →11:32:52 →11:32:57Z.
- B:11:24:30 →11:25:39 →11:25:47Z.
- C:11:38:37 →11:39:14 →11:39:19Z.
- D:11:39:21 →11:39:58 →11:40:45Z.
- E:11:39:59 →11:40:39 →11:40:43Z.

Audit work overlapped remaining reviews/promotions. Final aggregate/mechanical
work ran during the last audit groups; audit acceptance, report assembly and
runtime close finished11:42:03Z. Exact isolated coordinator active time and
transport delay are not measured; journal events lack reliable per-stage clocks.
Post-close retrospective/status writing is separate from operational duration.

## What the ten-page pilot establishes

Ten pages fit existing ownership/runtime controls without new machinery; quality
stayed acceptable with9/10 first reviews and20/20 queries. It did NOT demonstrate
a speedup: C09 was12m40s for5 (152seconds/page), versus159.1seconds/page here,
about4.7% slower per page. The page mixes differ, so this is descriptive rather
than causal. Two C09-sized runs would total25m20s,71seconds less than this run.

The one bounded correction did not cause repeated full reads. Observed latency
is concentrated in many role handoffs/queues and the delayed Revoke result,
not a flood of failed reviews. Reporting remains more verbose than necessary:
future existing-schema reasons should state blockers/verdict/evidence succinctly;
query answers still retain required object/action, answer, locator and verdict.
Keep prompt completion-to-handoff immediate, avoid stylistic polishing, and
continue ready-group audits while remaining reviews run. These are execution
discipline improvements, not another validator, scheduler or registry. Do not
claim that increasing campaign size alone reduces per-page cost, and do not
waive independent review or change campaign scope without separate approval.

All C10 assigned agents have returned their final results; idle/completed agent
records do not by themselves prove thread-resource release. No commit/push or
next campaign executed; unrelated working-tree changes preserved.
