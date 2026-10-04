# Braintree C36 timing and observations

Status: complete. Runtime started 2026-10-04T06:46:10Z; completed 2026-10-04T07:16:48Z. Total 30m38s. No commit or push.

- Primary volume: 2,096 lines / 17,301 words, twenty AIB AF/BF pages. C35: 2,216 lines / 16,606 words. Differing content prevents a concurrency-only performance claim.
- First worker handoff: 2026-10-04T06:47:51Z; full review dispatched immediately while remaining workers were filled.
- Initial role pool reached ten shared child roles (workers/reviewers), not ten simultaneous workers. A fresh reviewer spawn and a follow-up to an evicted completed agent hit host thread limit. Live inventory showed one retained completed C35 auditor; following up that exact listed agent succeeded as the independent C36 reviewer. No configuration change or review waiver; trusted pending review order preserved.
- System Python encountered the known Xcode-license issue for one worker's optional local check; coordinator uses the bundled Python runtime for required acceptance validation. No runtime installation or repair.

The milestone windows below are elapsed wall-clock windows, not additive role execution costs; worker/reviewer/query work overlaps.

- Last initial worker artifact mtime: 2026-10-04T07:01:00Z (14m50s from initialization). The overview worker reported local 15:01 as Z; filesystem UTC confirms 07:01. No time claim is derived from that mislabeled message.
- Last full initial review handoff: 2026-10-04T07:04:08Z. Last bounded targeted review: 2026-10-04T07:07:30Z. First pass 18/20, twenty full initial reviews plus two targeted reviews; zero repeated full reviews and zero schema-rejected or normalized worker handoffs.
- First correction: BF pricing source repeated a binary Pricing Schedule classifier while only its shared suggestion preserved the separate IC++ identification gap. Two source passages now make the conflict explicit; quotes/suggestions/other bytes unchanged.
- Second correction: AF funding overview incorrectly placed settlement batching after settlement. One sentence now preserves batching-to-confirm-settlement followed by post-settlement AIB disbursement; all other bytes/quotes/suggestions unchanged.
- All twenty sources promoted and catalogs/counts ready by 2026-10-04T07:08:22Z (22m12s). Count 392=375 website+17 GitHub. Six existing concepts updated; no new concepts. Source volume 12,233 words. Every main concept already had a provider-index route; no index-edge repair.
- Initial structural close passed at 07:08:22Z: candidate equality, hashes, canonical/primary ownership, approved updates, source/concept/raw/index reciprocal routes, catalogs/counts. Query groups overlap promotion; A analysis/handoff 07:05:38/07:06:05; B 07:06:09/07:07:50. Keep those overlapping milestones separate from additive windows.

## Final stage windows

| Milestone window | Elapsed |
| --- | --- |
| Initialization to last initial worker artifact | 14m50s |
| Remaining initial-review tail, to 07:04:08Z | 3m08s |
| Targeted correction tail, to 07:07:30Z | 3m22s |
| Promotion/catalog/structural-close tail, to 07:08:22Z | 52s |
| Remaining query-analysis tail, to 07:10:57Z | 2m35s |
| Report delivery/persistence, final logs, typed validation and runtime close | 5m51s |
| Total | 30m38s |

- Query groups A–E passed 40/40 without post-audit correction. C analysis/handoff: 07:07:05/07:08:50Z. D analysis/prepared-report: 07:08:27/07:08:48Z, but actual artifact mtime was 07:10:02Z and coordinator observation 07:10:39Z; prepared time is not actual delivery. E analysis/reported artifact handoff: 07:10:57/07:11:25Z; coordinator persisted all reports by 07:13:02Z.
- Final existing typed validation passed for 28 pages; git diff --check passed. Runtime closed with zero coordinator repairs.
- C35 total was 47m44s: this round is 17m06s shorter (about 36%). However, catalog readiness is 22m12s versus C35 22m24s, essentially unchanged. The main saving is avoiding the prior audit-correction tail, not demonstrated concurrency acceleration. Raw volume increased 4.2% and source word count increased 4.6%; no shorter-prose claim.
- Remaining small optimization opportunity: use the existing audit report format without repeating evidence inventories and boilerplate caveats. B/C report tails were 101/105 seconds, and final delivery/persistence/close took 5m51s. Preserve query answers, material warnings and actual route checks; no new validator, monitoring framework or hard report cap is warranted.
