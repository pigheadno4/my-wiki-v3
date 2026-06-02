---
title: "Stripe — Radar Risk Signals for Multiple Payment Processors"
type: source
date_ingested: 2026-05-10
original_format: webpage
raw_files:
  - "stripe-radar-multiprocessor-2026.md"
tags: [stripe, radar, multiprocessor, payment-evaluation, external-processor, fraudulent-payment, early-fraud-warning]
---

## Summary

Use Stripe Radar to evaluate non-Stripe-processed payments in real time. Get risk signals at any point in the payment lifecycle via the Payment Evaluation API.

## Signals

| Signal | Status | What it detects |
| --- | --- | --- |
| `fraudulent_payment` | GA (default) | Payment likely to result in fraud dispute or EFW |
| `fraudulent_dispute` | Private preview | Payment likely to result in fraudulent dispute; blocks these payments |
| `early_fraud_warning` | Private preview | Payment likely to result in EFW |

## Prerequisites

- Tokenized PaymentMethod (card type only)
- Radar Session token (for advanced risk factors)
- Customer email via `billing_details.email` on PaymentMethod or Customer object

## API

`POST /v1/radar/payment_evaluations` — evaluate at any point in payment lifecycle.

## Related Pages

- [[stripe-radar]] — concept page (updated with multiprocessor signals)
- [[source-stripe-radar-sessions]] — Radar Sessions (prerequisite)
- [[source-stripe-radar-payg-abuse]] — Payment Evaluation API (different use case)

## Raw Sources

- [[stripe-radar-multiprocessor-2026]] — verbatim multiprocessor risk signals guide
