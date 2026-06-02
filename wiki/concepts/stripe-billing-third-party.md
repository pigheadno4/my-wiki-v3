---
title: "Stripe Billing with Third-Party Payment Processors"
type: concept
category: framework
tags: [stripe, billing, subscriptions, third-party, custom-payment-methods, payment-records, off-stripe, orchestration]
---

## Overview

Stripe Billing supports processing subscription payments through non-Stripe payment processors. Two approaches: (1) **Own processor** using Custom Payment Methods + Payment Records API (`charge_automatically`-compatible, webhook-driven); (2) **Out-of-band** (legacy, `send_invoice` + `paid_out_of_band`).

## Approach 1: Own processor (recommended)

Uses two Stripe primitives:
- **Custom payment methods**: Stripe objects referencing non-Stripe PMs (card, bank account, etc.)
- **Payment records**: Reports off-Stripe payment outcomes to Stripe

### Setup flow

1. Create custom PM type in Dashboard (name + logo)
2. Create subscription: `payment_behavior=default_incomplete`
3. Customer pays via 3rd party → create custom PM → attach to customer → set as subscription default
4. `paymentRecords.reportPayment()` → `invoices.attachPayment(invoiceId, { payment_record: id })`
5. **Must report within 23 hours** or subscription → `incomplete_expired`

### Renewal flow (off-session)

Listen for `invoice.payment_attempt_required` → collect payment at 3rd party → `reportPayment()` → `attachPayment()`.

### Retry logic

Use `reportPaymentAttempt` against the **existing** PaymentRecord for retries. **Do NOT create a new PaymentRecord** for each retry — causes duplicate payment entries on invoice.

### Refunds

Process refund at 3rd party → `paymentRecords.reportRefund()` → create Credit Note for invoice adjustment.

### Limitations

- No Checkout (use Payment Element or custom flow)
- Cannot manage disputes in Stripe
- Cannot initiate refunds from Stripe
- No Smart Retries, no revenue recovery emails
- Hosted Invoice Page not supported
- Customer portal: cannot add discounts if `proration_behavior=always_invoice`
- Country restrictions: 43 business countries, 100+ processor countries

### Revenue recovery

Supported: automations, scheduled retries, analytics. NOT supported: Smart Retries, recovery emails.

## Approach 2: Out-of-band (legacy)

**Setup**: disable invoice emails in Dashboard; disable customer portal PM management; create subscription with `collection_method=send_invoice`, `days_until_due=30`; store 3rd party tokens in Customer metadata.

**Payment**: listen for `invoice.finalized` → collect at 3rd party → `invoices.pay(id, { paid_out_of_band: true })`.

**Limitations**: no partial payments, no Checkout/Elements, must handle all retries yourself.

## Switching approaches

Out-of-band → charge_automatically: collect new PM, update `collection_method` + `default_payment_method`.

## Billing volume / pricing

3rd party billing volume counts toward total Stripe Billing volume (same as on-Stripe transactions).

## API version

Uses `2026-04-22.dahlia` for Payment Records API.

## Sources

- [[source-stripe-subscriptions-third-party]] — Stripe docs: full integration guide (custom PMs, payment records, webhook handler, retry logic, refunds, out-of-band legacy)
