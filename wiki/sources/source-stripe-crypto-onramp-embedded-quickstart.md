---
title: "Stripe — Crypto Onramp: Embedded Quickstart"
type: source
date_ingested: 2026-05-11
original_format: notes
raw_files:
  - "stripe-crypto-onramp-embedded-quickstart-2026.md"
tags: [stripe, crypto, onramp, embedded, react, node, fiat-to-crypto, session-api]
---

## Summary

Full working integration guide for the embedded onramp: Node.js/Express server, React client with custom `CryptoElements`/`OnrampElement` components, dark mode, and session state callbacks.

## Server Side

Custom extension to official Stripe library (limited beta — not built-in):

```js
const OnrampSessionResource = Stripe.StripeResource.extend({
  create: Stripe.StripeResource.method({ method: 'POST', path: 'crypto/onramp_sessions' }),
});
```

`POST /create-onramp-session` requires: `destination_currency`, `destination_exchange_amount`, `destination_network`, `customer_ip_address` → returns `{ clientSecret }`.

## Client Side

**Packages**: `@stripe/crypto`, `@stripe/stripe-js`

```js
const stripeOnrampPromise = loadStripeOnramp(publishableKey);
// In OnrampElement component:
stripeOnramp.createSession({ clientSecret, appearance: { theme: 'dark' } }).mount(containerRef);
```

**Custom React components needed** (not yet released as npm module):
- `CryptoElements` — React context provider wrapping `stripeOnrampPromise`
- `OnrampElement` — mounts onramp iframe, wires session events

**Events**:
- `onramp_ui_loaded` → `onReady` prop
- `onramp_session_updated` → `onChange` prop (payload includes `session.status`)

## Sandbox Test Values

```js
destination_currency: 'usdc'
destination_exchange_amount: '13.37'
destination_network: 'ethereum'
```

## Related Pages

- [[stripe-crypto-onramp]] — concept page (updated with implementation details)
- [[source-stripe-crypto-onramp-embedded]] — embedded overview

## Raw Sources

- [[stripe-crypto-onramp-embedded-quickstart-2026]] — verbatim embedded quickstart guide
