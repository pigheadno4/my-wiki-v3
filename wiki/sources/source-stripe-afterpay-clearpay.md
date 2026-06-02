---
title: "Stripe: Afterpay and Clearpay Payments"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-afterpay-clearpay-2025.md"
tags: [stripe, bnpl, afterpay, clearpay, cash-app, buy-now-pay-later, installments, connect, disputes]
---

## Summary

Deep-dive on Afterpay/Clearpay as a Stripe payment method. Covers the Cash App Afterpay US rebrand, country-specific transaction limits, US installment tiers, prohibited categories, dispute process, and Connect requirements.

## Key Details

**US rebrand**: Afterpay → Cash App Afterpay (no integration changes required).

**Domestic only**: customer country must match merchant country. Buyer country: shipping address → geocoded IP.

**Transaction limits by country**:

| Country | Currency | Limit |
| --- | --- | --- |
| AU | AUD | 1–4,000 |
| CA | CAD | 1–2,000 |
| NZ | NZD | 1–4,000 |
| UK | GBP | 1–1,200 |
| US | USD | 1–4,000 |

**US installment tiers**:
- $1–$399.99: Pay in 4 only
- $400–$2,000: Pay in 4 + monthly (interest-bearing 6 or 12 months)
- $2,000.01–$4,000: Monthly only

Non-US markets: Pay in 4 only.

**Disputes**: up to 120 days to file; 14-day merchant evidence window; 30-day Afterpay decision. Afterpay covers fraud losses.

**Refunds**: up to 120 days; async.

**Prohibited**: alcohol, bars/lounges, donations, pre-orders, NFTs, B2B.

**Connect**: direct, destination, separate charges + transfers all supported. Correct MCCs required.

## Raw Sources

- [[stripe-afterpay-clearpay-2025]] — verbatim webpage content (196 lines); fixed `_Connect_` → `*Connect*`; MP4 video CDN URL left as-is
