---
title: "Adyen Checkout API v72 POST /orders — Create an order"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/post/orders"
raw_files:
  - "adyen/api-explorer/Checkout/latest/post/orders/2026-09-15.md"
tags: [adyen, checkout, api, orders, partial-payments]
---

## Overview

This captured API Explorer reference documents Checkout API v72 `POST /orders` at the test server. It creates an order for partial payments with different payment methods before a `/payments` call. The order is distinct from any subsequent payment authorization, capture, or settlement. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The request body table marks `amount` (with currency and minor-unit value), `merchantAccount`, and `reference` required. `expiresAt` is optional; without it, the documented default expiry is one day. The optional `Idempotency-Key` header has a 64-character maximum.
- A 200 response reports order creation with `resultCode: Success`, initial `amount`, `remainingAmount`, `expiresAt`, and encrypted `orderData` for adding payments to the order. Its `pspReference` is described as a transaction/request reference; the response is not proof that a payment was authorized or that the order is fully paid.
- The captured reference lists 400, 401, 403, 422, and 500 errors. Their response examples illustrate errors, rather than adding request requirements: for example, the 422 example says “Return URL is missing” although `returnUrl` is absent from this endpoint's request body table. Do not treat that generic example as this endpoint's required field.
- The URL says `latest`, while the captured server is `https://checkout-test.adyen.com/v72` (2026-09-15 snapshot). It does not establish the current live version or availability.

## Detail locators

- Purpose, server, optional header, and request body: raw lines 5–28.
- Success response fields and their requiredness: raw lines 43–69.
- HTTP errors and generic error schemas: raw lines 72–139.
- Illustrative success and error payloads: raw lines 141–225. The success example's `amount.value` differs from its request example; use the schema descriptions for field meaning.

## Related

- [[source-adyen-docs-online-payments-partial-payments]] — broader multi-method order lifecycle guide.
- [[adyen-online-payments]] — provider concept route.

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/post/orders/2026-09-15|Captured Checkout API POST /orders reference]]
