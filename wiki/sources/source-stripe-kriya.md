---
title: "Stripe: Kriya Payments"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-kriya-2025.md"
tags: [stripe, bnpl, kriya, buy-now-pay-later, b2b, uk, disputes, refunds]
---

## Summary

Deep-dive on Kriya as a Stripe B2B BNPL payment method. UK-only, GBP-only, no Connect support. Notable for the most extensive prohibited category list of any BNPL method.

## Key Details

**B2B only** — UK only, GBP only. **No Connect support** — only BNPL method on Stripe without it.

**Disputes**: 12-day evidence window. Types: fraud, double payments, amount discrepancy.

**Refunds**: 180-day window; async (up to 5 min). `refund.updated`/`refund.failed` webhooks.

**Prohibited categories** (~36, most extensive of any BNPL): advertising, airlines, gambling, car rentals, charities, courier services, cruise lines, adult content, drugs/pharmacies, financial institutions, hotels, insurance underwriting, massage parlors, crypto, pawn shops, petroleum, political/religious organizations, security brokers, travel agencies, timeshares, trailer parks, video arcades, and more.

## Raw Sources

- [[stripe-kriya-2025]] — verbatim webpage content (171 lines); fixed `_webhook_` → `*webhook*`; MP4 video URL left as-is
