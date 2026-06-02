---
title: "Stripe — x402 Payment Endpoint Builder (Quickstart)"
type: source
date_ingested: 2026-05-12
original_format: notes
raw_files:
  - "stripe-machine-payments-x402-quickstart-2026.md"
tags: [stripe, machine-payments, x402, base, usdc, facilitator, hono, quickstart, node]
---

## Summary

Full Hono/TypeScript quickstart for x402 machine payments on the Base network. Uses `@x402/hono` middleware and an external facilitator for payment proof verification and on-chain settlement.

## Key Differences from MPP Quickstart

| | MPP (Tempo) | x402 (Base) |
| --- | --- | --- |
| Network | Tempo (`tempo`) | Base (`eip155:84532`) |
| Packages | `mppx/server` | `@x402/hono`, `@x402/evm/exact/server`, `@x402/core/server` |
| Middleware | `Mppx.create` + `mppx.charge` | `paymentMiddleware` + `x402ResourceServer` |
| Facilitator | Not needed | Required (`FACILITATOR_URL`); verifies proofs on-chain |
| Payment header | `Authorization` header | Base64-encoded `paymentHeader` → `decoded.payload.authorization.to` |
| Test tool | `npx mppx http://...` | `purl http://...` |

## Facilitator

External service that verifies x402 payment proofs and settles transactions on-chain. For testing: x402.org testnet. For production: run your own or use a trusted third-party.

## Middleware Configuration

```js
paymentMiddleware(
  {
    "GET /paid": {
      accepts: [{
        scheme: "exact",         // exact-amount payment
        price: "$0.01",
        network: "eip155:84532", // Base Sepolia testnet
        payTo: createPayToAddress,
      }],
    },
  },
  new x402ResourceServer(facilitatorClient).register("eip155:84532", new ExactEvmScheme())
)
```

## Deposit Address Flow

Same NodeCache pattern as MPP: check `paymentHeader` for retry (base64-decode → `payload.authorization.to`) → otherwise create new PaymentIntent with `deposit_options: { networks: ["base"] }`.

## Related Pages

- [[stripe-machine-payments]] — concept page (updated with x402 details)
- [[source-stripe-machine-payments-mpp-quickstart]] — MPP Tempo variant

## Raw Sources

- [[stripe-machine-payments-x402-quickstart-2026]] — formatted from x402 quickstart UI (full Hono server code)
