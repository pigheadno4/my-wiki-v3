---
title: "Elements with Checkout Sessions API Beta Changelog"
type: source
date_ingested: 2026-04-22
original_format: webpage
raw_files:
  - "stripe-checkout-elements-beta-changelog-2025.md"
tags: [stripe, checkout-sessions, elements, migration, clover, basil, beta-changelog, breaking-changes]
---

## Summary

Migration guide from older beta versions to the stable Clover (latest) and Basil releases of Elements with Checkout Sessions API. Critical reference for developers upgrading from `custom_checkout_beta_*` versions.

> The wiki's current code examples already reflect Clover behavior (`loadActions()`, `@stripe/react-stripe-js/checkout`, `useCheckout()` returning a disjoint union).

> [!warning] Contradiction
> “Latest” is relative to this page's 2026-04-22 collection. The retained `@stripe/stripe-js@9.12.1` source targets `dahlia`, removes `initCheckout()`, and uses `initCheckoutElementsSdk()` for the Elements path. Keep this page as historical Clover migration evidence; use [[source-github-stripe-js]] and [[changelog-github-stripe-js]] for package-qualified v9 behavior.

## Clover (Latest) — Key Breaking Changes

Requires: `@stripe/stripe-js >= 8.0.0`, `@stripe/react-stripe-js >= 5.0.0`, API version `2025-09-30.clover`

### `initCheckout` is now synchronous

```js
// Clover — no await
const checkout = stripe.initCheckout({ clientSecret });
const paymentElement = checkout.createPaymentElement();
paymentElement.mount('#payment-element');
const loadActionsResult = await checkout.loadActions();
if (loadActionsResult.type === 'success') {
  const session = loadActionsResult.actions.getSession();
}
```

- Remove all `await`/`.then()` from `initCheckout` calls
- Replace `fetchClientSecret` function with a client secret string or Promise
- Use `checkout.loadActions()` for async operations (once only)

### React: Import path changes

```jsx
// Before
import {useCheckout, PaymentElement} from '@stripe/react-stripe-js';

// After
import {useCheckout, PaymentElement} from '@stripe/react-stripe-js/checkout';
```

### React: `useCheckout` returns disjoint union

```jsx
const {type, ...rest} = useCheckout();
// type: 'loading' | 'success' | 'error'
// On success: rest.checkout contains session + methods
// No longer throws errors
```

### React: `CheckoutProvider` renders children unconditionally

Previously rendered `null` before `initCheckout` succeeded. Now renders children immediately — enables skeleton loaders.

### Other Clover changes

- Saved PMs auto-enabled when configured on session (no `elementsOptions.savedPaymentMethod` needed)
- Postal codes no longer auto-collected for Canada/UK/Puerto Rico card payments
- `CheckoutProvider` replaces `fetchClientSecret` with `clientSecret` option

## Basil — Key Changes

Requires: `@stripe/stripe-js >= 7.0.0`, `@stripe/react-stripe-js >= 3.6.0`, API version `2025-03-31.basil`

- Async method success: result now under `session` key (was `success` in beta_5)
- `returnUrl` on `confirm` throws error if `return_url` already set on Checkout Session
- Subscription sessions: `subscription` and `invoice` null until session completes (created after payment, not before)
- `discountAmounts.percentOff` added

## Beta Version Method Renames (beta_6)

| Old | New |
| --- | --- |
| `createElement('payment')` | `createPaymentElement()` |
| `createElement('address', {mode: 'billing'})` | `createBillingAddressElement()` |
| `createElement('address', {mode: 'shipping'})` | `createShippingAddressElement()` |
| `createElement('expressCheckout')` | `createExpressCheckoutElement()` |
| `getElement(...)` | `getPaymentElement()` / `getBillingAddressElement()` / etc. |
| `initCustomCheckout` | `initCheckout` (from beta_5) |

## Related Pages

- [[stripe-checkout]] — Checkout concept page
- [[stripe-elements]] — Elements concept page
- [[source-stripe-checkout-elements-quickstart]] — Checkout Elements quickstart

## Raw Sources

- [[stripe-checkout-elements-beta-changelog-2025]] — verbatim beta changelog (290 lines)
