---
title: "Stripe — Set Up Payment Methods for Subscriptions with No Initial Payment"
type: source
date_ingested: 2026-05-12
original_format: webpage
raw_files:
  - "stripe-subscriptions-setup-intents-2026.md"
tags: [stripe, subscriptions, setup-intent, free-trial, off-session, authentication, authorization]
---

## Summary

SetupIntents for subscriptions that don't require an initial payment (free trials, usage-based, coupons, credit balances). Covers auto-creation, failure handling, and the critical cancellation footgun.

## When SetupIntents Are Auto-Created

Stripe auto-creates a SetupIntent when a subscription has no initial payment. `subscription.pending_setup_intent` is `null` when auth + authorization succeed or aren't required.

## Critical: SetupIntent Doesn't Auto-Cancel

`pending_setup_intent` does **not** cancel when the subscription ends. Must manually cancel on `customer.subscription.deleted` event.

## Two Failure Modes

| Failure | SetupIntent status | Handle by |
| --- | --- | --- |
| Authentication | `requires_action` | `stripe.confirmCardSetup(client_secret)` |
| Authorization | `requires_payment_method` | Collect new payment method |

```js
const { client_secret, status } = subscription.pending_setup_intent;

if (status === 'requires_action') {
  await stripe.confirmCardSetup(client_secret);
} else if (status === 'requires_payment_method') {
  // Collect new payment method
}
```

## Related Pages

- [[stripe-subscriptions]] — concept page (updated with SetupIntent for zero-payment subs)

## Raw Sources

- [[stripe-subscriptions-setup-intents-2026]] — verbatim guide (82 lines, 2 SVG diagrams downloaded)
