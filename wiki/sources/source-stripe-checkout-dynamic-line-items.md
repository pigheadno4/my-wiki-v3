---
title: "Dynamically Update Line Items"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-checkout-dynamic-line-items-2025.md"
tags: [stripe, checkout-sessions, line-items, dynamic-updates, runServerUpdate, beta, subscription, payment-intents]
---

## Summary

Beta feature for dynamically updating line items on a Checkout Session from the server, triggered by client-side actions. Uses the same `runServerUpdate` pattern as dynamic shipping. Works in both payment and subscription modes.

> **Contradiction fixed**: `stripe-checkout.md` previously noted dynamic line items as "not supported" in the Elements path. This source confirms they ARE supported via the beta `runServerUpdate` pattern (SDK version `2025-03-31.basil`+).

## Key Constraints

- Requires SDK version `2025-03-31.basil` or later
- Works in both **payment and subscription** modes (unlike dynamic shipping which is payment only)
- **Payment Intents**: no built-in support — must create a new PaymentIntent with adjusted amounts
- `runServerUpdate` has a **20-second timeout** — wrap in try/catch and record metrics

## Setup

```js
const stripe = require('stripe')('SK', { apiVersion: '2025-03-31.basil' });
```

## Server Endpoint Pattern

```js
// Specific endpoint for each action (not generic "update")
app.post('/change-subscription-interval', async (req, res) => {
  const { checkout_session_id, interval } = req.body;
  // 1. Validate inputs server-side
  // 2. Calculate new line items
  // 3. Update session
  await stripe.checkout.sessions.update(checkout_session_id, { line_items: newItems });
  return res.json({ type: 'success' });
});
```

### Security Guidelines

- Create **specific endpoints per action** (e.g. "add cross-sell") not generic "update"
- Never trust client-passed session data — only accept `session.id` and retrieve server-side
- Client-side data can be modified by malicious users

## Line Item Update Rules

Must retransmit the **entire array**:

| Goal | How |
| --- | --- |
| Keep existing item | Specify its `id` |
| Update existing item | Specify `id` + new field values |
| Add new item | Specify `price` + `quantity` (no `id`) |
| Remove item | Omit its `id` from the array |
| Reorder | Specify `id` at desired position |

## Client `runServerUpdate` Pattern

```js
// HTML+JS
try {
  const response = await checkout.runServerUpdate(() => fetch('/change-subscription-interval', {
    method: 'POST', headers: { 'Content-type': 'application/json' },
    body: JSON.stringify({ checkout_session_id: actions.getSession().id, interval: 'yearly' })
  }));
  if (!response.ok) { /* handle error */ }
} catch (error) { /* handle timeout */ }

// React: same but from checkoutState.checkout.runServerUpdate(...)
```

## Use Cases

| Use case | Notes |
| --- | --- |
| Subscription interval toggle | Switch monthly ↔ yearly price |
| Inventory check + hold | Validate quantity on server before allowing change |
| Add cross-sell | Add complimentary product if order total > $X |
| Update shipping rates | Combine with dynamic shipping feature |
| Update tax rates | For non-Stripe Tax integrations only |

## Related Pages

- [[source-stripe-checkout-dynamic-shipping]] — companion feature using same `runServerUpdate` pattern
- [[source-stripe-charge-shipping]] — basic static shipping rates
- [[stripe-checkout]] — Checkout concept page

## Raw Sources

- [[stripe-checkout-dynamic-line-items-2025]] — verbatim dynamic line items guide
