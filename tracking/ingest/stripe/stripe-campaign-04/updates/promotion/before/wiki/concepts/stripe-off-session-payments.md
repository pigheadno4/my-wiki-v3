---
title: "Stripe Off-Session Payments API"
type: concept
category: technology
tags: [stripe, off-session, recurring, smart-retries, multi-processor, v2-api]
---

## Overview

The Off-Session Payments API (`stripe.v2.payments.offSessionPayments`) is a v2 API for initiating recurring and unscheduled payments against saved payment methods. It adds two capabilities not in standard Payment Intents: **AI-powered smart retries** and **multi-processor routing**, both handled by Stripe in a single API call.

## Key Features

**Smart retries**: Set `retry_details.retry_strategy: 'best_available'` and Stripe uses AI inference to choose optimal retry times for failed payments — no retry logic required on your server.

**Multi-processor routing**: Route to any Stripe-supported processor or let Stripe auto-route. Works with the Off-Session Payments API and other supported payments APIs.

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

Full API reference at `docs.stripe.com/api/v2/payments/off-session-payments/object` (preview).

## Workflow

1. Collect and save the customer's payment method using Checkout Sessions, Payment Intents, or Setup Intents (see [[stripe-saved-payment-methods]])
2. Pass the saved `payment_method` ID to the Off-Session Payments API
3. Stripe handles the charge and any retries automatically

## Relationship to Orchestration

Multi-processor routing in the Off-Session Payments API overlaps with [[stripe-orchestration]]. Orchestration is the broader routing layer for card payments across external processors; Off-Session Payments adds AI smart retries on top for recurring use cases.

## Sources

- [[source-stripe-off-session-payments-api]] — overview: features, API, compatible APIs, compliance
