---
title: "Stripe Subscriptions — Set Up Klarna Subscription"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-klarna-2026.md"
tags: [stripe, billing, subscriptions, klarna, bnpl, checkout, payment-element, mandate]
---

## Summary

Integration guide for Klarna subscriptions. Two paths: Checkout (recommended) and Payment Element (custom UI). Notable for 23-country test data matrix and cookie-based session tracking in sandbox. Payment options vary by country.

## Two integration paths

### Path 1: Checkout (recommended)

Standard `checkout.sessions.create` with `mode='subscription'`. Enable Klarna from Dashboard — no `payment_method_types` override needed. Retrieve subscription via `checkout.session.completed` webhook or success URL `stripe.checkout.sessions.retrieve(sessionId, { expand: ['subscription'] })`.

Trial support: `subscription_data.trial_period_days` or `trial_end`.

### Path 2: Payment Element (advanced)

1. Server: Create subscription with `payment_behavior=default_incomplete`, `save_default_payment_method='on_subscription'`; expand `latest_invoice.confirmation_secret`
2. Client: Mount Payment Element with `clientSecret`; `stripe.confirmPayment({ elements, confirmParams: { return_url, mandate_data } })`
3. Klarna redirects customer to its own flow; on return, check PaymentIntent status

## Key Klarna characteristics

- **Payment options vary by country** — check Klarna's supported payment options before integrating
- **BNPL / redirect-based**: Klarna redirects customer to complete payment selection and authorization
- **23 supported countries**: AU, AT, BE, CA, CZ, DK, FI, FR, DE, GR, IE, IT, NL, NZ, NO, PL, PT, RO, ES, SE, CH, UK, US

## Testing

- **Cookie-based session tracking**: must log out of Klarna sandbox between different country tests
- **Approval/denial by email**: `customer@email.{country}` = approve; `customer+denied@email.{country}` = deny
- **Two-step auth**: any 6-digit code passes; `999999` fails
- **Repayment methods available in test flow**: Direct Debit (IBAN), Bank transfer (Demo Bank), Credit Card (`4111 1111 1111 1111`), Debit Card (`4012 8888 8888 1881`)

Per-country test data (name, address, DOB, phone) in raw file: [[stripe-subscriptions-klarna-2026]].

## Related pages

- [[stripe-klarna]] — concept page
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-klarna-2026]] — verbatim Stripe docs webpage (1038 lines, 23-country test data)
