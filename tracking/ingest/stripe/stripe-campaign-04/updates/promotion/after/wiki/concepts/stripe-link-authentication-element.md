---
title: "Stripe Link Authentication Element"
type: concept
category: technology
tags: [stripe, elements, link, link-authentication-element, autofill, email, appearance-api]
---

## Definition

Contact Details Element, previously Link Authentication Element, collects an email address and starts Link authentication from one field. In the dated standard Elements flow, a recognized Link email triggers a one-time code to the customer’s phone. Successful authentication allows Stripe to display saved addresses and payment methods. See [[source-stripe-elements-link]].

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

React in the retained `@stripe/react-stripe-js@7.0.0` standard root uses `<LinkAuthenticationElement>` or `<ContactDetailsElement>` inside the `<Elements>` provider for this PaymentIntent client-secret flow. The lowercase JSX printed in the May guide differs from these exports. Standard Stripe.js creation strings are lowercase `linkAuthentication` and `contactDetails`. `LinkSignupElement` is a separate beta export. See [[source-github-react-stripe-js]].

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

In [[source-stripe-add-link-elements-integration|the dated custom PaymentIntent checkout guide]], May 8, 2026 uses this Link Authentication Element stack, with Address Element optional. November 7 setup and shipping use `ContactDetailsElement`. The November React confirmation example still renders `LinkAuthenticationElement`, and the redisplay snippet imports it. These are distinct root bindings in the retained React 7.0.0 source.

## Integration Notes

- Domain must be registered before use
- The May client-secret setup is a standard PaymentIntent Elements flow. The May 27 Dahlia rename retains `linkAuthentication` and `contactDetails` creation strings and preserves the documented behavior for existing integrations.
- The separate May 27 Dahlia change adds Contact Details Element email collection, validation and Link sign-in with Elements and Checkout Sessions at the linked `2026-05-27.dahlia` API version. The prior Checkout Sessions route used a custom email input with `updateEmail`. Checkout’s React entrypoint in the retained 7.0.0 snapshot has its own `ContactDetailsElement` export. See [[source-stripe-elements-link#Contact Details Rename and API Scope]].
- `loader: 'auto'` on the Elements instance enables skeleton loader UI — recommended for optimal loading UX

## Key Players

- [[stripe]] — the sole provider of this element

## Sources

- [[source-stripe-link-authentication-element]] — primary reference: dual-purpose email/auth, onChange, prefill patterns, combining elements
- [[source-stripe-express-checkout-link]] — May 2026 navigation uses Link Authentication Element and the November capture points to Contact Details Element. The May 27 Dahlia rename keeps both standard creation strings. The separate contact field is outside the Express Checkout mount sample.
