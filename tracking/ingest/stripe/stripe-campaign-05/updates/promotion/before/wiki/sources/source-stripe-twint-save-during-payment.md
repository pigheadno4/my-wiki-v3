---
title: "Stripe: Save Payment Details During a TWINT Payment"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-twint-save-during-payment-2025.md"
tags: [stripe, twint, switzerland, chf, recurring, setup-intents, save-payment-method]
---

## Summary

Guide for saving TWINT payment method during a payment for future off-session use. Covers Checkout, Elements, and Direct API. Same pattern as Bancontact/iDEAL: payment + mandate simultaneously.

## Key Details

### Checkout path

- `payment_intent_data.setup_future_usage: 'off_session'` + `payment_method_types: ['twint']`, `chf`
- After: retrieve PaymentIntent from webhook or success URL → get `payment_method` ID

### Elements path

- `setup_future_usage: 'off_session'` on PaymentIntent + `stripe.confirmPayment()` with `return_url`
- Monitor `payment_intent.succeeded` webhook → store `payment_method` ID

### Direct API path

- `payment_method_data.type: 'twint'` + `setup_future_usage: 'off_session'`
- Server-side confirm: requires `mandate_data.customer_acceptance.online` with `ip_address`+`user_agent`

### Off-session charging

- `off_session: true`, `confirm: true` on PaymentIntent with saved `payment_method` ID
- `return_url` **not required** when reusing a previously saved TWINT method

## Raw Sources

- [[stripe-twint-save-during-payment-2025]] — verbatim webpage content (1222 lines, Checkout + Elements + Direct API)
