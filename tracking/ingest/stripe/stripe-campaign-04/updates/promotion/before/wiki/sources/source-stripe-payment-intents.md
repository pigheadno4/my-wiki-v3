---
title: "Stripe PaymentIntents and SetupIntents Lifecycle"
type: source
date_ingested: 2026-04-19
original_format: webpage
raw_files:
  - "stripe-payment-setup-intents-2025.md"
  - "stripe-payment-intents-api-2025.md"
  - "stripe-payment-status-updates-2025.md"
  - "stripe-async-capture-2025.md"
  - "stripe-setup-intents-api-2025.md"
tags: [stripe, payment-intents, setup-intents, lifecycle, 3ds, checkout-sessions]
---

## Summary

Detailed lifecycle reference for Stripe PaymentIntents and SetupIntents. Both use the same state-machine pattern — PaymentIntent creates a charge, SetupIntent saves a payment method without charging.

## Key Takeaways

- **Stripe recommends Checkout Sessions over Payment Intents** for most integrations — Checkout Sessions covers the same use cases with less code; Adaptive Pricing only available with Checkout Sessions
- **PaymentIntent vs SetupIntent**: PaymentIntent = immediate charge; SetupIntent = save payment method, no charge; 3DS on SetupIntent creates a mandate for future charges
- **`requires_action`** status = 3DS authentication needed (not in the API tour summary)
- **`requires_capture`** status = authorize+capture flow; attempting capture moves to `processing` or `succeeded`
- **Cancel in `processing`**: only possible for ACH, ACSS, AU BECS, BACS, NZ BECS, SEPA — may fail due to limited cancellation window
- **Auto-cancel**: PaymentIntent auto-transitions to `canceled` if confirmed too many times
- **API version note**: before 2019-02-11, `requires_source` = `requires_payment_method`; `requires_source_action` = `requires_action`

## Full PaymentIntent Lifecycle

```
requires_payment_method
  → requires_confirmation (often skipped)
    → requires_action (if 3DS needed)
      → processing (async methods: bank debits; cards skip this)
        → succeeded
        → requires_payment_method (on failure — retry same PaymentIntent)
  → requires_capture (if authorize+capture flow)
    → processing / succeeded
  → canceled (manual or auto after too many confirmations)
```

## Full SetupIntent Lifecycle (parallel, no charge)

```
requires_payment_method
  → requires_confirmation (often skipped)
    → requires_action (if 3DS needed)
      → processing
        → succeeded (attach to Customer for future payments)
        → requires_payment_method (on failure)
  → canceled
```

## PaymentIntent vs SetupIntent

| | PaymentIntent | SetupIntent |
| --- | --- | --- |
| Creates charge | Yes | No |
| Purpose | Collect payment now | Save payment method for later |
| 3DS | Authenticates for this transaction | Authenticates + creates mandate for future charges |

## Checkout Sessions vs Payment Intents

Stripe recommends Checkout Sessions (`ui_mode: "elements"`) for most integrations:
- Uses `client_secret` to initialize checkout via `stripe.initCheckoutElementsSdk`
- React: import from `@stripe/react-stripe-js/checkout`; use `CheckoutElementsProvider`; confirm with `checkout.confirm`
- HTML: `checkout.createPaymentElement(); checkout.loadActions(); actions.confirm()`
- Adaptive Pricing only available with Checkout Sessions

## Cancel Rules

PaymentIntent can be canceled before `processing` or `succeeded`. Exception: can cancel in `processing` for ACH, ACSS, AU BECS, BACS, NZ BECS, SEPA (may fail). Canceling releases any held funds. Cannot be undone.

## Related Pages

- [[stripe]] — Stripe company page
- [[source-stripe-api-tour]] — Stripe API tour overview

## Raw Sources

- [[stripe-payment-setup-intents-2025]] — full PaymentIntent + SetupIntent lifecycle: all statuses, cancel rules, Checkout Sessions recommendation, API version notes
- [[stripe-setup-intents-api-2025]] — SetupIntents API: 3 use cases (car rental/crowdfunding/utilities); on-session = explicit checkbox consent; off-session = mandate required (permission/frequency/amount); allow_redisplay on PaymentMethod; MIT exemption from SCA for properly saved cards; usage=off_session (default) authenticates upfront for smoother later charges; build recovery process
- [[stripe-async-capture-2025]] — Asynchronous capture: capture_method=automatic_async (default in latest API); balance_transaction/transfer/application_fee null on Charge+webhooks initially; charge.updated SLA = 1hr; subscribe to charge.updated/application_fee.created/transfer.created for deferred data
- [[stripe-payment-status-updates-2025]] — Payment status monitoring: NEVER fulfill client-side (use webhooks); don't poll; verify webhooks with constructEvent; last_payment_error.message; 4 events (processing/succeeded/amount_capturable_updated/payment_failed); latest_charge; next_action for manual auth; Stripe CLI for local testing
- [[stripe-payment-intents-api-2025]] — PaymentIntents API implementation guide: client_secret (server-only, TLS required), 2 delivery patterns (SPA fetch vs SSR embed), setup_future_usage (on_session/off_session), statement_descriptor_suffix (cards, 22-char limit), metadata (order_id reconciliation, don't store PII), multiple Charges per PI on retry
