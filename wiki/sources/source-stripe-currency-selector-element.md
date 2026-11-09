---
title: "Stripe Currency Selector Element"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/elements/currency-selector-element"
raw_files:
  - "stripe-elements-currency-selector-element-2026-11-07.md"
  - "stripe-currency-selector-element-2025.md"
tags: [stripe, elements, currency-selector, adaptive-pricing, checkout-sessions, localization]
---

## Summary

The Currency Selector Element is an embeddable UI toggle for presenting Adaptive Pricing currency options to customers. The captured page restricts configuring Adaptive Pricing and this Element to **Elements with the Checkout Sessions API**; it does not establish a PaymentIntents integration path or account-specific eligibility. The November capture adds explicit prerequisites for displaying currency options. See [[stripe-currency-selector-element]]. [April capture](../../raw/stripe-currency-selector-element-2025.md#L4-L14); [November capture](../../raw/stripe-elements-currency-selector-element-2026-11-07.md#L5-L25)

## Eligibility and display prerequisites

- The Checkout Sessions API restriction is present in both captures. The November guide says currency options require Adaptive Pricing enabled, `adaptivePricing.allowed` set to `true` **in the Checkout Session**, and an integration or price currency eligible for settlement by the **merchant of record**. These are session and currency prerequisites on this integration path, not an account-wide flag or proof of available options for a particular customer. [April capture](../../raw/stripe-currency-selector-element-2025.md#L8-L10); [November capture](../../raw/stripe-elements-currency-selector-element-2026-11-07.md#L11-L21)
- Stripe says merchants are responsible for compliance with laws applicable to price localization in their or customers' regions. Separately, Stripe says the Currency Selector Element **must be rendered** when using Adaptive Pricing with Elements and recommends business-specific legal advice. The capture does not state that a law itself mandates rendering this particular Element. [April capture](../../raw/stripe-currency-selector-element-2025.md#L14); [November capture](../../raw/stripe-elements-currency-selector-element-2026-11-07.md#L25)

## Initialization and appearance

The documented example initializes the Checkout Elements SDK with `clientSecret` and `elementsOptions`, creates the selector from the `checkout` instance with `checkout.createCurrencySelectorElement()`, and mounts it. It uses the Appearance API with a `flat` theme and `.ToggleItem` styling. This is a captured example, not evidence of a successful runtime checkout. [April capture](../../raw/stripe-currency-selector-element-2025.md#L16-L42); [November capture](../../raw/stripe-elements-currency-selector-element-2026-11-07.md#L27-L53)

```js
const checkout = stripe.initCheckoutElementsSdk({ clientSecret, elementsOptions });
const currencySelectorElement = checkout.createCurrencySelectorElement();
currencySelectorElement.mount('#currency-selector-element');
```

## Placement best practices

The page recommends positioning the selector near payment details, ideally directly above the Payment Element, because the selected currency might affect available payment methods. A card-only flow can place it below the Payment Element; if that Element is not initially visible, place the selector near the total. With Express Checkout Element, place the selector above it so customers see the charge currency. Apply placement across screen sizes. These are design recommendations, not universal placement requirements or a guarantee of payment-method availability. [April capture](../../raw/stripe-currency-selector-element-2025.md#L44-L53); [November capture](../../raw/stripe-elements-currency-selector-element-2026-11-07.md#L55-L64)

## Related Pages

- [[stripe-currency-selector-element]] — concept and reciprocal source route
- [[stripe-adaptive-pricing]] — underlying pricing mechanism
- [[stripe-elements]] — parent Elements framework
- [[stripe]] — company page

## Raw Sources

- [[raw/stripe-elements-currency-selector-element-2026-11-07|November 7, 2026 Currency Selector capture]] — verbatim webpage content (64 lines)
- [[raw/stripe-currency-selector-element-2025|April 21, 2026 Currency Selector capture]] — historical webpage content (53 lines; appearance image)
