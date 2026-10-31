---
title: "Adyen Configuration webhooks v2: managed payout schedule updated on a balance account"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutSchedule.updated"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutSchedule.updated/2026-09-15.md"
tags: [adyen, webhooks, balance-platform, managed-payouts]
---

## Overview

Captured Configuration webhooks v2 reference for the incoming `balancePlatform.balanceAccountPayoutSchedule.updated` event. Adyen says it sends this webhook when a managed payout schedule on a balance account is successfully updated. This is schedule-configuration evidence, not a merchant POST operation or evidence that a scheduled payout executed or reached a bank. See [[adyen]], [[adyen-webhooks]], and [[adyen-platforms]].

## Key takeaways

- The request-body table marks top-level `data`, `environment`, and `type` required; `timestamp` is optional. Every listed child of `data` is marked optional, including balance-account and payout-schedule identifiers, platform, currency, enabled state, frequency, amount controls, retained amount, sales-day closing time and destination transfer instrument. The table does not make the event's complete object snapshot or any individual child identifier mandatory.
- The event is about a schedule update. The listed `enabled` field describes whether a schedule is active; `retainedAmount` describes funds that must remain available after execution and says execution is not initiated if funds are below it. These field descriptions do not show that this webhook records an execution, transfer booking, settlement, or recipient-bank receipt.
- The response section says any `2xx` HTTP status accepts the webhook; its example is `200 Success` with optional `notificationResponse`. That acceptance is separate from the underlying schedule change or later payout outcome. The captured `latest` route and versioned family context do not establish the version currently served, and this reference does not specify delivery order, retries, deduplication, or signature verification.

## Detail locators

- Event identity and trigger: pinned raw lines 5–7.
- `## Parameters` → `### Request body`: required top-level fields, optional `data` children, and field constraints: lines 9–32. In particular, `frequencyValue` is allowed only for monthly or weekly schedules (line 22); description and beneficiary-reference qualifications are at lines 19 and 26.
- `## Responses` → `### 200 Success`: webhook acceptance and response-body entry, lines 34–42.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutSchedule.updated/2026-09-15|Captured managed payout schedule updated webhook reference (2026-09-15)]]
