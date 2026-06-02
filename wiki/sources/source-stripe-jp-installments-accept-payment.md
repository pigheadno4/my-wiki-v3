---
title: "Stripe: Accept Installment Card Payments (Japan)"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-jp-installments-accept-payment-2025.md"
tags: [stripe, japan, installments, checkout, payment-element, payment-intents, invoices, payment-links]
---

## Summary

Integration guide for Japan installment payments across 4 Stripe products: Checkout, Payment Element, Direct API (Payment Intents), and Invoices. Payment Links is also supported (no-code, enable via Dashboard).

## Key Integration Details

**Checkout**: create session with `payment_method_options.card.installments.enabled: true`. `payment` mode only (not `setup`/`subscription`).

**Payment Element**: create PaymentIntent with `payment_method_options.card.installments.enabled: true`. Dynamic payment methods → installments appear automatically (don't manually set `enabled: false`).

**Direct API (4 steps)**:
1. Collect card on client (Elements Card Element)
2. Create PaymentIntent server-side with `installments.enabled: true` (don't confirm yet)
3. Return `available_plans` to client for customer selection
4. Confirm PaymentIntent with selected `plan` object

**Plan removal gotcha**: once a plan is set on a PaymentIntent, it persists until explicitly unset. Must clear when retrying with a different card.

**Invoices**: `collection_method: 'send_invoice'` only (not `charge_automatically`). Individual invoices only (not subscriptions). Customer selects plan on hosted invoice page.

**Payment Links**: enable/disable via Dashboard payment methods settings (enabled by default).

## Test Cards

| Brand | Success | Failure |
| --- | --- | --- |
| Visa | 4000003920000003 | 4000003920000029 (`card_declined`) |
| Mastercard | 5200003920000008 | — |
| JCB | 3530111333300000 | — |
| Diners | 36000039200009 | — |

PM IDs: `pm_card_jp`, `pm_card_jp_mastercard`, `pm_card_jcb`, `pm_card_jp_diners`, `pm_card_jp_visa_installmentsDeclined`.

## Raw Sources

- [[stripe-jp-installments-accept-payment-2025]] — verbatim webpage content (Checkout/Elements/Direct API/Invoices/Payment Links + test cards)
