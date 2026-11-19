---
title: "Collect Taxes — Checkout Sessions and Payment Intents"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-checkout-collect-taxes-2025.md"
tags: [stripe, tax, checkout-sessions, payment-intents, stripe-tax, tax-api, tax-calculations, tax-id, reversal, automatic-tax]
---

## Summary

Comprehensive tax collection guide covering both Checkout Sessions and Payment Intents paths. The CS path uses `automatic_tax`, the PI path uses the full Tax API (`stripe.tax.calculations.create`). Also covers Tax ID collection and the real-time verification beta.

> See also [[source-stripe-checkout-taxes]] for existing CS tax coverage.

## Checkout Sessions Path

### Setup

```js
stripe.checkout.sessions.create({
  automatic_tax: { enabled: true },
  line_items: [{
    price_data: {
      product_data: { name: 'T-shirt', tax_code: 'txcd_99999999' },
      tax_behavior: 'exclusive', // or 'inclusive'
      unit_amount: 2000, currency: 'usd',
    },
    quantity: 1,
  }],
  billing_address_collection: 'auto', // collect minimal tax address via Payment Element
});
```

### Address Collection for Tax

| Setting | Behavior |
| --- | --- |
| `billing_address_collection: 'auto'` | Payment Element collects country + postal code (minimum) |
| `billing_address_collection: 'required'` | Must use Address Element or custom form for full address |
| `fields.billingDetails.address: 'never'` | Must collect tax address another way |
| `fields.billingDetails.address.postalCode: 'never'` | **Returns error** — postal code required for some countries |
| `fields.billingDetails.address.country: 'never'` | Customer's detected country used |

Do **not** pass `shipping_address_collection` when using billing address for tax — if shipping address is provided, tax uses shipping address instead.

### Render Tax Amounts

```js
// React: from checkoutState.checkout.total
checkout.total.subtotal.amount
checkout.total.taxExclusive.amount  // or taxInclusive — use the right one
checkout.total.total.amount

// HTML+JS: from session.total on 'change' event
session.total.taxExclusive.amount
```

### Tax ID Collection

```js
// Enable on session
tax_id_collection: { enabled: true }

// Beta flag + element
const stripe = Stripe('PK', { betas: ['custom_checkout_tax_id_1'] });
const taxIdElement = checkout.createTaxIdElement();
// or React: <TaxIdElement /> from '@stripe/react-stripe-js/checkout'
```

After session: `session.customer_details.tax_ids[].type / .value`; saved to `customer.tax_ids` if customer attached.

### Real-Time Tax ID Verification (Public Preview)

```js
const taxIdElement = checkout.createTaxIdElement({
  verification: { taxId: { mode: 'if_supported' } },
});
// Requires beta: 'custom_checkout_tax_id_verification_1'
// 'change' event includes verification.taxId.status: 'pending'|'verified'|'unverified'|'unavailable'
// Falls back to format validation + async if government DB unavailable
// Supports: ABN (AU), EU VAT, GB VAT
```

## Payment Intents Path: Full Tax API

### Calculate Tax

```js
const calculation = await stripe.tax.calculations.create({
  currency: 'usd',
  line_items: [{ amount: 1000, reference: 'L1', tax_code: 'txcd_99999999' }],
  customer_details: {
    address: { line1: '920 5th Ave', city: 'Seattle', state: 'WA', postal_code: '98104', country: 'US' },
    address_source: 'shipping',
  },
  shipping_cost: { amount: 500 },
});
```

Supports: multiple items, quantity-based exemptions (e.g. NY clothing <$110/item), EU inclusive pricing, ship-from address (beta for Illinois-origin rules).

### Record Transaction

```js
await stripe.tax.transactions.createFromCalculation({
  calculation: calculation.id,
  reference: 'order_123',
});
```

Must record to appear in Stripe Tax reporting.

### Reversal

```js
await stripe.tax.transactions.createReversal({
  original_transaction: 'tax_txn_...',
  reference: 'refund_123',
  mode: 'full', // or 'partial' with line_items
});
```

Use `mode: 'partial'` for line-item level control — key reason to use Tax API over PI automatic tax.

### IP-Based Tax Estimate

Available for initial estimate before customer enters address. Details in raw file.

### Choose PI Tax Integration

| Approach | Use when |
| --- | --- |
| Payment Intents `automatic_tax` | Simple flows; flat-amount refund reversals are fine |
| **Custom Tax API** | Need line-item level reversals; multiple payment processors; full control over recording timing |

## Supported Tax ID Types

100+ types across 100+ countries. Key ones with "Impact in Tax Calculation":
- EU VAT (`eu_vat`) — all EU countries
- GB VAT (`gb_vat`), AU ABN (`au_abn`), IN GST (`in_gst`), CA GST/HST (`ca_gst_hst`), SG GST (`sg_gst`)
- Full table in raw file.

## Async vs Real-Time Validation

- **Async** (always): Stripe validates against government DBs for AU ABN, EU VAT, GB VAT after session
- **Real-time** (preview): verifies as customer types; falls back to format validation if DB unavailable

## Related Pages

- [[stripe-tax]] — Stripe Tax concept page
- [[stripe-tax-id-element]] — Tax ID Element concept page
- [[source-stripe-checkout-taxes]] — CS automatic tax (earlier source)
- [[source-stripe-tax-id-element]] — Tax ID Element source

## Raw Sources

- [[stripe-checkout-collect-taxes-2025]] — verbatim comprehensive tax guide (2599 lines, both API paths)
