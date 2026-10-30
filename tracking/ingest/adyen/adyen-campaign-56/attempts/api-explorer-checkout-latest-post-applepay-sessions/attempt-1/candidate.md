---
title: "Adyen Checkout API v72: POST /applePay/sessions"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/post/applePay/sessions"
raw_files:
  - "adyen/api-explorer/Checkout/latest/post/applePay/sessions/2026-09-15.md"
tags: [adyen, checkout, apple-pay, merchant-validation, api-reference]
---

## Overview

This captured [[adyen]] Checkout API reference describes `POST /applePay/sessions` for an API-only Apple Pay integration that uses Adyen's Apple Pay certificate. It returns Apple Pay session data for Apple Pay merchant/session validation. This is a merchant-validation session, distinct from a Checkout payment session and from a payment authorization. The captured server is `https://checkout-test.adyen.com/v72`; the `latest` URL does not establish a currently live latest version or live endpoint.

## Key takeaways

- The request table marks `displayName`, `domainName`, and `merchantIdentifier` required. It directs `displayName` to `configuration.merchantName` and `merchantIdentifier` to `configuration.merchantId` from `/paymentMethods`. The `domainName` is the domain configured for Apple Pay in Customer Area and must match the web shop's `window.location.hostname`.
- The optional `Idempotency-Key` header is described as a unique identifier of up to 64 characters, with a UUID recommended.
- HTTP 200 means the request succeeded. Its response table requires a Base64 encoded `data` string for completing Apple Pay merchant validation. The example contains abbreviated data; it does not prove completed validation, payment authorization, capture, settlement, merchant eligibility, or a live outcome.
- This captured page gives no error-response table or error examples. Consult the linked Apple Pay integration and error guidance for separate setup and diagnostics; do not infer failure codes from this endpoint's response example.

## Detail locators

- Endpoint purpose, certificate-specific scope, session validation and v72 TEST server: raw lines 5–12.
- Header and required request properties, including `/paymentMethods` origins and domain match: raw lines 16–27; illustrative body: lines 29–38.
- HTTP 200, required response `data` and abbreviated example: raw lines 39–58.

## Related

- [[adyen-online-payments]] — provider-level Checkout architecture and Apple Pay guidance route.
- [[source-adyen-docs-payment-methods-apple-pay-api-only]] — API-only Apple Pay integration guide.
- [[source-adyen-docs-payment-methods-apple-pay-handle-apple-pay-errors]] — separate Apple Pay error guidance.

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/post/applePay/sessions/2026-09-15|Checkout v72 POST /applePay/sessions capture]]
