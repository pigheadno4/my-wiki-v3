---
title: "Stripe Checkout: Email Receipts and Paid Invoices"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-checkout-receipts-2025.md"
tags: [stripe, checkout, receipts, invoices, invoice-creation, email, localization]
---

## Summary

Guide for sending email receipts and paid invoices from Stripe Checkout. Covers automated receipt setup, customization, paid invoice generation (`invoice_creation`), the `invoice_data` customization hash, delayed PM behavior, and receipt/invoice localization logic.

## Key Takeaways

- **Receipts**: Dashboard → Customer emails → Successful payments toggle; only sent on successful payment; customized via Branding + Public details settings
- **`payment_intent_data.description`**: custom text on receipt (goods description, auth code, cancellation policy)
- **Receipts from Charge**: receipt data comes from `Charge` object — to update post-charge, update Charge directly (not PaymentIntent)
- **Paid invoices**: `invoice_creation: { enabled: true }` on session create; one-time payments only (subscriptions auto-generate); **priced separately** from Invoicing product
- **Prerequisites for invoices**: "Successful payments" email toggle must be on; incompatible with `payment_intent_data.capture_method: 'manual'`
- **Delayed PMs**: invoices sent after payment succeeds (not on session completion) — later delivery for ACH, Bacs, etc.
- **`invoice.paid` event**: programmatic access to invoice after payment

## Receipt Customization

| Option | Where to configure |
| --- | --- |
| Logo, colors | Dashboard → Branding settings (logo max 512KB, 128×128px min, JPG/PNG/GIF) |
| Contact info, website | Dashboard → Public details settings |
| Custom text on receipt | `payment_intent_data.description` on session create |

## Invoice Creation

```js
stripe.checkout.sessions.create({
  mode: 'payment',
  invoice_creation: {
    enabled: true,
    invoice_data: {
      description: 'Invoice for Product X',
      metadata: { order: 'order-xyz' },
      account_tax_ids: ['DE123456789'],
      custom_fields: [{ name: 'Purchase Order', value: 'PO-XYZ' }],
      rendering_options: { amount_tax_display: 'include_inclusive_tax' },
      footer: 'B2B Inc.',
    },
  },
  ...
})
```

`invoice_data` fields: `description`, `metadata`, `account_tax_ids`, `custom_fields`, `rendering_options`, `footer`.

## Localization Priority

1. `Account.defaults.locales` (Accounts v2) or `Customer.preferred_locales` (Customers v1)
2. Dashboard language setting (if customer set but no preferred locales)
3. Browser locale of user opening the Checkout Session URL (if no customer set)

## Related Pages

- [[stripe-checkout]] — Stripe Checkout concept page
- [[source-stripe-checkout-fulfillment]] — Post-payment fulfillment guide

## Raw Sources

- [[stripe-checkout-receipts-2025]] — Email receipts: automatic setup, branding, custom text, paid invoice creation, invoice_data, delayed PMs, localization (3 CDN images)
