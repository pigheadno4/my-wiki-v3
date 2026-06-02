---
title: "Stripe Subscriptions — Set Up Pix Subscription"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-pix-2026.md"
tags: [stripe, billing, subscriptions, pix, pix-automatico, brazil, brl, mandate, qr-code, setup-intents]
---

## Summary

Integration guide for Pix subscriptions (Brazil only, BRL). Uses Pix Automático — a mandate-based recurring payment system. Three integration paths: Checkout, SetupIntents, Subscriptions API. Key specifics: mandate options required, tax_id (CPF/CNPJ) required from customer, mandate revocation via banking app triggers `mandate.updated`.

## Pix Automático concept

Pix subscriptions use Pix Automático — customer authorizes a mandate in their banking app once, then future charges happen automatically. Requires `mandate_options.amount` and `payment_schedule` in `payment_method_options.pix`.

**`mandate_options.amount` tip**: can be set higher than subscription price to allow future upgrades without requiring re-authorization.

## Three integration paths

### Path 1: Checkout

```js
stripe.checkout.sessions.create({
  payment_method_types: ['pix'],
  payment_method_options: {
    pix: { mandate_options: { amount: 2000, payment_schedule: 'monthly' } }
  },
  line_items: [{ price: priceId, quantity: 1 }],
  mode: 'subscription',
  success_url: '...'
})
```

Customer authorizes mandate in banking app → subscription activates automatically.

### Path 2: SetupIntents

1. Create SetupIntent with `payment_method_types=['pix']` + mandate options
2. `stripe.confirmPixSetup(clientSecret, { payment_method: { billing_details: { name, email, tax_id } }, return_url })`
3. Customer scans QR in banking app → SetupIntent `succeeded`
4. Create subscription with `default_payment_method` from SetupIntent PM

### Path 3: Subscriptions API

1. Create subscription: `default_incomplete` + `save_default_payment_method='on_subscription'` + `payment_method_options.pix.mandate_options`
2. Display QR via `stripe.confirmPix()` (or use `handleActions: false` for manual QR display)
3. Customer scans → subscription activates

## Required customer fields

| Field | Value |
|---|---|
| `name` | Full name of account holder |
| `email` | Email address |
| `tax_id` | CPF (individual) or CNPJ (business) — required by Brazilian government |

## Manual QR code display

Use `handleActions: false` in `confirmPixSetup` to get `next_action.pix_display_qr_code`:
- `data` — EMV string ("copy and paste")
- `image_url_svg` / `image_url_png` — QR code images
- `expires_at` — Unix timestamp
- `hosted_instructions_url` — Stripe-hosted page

## Mandate revocation

Customer can revoke in banking app → `mandate.updated` event → bring customer back on-session to create new mandate.

## Testing

- Tax identifier: `000.000.000-00` (CPF/CNPJ)
- "Simulate scan" button in sandbox → Stripe-hosted test approval page
- Email-based test scenarios (6 variants):
  - `expire_immediately@test.com` — expires immediately, no mandate
  - `expire_with_delay@test.com` — expires after 3 min, no mandate
  - `succeed_mandate_expire_payments_immediately@test.com` — mandate created, recurring payments expire immediately
  - `succeed_mandate_expire_payments_with_delay@test.com` — mandate created, recurring payments expire after 3 min
  - `succeed_immediately@test.com` — mandate + payments succeed immediately
  - `anything@test.com` (default) — mandate + payments succeed after 3 min

## Related pages

- [[stripe-pix]] — concept page
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-pix-2026]] — verbatim Stripe docs webpage (1059 lines)
