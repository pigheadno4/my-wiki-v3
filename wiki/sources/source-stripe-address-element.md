---
title: "Stripe Address Element"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-address-element-2025.md"
tags: [stripe, elements, address-element, shipping, billing, autocomplete, link, appearance-api]
---

## Summary

The Address Element is a Stripe embeddable UI component for collecting complete billing or shipping addresses. It integrates seamlessly with the Payment Element and Express Checkout Element — when all elements share the same `Elements` instance, Stripe automatically routes address data into the correct PaymentIntent fields.

## Key Takeaways

- **Two modes**: `shipping` (collects shipping address + optional reuse as billing) and `billing` (billing only)
- **Automatic PaymentIntent routing**: shipping mode → `shipping` field; billing mode → `billing_details`
- **Works with both APIs**: Checkout Sessions API and Payment Intents API
- **236 regional address formats** supported, including right-to-left formats
- **Autocomplete**: 26 countries; uses Stripe's Google Maps key when paired with Payment Element; requires your own key standalone
- **Link autofill**: returning Link customers get shipping info autofilled on authentication

## Modes

### Shipping Mode

```js
const addressElement = elements.create('address', { mode: 'shipping' });
```

- Collects shipping address
- Offers customer the option to use it as billing address too
- Shipping address → `PaymentIntent.shipping`; if billing opted in → also `PaymentIntent.payment_method_data.billing_details`

### Billing Mode

```js
const addressElement = elements.create('address', { mode: 'billing' });
```

- Collects billing address only
- → `PaymentIntent.payment_method_data.billing_details`

## Combining with Other Elements

All elements must be created from the **same `Elements` instance** for automatic data combining to work:

```js
const elements = stripe.elements({ clientSecret });
const addressElement = elements.create('address', { mode: 'shipping' });
const paymentElement = elements.create('payment', { layout: 'accordion' });
// Both mount separately; Stripe combines on confirmPayment
```

Options for collecting both shipping and billing:
1. Use two Address Elements (one per mode)
2. Use Address Element in shipping mode + Payment Element (which collects minimal billing details itself)

Validation runs automatically on PaymentIntent/SetupIntent confirmation; field errors display inline.

## Autocomplete

Supported countries (26): AU, BE, BR, CA, CH, DE, ES, FR, GB, IE, IN, IT, JP, MX, MY, NL, NO, NZ, PH, PL, RU, SE, SG, TR, US, ZA

- **With Payment Element**: autocomplete enabled automatically via Stripe's Google Maps API key (no config)
- **Standalone**: must pass your own Google Maps Places Library key via `autocomplete.apiKey` option
- Usage requires compliance with Google Maps Platform Acceptable Use Policy

## Link Autofill

When `linkAuthentication`, `address`, and `payment` elements all share the same `Elements` instance, returning Link customers get shipping info autofilled on authentication.

![Address Element with Link autofill](../raw/assets/stripe-address-element-link-with-elements.png)

## Options Reference

| Option | Description |
| --- | --- |
| `mode` | `'shipping'` or `'billing'` — required |
| `fields.phone` | Enable phone number collection |
| `autocomplete` | Enable address autocomplete; `autocomplete.apiKey` for standalone use |
| `contacts` | Enable saved contacts for address selection |

## Appearance

Uses the Appearance API for theming. Example — flat theme with custom text color:

```js
const appearance = { theme: 'flat', variables: { colorPrimaryText: '#262626' } };
const elements = stripe.elements({ clientSecret, appearance });
```

![Address Element appearance example](../raw/assets/stripe-address-element-appearance-example.png)

Full theme/variable list in Appearance API docs (Checkout Sessions or Advanced integration).

## Related Pages

- [[stripe-address-element]] — concept page
- [[stripe-elements]] — parent Elements framework
- [[stripe-express-checkout-element]] — works with Address Element automatically
- [[stripe]] — company page

## Raw Sources

- [[stripe-address-element-2025]] — verbatim Stripe docs webpage
