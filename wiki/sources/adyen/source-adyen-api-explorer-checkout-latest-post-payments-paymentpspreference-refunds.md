---
title: "Adyen Checkout API v72 refund a captured payment"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference)/refunds"
raw_files:
  - "adyen/api-explorer/Checkout/latest/post/payments/(paymentPspReference)/refunds/2026-11-02.md"
tags: [adyen, checkout-api, refunds, online-payments, webhooks]
---

## Overview

This 2026-11-02 API Explorer snapshot documents Checkout API v72 `POST /payments/{paymentPspReference}/refunds` at the listed test server. It requests a full or partial refund of a captured payment and returns a separate reference for the refund request. The `REFUND` webhook provides the asynchronous request outcome; the captured reference alone does not demonstrate current availability, live processing, or completed repayment.

## Key takeaways

- The path `paymentPspReference` identifies the original payment, while response `pspReference` identifies the refund request. The response also returns `paymentPspReference`, `merchantAccount`, and `amount` (currency and minor-unit value). A 201 response sets `status` to lowercase `received`; it is request receipt, not final financial success.
- The table marks `amount` and `merchantAccount` required in the request body, with `amount.currency` and `amount.value` required inside the amount object. Currency must match the authorization currency. The amount field says value is at most the authorized amount, while the overview says the sum of multiple partial refunds cannot exceed the captured amount. Some payment methods do not support partial refunds.
- Optional `Idempotency-Key` is a unique message identifier of at most 64 characters; the page recommends a UUID. Optional request `reference` has an 80-character maximum. `capturePspReference` is available only for PayPal refunds and identifies the particular capture.
- `lineItems` is table-optional but required for partial refunds with 3x 4x Oney, Affirm, Afterpay, Atome, Clearpay, Klarna, Ratepay, Walley, and Zip. Optional `splits` has integration- and type-dependent required child fields; `store` must match the configured Customer Area store name or the refund fails.
- If capture status is uncertain, the page directs the caller to the separate reversal endpoint. Its 400, 401, 403, 422, and 500 cases represent request, authentication, permission, validation, or server errors; the error body fields are optional in the schema.

> [!warning] Contradiction
> In this snapshot, the overview caps cumulative partial refunds at the captured amount (raw line 9), while the `amount` field says its value must be at most the authorized amount (raw line 37). These are differently stated limits; this entry does not treat authorization amount as permission to refund more than was captured.

## Detail locators

- `## Servers` and `## Parameters` — test endpoint `https://checkout-test.adyen.com/v72`, original-payment path reference, optional idempotency header, and refund request schema (raw lines 17–167). The body table includes optional application information, enhanced scheme data, reason values, line items, and platform split rules; nested “Yes” markings apply within their objects.
- `## Request examples` — one illustrative EUR 25.00 request with reference and merchant account; it does not expand the field rules (raw lines 169–181).
- `## Responses` — 201 success schema, separate refund and payment references, `received` status, optional response fields, and 400/401/403/422/500 error schemas (raw lines 182–305).
- `## Response examples` — illustrative 201 and generic error JSON, including example error codes and types rather than a complete error taxonomy (raw lines 307–386).

## Related

- Company: [[adyen]]
- Concept: [[adyen-refunds]]
- Background refund guide: [[source-adyen-docs-online-payments-refund]]

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/post/payments/(paymentPspReference)/refunds/2026-11-02|2026-11-02 Checkout API v72 refund endpoint snapshot]]
