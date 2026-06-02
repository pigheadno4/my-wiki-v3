---
title: "Manually Approve Payments on Your Server"
type: source
date_ingested: 2026-04-22
original_format: webpage
raw_files:
  - "stripe-checkout-manual-approval-2025.md"
tags: [stripe, checkout-sessions, manual-approval, fraud-prevention, inventory, server-side]
---

## Summary

Stub/navigation page for the manual approval feature in Checkout Sessions. Allows server-side logic to run before finalizing a payment. Implementation guide is behind the full Checkout Sessions integration path.

## Key Facts

- **Checkout Sessions only** — not available for Payment Intents API
- **Compatible with**: dynamic line items feature
- **PI alternative**: "finalize payments on the server" pattern (`stripe.paymentIntents.confirm()` server-side)

## Use Cases

- Custom or third-party fraud prevention logic
- Inventory checks before confirming payment
- Payment method compatibility checks

## Related Pages

- [[source-stripe-checkout-dynamic-line-items]] — compatible feature
- [[stripe-checkout]] — Checkout concept page

## Raw Sources

- [[stripe-checkout-manual-approval-2025]] — verbatim stub page (22 lines)
