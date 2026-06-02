---
title: "Stripe: Billie Payments"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-billie-2025.md"
tags: [stripe, bnpl, billie, buy-now-pay-later, b2b, europe, connect, disputes]
---

## Summary

Deep-dive on Billie as a Stripe B2B BNPL payment method for Europe. Covers Pay in 30, multi-currency support, prohibited categories, dispute process, refunds, and Connect requirements.

## Key Details

**B2B only** — Pay in 30 days. Available to businesses across 11 European countries (DE, FR, NL, SE, NO, FI, AT, ES, DK, CH, GB). Multi-currency: EUR, SEK, NOK, DKK, GBP, CHF.

**Minimum**: 0.01 EUR or equivalent. No stated maximum.

**Include `line_items`**: improves approval rates (early access via Payments line items feature).

**Disputes**: 12-day merchant evidence window. Types: suspected fraud, double payments, order/amount discrepancy.

**Refunds**: 180-day window; async (up to 5 min). `refund.updated`/`refund.failed` webhooks.

**Connect**: `billie_payments` capability required on platform AND connected accounts. Statement descriptor source varies by charge type (direct → connected account; destination/SCT → platform; with `on_behalf_of` → connected account).

**Prohibited**: gambling, country clubs, adult content, financial institutions, crypto exchanges, postal services (govt), precious metals/jewelry.

**Supported currencies by country**: EUR for most; SEK/NOK/DKK multi-currency across DE/FR/NL/SE/NO/FI/AT/ES/DK; GBP for GB; CHF for CH.

## Raw Sources

- [[stripe-billie-2025]] — verbatim webpage content (187 lines); fixed `_webhook_` + `_Connect_` → `*italic*`; MP4 video URL left as-is
