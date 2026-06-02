---
title: "Stripe Subscriptions — Set Up PayPal Subscription"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-paypal-2026.md"
tags: [stripe, billing, subscriptions, paypal, checkout, setup-intents, mandate, billing-agreement]
---

## Summary

Integration guide for PayPal subscriptions on Stripe. Two paths: Checkout (simple) and Direct API (SetupIntents + billing agreement). Key specifics: recurring payments may need manual Dashboard enable, `off_session=true` required on all updates, detaching PM cancels PayPal billing agreement.

## Important prerequisites

- Stripe auto-enables PayPal recurring payments for most users on activation. May need manual enable in Dashboard due to PayPal regional restrictions.
- Direct API path: must explicitly enable recurring payments in Dashboard; only available in specific business locations.

## Two integration paths

### Path 1: Checkout (Stripe-hosted)

```js
stripe.checkout.sessions.create({
  payment_method_types: ['paypal'],
  line_items: [{ price: priceId, quantity: 1 }],
  mode: 'subscription',
  success_url: '...'
})
```

- Buyer gets receipt from both Stripe and PayPal
- Supports: setup fee (one-time + recurring `line_items`), inline pricing, existing customer, prefill email, trials, fixed/dynamic tax rates, coupons, promo codes

### Path 2: Direct API (SetupIntents)

1. Create Customer/Account
2. Create SetupIntent: `payment_method_types=['paypal']`, `payment_method_data.type='paypal'`
3. Client: `stripe.confirmPayPalSetup(clientSecret, { return_url, mandate_data })` → redirect to PayPal billing agreement approval
4. Listen for `setup_intent.succeeded` webhook
5. Create subscription: `default_payment_method` from SetupIntent PM + **`off_session=true`**

## Critical: `off_session=true` required

**All subscription creates and updates** via Direct API require `off_session=true`. Without it, any new payment requires another user redirect to PayPal for re-confirmation.

## Mandate fields

After `setup_intent.succeeded`, the Mandate object contains:
- `payer_email` — buyer's PayPal email
- `payer_id` — unique PayPal payer ID
- `billing_agreement_id` — PayPal BAID (Billing Agreement ID)

## Webhook events (Direct API)

| Event | When |
|---|---|
| `setup_intent.succeeded` | Billing agreement authorized |
| `setup_intent.setup_failed` | Authorization failed; status → `requires_payment_method` |
| `mandate.updated` | Customer revokes billing agreement from PayPal |

## Removing a PayPal payment method

`paymentMethods.detach(id)` — revokes the Stripe mandate AND calls PayPal API to cancel the associated billing agreement.

## Optional features (both paths)

- `billing_cycle_anchor` — manual billing cycle start
- `trial_end` — free trial period; can combine with billing anchor

## Related pages

- [[stripe-paypal]] — concept page
- [[stripe-subscriptions]] — concept page
- [[paypal-subscriptions]] — PayPal-native Subscriptions API (distinct from Stripe's PayPal integration)
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-paypal-2026]] — verbatim Stripe docs webpage (994 lines, 1 image reused)
