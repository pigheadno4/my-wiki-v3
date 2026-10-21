---
title: "Adyen Marketplace payment methods"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/payment-methods"
raw_files:
  - "adyen/docs/marketplaces/payment-methods/2026-09-15.md"
tags: [adyen, marketplaces, platforms, payment-methods]
---

## Overview

This 2026-09-15 Marketplace-path [[adyen]] page lists payment-method families documented for a marketplace integration under [[adyen-platforms]]. Before processing payments for users, a marketplace must configure the methods those users can accept in Customer Area (raw lines 15–23). The list is a navigation catalog, not evidence that a specific merchant, store, country, currency or user is enabled.

## Key takeaways

- The catalog names card schemes, wallets, bank-based and other local methods, including American Express, Mastercard and Visa; Apple Pay and Google Pay; ACH Direct Debit, iDEAL and PayTo; Klarna, Afterpay and PayPal, among others (raw lines 25–59). Each name links to its own method guide for applicable setup and conditions. The page does not provide method variant codes, channel flags, currencies, merchant approvals or transaction outcomes.
- The documented next steps link to adding payment methods and to viewing, enabling, disabling or updating them (raw lines 61–71). The add/manage guides supply operational detail beyond this list. Being named as supported does not show the method is configured, activated or available for an individual user or transaction.
- This Marketplace catalog differs in scope from the broader Platforms per-store ecommerce/POS variant table. Do not infer point-of-sale support or a specific payment-facilitator/store arrangement from this Marketplace list alone (raw lines 19–59).

## Detail locators

- Marketplace pre-processing configuration requirement and catalog scope: raw lines 15–23.
- Full linked method-family list: raw lines 25–59.
- Add and manage payment-method navigation: raw lines 61–71.

## Evidence boundary

The pinned list is a dated documentation support claim. It does not establish current method availability by region, currency or channel; specific Customer Area configuration; user eligibility; payment authorization; capture; settlement; or payout. A method-specific guide and actual merchant configuration are needed for those questions.

## Related

- [[adyen-platforms]] — modern platform and Marketplace context.
- [[source-adyen-docs-platforms-payment-methods]] — broader Platforms per-store ecommerce/POS variant catalog.

## Raw Sources

- [[raw/adyen/docs/marketplaces/payment-methods/2026-09-15|Pinned Marketplace payment-method catalog, captured 2026-09-15]]
