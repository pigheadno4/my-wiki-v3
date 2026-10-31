---
title: "Adyen Webhooks: POSTPONED_REFUND notification"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Webhooks/latest/post/POSTPONED_REFUND"
raw_files:
  - "adyen/api-explorer/Webhooks/latest/post/POSTPONED_REFUND/2026-09-15.md"
tags: [adyen, webhooks, refunds, capture]
---

## Overview

This captured Adyen API Explorer `Webhooks/latest` POST reference describes an incoming `POSTPONED_REFUND` notification: the refund was postponed until after payment capture. The page says to contact Adyen Support to enable this notification. The POST heading is a webhook event route, not an instruction to submit a refund. See [[adyen]], [[adyen-refunds]], and [[adyen-webhooks]].

## Key takeaways

- The displayed request-body table marks `live`, `notificationItems`, and the nested `NotificationRequestItem` wrapper optional. Within the item, `amount`, `eventCode`, `eventDate`, `merchantAccountCode`, `merchantReference`, `pspReference`, and `success` are marked required. The example uses `eventCode: "POSTPONED_REFUND"`; its EUR 1000 amount and `directdebit_NL` payment method are illustrative, not general conditions for the event.
- `merchantReference` identifies the merchant's payment reference. `pspReference` is Adyen's transaction or request reference. Optional `originalReference` is described for modifications as corresponding to the original payment request; the example contains distinct original and PSP references.
- `success` describes execution of the specified event, not successful payment capture, completed refund, shopper credit, or settlement. `reason` is described as a short refusal explanation if `success=false`. The notification's defining state is postponement until after capture.
- The example includes `additionalData.hmacSignature`, but this reference does not define a signature verification procedure or state that every event includes that field.
- The response section lists `200 Success` and says webhook events are accepted based on HTTP status. Receiver acceptance is separate from the refund state. This reference does not establish delivery order, retries, deduplication, or a later refund outcome.

## Detail locators

- Raw lines 5–7: postponed-until-after-capture meaning and Support enablement condition.
- Raw lines 11–27: request-body schema, optional versus required item fields, `live` environment flag, reference identities, conditional `reason`, and event-scoped `success`. `amount` is described as the payment amount; the table notes currency and value as URL parameters for HTTP POST notifications.
- Raw lines 29–58: illustrative test-origin payload, `hmacSignature` extra field, EUR 1000 amount, `directdebit_NL`, and `success="true"`.
- Raw lines 59–62: `200 Success` and HTTP status based webhook acceptance.

## Related

- [[adyen-refunds]] — online refund lifecycle and outcome boundaries.
- [[adyen-webhooks]] — Adyen webhook families and receiver context.
- [[adyen-payment-capture]] — capture lifecycle context.

## Raw Sources

- [[raw/adyen/api-explorer/Webhooks/latest/post/POSTPONED_REFUND/2026-09-15|Captured POSTPONED_REFUND webhook reference]]
