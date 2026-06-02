---
title: "Design a Custom Payment Element Integration"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-payment-element-design-integration-2025.md"
tags: [stripe, payment-element, payment-intents, setup-intents, integration-design, deferred-intent, client-confirmation, server-confirmation]
---

## Summary

Architectural decision guide for the Payment Intents API path with the Payment Element. The Checkout Sessions section is a one-liner — the substantive content is a **2×2 decision framework** covering when to create the Intent and where to confirm it.

> The Checkout Sessions API is recommended for most integrations. This guide applies specifically to the Payment Intents API path.

## Decision 1 — When to Create the PaymentIntent/SetupIntent

| Approach | When to use |
| --- | --- |
| **Deferred** — create Payment Element first, Intent later | Multi-page flows; dynamic amounts (items, quantities, discounts can change before Pay) |
| **Eager** — create Intent + Payment Element together | Static checkout pages; simplest integration |

**Why deferred matters**: Amount changes affect payment method eligibility. Deferring Intent creation until after the customer presses Pay avoids needing to sync the Intent every time the client changes items or applies a discount code.

## Decision 2 — Where to Confirm the PaymentIntent/SetupIntent

| Approach | When to use |
| --- | --- |
| **Client-side** | No server-side business logic required; quickest integration; Stripe SDK handles 3DS + next actions automatically + localizes error messages |
| **Server-side** | Must run business logic before confirmation (payment method restrictions, application fees); confirm immediately after logic runs to prevent client from invalidating it |

**Key constraint for server-side**: must confirm the Intent immediately after running business logic — don't allow time for the client to make changes that could invalidate the server-side decisions.

## Related Pages

- [[stripe-payment-intents]] — concept page
- [[source-stripe-checkout-sessions-vs-payment-intents]] — comparison of the two APIs
- [[stripe]] — company page

## Raw Sources

- [[stripe-payment-element-design-integration-2025]] — verbatim architectural decision guide
