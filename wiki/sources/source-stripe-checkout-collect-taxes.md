---
title: "Collect Taxes — Checkout Sessions and Payment Intents"
type: source
date_ingested: 2026-04-21
date_updated: 2026-11-15
original_format: webpage
canonical_url: "https://docs.stripe.com/payments/advanced/tax"
raw_files:
  - "stripe-checkout-collect-taxes-2025.md"
tags: [stripe, tax, checkout-sessions, payment-intents, stripe-tax, tax-api, tax-calculations, tax-id, reversal, automatic-tax]
---

## Summary

The April 21, 2026 full guide covers custom Elements tax collection through Checkout Sessions and Payment Intents. Its Checkout Sessions example uses `automatic_tax`; its Payment Intents section presents a choice between Stripe-managed Payment Intents tax handling and a custom Tax API flow (`stripe.tax.calculations.create`) for greater reversal and recording control. It also covers path-specific Tax ID Element collection and preview verification. The November 7 capture is a variant index only and does not establish current behavior or beta status.

> See also [[source-stripe-checkout-taxes]] for existing CS tax coverage.

## Capture boundary

The operational details below are from the full April 21, 2026 capture. The November 7, 2026 capture at the same canonical URL gives only a purpose statement and links to Checkout Sessions and Payment Intents variants. Those variant bodies were not included in this packet. Read April details as dated guidance; the index neither renews nor withdraws their API, UI, SDK, legal, eligibility, or outcome claims.

## Checkout Sessions Path (April 21, 2026)

### Setup

The captured example creates a Checkout Session with `mode: 'payment'` and `ui_mode: 'elements'`. Stripe Tax calculates only where the account is registered to collect tax; the guide says to enable `automatic_tax` and supply a line-item tax code and tax behavior or use Dashboard defaults. The example is a request shape, not proof of a completed payment or correct tax outcome.

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

For the April guide's minimum billing-address collection path, omit `shipping_address_collection`: when supplied, Stripe uses shipping address details for tax instead. `billing_address_collection: 'required'` calls for a full billing address via Address Element or a custom form. Minimum country/postal-code input can differ from the tax result for a full address in some regions; the guide recommends full address collection where relevant. `action.updateBillingAddress` returns an error in this Payment Element path because it can conflict with that collection.

### Render Tax Amounts

```js
// React: from checkoutState.checkout.total
checkout.total.subtotal.amount
checkout.total.taxExclusive.amount  // or taxInclusive — use the right one
checkout.total.total.amount

// HTML+JS: from session.total on 'change' event
session.total.taxExclusive.amount
```

### Tax ID Collection (April preview)

`tax_id_collection: { enabled: true }` is a server-side Checkout Session setting. The separate client-side Tax ID Element is marked public preview in the April guide and uses the captured `custom_checkout_tax_id_1` flag. Collection targets business tax IDs; correct format during checkout is not government validity. For an existing Customer, `customer_update.address` or `.shipping` set to `auto` replaces previously saved address data with checkout-entered data. No November variant body was read to confirm current flag or preview status.

```js
// Enable on session
tax_id_collection: { enabled: true }

// Beta flag + element
const stripe = Stripe('PK', { betas: ['custom_checkout_tax_id_1'] });
const taxIdElement = checkout.createTaxIdElement();
// or React: <TaxIdElement /> from '@stripe/react-stripe-js/checkout'
```

After session: `session.customer_details.tax_ids[].type / .value`; saved to `customer.tax_ids` if customer attached.

### Real-Time Tax ID Verification (April public preview)

```js
const taxIdElement = checkout.createTaxIdElement({
  verification: { taxId: { mode: 'if_supported' } },
});
// Requires beta: 'custom_checkout_tax_id_verification_1'
// 'change' event includes verification.taxId.status: 'pending'|'verified'|'unverified'|'unavailable'
// Falls back to format validation + async if government DB unavailable
// Supports: ABN (AU), EU VAT, GB VAT
```

## Payment Intents Path: Tax choices and custom Tax API (April 21, 2026)

The older guide distinguishes a Payment Intents tax integration, where Stripe handles tax transactions and flat-amount refund reversals automatically, from the custom Tax API for line-item reversal control, multiple processors, or control over transaction recording. The calculations, recording and reversal examples below describe the **custom Tax API** option; they do not describe every Payment Intents tax integration. Stripe Tax calculation requires tax registrations in applicable jurisdictions.

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

