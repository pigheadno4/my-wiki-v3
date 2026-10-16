---
title: "Adyen Currencies and FX"
type: concept
category: technology
tags: [adyen, currencies, minor-units, foreign-exchange]
---

## Overview

Adyen's dated payout-currency guide distinguishes payment acquiring, settlement into an Adyen bank account, and a later payout to the merchant bank. Settlement currency depends on acquiring region and payment method; local versus SWIFT payout depends on the receiving-bank currency/location and the acquiring-connection table. Per-currency payout accounts are configured at merchant-account level. The page's blanket no-SWIFT statement for MXN and AED conflicts with EU/UK table rows marking cross-border payout available, so the applicable route requires current Adyen/account verification. [[source-adyen-docs-account-supported-currencies]]


Adyen's API currency reference pairs each currency code with an amount decimal count. In the 2026-09-15 snapshot, most Adyen APIs require amount values in minor units; Terminal API is the stated exception. For CLP, CVE, IDR, and ISK, Adyen says its table's decimals take precedence over the differing ISO 4217 counts when submitting minor-unit amounts. The snapshot lists CLP 2, CVE 0, IDR 0, and ISK 2.

Where Adyen converts a transaction amount between currencies, it describes an FX reference rate plus an FX management fee or spread. The fee calculation comes from the merchant's Adyen contract; the default currency-category route and optional Visa/Mastercard scheme-rate route are detailed in the source. The snapshot does not establish a current currency's availability or a merchant-specific conversion rate or fee.

## Sources

- [[source-adyen-docs-account-supported-currencies]] — 2023-modified, 2026-09-15-captured acquiring-connection, settlement-currency and local/SWIFT payout matrix with unresolved MXN/AED prose-versus-table conflict.


- [[source-adyen-docs-point-of-sale-currency-conversion-download-and-use-the-dcc-overview-file]] — 2026-09-15 Adyen Docs snapshot of live Customer Area DCC dashboard/filtered CSV reporting and transaction not-offered reasons; separate from transaction-time rate or offer proof.


- [[source-adyen-docs-point-of-sale-currency-conversion]] — 2026-09-15 Adyen POS DCC guide for the shopper's local-versus-card-billing-currency choice, terminal disclosure, merchant markup/reporting, and dated eligibility; separate from generic FX management fees.


- [[source-adyen-docs-development-resources-currency-codes]] — Adyen currency-code and decimal table, Terminal API exception, four ISO differences, and contract-qualified FX fee structure (webpage snapshot, 2026-09-15).
