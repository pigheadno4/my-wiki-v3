---
title: "Stripe — Prebuilt Subscription Page with Checkout (Quickstart)"
type: source
date_ingested: 2026-05-12
original_format: notes
raw_files:
  - "stripe-checkout-subscriptions-quickstart-2026.md"
tags: [stripe, subscriptions, checkout, billing, quickstart, entitlements, customer-portal, trial, automatic-tax]
---

## Summary

Full Checkout-based subscription quickstart. React client + Node.js/Express server. Covers product/price setup, Checkout Session creation (lookup_key pattern), customer portal, webhook fulfillment, and optional trial/billing-anchor/auto-tax.

## Key Implementation Pattern

**Server**: `stripe.prices.list({ lookup_keys: [lookup_key] })` → `stripe.checkout.sessions.create({ mode: 'subscription', line_items, success_url with {CHECKOUT_SESSION_ID} })` → redirect to `session.url`

**Customer portal**: retrieve `checkoutSession` to get `customer` → create portal session → redirect

**Webhook events** (5):
- `customer.subscription.trial_will_end`
- `customer.subscription.deleted`
- `customer.subscription.created`
- `customer.subscription.updated`
- `entitlements.active_entitlement_summary.updated`

## Optional Parameters

- `subscription_data.trial_period_days` (min 1); for free trials: `trial_settings[end_behavior][missing_payment_method]=pause|cancel`
- `subscription_data.billing_cycle_anchor` (Unix timestamp)
- `automatic_tax: { enabled: true }` (requires Stripe Tax activated in Dashboard)

## Test Cards

- Success: `4242 4242 4242 4242`
- 3DS: `4000 0025 0000 3155`
- Declined: `4000 0000 0000 9995`

## Related Pages

- [[stripe-subscriptions]] — concept page
- [[source-stripe-subscriptions-overview]] — lifecycle/status guide

## Raw Sources

- [[stripe-checkout-subscriptions-quickstart-2026]] — formatted from quickstart UI (React + Node.js)
