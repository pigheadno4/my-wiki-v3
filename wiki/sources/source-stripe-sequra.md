---
title: "Stripe: SeQura Payments"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-sequra-2025.md"
tags: [stripe, bnpl, sequra, buy-now-pay-later, consumer, spain, installments, eur]
---

## Summary

Overview of SeQura as a Stripe consumer BNPL for Southern Europe (Spain only). Pay in 3 interest-free or up to 12 total installments. No Connect. Most extensive prohibited category list of any BNPL (~160+ categories).

## Key Details

**Consumer BNPL** — Spain (ES) only, EUR only. Pay in 3 interest-free or up to 12 installments. **No Connect support**.

**Transaction limits**: min €29. No stated maximum.

**Prohibited categories**: ~160+ categories — the most extensive prohibited list of any payment method on Stripe (exceeds even Mondu's ~90). Includes restaurants, doctors, legal services, marketplaces, digital goods, bakeries, and many more everyday categories.

**Disputes**: 12-day evidence window.

**Refunds**: 180-day window; async (up to 5 min). `refund.updated`/`refund.failed` webhooks.

## Raw Sources

- [[stripe-sequra-2025]] — verbatim webpage content (329 lines); fixed `_webhook_` → `*webhook*`; MP4 video URL left as-is
