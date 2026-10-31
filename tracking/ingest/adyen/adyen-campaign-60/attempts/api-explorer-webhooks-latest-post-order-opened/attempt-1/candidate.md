---
title: "Adyen Webhooks POST /ORDER_OPENED — first partial payment for order"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/ORDER_OPENED"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/ORDER_OPENED/2026-09-15.md"
tags: [adyen, webhooks, online-payments, partial-payments]
---

## Overview

This 2026-09-15 snapshot of the Adyen Webhooks `latest` POST /ORDER_OPENED reference describes an incoming notification when the first partial payment was made and the order was created. The POST label identifies a webhook event, not a merchant order-creation operation. See [[adyen]], [[adyen-webhooks]], and [[adyen-online-payments]].

## Key takeaways

- The example notification item sets `eventCode` to `ORDER_OPENED` and `success` to the string `true`. The table defines required `success` as the outcome of the event named by `eventCode`; optional `reason` provides a short refusal explanation when it is `false`. The example is illustrative, not a guarantee for all orders.
- The nested item table marks `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` required. Optional `originalReference` is described generically for modifications as the original payment request; the ORDER_OPENED example omits it. `pspReference` identifies the transaction or request, not an explicitly identified order resource in this page.
- The response section shows `200 Success` and says webhook events are accepted based on HTTP status code. Receiver acceptance is separate from the event outcome and does not establish order completion or final payment settlement.

## Detail locators

- Request body table, including optional outer `live` and `notificationItems`, nested field requirements and reference descriptions: raw lines 9–27. Do not promote nested required fields into an assertion that the outer body fields are required.
- One JSON example with EUR 1000, `ORDER_OPENED`, and `success: "true"`: raw lines 29–53.
- HTTP acceptance wording: raw lines 54–57. This snapshot gives no delivery ordering, retry, deduplication, signature, order-completion, capture, or settlement guarantee.

## Related

- [[adyen]] — provider context.
- [[adyen-webhooks]] — incoming webhook context.
- [[adyen-online-payments]] — partial-payment and order routes.

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/ORDER_OPENED/2026-09-15|Adyen Webhooks latest POST /ORDER_OPENED, captured 2026-09-15]]
