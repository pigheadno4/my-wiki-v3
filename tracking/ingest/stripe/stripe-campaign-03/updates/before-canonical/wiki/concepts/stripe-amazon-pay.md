---
title: "Stripe Amazon Pay"
type: concept
category: framework
tags: [stripe, amazon-pay, subscriptions, payment-methods, setup-intents, mandate]
---

## Overview

Amazon Pay is a redirect-based payment method on Stripe that lets customers pay using their Amazon account credentials. Customers authenticate at Amazon's hosted page before returning to complete the purchase. Supports one-time payments and recurring subscriptions.

## Key characteristics

- **Redirect-based**: customer is sent to Amazon for authorization, then redirected back
- **API examples**: the 2026-05-13 SetupIntent and PaymentIntent examples include `mandate_data` for customer acceptance and `return_url` for the redirect; the hosted Checkout variant instead uses customer authorization on its hosted page and shows `success_url`
- SetupIntent `usage` may be `off_session` or `on_session`; the guide's recurring-payment sample chooses `off_session`

## Subscription integration paths

The 2026-05-13 guide describes three example paths for Amazon Pay subscriptions below. The 2026-11-07 capture is only a variant index linking to path bodies; those November bodies were not captured here.

### 1. SetupIntents API (pre-authorize)

Best when you want to authorize the mandate before creating the subscription.

The May 2026 server example creates a SetupIntent with `payment_method_types=['amazon_pay']`, `confirm=true`, `usage=off_session`, `mandate_data`, and `return_url`; the text also allows `usage=on_session`. A later client example calls `stripe.confirmAmazonPaySetup(clientSecret, { return_url, mandate_data })` for Amazon authorization. After obtaining the SetupIntent PaymentMethod, the subscription example sets `default_payment_method` and `off_session=true`.

> [!warning] Contradiction
> The guide shows both server-side `confirm=true` and later client-side `confirmAmazonPaySetup`, without explaining whether both belong in one runnable sequence. These are dated examples, not a validated combined flow. See [[source-stripe-subscriptions-amazon-pay]].

### 2. Payment Intents API (create + confirm)

Best for integrations with custom checkout UI.

1. Create subscription: `payment_behavior=default_incomplete`, `payment_settings.payment_method_types=['amazon_pay','card']`, expand `latest_invoice.confirmation_secret`
2. Confirm PaymentIntent: the May 2026 POST example uses `payment_method_data[type]=amazon_pay`, `mandate_data`, and `return_url`.

> [!warning] Contradiction
> The May guide's confirm-call prose says `payment_method_types=amazon_pay`, while the adjacent POST example instead uses `payment_method_data[type]=amazon_pay`. The capture does not resolve the intended confirm-call parameter. Subscription-creation `payment_settings.payment_method_types` is a separate setting. See [[source-stripe-subscriptions-amazon-pay]].
3. A `requires_action` response means the customer still needs to authenticate with Amazon Pay. In the May guide, the subscription becomes active and saves the payment method as default only after successful payment.

`save_default_payment_method='on_subscription'` auto-saves the PM when subscription activates.

### 3. Checkout (hosted)

In the 2026-05-13 hosted Checkout example, the server creates a Session with a recurring price and quantity, `mode='subscription'`, `success_url`, and `payment_method_types` including `amazon_pay`, then redirects the customer to the returned Session URL. The customer authorizes future Amazon-account payments through Checkout.

## Key parameters

| Parameter | Purpose |
|---|---|
| `mandate_data` | Shown in the May SetupIntent and PaymentIntent API examples for customer acceptance; not shown as a Checkout Session parameter in the hosted variant |
| `return_url` | Shown in the May API examples for redirects; hosted Checkout example instead shows `success_url` |
| `usage=off_session` / `usage=on_session` | Both named for SetupIntent creation; the sample chooses `off_session` |
| `off_session=true` | Shown on subscription creation in the SetupIntents example |
| `save_default_payment_method='on_subscription'` | Shown in the PaymentIntents subscription example; saves the method when the subscription activates |

## Sources

- [[source-stripe-subscriptions-amazon-pay]] — Stripe docs: Amazon Pay subscription integration (3 paths: SetupIntents, PaymentIntents, Checkout)
