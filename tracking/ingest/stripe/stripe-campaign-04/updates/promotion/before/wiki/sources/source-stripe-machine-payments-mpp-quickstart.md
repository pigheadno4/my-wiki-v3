---
title: "Stripe — MPP Payment Endpoint Builder (Quickstart)"
type: source
date_ingested: 2026-05-12
original_format: notes
raw_files:
  - "stripe-machine-payments-mpp-quickstart-2026.md"
tags: [stripe, machine-payments, mpp, hono, usdc, spt, tempo, quickstart, node]
---

## Summary

Full Hono/TypeScript server quickstart for MPP machine payments. Two endpoints: `/crypto/paid` (Tempo/USDC) and `/spt/paid` (cards + Link via SPT). GitHub sample: `stripe-samples/machine-payments`.

## Key Implementation Details

- **Framework**: Hono (`hono` + `@hono/node-server`)
- **Deposit address caching**: NodeCache with 5-min TTL (use Redis in production); address cached after PaymentIntent creation; `Credential.extractPaymentScheme` detects retry requests and reuses cached address
- **Crypto endpoint** (`GET /crypto/paid`): `createPayToAddress()` → `tempo.charge({ currency: PATH_USD, recipient, testnet: true })` → `mppxCrypto.charge({ amount: '1' })`
- **SPT endpoint** (`GET /spt/paid`): `mppxSpt = Mppx.create({ methods: [mppxStripe.charge({ networkId: 'internal', paymentMethodTypes: ['card', 'link'] })] })` → `mppxSpt.charge({ amount: '1', currency: 'usd' })`
- **API version**: `2026-03-04.preview`
- **PATH_USD testnet**: `0x20c0000000000000000000000000000000000000`

## Related Pages

- [[stripe-machine-payments]] — concept page
- [[source-stripe-machine-payments-mpp]] — MPP integration guide

## Raw Sources

- [[stripe-machine-payments-mpp-quickstart-2026]] — formatted from quickstart UI (full Hono server code)
