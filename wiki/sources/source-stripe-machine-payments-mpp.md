---
title: "Stripe — MPP Payments Integration Guide"
type: source
date_ingested: 2026-05-12
original_format: webpage
raw_files:
  - "stripe-machine-payments-mpp-2026.md"
tags: [stripe, machine-payments, mpp, x402, usdc, spt, shared-payment-token, tempo, crypto, stablecoin]
---

## Summary

Implementation guide for Machine Payments Protocol (MPP) using the `mppx` Node.js library. Covers both payment methods (crypto on-chain and SPT fiat), PaymentIntent creation, testing, and live mode setup.

## MPP Flow

HTTP 402 → client pays → server returns content + receipt. Implemented via `mppx` middleware.

## Two Methods

| Method | Implementation | Settlement |
| --- | --- | --- |
| Crypto | `tempo.charge({ currency, recipient, testnet })` → deposit address | On-chain (Stripe auto-captures) |
| SPT | `stripe.charge({ networkId, paymentMethodTypes, secretKey })` | Stripe payment rails |

## `mppx` Library Pattern

```js
const mppx = Mppx.create({ methods: [...], secretKey: mppSecretKey });
const result = await mppx.charge({ amount, currency })(request);
if (result.status === 402) return result.challenge;
return result.withReceipt(Response.json({ data }));
```

## Crypto PaymentIntent

API version: `Stripe-Version: 2026-03-04.preview`

```js
stripe.paymentIntents.create({
  payment_method_types: ['crypto'],
  payment_method_options: { crypto: { mode: 'deposit', deposit_options: { networks: ['tempo'] } } },
  confirm: true
})
// → next_action.crypto_display_details.deposit_addresses.tempo.address
```

Cache deposit address in-memory (Redis for production, 5-min TTL). Stripe auto-captures on-chain settlement.

## SPT PaymentIntent

Created automatically by `stripe.charge` method when it receives a valid SPT credential.

## Testing

**Crypto**: sandbox doesn't monitor testnets → use `POST /v1/payment_intents/:id/simulate_crypto_deposit`; `npx mppx account create && fund && http://localhost:4242/paid`

**SPT**: `link-cli` — `spend-request create --credential-type shared_payment_token --network-id profile_test_xxx --test`; then `mpp pay` against endpoint

## Live Mode

- Crypto: remove `testnet: true`; use mainnet USDC address (`0x20c000000000000000000000b9537d11c60e8b50`)
- SPT: switch to live `profile_` ID and live secret key

## Related Pages

- [[stripe-machine-payments]] — concept page (updated with MPP details)
- [[source-stripe-machine-payments]] — overview source

## Raw Sources

- [[stripe-machine-payments-mpp-2026]] — verbatim MPP integration guide (441 lines)
