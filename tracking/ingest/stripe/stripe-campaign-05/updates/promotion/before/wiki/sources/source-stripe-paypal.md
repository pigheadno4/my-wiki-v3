---
title: "Stripe: PayPal Payments (via Stripe)"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-paypal-2025.md"
tags: [stripe, wallets, paypal, europe, eur, gbp, usd, recurring, connect, marketplace, seller-protection, 180-day-refunds]
---

## Summary

Overview of Stripe's PayPal payment method — processing PayPal through Stripe's infrastructure for European businesses. Worldwide customers. 14 currencies. Connect for online marketplaces only (requires approval). 180-day refunds. PayPal fees not in Stripe tax invoice.

## Key Details

**API enum**: `paypal`. Worldwide customers. 30 European merchant countries. 14 currencies: EUR, GBP, USD, CHF, CZK, DKK, NOK, PLN, SEK, AUD, CAD, HKD, NZD, SGD.

**Distinct from PayPal-processed**: this is PayPal via Stripe's infrastructure — different from using your own PayPal account.

**Funding sources**: PayPal wallet, linked card/bank account, or BNPL.

**Connect: Partial** — online marketplaces only (e.g. Deliveroo, ManoMano). NOT available for platforms onboarding other businesses (e.g. Shopify). Requires manual approval. Only Destination and Separate charges; Direct and `on_behalf_of` not supported.

**Recurring**: Yes — may require additional approval.

**Refunds**: **180-day** window. Settlement preference determines funding source (Stripe balance or PayPal balance).

**PayPal fees**: listed in Balance reports but **not** in Stripe tax invoice — access from PayPal dashboard.

**PayPal Seller Protection**: applies to eligible transactions.

**Disputes**: direct customer contact for certain types must go through PayPal dashboard (not Stripe Dashboard).

**No minimum charge amount** (Stripe minimum/maximum enforced).

## Raw Sources

- [[stripe-paypal-2025]] — verbatim webpage content (160 lines); fixed `*Customer*` ×1 (line-start); 5 SVG flow diagrams downloaded to assets/
