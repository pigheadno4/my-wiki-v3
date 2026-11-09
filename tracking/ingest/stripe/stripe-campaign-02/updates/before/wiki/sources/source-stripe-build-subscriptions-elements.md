---
title: "Build a Subscriptions Integration with Elements"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-build-subscriptions-elements-2025.md"
tags: [stripe, subscriptions, checkout-sessions, elements, entitlements, billing, plan-change, proration, cancel, accounts-v2]
---

## Summary

End-to-end guide for building a subscriptions integration using Stripe Elements + Checkout Sessions API. Covers both Customer v1 and Accounts v2 customer models. Includes entitlements for feature gating, plan changes, proration preview, and cancellation.

## API Objects Involved

| Object | Role |
| --- | --- |
| Product | What you sell |
| Price | Unit amount, currency, billing interval (`recurring: { interval: 'month' }`) |
| Customer (v1) or Account (v2) | Who is being billed |
| Subscription | Scheduled recurring purchase |
| Invoice | Auto-generated per billing period; tracks payment status |
| PaymentIntent | Auto-created by Invoice for payment collection |
| Feature | A function/ability customers can access |
| ProductFeature | Links a Feature to a Product |
| Entitlement | Auto-created when Subscription created; one per Feature in the subscribed Product |

## Checkout Session for Subscriptions

```js
const session = await stripe.checkout.sessions.create({
  ui_mode: 'elements',
  mode: 'subscription',          // key: subscription mode
  customer: 'cus_...',           // or customer_account: 'acct_...' for Accounts v2
  line_items: [{ price: 'price_...', quantity: 1 }],
  return_url: 'https://example.com/return?session_id={CHECKOUT_SESSION_ID}',
});
// Send session.client_secret to client
```

## Client-Side: Confirm Payment

```js
const checkout = stripe.initCheckoutElementsSdk({ clientSecret });

// Display session data
const session = loadActionsResult.actions.getSession();
session.lineItems;          // items
session.total.total.amount; // total

// Gate Pay button
checkout.on('change', (session) => {
  document.getElementById('pay-button').disabled = !session.canConfirm;
});

// Confirm
actions.confirm();          // HTML+JS
// React: checkoutState.checkout.confirm()
```

## Entitlements Pattern

Entitlements are automatically created when a subscription is created — one per Feature associated with the subscribed Product. Use active entitlements to gate features; don't re-query the subscription/product/feature chain.

```
Product A → has ProductFeature → Feature X
Customer subscribes to Product A
→ Stripe auto-creates Entitlement: Customer ↔ Feature X

Gate access by checking: customer.activeEntitlements.includes(featureX)
```

Listen to `entitlement.active_entitlement_summary.updated` to provision/deprovision.

## Webhook Events for Subscriptions

| Event | Action |
| --- | --- |
| `invoice.paid` | Provision access; store `product.id` + `subscription.id` + `status` |
| `invoice.payment_failed` | Notify customer; subscription → `past_due` |
| `customer.subscription.created` | Grant access |
| `customer.subscription.updated` | Sync access (plan change) |
| `customer.subscription.deleted` | Revoke access |

Check `product.id` (not price) when granting access — more resilient to pricing changes.

## Plan Change

```js
// Server-side
const sub = await stripe.subscriptions.retrieve(subscriptionId);
await stripe.subscriptions.update(subscriptionId, {
  cancel_at_period_end: false,
  items: [{ id: sub.items.data[0].id, price: newPriceId }],
});
// Triggers customer.subscription.updated
```

## Proration Preview

```js
const invoice = await stripe.invoices.createPreview({
  customer: customerId,          // or customer_account
  subscription: subscriptionId,
  subscription_details: {
    items: [
      { id: currentItemId, deleted: true },
      { price: newPriceId, deleted: false },
    ],
  },
});
```

Display `invoice.amount_due` to show the customer what they'll owe.

## Cancellation

```js
await stripe.subscriptions.del(subscriptionId);
// Triggers customer.subscription.deleted
```

> **Canceled subscriptions cannot be reactivated.** Collect new billing info, update default PM, and create a **new** subscription on the existing customer record.

## Customer Models

- **Customers v1**: `stripe.customers.create({ email, name, address, shipping })`; pass `customer: 'cus_...'` to session
- **Accounts v2** (recommended): `stripe.v2.core.accounts.create({ contact_email, configuration: { customer: {...} } })`; pass `customer_account: 'acct_...'` to session; requires API version `2026-03-25.dahlia`

## Related Pages

- [[stripe-subscriptions]] — concept page
- [[source-stripe-checkout-build-subscriptions]] — earlier subscriptions guide
- [[stripe-checkout]] — Checkout concept page

## Raw Sources

- [[stripe-build-subscriptions-elements-2025]] — verbatim end-to-end subscriptions guide (3003 lines)
