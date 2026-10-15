---
title: "Tokenization | Adyen Classic API"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/tokenization"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/2026-09-15.md"
tags: [adyen, classic-api, tokenization, recurring-payments, shopper-reference]
---

## Overview

This dated Adyen Classic API overview defines a recurring contract as one or more stored payment details linked to a unique shopper under a merchant account. The contract is identified by `shopperReference` plus `merchantAccount`; each detail has a unique 16-character `recurringDetailReference` that can stand in for the payment details in a later payment request. The page marks the endpoint inactive for new integrations and directs new builds to Checkout API and existing users toward migration.

## Key takeaways

- The page describes shopper-present one-click/Card on File transactions as requiring the shopper's CVC for each transaction. It says the shopper chooses to store details at the first payment by selecting a checkbox; full card authorization, including security-code checks and 3D Secure if applicable, accompanies each payment in this described flow.
- For shopper-not-present Subscription/Card on File transactions, the page describes a shopper allowing merchant deduction at an agreed timeframe, with subsequent recurring payments not needing the card security code. Details may be stored with Adyen or a third party; the page routes third-party-stored details to a separate authorization guide.
- Classic recurring contracts are established and used within one merchant account by default. Cross-account reuse among accounts associated with a company account requires configuration through Adyen Support; the page does not establish that it is enabled for any particular account.
- The page advises merchants to notify shoppers that their details will be used for recurring payments and recommends a website note. The described checkbox is a first-payment shopper choice for the one-click flow, not evidence of consent for every recurring model or of a successful later authorization.
- The page says most recurring payments use the same method as the initial payment but points to method-specific exceptions and a separate supported-method list. It does not enumerate those exceptions here.

## Detail locators

- Raw lines 16–21 — inactive endpoint lifecycle and Checkout API migration routes.
- Raw lines 23–25 — contract identity, merchant/shopper scope, and stored-detail reference role.
- Raw lines 27–37 — third-party-detail route, shopper-present and shopper-not-present contract descriptions, and optional cross-account configuration.
- `Supported payment methods` — same-method generalization, exceptions route, shopper notification guidance, and methods-list route.

## Related

- Company: [[adyen]]
- Concept: [[adyen-tokenization]]
- Related concept: [[recurring-payments]]
- Related sources: [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-tokenization-store-payment-details]], [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-tokenization-retrieve-stored-details]]

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/tokenization/2026-09-15|2026-09-15 snapshot — Classic tokenization overview]]
