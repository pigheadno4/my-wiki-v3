---
title: "Stripe Docs — Stablecoins on Link"
type: source
date_ingested: 2026-05-08
original_format: webpage
raw_files:
  - "stripe-stablecoins-on-link-2025.md"
tags: [stripe, link, stablecoins, crypto, us-only, usd, guaranteed-settlement]
---

## Summary

Guide for stablecoin payments on Link. US businesses can accept any stablecoin (any wallet/token/network) via Link; payments always settle in USD. Link guarantees funds — zero integration changes needed.

## Key Facts

- **US businesses only**, USD only; 1–10,000 USD; one-time + on-session only
- **Supported integrations**: Payment Links, Stripe Checkout, Elements only
- **Settlement**: always USD to Stripe balance regardless of which stablecoin/network customer used
- **Link guarantees funds** — no integration changes required
- **Refunds**: returned to customer's original wallet as stablecoins
- **Disputes**: not supported
- **Testing**: requires blockchain testnet wallet with testnet funds

## Customer Flow

**New customer**: select "Crypto" → fill details → "Continue with Crypto" → Stripe Crypto payments page → select wallet → authorize Stripe → confirm payment → wallet confirmation → Stripe confirms success; customer auto-signed up to Link

**Returning customer**: select saved stablecoin wallet → "Continue with Crypto" → prefilled details → confirm → wallet confirmation → success

## Related Pages

- [[stripe-link]] — Link concept page (Stablecoins on Link section)
- [[stripe]] — Stripe company page

## Raw Sources

- [[stripe-stablecoins-on-link-2025]] — verbatim webpage content (62 lines)
