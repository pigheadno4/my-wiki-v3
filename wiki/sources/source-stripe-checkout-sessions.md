---
title: "Stripe Checkout Sessions API"
type: source
date_ingested: 2026-04-19
original_format: webpage
raw_files:
  - "stripe-checkout-sessions-api-2025.md"
tags: [stripe, checkout-sessions, checkout, payment-element, adaptive-pricing, subscriptions]
---

## Summary

Overview of the Stripe Checkout Sessions API — Stripe's recommended approach for most payment integrations. Manages the full checkout lifecycle with built-in tax, discounts, shipping, subscriptions, and Adaptive Pricing.

## Key Takeaways

- **Stripe's recommended API** for most integrations — significantly less code than Payment Intents
- **3 UI modes**: Stripe-hosted page (redirect), Embedded form, Custom flow (`ui_mode: "custom"` with Stripe Elements)
- **5 built-in features**: tax calculation, discounts, shipping, subscriptions, Adaptive Pricing — no extra API integrations needed
- **When to use Payment Intents instead**: need full checkout state control OR building discount/tax/subscription/currency logic yourself
- **Metadata**: attach `order_id` for reconciliation; don't store PII

## Checkout Sessions vs Payment Intents

| | Checkout Sessions | Payment Intents |
| --- | --- | --- |
| Code complexity | Less code | More code |
| Built-in features | Tax, discounts, shipping, subscriptions, Adaptive Pricing | None (build yourself) |
| Adaptive Pricing | Yes | No |
| Use when | Most integrations | Full control needed |

## 3 UI Modes

| Mode | Description |
| --- | --- |
| Stripe-hosted page | Redirect to Stripe; no UI code needed |
| Embedded form | Stripe form embedded in your site |
| Custom (`ui_mode: "custom"`) | Stripe Elements (Payment Element) on your page |

## Session Creation (Custom Mode)

```javascript
const session = await stripe.checkout.sessions.create({
  mode: "payment",
  ui_mode: "custom",
  return_url: "https://example.com/return",
  metadata: { order_id: "6735" }
});
// Pass session.client_secret to client for Stripe Elements
```

## Related Pages

- [[stripe]] — Stripe company page
- [[source-stripe-payment-intents]] — Payment Intents + SetupIntents reference

## Raw Sources

- [[stripe-checkout-sessions-api-2025]] — Checkout Sessions API overview: 3 UI modes, 5 built-in features, vs Payment Intents comparison, metadata usage
