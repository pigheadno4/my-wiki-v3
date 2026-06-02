---
title: "Stripe: PayPal Payout Reconciliation"
type: source
date_ingested: 2026-05-07
original_format: webpage
raw_files:
  - "stripe-paypal-reconciliation-2025.md"
tags: [stripe, wallets, paypal, reconciliation, settlement, payout, transaction-id, reference]
---

## Summary

Explains how to reconcile PayPal transactions when settling on PayPal (not Stripe). Stripe auto-reconciles when settling on Stripe. Two methods: using a merchant-controlled `reference` field (recommended) or the PayPal-assigned `transaction_id`.

## Key Details

**Applies to**: PayPal-settlement-on-PayPal only. When settling on Stripe, reconciliation is automatic.

## Method 1: Reference field (recommended)

Set `payment_method_options.paypal.reference` on PaymentIntent with your own order/invoice ID.

```node
payment_method_options: {
  paypal: { reference: 'my_order_id' }
}
```

- Appears as **Invoice ID** in PayPal settlement report
- Visible to the buyer
- Cascades to refunds and disputes derived from the original payment
- Preferred when you have a business-generated order or invoice ID

## Method 2: transaction_id (fallback)

Retrieve from `charge.payment_method_details.paypal.transaction_id` after capture.

- Appears as **Transaction ID** in PayPal settlement report
- Only present after payment is captured
- Use only if no business-generated order ID exists

## PayPal Settlement Report

- 24-hour view of all balance-impacting transactions
- Access: paypal.com → Activity → All Reports → Transactions → Settlement
- Also available via sFTP (contact PayPal to enable)

## Raw Sources

- [[stripe-paypal-reconciliation-2025]] — verbatim reconciliation guide (117 lines); 1 italic fix (_settle_)
