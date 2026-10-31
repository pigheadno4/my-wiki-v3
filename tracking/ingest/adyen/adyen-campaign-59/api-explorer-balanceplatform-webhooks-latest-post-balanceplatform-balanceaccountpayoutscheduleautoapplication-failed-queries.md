# C59 worker fixed-query answers: balanceAccountPayoutScheduleAutoApplication.failed

Pinned raw: `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutScheduleAutoApplication.failed/2026-09-15.md` (SHA-256 `cc7f104a45b93ab096515b9953519b8a2fc367c434a885a9fbabb4ba6ba5de03`). Canonical route: [Adyen API Explorer, balancePlatform.balanceAccountPayoutScheduleAutoApplication.failed](https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutScheduleAutoApplication.failed). Proposed source route: [[source-adyen-api-explorer-balanceplatform-webhooks-latest-post-balanceplatform-balanceaccountpayoutscheduleautoapplication-failed]].

## Q1

The heading names the incoming `balancePlatform.balanceAccountPayoutScheduleAutoApplication.failed` POST event, and Adyen says it sends the webhook when a managed payout schedule could not be automatically applied to a balance account (raw lines 5–7). The table requires top-level `data`, `environment` and `type`, allows `test` or `live` environment, and marks `timestamp` optional (lines 11–22). All five listed `data` properties are optional: `balanceAccountId` for the affected balance account, `balancePlatform`, `balancePlatformPayoutScheduleId` for the unsuccessfully applied schedule, `reason`, and `transferInstrumentId` for the linked counterparty account (lines 14–19). No request example or reason enum appears in this capture.

## Q2

The event reports failed automatic schedule application to the balance account. It does not establish that a payout was executed, failed, reversed, settled or credited to a bank. The response section instructs any HTTP `2xx` to accept the webhook (raw lines 24–32), without an event-specific delivery, ordering, retry, deduplication or signature contract. The `latest` URL and 2026-09-15 fetched date identify a snapshot, not a fixed current API version (raw lines 1–2).
