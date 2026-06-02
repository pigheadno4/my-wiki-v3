---
title: "Stripe: Przelewy24 Payments"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-p24-2025.md"
tags: [stripe, p24, przelewy24, poland, eur, pln, bank-redirect, authenticated, prohibited-categories]
---

## Summary

Reference page for Przelewy24 (P24) on Stripe. Poland-only payment method **aggregator** (not just bank redirect — supports multiple payment types). Dual currency: EUR or PLN. No disputes, no recurring, 180-day refunds. Significant prohibited category list and website requirements.

## Key Details

- **Customers**: Poland only; **Currency**: EUR or PLN; **Business**: 40 countries
- **Type**: Payment aggregator (not just bank redirect)
- **Recurring**: No; **Disputes**: No chargebacks
- **Refunds**: 180 days
- **Checkout**: Not in subscription/setup mode; Invoicing: invite-only

**Prohibited business categories** (10):
Dropshipping, automotive sales/services/rentals, specialty food retail, pawn shops, higher education/vocational training, healthcare providers/medical, entertainment/event promotion, IT/telecom, advertising/marketing, real estate management/brokerage.

**Website requirements** (or P24 can suspend/terminate):
1. Products/services list with prices
2. Company legal details: address, tax number, registration number
3. Refund policy + privacy policy links

## Raw Sources

- [[stripe-p24-2025]] — verbatim webpage content; 6 flow diagram SVGs reused from existing `raw/assets/`
