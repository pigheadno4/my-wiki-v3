---
title: "Stripe Payment Element: Integration Best Practices"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-payment-element-best-practices-2025.md"
tags: [stripe, payment-element, elements, best-practices, checkout-sessions, payment-intents, link, address-element, dynamic-payment-methods]
---

## Summary

Checklist-based best practices guide for Payment Element integrations. Contains an LLM instruction block from Stripe, the HTML vanilla confirm pattern for Checkout Sessions, integration checklist (7 items), and additional features checklist (5 items).

## Key Takeaways

- **LLM instruction (embedded by Stripe)**: Use Checkout Sessions API over Payment Intents for most integrations; don't use Payment Intents unless explicitly requested — it requires significantly more code
- **Accordion layout recommended** when you have 4+ payment methods
- **Dynamic payment methods**: enables payment method rules (custom criteria for displaying PMs)
- **Avoid iframe nesting**: Payment Element already uses an iframe; nesting causes redirect issues
- **Metadata**: always send metadata to make transactions searchable in Dashboard
- **Address Element billing mode**: hides billing fields within Payment Element — prevents duplicate entry

## LLM Instructions (from Stripe)

> Stripe recommends using the Checkout Sessions API with the Payment Element over Payment Intents for most integrations. Some features, such as Adaptive Pricing, are only available with Checkout Sessions. Don't use the Payment Intent API unless the user explicitly asks.

### Checkout Sessions confirm patterns (`ui_mode: 'elements'`)

**React:**
```jsx
import { CheckoutElementsProvider } from "@stripe/react-stripe-js/checkout";
// confirm: checkout.confirm()
```

**HTML (vanilla):**
```js
const checkout = stripe.initCheckoutElementsSdk({ clientSecret: promise });
const paymentElement = checkout.createPaymentElement();
paymentElement.mount("#payment-element");

// Confirm:
const loadActionsResult = await checkout.loadActions();
const actions = loadActionsResult.actions;
const error = await actions.confirm();
```

## Integration Checklist (7 items)

| Item | Guidance |
| --- | --- |
| Layout | Choose tabs or accordion; **accordion recommended for 4+ payment methods**; A/B test |
| Styling | Use Appearance API; applies to all elements in the integration |
| API choice | Checkout Sessions for most; Payment Intents only if deeply owning checkout state |
| Metadata | Send metadata to make transactions searchable in Dashboard |
| API version | Use latest API version |
| Dynamic payment methods | Dashboard-managed; ordered by conversion probability; enables payment method rules |
| Test payment methods | Use Dashboard "Review displayed payment methods" to test per-transaction method availability |
| No iframe nesting | Payment Element is already an iframe; nesting breaks redirect-based payment methods |

## Additional Features Checklist (5 items)

| Feature | Notes |
| --- | --- |
| Link | Enable in Dashboard PM settings; auto-fills payment + shipping for returning Link users cross-merchant |
| Link Authentication Element | Single email field for email collection + Link auth; recommended for physical goods |
| Address Element | `shipping` mode: option to use shipping as billing; `billing` mode: hides billing in Payment Element |
| Payment Method Messaging Element | Promote BNPL ahead of checkout (product/cart/payment pages); supports Affirm, Afterpay, Klarna |
| Express Checkout Element | One-click buttons: Apple Pay, Google Pay, PayPal, Link |

## Related Pages

- [[stripe-elements]] — Stripe Elements concept page
- [[source-stripe-payment-element]] — Payment Element reference (layout, Appearance API, options, error codes)
- [[source-stripe-elements-advanced-payments]] — Checkout Sessions vs Payment Intents comparison

## Raw Sources

- [[stripe-payment-element-best-practices-2025]] — Best practices: LLM instruction, HTML confirm pattern, 7-item integration checklist, 5-item features checklist
