# C59 fixed-query answers: balancePlatform.balanceAccountPayoutSchedule.updated

Canonical route: [[source-adyen-api-explorer-balanceplatform-webhooks-latest-post-balanceplatform-balanceaccountpayoutschedule-updated]]; [captured API Explorer URL](https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutSchedule.updated). Evidence: [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutSchedule.updated/2026-09-15]].

## Q1

The captured Configuration webhooks v2 reference identifies the incoming `balancePlatform.balanceAccountPayoutSchedule.updated` event. Adyen says it sends it when a managed payout schedule on a balance account is successfully updated (raw lines 5–7). The request-body table requires `data`, `environment` and `type`, while `timestamp` and each listed `data` child are optional (lines 11–32). Optional children include the balance-account ID, schedule ID, platform, currency, active flag, frequency and value, payout amount controls, retained amount, closing time and transfer instrument. `frequencyValue` is allowed only for monthly or weekly schedules (line 22); if balance-account funds are below `retainedAmount`, execution is not initiated (line 27). The table describes the schedule ID as the identifier of a balance-platform payout schedule applied to the balance account (line 16); it does not make that ID required.

## Q2

This event reports successful schedule update, not a payout execution or funds-transfer outcome (raw line 7). The separate response section says any `2xx` accepts the webhook (lines 34–42); receipt or acceptance does not establish payout booking, settlement or recipient-bank receipt. This reference has no delivery-order, retry, deduplication or signature guarantee, no event-specific reversal rule, and no proof of current served version despite the captured `latest` URL (full raw lines 1–42). Later payout execution and transfer outcomes need separate evidence.
