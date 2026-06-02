---
title: "Email Receipts"
type: source
date_ingested: 2026-04-22
original_format: webpage
raw_files:
  - "stripe-email-receipts-2025.md"
tags: [stripe, receipts, invoices, invoice-creation, checkout-sessions, payment-intents, email, localization]
---

## Summary

Guide for sending email receipts and paid invoices. Both API paths auto-send receipts when enabled; key differences: CS can generate paid invoices (separate pricing), PI cannot — must use Stripe Billing directly.

> See also [[source-stripe-checkout-receipts]] for deeper CS receipt/invoice coverage.

## Checkout Sessions Path

- Auto receipts: Dashboard → Customer emails → "Successful payments"
- Custom text: `payment_intent_data.description`
- Paid invoices: `invoice_creation: { enabled: true }` — one-time payments only; priced separately from Invoicing product
- `invoice_data` hash: `description`, `metadata`, `account_tax_ids`, `custom_fields`, `rendering_options.amount_tax_display`, `footer`
- Delayed PMs: invoice sent after `payment_intent.succeeded`, not at `checkout.session.completed`
- Localization priority: `Customer.preferred_locales` → Dashboard setting → browser locale (if no customer)

## Payment Intents Path (Key Differences)

### `receipt_email` Parameter

```js
stripe.paymentIntents.create({
  amount: 1099, currency: 'usd',
  description: 'Thanks for your purchase!',
  receipt_email: 'extra@example.com',  // additional address — not a replacement
});
```

- `receipt_email` is **additional** — sent alongside the customer's email, not instead of it
- NOT sent to email in `PaymentMethod.billing_details.email`
- To trigger receipt post-confirmation: update `receipt_email` on the confirmed PaymentIntent
- Receipt shows: amount + public business info + `description` only — **no line items**

### Cannot Generate Invoices

Payment Intents API **cannot** generate invoices. Use Stripe Billing (`stripe.invoices.create()`) directly.

### Localization

Localization priority (PI): `Customer.preferred_locales` → Dashboard setting. Browser locale is **not** used even if no customer is set (differs from CS path).

## Shared: Receipts Pull from Charge

Receipts pull data from the `Charge` object created at PaymentIntent confirmation. To update receipt data (e.g. `description`) after the charge is generated:
- Update the `Charge` object: `stripe.charges.update(chargeId, { description: '...' })`
- Changes to a confirmed PaymentIntent do NOT appear on receipts

## Images (Invoice PDF, receipt, email)

![Invoice PDF](../raw/assets/stripe-invoice-pdf-example.png)
![Invoice receipt](../raw/assets/stripe-invoice-receipt-example.png)
![Invoice summary email](../raw/assets/stripe-invoice-summary-email.png)

## Related Pages

- [[source-stripe-checkout-receipts]] — CS receipts (deeper coverage, 3 CDN images)
- [[stripe-checkout]] — Checkout concept page
- [[stripe-payment-intents]] — Payment Intents concept page

## Raw Sources

- [[stripe-email-receipts-2025]] — verbatim receipts guide (both API paths)
