---
title: "Stripe Checkout: Analyze Your Conversion Funnel (GA4)"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-checkout-conversion-funnel-2025.md"
tags: [stripe, checkout, analytics, google-analytics, ga4, conversion-funnel, measurement-protocol]
---

## Summary

Guide for tracking Stripe Checkout conversion funnel metrics using Google Analytics 4. Covers gtag.js instrumentation, the GA4 Measurement Protocol for server-side events, and linking client/server events via session metadata.

## Key Takeaways

- **Critical setup**: add `checkout.stripe.com` to GA4 referral exclusion list (prevents Stripe from appearing as a traffic source)
- **3 funnel steps**: product page view → `begin_checkout` event (Buy click) → success page view
- **3 integration approaches** — see table below
- **Embedded**: uses separate analytics integration (`embedded-analytics.md` — not covered here)

## 3 Approaches

| Approach | begin_checkout | purchase | Client linkage |
| --- | --- | --- | --- |
| Client-side | gtag event before redirect | success page view | Automatic |
| Server-side | GA4 Measurement Protocol on `checkout.session.completed` | Same | Anonymous (separate client ID) |
| Server-side + linked client ID | GA4 Measurement Protocol | Same | Store GA `client_id` in session metadata |

## Client-Side Pattern

```js
// Fire before redirecting to Stripe
fetch('/create-checkout-session', { method: 'POST' })
  .then(res => res.json())
  .then(session => {
    gtag('event', 'begin_checkout', {
      event_callback: () => { window.location.href = session.url; }
    });
  });
```

Add `gtag.js` script to product, success, and canceled pages.

## Server-Side Measurement Protocol

```js
// On checkout.session.completed webhook:
fetch(`https://www.google-analytics.com/mp/collect?measurement_id=${MEASUREMENT_ID}&api_secret=${API_SECRET}`, {
  method: 'POST',
  body: JSON.stringify({
    client_id: 'XXXXXXXXXX.YYYYYYYYYY',  // anonymous if not linked
    events: [{ name: 'purchase', params: {} }]
  })
});
```

## Linking Client + Server Events

1. Client: `gtag('get', GA_CLIENT_ID, 'client_id', (clientID) => { ... send clientID with request ... })`
2. Server: store in `session.metadata.analyticsClientId`
3. On webhook: read from `event.data.object.metadata.analyticsClientId` → send as `client_id` to Measurement Protocol

This links server-side `purchase` events to the correct client session in GA4.

## Funnel Metrics

| Metric | Source |
| --- | --- |
| Product page views | gtag page_view event (auto-fire on load) |
| begin_checkout count | gtag event before Stripe redirect |
| Success page views | gtag page_view event (auto-fire on load) |
| purchase (server-side) | GA4 Measurement Protocol on webhook |

## Related Pages

- [[stripe-checkout]] — Stripe Checkout concept page
- [[source-stripe-checkout-fulfillment]] — Fulfillment webhooks (used for server-side analytics)

## Raw Sources

- [[stripe-checkout-conversion-funnel-2025]] — GA4 conversion funnel: site setup, gtag instrumentation, begin_checkout event, server-side Measurement Protocol, client ID linking, server-side redirects
