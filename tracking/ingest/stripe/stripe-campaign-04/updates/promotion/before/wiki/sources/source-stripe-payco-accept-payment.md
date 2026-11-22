---
title: "Stripe Docs — Accept a payment using PAYCO in South Korea"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-payco-accept-payment-2025.md"
tags: [stripe, south-korea, krw, payco, local-payment-methods, nicepay, payment-intents, checkout]
---

## Summary

Integration guide for PAYCO (`payco`) in South Korea via Stripe's local processor partner (NICEPAY). Payment mode only — no setup or subscription mode (no recurring). Simpler integration than Naver Pay (no funding source parameter, no buyer email required).

## Key Facts

- **PM type**: `payco`
- **Currency**: KRW only; **28 business locations** (all 28 including Singapore)
- **Minimum**: 100 KRW; stored value top-up max: 2,000,000 KRW (no max for card passthrough)
- **Modes**: payment only — setup ✗, subscription ✗ (no recurring)
- **No buyer email required**, no funding source parameter
- **NICEPAY disclosure required** — same text as all other KR methods

## Integration Paths

### Checkout

- Add `payco` to `payment_method_types`; all line items in `krw`
- Testing: select "PAYCO" → Stripe-hosted redirect page → authorize or fail

### Direct API

1. Create PaymentIntent: `payment_method_types: ['payco']` + `payment_method_data: { type: 'payco' }`
2. Client: `stripe.confirmPayment()` with `payment_method_data.type: 'payco'` + `return_url`
3. NICEPAY disclosure required on checkout page
4. Post-payment: `payment_intent.succeeded` webhook

## Related Pages

- [[stripe-korea-payment-methods]] — South Korea payment methods concept page
- [[source-stripe-korea-payment-methods]] — South Korea overview
- [[source-stripe-naver-pay-accept-payment]] — Naver Pay integration (has funding source + points)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-payco-accept-payment-2025]] — verbatim webpage content
