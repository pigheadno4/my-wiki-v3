---
title: "Adyen Checkout API POST /orders/cancel"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/post/orders/cancel"
raw_files:
  - "adyen/api-explorer/Checkout/latest/post/orders/cancel/2026-09-15.md"
tags: [adyen, checkout, api, orders, partial-payments, cancellation]
---

## Overview

This 2026-09-15-captured [[adyen]] Checkout API reference documents `POST /orders/cancel` on the listed test server `https://checkout-test.adyen.com/v72`. It cancels an order and says order cancellation automatically rolls back payments made in that order by cancellation or refund, according to payment-method type. The URL's `latest` segment does not establish a current API version.

## Key takeaways

- The request body lists `merchantAccount` and `order` as required. The merchant account is the one to which the encrypted `orderData` belongs. The required order object pairs that data with the order's `pspReference`; the example values are illustrative.
- `Idempotency-Key` is an optional header, with a maximum of 64 characters.
- A 200 response contains a cancellation-request `pspReference` and `resultCode`. The documented `Received` value means Adyen received the cancellation request for processing. This response alone does not establish that every payment cancellation or refund has completed.
- The page lists 400, 401, 403, 422 and 500 error responses. Their example payloads do not define endpoint-specific preconditions beyond the request contract.

## Detail locators

- Request header, body and example: raw lines 12–39.
- 200 response and acknowledgement meaning: raw lines 40–49; response example at 121–131.
- Error response tables and examples: raw lines 52–119 and 133–194.

## Related

- [[adyen-online-payments]] — Adyen online-payment and partial-payment source route.

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/post/orders/cancel/2026-09-15|Checkout API POST /orders/cancel, captured 2026-09-15]]
