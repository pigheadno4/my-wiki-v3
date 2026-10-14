---
title: "Adyen POS load funds to a gift card"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/alternative-payment-methods/gift-cards-terminal-api/load-a-balance"
raw_files:
  - "adyen/docs/point-of-sale/alternative-payment-methods/gift-cards-terminal-api/load-a-balance/2026-09-15.md"
tags: [adyen, point-of-sale, gift-cards, terminal-api, stored-value, load]
---

## Overview

This Adyen point-of-sale guide explains adding funds to an **activated** gift card, either as its initial loaded amount or to increase an existing balance. Its Terminal API operation is a `StoredValueRequest` with `StoredValueTransactionType=Load`, separate from the `PaymentRequest` used to redeem a gift card for a purchase. The page was last modified 2019-10-01 and captured 2026-09-15; it is historical documentation, not evidence of current provider eligibility or a completed live load. [[adyen]] [[adyen-pos-gift-cards]] [[adyen-pos-alternative-payment-methods]]

## Key takeaways

- The guide assumes a Terminal API integration with a payment terminal, the gift-card payment method added to the Adyen account, provider onboarding and an already activated card. A load request can establish the card's initial funded amount or add to an existing balance; it is not the activation action and does not itself document how the shopper pays for that value.
- Choose the card-entry method first: scan and include card number and expiry in the request, or send the request before swipe/manual-key entry so the terminal prompts. The stored-value account identifies `GiftCard`, provider and PAN, with entry-specific fields. The optional `ssc` in `SaleToAcquirerData` is described only for SVS cards as a secondary security code of up to eight digits, not a general PIN requirement.
- Send `SaleToPOIRequest` with `MessageClass=Service`, `MessageCategory=StoredValue`, and `StoredValueRequest.StoredValueData` containing `Load`, `ItemAmount`, `Currency` and the gift-card account identity. The `ServiceID` must be unique for the terminal for the preceding 48 hours; `SaleTransactionID.TransactionID` is a request reference recommended unique. This is an identity constraint, not an idempotent retry or duplicate-load guarantee.
- Inspect `StoredValueResponse`: `StoredValueResult.StoredValueTransactionType=Load` and `Response.Result=Success` are the guide's successful-load indicators, with response `ItemAmount`, `Currency` and a POI transaction ID. The guide calls response amount and currency the value associated with the card; do not interpret a load amount as a post-load balance without a balance inquiry. Request submission or sample code alone does not prove funds were added.
- The GBP 15 JSON request/response are examples. The Java example sets `ItemAmount` to 10 while the adjacent prose and JSON show 15, so the examples are inconsistent and should not be combined as one exact payload. Provider identifiers and sample card/terminal IDs are illustrative and do not establish current supported operations, currency, region or merchant entitlement.

## Detail locators

- Raw `# Load funds to a gift card` and `## Requirements` (lines 15–30): activated-card prerequisite, initial versus incremental balance, Terminal API and account/provider setup.
- Raw `## Make a load request` (lines 31–79): entry modes, header and reference fields, SVS-specific `ssc`, `Load`, amount/currency and stored-value account fields.
- Raw request examples (lines 80–172): illustrative scanned-card JSON and Java; note their GBP 15 versus 10 amount conflict.
- Raw response check and example (lines 174–215): `Load` plus `Success`, amount/currency and POI transaction ID; this is not a separate balance-query result.

## Related

- [[adyen-pos-gift-cards]] — POS gift-card lifecycle and provider-specific action route.
- [[adyen-pos-alternative-payment-methods]] — in-person alternative-method umbrella.
- [[adyen-terminal-api]] — terminal request/response architecture.

## Related raw API references

Navigation named by the guide, not further behavior reviewed for this entry:

- Activate a gift card — https://docs.adyen.com/point-of-sale/gift-cards-terminal-api/activate
- Check gift-card balance — https://docs.adyen.com/point-of-sale/gift-cards-terminal-api/query-the-balance
- Terminal API StoredValueRequest — https://docs.adyen.com/api-explorer/terminal-api/latest/post/storedvalue

## Raw Sources

- [[raw/adyen/docs/point-of-sale/alternative-payment-methods/gift-cards-terminal-api/load-a-balance/2026-09-15|Load funds to a gift card, fetched 2026-09-15]]
