---
title: "Stripe: PayNow Payments"
type: source
date_ingested: 2026-05-06
original_format: webpage
raw_files:
  - "stripe-paynow-2025.md"
tags: [stripe, real-time-payments, paynow, singapore, sgd, qr-code, connect, terminal, billing]
---

## Summary

Overview of Stripe's PayNow integration — Singapore-only QR code payment method. 1.3% pricing, T+1 payout, 90-day refunds, no disputes, no statement descriptor customization. Connect and Terminal supported; billing via `send_invoice` only.

## Key Details

**API enum**: `paynow`. SGD only. Singapore customers and merchants only (SG accounts only).

**Pricing**: 1.3%.

**Payout**: T+1 — funds available in Stripe balance the day after the transaction.

**Refunds**: 90-day window. Asynchronous — via `refund.updated`/`refund.failed` webhook events.

**QR code expiration**: 1 hour. Expired QR → `payment_intent_payment_attempt_expired` error. Must webhook customer back to create a new PaymentIntent/QR.

**Duplicate protection**: QR code rejected after first successful use.

**Statement descriptor**: ignored — `STRIPE PAYMENTS SINGAPORE PTE. LTD.` always shown (cannot customize).

**No disputes** — QR authentication prevents chargebacks.

**Billing**: supports subscriptions and invoices via `send_invoice` collection method only (no auto-charge).

**Prohibited categories**: Petroleum and Petroleum Products, Fuel Dealers, Service Stations, Automated Fuel Dispensers.

**Connect**: Direct, Destination, Separate charges and transfers. Capability: `paynow_payments`. Must set correct MCC for connected accounts.

**Product support**: Connect, Checkout (not subscription/setup mode), Payment Links, Elements (not Express Checkout Element), Subscriptions (`send_invoice`), Invoicing (`send_invoice`), Terminal.

## Raw Sources

- [[stripe-paynow-2025]] — verbatim webpage content (160 lines); fixed `*webhook*` ×1, `*subscriptions*` ×1, `*invoices*` ×1, `*Connect*` ×1
