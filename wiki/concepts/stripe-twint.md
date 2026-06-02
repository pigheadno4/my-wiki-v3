---
title: "TWINT (Stripe)"
type: concept
category: technology
tags: [stripe, twint, switzerland, chf, bank-redirect, recurring, disputes, connect]
---

## Definition

TWINT is Switzerland's dominant mobile payment method. Customers authenticate via a TWINT app — either by mobile redirect or by scanning a desktop QR code. API enum: `twint`. Customer-initiated, immediate notification.

**Currency**: CHF only. **Customers**: Switzerland only. **Business**: 36 countries (European focus). **Max**: 5,000 CHF per transaction.

## Two Payment Flows

1. **Mobile**: customer redirected from site/app → TWINT app → authorizes → returns
2. **Desktop**: QR code displayed on website → customer scans with TWINT app → authorizes

## Key Properties

- **Recurring**: Yes — notable for a bank redirect method
- **Disputes**: Yes — rare (25–50 per 1,000,000 transactions); filed via customer's bank
- **Refunds**: 180 days; full and partial; multiple partial refunds allowed
- **ECE**: not supported; all other products (Checkout, Elements, Payment Links, Subscriptions, Invoicing, Connect) supported

## Onboarding Requirements

Must comply *before* requesting access or capability stays `pending`:

- Functional public website (not password-protected)
- Legal notice/T&C displaying: company name/legal form, full address, contact (email or phone)
- CHF prices displayed; Switzerland as shipping destination for physical goods
- TWINT can **suspend or terminate** access for non-compliance

## Connect

`twint_payments` capability required. Direct, Destination, and Separate charges all supported. Connected account name appears in TWINT app.

## Integration

**Checkout (one-time payment)**: `payment_method_types: ['twint']`, `chf`, payment mode only.

**Checkout (setup mode)**: `mode: "setup"`, `payment_method_types: ['twint']` — saves mandate with no payment upfront.

**Elements**: `stripe.confirmSetup()` (setup mode) or `stripe.confirmPayment()` with `setup_future_usage` (payment mode).

**Direct API**: `stripe.confirmTwintPayment()` (payment) or `stripe.confirmTwintSetup()` (setup) → redirect. Server-side confirm requires `mandate_data.customer_acceptance.online` (ip_address + user_agent).

**return_url**: not required when reusing a previously saved TWINT method.

## Sources

- [[source-stripe-twint]] — primary source: payment flows, onboarding requirements, disputes, refunds, Connect
- [[source-stripe-twint-accept-payment]] — integration guide: Checkout + Direct API legacy, confirmTwintPayment, redirect flow
- [[source-stripe-twint-save-during-payment]] — save during payment: setup_future_usage, off-session charging, return_url not required for saved method
- [[source-stripe-twint-set-up-future-payments]] — setup-only (no payment): SetupIntent via Checkout/Elements/Direct API, confirmTwintSetup, mandate_data
- [[source-stripe-subscriptions-twint]] — subscription guide: 3 paths (Checkout/SetupIntents/Subscriptions API), CHF only, mandate_data+return_url required, QR via redirect
