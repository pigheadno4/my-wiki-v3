---
title: "Adyen Checkout API v72 POST /calculateTax"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/post/calculateTax"
raw_files:
  - "adyen/api-explorer/Checkout/latest/post/calculateTax/2026-11-02.md"
tags: [adyen, checkout, api, tax, india]
---

## Overview

This 2026-11-02 [[adyen]] Checkout API Explorer capture documents `POST /calculateTax` on the listed TEST v72 server. It calculates applicable tax from a taxable amount and tax context; the page gives India Liberalised Remittance Scheme Tax Collected at Source (LRS TCS) as the initial supported case. The response describes a canonical calculation, an attempt reference and an opaque token for a subsequent `/payments` request. The endpoint itself does not submit or complete a payment. The URL's `latest` segment does not establish current version, LIVE availability or merchant eligibility.

## Key takeaways

- The request-body table marks `merchantAccount`, `taxCalculationContext` and `taxableAmount` required; it does not separately state whole-body requiredness. Inside the required context, `calculationType` (initially only `LRS_TCS`), `lrs` declarations (`remittancePurpose` and `sublimitStatus`) and `taxCountryCode` (initially only `IN`) are marked required. The taxable amount requires a three-character ISO `currency` and integer `value` in minor units. No default, numeric amount limit or alternate conditional field path is stated.
- The 200 schema marks top-level `taxCalculation`, `taxCalculationReference` and `taxCalculationToken` optional. The calculation is described as informational in the initial release. Within the optional calculation, the schema lists accepted merchant/context/taxable amount, individual tax components, `totalTaxAmount` and `totalAmount`; nested `currency` and `value` fields are required when their amount object is present. The attempt reference identifies this calculation attempt; the token is described as opaque, encrypted and signed.
- The page directs a subsequent `/payments` request to use `taxCalculation.totalAmount` as `/payments.amount` and `taxCalculationToken` as the required token. Because the 200 response schema marks those containing fields optional, the page does not guarantee their presence in every success response. A successful calculation is not payment authorization, capture, settlement or tax remittance.
- The documented errors are 400 (request problem), 401 (authentication required), 403 (insufficient permissions), 422 (validation) and 500 (server processing). This endpoint page does not specify an idempotency header, token lifetime, deletion/reversal action, propagation timing or asynchronous payment outcome; those cannot be inferred from the calculation response.

## Detail locators

- Raw lines 5–10: endpoint purpose, downstream payment instruction and captured TEST v72 server.
- Raw lines 12–26: request-body field hierarchy, initial `LRS_TCS`/`IN` scope, declarations and minor-unit taxable amount.
- Raw lines 28–55: 200 response optional parents, nested amount fields, total and tax amounts, calculation reference and token.
- Raw lines 58–120: 400, 401, 403, 422 and 500 error descriptions and response schemas.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-api-explorer-checkout-latest-post-payments]]

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/post/calculateTax/2026-11-02|Adyen Checkout API Explorer POST /calculateTax (captured 2026-11-02)]]
