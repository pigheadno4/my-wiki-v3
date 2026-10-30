---
title: "Adyen Payment API v68 POST /getAuthenticationResult"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Payment/latest/post/getAuthenticationResult"
raw_files:
  - "adyen/api-explorer/Payment/latest/post/getAuthenticationResult/2026-09-15.md"
tags: [adyen, payment-api, classic, 3d-secure, authentication]
---

## Overview

Captured **Payment API v68** `POST /getAuthenticationResult` reference on the `pal-test` server. It returns a 3D Secure authentication result after **authentication only**, using the transaction's `pspReference` and `merchantAccount`. This is the Classic Payment API route, distinct from Checkout API; [[source-adyen-api-explorer-payment-latest-overview]] marks the Payment API inactive and directs new integrations to Checkout. See [[adyen]] and [[adyen-3d-secure]].

## Key takeaways

- The request table marks `merchantAccount` (the account used for authentication) and the transaction `pspReference` required. The page does not separately label the request body as required. The example supplies those two properties.
- The 200 response schema has optional `threeDS1Result` and `threeDS2Result` objects. The 3DS1 object can include CAVV, ECI, authentication/offered responses and XID. The 3DS2 object can include authentication value, ECI, transaction IDs, status/reason, challenge and exemption indicators, and Cartes Bancaires-specific fields. Consult the raw response table for field meanings and allowed values.
- A successful HTTP request and authentication data do not establish a payment authorization, capture, settlement, refund or liability shift. The raw gives no 200 response example, no payment `resultCode`, and no later financial-state transition.
- The listed server is `https://pal-test.adyen.com/pal/servlet/Payment/v68`. `latest` in the canonical URL does not establish a current latest version or a live endpoint.
- Error classes shown are 400 (request parsing), 401 (authentication), 403 (permissions), 422 (validation) and 500 (server processing); only 400, 401 and 500 have illustrative response bodies.

## Detail locators

- Raw lines 5–18: endpoint purpose, captured server and both required request properties.
- Raw lines 20–28: request example.
- Raw lines 29–58: 200 response schema, including optional 3DS1/3DS2 fields and enum text.
- Raw lines 61–128 and 130–167: error schemas and illustrative error response bodies.

## Related

- [[adyen-3d-secure]] — provider 3D Secure concept.
- [[source-adyen-api-explorer-payment-latest-overview]] — Payment API v68 lifecycle and endpoint directory.

## Raw Sources

- [[raw/adyen/api-explorer/Payment/latest/post/getAuthenticationResult/2026-09-15|Captured Payment API v68 POST /getAuthenticationResult reference]]