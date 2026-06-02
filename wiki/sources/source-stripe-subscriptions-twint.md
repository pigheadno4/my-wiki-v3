---
title: "Stripe Subscriptions — Set Up TWINT Subscription"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-twint-2026.md"
tags: [stripe, billing, subscriptions, twint, switzerland, chf, checkout, setup-intents, mandate, qr-code]
---

## Summary

Integration guide for TWINT subscriptions (Switzerland, CHF). Three paths: Checkout, SetupIntents, Subscriptions API. TWINT uses QR code via hosted page redirect (`next_action.redirect_to_url.url`), not client-side QR rendering. Same 3-path structure as Amazon Pay / Cash App Pay / Revolut Pay.

## Three integration paths

### Path 1: Checkout

`payment_method_types=['card','twint']`, `mode='subscription'`. Test: authorize mandate → `succeeded`; decline → `requires_payment_method`.

### Path 2: SetupIntents

SetupIntent: `payment_method_data.type='twint'`, `confirm=true`, `usage=off_session`, `mandate_data`, `return_url` → `requires_action` → redirect to `next_action.redirect_to_url.url` (TWINT-hosted QR page) → `succeeded` → create subscription with `default_payment_method`.

### Path 3: Subscriptions API

Create subscription: `default_incomplete` + `save_default_payment_method='on_subscription'` → confirm PaymentIntent: `payment_method_data[type]=twint` + `mandate_data` + `return_url` → `requires_action` → TWINT QR page → `succeeded` → activates.

## Key requirements

- **CHF only** (Switzerland)
- `mandate_data` required
- `return_url` required
- QR code displayed via `next_action.redirect_to_url.url` (Stripe-hosted TWINT page)

## Related pages

- [[stripe-twint]] — concept page (updated)
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-twint-2026]] — verbatim Stripe docs webpage
