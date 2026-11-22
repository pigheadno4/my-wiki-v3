---
title: "Stripe Docs — Link in the Payment Request Button"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-payment-request-button-link-2025.md"
tags: [stripe, link, payment-request-button, deprecated, connect]
---

## Summary

Overview of Link in the Payment Request Button — a **deprecated integration path** that Stripe no longer recommends. Documented for legacy integrations.

## Deprecation Notice

> Stripe no longer recommends the Payment Request Button for Link integrations. Use instead: Link Authentication Element, Express Checkout Element, or Payment Element.

## Key Facts (for existing integrations)

- **90-day auth window**: if customer authenticated Link within 90 days on any Link-enabled site, they can pay instantly without re-authenticating
- **No additional fees**; compatible with subscriptions and card features
- **New customers**: prompted to save information in Link account when clicking the Link button

## Connect

- Auto-available to connected accounts using Payment Request Button via Connect platform
- Connect platform manages Link settings for platform-processed payments
- Connected accounts manage their own for non-platform payments

## CDN Assets

- `raw/assets/stripe-link-payment-request-button.png` — Payment Request Button with Link (145 KB)

## Related Pages

- [[stripe-link]] — Link concept page (Payment Request Button deprecated section)
- [[source-stripe-express-checkout-link]] — preferred alternative (Express Checkout Element)
- [[source-stripe-payment-element-link]] — preferred alternative (Payment Element)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-payment-request-button-link-2025]] — verbatim webpage content (31 lines)
