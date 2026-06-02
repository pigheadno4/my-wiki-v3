---
title: "Stripe — Embeddable Pricing Table for Subscriptions"
type: source
date_ingested: 2026-05-12
original_format: webpage
raw_files:
  - "stripe-pricing-table-2026.md"
tags: [stripe, subscriptions, pricing-table, checkout, no-code, customer-session, embed]
---

## Summary

Dashboard-created embeddable pricing table (`<stripe-pricing-table>` web component). No-code; supports flat-rate, per-seat, tiered, free trials. Max 4 products, 3 prices/product, 3 unique intervals. Does NOT support usage-based billing or Connect.

## Key Web Component Attributes

- `pricing-table-id`, `publishable-key` — required
- `customer-email` — pre-fills email; also used for local currency testing (`test+location_FR@email.com`)
- `customer-session-client-secret` — pass existing customer via CustomerSession
- `client-reference-id` — for reconciliation; max 200 chars; no sensitive data

## Pass Existing Customer

```js
stripe.customerSessions.create({
  customer_account: id,   // Accounts v2
  // OR customer: id,     // Customers v1
  components: { pricing_table: { enabled: true } }
})
// → pass client_secret as customer-session-client-secret attribute
// Expires 30min from creation; additional 30min to complete payment
```

## Custom CTA

One product can have a custom CTA button. URL formats: absolute, relative, mailto, tel, `{PRODUCT_ID}`, `{CUSTOMER_EMAIL}`.

## Custom Fields (3 types)

Text (255 chars), Numbers only (255 digits), Dropdown (up to 10 options). Sent in `checkout.session.completed` event.

## CSP Requirements

`frame-src` + `script-src`: `https://js.stripe.com`

## Limitations

- No usage-based billing
- No Connect support
- No intermediate signup step before checkout
- Rate limit: 50 read ops/sec (shared across all pricing tables)
- Requires `allow-top-navigation` if embedded in iframe

## Related Pages

- [[stripe-pricing-table]] — concept page
- [[stripe-subscriptions]] — subscriptions context

## Raw Sources

- [[stripe-pricing-table-2026]] — verbatim pricing table guide (342 lines)
