---
title: "Stripe Checkout Quickstart — Hosted & Embedded"
type: source
date_ingested: 2026-04-20
original_format: webpage
raw_files:
  - "stripe-checkout-quickstart-2025.md"
  - "stripe-checkout-embedded-quickstart-2025.md"
tags: [stripe, checkout, checkout-sessions, quickstart, payment, subscription, react, node]
---

## Summary

End-to-end quickstarts for Stripe Checkout — both the hosted (redirect) and embedded (on-site form) variants. Covers server setup, React client integration, test cards, and customization options for both modes.

## Key Takeaways

- **3 modes**: `payment` (one-time) | `subscription` (recurring) | `setup` (future payments)
- **Order is final once redirected** — can't modify without creating a new Checkout Session
- **Guest customers by default** for one-time payments; set `customer_creation: 'always'` to always create
- **Client pattern (hosted)**: check `?success=true` / `?canceled=true` URL params on return page
- **Local dev**: add `"proxy": "http://localhost:4242"` to `package.json`

## Hosted vs Embedded — Key Differences

| | Hosted page | Embedded page |
| --- | --- | --- |
| `ui_mode` | *(default)* | `embedded_page` |
| Customer experience | Leaves your site | Stays on your site |
| Return URL param | `success_url` | `return_url` with `{CHECKOUT_SESSION_ID}` |
| Server response | Redirect to `session.url` | Return `clientSecret` |
| Status check | URL params | `/session-status` endpoint + `session.status` |
| On failure | New session needed | `status === 'open'` → remount Checkout |

## Embedded-specific Details

- **`EmbeddedCheckoutProvider` + `EmbeddedCheckout`** from `@stripe/react-stripe-js`
- **`fetchClientSecret`** callback calls server, returns `clientSecret`
- **`loadStripe`** must be called **outside** component render — avoids recreating Stripe object on every render
- **Return page logic**: `complete` → show success; `open` → redirect to `/checkout` to remount
- **`/session-status`** endpoint: `stripe.checkout.sessions.retrieve(session_id)` → returns `status` + `customer_details.email`

## Key Session Parameters

| Parameter | Description |
| --- | --- |
| `line_items[].price` | Predefined Price ID |
| `line_items[].price_data` | Inline price definition |
| `mode` | `payment` / `subscription` / `setup` |
| `success_url` | Redirect after success (must be public) |
| `customer_email` | Prefills email field |
| `submit_type` | Submit button copy (4 options, e.g. `donate`) |
| `billing_address_collection` | `auto` or `required` |
| `shipping_address_collection.allowed_countries` | ISO country code array |
| `automatic_tax.enabled` | Enable Stripe Tax |
| `customer_creation` | `always` to always create Customer object |
| `customer` | Existing Customer ID to associate |

## Test Cards

| Card | Scenario |
| --- | --- |
| 4242 4242 4242 4242 | Success |
| 4000 0025 0000 3155 | Requires 3DS |
| 4000 0000 0000 9995 | Declined |

## Next Steps (from guide)

- Fulfill orders via `checkout.session.completed` webhook
- Receive payouts to bank account
- Refunds via API or Dashboard
- Customer self-management portal
- Adaptive Pricing for local currencies

## Related Pages

- [[stripe-checkout]] — Stripe Checkout concept page
- [[source-stripe-checkout-sessions]] — Checkout Sessions API deep dive
- [[source-stripe-accept-a-payment]] — Full integration guide (4 UI modes, mobile)

## Raw Sources

- [[stripe-checkout-quickstart-2025]] — Hosted page quickstart: 3-step setup, all key session params, React client example, test cards, customer handling
- [[stripe-checkout-embedded-quickstart-2025]] — Embedded page quickstart: ui_mode embedded_page, EmbeddedCheckoutProvider, fetchClientSecret, return_url template, session-status endpoint, remount on failure
