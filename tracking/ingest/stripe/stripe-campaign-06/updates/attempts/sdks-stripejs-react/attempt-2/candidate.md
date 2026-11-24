---
title: "Stripe Docs — React Stripe.js reference"
type: source
date_ingested: 2026-05-08
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/sdks/stripejs-react"
raw_files:
  - "stripe-react-stripejs-2025.md"
tags: [stripe, react, stripe-elements, checkout-elements-provider, elements-provider, usestripe, useelements, elementsconsumer]
---

## Summary

The 2026-05-08 React Stripe.js reference contains both integration paths: Checkout Sessions (`CheckoutElementsProvider`) and advanced integration with Payment Intents (the standard `Elements` provider). It documents loading Stripe.js asynchronously with a publishable key via `loadStripe`, then passing the resulting promise to the provider. See the raw for the prop tables, hooks, and class component examples.

## Two Integration Paths

### Checkout Sessions (`@stripe/react-stripe-js/checkout`)

| API | Purpose |
| --- | --- |
| `CheckoutElementsProvider` | Root provider that accepts `stripe`. Pass the created Checkout Session's client secret in the provider's `options.clientSecret`. |
| `useCheckoutElements()` | Returns a loading, error, or success state. Only success supplies `checkout`. |
| `checkout.confirm()` | Confirms the Checkout Session in the successful hook branch after loading and error handling. |
| `onReady`, `onChange`, etc. | Element event props. |

Available elements: BillingAddressElement, CurrencySelectorElement, ExpressCheckoutElement, PaymentElement, PaymentMethodMessagingElement, ShippingAddressElement, TaxIdElement.

Use `useCheckoutForm()` inside `CheckoutFormProvider`. The 2026-05-08 reference directs pre-v6 users to `useCheckout()`. The retained package history identifies it as an alias deprecated since 6.3.0 and still implemented and exported from `/checkout` in the pinned 7.0.0 snapshot. See [[source-github-react-stripe-js]].

### Payment Intents (`@stripe/react-stripe-js`)

| API | Purpose |
| --- | --- |
| `Elements` | Root provider. When rendering the Payment Element, supply the Intent's `clientSecret` unless rendering before creating the Intent. |
| `useStripe()` | Stripe instance, initially null if a Stripe promise is unresolved. |
| `useElements()` | Elements instance, initially null if a Stripe promise is unresolved. Use `elements.getElement(Component)` for imperative access in this path. |
| `ElementsConsumer` | Class component alternative with `({ stripe, elements }) => ...` render props. |

Available elements: AddressElement, ExpressCheckoutElement, LinkAuthenticationElement, PaymentElement, PaymentMethodMessagingElement, TaxIdElement.

The advanced confirmation example waits for both `stripe` and `elements` before calling `stripe.confirmPayment`.

## Key Rules

- Both providers document setting the `stripe` prop once. Initial server-side rendering or static generation can pass `null` or a promise resolving to `null`.
- The 2026-05-08 advanced reference describes the standard `Elements` provider's `options` prop as immutable after setup and directs appearance changes through `elements.update()`.
- The UMD instructions require Stripe.js to load directly from `js.stripe.com` and prohibit self-hosting or bundling the script.
- The Checkout path's imperative example captures an Element through `onReady`. The advanced path's example retrieves it through `elements.getElement(...)`.
- Mount at most one of each Element type per provider.

> [!warning] 2026-05-08 website reference and retained 6.8.0 implementation
> The 2026-05-08 advanced website reference describes blanket `Elements.options` immutability. The retained `@stripe/react-stripe-js@6.8.0` implementation in [[source-github-react-stripe-js]] treats `clientSecret` and `fonts` as immutable and forwards other changed provider options through `elements.update()`.

## Related Pages

- [[stripe-elements]] — Stripe Elements concept page
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-react-stripejs-2025]] — 2026-05-08 complete two-variant website capture (673 lines with prop tables reformatted by linter)

## Related raw API references

- [[raw/stripe-sdks-stripejs-react-2026-11-07|2026-11-07 React Stripe.js reference index]] — navigation to [Elements](https://docs.stripe.com/sdks/stripejs-react.md?ui=embedded-components) and [Advanced integration](https://docs.stripe.com/sdks/stripejs-react.md?ui=elements). The capture contains the index only.
