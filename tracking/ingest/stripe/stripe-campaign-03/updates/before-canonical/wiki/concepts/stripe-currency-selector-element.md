---
title: "Stripe Currency Selector Element"
type: concept
category: technology
tags: [stripe, elements, currency-selector, adaptive-pricing, checkout-sessions, localization]
---

## Definition

The Currency Selector Element is a Stripe UI component that presents a currency toggle on the checkout page, allowing customers to pay in their local currency via Adaptive Pricing. It is **exclusively available with the Checkout Sessions API** — not compatible with the Payment Intents API.

## API Constraint

> Only works with Checkout Sessions API (`ui_mode: 'elements'` + `initCheckoutElementsSdk`).

To display currency options on this Checkout Sessions Elements path, the November 2026 guide says to enable Adaptive Pricing, set `adaptivePricing.allowed` to `true` **in the Checkout Session**, and use an integration or price currency eligible for settlement by the merchant of record. The April capture already restricted the selector to Checkout Sessions; these new display prerequisites do not imply PaymentIntents support or account-specific eligibility. See [[source-stripe-currency-selector-element]] (https://docs.stripe.com/elements/currency-selector-element; April `raw/stripe-currency-selector-element-2025.md:8-10`; November `raw/stripe-elements-currency-selector-element-2026-11-07.md:11-21`).

Initialized from the checkout instance, not from `elements.create(...)`:

```js
const checkout = stripe.initCheckoutElementsSdk({ clientSecret, elementsOptions });
const currencySelectorElement = checkout.createCurrencySelectorElement();
currencySelectorElement.mount('#currency-selector-element');
```

## Stripe rendering instruction and price-localization law

Stripe says merchants using Adaptive Pricing with Elements **must render** the Currency Selector Element. Separately, merchants are responsible for complying with applicable price-localization laws in their and their customers' regions; the captured page does not say a law itself mandates this particular Element. Stripe recommends legal advice specific to the business. See [[source-stripe-currency-selector-element]] (https://docs.stripe.com/elements/currency-selector-element; April `raw/stripe-currency-selector-element-2025.md:14`; November `raw/stripe-elements-currency-selector-element-2026-11-07.md:25`).

## Appearance

Uses the Appearance API. The `.ToggleItem` rule controls toggle button styling:

```js
const appearance = {
  theme: 'flat',
  rules: {
    '.ToggleItem': { backgroundColor: '#000000', color: '#ffffff' }
  }
};
```

![Currency Selector Element appearance variations](../raw/assets/stripe-currency-selector-element-appearance.png)

## Placement Best Practices

Currency selection might affect which payment methods are available, so placement matters:

| Scenario | Recommended placement |
| --- | --- |
| Payment Element visible on load | Directly above Payment Element |
| Card-only integration | Above or below Payment Element |
| Payment Element below the fold | Near the total price display |
| Express Checkout Element in use | Above the Express Checkout Element |

## Relationship to Adaptive Pricing

The Currency Selector Element is the UI surface for [[stripe-adaptive-pricing]]. Adaptive Pricing handles the actual currency conversion and local pricing logic; the Currency Selector Element exposes the customer-facing toggle.

## Key Players

- [[stripe]] — the sole provider of this element

## Sources

- [[source-stripe-currency-selector-element]] — April and November 2026 guide for Checkout Sessions eligibility, November display prerequisites, Appearance API, placement advice, Stripe's must-render instruction, and separate price-localization-law responsibility
- [[source-stripe-adaptive-pricing]] — Adaptive Pricing mechanics that power this element
