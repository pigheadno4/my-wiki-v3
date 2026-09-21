# Braintree C07 execution notes

Status: COMPLETE. Exact five-job manifest approved on 2026-09-20.
Operational closure: 14:35:15–14:48:13Z, 12m58s. Final audit 10/10 PASS.
Initial worker handoffs 5/5; initial content approvals 5/5; no retries, full
rereviews, targeted rereviews, coordinator semantic repairs or post-audit repairs.
All raw hashes, canonical ownership and absent source targets rechecked. C06 is
closed. Three initial trusted orders persisted and native Sol medium workers
confirmed: Address Create, Dispute Webhooks and Address Update. No startup
capacity error. Baseline 46 sources (30 website +16 GitHub).

Actual start/end come from campaign.json. Role intervals may overlap; record
observations without reconstructing missing dispatch/queue timestamps.
Only coordinator writes repository files. No collection, GitHub ingest,
code/rule changes, commit/push or subsequent campaign authorized.

| Role | Actual reported start UTC | Handoff end UTC |
| --- | --- | --- |
| Dispute Webhooks worker | 14:36:05 | 14:38:00 |
| Address Update worker | 14:36:20 | 14:38:08 |
| Address Create worker | 14:36:18 | 14:38:54 |

All three initial worker receipts accepted without format repair. At the next
dispatch, fresh Address Delete spawn hit native thread limit. No duplicate agent
started; the persisted order/identity bt07-w-delete was delivered to the idle
Sol medium Create worker using followup_task. Model and one-page ownership remain
unchanged; that agent will not independently review its own pages.

| Further role | Reported start UTC | End UTC |
| --- | --- | --- |
| Address Delete worker | 14:39:51 | 14:40:54 |
| Plan All worker | 14:41:37 | 14:42:51 |
| Dispute Webhooks initial review | 14:38:59 | 14:40:21 |
| Address Update initial review | 14:39:31 | 14:41:10 |
| Address Create initial review | 14:41:14 | 14:41:51 |
| Address Delete initial review | 14:42:29 | 14:42:59 |

Five initial worker receipts accepted; no format retry. Four initial reviews
approved without corrections. Dispute/Create/Update promoted before 14:43:15Z;
Audit A dispatched immediately after Create promotion and overlaps final reviews.
Delete then approved/promoted. Reused idle independent Sol high reviewers for
subsequent jobs; reviewer identities remain distinct from each page's worker.
Some reported review starts follow dispatch; these are observed reading/review
windows, not proof of complete dispatch-to-return latency.

Plan All first review: reported 14:43:46–14:44:17Z. Approved and promoted without
changes; Audit B dispatched immediately afterward, before shared aggregation.
Audit A: actual start 14:43:03Z, analysis end 14:44:06Z, handoff 14:44:09Z
(1m03s analysis, 3s handoff), 4/4 PASS, no additional raw evidence or repairs.

By 14:46:02Z, shared aggregation and the single mechanical close check passed:
five exact approved candidates, pinned hashes, canonical identity, unique raw
ownership, approved reciprocal updates, unique catalog entries and count51.
Generic typed validator passed all10 touched pages (five sources, three concepts,
company and provider log); git diff --check passed. Audit A's pending aggregate
observation is resolved. No new concept; disputes received one existing-concept
cross-cutting route in addition to the two provider concepts.

Audit B: reported actual start 14:45:21Z, analysis end 14:46:23Z and artifact
handoff 14:46:46Z (1m02s analysis plus23s report). Final completion message was
received later; coordinator inspected and closed at14:48:13Z. Do not equate the
artifact's reported handoff timestamp with coordinator receipt/acceptance.
Six questions PASS, no extra selected raw reads and no repair.

## Stage observations

| Stage | Observed UTC window | Duration/window |
| --- | --- | --- |
| Initialization to final worker handoff | 14:35:15–14:42:51 | 7m36s |
| Initial review windows (overlap workers) | 14:38:59–14:44:17 | 5m18s |
| Query audit A | 14:43:03–14:44:09 | 1m06s |
| Query audit B | 14:45:21–14:46:46 | 1m25s |
| Final promotion/aggregate/check | after14:44:17, done by14:46:02 | at most1m45s |
| Audit B artifact handoff to closure | 14:46:46–14:48:13 | 1m27s |

These overlapping windows are not additive model compute durations. No token or
cost total is claimed. C07 operational closure is6m22s shorter than C06's19m20s,
but C07 has184 raw logical lines versus C06's403 and no format retry; it does not
prove a causal workflow speedup. The operational refinements were actually used:
all five worker status fields passed first time; both audit groups were dispatched
as their sources became live, before aggregate/report work; A overlapped remaining
reviews and B overlapped aggregation. Native thread-cap recovery reused eligible
idle roles without a new thread-management subsystem.

No further architecture or validator changes are justified by this run. Retain
the same handoff reminder and early audit dispatch. The residual tail includes
message delivery, coordinator acceptance and report closure, not failed ingestion.
No raw changes, collection, GitHub ingest, commit/push or next campaign executed.
