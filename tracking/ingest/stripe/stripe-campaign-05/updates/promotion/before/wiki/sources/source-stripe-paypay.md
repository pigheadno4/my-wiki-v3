---
title: "Stripe: PayPay Payments"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-paypay-2025.md"
tags: [stripe, wallets, paypay, japan, jpy, redirect]
---

## Summary

Overview of Stripe's PayPay integration — Japan-only digital wallet, JPY only, redirect-based. No recurring, Connect, disputes, or manual capture. Instant refunds up to 365 days.

## Key Details

**API enum**: `paypay`. Japan only (JP merchants and customers). JPY only.

**No recurring. No Connect support. No dispute support. No manual capture.**

**Refunds**: full and partial. 365-day window. Instant. `refund.updated` / `refund.failed` webhooks.

**Charge limits**: min 50 JPY, max 1,000,000 JPY.

**Product support**: Payment Links, Checkout (not subscription/setup mode), Elements (not Express Checkout Element).

**Prohibited**: cryptocurrency exchanges/wallets + additional categories at PayPal discretion.

**PayPay Connect**: requires invite (noted in wallets hub page).

## Raw Sources

- [[stripe-paypay-2025]] — verbatim hub page (109 lines); 1 italic fix (_webhook_)
