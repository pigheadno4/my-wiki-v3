---
title: "Stripe Cash App Pay"
type: concept
category: framework
tags: [stripe, cash-app-pay, subscriptions, payment-methods, setup-intents, mandate, qr-code, us-only]
---

## Overview

Cash App Pay is a US-only mobile wallet payment method on Stripe. Customers authenticate by scanning a QR code with the Cash App app (desktop) or being redirected to Cash App (mobile). Supports one-time payments and recurring subscriptions.

## Key characteristics

- **US only** — USD only
- **QR code or redirect**: desktop shows QR; mobile redirects to Cash App
- **Mandate required**: must collect `mandate_data` for recurring use
- `return_url` required — Cash App redirects here after authentication
- `next_action.cashapp_handle_redirect_or_display_qr_code` used to handle the auth step
- `usage='off_session'` for recurring charges without customer present

## Subscription integration paths

Three approaches (same structure as Amazon Pay):

### 1. SetupIntents API (pre-authorize)

1. Create SetupIntent: `confirm=true`, `usage='off_session'`, `payment_method_types=['cashapp']`, `mandate_data`, `return_url`
2. Status → `requires_action` → redirect/QR for Cash App authentication
3. SetupIntent → `succeeded`
4. Create subscription with `default_payment_method` from SetupIntent PM

### 2. Subscriptions API (create + confirm)

1. Create subscription: `payment_behavior=default_incomplete`, `payment_settings.save_default_payment_method='on_subscription'`, expand `latest_invoice.confirmation_secret`
2. Confirm PaymentIntent: `POST /v1/payment_intents/:id/confirm` with `payment_method_data[type]=cashapp`, `mandate_data`, `return_url`
3. Status → `requires_action` → redirect/QR → subscription activates on success

### 3. Checkout (hosted)

Add `cashapp` to `payment_method_types` in a Checkout Session with `mode='subscription'`.

## Authentication UX

| Platform | Flow |
|---|---|
| Mobile | Redirect to Cash App app; after auth, app redirects to `return_url` |
| Desktop | Display QR code; customer scans with Cash App → redirects to `return_url` |

## Key parameters

| Parameter | Purpose |
|---|---|
| `mandate_data` | Required for recurring; captures customer acceptance |
| `return_url` | Where Cash App redirects after authentication |
| `usage='off_session'` | Enables recurring charges without customer present |
| `save_default_payment_method='on_subscription'` | Auto-saves PM when subscription activates |

## Testing

- Mobile sandbox: tap Subscribe → test approve/decline page
- Desktop sandbox: scan QR with any QR reader → test URL
- Live mode: Cash App auto-approves — no manual approve/decline

## vs Amazon Pay

Very similar 3-path structure to [[stripe-amazon-pay]]. Key difference: Cash App uses QR code (desktop) while Amazon uses a redirect-only flow. Both require `mandate_data` and `return_url`.

## Sources

- [[source-stripe-subscriptions-cash-app-pay]] — Stripe docs: Cash App Pay subscription integration (3 paths: SetupIntents, Subscriptions API, Checkout)
