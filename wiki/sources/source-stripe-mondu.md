---
title: "Stripe: Mondu Payments"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-mondu-2025.md"
tags: [stripe, bnpl, mondu, buy-now-pay-later, b2b, europe, uk, disputes, refunds]
---

## Summary

Deep-dive on Mondu as a Stripe B2B BNPL payment method (Pay in 30) for EU/UK businesses. Multi-currency, no Connect, and the most extensive prohibited category list of any payment method (~90 categories).

## Key Details

**B2B only** — Pay in 30 days. EU/UK, 14 merchant countries. Multi-currency: EUR, CHF, GBP. **No Connect support**.

**Maximum**: €19,999.99 EUR (or equivalent). No stated minimum.

**Disputes**: 12-day evidence window.

**Refunds**: 180-day window; async (up to 5 min). `refund.updated`/`refund.failed` webhooks.

**Prohibited categories** (~90, the most extensive of any payment method): transportation (airlines, buses, taxis, ferries, railways), services (cleaning, repair, landscaping, laundry), gambling, healthcare (nursing, opticians, ambulances), government services, chemicals, fuel, utilities, crypto, pawn shops, timeshares, and many more.

**Currencies by country**: EUR for DE/NL/FR/FI/AT/IT/ES/BE/PL/NO/DK/SE/CH; CHF for CH; GBP for GB.

## Raw Sources

- [[stripe-mondu-2025]] — verbatim webpage content (261 lines); fixed `_webhook_` → `*webhook*`; MP4 video URL left as-is
