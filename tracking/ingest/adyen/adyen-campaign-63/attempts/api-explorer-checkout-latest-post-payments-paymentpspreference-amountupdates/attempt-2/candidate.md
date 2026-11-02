---
title: "Adyen Checkout API: POST /payments/{paymentPspReference}/amountUpdates"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference)/amountUpdates"
raw_files:
  - "adyen/api-explorer/Checkout/latest/post/payments/(paymentPspReference)/amountUpdates/2026-11-02.md"
tags: [adyen, checkout-api, authorization-adjustment, payments]
---

## Overview

This 2026-11-02 capture of the Checkout API `latest` page lists the TEST server as `https://checkout-test.adyen.com/v72`. `POST /payments/{paymentPspReference}/amountUpdates` increases or decreases the authorised amount of a payment and returns a distinct reference for the amount-update request. The requested `amount` is the updated total, not an increment. The page says only authorised amounts not yet captured can be updated. The outcome is delivered in an `AUTHORISATION_ADJUSTMENT` webhook for the asynchronous path; the captured page does not establish current live availability, merchant eligibility, issuer acceptance, or a successful adjustment.

## Key takeaways

- The path `paymentPspReference` identifies the original payment's `pspReference`; the 201 response's `paymentPspReference` identifies that payment, while its `pspReference` is Adyen's 16-character reference for this amount-update request. `reference` is the merchant's amount-update reference, with an 80-character maximum in the request.
- The request-body table marks `merchantAccount` and the `amount` object required, with `amount.currency` and `amount.value` required inside it. Currency must match the original authorisation; value is in minor units. Optional `adjustAuthorisationData` is the blob passed from the payment response or webhook for a synchronous adjustment. Optional `mpiData` is described as required for cardholder-initiated adjustments; nested and platform-split conditions remain in the raw schema.
- The optional `Idempotency-Key` header is a unique message identifier, at most 64 characters; the page recommends a UUID. This captured schema does not state duplicate-request behavior.
- A 201 response contains `amount`, `merchantAccount`, `paymentPspReference`, the distinct update `pspReference`, `reference`, and `status` as required response fields. With `adjustAuthorisationData` in the request, `status` may be `authorised` or `refused`; otherwise it is `received`. The response can include a new `adjustAuthorisationData` blob when using the synchronous flow. A `received` state is request receipt, not the later adjustment outcome, capture, settlement, or transfer of funds.

> [!warning] Contradiction: adjustment after partial capture
> This API page says only authorised amounts that have not yet been captured can be updated (raw line 9). The separately captured Adyen pre-authorisation guide describes a Support-enabled multiple-partial-capture sequence with an adjustment after the first partial capture (guide raw line 56 for Support enablement and raw lines 1032-1040 for the sequence). These statements have different scope and remain unresolved; do not infer from this endpoint page alone that every post-partial-capture update is allowed, or from the guide that an arbitrary captured payment is adjustable.

> [!warning] Request/response schema qualifications
> The request table marks merchant `reference` optional (raw line 104), while the 201 response marks it required (raw line 170); the page does not explain how an omitted request reference is populated. The `lineItems` description on this amount-update page refers to refunded items and partial-refund requirements (raw lines 63 and 140). Preserve that wording as a schema locator rather than treating it as a general amount-update rule.

## Detail locators

- Purpose, uncaptured restriction, updated-total semantics, TEST v72 server: raw lines 5-16.
- Path and optional idempotency header: raw lines 18-29.
- Request schema, including nested application, line-item, MPI and platform split fields, conditional requirements, defaults and split-type values: raw lines 32-112.
- Request example: raw lines 114-126.
- 201 response fields and status meanings: raw lines 127-179; successful response example: raw lines 251-268.
- Documented 400/401/403/422/500 error categories and optional error-body fields: raw lines 182-249; examples: raw lines 270-330. The 401 describes authentication required and 403 insufficient permissions; this page does not specify a credential type or role.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-authorization-adjustment]]
- General integration context: [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/post/payments/(paymentPspReference)/amountUpdates/2026-11-02|Checkout API amount-update endpoint, 2026-11-02 capture]]