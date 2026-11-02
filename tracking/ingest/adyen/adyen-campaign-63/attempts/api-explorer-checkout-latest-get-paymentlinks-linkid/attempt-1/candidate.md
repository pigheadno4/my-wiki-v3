---
title: "Adyen Checkout API v72: Get a payment link"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/get/paymentLinks/(linkId)"
raw_files:
  - "adyen/api-explorer/Checkout/latest/get/paymentLinks/(linkId)/2026-11-02.md"
tags: [adyen, checkout-api, pay-by-link, payment-links]
---

## Overview

Captured 2026-11-02 API Explorer reference for Checkout TEST v72 `GET /paymentLinks/{linkId}`. It retrieves payment-link details by the link's unique `id`; the required `linkId` path parameter identifies the link, while the required response `reference` is the merchant's reference for identifying the payment in later status communications. This is a payment-link lookup, not a payment-session, token, payment modification or payment-outcome endpoint.

## Key takeaways

- The listed server is `https://checkout-test.adyen.com/v72`. A successful HTTP 200 means the lookup request succeeded; it does not attest to a live endpoint, successful authorization, capture, settlement or final financial result.
- Required top-level 200 response properties are `amount` (with required `currency` and minor-unit `value`), `id`, `merchantAccount`, `reference`, `status`, and shopper-facing `url`. `linkId` is the only listed request parameter; no request body or idempotency header is specified on this captured GET page.
- The exact link statuses are `active` (usable for payments), `expired` (expiry passed; no longer usable), `completed` (shopper completed the payment), and `paymentPending` (shopper is making a payment in an asynchronous flow). In particular, `paymentPending` is not a final payment outcome. Do not equate a link's `completed` label with capture or settlement.
- The response schema describes optional `expiresAt` with a default of 24 hours after creation and a maximum 70 days after creation, and optional `reusable` defaulting to `false`, meaning one successful payment only. These describe link settings, not a new default applied by this GET.
- Optional response properties have their own conditions: for example, `recurringProcessingModel` is required when `storePaymentMethodMode` is `askForConsent` or `enabled`; `lineItems` is required for listed BNPL methods; `shopperName` is required for some methods or PayPal Seller Protection. Nested `Yes` fields belong to their parent objects; they do not make every optional parent required.
- The page lists HTTP 400 (request problem), 401 (authentication required), 403 (insufficient permissions), 422 (validation error) and 500 (server processing failure). Their response properties are optional in the schema, and example codes/messages are examples, not a full failure contract. The page gives no deletion, propagation, reversal, retry, or idempotency guarantee.

## Detail locators

- Request identity, TEST v72 server, path parameter and 200 meaning: raw lines 5–22.
- Complete 200 schema, including optional nested fields, conditions, limits, statuses and URL: raw lines 24–229. The response example is at lines 301–322.
- Link expiry, reuse, reference and status: raw lines 72–73, 177–188 and 212–229.
- HTTP errors and their schemas: raw lines 232–300; illustrative error responses: lines 324–384.

## Related

- [[adyen]]
- [[adyen-unified-commerce]] — Pay by Link source route and wider commerce context.

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/get/paymentLinks/(linkId)/2026-11-02|Checkout API v72 GET payment link, captured 2026-11-02]]
