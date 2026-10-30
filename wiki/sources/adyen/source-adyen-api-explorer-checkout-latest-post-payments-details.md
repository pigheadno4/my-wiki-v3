---
title: "Adyen Checkout API v72: POST /payments/details"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/details"
raw_files:
  - "adyen/api-explorer/Checkout/latest/post/payments/details/2026-09-15.md"
tags: [adyen, checkout, payments, payment-details, api-reference]
---

## Overview

This captured [[adyen]] Checkout API reference describes `POST /payments/details`: submit follow-up details for a payment created with `/payments` when that request has not reached a final state, such as after a shopper redirect. The captured server is `https://checkout-test.adyen.com/v72`; the `latest` URL does not establish a currently live latest version or a live endpoint.

## Key takeaways

- The request-body table marks the `details` object **required**. Its listed child fields are individually marked optional and cover flow-specific return data, including `redirectResult`, 3DS results, wallet identifiers and callbacks. The redirect and native 3DS examples illustrate alternatives, not a requirement to send every listed field.
- `authenticationData.authenticationOnly` is marked optional, with the page saying `true` triggers an authentication-only 3DS2 flow without proceeding to payment authorization. `threeDSAuthenticationOnly` changes the value previously set in `/payments` only when a change is wanted. The `paymentData` note gives distinct authentication-only values to submit after `AuthenticationNotRequired` and `AuthenticationFinished`; use the precise field mapping in the raw table.
- HTTP 200 says the **request** succeeded. The optional `resultCode` describes payment state: `Authorised`, `Cancelled`, `Error` and `Refused` are listed as final, while `Pending` lacks a final status; `Received` is an initial received state; `ChallengeShopper`, `IdentifyShopper`, `PresentToShopper` and `RedirectShopper` require further interaction or presentation. Authentication-only results are not payment authorization. An optional `action` can require more work. A 200 response or the illustrated `Authorised` response does not guarantee authorization for every call, capture, or settlement.
- The optional `pspReference` refers to the transaction/request; the optional `order` carries updated order information when order information was provided. Neither is interchangeable with the other. The optional `paymentMethod` and `paymentValidations` objects have narrower `Authorised` conditions in the response table.
- The raw reference documents 400, 401, 403, 422 and 500 error categories and response shapes. Example codes/messages are examples, not an exhaustive error contract.

## Detail locators

- Purpose, captured test server and idempotency header: raw lines 5–17.
- Request `details`, flow-specific child fields, authentication-only controls and `paymentData`: raw lines 20–47; alternative request examples: lines 49–67.
- 200 response fields and conditional objects: raw lines 68–110; `resultCode` states, 3DS response fields and `threeDSPaymentData`: lines 111–148.
- Error categories and response schema: raw lines 151–218; illustrative responses: lines 220–293.

## Related

- [[adyen-online-payments]] — provider-level server/client/webhook architecture and online-payment routes.
- [[adyen-3d-secure]] — authentication flow context; this API reference retains the versioned request and response contract.
- [[source-adyen-docs-online-payments-build-your-integration-payment-result-codes]] — broader result-code and later-status guidance.

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/post/payments/details/2026-09-15|Checkout v72 POST /payments/details capture]]
