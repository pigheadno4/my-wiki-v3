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

To display currency options on this Checkout Sessions Elements path, the November Adaptive Pricing configuration section puts client readiness at `adaptivePricing: { allowed: true }` in `initCheckoutElementsSdk` or `CheckoutElementsProvider` options, and uses Dashboard settings or per-Session `adaptive_pricing.enabled` to enable Adaptive Pricing. The integration or price currency must be eligible for settlement by the merchant of record, the customer cross-border, and the currency pair supported. Its troubleshooting bullet says the Checkout Session includes camel-case `adaptivePricing.allowed`, which conflicts with the explicit client versus Session configuration; treat that bullet's field placement as unresolved rather than a separate verified Session recipe. These conditions do not imply Payment Intents support or account-specific eligibility. See [[source-stripe-currency-selector-element]] for the selector guide and [[source-stripe-adaptive-pricing-elements]] for the November configuration (`raw/stripe-payments-custom-localize-prices-adaptive-pricing-2026-11-07.md:108-115,132-164`).

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
