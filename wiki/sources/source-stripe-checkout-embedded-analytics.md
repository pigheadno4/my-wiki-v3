---
title: "Stripe Checkout: Track Analytics Events in Embedded Checkout"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-checkout-embedded-analytics-2025.md"
tags: [stripe, checkout, embedded, analytics, events, onAnalyticsEvent, client-metadata, segment, ga4]
---

## Summary

Guide for using real-time analytics events in Embedded Checkout (private preview as of 2026-04-20). Covers the 6 event types, `onAnalyticsEvent` callback, `client_metadata` for campaign attribution, event schemas, failure reasons, and integration examples (Segment, custom backend).

## Key Takeaways

- **Private preview** as of ingestion date
- **Embedded only** — `onAnalyticsEvent` callback on `stripe.createEmbeddedCheckoutPage()`
- **`client_metadata`** on session create — custom KV pairs threaded into all events; **don't put sensitive data** (client-accessible)
- **Amounts**: always in smallest currency unit (cents for USD); don't recalculate; best-effort delivery
- **Pattern**: analytics events for behavioral tracking + `checkout.session.completed` webhook for accurate conversion data
- **TypeScript**: `StripeCheckoutAnalyticsEvent` from `@stripe/stripe-js`

## 6 Analytics Events

| Event | When | Key data |
| --- | --- | --- |
| `deviceData` | UI renders | Device category, language, platform, viewport |
| `checkoutRendered` | UI renders | Line items, currency, amount |
| `promotionCodeApplied` | Promo code applied | code |
| `lineItemChange` | Items/qty/currency change (upsells, cross-sells, optional items) | Line items, currency, amount |
| `checkoutSubmitted` | Customer submits payment | PM type, line items, currency, amount |
| `checkoutSubmitFailed` | Valid submission fails | PM type, failureReason, line items, currency, amount |

## Event Structure

```typescript
{
  eventType: string;
  checkoutSession: string;
  details: object;
  clientMetadata: {[key: string]: string};
  timestamp: number;  // Unix seconds
}
```

## `checkoutSubmitFailed.failureReason` Values

| Value | Description |
| --- | --- |
| `api_error` | Card declines, 3DS failure, network/API errors, server validation |
| `user_cancelled` | User canceled after submitting (e.g., Link/Klarna flow dismissal) |
| `reverification` | Link reverification required (e.g., expired session) |
| `unexpected` | Unknown errors |

## Implementation

```js
// 1. Session create with client_metadata
stripe.checkout.sessions.create({
  ui_mode: 'embedded_page',
  client_metadata: {
    funnel_id: 'summer_sale_2025',
    campaign: 'email_promo',
  },
  ...
})

// 2. Initialize with onAnalyticsEvent
const checkout = await stripe.createEmbeddedCheckoutPage({
  clientSecret: session.client_secret,
  onAnalyticsEvent: (event) => {
    const { eventType, details, clientMetadata, checkoutSession, timestamp } = event;
    // Send to Segment, GA4, custom backend, etc.
  },
});
```

## Conversion Tracking

Analytics events = behavioral (best-effort). For accurate conversion: listen to `checkout.session.completed` webhook + read `session.client_metadata` for attribution.

```js
// session.client_metadata available on webhook object
if (event.type === 'checkout.session.completed') {
  const { funnel_id, campaign } = session.client_metadata;
  analytics.track('Purchase Completed', { checkout_id: session.id, funnel_id, campaign });
}
```

## Related Pages

- [[stripe-checkout]] — Stripe Checkout concept page
- [[source-stripe-checkout-conversion-funnel]] — GA4 funnel tracking for hosted Checkout

## Raw Sources

- [[stripe-checkout-embedded-analytics-2025]] — Embedded analytics (private preview): 6 event types + schemas, failureReason table, onAnalyticsEvent callback, client_metadata, Segment + custom backend examples, TypeScript types
