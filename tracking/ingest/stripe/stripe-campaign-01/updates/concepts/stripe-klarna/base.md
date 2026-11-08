---
title: "Stripe Klarna"
type: concept
category: framework
tags: [stripe, klarna, bnpl, subscriptions, payment-methods, checkout, payment-element, mandate, 23-countries]
---

## Overview

Klarna is a Buy Now Pay Later (BNPL) payment method available on Stripe across 23 countries. Customers authenticate and select repayment options (Pay Now, Pay Later, Pay in installments) via a Klarna-hosted redirect. Supports subscriptions.

**Important**: Payment options available to customers vary by use case and buyer country — check Klarna's supported options before integrating.

## Supported countries (23)

AU, AT, BE, CA, CZ, DK, FI, FR, DE, GR, IE, IT, NL, NZ, NO, PL, PT, RO, ES, SE, CH, UK, US

## Subscription integration

Stripe recommends **Checkout** for Klarna subscriptions.

### Checkout (recommended)

Enable Klarna from Dashboard payment methods settings. Create Checkout Session with `mode='subscription'`. Retrieve subscription via `checkout.session.completed` webhook or by expanding the session.

Supports trial periods via `subscription_data.trial_period_days` or `trial_end`.

### Payment Element (advanced)

Create subscription with `payment_behavior=default_incomplete` + `save_default_payment_method='on_subscription'` → mount Payment Element → `stripe.confirmPayment({ return_url, mandate_data })` → Klarna redirects customer → on return check PaymentIntent status.

## Testing

- **Cookie-based**: log out of Klarna sandbox between different country test sessions
- **Email controls outcome**: `customer@email.{country}` = approve; `customer+denied@email.{country}` = deny
- **Two-step auth**: any 6-digit code passes; `999999` = fail
- **Repayment options in test flow**: Direct Debit, Bank transfer, Credit/Debit cards

Full per-country test data (name, DOB, address, phone for 23 countries) in [[source-stripe-subscriptions-klarna]].

## Sources

- [[source-stripe-subscriptions-klarna]] — Stripe docs: Klarna subscription integration guide (Checkout + Payment Element, 23-country test data)
