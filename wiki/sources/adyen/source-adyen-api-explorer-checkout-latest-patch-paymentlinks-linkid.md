---
title: "Checkout API PATCH /paymentLinks/{linkId}: expire a payment link"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/patch/paymentLinks/(linkId)"
raw_files:
  - "adyen/api-explorer/Checkout/latest/patch/paymentLinks/(linkId)/2026-11-02.md"
tags: [adyen, checkout-api, pay-by-link, payment-links]
---

## Overview

This 2026-11-02-captured Checkout API reference documents `PATCH /paymentLinks/{linkId}` on the listed TEST v72 server, `https://checkout-test.adyen.com/v72`. It changes a particular payment link's status to `expired`, forcing its expiry. The path `linkId` identifies the link; it is separate from the payment `reference` returned in the link details and any payment `pspReference` in a generic error body. See [[adyen]] and [[adyen-unified-commerce]].

## Key takeaways

- **Request:** `linkId` is a required path string. The request body requires `status`; `expired` is its only listed value. The basic request example contains only `{"status":"expired"}` (raw lines 12–32). The page does not define a request idempotency key/header or another update operation.
- **Success:** HTTP 200 is described as a successful request and returns the payment-link object. Its required response fields are `amount` (with required `currency` and minor-unit `value`), `id`, `merchantAccount`, `reference`, `status`, and `url` (raw lines 35–44, 156, 191, 199, 226, 243). The response status vocabulary includes `active`, `expired`, `completed`, and `paymentPending`; the latter describes a shopper still making a payment in an asynchronous flow. The sample response has `status: "expired"` and `expiresAt` (raw lines 315–336). The linked [[source-adyen-docs-unified-commerce-pay-by-link-create-payment-links-api|Pay by Link API guide]] says forced expiry also sets `expiresAt` to the current date/time and illustrates both updated fields (its raw lines 3644–3648, 3839–3858).
- **Response detail, not PATCH inputs:** The large 200 schema describes link attributes, not additional request-body fields. It lists optional `expiresAt` with a 24-hour creation default and a 70-day maximum, optional `reusable` defaulting to `false` (one successful payment), and optional `updatedAt` (raw lines 87, 202, 242). These defaults and limits describe the link, not an ability to set them with this PATCH. Other response-only payment, shopper, split, tokenization and method fields, including nested or conditional requirements, are in raw lines 41–242.
- **Errors and boundary:** The page lists 400 malformed/understood request, 401 authentication required, 403 insufficient permission, 422 validation and 500 server error, with generic error fields and examples (raw lines 246–398). The 422 example says `Return URL is missing.`, but this PATCH request schema does not list `returnUrl`; do not infer a PATCH `returnUrl` requirement from that generic example. The page gives no authentication mechanism, idempotency contract or final payment/capture/refund outcome. An expired link is no longer usable for new payments; it does not establish reversal of an existing payment.

## Detail locators

- Purpose, TEST v72 server, path/body and request example: raw lines 5–32.
- Successful response schema, required/optional and conditional nested attributes: raw lines 33–243.
- Error schema and examples: raw lines 246–398.
- Successful example with link identity, status and expiry: raw lines 315–336.

## Related

- [[adyen]]
- [[adyen-unified-commerce]]
- [[adyen-online-payments]]
- [[source-adyen-docs-unified-commerce-pay-by-link-create-payment-links-api]]

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/patch/paymentLinks/(linkId)/2026-11-02|Checkout API PATCH payment link status, captured 2026-11-02]]
