---
title: "Stripe Docs — React Stripe.js reference"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-react-stripejs-2025.md"
tags: [stripe, react, stripe-elements, checkout-elements-provider, elements-provider, usestripe, useelements, elementsconsumer]
---

## Summary

Full React Stripe.js API reference covering both integration paths: Checkout Sessions (`CheckoutElementsProvider`) and Payment Intents (`Elements` provider). 673 lines including complete prop tables, hooks, and class component support.

## Two Integration Paths

### Checkout Sessions (`@stripe/react-stripe-js/checkout`)

| API | Purpose |
| --- | --- |
| `CheckoutElementsProvider` | Root provider; `stripe` + `options.clientSecret` (from Checkout Session) |
| `useCheckoutElements()` | Returns `{ type, checkout }` — type: `'loading'|'error'|'success'` |
| `checkout.confirm()` | Submits the Checkout Session |
| `onReady`, `onChange`, etc. | Element event props |

Available elements: BillingAddressElement, CurrencySelectorElement, ExpressCheckoutElement, PaymentElement, PaymentMethodMessagingElement, ShippingAddressElement, TaxIdElement

Note: `useCheckoutElements` replaces `useCheckout` from pre-v6.

### Payment Intents (`@stripe/react-stripe-js`)

| API | Purpose |
| --- | --- |
| `<Elements stripe={promise} options={{ clientSecret }}>` | Root provider; `options` immutable after set |
| `useStripe()` | Stripe instance (null until Promise resolves) |
| `useElements()` | Elements instance; `elements.getElement(Component)` for imperative access |
| `ElementsConsumer` | For class components; render props `({ stripe, elements }) => ...` |

Available elements: AddressElement, ExpressCheckoutElement, LinkAuthenticationElement, PaymentElement, PaymentMethodMessagingElement, TaxIdElement

## Key Rules

- `stripe` prop immutable after set
- `options` prop immutable — use `elements.update()` for appearance changes
- Always load Stripe.js from `js.stripe.com` (PCI compliance — never bundle)
- Use `onReady` prop to capture Element instance for imperative methods like `focus()`
- One of each Element type per provider

> [!warning] Contradiction
> The retained `@stripe/react-stripe-js@6.8.0` implementation in [[source-github-react-stripe-js]] treats `clientSecret` and `fonts` as immutable but forwards other changed provider options through `elements.update()`. The broader immutability statement above reflects this source's 2025 documentation snapshot.

## Related Pages

- [[stripe-elements]] — Stripe Elements concept page (React API section added)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-react-stripejs-2025]] — verbatim webpage content (673 lines; prop tables reformatted by linter)
