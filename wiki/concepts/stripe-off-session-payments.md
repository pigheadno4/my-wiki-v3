---
title: "Stripe Off-Session Payments API"
type: concept
category: technology
tags: [stripe, off-session, recurring, smart-retries, multi-processor, v2-api]
---

## Overview

The Off-Session Payments API (`stripe.v2.payments.offSessionPayments`) is a v2 private preview for initiating recurring and unscheduled payments against saved payment methods. Stripe's November overview documents an access request. The API supports eligible retries and has a separate Orchestration route.

## Key Features

**Retry strategy**: `retry_details.retry_strategy=best_available` requests an eligible retry strategy. The response can show `smart` for AI-based Smart Retries, `scheduled` for a custom schedule, or `heuristic` for Direct Debit. A payment can enter `pending_retry`. Hard declines such as `authentication_required` prevent automatic retry. See [[source-stripe-off-session-payments-api#Retry strategy|the dated strategy comparison]].

**Multi-processor routing**: The May overview described routing to supported processors. The November overview omits that paragraph, while the separate November guide documents an opted-in, card-only Orchestration path that excludes Smart Retries.

## API (v2 namespace)

```js
stripe.v2.payments.offSessionPayments.create({
  amount: { value: 1000, currency: 'usd' },
  customer: 'cus_xxx',
  payment_method: 'pm_xxx',
  cadence: 'recurring',
  retry_details: { retry_strategy: 'best_available' },
})
```

The May guide links the [preview API reference](https://docs.stripe.com/api/v2/payments/off-session-payments/object.md?api-version=preview). The [[source-stripe-off-session-payments-api#Create an off-session payment|dated request examples]] distinguish the November overview's `2026-04-22.preview` from the integration guide's `2026-08-26.preview` payment request and `2026-10-28.preview` event destination example.

## Workflow

1. Collect and save the customer's payment method using Checkout Sessions, Payment Intents, or Setup Intents (see [[stripe-saved-payment-methods]])
2. Pass the saved `payment_method` ID to the Off-Session Payments API
3. Stripe attempts authorization after returning the create response. A separate v2 event destination reports authorization attempts and outcomes. See [[source-stripe-off-session-payments-api#Asynchronous attempts and outcomes|the event and capture distinctions]].

## Relationship to Orchestration

The November companion describes [[stripe-orchestration|Orchestration]] for Off-Session Payments as a separate card-only routing path with access to both previews, an onboarded processor, an active configuration and per-request opt-in. It excludes Connect, raw card data and Smart Retries. A routing rule can name an optional retry processor. See [[source-stripe-off-session-payments-api#Separate Orchestration path|the dated routing scope]].

## Sources

- [[source-stripe-off-session-payments-api]] — overview: features, API, compatible APIs, compliance
