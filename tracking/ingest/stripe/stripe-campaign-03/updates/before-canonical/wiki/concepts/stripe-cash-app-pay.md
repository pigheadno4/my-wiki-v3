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
- The 2026-05-13 direct SetupIntent and PaymentIntent-confirm examples include `mandate_data` and `return_url`; its Checkout Session example omits both. These examples do not establish requirements across all three paths.
- `next_action.cashapp_handle_redirect_or_display_qr_code` appears in the May direct API authentication flows.
- `usage='off_session'` appears in the May SetupIntent example for future use; its path-wide requiredness is not established by that example.

## Subscription integration paths

The 2026-05-13 combined guide describes three subscription approaches below. The 2026-11-07 capture is a variant index; it does not verify current variant request fields, eligibility, or runtime outcomes.

### 1. SetupIntents API (pre-authorize)

1. The 2026-05-13 Node.js example creates a SetupIntent with `confirm=true`, `usage='off_session'`, `payment_method_types=['cashapp']`, `mandate_data`, and `return_url`; it does not prove all values are required for every SetupIntent path.
2. If the SetupIntent is `requires_action`, use its QR or redirect next action to start customer authentication; displaying the QR or redirecting is not a success signal.
3. After customer authentication, verify that the SetupIntent reaches `succeeded`.
4. Only then create the subscription with `default_payment_method` from the succeeded SetupIntent's PaymentMethod.

### 2. Subscriptions API (create + confirm)

1. Create subscription: `payment_behavior=default_incomplete`, `payment_settings.save_default_payment_method='on_subscription'`, expand `latest_invoice.confirmation_secret`
2. Confirm the PaymentIntent separately. The May prose names `payment_method_types=cashapp`, but its adjacent curl example sends `payment_method_data[type]=cashapp`, `mandate_data`, and `return_url`; the intended confirm parameter remains unresolved by these captures.
3. If the PaymentIntent requires customer action, use the QR or redirect path. The May guide places PaymentIntent `succeeded` after authentication and states that the subscription becomes active after successful payment; QR display or redirect alone is not activation.

### 3. Checkout (hosted)

In the 2026-05-13 hosted Checkout example, create a Session with a recurring Price and quantity in `line_items`, `mode='subscription'`, `payment_method_types=['card', 'cashapp']`, and `success_url`. Redirect the customer to the Session URL to authorize future Cash App payments. This is the May example, not a verified current Session recipe.

## Authentication UX

| Platform | Flow |
|---|---|
| Mobile | In the 2026-05-13 direct SetupIntent and PaymentIntent examples, Cash App redirects the customer to the example `return_url` after authentication. The May Checkout Session example instead sets `success_url` and omits `return_url`; the November index establishes no Checkout return behavior. |
| Desktop | The May direct API examples describe QR display for Cash App authentication, and its Checkout section describes scanning a QR code in test and live modes. These captures do not establish a universal post-scan return destination. |

## Key parameters

| Parameter | Purpose |
|---|---|
| `mandate_data` | Included in the May direct SetupIntent and PaymentIntent-confirm examples for customer acceptance; absent from its Checkout Session example |
| `return_url` | Included in those May direct examples as the post-authentication return destination; absent from its Checkout Session example |
| `usage='off_session'` | Value shown in the May SetupIntent example for future use; not proven path-wide required |
| `save_default_payment_method='on_subscription'` | Auto-saves PM when subscription activates |

## Testing

For the 2026-05-13 hosted Checkout variant:

- Mobile sandbox: tap Subscribe → test approve/decline page
- Desktop sandbox: scan QR with any QR reader → test URL
- Live-mode setup flow: after a Cash App redirect or QR scan, the May guide says there is no sandbox-style approval/decline choice and describes the setup as automatically approved. This does not establish a successful payment, approval for every customer, or a future subscription charge.

## vs Amazon Pay

The May Cash App Pay guide has three subscription paths, like the routed [[stripe-amazon-pay]] concept. Its direct API examples show a desktop QR flow and mobile redirect; this Cash App capture does not establish `mandate_data` or `return_url` as requirements for all three paths.

## Sources

- [[source-stripe-subscriptions-cash-app-pay]] — Cash App Pay subscription guide: three detailed variants captured 2026-05-13; the 2026-11-07 base capture is a variant index.
