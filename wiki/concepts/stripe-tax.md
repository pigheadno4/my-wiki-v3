---
title: "Stripe Tax"
type: concept
category: technology
tags: [stripe, tax, automatic-tax, stripe-tax, tax-codes, tax-behavior, checkout, invoicing, accounts-v2, manual-tax-rates, tax-rates-api]
---

## Stripe Tax

Stripe's automated tax calculation and collection product. Handles sales tax, VAT, and GST across 50+ countries. Integrates natively with Checkout, Payment Intents, Invoicing, and Subscriptions.

## How It Works

- **Enable**: `automatic_tax: { enabled: true }` on a Checkout Session, Invoice, or Payment Intent
- **Location**: Stripe uses the customer's address to determine applicable tax jurisdiction
  - Priority: shipping address > billing address (fallback)
- **Rates**: Stripe maintains and updates tax rates; no manual rate management needed
- **Tax codes**: product/price-level `tax_code` field categorizes goods/services for correct rates; defaults to Tax Settings dashboard default if unset
- **Tax behavior**: `inclusive` (price includes tax) or `exclusive` (tax added on top)

## Checkout Integration

- **New customers**: Checkout auto-creates customer + saves collected address; no extra config needed
- **Existing customers — use saved address**: verify address validity first
  - Accounts v2: check `automatic_indirect_tax.status = 'active'`
  - Customers v1: check `tax.automatic_tax = 'supported'` or `'not_collecting'`
- **Existing customers — use checkout-entered address**: `customer_update.shipping: 'auto'` or `customer_update.address: 'auto'` to propagate address to customer record
- **Wallet constraints**: Google Pay requires shipping address collection or existing customer with saved shipping; Apple Pay requires browser with Apple Pay v12+
- **Result**: `total_details.amount_tax` on Checkout Session

## Accounts v2 vs Customers v1

Stripe Tax supports both the newer Accounts v2 API (GA for Connect, public preview for others) and the legacy Customers v1 API:

| | Accounts v2 | Customers v1 |
| --- | --- | --- |
| Session param | `customer_account` | `customer` |
| Validate address | `automatic_indirect_tax.status = 'active'` | `tax.automatic_tax = 'supported'/'not_collecting'` |
| Recommended | Yes (for new integrations) | Legacy |

## Key Concepts

- **Tax codes**: categorize products for correct tax treatment (e.g., `txcd_92010001` = Shipping, `txcd_00000000` = Nontaxable); set on Product or inline `price_data.product_data`
- **Tax behavior**: `exclusive` = tax added on top of price; `inclusive` = tax embedded in price
- **Stripe-managed rates**: Stripe maintains rate database across jurisdictions; no manual updates required

## Payment Intents: Full Tax API

For maximum control — especially line-item level reversals:

```js
// 1. Calculate
const calc = await stripe.tax.calculations.create({
  currency: 'usd',
  line_items: [{ amount: 1000, reference: 'L1', tax_code: 'txcd_99999999' }],
  customer_details: { address: { ... }, address_source: 'shipping' },
  shipping_cost: { amount: 500 },
});

// 2. Take payment, then record transaction
await stripe.tax.transactions.createFromCalculation({
  calculation: calc.id, reference: 'order_123',
});

// 3. Reversal (full or partial)
await stripe.tax.transactions.createReversal({
  original_transaction: 'tax_txn_...', reference: 'refund_123',
  mode: 'full', // or 'partial' for line-item level
});
```

**Choose PI Tax API over `automatic_tax`** when: you need line-item level reversals, work with multiple payment processors, or need full control over recording timing.

Supports: IP-based initial estimate, quantity-based exemptions (e.g. NY clothing), EU inclusive pricing, ship-from address (beta for Illinois-origin rules).

## Checkout Sessions: Display Tax Amounts

```js
// React: from checkoutState.checkout.total
checkout.total.taxExclusive.amount  // or taxInclusive — match your tax_behavior
checkout.total.subtotal.amount
checkout.total.total.amount

// HTML+JS: from session.total on 'change' event
session.total.taxExclusive.amount
```

## Manual Tax Rates (Legacy Alternative)

Use `stripe.taxRates.create()` when you need hard-coded rates instead of automatic calculation. **Stripe Tax is recommended** for most integrations.

- **TaxRate object**: `display_name`, `inclusive`, `percentage` (required); `country`, `state`, `jurisdiction` (optional); `percentage`/`country`/`state` are **immutable** — archive + create new to change
- **Fixed rates**: `line_items.tax_rates` (payment) or `subscription_data.default_tax_rates` (subscription)
- **Dynamic rates**: `line_items.dynamic_tax_rates` — Stripe matches customer shipping/billing address to rate; 30 supported countries (EU + AU + US); billing address auto-collected
- `tax_rates` and `dynamic_tax_rates` are **mutually exclusive** per line item
- Apple Pay + Google Pay disabled with dynamic rates unless `shipping_address_collection` is set
- **Tax reporting**: Dashboard exports; payment mode needs 2 exports (line item + totals); subscription mode uses Stripe Billing exports

## Sources

- [[source-stripe-checkout-taxes]] — Stripe Tax + Checkout: automatic_tax param, new/existing customer flows, Accounts v2 + Customers v1, customer_update, wallet constraints
- [[source-stripe-checkout-shipping]] — Shipping tax: `tax_code: 'txcd_92010001'` for ShippingRate objects
- [[source-stripe-checkout-manual-tax-rates]] — Manual Tax Rates: TaxRate API, fixed + dynamic rates, 30-country list, wallet constraints, Dashboard reporting exports
- [[source-stripe-checkout-collect-taxes]] — Comprehensive tax guide: CS automatic_tax + Tax ID Element + real-time verification; PI Tax API (calculate/record/reverse), 100+ tax ID types
- [[source-stripe-billing-taxes-collect]] — Billing tax guide: Stripe Tax + Tax Rates for subscriptions, Elements without Intent flow, address validation, invoice.finalization_failed webhook, Credit Note refunds
- [[source-stripe-billing-customer-tax-ids]] — Customer Tax IDs: 130+ types, "Impact in Tax Calculation" flag (reverse charge), AU/EU/GB auto-validation, VIES tooltip, 3 test magic IDs
- [[source-stripe-billing-taxes-migration]] — migrating subscriptions to Stripe Tax: automated tooling + manual steps, tax_behavior immutability, schedule approach to avoid prorations
