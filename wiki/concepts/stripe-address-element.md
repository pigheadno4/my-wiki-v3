---
title: "Stripe Address Element"
type: concept
category: technology
tags: [stripe, elements, address-element, shipping, billing, autocomplete, link, appearance-api]
---

## Definition

The Address Element is a Stripe UI component for collecting complete billing or shipping addresses. It supports 236 regional address formats (including right-to-left), built-in address autocomplete for 26 countries, and automatic data routing into PaymentIntent fields when combined with other Elements.

## Modes

| Mode | What it collects | PaymentIntent field |
| --- | --- | --- |
| `shipping` | Shipping address + optional reuse as billing | `shipping`; optionally also `billing_details` |
| `billing` | Billing address only | `billing_details` |

```js
// Shipping mode
elements.create('address', { mode: 'shipping' });

// Billing mode
elements.create('address', { mode: 'billing' });
```

In shipping mode, the customer can opt to use their shipping address as billing — if they do, it populates both fields automatically.

## Automatic PaymentIntent Routing

When Address Element, Payment Element, and/or Express Checkout Element all share the **same `Elements` instance**, Stripe automatically combines the address with the payment method into the correct PaymentIntent fields on confirmation. No manual data extraction needed.

```js
const elements = stripe.elements({ clientSecret });
const addressElement = elements.create('address', { mode: 'shipping' });
const paymentElement = elements.create('payment', { layout: 'accordion' });
// confirmPayment combines both automatically
```

Validation runs on confirmation — inline field errors display automatically.

## Collecting Both Shipping and Billing

Two options:
1. **Two Address Elements**: one in `shipping` mode + one in `billing` mode
2. **One Address Element + Payment Element**: use shipping mode for the Address Element; Payment Element handles the minimal billing details it needs

## Autocomplete

Built-in address autocomplete for 26 countries: AU, BE, BR, CA, CH, DE, ES, FR, GB, IE, IN, IT, JP, MX, MY, NL, NO, NZ, PH, PL, RU, SE, SG, TR, US, ZA

- **With Payment Element**: enabled automatically via Stripe's Google Maps API key
- **Standalone**: requires your own Google Maps Places Library key via `autocomplete.apiKey`
- Must comply with Google Maps Platform Acceptable Use Policy

## Link Autofill

When `linkAuthentication`, `address`, and `payment` elements all share the same `Elements` instance, returning Link customers get their saved shipping info autofilled on authentication.

## API Path Differences

The Address Element API differs between the Checkout Sessions and Payment Intents paths:

| | Checkout Sessions | Payment Intents |
| --- | --- | --- |
| Create billing | `checkout.createBillingAddressElement()` | `elements.create('address', { mode: 'billing' })` |
| Create shipping | `checkout.createShippingAddressElement()` | `elements.create('address', { mode: 'shipping' })` |
| React billing | `<BillingAddressElement>` from `@stripe/react-stripe-js/checkout` | `<AddressElement options={{mode:'billing'}}>` |
| React shipping | `<ShippingAddressElement>` from `@stripe/react-stripe-js/checkout` | `<AddressElement options={{mode:'shipping'}}>` |

### Checkout Sessions: Sync Address Checkbox

When using both billing and shipping Address Elements, enable a checkbox to let customers sync them:

```js
elementsOptions: { syncAddressCheckbox: 'shipping' } // 'billing'(default) | 'shipping' | 'none'
```

### Checkout Sessions: Programmatic Prefill

```js
actions.updateBillingAddress({ name: 'Jane Doe', address: { line1: '...', country: 'US' } });
actions.updateShippingAddress({ ... });
```

## Retrieving Address Value (Payment Intents Path)

### Imperative: `getValue()`

```js
const { complete, value } = await addressElement.getValue();
if (complete) { /* use value.address */ }
```

For **multi-page flows**: retrieve address before moving to the next step, then manually update the PaymentIntent or Customer object with the address details.

## Key Options

| Option | Description |
| --- | --- |
| `mode` | `'shipping'` or `'billing'` — required (Payment Intents path) |
| `fields.phone` | Collect phone number alongside address |
| `autocomplete` / `autocomplete.apiKey` | Enable autocomplete; own key with `mode: 'google_maps_api'` |
| `contacts` | Allow customer to pick from saved contacts |
| `allowedCountries` | Restrict to specific countries |
| `blockPoBox` | Reject PO box addresses (`true`/`false`) |
| `validation.phone.required` | Set phone requirement (`'always'`/`'never'`/`'auto'`) |

## Autocomplete Details

- **Auto-enabled** (Stripe's key): when paired with Payment Element or in an active Link session
- **Own Google Maps key**: pass `autocomplete: { mode: 'google_maps_api', apiKey: '...' }` for all other scenarios
- **CSP requirement** when using own key: add `https://maps.googleapis.com` to `connect-src` and `script-src`

## Validation

- **Single-page + PaymentIntent**: `stripe.confirmPayment()` triggers automatic validation + inline errors
- **Multi-page**: call `addressElement.getValue()` to trigger inline field validation before moving to next step

## API Compatibility

Works with both the Checkout Sessions API and the Payment Intents API (Advanced integration).

## Appearance

Uses the Appearance API — same theming system as Payment Element and Express Checkout Element. Example: flat theme with custom primary text color.

## Key Players

- [[stripe]] — the sole provider of this element

## Sources

- [[source-stripe-address-element]] — primary reference: modes, autocomplete, Link autofill, combining with other elements
- [[source-stripe-collect-addresses]] — full integration guide: Checkout Sessions vs Payment Intents API differences, syncAddressCheckbox, getValue(), blockPoBox, multi-page flow, CSP for own Maps key
- [[source-stripe-inapp-collect-addresses]] — mobile integration: iOS UIKit (AddressViewController), iOS SwiftUI, Android (AddressLauncher + Google Places), React Native (AddressSheet); distinct APIs from web variant
