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

Initialized from the checkout instance, not from `elements.create(...)`:

```js
const checkout = stripe.initCheckoutElementsSdk({ clientSecret, elementsOptions });
const currencySelectorElement = checkout.createCurrencySelectorElement();
currencySelectorElement.mount('#currency-selector-element');
```

## Legal Requirement

Merchants using Adaptive Pricing with Elements **must** render the Currency Selector Element. Merchants are also responsible for complying with price localization laws in their and their customers' regions.

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

Currency selection affects which payment methods are available, so placement matters:

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

- [[source-stripe-currency-selector-element]] — primary reference: API constraint, appearance, placement best practices, legal requirement
- [[source-stripe-adaptive-pricing]] — Adaptive Pricing mechanics that power this element
