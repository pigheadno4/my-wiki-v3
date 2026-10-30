---
title: "Adyen Checkout API v72 POST /payments"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/post/payments"
raw_files:
  - "adyen/api-explorer/Checkout/latest/post/payments/2026-09-15.md"
tags: [adyen, checkout, api, online-payments, payment]
---

## Overview

This 2026-09-15 capture of [[adyen]] Checkout API Explorer documents `POST /payments`, which sends a transaction amount and shopper payment details to start a payment. The captured server is `https://checkout-test.adyen.com/v72`; the URL segment `latest` is a navigation route, not evidence of a later API version or LIVE behavior. This endpoint is part of the [[adyen-online-payments]] Advanced flow.

## Key takeaways

- The request table marks `amount` (currency and minor-unit value), `merchantAccount`, `paymentMethod`, `reference`, and `returnUrl` required. The table does not separately state whether the entire HTTP request body is required. `returnUrl` is the return destination for redirects and must exclude personal information. The optional `Idempotency-Key` header has a 64-character maximum.
- Method and flow determine further inputs. For example, the page requires billing address for browser and mobile 3D Secure 2 transactions, full browser information for web 3D Secure, and `origin` for browser-based Web 3D Secure 2. `lineItems` is required for the listed buy-now-pay-later methods. `shopperReference` is required for recurring payments and `recurringProcessingModel` for storing or using stored details. Raw card details are expressly limited to fully PCI-compliant collection. Consult the exact field descriptions and method guides before constructing a method-specific request.
- In a direct flow, the response can provide `pspReference` and `resultCode`, such as `Authorised` or `Refused`. A redirect or additional-action flow returns `action`; the response table says `pspReference` for such methods arrives in `/payments/details`. `IdentifyShopper`, `ChallengeShopper`, `RedirectShopper`, `PresentToShopper`, `Pending`, and `Received` have distinct non-final or further-action meanings. An authentication-only result is not a payment authorization. The response table calls `Authorised`, `Cancelled`, `Error`, and `Refused` final payment-result states; it does not establish capture, settlement, or merchant payout.
- HTTP 200 means the request succeeded, not that every payment was authorised: the 200 schema includes refusal and error result codes. Separate 400, 401, 403, 422, and 500 sections describe request, authentication, permission, validation, and server errors. The examples are illustrative TEST payloads and responses, not guarantees for a merchant or a live transaction.

## Detail locators

- Raw lines 5-22: endpoint purpose, direct/action split, captured TEST v72 server and idempotency header.
- Raw lines 25-520: complete request schema, including requiredness and conditional 3DS, recurring, platform, token, split, and method fields. Raw lines 523-1007: request examples.
- Raw lines 1008-1087: 200 response schema, result-code meanings, PSP reference timing and additional-details handoff. Raw lines 1090-1157: HTTP error schemas.
- Raw lines 1159-1457: response and error examples. The card and redirect examples show different outcomes; do not generalize an example to all methods.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-api-idempotency]]
- [[source-adyen-docs-online-payments-build-your-integration-advanced-flow]] — flow-level client action, webhook and live-region qualifications.

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/post/payments/2026-09-15|Adyen Checkout API Explorer POST /payments (captured 2026-09-15)]]
