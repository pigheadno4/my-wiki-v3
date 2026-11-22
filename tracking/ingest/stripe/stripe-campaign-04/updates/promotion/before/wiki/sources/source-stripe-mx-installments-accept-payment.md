---
title: "Stripe: Accept Meses Sin Intereses Card Payments"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-mx-installments-accept-payment-2025.md"
tags: [stripe, mexico, installments, meses-sin-intereses, checkout, payment-element, payment-intents, invoices, payment-links]
---

## Summary

Integration guide for Mexico meses sin intereses across 4 Stripe products: Checkout, Payment Element, Direct API (Payment Intents), and Invoices. Payment Links also supported (no-code). Accounts v2 API supported for customer representation.

## Key Integration Details

**Checkout**: `payment_method_options.card.installments.enabled: true`. `payment` mode only.

**Payment Element**: same PaymentIntent parameter. Dynamic payment methods → installments appear automatically.

**Direct API**: same 4-step flow as Japan installments (collect card → retrieve plans → select plan → confirm with chosen plan). Plan removal gotcha applies.

**Invoices**: `send_invoice` mode only (not `charge_automatically`). Min 300 MXN for plans to show. Individual invoices only (not subscriptions).

**Payment Links**: enable via Dashboard payment methods settings.

**Custom settings**: Dashboard allows configuring specific monthly plans, min and max transaction amounts per plan — applies to all integrations.

## Test Cards

| Number | Description |
| --- | --- |
| 4000004840000008 | All 6 plans (3/6/9/12/18/24 months) available |
| 4242424242424242 | No installment plans available |

## Raw Sources

- [[stripe-mx-installments-accept-payment-2025]] — verbatim webpage content (Checkout/Elements/Direct API/Invoices/Payment Links + test cards + custom settings)
