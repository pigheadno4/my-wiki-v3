---
title: "Stripe — Crypto Onramp: Stripe-Hosted Integration"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-crypto-onramp-stripe-hosted-2026.md"
tags: [stripe, crypto, onramp, fiat-to-crypto, redirect, session-api, pci]
---

## Summary

Implementation guide for the Stripe-hosted (standalone) crypto onramp. Covers two customization paths, available currencies with geo restrictions, and the onramp session API.

## Two Customization Paths

| Path | Where | Best for |
| --- | --- | --- |
| Generate redirect URL | Frontend (no Stripe account needed) | Lightweight, light customization, no branding |
| Mint session with redirect URL | Backend (Stripe account) | Full customization incl. wallet address, branding |

**Frontend scripts**: must load from `js.stripe.com` and `crypto-js.stripe.com` — never bundle or self-host (breaks without warning, PCI requirement).

## Frontend API

```js
window.StripeOnramp.Standalone({
  source_currency: 'usd',          // or 'eur'
  amount: { source_amount: '42' }, // or destination_amount
  destination_networks: ['ethereum', 'bitcoin'],
  destination_currencies: ['eth', 'btc'],
  destination_currency: 'eth',
  destination_network: 'ethereum'
}).getUrl()
```

## Backend API

`POST /v1/crypto/onramp_sessions` → returns `redirect_url`, `client_secret`, `transaction_details`

Session object: `cos_*` ID, `status: initialized`.

## Supported Currencies (US + EU)

ETH, ETH (Base), SOL, POL, MATIC, BTC, AVAX, XLM, USDC (Ethereum/Solana/Polygon/Avalanche/Base/Stellar)

**Geo restrictions**:
- XLM, USDC (Stellar/Avalanche/Polygon): not available in New York
- ETH (Base), MATIC, AVAX, USDC (Solana/Polygon/Avalanche/Base): not supported in EU

## Related Pages

- [[stripe-crypto-onramp]] — concept page (updated with currencies and session API)
- [[source-stripe-crypto-onramp]] — overview source

## Raw Sources

- [[stripe-crypto-onramp-stripe-hosted-2026]] — verbatim Stripe-hosted onramp guide (136 lines)
