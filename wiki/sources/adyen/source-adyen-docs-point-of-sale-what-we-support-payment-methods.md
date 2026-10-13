---
title: "In-person payment methods | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/what-we-support/payment-methods"
raw_files:
  - "adyen/docs/point-of-sale/what-we-support/payment-methods/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, payment-methods, cards, wallets]
---

## Overview

This Adyen webpage snapshot lists payment-method families presented for point-of-sale integrations using Adyen Terminal API and Adyen-supplied payment terminals. Its tables distinguish card schemes, NFC and QR wallets, one-time numeric codes, and gift or prepaid cards by listed countries/regions, referenced and unreferenced refunds, and chargebacks. These historical listings are retrieval evidence, not proof of current merchant enablement, terminal/model support, currency acceptance, a live transaction result, or the behavior of a versioned SDK.

## Key takeaways

- The page is scoped to a Terminal API integration. It separately notes that Standalone terminals accept cards and wallet methods. Its card table includes global and local credit/debit schemes and US debit networks; the tables must be read per method and country/region rather than treating all listed methods as available for every merchant or terminal.
- Card entry includes chip, NFC contactless and magnetic swipe, with manual entry after those fail. The page warns that Bancontact, BankAxept, Cartes Bancaires, Dankort, girocard, and Interac decline transactions obtained by swipe or manual entry. US debit offline routing can return the `uspindebit` variant when the terminal does not yet know the eventual debit network. Co-badged card application selection is a separate routing concern.
- NFC wallets listed are Apple Pay, Google Pay and Samsung Pay on Adyen-supplied terminals; their payment flow is described as card-like with device presentation and verification. Wallet passes are a distinct feature, with Apple Wallet passes listed in this snapshot. QR wallets use merchant-presented or shopper-presented QR exchange, but several listed methods support only merchant-presented flow. The per-method QR table has materially different refund and chargeback entries.
- The page imposes method and region qualifications: unreferenced refunds are unavailable in Brazil and Mexico; GrabPay is limited to full referenced refunds; IRIS refunds and cancellations go through the acquirer bank rather than Adyen, and IRIS requires onboarding with a Greek bank while Adyen serves as gateway. BLIK is the one-time numeric-code method listed for Poland. Gift-card providers and local gift-card operations vary.
- The source's chargeback discussion distinguishes secure card-entry/verification combinations from offline or manually keyed transactions, which it describes as lacking fraud-chargeback liability shift. The Mobile solutions section explicitly says those solutions do not support every method listed here and redirects readers to their own supported-method status. No currency matrix appears on this page; do not infer currency support from a country/region cell.

## Detail locators

- `Credit and debit cards` — card-scheme and US debit table with payment type, refund/chargeback indicators and countries/regions; Brazil/Mexico refund restriction and girocard offline note.
- `Debit cards in the US`, `Card entry methods`, `Cardholder verification`, and `Co-badged cards` — network routing, entry restrictions, CVM, and application selection.
- `NFC wallets` and `Wallet passes` — listed wallet services, card-like terminal flow, and Apple Wallet pass scope.
- `QR code wallets` > `Supported flows`, `Refunds`, `Local onboarding` — method/region table, merchant-presented-only methods, GrabPay and IRIS exceptions, Greek-bank onboarding.
- `One-time numeric code` and `Prepaid and gift cards` — BLIK and stored-value provider tables, including limits on local gift-card operations.
- `Chargeback risk`, `Payment methods in Mobile solutions`, and `Next steps` — risk qualifications, mobile-solution limitation, and separate request/manage-payment-method navigation.

## Related

- Company: [[adyen]]
- Concept: [[adyen-terminal-api]]
- Related variant reference: [[adyen-payment-method-variants]] (transaction labels and Management API adding-method indicators have different scope)

## Raw Sources

- [[raw/adyen/docs/point-of-sale/what-we-support/payment-methods/2026-09-15|2026-09-15 Adyen POS payment-method snapshot]]
