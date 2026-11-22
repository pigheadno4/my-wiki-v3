---
title: "Stripe Docs — Klarna on Link"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-klarna-on-link-2025.md"
tags: [stripe, link, klarna, bnpl, us-only, buy-now-pay-later, installments]
---

## Summary

Guide for Klarna as a Link payment method (US-only). Auto-enabled with Link; only supported in Payment Links, Stripe Checkout (Hosted), and Payment Element.

## Key Facts

- **US-only** — Link customers in the US only
- **Supported integrations**: Payment Links, Stripe Checkout (Hosted), Payment Element only — not other payment flows
- **Disable**: Link settings → unselect "Pay later with Klarna"
- **Settlement**: Stripe deposits full purchase amount immediately; merchant does NOT wait for Klarna installment collection
- **New customer flow**: "Pay later" → identity confirmation → Klarna account creation → select plan → Pay
- **Returning customer**: Klarna details pre-saved to Link account → "Pay later" → review pre-populated details → Pay

## Test Cards

| Card | Number | Usage |
| --- | --- | --- |
| Visa (credit) | 4242424242424242 | Installment plans |
| Unbranded (debit) | 4687388888888881 | Financing plans |

## CDN Assets (7 screenshots)

- `raw/assets/stripe-klarna-link-pay-later.png` — pay later selection (138 KB)
- `raw/assets/stripe-klarna-link-confirm-info.png` — identity confirmation (92 KB)
- `raw/assets/stripe-klarna-link-select-plan.png` — plan selection (150 KB)
- `raw/assets/stripe-klarna-link-pay.png` — confirm payment (129 KB)
- `raw/assets/stripe-klarna-link-returning-pay-later.png` — returning pay later (92 KB)
- `raw/assets/stripe-klarna-link-returning-confirm-info.png` — returning confirm (118 KB)
- `raw/assets/stripe-klarna-link-returning-success.png` — success page (63 KB)

## Related Pages

- [[stripe-link]] — Link concept page (Klarna on Link section)
- [[source-stripe-klarna]] — standard Klarna integration (non-Link)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-klarna-on-link-2025]] — verbatim webpage content (64 lines)
