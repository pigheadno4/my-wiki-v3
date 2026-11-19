---
title: "Update the Customer During Checkout"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-checkout-update-customer-2025.md"
tags: [stripe, checkout-sessions, customer, guest-checkout, authentication, saved-payment-methods]
---

## Summary

A Customer object can be attached to an existing Checkout Session after creation by calling `checkout.sessions.update(sessionId, { customer: 'cus_...' })`. Attaching a customer enables their saved payment methods, email, and billing information to auto-populate — without losing any information the customer has already entered.

## Use Case

Guest checkout with mid-checkout login:
1. Customer starts checkout as a guest (no `customer` on session)
2. Customer opts to log in during checkout
3. Server calls `checkout.sessions.update(sessionId, { customer: authenticatedCustomerId })`
4. Saved PMs, email, and billing info populate automatically

## Key Behavior

- Previously entered info is **preserved** — not lost when customer is attached
- Saved payment methods, email, and billing details auto-populate from the Customer object

## Related Pages

- [[stripe-checkout]] — Checkout concept page

## Raw Sources

- [[stripe-checkout-update-customer-2025]] — verbatim page (overview only; no code samples in source)
