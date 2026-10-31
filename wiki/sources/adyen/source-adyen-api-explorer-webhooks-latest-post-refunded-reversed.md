---
title: "Adyen Webhooks: REFUNDED_REVERSED notification"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/REFUNDED_REVERSED"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/REFUNDED_REVERSED/2026-09-15.md"
tags: [adyen, webhooks, refunds, reversal]
---

## Overview

Captured API Explorer `Webhooks/latest` `POST /REFUNDED_REVERSED` reference for an incoming notification about a reversed refunded amount. This reference says the amount was reversed and returned to “your bank account.” The separate [[source-adyen-docs-online-payments-refund|Adyen refund guide]] instead says the funds return to Adyen and are back in the merchant account; the captured sources do not reconcile that destination wording. The POST heading describes webhook delivery, not a merchant reversal operation. See [[adyen]], [[adyen-refunds]], and [[adyen-webhooks]].

## Key takeaways

- The body table marks top-level `live` and `notificationItems` and the nested `NotificationRequestItem` wrapper as not required. Within an item, it marks `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` required. These item-level flags do not make the outer container required.
- `success` is a string for whether the event named by `eventCode` executed successfully. Optional `reason` is described as a short refusal explanation when `success` is `false`. The example pairs `eventCode: "REFUNDED_REVERSED"` and `success: "true"`, yet supplies a nonempty `reason`; the page does not explain that mismatch, so the example must not redefine the documented condition.
- `merchantReference` is the merchant's payment reference; `pspReference` is Adyen's transaction or request reference. Optional `originalReference` corresponds, for modifications, to the original payment request; the example contains it. Keep original-payment and event/request identities separate.
- `amount` is described as the payment amount. The table says currency and value for HTTP POST notifications are URL parameters (raw line 18), while the example puts them in a nested JSON `amount` object (raw lines 38–41); the snapshot does not reconcile those representations. `eventDate` is event-generation time, and optional `live` distinguishes live from test origin.
- The response section labels `200` Success and says webhook events are accepted based on HTTP status code. Receiver acceptance is separate from the refund-reversal event outcome. This `latest` snapshot states no numbered version, response body, delivery, ordering, retry, deduplication, signature, or independent bank-receipt guarantee.

## Detail locators

- Event purpose and destination wording: raw lines 5–7.
- Body requiredness, identity, amount and success conditions: raw lines 11–27.
- Illustrative modification payload and reason/success mismatch: raw lines 29–55.
- HTTP status acceptance: raw lines 56–59.

## Related

- [[adyen]]
- [[adyen-refunds]]
- [[adyen-webhooks]]
- [[source-adyen-docs-online-payments-refund|Adyen refund guide]]

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/REFUNDED_REVERSED/2026-09-15|Captured REFUNDED_REVERSED webhook reference]]
