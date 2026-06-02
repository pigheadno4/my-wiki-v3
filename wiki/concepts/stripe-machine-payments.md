---
title: "Stripe Machine Payments"
type: concept
category: technology
tags: [stripe, machine-payments, mpp, x402, agentic-commerce, usdc, stablecoin, frontier, base, solana]
---

## Overview

Stripe Machine Payments ("Frontier") enables **machine-to-machine payments** — AI agents pay for API calls and services programmatically using crypto (USDC) or Stripe card networks. Payments settle in fiat directly into the seller's Stripe balance.

## Two Roles

**Sellers**: accept pay-per-use billing for API requests (min 0.01 USDC per transaction); paywall data or content; use existing Stripe integration.

**Agents**: pay per API invocation without needing an account or API key — just a crypto wallet.

## Supported Networks and Protocols

| Network | Protocol | Currency |
| --- | --- | --- |
| Base | x402 | USDC |
| Solana | MPP | USDC |
| Tempo | MPP | USDC |
| Stripe card networks | MPP | Stripe currencies |

**MPP** (Machine Payments Protocol): multi-network; covers Solana, Tempo, and Stripe card networks.

**x402**: HTTP-based payment protocol for Base/USDC payments. Uses `@x402/hono` middleware + external **facilitator** (verifies payment proofs on-chain; testnet: x402.org; env: `FACILITATOR_URL`; mainnet: CDP Facilitator). Test with `purl` CLI. Network: `eip155:84532` (Base Sepolia testnet).

**USDC contract addresses**:

| Network | Contract |
| --- | --- |
| Tempo | `0x20c000000000000000000000b9537d11c60e8b50` |
| Base | `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` |
| Solana | `EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` |

## Key Features

- **Min charge**: 0.01 USDC (microtransaction-friendly)
- **Fiat settlement**: payments land in Stripe balance; same reporting, multi-currency payouts as regular payments
- **Privacy**: unique deposit address per payment (reduces on-chain visibility of processing volume)
- **Refunds**: stablecoin refunds returned to "From" wallet address
- **US only**: SPT card payments nationwide (US legal entity); stablecoin: all states except **New York and Texas**

## MPP Implementation (`mppx` library)

HTTP 402 middleware pattern: `Mppx.create({ methods, secretKey })` → `mppx.charge({ amount, currency })(request)` → return `result.challenge` (402) or `result.withReceipt(content)`.

**Crypto**: `tempo.charge({ currency: PATH_USD_address, recipient, testnet })` → `paymentIntents.create({ payment_method_types: ['crypto'], mode: 'deposit', networks: ['tempo'] })` → `next_action.crypto_display_details.deposit_addresses.tempo.address`; cache address; Stripe auto-captures on settlement. API version: `2026-03-04.preview`.

**SPT**: `stripe.charge({ networkId, paymentMethodTypes, secretKey })` — PaymentIntent created automatically from SPT credential.

**Testing**: crypto → `simulate_crypto_deposit` test helper (sandbox doesn't monitor testnets); SPT → `link-cli spend-request create --credential-type shared_payment_token --network-id profile_test_xxx --test`.

## Relationship to Other Products

- [[stripe-agentic-commerce]] — broader agent commerce context (ACS, RequestedSession, OCA)
- [[stripe-stablecoin-payments]] — stablecoin payment acceptance on Stripe

## Sources

- [[source-stripe-machine-payments]] — overview: seller/agent use cases, networks, protocols, geo restrictions
- [[source-stripe-machine-payments-mpp]] — MPP implementation: mppx library, crypto + SPT payment flows, PaymentIntent, testing with link-cli
- [[source-stripe-machine-payments-mpp-quickstart]] — Hono quickstart: /crypto/paid + /spt/paid endpoints, NodeCache deposit address caching pattern
- [[source-stripe-machine-payments-x402-quickstart]] — x402 Hono quickstart: Base network, @x402/hono middleware, facilitator (FACILITATOR_URL), purl testing tool
- [[source-stripe-machine-payments-x402]] — x402 integration guide: USDC contract addresses (Tempo/Base/Solana), CDP mainnet facilitator
