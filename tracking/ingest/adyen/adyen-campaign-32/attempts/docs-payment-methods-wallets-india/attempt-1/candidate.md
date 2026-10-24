---
title: "Adyen Wallets India overview"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/wallets-india"
raw_files:
  - "adyen/docs/payment-methods/wallets-india/2026-09-15.md"
tags: [adyen, wallets-india, india, online-payments]
---

## Overview

This 2026-09-15 Adyen Wallets India overview describes a shopper choosing from available wallet options and being redirected to that wallet's page to complete a payment. It says processing requires compliance with regulations in India plus a **local entity and local integration in India**, and directs merchants to their account manager or Support for detail. Its dated capability table and channel links do not prove current legal compliance, merchant enablement or an actual payment outcome. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The captured feature table classifies this as a **Wallets / Direct** payment flow for country **IN** and currency **INR**. It marks refunds, partial refunds and multiple partial refunds supported; recurring, separate captures, partial captures, multiple partial captures and chargebacks unsupported. These are page-level capability marks, not an entitlement or a description of specific refund processing or payment settlement.
- The guide points to **Web** pre-built UI, **API-only** custom UI for website/iOS/Android, and **Pay by Link** routes. This overview itself gives no request fields, SDK versions, redirect-return handling, final-status interpretation, or per-wallet availability; the linked implementation guides need separate evidence.
- The table's 'Direct' category and the prose's wallet-page redirect describe different aspects of the captured offering; do not infer that the shopper stays on the merchant page or that redirect completion establishes authorization.

## Detail locators

- India regulation/local-entity/local-integration prerequisites and contact route: raw line 19. Wallet selection and redirect: raw line 21. Full country/currency and feature table: raw lines 23–25.
- Web, API-only and Pay by Link navigation: raw lines 27–45.

## Related

- [[adyen-online-payments]] — online payment-method context.
- [[source-adyen-docs-payment-methods-wallets-india-api-only]] — separately captured API-only implementation route; this overview alone does not supply its behavior.

## Raw Sources

- [[raw/adyen/docs/payment-methods/wallets-india/2026-09-15|Wallets India overview, captured 2026-09-15]]
