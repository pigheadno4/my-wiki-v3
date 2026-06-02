---
title: "iOS Subscription Management with Customer Portal"
type: source
date_ingested: 2026-04-22
original_format: webpage
raw_files:
  - "stripe-inapp-digital-goods-customer-portal-2025.md"
tags: [stripe, mobile, ios, digital-goods, customer-portal, subscriptions, universal-links, webhooks, billing-portal]
---

## Summary

Companion to the iOS digital goods payment guides — covers subscription *management* (not purchase). Redirect customers to a Stripe-hosted customer portal opened in Safari via Universal Links for return.

> See [[source-stripe-inapp-digital-goods-checkout]] for subscription purchase (Checkout path).

## Portal Session API

```javascript
// Server-side: generate portal URL
const billingSession = await stripe.billingPortal.sessions.create({
  customer: customerId,
  return_url: 'https://example.com/portal_redirect', // Universal Link
});
res.json({ url: billingSession.url });

// Client-side: open in Safari
UIApplication.shared.open(url)
// handle return via .onOpenURL { url in ... }
```

## Portal Configuration

Dashboard or API (`stripe.billingPortal.configurations.create()`):
- `features.invoice_history.enabled: true`
- Product catalog required for upgrades/downgrades (not for invoicing-only)

**Product catalog attributes**:
- Editable: product name, description, quantity restrictions
- Fixed (set at creation): price amount, currency, billing interval

**Optional**: tax ID collection — toggle on in Dashboard → Customer portal settings → Tax ID (requires Stripe Tax)

## Webhook Events (Subscription Lifecycle)

| Event | Action |
| --- | --- |
| `customer.subscription.created` | Mark subscription active |
| `customer.subscription.updated` | Handle pause/upgrade/cancel changes |
| `customer.subscription.deleted` | Mark subscription inactive |

## Connect Note

Configure portal for the **platform**, not a connected account.

## Optional: Deep Links

`customer-management/portal-deep-links` — link directly to specific portal page/action with custom redirect behavior after completion.

## Related Pages

- [[stripe-inapp-payments]] — in-app payments concept page
- [[stripe-subscriptions]] — Stripe subscriptions concept page
- [[source-stripe-inapp-digital-goods-checkout]] — subscription purchase (Checkout path)
- [[source-stripe-inapp-digital-goods-custom-checkout]] — subscription purchase (Elements path)

## Raw Sources

- [[stripe-inapp-digital-goods-customer-portal-2025]] — verbatim guide (~348 lines, 1 image)
