---
title: "Stripe — Off-Session Payments API"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-off-session-payments-api-2026.md"
tags: [stripe, off-session, recurring, smart-retries, multi-processor, v2-api, payment-method]
---

## Summary

New v2 API for recurring and unscheduled off-session payments. Key differentiators from Payment Intents: AI-powered smart retries and multi-processor routing in a single API call.

## Features

- **Smart retries**: AI inference selects optimal retry times for failed payments (`retry_strategy: 'best_available'`)
- **Multi-processor routing**: Route to any Stripe-supported processor or use automatic routing

## API

```js
stripe.v2.payments.offSessionPayments.create({
  amount: { value: 1000, currency: 'usd' },
  customer: '{{CUSTOMER_ID}}',
  payment_method: '{{PAYMENTMETHOD_ID}}',
  cadence: 'recurring',
  metadata: {},
  retry_details: { retry_strategy: 'best_available' },
})
```

Full reference: `docs.stripe.com/api/v2/payments/off-session-payments/object` (preview)

## Compatible Payment Collection APIs

Use these to collect and save payment methods, then pass the saved `payment_method` to Off-Session Payments:

| API | Use case |
| --- | --- |
| Checkout Sessions | Prebuilt form; save with or without initial payment |
| Payment Intents | Advanced flow; pass final amount directly |
| Setup Intents | Save without initial payment; for future recurring charges |

## Compliance

Must collect explicit written consent from customers covering: authorization for the payment series, timing/frequency, amount determination, and cancellation policy.

## Related Pages

- [[stripe-off-session-payments]] — concept page
- [[stripe-saved-payment-methods]] — saving payment methods (prerequisite for off-session)

## Raw Sources

- [[stripe-off-session-payments-api-2026]] — verbatim Off-Session Payments API overview (63 lines)
