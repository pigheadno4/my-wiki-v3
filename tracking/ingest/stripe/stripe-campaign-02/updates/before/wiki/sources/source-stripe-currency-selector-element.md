---
title: "Stripe Currency Selector Element"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-currency-selector-element-2025.md"
tags: [stripe, elements, currency-selector, adaptive-pricing, checkout-sessions, localization]
---

## Summary

The Currency Selector Element is a Stripe UI component that displays a currency toggle so customers can pay in their local currency via Adaptive Pricing. It is **Checkout Sessions API only** — not available with the Payment Intents API. Merchants are legally required to render it when using Adaptive Pricing with Elements.

## Key Takeaways

- **API constraint**: only works with Checkout Sessions API (`initCheckoutElementsSdk`)
- **Legal requirement**: must render when using Adaptive Pricing with Elements; must comply with local price localization laws
- **Initialization**: `checkout.createCurrencySelectorElement()` — not `elements.create(...)`
- **Appearance**: uses Appearance API; `.ToggleItem` rule controls the toggle button styling
- **Placement matters**: currency choice affects available payment methods

## Initialization

```js
const checkout = stripe.initCheckoutElementsSdk({ clientSecret, elementsOptions });
const currencySelectorElement = checkout.createCurrencySelectorElement();
currencySelectorElement.mount('#currency-selector-element');
```

Appearance customization via `elementsOptions`:

```js
const appearance = {
  theme: 'flat',
  rules: {
    '.ToggleItem': { backgroundColor: '#000000', color: '#ffffff' }
  }
};
const elementsOptions = { appearance };
```

![Currency Selector Element appearance](../raw/assets/stripe-currency-selector-element-appearance.png)

## Placement Best Practices

| Scenario | Recommended placement |
| --- | --- |
| Payment Element visible on load | Directly above Payment Element |
| Only card payments accepted | Above or below Payment Element |
| Payment Element below the fold / multi-step | Near the total price display |
| Express Checkout Element in use | Above the Express Checkout Element |

Currency selection affects available payment methods — place it where customers can see it before choosing a payment method.

## Related Pages

- [[stripe-currency-selector-element]] — concept page
- [[stripe-adaptive-pricing]] — the underlying pricing mechanism
- [[stripe-elements]] — parent Elements framework
- [[stripe]] — company page

## Raw Sources

- [[stripe-currency-selector-element-2025]] — verbatim Stripe docs webpage
