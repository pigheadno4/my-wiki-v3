---
title: "Adaptive Pricing — Elements Integration Guide"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-adaptive-pricing-elements-2025.md"
tags: [stripe, adaptive-pricing, checkout-sessions, currency-selector, localization, elements, local-payment-methods]
---

## Summary

Full integration guide for Adaptive Pricing with Elements (Checkout Sessions API only). Key new content vs existing [[source-stripe-adaptive-pricing]]: the `adaptivePricing.allowed: true` SDK flag required to enable, React `CurrencySelectorElement` component, and `currencyOptions` guard pattern.

## Key Integration Steps

1. Enable Adaptive Pricing in Dashboard (Payments settings → Adaptive Pricing)
2. Display `session.total.total.amount` (pre-formatted) in your UI
3. Mount Currency Selector Element (`checkout.createCurrencySelectorElement()` or `<CurrencySelectorElement />`)
4. Set `adaptivePricing: { allowed: true }` in `initCheckoutElementsSdk` options

```js
const checkout = stripe.initCheckoutElementsSdk({
  clientSecret,
  adaptivePricing: { allowed: true },  // REQUIRED to activate
});
```

React:
```jsx
<CheckoutElementsProvider options={{ clientSecret, adaptivePricing: { allowed: true } }}>
```

After this flag is set, manage Adaptive Pricing via Dashboard or `adaptive_pricing.enabled` per session.

## Currency Selector Element

```js
// HTML+JS
const currencySelectorElement = checkout.createCurrencySelectorElement();
currencySelectorElement.mount('#currency-selector');

// React
import {CurrencySelectorElement} from '@stripe/react-stripe-js/checkout';
<CurrencySelectorElement />
```

Guard: if `currencyOptions` is empty, mounting the element renders nothing — safe to always mount.

![Currency Selector placement above Payment Element](../raw/assets/stripe-adaptive-pricing-currency-selector-placement.png)

## Local Payment Methods Unlocked (20)

Amazon Pay, Bancontact, BLIK, EPS, iDEAL, Link, P24, Pix, South Korean cards, MB WAY, Naver Pay, Kakao Pay, PAYCO, PayPal, Revolut Pay, Samsung Pay, TWINT, WeChat Pay, Klarna (EU+UK only), UPI

> Cross-border subscriptions: only card, Link, Apple Pay, Google Pay supported.

## Restrictions (All)

- Payment Intents API: not supported
- Indian businesses: not supported
- `capture_method: 'manual'`: Adaptive Pricing disabled for that session
- Custom amounts: disabled
- Price already has `currency_options` for that currency: AP won't convert to it (but can still convert to others)
- Integration currency must be a settlement currency

## Testing

```js
// Simulate French customer
stripe.checkout.sessions.create({
  customer_email: 'test+location_FR@example.com',
  // ...
});
// Any +location_XX suffix works; XX = ISO country code
```

## Supported: 150+ Countries

Full list in raw file organized by region (North America, South America, Europe, Asia, Oceania, Africa).

## Pricing & Refunds

- Merchant: 0% fee
- Customer: 2–4% conversion fee (built into presented exchange rate)
- Rate guaranteed 24 hours (mid-market + fee)
- Refunds: merchant refunds in integration currency → customer refunded in local currency at original exchange rate

## Related Pages

- [[stripe-adaptive-pricing]] — concept page
- [[source-stripe-adaptive-pricing]] — earlier source (Checkout-hosted path)
- [[stripe-currency-selector-element]] — Currency Selector Element concept page

## Raw Sources

- [[stripe-adaptive-pricing-elements-2025]] — verbatim Elements integration guide
