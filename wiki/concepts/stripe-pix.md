---
title: "Stripe Pix (Brazil)"
type: concept
category: framework
tags: [stripe, pix, pix-automatico, brazil, brl, subscriptions, payment-methods, mandate, qr-code, setup-intents]
---

## Overview

Pix is Brazil's instant payment system. On Stripe, Pix subscriptions use **Pix Automático** — a customer-authorized mandate that enables automatic recurring charges without requiring customer action for each payment. Brazil only, BRL currency only.

## Pix Automático

Pix Automático is a mandate-based extension of Pix for recurring payments. The customer scans a QR code once in their banking app to authorize the mandate. All subsequent subscription charges happen automatically.

**Key fields**:
- `payment_method_options.pix.mandate_options.amount` — maximum amount that can be charged per period. Can be set higher than current price to allow future upgrades without re-authorization.
- `payment_method_options.pix.mandate_options.payment_schedule` — `monthly`, `weekly`, etc.

## Required customer fields

| Field | Requirement |
|---|---|
| `name` | Full name of account holder |
| `email` | Email address |
| `tax_id` | CPF (individual) or CNPJ (business) — required by Brazilian government |

## Subscription integration paths

### Checkout

```js
stripe.checkout.sessions.create({
  payment_method_types: ['pix'],
  payment_method_options: {
    pix: { mandate_options: { amount: 2000, payment_schedule: 'monthly' } }
  },
  mode: 'subscription', ...
})
```

### SetupIntents

SetupIntent → `stripe.confirmPixSetup(clientSecret, { payment_method: { billing_details: { name, email, tax_id } }, return_url })` → customer scans QR → `succeeded` → create subscription with `default_payment_method`.

### Subscriptions API

Create subscription with `default_incomplete` + mandate options → display QR → customer scans → activates.

## QR code display options

`stripe.confirmPixSetup` auto-handles QR display. Or use `handleActions: false` to get `next_action.pix_display_qr_code`:
- `data` — EMV string ("copy and paste")
- `image_url_svg` / `image_url_png` — QR code images
- `expires_at` — expiry timestamp
- `hosted_instructions_url` — Stripe-hosted page URL

## Mandate revocation

Customer can revoke in their banking app at any time → Stripe fires `mandate.updated` → bring customer back on-session to create a new mandate.

## Testing

- Tax ID: `000.000.000-00`
- In sandbox: "Simulate scan" → test approval/expiry page
- Email controls behavior: `succeed_immediately@test.com`, `expire_immediately@test.com`, etc. (6 email patterns)

## Sources

- [[source-stripe-subscriptions-pix]] — Stripe docs: Pix subscription guide (Checkout + SetupIntents + Subscriptions API, Pix Automático, 6 test email patterns)
