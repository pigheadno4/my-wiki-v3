---
title: "Stripe: Set Up Future BLIK Recurring Payments"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-blik-set-up-payment-2025.md"
tags: [stripe, blik, poland, pln, recurring, setup-intents, mandates, off-session]
---

## Summary

Guide for saving BLIK payment method via SetupIntent **without an initial payment**. Key difference from save-during-payment: no charge, customer only authorizes mandate. Covers Checkout (setup mode), Elements (`stripe.confirmSetup()`), and Direct API (`mandate_data` with `ip_address`/`user_agent` required).

## Key Details

### Checkout setup mode

- `mode: 'setup'`, `payment_method_types: ['blik']`
- Customer enters BLIK code and approves mandate in banking app

### Elements path

- `setupIntents.create({ usage: 'off_session' })` → `stripe.confirmSetup({ elements, confirmParams: { return_url } })`
- After confirm: `requires_action` with `blik_authorize` next_action; customer has 60s to approve

### Direct API path

- `setupIntents.create({ confirm: true, mandate_data: { customer_acceptance: { type: 'online', online: { ip_address, user_agent } } } })`
- Webhooks: `setup_intent.succeeded`, `setup_intent.setup_failed`, `mandate.updated`

### Key distinction from save-during-payment

- This guide: **SetupIntent only** — no initial charge, mandate authorization only
- Save-during-payment: PaymentIntent — real payment + mandate simultaneously

### Same recurring constraints and test patterns as save-during-payment

- Max 2000 PLN per off-session payment; PLN only
- Same 6 recurring failure email patterns

## Raw Sources

- [[stripe-blik-set-up-payment-2025]] — verbatim webpage content (697 lines, Checkout + Elements + Direct API)
