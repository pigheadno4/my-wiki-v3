---
title: "Stripe: Accept a Klarna Payment"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-klarna-accept-payment-2025.md"
tags: [stripe, bnpl, klarna, buy-now-pay-later, checkout, payment-intents, elements, ios, testing]
---

## Summary

Integration guide for Klarna across Checkout, Elements (Checkout Sessions + PaymentIntents), Direct API, iOS, and Android. Notable for the most comprehensive per-country test data of any Stripe doc. Covers billing prefill for conversion optimization and manual capture.

## Key Details

**Prefill billing details** via `payment_method_options.klarna` and customer billing address — improves conversion and enables correct payment option display.

**Manual capture**: supported with `capture_method: 'manual'`.

**Sandbox test data**: per-country approved/denied credentials for all 23 customer countries. Test tip: amount `3500` in local currency covers all options except Financing. 2FA: any 6-digit code; `999999` to fail. Repayment: Direct Debit IBAN, Demo Bank, test credit/debit cards.

**iOS**: webview-based authentication via `confirmPayment` — customer confirms in Klarna's webview then returns to app.

## Raw Sources

- [[stripe-klarna-accept-payment-2025]] — verbatim webpage content (3657 lines); fixed `_confirm_` (4×), `_client secret_` (4×), `_webhook_` (4×); downloaded CDN image 4× → `raw/assets/stripe-klarna-kpp-prefilled-customized.png`
