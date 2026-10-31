---
title: "Adyen Webhooks latest CAPTURE_FAILED notification"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/CAPTURE_FAILED"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/CAPTURE_FAILED/2026-09-15.md"
tags: [adyen, webhooks, capture, capture-failed]
---

## Overview

This 2026-09-15 snapshot of Adyen's Webhooks `latest` POST `/CAPTURE_FAILED` reference describes an incoming notification that a capture request failed because the card scheme rejected it. The POST heading names the webhook delivered to a receiver; it is not a merchant capture operation.

## Key takeaways

- The notification item identifies its event through `eventCode`; the example uses `CAPTURE_FAILED`, an original payment reference in `originalReference`, and a separate Adyen request/transaction reference in `pspReference`. The schema marks `originalReference` optional, while `eventCode`, `pspReference`, `merchantReference`, `merchantAccountCode`, `eventDate`, `amount`, and `success` are required within `NotificationRequestItem`. The outer `live`, `notificationItems`, and wrapper item are marked optional in this page's table.
- `success` describes whether the named event was executed successfully, not whether capture succeeded. The failed-capture example has `success: "true"` and `reason: "Capture Failed"`; the table describes `reason` as an explanation when `success` is `false`. Preserve both the generic field description and this example without treating the example as a universal rule.
- The response section says webhook events are accepted on the basis of HTTP status code and labels `200 Success`. That is receiver acceptance, not a successful capture, settlement, or payment outcome. This page does not establish delivery order, retries, deduplication, signature verification procedure, or a capture recovery action.

## Detail locators

- Trigger and event purpose: raw lines 5–7. Request-body requiredness, environment flag, references, event outcome and conditional reason: raw lines 11–27. Example payload, including amount, currency, identities and the `success` value: raw lines 29–60. HTTP acceptance statement: raw lines 61–64.

## Related

- [[adyen]] — provider overview.
- [[adyen-webhooks]] — incoming webhook context.
- [[adyen-payment-capture]] — capture outcome and failure context.

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/CAPTURE_FAILED/2026-09-15|CAPTURE_FAILED webhook reference (2026-09-15)]]
