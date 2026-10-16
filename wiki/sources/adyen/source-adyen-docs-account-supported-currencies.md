---
title: "Supported payout currencies | Adyen Docs"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/account/supported-currencies"
raw_files:
  - "adyen/docs/account/supported-currencies/2026-09-15.md"
tags: [adyen, payout-currencies, settlement-currencies, acquiring, bank-accounts]
---

## Overview

This Adyen guide to **supported payout currencies** (last modified 2023-02-22; captured 2026-09-15) explains an acquiring → settlement → payout path and lists settlement currencies, Adyen funds locations, and local or cross-border payout availability by **acquiring connection**. Its tables are a dated route matrix, not a universal promise of merchant-account enablement, payment-method support, a conversion-free path, payout initiation, or bank arrival. [[adyen-currencies-and-fx]]

## Key takeaways

- Adyen says settlement currency depends on acquiring region **and payment method**. The Adyen bank-account location depends on settlement currency and acquiring entity and affects payout rails. The methods acquired include regional or alternative methods only when enabled on the merchant account. The bank-account payout is a later step, separate from acquiring and settlement. See raw lines 19–29.
- A local payout uses the currency's local rails and requires a bank account in a country where that currency is legal tender; cross-border payout uses SWIFT and can take longer or incur the receiving bank's fees. A merchant account can configure multiple payout currencies but needs a payout account for each currency; the same details can serve multiple payout accounts for a multi-currency bank account. See raw lines 29–44.
- **Internal conflict:** the prose says BRL, INR, MYR, MXN, and AED cannot use SWIFT and can only be paid to a local bank account (raw line 40), but the EU and UK tables mark cross-border payout available for AED and MXN (raw lines 123, 138, 154, 166). Do not silently choose one rule; verify the current acquiring connection, method, account configuration and receiving-bank route with Adyen.
- The regional tables are keyed to acquiring connections, not simply the merchant's location. If a country is absent, the page directs the reader to the country or region of the acquiring connection that routes the transaction. The tables do not guarantee like-for-like processing/settlement/payout currency or specify merchant-specific FX rates. See raw lines 44–224 and [[source-adyen-docs-development-resources-currency-codes]] for separate FX terms.

## Detail locators

- **Acquiring, settlement currency, bank location and payout sequence:** raw lines 19–32.
- **Local/SWIFT bank location rule, named-currency restriction and account setup:** raw lines 34–44.
- **APAC acquiring-connection tables:** raw lines 48–115.
- **Europe acquiring-connection tables, including AED/MXN conflicting rows:** raw lines 117–176.
- **North America, South America and Middle East tables:** raw lines 178–224.

## Related

- [[adyen]]
- [[adyen-currencies-and-fx]]
- [[adyen-account-structure]] — merchant-account hierarchy and payout-account context
- [[source-adyen-docs-development-resources-currency-codes]] — separate currency decimals and contract-qualified FX information

## Raw Sources

- [[raw/adyen/docs/account/supported-currencies/2026-09-15|Adyen supported payout currencies — collected 2026-09-15]]
