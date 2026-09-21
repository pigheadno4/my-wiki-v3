# Braintree C04 execution notes

Status: COMPLETE. Exact five-page manifest approved on 2026-09-20.
Started 2026-09-20T13:07:28Z; completed 2026-09-20T13:24:29Z.
Operational wall time: 17m01s, excluding post-close reporting.
See campaign.json for authoritative start/end UTC.
Five hashes verified and source targets absent before runtime initialization.
Baseline cumulative source count: 31. Initial three worker orders persisted and
dispatched individually: Tokenization Key, Webhook Testing, Nonce Find.
Sol medium workers, independent Sol high reviewers, three dynamic child slots.
Coordinator owns all canonical writes; no collection, GitHub ingest, commit/push
or next campaign authorized. Observed stage timings follow; intervals may overlap.

| Role | Start UTC | End UTC | Duration |
| --- | --- | --- | --- |
| Key worker | 13:08:14 | 13:10:23 | 2m09s |
| Testing worker | 13:08:44 | 13:10:37 | 1m53s |
| Find worker | 13:08:56 | 13:10:45 | 1m49s |
| Key initial review | 13:11:17 | 13:12:32 | 1m15s |
| Testing initial review | 13:11:29 | 13:12:22 | 53s |
| Create worker | 13:12:30 | 13:13:52 | 1m22s |
| Find initial review | 13:13:38 | 13:15:20 | 1m42s |
| Delete worker | 13:14:05 | 13:15:03 | 58s |
| Create initial review | 13:15:14 | 13:17:02 | 1m48s |
| Delete initial review | 13:15:55 | 13:16:53 | 58s |
| Query audit A | 13:16:45 | 13:18:15 | 1m30s |
| Create targeted correction | 13:18:04 | 13:18:56 | 52s |
| Create targeted review | 13:19:45 | 13:20:14 | 29s |

All three initial handoffs passed runtime validation. Key and Testing reviews
dispatched; Create worker filled the worker reserve while Find awaits review.

Key/Testing promoted by 13:13:54Z. Find review analysis ended 13:15:00Z,
artifact verification/handoff ended 13:15:20Z. Find approved and promoted;
Create/Delete reviews run alongside the Key/Testing four-question audit.

Initial approvals: 4/5. Create source and quotes passed; only shared concept
wording hardened the raw's should-only guidance into an unqualified restriction.
Original worker corrected that route and warning without changing the source
or quotes; original reviewer handles targeted diff/context review.
Audit A: 4/4 PASS, zero extra raw reads or repairs; analysis ended 13:17:32Z,
handoff 43s later. No new concepts or new validation mechanism.

All five jobs approved after targeted review ended 13:20:14Z. Final source
promoted and audit B dispatched, then company/index/log aggregate and mechanical
checks completed by 13:21:54Z. Count: 36 cumulative sources (20 website +16 GitHub).
One close pass checked five unchanged hashes, exact candidate/receipt equality,
canonical identity, raw ownership, approved reciprocal updates, single catalog
entries and counts. Generic validator passed 10 typed pages, git diff --check
passed; mechanical check duration 0.68s. No coordinator semantic repairs.

## Final outcome and stage timing

- Five sources ingested, first-pass approvals 4/5; five full initial reviews and
  one targeted review. One concept-only correction; source/quotes unchanged.
  Zero full retries, coordinator semantic repairs, new concepts or audit repairs.
- Audit B: 13:21:25–13:23:48Z (2m23s). Analysis ended 13:23:42Z; handoff 6s later.
  All six questions passed. Combined audit: 10/10 PASS, zero extra full raw reads.
- Runtime complete, 36 cumulative sources (20 website +16 GitHub). All primary
  raws unchanged; all canonical sources equal their latest approved candidates.
- No collection, GitHub ingest, commit, push or next campaign executed.

| Non-overlapping wall-time window | Duration | Meaning |
| --- | --- | --- |
| Start → all reviews approved, 13:20:14Z | 12m46s | Dispatch, drafting, review, one bounded correction; audit A overlaps |
| All approved → aggregation/check confirmed, 13:21:54Z | 1m40s | Final promotion and shared-file close; audit B starts concurrently |
| Aggregate complete → audit B handoff, 13:23:48Z | 1m54s | Remaining final query audit |
| Audit handoff → runtime close, 13:24:29Z | 41s | Accept report, archive evidence and close runtime |

C03 took 22m39s; C04 took 17m01s, 5m38s shorter (about 25%). This is observed
wall time, not proof of a general throughput gain: content mix differs and C03
required post-audit conflict repair. Mechanical checks are not the bottleneck.
The correction itself took 52s and targeted review 29s; elapsed time from initial
changes_requested at 13:17:02Z to approval 13:20:14Z was 3m12s, including 1m51s
of intervening dispatch/start/handoff time. Continue reducing those gaps within
the existing runtime; do not add a scheduler, new review tier or blanket adjacent
raw reads. Preserve advisory modal words in concept routes as well as sources.
