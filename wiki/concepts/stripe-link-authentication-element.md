---
title: "Stripe Link Authentication Element"
type: concept
category: technology
tags: [stripe, elements, link, link-authentication-element, autofill, email, appearance-api]
---

## Definition

The Link Authentication Element is a single email input field that serves two purposes simultaneously: collecting the customer's email address and triggering Link authentication for returning Link users. When a returning customer enters their email, Stripe autofills their saved payment and shipping details.

## How It Works

1. Customer types their email into the Link Authentication Element
2. If Stripe recognizes the email as a Link account, authentication is triggered
3. On successful authentication, Link autofills the customer's saved payment and shipping info into the Payment Element and Address Element (if present)

## Initialization

```js
// loader: 'auto' enables skeleton loader — best practice
const elements = stripe.elements({ clientSecret, loader: 'auto' });
const linkAuthenticationElement = elements.create('linkAuthentication');
linkAuthenticationElement.mount('#link-authentication-element');
```

React: `<LinkAuthenticationElement />` from `@stripe/react-stripe-js` inside an `<Elements>` provider.

All elements must share the **same `Elements` instance** for Link autofill to work across elements.

## Key Behaviors

### Retrieve Email

```js
linkAuthenticationElement.on('change', (event) => {
  const email = event.value.email;
});
```

Fires on every keystroke AND when Link autofills a saved email — useful for capturing email before payment confirmation.

### Prefill Email (Start Auth on Load)

```js
elements.create('linkAuthentication', { defaultValues: { email: 'customer@example.com' } });
```

Prefilling email starts the Link authentication flow immediately when the page loads — reduces friction for returning customers.

### Prefill Billing Details

Additional customer data (name, phone, address) is prefilled via the **Payment Element**, not the Link Authentication Element:

```js
elements.create('payment', {
  defaultValues: {
    billingDetails: { name: 'John Doe', phone: '888-888-8888', address: { postal_code: '10001', country: 'US' } }
  }
});
```

Prefilling as much data as possible simplifies Link account creation and reuse.

## Combining with Other Elements

The Link Authentication Element only directly interacts with the Payment Element (Link autofill). It can be displayed alongside any other elements:

![Link Authentication + Address + Payment Element layout](../raw/assets/stripe-link-authentication-element-with-ae-pe.png)

Typical stack: **Link Authentication Element** → **Address Element** → **Payment Element**

## Integration Notes

- Domain must be registered before use
- Works with both Checkout Sessions API and Payment Intents API
- `loader: 'auto'` on the Elements instance enables skeleton loader UI — recommended for optimal loading UX

## Key Players

- [[stripe]] — the sole provider of this element

## Sources

- [[source-stripe-link-authentication-element]] — primary reference: dual-purpose email/auth, onChange, prefill patterns, combining elements
