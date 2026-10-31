---
title: "Adyen Webhooks latest REFUND notification"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/REFUND"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/REFUND/2026-09-15.md"
tags: [adyen, webhooks, refunds, online-payments]
---

## Overview

This 2026-09-15 Adyen Webhooks `latest` API Explorer POST reference describes an incoming `REFUND` notification reporting the result of a request to refund a payment. The POST heading identifies the webhook endpoint, not a merchant operation to submit a refund. See [[adyen]], [[adyen-webhooks]], and [[adyen-refunds]] for the wider asynchronous refund lifecycle.

## Key takeaways

- The item schema marks `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` required. Outer `live` and `notificationItems`, the item wrapper, `additionalData`, `originalReference`, `paymentMethod`, and `reason` are marked optional. These are table markings, distinct from the fields present in the one example.
- `merchantReference` identifies the merchant's payment reference; `pspReference` identifies Adyen's associated transaction or request. The table describes optional `originalReference` for modifications. `success` reports whether the named event executed successfully, and optional `reason` is described for a false value. The example shows `eventCode: REFUND`, `success: "false"`, and `reason: "Transaction hasn't been captured, refund not possible"`; this is an illustrative failed refund result, not a general rule for all failures.
- The response section shows `200 Success` and says webhook events are accepted on the basis of HTTP status. HTTP acceptance is separate from the refund event result. This endpoint alone does not prove shopper receipt of funds or exclude later refund failure or reversal.

## Detail locators

- Pinned raw, lines 5–7: endpoint purpose.
- Pinned raw, lines 11–27: envelope and item field requiredness, references, and event outcome.
- Pinned raw, lines 29–55: failed-refund example with amount, original reference, reason and success flag.
- Pinned raw, lines 56–59: HTTP status acceptance.

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/REFUND/2026-09-15|REFUND API Explorer reference, captured 2026-09-15]]
