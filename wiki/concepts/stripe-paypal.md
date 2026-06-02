---
title: "Stripe PayPal Integration"
type: concept
category: framework
tags: [stripe, paypal, subscriptions, payment-methods, setup-intents, mandate, billing-agreement, checkout]
---

## Overview

Stripe supports PayPal as a payment method for one-time payments and subscriptions. Customers authenticate via PayPal redirect and authorize a billing agreement for recurring charges. Two integration paths: Checkout (recommended) and Direct API (SetupIntents).

> Note: This page covers Stripe's PayPal integration, not PayPal's own native Subscriptions API (see [[paypal-subscriptions]] for that).

## Prerequisites

- Activate PayPal in Stripe Dashboard
- **Recurring payments**: Stripe auto-enables for most users on activation. May need manual enable in Dashboard due to PayPal regional policies.
- **Direct API**: must explicitly enable recurring payments; only available in specific business locations

## Subscription paths

### 1. Checkout (recommended)

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
5. Create subscription with `default_payment_method` + **`off_session=true`**

## Critical: `off_session=true`

**Required** on all subscription creates and updates via Direct API. Without it, any payment requiring action triggers another redirect to PayPal.

## Mandate (billing agreement)

After setup, the Mandate object contains:
- `payer_email` — buyer's PayPal email
- `payer_id` — unique PayPal payer ID  
- `billing_agreement_id` — PayPal BAID

## Webhook events

| Event | Meaning |
|---|---|
| `setup_intent.succeeded` | Billing agreement authorized |
| `setup_intent.setup_failed` | Authorization failed |
| `mandate.updated` | Customer revoked from PayPal side |

## Removing PayPal PM

`paymentMethods.detach(pmId)` — revokes Stripe mandate AND cancels PayPal billing agreement via PayPal API.

## Sources

- [[source-stripe-subscriptions-paypal]] — Stripe docs: PayPal subscription guide (Checkout + Direct API, billing agreement, off_session requirement)
