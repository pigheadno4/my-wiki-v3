---
title: "Stripe: Accept Stablecoin Payments"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-accept-stablecoin-payments-2025.md"
tags: [stripe, stablecoin, crypto, usdc, checkout, elements, payment-intents, metamask, testnet]
---

## Summary

Integration guide for accepting stablecoin payments. Covers enablement via Dashboard, 3 integration paths (Checkout, Elements/Checkout Sessions API, Elements/PaymentIntents API), and testnet setup.

## Key Integration Details

**Enable**: Dashboard → Payment Methods → request "Stablecoins and Crypto" → Stripe reviews → approve → active.

**Dynamic payment methods**: no code changes needed — Stripe auto-shows crypto to eligible customers.

**Checkout (curl)**: add `crypto` to `payment_method_types`; all `line_items` must use `usd`.

**Elements + Checkout Sessions API**: `ui_mode: 'elements'`; return `client_secret`; `initCheckoutElementsSdk`; `PaymentElement` component; `confirm()`.

**Elements + PaymentIntents API**: `payment_method_types: ['crypto']`; `currency: 'usd'`; `stripe.confirmPayment` with `return_url`; supports Accounts v2 (`customer_account`) and Customers v1 (`customer`).

**PaymentIntent updates**: after server-side update, call `elements.fetchUpdates()` to sync UI.

## Testnet Setup (MetaMask + Polygon Amoy)

1. Install MetaMask; add Polygon Amoy network (Chain ID 80002, RPC `https://rpc-amoy.polygon.technology/`)
2. Import USDC token: contract `0x41E94Eb019C0762f9Bfcf9Fb1E58725BfB0e7582`
3. Get USDC: faucet.circle.com → Polygon PoS Amoy → 20 USDC
4. Get POL (gas): faucet.polygon.technology → Polygon Amoy

Other faucets: Paxos USDP, Devnet SOL, Sepolia ETH, Amoy POL.

## Raw Sources

- [[stripe-accept-stablecoin-payments-2025]] — verbatim webpage content (2259 lines; Checkout/Elements/PaymentIntents API + testnet setup + React/HTML+JS variants)
