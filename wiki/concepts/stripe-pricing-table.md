---
title: "Stripe Pricing Table"
type: concept
category: technology
tags: [stripe, subscriptions, pricing-table, checkout, no-code, embed, customer-session]
---

## Overview

The Stripe pricing table is a Dashboard-created embeddable web component (`<stripe-pricing-table>`) that displays subscription pricing and routes customers to Checkout. No code required to create; embed with a `<script>` tag and web component.

## Capabilities

- Supports: flat-rate, per-seat, tiered pricing, free trials
- **Not supported**: usage-based billing, Connect
- Max: 4 products, 3 prices/product, 3 unique billing intervals
- Rate limit: 50 read ops/sec (shared)

## Embed

```html
<script async src="https://js.stripe.com/v3/pricing-table.js"></script>
<stripe-pricing-table
  pricing-table-id="{{PRICING_TABLE_ID}}"
  publishable-key="{{PUBLISHABLE_KEY}}"
></stripe-pricing-table>
```

Key attributes: `customer-email`, `customer-session-client-secret`, `client-reference-id` (max 200 chars, for reconciliation).

## Pass Existing Customer

For an already authenticated customer, create a `CustomerSession` server-side for a customer-configured Account (`customer_account`) or Customer (`customer`), with the `pricing_table` component enabled; pass its `client_secret` as `customer-session-client-secret`. Both the 2026-05-12 and 2026-11-07 guides allow 30 minutes to include the secret in the table, then an additional 30 minutes **after rendering the pricing table** to complete payment. If the customer session has expired before Checkout Session creation, the new Session has no associated customer; if it expires after Session creation but before confirmation, confirmation fails. The November guide adds a Dashboard route for other-user Accounts v2 public-preview enrollment, while retaining Connect GA and preview-version qualifications. See [[source-stripe-pricing-table]].

## Custom CTA

One product per table can have a custom call-to-action URL. Supports absolute, relative, mailto, tel, `{PRODUCT_ID}`, `{CUSTOMER_EMAIL}` template vars.

## Local Currency Testing

Set `customer-email="test+location_FR@email.com"` to test pricing display in France's currency.

## CSP

`frame-src` + `script-src`: `https://js.stripe.com`

## Sources

- [[source-stripe-pricing-table]] — full guide: embed, customize, customer session, limitations
