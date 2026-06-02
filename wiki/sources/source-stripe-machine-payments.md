---
title: "Stripe — Machine Payments"
type: source
date_ingested: 2026-05-12
original_format: notes
raw_files:
  - "stripe-machine-payments-2026.md"
tags: [stripe, machine-payments, mpp, x402, agentic-commerce, usdc, stablecoin, frontier, base, solana, tempo]
---

## Summary

"Frontier" product enabling machine-to-machine payments — agents pay for API calls/services programmatically using crypto (USDC) or Stripe card networks. Settles in fiat in Stripe balance.

## Two Perspectives

| | Use case |
| --- | --- |
| **Sellers** | Pay-per-use API billing (≥ 0.01 USDC); paywall for data/content |
| **Agents** | No account/API key needed — just a crypto wallet; pay per invocation |

## Features

- Settles in fiat in Stripe balance (same metrics/reporting/payouts as other Stripe payments)
- Refunds: stablecoin refunds go to "From" wallet address
- Microtransactions: min 0.01 USDC
- Privacy: unique deposit address per payment
- US only: SPT card payments nationwide (US legal entity); stablecoin: all states except NY and TX

## Supported Networks

| Network | Protocol | Currency |
| --- | --- | --- |
| Base | x402 | USDC |
| Solana | MPP | USDC |
| Tempo | MPP | USDC |
| Stripe card networks | MPP | Stripe currencies |

## Two Protocols

- **MPP (Machine Payments Protocol)**: works with Solana, Tempo, and Stripe card networks
- **x402**: HTTP payment protocol for Base/USDC

## Related Pages

- [[stripe-machine-payments]] — concept page
- [[stripe-agentic-commerce]] — broader agentic commerce context

## Raw Sources

- [[stripe-machine-payments-2026]] — formatted from structured UI text (machine payments overview)
