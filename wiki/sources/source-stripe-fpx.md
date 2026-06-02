---
title: "Stripe: FPX Payments"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-fpx-2025.md"
tags: [stripe, fpx, malaysia, myr, bank-redirect, authenticated, brn]
---

## Summary

Reference page for FPX (Financial Process Exchange) on Stripe. Malaysia-only bank redirect, MYR-only, customer-authenticated two-step auth. Requires Business Registration Number (BRN). No disputes, no recurring. Refunds: up to 60 days, async ~1 week.

## Key Details

- **Customers**: Malaysia only; **Currency**: MYR; **Business locations**: MY only
- **BRN required**: Businesses must provide Business Registration Number to process FPX and receive payouts
- **Recurring**: No; **Disputes**: No chargebacks (authentication)
- **Refunds**: Up to 60 days; async ~1 week; `refund.updated`/`refund.failed` webhooks; refund can fail → returned to Stripe balance
- **Payout timing**: 5 business days
- **Checkout**: Not in subscription or setup mode; ECE: unsupported

**Payment flow**: checkout → bank selection → redirect to bank → 2-step auth (SMS or scanner) → confirmation → optional return.

## Raw Sources

- [[stripe-fpx-2025]] — verbatim webpage content; 6 flow diagram SVGs reused from existing `raw/assets/`; video URL kept as external reference
