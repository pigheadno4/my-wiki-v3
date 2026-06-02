---
title: "Collect Physical Addresses and Phone Numbers"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-collect-addresses-2025.md"
tags: [stripe, address-element, address-collection, checkout-sessions, payment-intents, autocomplete, billing, shipping, phone, sync]
---

## Summary

Full integration guide for the Address Element across both API paths. The Checkout Sessions path uses separate `createBillingAddressElement()` / `createShippingAddressElement()` methods on the checkout instance. The Payment Intents path uses a single `elements.create('address', { mode })`. Both paths support autocomplete, prefill, and validation.

## API Path Differences

| | Checkout Sessions | Payment Intents |
| --- | --- | --- |
| Create billing element | `checkout.createBillingAddressElement()` | `elements.create('address', { mode: 'billing' })` |
| Create shipping element | `checkout.createShippingAddressElement()` | `elements.create('address', { mode: 'shipping' })` |
| React billing | `<BillingAddressElement>` from `@stripe/react-stripe-js/checkout` | `<AddressElement options={{mode: 'billing'}}>` |
| React shipping | `<ShippingAddressElement>` from `@stripe/react-stripe-js/checkout` | `<AddressElement options={{mode: 'shipping'}}>` |
| Sync checkbox | `syncAddressCheckbox` option | N/A |
| Programmatic prefill | `actions.updateBillingAddress()` / `actions.updateShippingAddress()` | `defaultValues` option on create |
| Retrieve value | `checkout.on('change', event)` | `addressElement.on('change')` + `addressElement.getValue()` |

## Checkout Sessions-Specific Features

### Sync Address Checkbox

When using both billing and shipping elements, show a checkbox to let customers sync them:

```js
checkout = stripe.initCheckoutElementsSdk({
  clientSecret,
  elementsOptions: { syncAddressCheckbox: 'shipping' } // 'billing' | 'shipping' | 'none'
});
```

Default is `'billing'` (checkbox appears on billing element). Set `'shipping'` to show on shipping element. Set `'none'` to hide.

### Programmatic Prefill

```js
actions.updateBillingAddress({ name: 'Jenny Rosen', address: { line1: '27 Fredrick Ave', city: 'Brothers', state: 'OR', postal_code: '97712', country: 'US' } });
```

### Validation

Confirmed automatically when the Checkout Session is confirmed.

## Payment Intents-Specific Features

### Retrieve Address with `getValue()`

```js
const { complete, value } = await addressElement.getValue();
if (complete) { /* use value.address */ }
```

Useful for multi-page flows: retrieve address before navigating to next step, then manually update PaymentIntent or Customer object.

### Multi-Page Flow

In multi-page flows, manually update the PaymentIntent or Customer with address details from `change` event or `getValue()` before moving to the next step.

### Additional Options

```js
elements.create('address', {
  mode: 'shipping',
  allowedCountries: ['US'],
  blockPoBox: true,          // reject PO boxes
  fields: { phone: 'always' },
  validation: { phone: { required: 'never' } },
});
```

### Autocomplete with Own Google Maps Key

When Stripe's auto-provided key isn't available (not paired with Payment Element or Link session):

```js
elements.create('address', {
  mode: 'shipping',
  autocomplete: { mode: 'google_maps_api', apiKey: 'YOUR_KEY' },
});
```

CSP requirement: add `https://maps.googleapis.com` to `connect-src` and `script-src` directives.

### Validation

`stripe.confirmPayment()` / `stripe.confirmSetup()` automatically validates Address Element. For multi-page: call `getValue()` to trigger inline field validation errors.

## Related Pages

- [[stripe-address-element]] — concept page
- [[source-stripe-address-element]] — Address Element overview source

## Raw Sources

- [[stripe-collect-addresses-2025]] — verbatim integration guide (both API paths)
