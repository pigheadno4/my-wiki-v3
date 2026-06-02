---
title: "Stripe — x402 Payments Integration Guide"
type: source
date_ingested: 2026-05-12
original_format: webpage
raw_files:
  - "stripe-machine-payments-x402-2026.md"
tags: [stripe, machine-payments, x402, base, usdc, facilitator, cdp, token-addresses]
---

## Summary

x402 integration guide for machine payments on the Base network. Covers middleware setup, PaymentIntent creation, testing with `purl`, mainnet via CDP Facilitator, and USDC contract addresses for all three supported networks.

## USDC Contract Addresses

| Network | Token | Contract Address |
| --- | --- | --- |
| Tempo | USDC | `0x20c000000000000000000000b9537d11c60e8b50` |
| Base | USDC | `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` |
| Solana | USDC | `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` |

## Mainnet

Use Coinbase Developer Platform (CDP) Facilitator for mainnet x402 transactions. See [CDP x402 guide](https://docs.cdp.coinbase.com/x402/quickstart-for-sellers#running-on-mainnet).

## Key Technical Details

Same implementation as quickstart: `@x402/hono`, `paymentMiddleware`, `createPayToAddress`, Base Sepolia (`eip155:84532`), NodeCache for deposit address caching.

Testing: sandbox doesn't monitor testnets → use `simulate_crypto_deposit` test helper.

## Related Pages

- [[stripe-machine-payments]] — concept page (updated with USDC contract addresses)
- [[source-stripe-machine-payments-x402-quickstart]] — x402 Hono quickstart

## Raw Sources

- [[stripe-machine-payments-x402-2026]] — verbatim x402 integration guide (231 lines)
