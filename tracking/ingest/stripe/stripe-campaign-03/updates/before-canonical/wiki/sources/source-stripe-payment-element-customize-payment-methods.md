---
title: "Customize Payment Methods in the Payment Element"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-payment-element-customize-payment-methods-2025.md"
tags: [stripe, payment-element, payment-methods, dynamic-payment-methods, paymentMethodOrder, accordion, finland, sweden]
---

## Summary

Reference guide for customizing how the Payment Element displays payment methods. Three customization axes: which methods to enable, their sort order, and how many to show in accordion layout.

## Key Facts

- **Auto-hide**: Payment Element always hides methods unsupported for the current transaction (wrong currency, wrong payment type) — regardless of your configuration
- **Dynamic methods (default)**: Stripe pulls preferences from Dashboard, applies ML-based ordering for conversion
- **Manual override**: pass `payment_method_types` on the Intent to list methods explicitly

## Sort Order: `paymentMethodOrder`

```js
elements.create('payment', {
  paymentMethodOrder: ['apple_pay', 'google_pay', 'card', 'klarna']
});
```

- Specified methods appear first; remaining methods get dynamic ordering applied
- `apple_pay` and `google_pay` are valid values (in addition to standard payment method type strings)
- Methods specified but not available are silently ignored

> **Finland & Sweden regulation**: debit payment methods must appear before credit payment methods at checkout.

## Accordion Count: `visibleAccordionItemsCount`

```js
elements.create('payment', {
  layout: { type: 'accordion', visibleAccordionItemsCount: 3 }
});
```

- Accordion layout default: 5 visible, rest hidden behind "More" button
- Set to `0` to disable "More" button and show all available methods

## Related Pages

- [[source-stripe-payment-element]] — primary Payment Element source
- [[stripe-elements]] — parent Elements framework

## Raw Sources

- [[stripe-payment-element-customize-payment-methods-2025]] — verbatim customization reference
