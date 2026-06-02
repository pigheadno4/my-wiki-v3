---
title: "Stripe Link Authentication Element"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-link-authentication-element-2025.md"
tags: [stripe, elements, link, link-authentication-element, autofill, email, appearance-api]
---

## Summary

The Link Authentication Element is a single email input field that serves dual purposes: collecting the customer's email address and triggering Link authentication for returning customers. When a returning Link user enters their email, Stripe autofills their saved payment and shipping details.

## Key Takeaways

- **Dual-purpose**: one field for email collection + Link authentication
- **`loader: 'auto'`**: pass on the Elements instance for skeleton loader UI (best practice)
- **`onChange` event**: fires on input and on Link autofill — use to extract `event.value.email`
- **`defaultValues.email`**: prefilling email starts Link auth flow immediately on page load
- **Prefill billing details**: pass `defaultValues.billingDetails` on the **Payment Element** (not LAE) for name/phone/address
- **Domain registration required** before use

## Initialization

```js
const elements = stripe.elements({ clientSecret, loader: 'auto' });
const linkAuthenticationElement = elements.create('linkAuthentication');
linkAuthenticationElement.mount('#link-authentication-element');
```

React: `<LinkAuthenticationElement />` from `@stripe/react-stripe-js` inside `<Elements>` provider.

## Retrieve Email

```js
linkAuthenticationElement.on('change', (event) => {
  const email = event.value.email;
});
```

Fires on every keystroke and when Link autofills a saved email.

## Prefill Data

```js
// Start Link auth flow immediately on page load
elements.create('linkAuthentication', { defaultValues: { email: 'foo@bar.com' } });

// Prefill billing details (on Payment Element, not LAE)
elements.create('payment', {
  defaultValues: {
    billingDetails: { name: 'John Doe', phone: '888-888-8888', address: { postal_code: '10001', country: 'US' } }
  }
});
```

Prefilling billing details on the Payment Element simplifies Link account creation and reuse for returning customers.

## Combining with Other Elements

The Link Authentication Element only interacts with the Payment Element (triggers Link autofill). Can be displayed alongside any other elements. Typical combination:

![LAE + Address Element + Payment Element checkout layout](../raw/assets/stripe-link-authentication-element-with-ae-pe.png)

All elements must share the same `Elements` instance for Link autofill to work.

## Appearance

Uses the Appearance API — same theming as other Elements.

![Elements appearance light/dark example](../raw/assets/stripe-elements-appearance-example.png)

## Related Pages

- [[stripe-link-authentication-element]] — concept page
- [[stripe-elements]] — parent Elements framework
- [[stripe-address-element]] — commonly combined with LAE
- [[stripe]] — company page

## Raw Sources

- [[stripe-link-authentication-element-2025]] — verbatim Stripe docs webpage
