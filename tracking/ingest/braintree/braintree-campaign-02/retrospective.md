# Braintree C02 execution notes

Status: COMPLETE. Started 2026-09-19T12:00:40Z; closure confirmed by
2026-09-19T12:20:47Z. Campaign wall time through closure: 20m07s.
Exact five-page manifest approved.
No commit, push, collection or subsequent campaign authorized.

## Timing observations

- By 12:01:52Z, three individually persisted trusted orders had been dispatched
  to confirmed Sol medium workers: Hosted Fields events, Node Refund and Node
  webhook parsing. No other active child agents at preflight.
- All five pinned raw hashes verified; all five source targets absent. Baseline
  21 cumulative source summaries (16 GitHub plus five website), excluding GitHub
  changelog pages. No new runtime/schema/validator changes in this campaign.
- Role timing, first-pass results, promotion and audit observations follow below.
  Intervals overlap; do not sum them as campaign wall time.

| Role | Start UTC | End UTC | Recorded duration |
| --- | --- | --- | --- |
| Events worker | 12:01:58 | 12:03:43 | 1m45s |
| Refund worker | 12:02:06 | 12:04:09 | 2m03s |
| Parse worker | 12:02:13 | 12:04:38 | 2m25s |
| Events initial review | 12:05:09 | 12:06:23 | 1m14s |
| Refund initial review | 12:06:06 | 12:07:43 | 1m37s |
| Nonces worker | 12:07:23 | 12:10:00 | 2m37s |
| Parse initial review | 12:07:24 | 12:10:21 | 2m57s |
| Create worker | start not recorded | 12:11:00 | unavailable; artifact written 12:10:43 |

Events approved attempt1 and promoted by 12:07:34Z; Refund approved attempt1
and promoted by 12:09:03Z. Parse attempt1 requested a bounded targeted correction:
distinguish signature parameter from signed payload and rebalance grounding quotes
to include the retained parse invocation and non-sequential/timestamp warning.
No repeated full raw analysis requested. Original worker handles the correction.

- Parse correction: 12:11:37–12:12:36Z (59s); original reviewer targeted
  rereview 12:13:19–12:13:58Z (39s), approved. Approved concept paragraphs and
  Sources entry applied literally without the proposal's instructional wrapper,
  as explicitly permitted in the review. No semantic coordinator repair.
- Nonces approved attempt1 at 12:13:19Z (review start not recorded), promoted
  by 12:14:18Z. Create full review 12:12:08–12:14:05Z (1m57s), approved attempt1.
- All five sources and corresponding concept updates promoted by 12:15:08Z;
  company/provider-index aggregate completed 12:15:27Z. Source count now 26,
  comprising sixteen GitHub and ten website summaries, excluding changelogs.
- Audit A covers Events/Refund while remaining reviews/promotions run. Audit B
  starts after final catalog aggregation for Parse/Nonces/Create. One final
  ten-question audit only, no additional full-content sampling pass.

## Closure and results

- Five sources approved and promoted. First-pass 4/5; one targeted correction
  (59s) and targeted rereview (39s). Five initial full reviews, zero full retries,
  zero semantic coordinator repairs, no new concepts.
- Audit A: 12:14:38–12:16:19Z (1m41s; analysis 1m, report 41s).
  Audit B: 12:16:07–12:18:34Z (2m27s; analysis 1m43s, report 44s).
  Combined single ten-question audit: 10/10 PASS, zero query repairs or extra
  raw reads. Groups overlap by 12 seconds; do not sum as wall time.
- Mechanical closure verified all five raw hashes, canonical candidates versus
  approved receipts, raw ownership, forward/back links, approved concept snippets,
  single company/index entries and 26 cumulative source summaries. Generic
  validator passed 10 typed pages; git diff --check passed. The ad-hoc count
  assertion initially compared the parser's string `26` with integer 26; corrected
  the check to normalize the type, with no content change. Remaining validation
  took 0.63s. Runtime then closed successfully.
- Stage windows: startup to three dispatched orders 1m12s; startup through all
  source/concept promotion 14m28s; final company/index aggregation 19s after that;
  final audit handoff at elapsed 17m54s; audit handoff through recorded closure
  2m13s. These include coordinator handoffs and overlap with role work.
- C01 first-pass 2/5 versus C02 4/5 is encouraging, not a causal benchmark:
  raw workload differs (781 versus 437 lines) and C01 had a long interruption.
- Next optimization opportunity: reduce coordinator dispatch/receipt handoff
  gaps and keep audit handoffs compact. Preserve the existing bounded correction
  path; do not add another validation framework or review round. Another five-page
  campaign requires its own manifest approval.
- No collection, GitHub ingest, commit, push, or subsequent campaign execution.
