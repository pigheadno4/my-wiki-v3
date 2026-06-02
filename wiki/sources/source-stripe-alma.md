---
title: "Stripe: Alma Payments"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-alma-2025.md"
tags: [stripe, bnpl, alma, buy-now-pay-later, europe, installments, connect, disputes]
---

## Summary

Deep-dive on Alma as a Stripe BNPL payment method for Europe. Covers payment options, transaction limits, T+3 payout, prohibited categories, required customer terms, refunds, dispute process, and the Connect marketplace restriction.

## Key Details

**Coverage**: FR, IT, ES, NL, BE, LU. EUR only. 50–5,000 EUR range.

**Payment options**: Pay in 2, 3, or 4 (all interest-free). First installment may be higher based on customer credit factors.

**Payout timing**: T+3 (not standard).

**Refunds**: up to 180 days; async (up to 5 min). `refund.updated`/`refund.failed` webhooks.

**Disputes**: 120-day customer window; 14-day merchant evidence; **25-day Alma decision**. Alma covers fraud. Merchants must maintain low fraud/dispute rates or risk losing access.

**Connect restriction**: online marketplaces only (e.g., Deliveroo, ManoMano) — NOT for platforms that onboard other businesses (e.g., Shopify/Squarespace). Requires Dashboard onboarding request. Destination, separate, direct, `on_behalf_of` all supported.

**Prohibited**: sole proprietorships, B2B, education, professional services, transportation, travel, telecom/utilities, veterinary.

**Required customer terms** (must add to general terms of sale):
- Purchases in installments available via Alma
- Subject to Alma T&Cs
- Non-approval may cancel purchase
- 14-day withdrawal right

## Raw Sources

- [[stripe-alma-2025]] — verbatim webpage content (170 lines); fixed `_webhook_` → `*webhook*`; MP4 video CDN URL left as-is
