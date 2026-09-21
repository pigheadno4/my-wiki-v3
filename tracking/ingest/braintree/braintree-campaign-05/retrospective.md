# Braintree C05 execution notes

Status: COMPLETE; initial native dispatch capacity issue reconciled.
Started 2026-09-20T13:29:22Z; completed 2026-09-20T13:44:57Z.
Operational wall time: 15m35s, excluding post-close reporting.
Exact five-page manifest approved on 2026-09-20; hashes verified and targets absent.
Baseline source count 36; authoritative start in campaign.json.

Customer Create and Payment Method Find Sol medium workers confirmed dispatched.
Third persisted order (webhooks-payment-method-node, attempt1, bt05-w-webhook)
has NO confirmed agent: spawn rejected with agent thread limit reached; attempting
to reuse completed bt04_w_find also rejected with the same message.
Runtime running for that job means order persisted, NOT actual model execution.
Do not dispatch a duplicate order or accept a fabricated worker completion.
Retain the trusted input for reconciliation if capacity becomes available.
No CLI fallback, model substitution, reviewer waiver, canonical promotion,
collection, GitHub ingest, commit or push authorized by this failure.

Reconciliation: currently listed idle bt04_w_create accepted the existing C05
webhook order as worker bt05-w-webhook, retaining Sol medium. Returned validated
handoff /tmp/bt05-webhook-worker.json; no duplicate order/attempt. Later native
reviewer dispatches succeeded. The historical unconfirmed-order warning above
no longer describes current execution state.

| Role | Start UTC | End UTC | Duration |
| --- | --- | --- | --- |
| Customer Create worker | 13:29:50 | 13:32:13 | 2m23s |
| Payment Method Find worker | 13:30:41 | 13:31:45 | 1m04s |
| Payment Method Webhook worker | 13:31:15 | 13:32:35 | 1m20s |
| Payment Method Find review | 13:32:43 | 13:34:12 | 1m29s |
| Customer Create review | 13:33:56 | 13:34:57 | 1m01s |
| Customer Delete worker | 13:33:53 | 13:35:26 | 1m33s |
| Payment Method Webhook review | 13:35:29 | 13:36:57 | 1m28s |
| Customer Find worker | 13:36:01 | 13:37:21 | 1m20s |
| Customer Delete review | 13:36:38 | 13:37:32 | 54s |
| Customer Find review | 13:38:41 | 13:39:35 | 54s |
| Query audit A | 13:37:50 | 13:39:48 | 1m58s |

All three handoffs passed runtime checks. First two reviews dispatched;
Customer Delete worker fills the remaining worker slot.

First four sources approved and promoted. Customer Find review runs alongside
the first four-query audit group. No changes_requested or full retries so far.
Role windows are reported observations, not sums of campaign wall time.

All five initial reviews approved, zero retries. Audit A: 4/4 PASS, zero extra
full raw reads or repairs; analysis ended 13:39:32Z, handoff 16s later.
Final promotion followed by audit B dispatch and one shared close aggregate.
By 13:41:20Z company/index/log aggregation and mechanical validation complete:
five hashes/candidate equality/canonical identities/raw owners, approved reciprocal
routes, duplicate catalogs, count41 and nine typed pages all pass; git diff --check
passes. Mechanical duration 0.62s. No coordinator semantic repairs.

## Final outcome and stage timing

- Five initial approvals (5/5), five full initial reviews, zero retries or
  targeted reviews, zero coordinator or query repairs. Five canonical sources
  equal their approved candidates; two existing concepts updated, no new concepts.
- Audit B actual start 13:42:16Z, analysis end 13:42:57Z, handoff 13:44:19Z.
  Duration 2m03s, including 1m22s between analysis end and final handoff.
  Combined audit 10/10 PASS; zero extra full raw reads or unresolved conflicts.
- Cumulative count41: 25 website +16 GitHub source summaries, excluding changelogs.
  Missing upstream prose/code remains an explicit evidence gap; not invented or
  repaired by ingestion. Raw hashes unchanged. No collection, GitHub ingest,
  commit, push or next campaign executed.

| Non-overlapping wall-time window | Duration |
| --- | --- |
| Runtime start → all initial reviews approved, 13:39:35Z | 10m13s |
| All approved → aggregation/check confirmed, 13:41:20Z | 1m45s |
| Aggregation complete → audit B handoff, 13:44:19Z | 2m59s |
| Audit handoff → runtime close, 13:44:57Z | 38s |

C04 was 17m01s; C05 is 15m35s, 1m26s shorter. This is an observation, not a
controlled speed comparison: C05 had no correction and a different page mix.
The useful remaining optimization is still handoff/report latency: audit B's
41s reported analysis was followed by 1m22s reporting/completeness handoff. Keep
one compact completeness check, do not reduce raw reading or add validators.
No permanent thread-limit workaround was built; reuse of an existing idle worker
reconciled the one persisted order without altering model or reviewer controls.
