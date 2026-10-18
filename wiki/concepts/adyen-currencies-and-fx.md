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

- [[source-adyen-docs-business-accounts-compliance-guidelines-foreign-exchange-fees]] — 2026-09-15-captured cross-region FX rate/fee disclosure guideline and variable, fixed and intermediary-fee examples; no-legal-advice boundary and inconsistent fixed-fee table.


- [[source-adyen-docs-platforms-online-payments-currency-conversion-refunds]] — 2023-modified, 2026-09-15-captured limited-availability Platforms FX-refund overview for processing/settlement currencies, rate-plus-markup remainder, user/platform booking choice and liable-account default.


- [[source-adyen-docs-platforms-online-payments-currency-conversion-payments-fix-settlement-currency]] — 2026-09-15 snapshot of pilot Platforms online-payment currency conversion fixing a user's settlement-currency goods amount while calculating the customer's marked-up processing-currency amount; prerequisites and remainder split booking are in the source.

- [[source-adyen-docs-platforms-online-payments-currency-conversion-payments]] — 2026-09-15 limited-availability Platforms overview of processing-versus-settlement currencies and the choice between fixed customer and fixed user amount paths.

- [[source-adyen-docs-platforms-online-payments-currency-conversion]] — 2026-09-15 capture of the limited-availability Platforms online conversion hub distinguishing accepted and settled currencies and routing to separate payment/refund guides; no implementation or current-eligibility proof.



- [[source-adyen-docs-platforms-online-payments-currency-conversion-refunds-your-user]] — 2026-09-15 limited-availability Platforms FX-refund pilot guide for booking the processing-versus-settlement-currency remainder to the user's balance account through original or rate-adjusted splits.

- [[source-adyen-docs-platforms-online-payments-currency-conversion-refunds-your-platform]] — 2026-09-15 limited-availability Platforms FX-refund guide for reusing original processing/settlement amounts and routing the remainder to the platform's liable balance account.


- [[source-adyen-docs-platforms-online-payments-currency-conversion-payments-fix-processing-currency]] — 2026-09-15 limited-availability Platforms guide for a fixed processing-currency customer amount and FX-calculated settlement-currency user split, with explicit remainder booking.



- [[source-adyen-docs-account-supported-currencies]] — 2023-modified, 2026-09-15-captured acquiring-connection, settlement-currency and local/SWIFT payout matrix with unresolved MXN/AED prose-versus-table conflict.


- [[source-adyen-docs-point-of-sale-currency-conversion-download-and-use-the-dcc-overview-file]] — 2026-09-15 Adyen Docs snapshot of live Customer Area DCC dashboard/filtered CSV reporting and transaction not-offered reasons; separate from transaction-time rate or offer proof.


- [[source-adyen-docs-point-of-sale-currency-conversion]] — 2026-09-15 Adyen POS DCC guide for the shopper's local-versus-card-billing-currency choice, terminal disclosure, merchant markup/reporting, and dated eligibility; separate from generic FX management fees.

- [[source-adyen-docs-platforms-in-person-payments-dynamic-currency-conversion]] — 2026-09-15 Adyen for Platforms in-person DCC pilot guide for terminal customer choice, DCC markup allocation between user and liable balance accounts, and dated eligibility/receipt constraints; separate from generic FX fees and the broader POS guide.


- [[source-adyen-docs-development-resources-currency-codes]] — Adyen currency-code and decimal table, Terminal API exception, four ISO differences, and contract-qualified FX fee structure (webpage snapshot, 2026-09-15).
