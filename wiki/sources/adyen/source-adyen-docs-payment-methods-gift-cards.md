---
title: "Adyen gift cards"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gift-cards"
raw_files:
  - "adyen/docs/payment-methods/gift-cards/2026-09-15.md"
tags: [adyen, gift-cards, stored-value, online-payments, point-of-sale]
---

## Overview

This Adyen gift-card overview, last modified 2023-08-23 and captured 2026-09-15, describes virtual or plastic stored-value cards, online and in-person acceptance, partial payments, provider funding arrangements, other stored-value transactions, and a dated brand/provider table. It is not a current provider-availability list, merchant entitlement, or payment recipe. See [[adyen]], [[adyen-online-payments]], and [[adyen-pos-gift-cards]] for adjacent integration routes.

## Key takeaways

- Gift cards store monetary value on the card rather than in a bank account; some plastic cards can be reloaded and others are disposable. Adyen says it can process online and in-person gift-card payments, but merchant onboarding with a gift-card provider comes first. See raw lines 19–21.
- If balance is below the full purchase amount, a gift card can cover part and another method the rest; additional steps depend on integration. For a card usable only at the merchant, Adyen's page says funds are received upfront and redemption removes value through the provider without a new funds exchange. For a card usable at multiple businesses, the provider pays the redeeming merchant. These are distinct funding descriptions, not a settlement schedule. See raw lines 23–35.
- Other transactions, such as balance inquiry or deactivation, use separate stored-value guidance and depend on provider and online-versus-POS channel. The page routes to Web UI, API-only merchant UI, and in-person POS guides. See raw lines 37–39 and 47–65.
- A single capability row labeled “Loyalty program” lists Direct flow, International/Multiple scope, recurring and chargebacks unavailable, refunds/partial refunds and separate captures available, and partial captures unavailable. The refunds cell points to note [1], whose text discusses regulatory transaction-amount limits for some gift cards. Treat the row as a dated table entry, not a universal gift-card or account guarantee. See raw lines 41–45.
- The supported gift-card table maps named cards to country/region labels, paymentMethod.brand and provider; genericgiftcard is stated for cards not listed. These are dated directory labels. For example, Netscard's country cell includes a question mark, and Savvy is itself listed with genericgiftcard. Do not infer current country coverage, brand uniqueness, or provider onboarding from the table alone. See raw lines 67–115.

> [!warning] Dated matrix and directory qualifications
> The capability row is labeled “Loyalty program,” not every provider/card; its refunds footnote leads to a general transaction-amount limit statement (raw lines 41–45). The table includes an uncertain Netscard geography and a listed Savvy/genericgiftcard pairing (raw lines 69 and 95–102). Check provider and channel conditions before applying these entries to a specific program.

## Detail locators

- Stored-value definition and provider onboarding: raw lines 19–21.
- Partial payment and funding models: raw lines 23–35.
- Other operations and channel/provider limits: raw lines 37–39.
- Capability row and amount-limit note: raw lines 41–45.
- Web, API-only, POS navigation: raw lines 47–65.
- Brand/provider/country table and genericgiftcard statement: raw lines 67–115.

## Related

- [[adyen-online-payments]]
- [[adyen-pos-gift-cards]]
- [[source-adyen-docs-point-of-sale-alternative-payment-methods-gift-cards-terminal-api]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/gift-cards/2026-09-15|Gift cards overview, captured 2026-09-15]]
