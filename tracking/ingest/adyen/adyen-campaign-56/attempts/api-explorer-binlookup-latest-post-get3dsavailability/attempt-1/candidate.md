---
title: "Adyen BinLookup API v54 POST /get3dsAvailability"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/BinLookup/latest/post/get3dsAvailability"
raw_files:
  - "adyen/api-explorer/BinLookup/latest/post/get3dsAvailability/2026-09-15.md"
tags: [adyen, bin-lookup, api, 3d-secure]
---

## Overview

Captured **BinLookup API v54** `POST /get3dsAvailability` reference on the `pal-test` server. It checks whether 3D Secure is available for a specified BIN or card brand; for 3DS2 it can return device-fingerprinting keys and related card-range information. This is an availability lookup, not an authentication or payment result. See [[adyen]] and [[adyen-3d-secure]].

## Key takeaways

- The request table marks only `merchantAccount` required at the top level. `cardNumber` (card number or BIN), `brands`, `recurringDetailReference`, `shopperReference` and `additionalData` are optional in the captured schema. The purpose describes a specified BIN or brand, but the table does not specify a required-one-of constraint; the example uses `cardNumber`. The page does not separately label the entire body as required.
- Optional 200 fields include `threeDS1Supported`, `threeDS2supported` (preserve the lower-case “s” in `supported`), `threeDS2CardRangeDetails`, `dsPublicKeys` and `binDetails`. Card-range details can contain brands, BIN ranges, supported 3DS2 versions and browser `threeDSMethodURL`; DS key entries include SDK version, public key and root certificates.
- The example response has `threeDS1Supported: true`, `threeDS2supported: false` and an empty 3DS2 card-range array. It is an illustration, not a guarantee of support for a merchant, card or region. A returned availability flag or DS key does not prove authentication, liability shift, authorization, capture or settlement.
- The documented server is `https://pal-test.adyen.com/pal/servlet/BinLookup/v54`. `latest` in the canonical URL does not establish today's latest API version or a live endpoint. Errors shown are 400, 401, 403, 422 and 500; only 400 has an example body.

## Detail locators

- Raw lines 5–12: purpose, 3DS2 keys and captured test server.
- Raw lines 14–34: full request schema and card-number request example.
- Raw lines 35–59 and 131–142: 200 response schema and illustrative response.
- Raw lines 62–129 and 144–154: error classes, schema and 400 example.

## Related

- [[adyen-3d-secure]] — provider 3DS concept.

## Raw Sources

- [[raw/adyen/api-explorer/BinLookup/latest/post/get3dsAvailability/2026-09-15|Captured BinLookup API v54 POST /get3dsAvailability reference]]