---
title: "Stripe — Crypto Onramp: Embedded Setup Guide"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-crypto-onramp-embedded-setup-2026.md"
tags: [stripe, crypto, onramp, embedded, fiat-to-crypto, session-states, quotes-api, mobile, webhook]
---

## Summary

Extended embedded onramp integration guide. Covers SDK installation, session lifecycle states, full parameter pre-population (transaction + customer info), appearance customization, mobile webview integration, Quotes API, webhooks, error handling, session persistence, and use-case configurations (wallet/Dapp/DEX).

## Session States (5)

`initialized` → `rejected` | `requires_payment` → `fulfillment_processing` → `fulfillment_complete`

## Pre-populate Transaction Parameters

`wallet_addresses`, `lock_wallet_address`, `source_currency` (usd/eur), `source_amount` OR `destination_amount` (mutually exclusive), `destination_network`, `destination_currency`, `destination_currencies[]`, `destination_networks[]`

## Pre-populate Customer Information

Email, first_name, last_name, dob (year+month+day — all required together if any), address (country, line1, line2, city, state, postal_code). **SSN cannot be pre-populated.**

## Dark Mode

```js
stripeOnramp.createSession({ clientSecret, appearance: { theme: 'dark' } })
// or after render:
onrampSession.setAppearance({ theme: newTheme })
```

## Sandbox Test Values

- OTP: `000000`
- SSN: `000000000`
- Address line 1: `address_full_match`
- Card: `4242424242424242`

## Quotes API

`GET /v1/crypto/onramp/quotes` — params: `source_currency`, `source_amount` OR `destination_amount`, `destination_currencies[]`, `destination_networks[]`. Response: `destination_network_quotes` with `network_fee_monetary` + `transaction_fee_monetary` per pair.

## Webhook

`crypto.onramp_session.updated` — fires on status changes, NOT on session creation.

## Frontend Events

`onramp_ui_loaded`, `onramp_session_updated`, `onramp_ui_modal_opened`, `onramp_ui_modal_closed`. Use `'*'` to subscribe to all.

## Error Codes (14)

Key codes: `crypto_onramp_disabled`, `crypto_onramp_unsupportable_customer` (HTTP 400 with customer_ip_address), `crypto_onramp_invalid_source_destination_pair`, `crypto_onramp_incomplete_destination_currency_and_network_pair`, `crypto_onramp_invalid_destination_currency_and_network_pair`, `crypto_onramp_merchant_not_properly_setup`. See raw file for full table.

## Mobile Integration

Host onramp at a URL with client_secret in path → mount from URL → listen for `fulfillment_complete`/`rejected` → redirect via universal links. Can redirect at `fulfillment_processing` while polling in background.

## Session Persistence

OnrampSession is stateful server-side resource. Reuse client_secret for returning customers to resume where they left off. Link session to user account or store in local storage for Web3.

## Use Case Configurations

- **Wallet funding**: provide wallet_addresses + destination_networks
- **Transaction top-up**: provide wallet_addresses + destination_network + destination_currency + destination_amount (delta)
- **Dapp/NFT checkout**: provide wallet_addresses + destination_network + destination_currency + destination_amount (full or delta)
- **DEX**: provide wallet_addresses + destination_networks + destination_currencies (restrict to selected crypto)

## Related Pages

- [[stripe-crypto-onramp]] — concept page (updated with session states, sandbox values, quotes API)
- [[source-stripe-crypto-onramp-embedded-quickstart]] — simpler quickstart guide

## Raw Sources

- [[stripe-crypto-onramp-embedded-setup-2026]] — verbatim embedded setup guide (1,081 lines, 1 downloaded image)
