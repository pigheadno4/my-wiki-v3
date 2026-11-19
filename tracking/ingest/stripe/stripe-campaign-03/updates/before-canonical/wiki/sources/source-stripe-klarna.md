---
title: "Stripe: Klarna Payments"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-klarna-2025.md"
tags: [stripe, bnpl, klarna, buy-now-pay-later, installments, subscriptions, connect, cross-border]
---

## Summary

Deep-dive on Klarna as a Stripe BNPL payment method. Covers the 4 payment options with per-country/per-currency limits, cross-border payment rules, refund mechanics, Connect, and Klarna's loss liability model.

## Key Details

**Coverage**: 23 customer countries, 32 merchant countries, 13 currencies. Broadest BNPL on Stripe.

**4 payment options**:
- **Pay in full**: immediate payment via card/bank. Most countries/currencies.
- **Pay later**: 30-day single payment. ~20 countries.
- **Pay in 3 or 4**: interest-free installments. ~20 countries.
- **Financing**: up to 36 months (may include interest). AT, CA, DE, FI, GB, NO, SE, US.

**Recurring payments**: Pay in full, Pay later, and Pay in 3 or 4 support subscriptions (with country restrictions). Not available with `setup_future_usage`.

**No B2B** — Klarna rules explicitly prohibit business-to-business payments.

**Cross-border payments**: EEA ↔ EEA/CH/UK allowed (present in customer's local currency). Non-EEA countries (AU, CA, NZ, US) must sell domestically.

**Klarna takes loss liability** if customer can't repay installments.

**Refunds**: 180-day window; 5-7 business days. Partial refunds spread evenly across remaining installments. Refunds blocked during active disputes.

**Connect**: all charge types supported. `klarna_payments` capability required for Express/Custom accounts.

**Buyer country**: shipping address → geocoded IP fallback.

## Raw Sources

- [[stripe-klarna-2025]] — verbatim webpage content (318 lines); fixed `_European Economic Area (EEA)_` → `*EEA*`; MP4 video URL left as-is; tables garbled (rendering artifact)
