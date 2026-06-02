---
title: "Stripe Docs — Accept a payment using local cards in Nigeria"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-ng-card-accept-payment-2025.md"
tags: [stripe, nigeria, naira, ng-card, local-payment-methods, merchant-of-record, payment-intents, checkout, recurring]
---

## Summary

Integration guide for Naira card (`ng_card`) covering Checkout and Direct API paths. Uses Stripe's MoR partner redirect flow. Key differentiator from Naira bank transfer: supports setup and subscription mode (recurring).

## Key Facts

- **PM type**: `ng_card`
- **Currency**: NGN only; **business locations**: US only
- **Amount limits**: 500–100,000,000 NGN
- **Modes**: payment ✓, setup ✓, subscription ✓ (recurring supported — unlike bank transfer)

## Integration Paths

### Checkout

- Add `ng_card` to `payment_method_types`
- All `line_items` must use `ngn` currency
- Testing: select "Naira payment methods" and click Pay

### Direct API

1. Create PaymentIntent with `payment_method_types: ['ng_card']` **and** `payment_method_data: { type: 'ng_card' }` at creation time
2. Pass `client_secret` to client
3. Call `stripe.confirmPayment()` with `payment_method_data.type: 'ng_card'` + `return_url`
4. Customer redirected to MoR partner checkout; on return, `return_url` receives `payment_intent` + `payment_intent_client_secret` query params
5. Testing: success → `requires_action` → `succeeded`; fail → click "Fail test payment" → `requires_payment_method`
6. Post-payment: `payment_intent.succeeded` webhook

## Related Pages

- [[stripe-nigeria-payment-methods]] — Nigeria payment methods concept page
- [[source-stripe-nigeria-payment-methods]] — Nigeria overview (properties, disputes, refunds, VAT)
- [[source-stripe-ng-bank-transfer-accept-payment]] — Naira bank transfer integration (payment mode only)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-ng-card-accept-payment-2025]] — verbatim webpage content
