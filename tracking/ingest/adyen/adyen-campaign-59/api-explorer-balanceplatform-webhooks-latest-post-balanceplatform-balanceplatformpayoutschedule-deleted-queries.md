# C59 fixed-query answers: balancePlatform.balancePlatformPayoutSchedule.deleted

Canonical route: [[source-adyen-api-explorer-balanceplatform-webhooks-latest-post-balanceplatform-balanceplatformpayoutschedule-deleted]]; [captured API Explorer URL](https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balancePlatformPayoutSchedule.deleted). Evidence: [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balancePlatformPayoutSchedule.deleted/2026-09-15]].

## Q1

This incoming webhook is `balancePlatform.balancePlatformPayoutSchedule.deleted`; Adyen says it sends it when a payout schedule is successfully deleted on a balance platform (raw lines 5–7). The request body requires top-level `data`, `environment` and `type`, while `timestamp` and all listed `data` children are optional (lines 11–29). The optional children include platform and platform-schedule IDs, country/currency, default descriptions/frequency/references, payout limits and retained amount (lines 15–26). The ID description refers to a platform schedule applied to a balance account (line 16), but the trigger remains platform-level deletion. This endpoint page does not state an API version; the separately captured [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/overview/2026-09-15|family overview]] identifies Configuration webhooks v2 (overview raw line 5).

## Q2

The event reports successful deletion of a platform payout schedule, with no stated consequence for schedules previously applied to balance accounts (raw lines 5–29). The retained-amount text describes when later execution is not initiated, not an execution outcome for this event (line 26). Receiver `2xx` acceptance is documented separately (lines 31–39) and does not prove payout execution, transfer booking, settlement or bank receipt. The endpoint page lacks delivery-order, retry, deduplication, authentication/signature and reversal guarantees (full raw lines 1–39). Its captured `latest` route is not proof of the version currently served.
