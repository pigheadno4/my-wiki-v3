---
title: "Adyen Balance Platform payout schedule deleted webhook"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutSchedule.deleted"
raw_files:
  - "adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutSchedule.deleted/2026-09-15.md"
tags: [adyen, webhooks, platforms, payouts]
---

## Overview

Captured 2026-09-15 Adyen API Explorer `POST balancePlatform.balanceAccountPayoutSchedule.deleted` incoming webhook reference. Adyen says it sends this event when a payout schedule is successfully deleted from a balance account. This is a schedule-configuration event, not evidence that a payout was executed, booked, credited, or received at a bank. See [[adyen]], [[adyen-platforms]], and [[adyen-webhooks]].

## Key takeaways

- The request body requires the `data` object, `environment` (`test` or `live`), and `type`; the table marks `timestamp` and every listed property within `data` optional. The page does not supply a literal `type` value or an example payload.
- Optional `data` identifiers include `balanceAccountId`, `balanceAccountPayoutScheduleId`, and `balancePlatform`; optional schedule details include currency, active flag, frequency, payout amount limits, retained amount, transfer instrument, and references. Do not assume an optional identifier or field is present in every event.
- The response section says any HTTP `2xx` accepts the webhook. That acknowledgment is distinct from a financial outcome. The captured page does not specify delivery ordering, retries, deduplication, signature verification, or bank-payout finality.

## Detail locators

- Trigger and event identity: raw lines 5–7.
- Body requiredness and schedule identifiers: raw lines 9–18, 30–32.
- Schedule-field definitions and conditional `frequencyValue`: raw lines 19–29.
- Acceptance response: raw lines 34–42.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform-webhooks/latest/post/balancePlatform.balanceAccountPayoutSchedule.deleted/2026-09-15|Captured API Explorer webhook reference]]
