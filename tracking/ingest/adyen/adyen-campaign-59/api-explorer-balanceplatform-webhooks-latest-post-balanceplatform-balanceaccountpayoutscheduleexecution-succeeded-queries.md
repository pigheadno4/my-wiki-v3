# Fixed query answers — api-explorer-balanceplatform-webhooks-latest-post-balanceplatform-balanceaccountpayoutscheduleexecution-succeeded

Canonical route: [[source-adyen-api-explorer-balanceplatform-webhooks-latest-post-balanceplatform-balanceaccountpayoutscheduleexecution-succeeded]]; [captured API Explorer URL](https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutScheduleExecution.succeeded). Pinned raw: `raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutScheduleExecution.succeeded/2026-09-15.md`.

## Q1

The captured incoming POST reference names `balancePlatform.balanceAccountPayoutScheduleExecution.succeeded`; Adyen says it sends the webhook when a scheduled payout execution succeeds (raw lines 5–7). The table requires top-level `data`, `environment`, and `type`, but marks every listed `data` field optional (raw lines 14–26). Those optional fields identify the initiating balance account, managed payout schedule, balance platform, result, result details, and trigger time. Within optional `resultDetails`, `transferId` identifies a transfer created for the execution when present; `reason` and `reasonCode` describe an unsuccessful execution but are not stated to occur in this succeeded event (raw lines 18–23). The page defines no `result` enum and provides no request example (raw lines 18, 28).

## Q2

The event asserts success of a **scheduled payout execution**, not bank receipt or final external-transfer credit (raw lines 5–7). `transferId` is optional, so a populated transfer identifier cannot be assumed for every payload (raw lines 19–22). The response table says any HTTP `2xx` accepts the webhook; that receiver acknowledgement does not supply additional payout-state evidence (raw lines 28–36). This page does not define delivery order, retry/deduplication, authentication/signature checks, reversal or later bank-return semantics. Its `latest` URL does not establish a numbered version or current availability (raw lines 1–7, 9–36).
