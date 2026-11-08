---
title: "Stripe Subscriptions — Integrate with Third-Party Payment Processors"
type: source
date_ingested: 2026-05-13
original_format: webpage
raw_files:
  - "stripe-subscriptions-third-party-2026.md"
tags: [stripe, billing, subscriptions, third-party, custom-payment-methods, payment-records, off-stripe, orchestration]
---

## Summary

Guide for using Stripe Billing subscriptions/invoices with non-Stripe payment processors. Two approaches: (1) "Own processor" (modern) using custom payment methods + payment records API; (2) "Out-of-band" (legacy) using `paid_out_of_band`. API version: `2026-04-22.dahlia`.

## Two integration approaches

### Approach 1: Own processor (custom PMs + payment records) — recommended

Full lifecycle management via Stripe webhooks. Supports `charge_automatically` subscriptions.

**Setup flow**:
1. Create custom PM type in Dashboard (branding/logo)
2. Create subscription: `payment_behavior=default_incomplete`
3. Collect payment via 3rd party → create custom PM → attach to customer → set as subscription default
4. `paymentRecords.reportPayment()` → `invoices.attachPayment(invoiceId, { payment_record: id })`
5. Must report within **23 hours** or subscription → `incomplete_expired`

**Renewal flow**:
- Listen for `invoice.payment_attempt_required` webhook
- Collect payment off-session via 3rd party
- `paymentRecords.reportPayment()` → `invoices.attachPayment()`

**Retry logic**: use `reportPaymentAttempt` against existing PaymentRecord; do NOT create new PaymentRecord for retry (causes multiple payment entries on invoice).

**Refunds**: process at 3rd party → `paymentRecords.reportRefund()` → create Credit Note for invoice adjustment.

**Canceled payments**: `paymentRecords.reportPaymentAttemptCanceled()` (async flow only).

### Approach 2: Out-of-band (legacy)

**Setup**:
- Disable invoice emails in Dashboard
- Disable customer portal PM management
- Create subscription: `collection_method=send_invoice`, `days_until_due=30`
- Store 3rd party tokens in Customer metadata

**Payment flow**:
- Listen for `invoice.finalized` → collect at 3rd party → `invoices.pay(id, { paid_out_of_band: true })`

**Limitations**: no partial payments; must handle all retries yourself.

## Limitations (Approach 1)

- Cannot use Checkout (Payment Element or custom flow only)
- Cannot manage disputes in Stripe
- Cannot initiate refunds from Stripe
- No Smart Retries, no revenue recovery emails
- Hosted Invoice Page not supported
- Customer portal: cannot add discounts if `proration_behavior=always_invoke`
- Country restrictions: 43 business countries, 100+ processor countries

## Revenue recovery support (Approach 1)

Supported: automations, scheduled retries, revenue recovery analytics.
NOT supported: Smart Retries, recovery emails.

## Billing volume / pricing

3rd party billing volume counts toward total Stripe Billing volume for pricing (same as on-Stripe).

## Related pages

- [[stripe-billing-third-party]] — concept page
- [[stripe-custom-payment-methods]] — custom PM concept
- [[stripe-subscriptions]] — concept page
- [[stripe]] — company page

## Raw Sources

- [[stripe-subscriptions-third-party-2026]] — verbatim Stripe docs webpage (1027 lines)
