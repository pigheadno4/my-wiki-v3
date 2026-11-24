---
title: "Stripe PayPal Integration"
type: concept
category: framework
tags: [stripe, paypal, subscriptions, payment-methods, setup-intents, mandate, billing-agreement, checkout]
---

## Overview

Stripe supports PayPal as a payment method for one-time payments and subscriptions. The May 2026 subscription guide documents two paths: Stripe-hosted Checkout and Direct API with a SetupIntent and PayPal billing-agreement approval. The November 2026 canonical capture is a variant index only; it does not establish a current path preference or account eligibility.

> Note: This page covers Stripe's PayPal integration, not PayPal's own native Subscriptions API (see [[paypal-subscriptions]] for that).

## Prerequisites

- **Stripe-hosted Checkout, May 2026 guide:** After PayPal activation in the Dashboard, Stripe said recurring payments were automatically enabled for most users, with possible manual enablement due to PayPal policy or regional restrictions.
- **Direct API, May 2026 guide:** The guide instructed merchants to enable recurring payments in the Dashboard and check supported business locations.
- The 2026-11-07 canonical capture is a variant index only; it does not verify current account enablement or business-location eligibility.

## Subscription paths

### 1. Stripe-hosted Checkout (May 2026 guide)

```js
stripe.checkout.sessions.create({
  payment_method_types: ['paypal'],
  line_items: [{ price: priceId, quantity: 1 }],
  mode: 'subscription',
  success_url: '...'
})
```

Supports: setup fee, inline pricing, existing customer, prefill email, trials, fixed/dynamic tax rates, coupons, promo codes. Buyer receives receipt from both Stripe and PayPal.

### 2. Direct API (SetupIntents)

1. Create Customer/Account
2. Create SetupIntent: `payment_method_types=['paypal']`
3. `stripe.confirmPayPalSetup(clientSecret, { return_url, mandate_data })` → PayPal billing agreement page
4. `setup_intent.succeeded` webhook fires
5. The May guide's main subscription-create examples use `default_payment_method` and `off_session: true`; confirm setup authorization separately from successful subscription payment.

## `off_session` in the May 2026 guide

The guide instructs `off_session=true` for subscription updates to avoid another PayPal redirect for a new payment. Its main initial-create examples include the flag, but its optional billing-anchor and trial create snippets omit it. [[source-stripe-subscriptions-paypal]] gives the dated example and object boundaries.

> [!warning] Contradiction
> The May main create examples include `off_session: true`, while optional create examples omit it and `default_payment_method`. The captured guide does not establish an unconditional rule for every create; the November variant index supplies no contract text to resolve this.

## Mandate (billing agreement)

The May guide locates payer ID and Billing Agreement ID on the resulting Mandate under `payment_method_details`, and buyer email plus payer ID on `PaymentMethod.paypal`. Its field table does not assign all three fields to the Mandate; see [[source-stripe-subscriptions-paypal]].

## Webhook events

| Event | Meaning |
|---|---|
| `setup_intent.succeeded` | Billing agreement authorized |
| `setup_intent.setup_failed` | Authorization failed |
| `mandate.updated` | Customer revoked from PayPal side |

## Removing PayPal PM

The May 2026 guide says detaching a saved PayPal PaymentMethod revokes its Stripe Mandate and calls PayPal to cancel the associated billing agreement. The November variant index does not reverify this consequence for a current account; see [[source-stripe-subscriptions-paypal]].

## Sources

- [[source-stripe-subscriptions-paypal]] — May 2026 Stripe PayPal subscription guide (Stripe-hosted Checkout + Direct API); November 2026 canonical capture links variant routes only