The April examples include multiple items and shipping cost, a New York clothing quantity example, EU inclusive pricing, and a `ship_from_details` beta example for Illinois-origin rules. They illustrate dated cases, not current tax-law or account eligibility guarantees. The calculated `amount_total` can set a PaymentIntent amount; the guide stores the calculation ID in PaymentIntent metadata or the order database before taking payment. A calculation, returned `client_secret`, or browser return does not establish payment success.

### Record Transaction

```js
await stripe.tax.transactions.createFromCalculation({
  calculation: calculation.id,
  reference: 'order_123',
});
```

After the customer pays, the April custom Tax API guide calls for a separate tax transaction from the calculation so the tax appears in Stripe Tax reporting. It suggests an order endpoint after successful submission or a `payment_intent.succeeded` webhook, with a unique transaction and line-item reference; a calculation alone does not appear on the Tax Transactions page. The calculation can be used for transaction creation until its `expires_at`, described as 90 days after creation; tax is not recalculated when the transaction is recorded.

### Reversal

```js
await stripe.tax.transactions.createReversal({
  original_transaction: 'tax_txn_...',
  reference: 'refund_123',
  mode: 'full', // or 'partial' with line_items
});
```

Use `mode: 'partial'` for line-item control in this dated custom Tax API path. The guide caps partial reversals at 30 per sale, rejects reversal above collected tax, and warns that a full reversal does not undo prior partial reversals. Disproportionate partial tax refunds can make reports unreliable because taxable amounts and reasons are not adjusted automatically. Record a separate tax reversal after issuing a refund; a refund request alone is not a tax reversal.

### IP-Based Tax Estimate

The April guide offers IP geolocation for an initial estimate before address entry and advises against using it for the final tax amount because IP location can differ from the customer's actual location. See the old raw for request details.

### Choose PI Tax Integration

| Approach | Use when |
| --- | --- |
| Payment Intents tax integration | Stripe handles tax transactions and reversals automatically; flat-amount refund reversals fit |
| **Custom Tax API** | Need line-item reversal control, multiple payment processors, or control over recording timing |

## Supported Tax ID Types

The April guide's two tax-ID tables enumerate 107 country/type rows, 96 distinct country codes, and 80 distinct enum types; those counts describe the capture, not verified current coverage. Examples marked with "Impact in Tax Calculation" include:
- EU VAT (`eu_vat`) — all EU countries
- GB VAT (`gb_vat`), AU ABN (`au_abn`), IN GST (`in_gst`), CA GST/HST (`ca_gst_hst`), SG GST (`sg_gst`)
- Full tables and the tax-impact footnote are in the April raw. A listed tax ID format does not itself establish legal exemption or government validity.

## Tax ID validation boundaries (April 21, 2026)

- **Checkout Sessions Tax ID Element:** During the Session, Stripe checks format, not government validity. The guide describes later asynchronous government-database checks for AU ABN, EU VAT, and GB VAT.
- **Payment Intents Tax ID Element:** During payment or setup confirmation, Stripe checks format, not government validity, and the guide describes asynchronous government checks for the same three types. Its captured client initialization uses `elements_tax_id_1`; a `CustomerSession` is optional for collection but needed in the documented save and redisplay flow. Saving the tax ID to the Customer is conditional on successful payment and appropriate CustomerSession permissions.
- **Element real-time verification:** The dated Checkout and Payment Intents preview examples use `custom_checkout_tax_id_verification_1` and `elements_tax_id_verification_1` respectively. With `mode: 'if_supported'`, the `change` event can report `pending`, `verified`, `unverified`, or `unavailable`. If a government database is unavailable, the guide says verification falls back to synchronous format checking followed by asynchronous verification. The November index cannot confirm current preview or beta requirements.
- **Custom Tax API calculation:** `customer_details.tax_ids` can yield `tax_id_invalid` for invalid format, but the Tax API does **not** automatically check government databases. Validate through the separate customer tax ID validation route if that check is required before calculation. This is distinct from the Tax ID Element flows above.

## Related Pages

- [[stripe]] — Stripe company
- [[stripe-tax]] — Stripe Tax concept page
- [[stripe-tax-id-element]] — Tax ID Element concept page
- [[source-stripe-checkout-taxes]] — CS automatic tax (earlier source)
- [[source-stripe-tax-id-element]] — Tax ID Element source

## Raw Sources

- [[raw/stripe-checkout-collect-taxes-2025|April 21, 2026 full guide]] — dated Checkout Sessions and Payment Intents content, including custom Tax API and Tax ID Element flows.

## Related raw API references

- [[raw/stripe-payments-advanced-tax-2026-11-07|November 7, 2026 variant index]] — navigation only; links to Checkout Sessions and Payment Intents variant URLs, whose bodies were not captured here.
