---
title: "Stripe — Crypto Onramp: Embedded Components (Headless) Quickstart"
type: source
date_ingested: 2026-05-11
original_format: notes
raw_files:
  - "stripe-crypto-onramp-embedded-components-2026.md"
tags: [stripe, crypto, onramp, embedded-components, headless, link-auth, oauth, mobile, react-native, private-preview]
---

## Summary

Quickstart for the Embedded Components (headless) onramp — the private preview, mobile-first integration mode. Uses Link OAuth authentication and a custom UI state machine rather than an iframe widget. Supports JS/iOS/Android/React Native SDKs.

## Key Differences from Embedded Onramp

| | Embedded (iframe) | Embedded Components (headless) |
| --- | --- | --- |
| UI | Stripe-hosted iframe widget | Fully custom UI via SDK methods |
| Auth | Session client_secret | Link OAuth → crypto_customer_id |
| SDK | `loadStripeOnramp` | `loadCryptoOnrampAndInitialize` |
| Status | Public preview | **Private preview** |
| API version | Standard | `Stripe-Version: 2026-03-25.dahlia;crypto_onramp_beta=v2` |

## Server-Side Flow

1. **Create LinkAuthIntent**: `POST https://login.link.com/v1/link_auth_intent` with OAuth scopes (`crypto:ramp,kyc.status:read`)
2. **Exchange tokens**: `POST https://login.link.com/v1/link_auth_intent/:id/tokens` → access token; use in `Stripe-OAuth-Token` header; never expose to client
3. **Refresh token**: `POST https://login.link.com/auth/token` with `grant_type=refresh_token` + `LINK_CLIENT_ID`/`LINK_CLIENT_SECRET`
4. **Retrieve CryptoCustomer**: check KYC + verification status
5. **List ConsumerWallets / PaymentTokens**: determine what setup is needed
6. **Create CryptoOnrampSession**: `ui_mode: 'headless'` + `crypto_customer_id` + `payment_token` + amount/currency/network/wallet
7. **Refresh quote**: `POST /v1/crypto/onramp_sessions/:id/quote` (expired quote → HTTP 400 at checkout)
8. **Checkout**: `POST /v1/crypto/onramp_sessions/:id/checkout` with `mandate_data` (online, IP, user-agent) → returns `client_secret` for 3DS

## Client-Side State Machine

```
auth → [kyc] → [verify] → [wallet] → [payment] → checkout → complete
```

SDK methods by step:
- `registerLinkUser(email, phone, country)` — create Link account if 404
- `authenticate(authIntentId, callback)` — callback returns `crypto_customer_id`
- `submitKycInfo({...})` — personal details (uses sandbox: `address_full_match`, SSN `000000000`)
- `verifyDocuments()` — ID document verification
- `registerWalletAddress(address, network)`
- `collectPaymentMethod({ payment_method_types, wallets })` → `cryptoPaymentToken`
- `performCheckout(sessionId, fetchClientSecret)` — handles 3DS

## Related Pages

- [[stripe-crypto-onramp]] — concept page (updated with embedded components mode)
- [[source-stripe-crypto-onramp-embedded-setup]] — embedded (iframe) extended guide

## Raw Sources

- [[stripe-crypto-onramp-embedded-components-2026]] — verbatim embedded components quickstart (markdown-formatted from raw UI text)
