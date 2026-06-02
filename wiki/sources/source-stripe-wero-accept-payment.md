---
title: "Stripe: Accept a Payment with Wero"
type: source
date_ingested: 2026-05-05
original_format: webpage
raw_files:
  - "stripe-wero-accept-payment-2025.md"
tags: [stripe, wero, germany, eur, bank-redirect, checkout, elements, payment-intents]
---

## Summary

Integration guide for Wero across three paths: Checkout, Elements (Payment Element), and Direct API (`stripe.confirmWeroPayment`). Also covers a server-side manual redirect path. Includes error codes and failed payment handling.

## Key Details

### Checkout path

- `payment_method_types: ['wero']`, `currency: 'eur'`, `mode: 'payment'` only
- Listen for `checkout.session.completed` to fulfill orders
- Sandbox: redirected to test page to approve/decline

### Elements path

- Standard `stripe.confirmPayment()` with Payment Element + `return_url`
- Return URL receives `payment_intent` + `payment_intent_client_secret` query params

### Direct API path

- `stripe.confirmWeroPayment(clientSecret, { payment_method: { billing_details: { name, email } }, return_url })`
- Server-side manual: create PaymentMethod (`type=wero`, billing_details) → confirm PI → `requires_action` + `next_action.redirect_to_url`
- Return URL params: `payment_intent`, `payment_intent_client_secret`, `redirect_pm_type`, `redirect_status`

### Auth + failure behavior

- Authentication session expires after **1 hour** → PI reverts to `requires_payment_method`
- On decline or timeout: prompt customer to retry with different payment method; always offer `card` as fallback

### Error codes

| Code | Meaning |
| --- | --- |
| `payment_intent_invalid_currency` | Must use EUR |
| `payment_method_customer_decline` | Customer cancelled |
| `payment_intent_payment_attempt_failed` | Generic failure — check error message |
| `payment_intent_redirect_confirmation_without_return_url` | `return_url` required |

## Raw Sources

- [[stripe-wero-accept-payment-2025]] — verbatim webpage content (899 lines, Checkout + Elements + Direct API + error codes)
