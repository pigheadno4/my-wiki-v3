---
title: "Stripe Payment Method Rules"
type: concept
category: technology
tags: [stripe, payment-method-rules, dynamic-payment-methods, checkout, payment-element, klarna, bnpl, conversion]
---

## Definition

Payment method rules let merchants control when specific payment methods appear — based on order amount or buyer country/currency — directly from the Dashboard with no code. Part of the [[stripe-dynamic-payment-methods]] customization suite.

**Requires**: dynamic payment methods + Payment Element, Express Checkout Element, Checkout, or Payment Links.

## What Rules Can Do

- **Amount-based**: hide/show a PM if order total is above or below a threshold (e.g., require ≥ $100 for Klarna)
- **Location-based**: hide/show a PM for buyers in specific countries or using specific currencies

Rules do NOT apply when creating subscriptions.

## Setup

Dashboard → Payment methods settings → overflow menu on a PM → **Customize availability** → set rules → **Apply Overrides**. The PM gets a **Customized** tag.

Limits are configured in one currency; Stripe auto-converts at current exchange rate for other-currency transactions.

## Compatibility

- Works with [[stripe-ab-testing-payment-methods]] — rules can serve as A/B experiment targeting criteria
- Works with payment method configurations (different PM sets per scenario)

## Testing Location-Based Rules

**Checkout**: pass `customer_email: 'test+location_FR@example.com'` (ISO country code suffix) when creating a Checkout Session.

**Payment Links**: pass `prefilled_email` or `locked_prefilled_email` URL parameter with the location-formatted email.

## Sources

- [[source-stripe-payment-method-rules]] — primary: rule conditions, setup flow, subscription caveat, currency auto-conversion, location testing
