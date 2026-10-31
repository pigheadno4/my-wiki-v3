---
title: "Adyen Webhooks: AUTHORISATION_ADJUSTMENT result notification"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/AUTHORISATION_ADJUSTMENT"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/AUTHORISATION_ADJUSTMENT/2026-09-15.md"
tags: [adyen, webhooks, authorisation-adjustment, online-payments]
---

## Overview

This captured Adyen API Explorer `Webhooks/latest` POST reference describes an incoming `AUTHORISATION_ADJUSTMENT` notification reporting the result of a request to adjust an authorised payment amount through `/adjustAuthorisation`. The POST heading is the webhook delivery route, not a merchant adjustment operation. See [[adyen]] and [[adyen-webhooks]].

## Key takeaways

- The nested `NotificationRequestItem` schema marks `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` required. The enclosing `live` and `notificationItems` fields, the wrapper's `NotificationRequestItem` field, and `additionalData` are marked optional in this table. `eventCode` identifies the event type; the example sets it to `AUTHORISATION_ADJUSTMENT`.
- `originalReference` is optional and, for modifications, corresponds to the original payment request. `pspReference` is Adyen's reference associated with the transaction or request. Keep these distinct from the merchant's `merchantReference`. The example includes all three; it does not change their schema requiredness.
- `success` is the outcome of the specified `eventCode`: `true` means that event executed successfully and `false` means it did not. If `success` is `false`, `reason` includes a short refusal explanation. This is an adjustment-result notification, not proof of capture or settlement.
- The response section lists `200 Success` and says webhook events are accepted on the basis of the HTTP status code. This receiver acceptance is separate from the adjustment event's `success` value. This reference does not establish delivery order, retries, deduplication, signature checks, or later financial finality.

## Detail locators

- Raw lines 5–7: event purpose and `/adjustAuthorisation` relationship.
- Raw lines 11–27: request-body schema, required versus optional nested fields, `live` environment flag, reference identities, conditional `reason`, and event-scoped `success`. `amount` is described as the payment amount; the table notes currency and value as URL parameters for HTTP POST notifications.
- Raw lines 29–55: illustrative `AUTHORISATION_ADJUSTMENT` payload, including `live: "false"`, EUR 1000, an original reference, a distinct PSP reference, and `success: "true"`.
- Raw lines 56–59: `200 Success` and HTTP status based webhook acceptance.

## Related

- [[adyen-webhooks]] — Adyen webhook concepts and other event families.
- [[adyen-online-payments]] — online payment integration context.

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/AUTHORISATION_ADJUSTMENT/2026-09-15|Captured AUTHORISATION_ADJUSTMENT webhook reference]]
