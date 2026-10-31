---
title: "Adyen balance-platform payout-schedule deleted webhook"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balancePlatformPayoutSchedule.deleted"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balancePlatformPayoutSchedule.deleted/2026-09-15.md"
tags: [adyen, webhooks, balance-platform, managed-payouts]
---

## Overview

Captured incoming `balancePlatform.balancePlatformPayoutSchedule.deleted` webhook reference. Adyen says it sends the event when a payout schedule is successfully deleted on a balance platform. The `POST` heading describes an event sent to the receiver, not a merchant operation to invoke. This is platform-level schedule-deletion evidence; the page does not state what happens to schedules already applied to balance accounts. See [[adyen]], [[adyen-webhooks]], and [[adyen-platforms]].

## Key takeaways

- The request-body table requires the top-level `data` object, `environment` (`test` or `live`), and `type`; `timestamp` is optional. Every listed `data` child is marked optional, including `balancePlatform`, `balancePlatformPayoutScheduleId`, country/currency, default schedule fields, payout amount limits, and retained amount. The schedule ID's description refers to a platform schedule applied to a balance account, but the event trigger is deletion on the balance platform; the reference does not establish account-level removal or automatic replacement.
- `retainedAmount` describes a condition for later execution: if account funds are below that amount, execution is not initiated. This field description does not mean that a payout execution occurred in this deletion event. Nor does deletion prove any transfer booking, settlement, or bank receipt.
- The response section says any `2xx` HTTP status accepts the webhook, with optional `notificationResponse` in its `200 Success` response-body table. Acceptance is a receiver acknowledgement, separate from the schedule deletion and any later payout outcome. This endpoint page gives no delivery-order, retry, deduplication or signature rules. Its captured `latest` URL does not prove the currently served version; the endpoint page itself does not state a version.

## Detail locators

- Event identity and successful platform-level deletion trigger: pinned raw lines 5–7.
- `## Parameters` → `### Request body`: envelope requiredness and optional schedule details, lines 9–29. `defaultFrequencyValue` conditions are on line 21; `retainedAmount` execution condition is on line 26.
- `## Responses` → `### 200 Success`: response and `2xx` acceptance, lines 31–39.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balancePlatformPayoutSchedule.deleted/2026-09-15|Captured balance-platform payout-schedule deleted webhook reference (2026-09-15)]]
