---
title: "Stripe Docs — Explore the Link Authentication Element"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-elements-link-2025.md"
tags: [stripe, link, link-authentication-element, elements, payment-element, react, email, autofill]
---

## Summary

Integration guide for the Link Authentication Element — a single email input that handles both email collection and Link authentication in one component. Covers HTML+JS and React implementations.

## Key Facts

- **Purpose**: email collection + Link authentication trigger in one field
- **Supported PMs for Link signup** (if no existing account): credit card, debit card, US bank account
- **Returning customers**: OTP to phone → autofill of saved addresses + payment methods in Payment Element
- **Page order**: Link Authentication Element → Address Element (optional) → Payment Element
- **Multi-page**: elements can be on separate pages — show Link Auth Element only once per checkout flow
- **Domain registration required**

## Integration

### HTML + JS

```js
const elements = stripe.elements({ clientSecret, loader: 'auto' });
const linkAuthEl = elements.create('linkAuthentication', { defaultValues: { email: 'foo@bar.com' } });
linkAuthEl.mount('#link-authentication-element');
```

### React

Wrap with `<Elements>` + `loader: 'auto'`; use `<linkAuthenticationElement options={{ defaultValues: { email } }} />` inside form.

### Retrieve email via `onChange`

```jsx
<linkAuthenticationElement onChange={(event) => setEmail(event.value.email)} />
```

Fires on both user input and Link autofill.

## CDN Assets

- `raw/assets/stripe-link-authentication-element.png` — checkout page with Link Auth Element (639 KB)

## Related Pages

- [[stripe-link]] — Link concept page (Auth Element section updated)
- [[source-stripe-link-authentication-element]] — earlier source on this component (loader, onChange, prefill)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-elements-link-2025]] — verbatim webpage content (134 lines)
