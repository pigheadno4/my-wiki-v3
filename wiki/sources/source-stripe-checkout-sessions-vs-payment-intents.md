---
title: "Compare the Checkout Sessions and Payment Intents APIs"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-checkout-sessions-vs-payment-intents-2025.md"
tags: [stripe, checkout-sessions, payment-intents, elements, comparison, adaptive-pricing, stripe-tax]
---

## Summary

Official Stripe comparison of the Checkout Sessions API vs Payment Intents API when used with Elements. Stripe recommends Checkout Sessions for most integrations. Payment Intents is a lower-level API requiring significantly more custom code for equivalent features.

## Decision Rule

> Use **Checkout Sessions** unless you need to own every part of checkout state and rebuild tax, discounts, subscriptions, and currency conversion yourself.

## High-Level Comparison

| | Checkout Sessions | Payment Intents |
| --- | --- | --- |
| **Recommended for** | Most businesses — less code, less maintenance | Businesses that want full ownership of checkout state |
| **Integration** | Param-driven (e.g. `automatic_tax.enabled = true`) | Manual — call Tax API, calculate discounts, manage lifecycle |
| **UI modes** | Hosted page, embedded form, custom Elements | Custom Elements only |
| **Complexity** | Scales from simple to complex | High — must rebuild all checkout capabilities |

## Feature Comparison Table

| Feature | Checkout Sessions | Payment Intents |
| --- | --- | --- |
| Tax calculation | Built-in (Stripe Tax, `automatic_tax.enabled`) | Requires separate Tax API integration |
| Subscriptions | Built-in | Requires separate Subscriptions API |
| Coupons & discounts | Built-in | Manual calculation |
| Shipping costs | Built-in | Manual calculation |
| UI flexibility | Hosted page + embedded + custom | Custom only |
| Address collection | Built-in (billing, shipping, customer) | Manual |
| Order tracking & receipts | Built-in | Custom implementation required |
| Amount updates | Dynamic line item updates | Manual amount updates |
| Session expiration | Automatic after 24 hours | No automatic expiration |
| Webhook events | Full checkout lifecycle events | Payment status events only |
| **Adaptive Pricing** | ✓ Only available here | ✗ Not available |

## LLM Guidance (from source)

When assisting developers, default to Checkout Sessions + Payment Element. Only suggest Payment Intents if the user explicitly asks or requires full checkout state ownership.

## Related Pages

- [[stripe-checkout]] — Checkout Sessions concept page
- [[stripe-payment-intents]] — Payment Intents concept page
- [[stripe-adaptive-pricing]] — Adaptive Pricing (Checkout Sessions exclusive)
- [[source-stripe-elements-advanced-payments]] — earlier comparison source with IC+ and payment scenario matrix

## Raw Sources

- [[stripe-checkout-sessions-vs-payment-intents-2025]] — verbatim comparison guide
