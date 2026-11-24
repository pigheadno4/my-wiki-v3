---
title: "Stripe: PromptPay Payments"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-promptpay-2025.md"
tags: [stripe, real-time-payments, promptpay, thailand, thb, qr-code, connect, billing]
---

## Summary

Overview of Stripe's PromptPay integration — Thailand-only QR code payment method. Instant confirmation. No statement descriptor customization. Refunds require customer bank account input via email. Duplicate QR risk (unlike PayNow). Billing via `send_invoice` only. TH merchant accounts only.

## Key Details

**API enum**: `promptpay`. THB only. Thailand customers and merchants only (TH accounts only).

**Statement descriptor**: ignored — `STRIPE PAYMENTS (THAILAND) LTD` shown with amount and unique reference code.

**Refunds**: Customer must provide bank account number for refund routing — Stripe emails customer at PaymentIntent email address to request. Refund fails without it.

**Duplicate QR risk**: re-scanning a completed QR code can deduct funds again. Stripe reimburses excess to merchant balance, but merchant must refund customer outside Stripe (check/cash/store credit). Unlike PayNow which rejects duplicate QR scans.

**Disputes**: "Not applicable" — low fraud risk. Stripe notes irregularities can occur and reviews them directly.

**Billing**: `send_invoice` only (confirmed in product support footnotes).

**Mobile Payment Element**: supports PromptPay on iOS only (not Android).

**No payout timing specified** in overview (unlike PayNow's T+1).

**Connect**: Yes. No capability name stated in overview.

**Product support**: Connect, Checkout (not subscription/setup mode), Payment Links, Elements (Express Checkout Element not supported; Mobile Payment Element iOS only), Subscriptions (`send_invoice`), Invoicing (`send_invoice`).

## Raw Sources

- [[stripe-promptpay-2025]] — verbatim webpage content (118 lines); no italic fixes; 4 SVG flow diagrams downloaded to assets/
