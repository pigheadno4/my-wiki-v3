---
title: "Stripe: Accept a TWINT Payment"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-twint-accept-payment-2025.md"
tags: [stripe, twint, switzerland, chf, checkout, direct-api]
---

## Summary

Integration guide for accepting TWINT payments via Checkout and Direct API (legacy). Checkout path is straightforward; Direct API uses `stripe.confirmTwintPayment()` with redirect.

## Key Details

### Checkout path

- `payment_method_types: ['twint']`, `chf` only, payment mode only (no setup/subscription)
- Select 'TWINT' and click Pay to test; no special test numbers

### Direct API path (Legacy)

- `stripe.confirmTwintPayment(clientSecret, { payment_method: { billing_details: { name, email } }, return_url })`
- Returns redirect URL → customer authorizes on TWINT page
- Test: "Authorize test payment" / "Fail test payment" on redirect page

### Optional server-side redirect

- `paymentIntents.create({ payment_method_types: ['twint'], confirm: true, payment_method_data: { type: 'twint' }, return_url })`
- Returns `requires_action` + `redirect_to_url` next_action

## Raw Sources

- [[stripe-twint-accept-payment-2025]] — verbatim webpage content (369 lines, Checkout + Direct API legacy)
