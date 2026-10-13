---
title: "Adyen POS Card and Shopper Identifiers"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/card-acquisition/identifiers"
raw_files:
  - "adyen/docs/point-of-sale/card-acquisition/identifiers/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, card-acquisition, shopper-identifiers, card-alias, payment-account-reference, privacy]
---

## Overview

This Adyen Terminal API guide identifies card and shopper values that a merchant POS may receive in card-acquisition or payment responses and asynchronously in standard webhooks for recognition, insights, loyalty and recurring-use cases. Some fields are automatic, others require Customer Area additional-data settings, and shopper identifiers may first need to be collected or created by the merchant. It is a 2026-09-15 webpage snapshot with a 2020-03-27 `last_modified` value; its scheme availability and field paths do not establish current eligibility or a successful card acquisition, authorization or future payment.

## Key takeaways

- **Card alias** is a card-PAN representation for recognition and cannot be used to make payments. **Payment Account Reference (PAR)** represents the payment account behind a card or NFC wallet and may help link wallet and card activity when available; this dated guide says PAR is returned for Visa and Mastercard transactions when available. **Token variant** identifies an NFC wallet type and is not a payment token. By contrast, the **recurring detail reference** is the token the guide describes for recurring contract payments. Do not conflate alias, PAR, wallet variant, shopper reference and a chargeable token, or infer that a raw PAN is provided.
- The merchant defines a **shopper reference** of at least three characters; the guide advises excluding PII such as name or email. Shopper email must have been collected and submitted in a payment request to be returned. BIN and funding source are described as automatically returned in Terminal API responses; alias, issuer country/region, PAR, shopper reference and recurring detail reference need enabled additional-data options. PAR remains conditional on availability even when selected.
- For Terminal API responses, configure **Developers > Additional data** for the desired identifiers. The guide places values mainly in `AdditionalResponse`, either ampersand-separated key/value text or Base64-encoded JSON, and some also in structured fields. Standard webhook `additionalData` requires its own additional settings; PAR and token variant additionally need relevant **Developers > Additional data** switches. The example payment response and `AUTHORISATION` webhook are illustrative payloads, not proof that every request returns every identifier.
- Merchant use requires privacy review, explicit customer permission to store data, a merchant backend such as CRM/database, and merchant-owned business logic. The guide points to Adyen's Data Protection API for removing customer-related data stored with Adyen on a customer's request; this does not remove merchant-stored records by itself. The use-case matrix is illustrative and does not establish that card recognition, loyalty, tax-free treatment or recurring charge is authorized merely by receiving an identifier.

## Detail locators

- `## Requirements`, `## General considerations`, `## Customer data and privacy` — Terminal API and standard-webhook prerequisites, merchant storage/business logic, consent and erasure navigation.
- `## Overview of card and shopper identifiers` — BIN, alias, funding source, issuer country, PAR, recurring detail reference, shopper reference/email and token variant definitions; scheme/availability qualifications and use-case matrix.
- `## Receive identifiers in Terminal API responses` — automatic versus enabled values and exact Customer Area switches, response fields and `AdditionalResponse` encodings.
- `## Receive identifiers in webhooks` — standard-webhook additional settings, extra PAR/token-variant switches and sample `additionalData` payload.

## Related

- Company: [[adyen]]
- Terminal API/card-acquisition context: [[adyen-terminal-api]], [[source-adyen-docs-point-of-sale-card-acquisition]]
- Separate online-payment tokenization domain: [[adyen-tokenization]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/card-acquisition/identifiers/2026-09-15|2026-09-15 Adyen card and shopper identifiers snapshot]]
