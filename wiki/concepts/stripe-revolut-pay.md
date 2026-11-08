---
title: "Stripe Revolut Pay"
type: concept
category: framework
tags: [stripe, revolut-pay, subscriptions, payment-methods, setup-intents, mandate, redirect]
---

## Overview

Revolut Pay is a redirect-based payment method on Stripe. Customers authenticate via Revolut's app or web interface. The May 2026 subscription guide describes mandate authorization and three paths: SetupIntents API, direct Subscriptions API, and Stripe-hosted Checkout. The November 7 capture at https://docs.stripe.com/billing/subscriptions/revolut-pay is a variant index, not a new path-specific specification. See [[source-stripe-subscriptions-revolut-pay]].

## Subscription integration paths

### 1. SetupIntents API (pre-authorize)

The May guide's SetupIntent-create example sets `confirm=true`, `usage=off_session`, Revolut Pay method fields, `mandate_data`, and `return_url`. It says to pass the SetupIntent `client_secret` to Stripe.js for buyer redirect and mandate authorization, then shows subscription creation with the returned PaymentMethod as `default_payment_method` and **`off_session=true`** on that SetupIntents-path subscription-create request. The passage does not explicitly verify a `succeeded` SetupIntent status. See [[source-stripe-subscriptions-revolut-pay]].

### 2. Subscriptions API (create + confirm)

The May direct path creates a subscription with `default_incomplete` and `save_default_payment_method='on_subscription'`, then shows a PaymentIntent confirmation example with `payment_method_data[type]=revolut_pay`, `mandate_data`, and `return_url`. `requires_action` calls for customer authentication; the guide says the subscription becomes active and saves the default method **after successful payment**. See [[source-stripe-subscriptions-revolut-pay]].

### 3. Checkout (hosted)

Add `revolut_pay` to `payment_method_types` in Checkout Session with `mode='subscription'`.

## Key parameters

| Parameter | Purpose |
|---|---|
| `mandate_data` | Shown for customer acceptance in the May SetupIntent-create and direct PaymentIntent-confirm examples; not shown explicitly in the Checkout sample |
| `return_url` | Shown on those two direct API requests for redirect; not shown explicitly in the Checkout sample |
| `usage=off_session` | Set on SetupIntent creation in the May SetupIntents path |
| `off_session=true` | Required on subscription create (SetupIntents path) |

> [!warning] Contradiction
> The May direct-confirm prose says `payment_method_types=revolut_pay`, while its cURL example uses `payment_method_data[type]=revolut_pay`. The provided capture does not resolve which exact request to run. See [[source-stripe-subscriptions-revolut-pay]].

## Related payment methods

See [[stripe-amazon-pay]] and [[stripe-cash-app-pay]] for their separately sourced integration guides. The Revolut Pay captures alone do not establish structural identity.

## Sources

- [[source-stripe-subscriptions-revolut-pay]] — May 2026 full three-path Revolut Pay guide, plus November 2026 variant-index navigation; path details remain dated May evidence
