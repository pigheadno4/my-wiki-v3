---
title: "Stripe Docs — Accept a payment using local cards in South Korea"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-kr-card-accept-payment-2025.md"
tags: [stripe, south-korea, krw, kr-card, local-payment-methods, nicepay, payment-intents, checkout]
---

## Summary

Integration guide for South Korean local cards (`kr_card`) via Stripe's local processor partner (NICEPAY). Covers Checkout and Direct API paths.

## Key Facts

- **PM type**: `kr_card`
- **Currency**: KRW only; **28 merchant countries**
- **Minimum**: 100 KRW
- **Modes**: payment ✓, setup ✓, subscription ✓

## NICEPAY Disclosure (Required)

Must display on the checkout page before payment:

> "After submission, you're redirected to complete next steps. This transaction is processed through NICEPAY in accordance with NICEPAY's [terms of use](https://start.nicepay.co.kr/homepage/terms/bill.do)."

## Integration Paths

### Checkout

- Add `kr_card` to `payment_method_types`; all line items in `krw`
- Testing: select "Local cards" → Stripe-hosted redirect page → authorize or fail

### Direct API

1. Create PaymentIntent: `payment_method_types: ['kr_card']` + `payment_method_data: { type: 'kr_card' }`
2. Client: `stripe.confirmPayment()` with `payment_method_data.type: 'kr_card'` + `return_url`
3. Customer selects issuer and authenticates on NICEPAY checkout page
4. `return_url` receives `payment_intent` + `payment_intent_client_secret`
5. Post-payment: `payment_intent.succeeded` webhook

## CDN Assets

- `raw/assets/stripe-kr-card-payment-flow.mov` — payment flow demo video (4.8 MB)

## Related Pages

- [[stripe-korea-payment-methods]] — South Korea payment methods concept page
- [[source-stripe-korea-payment-methods]] — South Korea overview (all methods, installments, disputes, refunds)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-kr-card-accept-payment-2025]] — verbatim webpage content
