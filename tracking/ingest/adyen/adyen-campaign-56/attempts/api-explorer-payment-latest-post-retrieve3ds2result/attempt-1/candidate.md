---
title: "Adyen Payment API v68 POST /retrieve3ds2Result"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Payment/latest/post/retrieve3ds2Result"
raw_files:
  - "adyen/api-explorer/Payment/latest/post/retrieve3ds2Result/2026-09-15.md"
tags: [adyen, payment-api, classic, 3ds2, authentication]
---

## Overview

This 2026-09-15 [[adyen]] Payment API Explorer capture documents `POST /retrieve3ds2Result` at the listed TEST `Payment/v68` server. It retrieves `threeDS2Result` after a 3D Secure 2 authentication-only flow, using the `pspReference` returned by the earlier `/authorise` call. This is the Classic Payment API route, distinct from Checkout API payment and details endpoints. The URL's `latest` segment does not establish a newer captured version or LIVE availability.

## Key takeaways

- The request-body table marks `merchantAccount` and `pspReference` required properties. It does not separately state whole-body requiredness. The reference identifies the preceding `/authorise` request; it is not a generic shopper, order or capture reference.
- HTTP 200 says the retrieval request succeeded. The response schema marks the `threeDS2Result` object optional and lists authentication fields such as `authenticationValue`, `eci`, `transStatus`, `transStatusReason`, `dsTransID` and `timestamp` as optional. The captured page gives no 200 response example and no guarantee that every field is present. A retrieved authentication result is not itself payment authorization, capture, settlement or payout; a separate authorization step may be needed for an authentication-only flow.
- The page lists 400 request-reading, 401 authentication, 403 permission, 422 validation and 500 server errors, with common optional error fields. Its examples show 400, 401 and 500 payloads only. These are API failure illustrations, not payment outcome or retry rules. The page gives no deletion, propagation or asynchronous payment-status contract.

## Detail locators

- Raw lines 5–18: purpose, TEST Payment/v68 server and required request properties. Lines 20–28: request example.
- Raw lines 29–51: 200 response and nested 3DS2 authentication fields. Lines 54–121: error status tables. Lines 123–160: error examples.

## Related

- [[adyen]]
- [[adyen-3d-secure]]
- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-3d-secure-authentication-native-3ds2-authentication-only-integration]] — legacy flow and separate-authorization context.

## Raw Sources

- [[raw/adyen/api-explorer/Payment/latest/post/retrieve3ds2Result/2026-09-15|Adyen Payment API Explorer POST /retrieve3ds2Result (captured 2026-09-15)]]
