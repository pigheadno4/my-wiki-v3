---
title: "Stripe Revolut Pay"
type: concept
category: framework
tags: [stripe, revolut-pay, subscriptions, payment-methods, setup-intents, mandate, redirect]
---

## Overview

Revolut Pay is a redirect-based payment method on Stripe. Customers authenticate via Revolut's app or web interface. Supports subscriptions via mandate authorization. Three integration paths identical in structure to Amazon Pay and Cash App Pay.

## Subscription integration paths

### 1. SetupIntents API (pre-authorize)

Create SetupIntent → `confirm=true`, `usage=off_session`, `payment_method_data[type]=revolut_pay`, `mandate_data` → customer redirected to Revolut Pay → SetupIntent `succeeded` → create subscription with `default_payment_method` + **`off_session=true`**

### 2. Subscriptions API (create + confirm)

Create subscription: `default_incomplete`, `save_default_payment_method='on_subscription'` → confirm PaymentIntent with `payment_method_data[type]=revolut_pay` + `mandate_data` + `return_url` → `requires_action` → customer authenticates → activates

### 3. Checkout (hosted)

Add `revolut_pay` to `payment_method_types` in Checkout Session with `mode='subscription'`.

## Key parameters

| Parameter | Purpose |
|---|---|
| `mandate_data` | Required — captures customer acceptance |
| `return_url` | Required — redirect destination after auth |
| `usage=off_session` | For recurring charges without customer present |
| `off_session=true` | Required on subscription create (SetupIntents path) |

## vs Amazon Pay / Cash App Pay

Structurally identical 3-path integration. See [[stripe-amazon-pay]] and [[stripe-cash-app-pay]] for comparison.

## Sources

- [[source-stripe-subscriptions-revolut-pay]] — Stripe docs: Revolut Pay subscription integration (3 paths: SetupIntents, Subscriptions API, Checkout)
