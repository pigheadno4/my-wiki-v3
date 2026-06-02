---
title: "Stripe — Collect Payment Details Before Creating an Intent (Deferred)"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-accept-payment-deferred-2026.md"
tags: [stripe, payment-element, deferred-intent, payment-intent, setup-intent, elements, dynamic-update]
---

## Summary

Deferred intent pattern: render Payment Element with `mode`/`amount`/`currency` before creating a PaymentIntent or SetupIntent. Create PI server-side only when customer submits. Covers both payment and setup flows.

## Payment Mode Flow

1. `stripe.elements({ mode: 'payment', amount, currency })` — renders PM options
2. `elements.submit()` — validates form + triggers wallet collection (must call first)
3. Create PI on server → return `client_secret`
4. `stripe.confirmPayment({ elements, clientSecret, confirmParams: { return_url } })`

## Setup Mode Flow

Same as payment but:
- `mode: 'setup'`, no `amount` required
- Create SetupIntent on server
- `stripe.confirmSetup({ elements, clientSecret, confirmParams: { return_url } })`

## Key Features

- **Dynamic updates**: `elements.update({ amount: newAmount })` when amount changes (discount codes, etc.)
- **Saved PMs**: same CustomerSession pattern as two-step confirmation
- **Layouts**: accordion, tabs
- **Two-step alternative**: use ConfirmationToken for review page before confirming

## Limitations

- No BLIK, no ACSS
- No client-side `customer_balance` with dynamic PMs (create PI server-side instead)

## Related Pages

- [[stripe-payment-intents]] — concept page (updated with deferred intent pattern)
- [[source-stripe-two-step-confirmation]] — ConfirmationToken variant of this pattern

## Raw Sources

- [[stripe-accept-payment-deferred-2026]] — verbatim deferred intent guide (2490 lines)
