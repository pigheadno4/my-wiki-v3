# C59 fixed-query answers: Configuration webhooks v2 overview

Canonical route: [[source-adyen-api-explorer-balanceplatform-webhooks-latest-overview]]; [captured API Explorer URL](https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/overview). Evidence: [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/overview/2026-09-15]].

## Q1

The captured page is headed **Configuration webhooks v2** (raw line 5). Adyen says it sends platform-event details to the receiver's server by HTTP POST (lines 7–8); the listed POST entries are event types, including account-holder and balance-account changes, recurring top-ups, payout-schedule configuration and execution outcomes, sweeps, card orders, mandates, network tokens, payment instruments, and score signals (lines 12–45). Its examples include changed account-holder capabilities and created/updated sweep configuration (line 7), with internal status updates suggested as a use (line 10). This overview has no payload schema, required or conditional fields, or detailed transition rules.

## Q2

The catalog establishes named notifications and short event summaries, including payout-schedule execution failed, skipped, and succeeded (lines 27–30). It does not establish underlying funds movement, authorization, verification approval, transfer booking, settlement, or bank receipt. The overview does not state delivery order, retries, deduplication, authentication/signature requirements, or detailed failure/reversal semantics (full raw lines 1–45). Its `latest` URL and captured v2 heading do not establish the current served version; this is the 2026-09-15 snapshot. Individual event references and separate guidance are needed for those claims.
