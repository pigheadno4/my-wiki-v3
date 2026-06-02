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
- **Mandate required**: must collect `mandate_data` (customer acceptance: type, IP, user agent, timestamp) for recurring use
- `return_url` required for all flows
- `usage=off_session` for recurring charges without customer present

## Subscription integration paths

Three approaches for Amazon Pay subscriptions:

### 1. SetupIntents API (pre-authorize)

Best when you want to authorize the mandate before creating the subscription.

1. Create SetupIntent: `payment_method_types=['amazon_pay']`, `confirm=true`, `usage=off_session`, `mandate_data`, `return_url`
2. Client: `stripe.confirmAmazonPaySetup(clientSecret, { return_url, mandate_data })` → redirects to Amazon
3. After redirect: create subscription with `default_payment_method` from SetupIntent PM + `off_session=true`

### 2. Payment Intents API (create + confirm)

Best for integrations with custom checkout UI.

1. Create subscription: `payment_behavior=default_incomplete`, `payment_settings.payment_method_types=['amazon_pay','card']`, expand `latest_invoice.confirmation_secret`
2. Confirm PaymentIntent: `POST /v1/payment_intents/:id/confirm` with `payment_method_data[type]=amazon_pay`, `mandate_data`, `return_url`
3. Response `requires_action` → customer authenticates at Amazon → subscription activates on success

`save_default_payment_method='on_subscription'` auto-saves the PM when subscription activates.

### 3. Checkout (hosted)

Simplest path — just add `amazon_pay` to `payment_method_types` in a Checkout Session with `mode='subscription'`.

## Key parameters

| Parameter | Purpose |
|---|---|
| `mandate_data` | Required for recurring; captures customer acceptance |
| `return_url` | Where Amazon redirects after authorization |
| `usage=off_session` | Enables recurring charges without customer present |
| `off_session=true` | On subscription create (SetupIntents path) |
| `save_default_payment_method='on_subscription'` | Auto-saves PM when subscription activates |

## Sources

- [[source-stripe-subscriptions-amazon-pay]] — Stripe docs: Amazon Pay subscription integration (3 paths: SetupIntents, PaymentIntents, Checkout)
