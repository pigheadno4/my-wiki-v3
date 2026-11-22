---
title: "Stripe Docs — Link in the Express Checkout Element"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-express-checkout-link-2025.md"
tags: [stripe, link, express-checkout-element, apple-pay, google-pay, paypal, klarna, amazon-pay, one-click]
---

## Summary

Thin overview of Link in the Express Checkout Element — a one-click payment button integration supporting Link, Apple Pay, Google Pay, PayPal, Klarna, and Amazon Pay.

## Key Facts

- **6 supported PMs**: Link, Apple Pay, Google Pay, PayPal, Klarna, Amazon Pay
- **Dynamic button sorting** by customer location — no frontend changes needed to add new buttons
- **Reuses existing Elements instance** — minimal overhead if already using Elements
- **Setup**: `stripe.elements({ mode, amount, currency })` → `create('expressCheckout', options)` → `mount('#express-checkout-element')`

## CDN Assets

- `raw/assets/stripe-link-express-checkout-element.png` — Express Checkout Element UI with Link (181 KB)

## Related Pages

- [[stripe-link]] — Link concept page (Express Checkout Element section)
- [[stripe-express-checkout-element]] — broader Express Checkout Element concept (if exists)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-express-checkout-link-2025]] — verbatim webpage content (44 lines)
