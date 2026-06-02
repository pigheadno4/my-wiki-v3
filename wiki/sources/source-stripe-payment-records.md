---
title: "Stripe Payment Records API"
type: source
date_ingested: 2026-04-19
original_format: webpage
raw_files:
  - "stripe-payment-records-api-2025.md"
tags: [stripe, payment-records, orchestration, multi-processor, off-stripe, reconciliation]
---

## Summary

The Stripe Payment Records API provides a unified ledger for payments across on-Stripe (via PaymentIntents) and off-Stripe (third-party processors). Requires Orchestration to be enabled.

## Key Takeaways

- **Requires Orchestration**: on-Stripe PaymentIntents auto-create PaymentRecords; off-Stripe payments need manual reporting
- **3-level hierarchy**: PaymentRecord → PaymentAttemptRecord(s) → PaymentAttemptRecordEntry(ies) (append-only event log)
- **PaymentAttemptRecordEntries**: preview feature only; events: initiated → authenticated → authorized → guaranteed
- **Enables**: Subscriptions smart retries, out-of-band Invoice payments, multi-processor reconciliation
- **Partial refunds**: report multiple until full amount refunded; omit `amount` to refund full guaranteed amount

## 3-Level Object Hierarchy

```
PaymentRecord
  └── PaymentAttemptRecord (one per attempt; multiple on retry)
        └── PaymentAttemptRecordEntry (append-only log)
              types: initiated, authenticated, authorized, guaranteed
```

## 4 Reporting Methods

| Method | When to use |
| --- | --- |
| `reportPayment` | New off-Stripe payment succeeded |
| `reportPaymentAttemptFailed` | Payment attempt failed |
| `reportPaymentAttempt` | Retry on same PaymentRecord (same or different method/processor) |
| `reportRefund` | Full or partial refund; omit `amount` for full refund |

## Key Fields

- `latest_payment_attempt_record` — most recent attempt on the PaymentRecord
- `amount_guaranteed` — guaranteed funds on the PaymentAttemptRecord
- `processor_details.type` — `"custom"` for third-party processors
- `outcome` — `"guaranteed"` for success, `"refunded"` for refunds

## Retrieve

```javascript
// Retrieve by PaymentRecord ID or PaymentIntent ID (Orchestration only)
const paymentRecord = await stripe.paymentRecords.retrieve('{{PAYMENT_RECORD_ID}}');

// List all attempts for a PaymentRecord
const attempts = await stripe.paymentAttemptRecords.list({
  payment_record: '{{PAYMENT_RECORD_ID}}',
});
```

## Related Pages

- [[stripe]] — Stripe company page
- [[source-stripe-payment-intents]] — PaymentIntents lifecycle
- [[payment-reconciliation-reporting]] — Generic reconciliation concept

## Raw Sources

- [[stripe-payment-records-api-2025.md]] — Payment Records API: 3-level hierarchy, 4 reporting methods, Orchestration requirement, partial refunds, PaymentAttemptRecordEntries (preview)
