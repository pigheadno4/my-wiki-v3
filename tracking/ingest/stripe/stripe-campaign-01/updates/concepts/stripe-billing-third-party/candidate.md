---
title: "Stripe Billing with Third-Party Payment Processors"
type: concept
category: framework
tags: [stripe, billing, subscriptions, third-party, custom-payment-methods, payment-records, off-stripe, orchestration]
---

## Overview

The May 2026 Stripe guide documented two ways to use Billing subscriptions with non-Stripe processors: (1) **own processor**, using custom PaymentMethods and PaymentRecords with `charge_automatically` invoices; and (2) **out-of-band invoices**, using `send_invoice` and `paid_out_of_band`. The 2026-11-07 canonical capture lists these routes only and does not reverify current behavior or availability. The details below describe the May guide.

## Approach 1: Own processor (May 2026 guide)

Uses two Stripe primitives:
- **Custom payment methods**: Stripe objects referencing non-Stripe PMs (card, bank account, etc.)
- **Payment records**: Reports off-Stripe payment outcomes to Stripe

### Setup flow

1. Create custom PM type in Dashboard (name + logo)
2. Create subscription: `payment_behavior=default_incomplete`
3. Customer pays via 3rd party → create custom PM → attach to customer → set as subscription default
4. `paymentRecords.reportPayment()` → `invoices.attachPayment(invoiceId, { payment_record: id })`
5. The May guide says to report a payment within **23 hours** of subscription creation or the subscription becomes `incomplete_expired`.

> [!warning] Contradiction
> The May guide says attaching a PaymentRecord marks the invoice paid and subscription active (old line 340), but its asynchronous example attaches an initiated record before the processor outcome is reported (old lines 252–317). The exact status timing in that example is unresolved; a Stripe record is not proof of third-party settlement.

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

**Setup in the May 2026 out-of-band guide**: create a customer-configured Account v2 or Customer v1 and a subscription with `collection_method=send_invoice`. Choose `days_until_due` long enough for external recovery; **30 days is the guide’s example**, not a fixed requirement. Disable finalized-invoice emails only if all emailed subscription invoices use a third-party processor, because this setting also affects other `send_invoice` subscriptions. If using the customer portal, the guide says to disable payment-method view/update and plan switching. Store only non-sensitive third-party references in the selected Account or Customer metadata.

**Payment in the May 2026 out-of-band guide**: listen for `invoice.finalized`, collect through the third-party processor, and **only after that external payment succeeds** call `invoices.pay(id, { paid_out_of_band: true })`. An attempted or pending processor payment is not a paid Stripe invoice; the guide says to mark it paid before the subscription due date.

**Limitations**: no partial payments, no Checkout/Elements, must handle all retries yourself.

## Switching approaches

Out-of-band → charge_automatically: collect new PM, update `collection_method` + `default_payment_method`.

## Billing volume / pricing

3rd party billing volume counts toward total Stripe Billing volume (same as on-Stripe transactions).

## API version

Several May 2026 Node examples set `apiVersion: '2026-04-22.dahlia'` for PaymentRecord calls; the guide does not state that this is a universal minimum or verify current account/API availability. One May example has a malformed version string ending in a semicolon (old line 324).

## Sources

- [[source-stripe-subscriptions-third-party]] — May 2026 combined own-processor and out-of-band guide; November 2026 canonical capture is a variant index only
