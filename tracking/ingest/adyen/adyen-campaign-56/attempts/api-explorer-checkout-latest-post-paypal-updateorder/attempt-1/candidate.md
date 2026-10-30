---
title: "Adyen Checkout API POST /paypal/updateOrder — PayPal Express order update"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/post/paypal/updateOrder"
raw_files:
  - "adyen/api-explorer/Checkout/latest/post/paypal/updateOrder/2026-09-15.md"
tags: [adyen, checkout-api, paypal, express-checkout, order-update]
---

## Overview

This 2026-09-15 API Explorer snapshot documents Checkout API `POST /paypal/updateOrder` for updating a **PayPal Express Checkout order**: the PayPal lightbox can reflect a changed amount and delivery methods based on the delivery address. It is distinct from Checkout API partial-payment `POST /orders`. The captured server is Checkout **v72 test**, although the canonical URL contains `latest`. See [[adyen-online-payments]] and the related PayPal Express Web Component guide.

## Key takeaways

- The request schema marks every top-level body field **No** under Required and does not mark the body itself required. It describes `paymentData` from the client as changing on each `/paypal/updateOrder` request, the original `/payments` `pspReference`, and the original `/sessions` `sessionId`. Illustrative Advanced requests use `pspReference` plus `paymentData`; illustrative Sessions requests use `sessionId` plus `paymentData`. The table alone does not establish that an empty request can update an order or that both identifiers should be sent together.
- The optional `amount` is the updated final payment amount, described as item total plus the shipping cost of the selected delivery method. Optional `deliveryAddress`, `deliveryMethods`, `discountAmount`, `shippingAmount`, and `taxTotal` are specified separately. Nested amount objects require `currency` and minor-unit integer `value` when included; the delivery-method `selected` description permits only one selected method at a time. The address table makes `stateOrProvince` conditionally required for the US and Canada despite its **No** marker.
- A `200 Success` response has required `paymentData` and `status` response properties; `status` indicates whether the order was successfully updated with PayPal. The example value is `success`, but the source does not establish authorization, capture, settlement, or a final payment outcome. Keep the returned updated `paymentData` in the ongoing PayPal flow rather than treating the incoming value as invariant.
- The page documents `400` malformed/unreadable request, `401` authentication required, `403` insufficient permissions, `422` validation error, and `500` server processing error schemas. Their generic examples include error codes/messages; the example `422` missing Return URL and `500` unsupported payment details do not define all failure conditions for this endpoint.

## Detail locators

- Endpoint purpose and v72 test server: raw lines 5–10.
- Idempotency header, request fields, nested amount/address/delivery conditions, and changing `paymentData`: raw lines 12–55.
- Advanced versus Sessions request examples, each with and without delivery methods: raw lines 57–149.
- `200` response meaning and required response properties; `400`, `401`, `403`, `422`, `500` error schemas: raw lines 150–229.
- Success and generic error examples: raw lines 231–328.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-online-payments]]
- PayPal Express integration guide: [[source-adyen-docs-payment-methods-paypal-web-component-express-checkout]]

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/post/paypal/updateOrder/2026-09-15|Checkout API POST /paypal/updateOrder (2026-09-15)]]
