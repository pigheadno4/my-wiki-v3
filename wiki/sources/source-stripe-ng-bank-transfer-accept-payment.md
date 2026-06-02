---
title: "Stripe Docs — Accept a payment through local bank transfers in Nigeria"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-ng-bank-transfer-accept-payment-2025.md"
tags: [stripe, nigeria, naira, bank-transfer, ng-bank-transfer, merchant-of-record, payment-intents, checkout]
---

## Summary

Integration guide for Naira bank transfer (`ng_bank_transfer`) covering Checkout and Direct API paths. Uses Stripe's MoR partner redirect flow.

## Key Facts

- **PM type**: `ng_bank_transfer`
- **Currency**: NGN only; **business locations**: US only
- **Amount limits**: 500–100,000,000 NGN
- **Modes**: payment only (no setup, no subscription)

## Integration Paths

### Checkout

- Add `ng_bank_transfer` to `payment_method_types`
- All `line_items` must use `ngn` currency
- Testing: select "Nigerian payment methods" and click Pay

### Direct API

1. Create PaymentIntent with `payment_method_types: ['ng_bank_transfer']` **and** `payment_method_data: { type: 'ng_bank_transfer' }` at creation time
2. Pass `client_secret` to client
3. Call `stripe.confirmPayment()` with `payment_method_data.type: 'ng_bank_transfer'` + `return_url`
4. Customer redirected to MoR partner checkout; on return, `return_url` receives `payment_intent` + `payment_intent_client_secret` query params
5. Testing: success → `requires_action` → `succeeded`; fail → click "Fail test payment" → `requires_payment_method`
6. Post-payment: `payment_intent.succeeded` webhook

## Related Pages

- [[stripe-nigeria-payment-methods]] — Nigeria payment methods concept page
- [[source-stripe-nigeria-payment-methods]] — Nigeria overview (properties, disputes, refunds, VAT)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-ng-bank-transfer-accept-payment-2025]] — verbatim webpage content
