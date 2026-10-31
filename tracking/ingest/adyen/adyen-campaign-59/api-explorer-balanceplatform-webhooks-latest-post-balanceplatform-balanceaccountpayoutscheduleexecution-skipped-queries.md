# api-explorer-balanceplatform-webhooks-latest-post-balanceplatform-balanceaccountpayoutscheduleexecution-skipped fixed query answers

Pinned raw: `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutScheduleExecution.skipped/2026-09-15.md` (SHA-256 `f4f272ef6f5c504a3eb7631470170bae3f51d7026804accb26b84b5ee2d4b741`). Canonical source route: `wiki/sources/adyen/source-adyen-api-explorer-balanceplatform-webhooks-latest-post-balanceplatform-balanceaccountpayoutscheduleexecution-skipped.md`. Canonical URL: https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutScheduleExecution.skipped

## Q1

The captured Balance Platform Webhooks API Explorer POST reference describes Adyen's incoming `balancePlatform.balanceAccountPayoutScheduleExecution.skipped` notification when a scheduled payout execution is skipped (raw lines 5–7). Required envelope fields are `data`, `environment` (`test` or `live`), and `type`; the queued-event `timestamp` is optional (raw lines 14, 24–26). Optional `data` fields identify a source balance account, managed payout schedule, balance platform, execution result, result details and trigger time. Optional nested result details include a reason, `reasonCode` (a string containing a numeric code) and transfer ID described as a transfer created for this execution (raw lines 15–23). No numbered webhook API version appears in the pinned page; `latest` is only the captured route label.

## Q2

The webhook says the schedule execution was skipped. Its schema does not guarantee any optional reason or transfer ID, define result values or reason codes, or describe a sequence after the skip (raw lines 5–7, 14–23). It does not prove a payout was sent, booked, settled, returned or credited to a bank. The response table says any HTTP 2xx accepts the webhook and makes `notificationResponse` optional (raw lines 28–36); it does not prove business-process success. The captured reference has no request example and no event-specific delivery, ordering, retry, deduplication or signature rule (full raw lines 1–36).
