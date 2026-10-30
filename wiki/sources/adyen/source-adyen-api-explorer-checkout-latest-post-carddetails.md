---
title: "Adyen Checkout API v72 POST /cardDetails"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/post/cardDetails"
raw_files:
  - "adyen/api-explorer/Checkout/latest/post/cardDetails/2026-09-15.md"
tags: [adyen, checkout, api, cards, co-badged]
---

## Overview

This 2026-09-15 [[adyen]] Checkout API Explorer capture documents `POST /cardDetails` on the listed TEST v72 server. It looks up brands and other card or network-token details to inform transaction-routing and eligibility decisions. It is a card-information lookup, not a payment or authorization request. The URL's `latest` segment does not establish the current API version or LIVE availability.

## Key takeaways

- The request table marks `merchantAccount` required. `cardNumber`, `encryptedCardNumber`, `countryCode`, and `supportedBrands` are marked optional; the table does not explicitly state a required either-or rule for the two card-number fields or separately state whole-body requiredness. A raw `cardNumber` can be a minimum six-digit prefix, while a full number gives the best result; collecting raw card data requires full PCI compliance. `encryptedCardNumber` is the documented alternative. The `Idempotency-Key` header is optional.
- When `supportedBrands` is supplied, the response can indicate support for each identified brand. Without it, the API uses brands configured for the merchant account and, if provided, `countryCode`. In an API-only card-data integration, the page directs the merchant to identify co-badged cards and let the shopper choose the brand if both are supported. A response is not proof of a particular card's acceptance or a completed routing choice.
- The 200 response schema lists optional `brands` (with optional `type`, `supported`, and healthcare eligibility), `fundingSource`, `isCardCommercial`, and `issuingCountryCode`. Its examples show a Visa/Cartes Bancaires card with different `supported` values depending on the request's `supportedBrands`; they are illustrations, not guaranteed account or card outcomes. This captured page has no separate error-response table, so a specific failure code or retry behavior cannot be inferred.
- The developer-resources paragraph names a “BIN Lookup API” Postman collection even though this page's title, URL and server place the documented operation in Checkout `/cardDetails`. Treat that paragraph as navigation, not a change in endpoint identity.

## Detail locators

- Raw lines 5–11: purpose, supported-brand and co-badged shopper-choice conditions. Lines 35–42: developer-resources wording and captured TEST v72 server.
- Raw lines 44–59: header and request-body schema. Lines 61–82: basic and supported-brands request examples.
- Raw lines 83–97: 200 response schema. Lines 99–139: two response examples and their support flags.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[co-badged-cards]]

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/post/cardDetails/2026-09-15|Adyen Checkout API Explorer POST /cardDetails (captured 2026-09-15)]]
