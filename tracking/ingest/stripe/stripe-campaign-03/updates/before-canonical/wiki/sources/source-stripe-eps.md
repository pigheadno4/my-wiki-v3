---
title: "Stripe: EPS Payments"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-eps-2025.md"
tags: [stripe, eps, austria, eur, bank-redirect, authenticated]
---

## Summary

Reference page for EPS on Stripe. Austria-only bank redirect, EUR-only, customer-authenticated with immediate notification. No disputes (authentication prevents chargebacks), no recurring payments, 180-day refund window.

## Key Details

- **Customers**: Austria only; **Currency**: EUR; **Confirmation**: Customer-authenticated (immediate notification)
- **Recurring**: No — single-use only
- **Disputes**: No chargebacks (authentication prevents them)
- **Refunds**: Up to 180 days
- **Business locations**: 40 countries
- **Checkout**: Not supported in subscription or setup mode; **Invoicing**: invite-only; **ECE**: unsupported

**6-step payment flow**: select EPS → select bank → redirect to bank login → enter credentials → scanner/SMS auth → payment confirmation → optional return to merchant site.

## Raw Sources

- [[stripe-eps-2025]] — verbatim webpage content; 6 flow diagram SVGs (2 new: select-bank, pincode-sms; 4 reused from existing `raw/assets/`)
