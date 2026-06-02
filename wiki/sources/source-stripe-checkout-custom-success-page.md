---
title: "Stripe Checkout: Customize Redirect Behavior"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-checkout-custom-success-page-2025.md"
tags: [stripe, checkout, redirect, success-page, return-url, redirect-on-completion, onComplete, embedded]
---

## Summary

Guide for customizing post-payment redirect behavior in Stripe Checkout. Covers the hosted success page pattern, the embedded return page with session status check, and the `redirect_on_completion` param with its 3 modes and `onComplete` callback.

## Key Takeaways

- **Hosted**: `success_url` with `{CHECKOUT_SESSION_ID}` → retrieve session server-side → display order info
- **Embedded**: `return_url` with `{CHECKOUT_SESSION_ID}` → `/session-status` endpoint → handle `complete` vs `open`
- **`redirect_on_completion`** (embedded only): controls when redirect happens; 3 modes
- **`onComplete` callback**: fires on session complete OR `checkout.session.completed` webhook; destroy Checkout instance + render custom success UI

## Hosted Pattern

```js
// Session create
stripe.checkout.sessions.create({
  success_url: 'http://yoursite.com/order/success?session_id={CHECKOUT_SESSION_ID}',
})

// Success page server-side
app.get('/order/success', async (req, res) => {
  const session = await stripe.checkout.sessions.retrieve(req.query.session_id);
  const customer = await stripe.customers.retrieve(session.customer);
  res.send(`Thanks for your order, ${customer.name}!`);
});
```

## Embedded Pattern

`/session-status` endpoint → retrieve session → return `status` + `payment_status` + customer info.

Handle on client:
- `status === 'complete'` → show success page
- `status === 'open'` → remount Checkout (payment failed/canceled)

## `redirect_on_completion` (Embedded Only)

| Value | Behavior | `return_url` required | Notes |
| --- | --- | --- | --- |
| `always` (default) | Always redirect after payment | Yes | Standard embedded flow |
| `if_required` | Only redirect for redirect-based PMs; cards get default success state | Yes | Use `onComplete` for custom card success |
| `never` | No redirects; disables redirect-based PMs | No | Use `onComplete` for success state |

## `onComplete` Callback

```js
// HTML + JS
const checkout = await stripe.createEmbeddedCheckoutPage({
  fetchClientSecret,
  onComplete: async () => {
    checkout.destroy();
    // Retrieve details + show success UI
  }
});

// React
<EmbeddedCheckoutProvider options={{ fetchClientSecret, onComplete: () => setIsComplete(true) }}>
```

Fires when: session completes successfully OR `checkout.session.completed` webhook fires.

## Dynamic Payment Methods with `redirect_on_completion: 'never'`

- Dashboard-managed PMs: redirect-based PMs automatically excluded
- Manual `payment_method_types`: cannot include any redirect-based PMs

## Related Pages

- [[stripe-checkout]] — Stripe Checkout concept page
- [[source-stripe-checkout-fulfillment]] — Fulfillment guide (webhooks required alongside redirects)

## Raw Sources

- [[stripe-checkout-custom-success-page-2025]] — Custom redirect: hosted success page, embedded return page, redirect_on_completion (3 modes), onComplete callback, React + HTML+JS examples
