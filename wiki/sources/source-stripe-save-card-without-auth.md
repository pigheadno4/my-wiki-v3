---
title: "Stripe — Save a Card Without Bank Authentication"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-save-card-without-auth-2026.md"
tags: [stripe, saved-payment-methods, legacy, us-canada, error-on-requires-action, card-element, customer, setup-future-usage]
---

## Summary

Legacy US/CA-only pattern for saving cards and charging later. Non-compliant in India and other countries requiring auth for card saving. Uses `error_on_requires_action: true`.

## Flow

1. Client: `elements.create('card')` → `stripe.createPaymentMethod()` → send PM ID to server
2. Server: `stripe.customers.create({ payment_method })` OR `stripe.paymentMethods.attach(pm_id, { customer })`
3. Later: `stripe.paymentIntents.create({ customer, payment_method, error_on_requires_action: true, confirm: true })`

## Key Options

- **`setup_future_usage: 'on_session'`**: save + charge in one call without triggering unnecessary auth
- **CVC re-collection**: use `cardCvc` Element + `stripe.confirmCardPayment({ payment_method_options: { card: { cvc: cardCvcElement } } })`; configure Radar to block on failed CVC

## Compliance

Must display terms about future charges and get written customer agreement. Keep records.

## Limitations

- Non-compliant in countries requiring auth for saving cards (India etc.)
- Fails any payment requiring 2FA

## Related Pages

- [[stripe-saved-payment-methods]] — concept page
- [[source-stripe-payments-without-auth]] — companion guide (payments without auth)

## Raw Sources

- [[stripe-save-card-without-auth-2026]] — verbatim save card without auth guide (260 lines)
