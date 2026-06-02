---
title: "Stripe: Save BLIK Details During a Payment"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-blik-save-during-payment-2025.md"
tags: [stripe, blik, poland, pln, recurring, setup-intents, mandates, off-session]
---

## Summary

Guide for saving BLIK payment method during a payment for future recurring off-session use. Covers Checkout, Elements, and Direct API paths. Key: customer approves both payment and mandate authorization in banking app simultaneously. Not all Polish banks support BLIK recurring.

## Key Details

### Critical constraints

- **Not all banks support recurring**: fails with `recurring_not_supported_by_bank` if unsupported
- **Max off-session amount**: 2000 PLN per payment
- **Currency**: PLN only

### Checkout path

- `payment_intent_data.setup_future_usage: 'off_session'` on Checkout Session
- Reusable PaymentMethod attached to Customer after session

### Elements path

- `setup_future_usage: 'off_session'` on PaymentIntent
- `stripe.confirmPayment()` with `return_url`
- After confirm: `requires_action` with `blik_authorize` next_action; customer has 60s to approve payment + mandate

### Direct API path

- Requires `mandate_data.customer_acceptance.online` with `ip_address` + `user_agent`
- Pass BLIK code in `payment_method_options.blik.code` with `confirm: true`

### Off-session charging

- `off_session: true`, `confirm: true` on new PaymentIntent
- Bank validates against original mandate terms; `blik_authorize` next_action

### Additional sandbox failure patterns (recurring-specific)

- **Immediate**: `.*recurring_not_supported@.*`
- **8s delay**: `.*alias_declined@.*`
- **60s delay** (mandate setup timeout): `.*setup_timeout@.*`
- **6min delay** (lifecycle): `.*alias_unregistered@.*`, `.*alias_expired@.*`
- **Off-session failure**: `.*recurring_declined@.*`

## Raw Sources

- [[stripe-blik-save-during-payment-2025]] — verbatim webpage content (886 lines, Checkout + Elements + Direct API sections)
