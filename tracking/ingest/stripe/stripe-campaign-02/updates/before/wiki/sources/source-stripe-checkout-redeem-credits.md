---
title: "Redeem Credits"
type: source
date_ingested: 2026-04-21
original_format: webpage
raw_files:
  - "stripe-checkout-redeem-credits-2025.md"
tags: [stripe, checkout-sessions, credits, store-credit, gift-card, gated]
---

## Summary

Gated feature (private access program) for applying store credit or prepaid gift card amounts to a Checkout Session. The full integration guide is behind an access request gate — only the overview paragraph is publicly visible.

## Key Facts

- **Applied after** tax and shipping — reduces the net amount due
- **Stripe doesn't track credit balances** — merchant passes the available credit amount into the session
- **Reconciliation**: after session completion, retrieve session details to determine credit amount actually used
- **Use cases**: store credit, prepaid gift cards
- **Only** available with Elements + Checkout Sessions API (not Payment Intents)
- **Access**: private program — must request access

## Related Pages

- [[stripe-checkout]] — Checkout concept page

## Raw Sources

- [[stripe-checkout-redeem-credits-2025]] — verbatim overview (gated feature, limited public content)
