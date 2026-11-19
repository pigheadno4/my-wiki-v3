---
title: "Stripe — Build Two-Step Confirmation"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-two-step-confirmation-2026.md"
tags: [stripe, payment-element, confirmation-token, two-step, review-page, tax, customer-session, elements]
---

## Summary

Two-step checkout flow using ConfirmationToken: collect payment details → create ConfirmationToken → show review/validate/calculate tax → create PaymentIntent → confirm with token.

## Flow

1. Payment Element collects details (deferred intent — no PI yet)
2. `stripe.createConfirmationToken({ elements, params })` → get token
3. Send token ID to server; inspect `payment_method_preview` for review page
4. (Optional) Calculate tax using billing address from ConfirmationToken
5. Create PaymentIntent on server (link tax calculation via `hooks.inputs.tax`)
6. `stripe.confirmPayment({ clientSecret, confirmParams: { confirmation_token: id } })`

## Key API Points

- **Elements options**: `mode`, `currency`, `amount`, `setupFutureUsage`, `captureMethod`, `onBehalfOf`, `paymentMethodTypes`, `paymentMethodConfiguration`, `paymentMethodCreation`, `paymentMethodOptions` — **must match PI params exactly**
- **Saved PMs**: `CustomerSession` with `payment_method_redisplay/save/save_usage/remove` features; pass `customerSessionClientSecret` to `stripe.elements()`
- **CVC re-collection**: `require_cvc_recollection` on both PI creation and Elements creation
- **Change event**: `paymentElement.on('change', e => e.value.payment_method)` — detect saved PM selection

## Limitations

- No BLIK, no ACSS direct debits
- No client-side `customer_balance` with dynamic PMs (create PI server-side)

## Layouts

`accordion` (default), `tabs`. Pass via `elements.create('payment', { layout: { type: '...' } })`.

## Related Pages

- [[stripe-payment-intents]] — concept page (updated with two-step confirmation)
- [[source-stripe-payments-existing-customers]] — existing customer saved PM display

## Raw Sources

- [[stripe-two-step-confirmation-2026]] — verbatim two-step confirmation guide (906 lines, 4 screenshots)
