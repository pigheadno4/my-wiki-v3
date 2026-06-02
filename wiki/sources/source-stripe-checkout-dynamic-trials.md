---
title: "Dynamically Update Trial Durations"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-checkout-dynamic-trials-2025.md"
tags: [stripe, checkout-sessions, subscriptions, trials, dynamic-updates, runServerUpdate, private-preview]
---

## Summary

Private preview feature for dynamically updating trial durations on subscription Checkout Sessions from the server, triggered by client-side actions. Uses the same `runServerUpdate` pattern as dynamic shipping and line items. **Subscription mode only.**

## Key Constraints

- **Private preview** — requires SDK `stripe -v 15.1.0-beta.2` and API version `2025-03-31.preview; checkout_server_update_beta=v1;`
- **Subscription mode only**
- Same `betas: ['custom_checkout_server_updates_1']` client beta flag
- Payment Intents: use the Subscriptions API directly to adjust trial settings

## API Version Setup

```js
const stripe = require('stripe')('SK', {
  apiVersion: '2025-03-31.preview; checkout_server_update_beta=v1;',
});
```

## Server Endpoint Pattern

```js
// Update trial to 14 days for yearly upsell
await stripe.checkout.sessions.update(checkout_session_id, {
  subscription_data: {
    trial_period_days: 14,  // or trial_end: unixTimestamp
  },
});
```

## Trial Update Rules

| Parameter | Type | Remove trial |
| --- | --- | --- |
| `trial_period_days` | integer (days) | `trial_period_days: ""` |
| `trial_end` | Unix timestamp | `trial_end: ""` |

**Critical rules:**
- `trial_period_days` and `trial_end` are **mutually exclusive** — only one per request
- Must use the **same field** to remove that was used to set (can't use `trial_period_days: ""` to remove a trial set with `trial_end`)

## Client Pattern

Same as dynamic shipping/line items:

```js
// HTML+JS
const response = await checkout.runServerUpdate(() => fetch('/extend-trial-for-yearly', {
  method: 'POST', headers: { 'Content-type': 'application/json' },
  body: JSON.stringify({ checkout_session_id: actions.getSession().id })
}));

// React: runServerUpdate from useCheckout() / checkoutState.checkout.runServerUpdate(...)
```

## Use Cases

| Use case | Example |
| --- | --- |
| Dynamic trial management | Add/remove trials based on promotions |
| Extend trial for upsell | Monthly (7 days) → yearly (14 days) |

## Security Guidelines (Same as dynamic line items)

- Specific endpoints per action, not generic "update"
- Pass only `session.id` from client; retrieve session data server-side

## Related Pages

- [[source-stripe-checkout-dynamic-line-items]] — companion feature (line item updates)
- [[source-stripe-checkout-dynamic-shipping]] — companion feature (shipping updates)
- [[stripe-subscriptions]] — concept page

## Raw Sources

- [[stripe-checkout-dynamic-trials-2025]] — verbatim dynamic trial durations guide
