---
title: "Stripe Docs — Link payment methods"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-link-payment-methods-2025.md"
tags: [stripe, link, link-payment-methods, instant-bank-payments, klarna, pix, upi, stablecoins, bnpl, us-only]
---

## Summary

Overview of Link's alternative payment methods feature (US-only). Link automatically presents non-card payment methods (Instant Bank Payments, Klarna, Pix, UPI, Stablecoins) with zero integration required.

## Key Facts

- **US-only**: Link payment methods only available to US Stripe accounts
- **Zero integration**: no code changes; Link handles routing automatically
- **Supported PMs**: Instant Bank Payments, Klarna, Pix, UPI, Stablecoins
- **Dashboard**: all payments appear as `link` type regardless of underlying PM used
- **5 eligibility filters** per session: business eligibility, presentment currency (local required for some), transaction limits, customer location, recurring/off-session support

## Customer Experience

**New customers**: email → location detected → PM selected → Link signup + auth → instant payment confirmation → details saved cross-merchant

**Returning customers**: auto-detected via email/phone/browser cookie → OTP → autofill saved details + shipping

## Disabling

- To remove a PM: must turn off Link entirely (also removes accelerated checkout + returning customer benefits)
- **Exception**: BNPL methods can be configured individually on Link settings page (due to higher fees)
- Enabling a PM outside Link disables its Link interface (customers can't save details for faster checkout)

## Related Pages

- [[stripe-link]] — Link concept page (primary)
- [[stripe-wallets]] — wallets concept page (short Link summary)
- [[source-stripe-link]] — broader Link overview (two PM paths, Instant Bank Payments, Payment Element caveats)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-link-payment-methods-2025]] — verbatim webpage content (62 lines)
