---
title: "Manual Currency Prices"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-manual-currency-prices-2025.md"
tags: [stripe, checkout-sessions, currency, manual-currency, currency-options, localization, local-payment-methods]
---

## Summary

Static multi-currency pricing for Checkout Sessions — merchants set exact amounts per currency using `currency_options` on the Price object. Not supported on Payment Intents API. Manual currency prices override Adaptive Pricing for those specific currencies.

## Key Facts

- **Checkout Sessions API only** — not supported on Payment Intents
- **Overrides Adaptive Pricing** for defined currencies; AP still handles undefined currencies
- **Static**: merchant sets exact amounts; no dynamic conversion
- **Default currency must match** across all prices, shipping rates, and discounts
- **Testing**: same `+location_XX` email suffix (e.g. `test+location_FR@example.com`)

## Price Setup

```js
// API
const price = await stripe.prices.create({
  currency: 'usd',
  unit_amount: 1000,
  currency_options: {
    eur: { unit_amount: 950 },
    jpy: { unit_amount: 1500 },
  },
  product_data: { name: 'My Product' },
});

// Dashboard: Product → Add price → +Add a price by currency
```

## Session Behavior

- Auto-detects customer currency from `currency_options` (no `currency` param needed)
- `currency` param on session overrides auto-detection (forces specific currency)
- Local PMs auto-presented: e.g. iDEAL for EUR/Netherlands customers

## Requirements for Auto-Localization

All of the following must be true:
1. All prices, shipping rates, and discounts have `currency_options` for the relevant currency
2. If using Stripe Tax: `tax_behavior` specified for that currency on all items
3. `currency` param NOT set on session creation

If any condition fails → default currency presented.

## Restrictions

- Manual tax rates not supported
- `payment_intent_data.application_fee_amount` or `transfer_data.amount` not supported

## Fees

Standard Stripe transaction fees + international card fee (if applicable) + currency conversion fee.

## Related Pages

- [[source-stripe-checkout-local-currency]] — hub page (all 3 approaches)
- [[stripe-adaptive-pricing]] — recommended alternative (handles 150+ currencies automatically)
- [[stripe-fx-quotes-api]] — alternative with rate control

## Raw Sources

- [[stripe-manual-currency-prices-2025]] — verbatim manual currency prices guide
