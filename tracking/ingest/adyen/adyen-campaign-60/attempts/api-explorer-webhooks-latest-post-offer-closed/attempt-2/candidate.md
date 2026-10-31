---
title: "Adyen Webhooks: OFFER_CLOSED notification"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/OFFER_CLOSED"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/OFFER_CLOSED/2026-09-15.md"
tags: [adyen, webhooks, online-payments, offer-expiry]
---

## Overview

Captured API Explorer `Webhooks/latest` `POST /OFFER_CLOSED` reference for an incoming notification that an offer expired, for example after the shopper abandoned the session. For **cards**, the page says offers expire after 12 hours by default. The `POST` heading describes webhook delivery, not a merchant operation to close an offer. The `latest` label supplies no numbered version. See [[adyen]] and [[adyen-webhooks]].

## Key takeaways

- The body table marks top-level `live` and `notificationItems` as not required, and also marks the nested `NotificationRequestItem` wrapper as not required. Within an item, `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` are marked required. These nested field flags do not make the top-level container required.
- `success` is a **string** for the outcome of the event identified by `eventCode`: `true` means that event executed successfully; `false` means it did not. An optional `reason` gives a short refusal explanation when `success` is `false`. The example has `eventCode: "OFFER_CLOSED"` and `success: "true"`; this is an offer-closure event outcome, not a successful payment.
- The required `merchantReference` identifies the merchant's payment reference. `pspReference` identifies Adyen's transaction or request reference. Optional `originalReference` is described for modifications as corresponding to the original payment request; the example does not include it.
- `amount` is described as the payment amount. The table says HTTP POST notifications return currency and value as URL parameters (raw line 18), while the example places them in a nested JSON `amount` object (raw lines 42–45); this snapshot does not reconcile the two representations. `eventDate` is when the event was generated; optional `live` distinguishes live and test origin. The example shows EUR 1000, `paymentMethod: "ideal"`, and `additionalData` with `hmacSignature` and `paymentMethodVariant`. Those example fields do not establish a signature requirement or extend the card-specific default expiry to iDEAL.
- The response section labels `200` Success and says webhook events are accepted based on HTTP status code. Receiver acceptance is separate from the offer-expiry event's `success` value. This page gives no response-body, delivery, ordering, retry, deduplication, or payment finality contract.

## Detail locators

- Event purpose and card-specific default: raw lines 5–7.
- Request-body flags, identities, amount and success semantics: raw lines 11–27.
- Illustrative iDEAL notification and extra fields: raw lines 29–58.
- HTTP status acceptance: raw lines 59–62.

## Related

- [[adyen]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/OFFER_CLOSED/2026-09-15|Captured OFFER_CLOSED webhook reference]]
