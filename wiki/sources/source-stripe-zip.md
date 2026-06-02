---
title: "Stripe: Zip Payments"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-zip-2025.md"
tags: [stripe, bnpl, zip, buy-now-pay-later, consumer, australia, us, installments, connect]
---

## Summary

Overview of Zip as a Stripe BNPL for Australia and the US. Three products: Zip Pay (AU line of credit), Zip Money (AU larger credit), Zip Pay In 4 (US installments). Connect supported, no manual capture. Unique 14-day direct merchant resolution window before dispute escalation.

## Key Details

**Consumer BNPL** — AU and US. AUD/USD. **Connect supported**. **No manual capture**. **No setup_future_usage**.

**Three products**:
- **Zip Pay** (AU): up to $1k AUD, flexible repayment (weekly/bi-weekly/monthly)
- **Zip Money** (AU): $1k–$50k AUD, up to 36-month interest-free
- **Zip Pay In 4** (US): $35–$1.5k USD, 4 installments over 6 weeks, first at purchase

**Disputes**: 180-day customer window. Zip requires merchant-first resolution — customer must contact merchant first; 14-day direct resolution period before escalating to Zip. Zip covers fraud losses.

**Refunds**: 180-day window.

**Buyer country**: shipping address → geocoded IP.

**Additional requirements**: delivery within 60 days; retain records 18 months; no surcharging; no cash refunds. US: goods must be in US; no gift cards; USD only.

**Prohibited categories**: country-specific, linked to external Zip docs (not published in page).

## Raw Sources

- [[stripe-zip-2025]] — verbatim webpage content (185 lines); MP4 video URL left as-is
