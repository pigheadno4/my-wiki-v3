---
title: "Stripe Docs — Accept a payment using Kakao Pay in South Korea"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-kakao-pay-accept-payment-2025.md"
tags: [stripe, south-korea, krw, kakao-pay, local-payment-methods, nicepay, payment-intents, checkout]
---

## Summary

Integration guide for Kakao Pay (`kakao_pay`) in South Korea via Stripe's local processor partner (NICEPAY). Covers Checkout and Direct API paths.

## Key Facts

- **PM type**: `kakao_pay`
- **Currency**: KRW only; **27 business locations** (all KR card countries except Singapore — Kakao Pay not available in SG)
- **Minimum**: 100 KRW; stored value top-up max: 2,000,000 KRW (no max for card passthrough)
- **Modes**: payment ✓, setup ✓, subscription ✓ (recurring supported)
- **Buyer email required**: must pass `billing_details.email` in `payment_method_data` at PaymentIntent creation
- **NICEPAY disclosure required** — same text as kr_card

## Integration Paths

### Checkout

- Add `kakao_pay` to `payment_method_types`; all line items in `krw`; provide buyer email
- Testing: select "Kakao Pay" → Stripe-hosted redirect page → authorize or fail

### Direct API

1. Create PaymentIntent: `payment_method_types: ['kakao_pay']` + `payment_method_data: { type: 'kakao_pay', billing_details: { email: '...' } }`
2. Client: `stripe.confirmPayment()` with `payment_method_data.type: 'kakao_pay'` + `return_url`
3. Customer redirected to NICEPAY/Kakao Pay checkout
4. `return_url` receives `payment_intent` + `payment_intent_client_secret`
5. Post-payment: `payment_intent.succeeded` webhook

## Related Pages

- [[stripe-korea-payment-methods]] — South Korea payment methods concept page
- [[source-stripe-korea-payment-methods]] — South Korea overview (all methods, installments, disputes)
- [[source-stripe-kr-card-accept-payment]] — KR card integration for comparison
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-kakao-pay-accept-payment-2025]] — verbatim webpage content
