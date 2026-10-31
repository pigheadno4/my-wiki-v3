---
title: "Adyen Webhooks: CANCELLATION notification"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/CANCELLATION"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/CANCELLATION/2026-09-15.md"
tags: [adyen, webhooks, online-payments, cancellation]
---

## Overview

Captured API Explorer `Webhooks/latest` reference for an incoming `CANCELLATION` notification reporting the result of a request to cancel a payment. Its `POST /CANCELLATION` label describes the webhook delivery, not a merchant cancellation API call. This snapshot does not name a numbered Webhooks API version. See [[adyen]] and [[adyen-webhooks]].

## Key takeaways

- The request-body table marks both top-level `live` and `notificationItems` as not required. Within a `NotificationRequestItem`, it marks `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` as required. These are table-level flags; they do not make the top-level body fields required.
- `success` is a string describing the outcome of the event identified by `eventCode`: `true` means the event executed successfully; `false` means it did not. The optional `reason` gives a short refusal explanation when `success` is `false`. The example has `eventCode: "CANCELLATION"` and `success: "true"`; it illustrates one notification, not every cancellation result.
- `pspReference` is Adyen's reference for the transaction or request. Optional `originalReference` corresponds, for modifications, to the request assigned to the original payment. The required `merchantReference` is the merchant's payment reference. Keep these identities separate when correlating the cancellation result.
- `amount` describes the payment amount. The example uses EUR 1000, and the table says HTTP POST notifications return currency and value as URL parameters. `eventDate` is the event-generation time; `live` distinguishes live from test origin when present.
- The response section says webhook events are accepted on the basis of HTTP status code and labels `200` “Success.” That is receiver acceptance of the notification, distinct from the `success` field's cancellation-event outcome. This page does not specify a response body or establish delivery, ordering, retry, deduplication, signature, capture, or settlement guarantees.

## Detail locators

- Purpose and POST label: raw lines 5–7.
- Body required flags, event outcome and reference meanings: raw lines 11–27.
- Illustrative cancellation payload: raw lines 29–55.
- Receiver acceptance: raw lines 56–59.

## Related

- [[adyen]]
- [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/CANCELLATION/2026-09-15|Captured CANCELLATION webhook reference]]
