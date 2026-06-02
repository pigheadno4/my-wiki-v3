---
title: "Stripe Fiat-to-Crypto Onramp"
type: concept
category: technology
tags: [stripe, crypto, onramp, fiat-to-crypto, kyc, dapp]
---

## Overview

Stripe's fiat-to-crypto onramp enables customers to purchase and exchange cryptocurrencies directly within a merchant's platform or decentralized application (Dapp). Stripe acts as **merchant of record**, assuming full liability for fraud and disputes, handling KYC verifications, regulatory requirements, and sanctions screening.

Customer payment methods, KYC data, and wallet information are saved with Stripe, reducing friction for repeat onramp sessions.

## Integration Modes

| Mode | Status | Use Case |
| --- | --- | --- |
| **Stripe-hosted** | Public preview | No code required; redirect to crypto.link.com; some customization (amount, currency, network) |
| **Embedded** | Public preview | Embed in website/mobile webview via Onramp API; brand + full parameter customization |
| **Embedded components** (mobile SDK) | Private preview | Native iOS/Android; full UI + parameter customization via Onramp SDK + API |

## Access

Application required at `dashboard.stripe.com/crypto-onramp/get-started`. Reviewed within 48 hours. Required even for sandbox/test access.

## Supported Currencies (US + EU)

ETH, ETH (Base), SOL, POL, MATIC, BTC, AVAX, XLM, USDC (Ethereum/Solana/Polygon/Avalanche/Base/Stellar)

**Geo restrictions**:

- XLM, USDC (Stellar/Avalanche/Polygon): not in New York
- ETH (Base), MATIC, AVAX, USDC (Solana/Polygon/Avalanche/Base): not in EU

## Stripe-Hosted: Two Customization Paths

| Path | Requirements | Capability |
| --- | --- | --- |
| Generate redirect URL (frontend) | No Stripe account | Light customization; no branding |
| Mint session with redirect URL (backend) | Stripe account + API | Full customization incl. wallet address; branding |

Frontend scripts must load from Stripe domains (`js.stripe.com`, `crypto-js.stripe.com`) — never bundle or self-host (PCI requirement).

Session API: `POST /v1/crypto/onramp_sessions` → `redirect_url`, `client_secret`, `transaction_details`.

## Embedded Integration (React + Node.js)

**Packages**: `@stripe/crypto`, `@stripe/stripe-js`

**Server** (custom extension — official library doesn't support onramp API yet):

```js
const OnrampSessionResource = Stripe.StripeResource.extend({
  create: Stripe.StripeResource.method({ method: 'POST', path: 'crypto/onramp_sessions' }),
});
// POST /create-onramp-session → { clientSecret }
// Required params: destination_currency, destination_exchange_amount, destination_network, customer_ip_address
```

**Client**:

```js
const stripeOnramp = await loadStripeOnramp(publishableKey);
stripeOnramp.createSession({ clientSecret, appearance: { theme: 'dark' } }).mount(containerRef);
```

**Events**: `onramp_ui_loaded` (UI ready) and `onramp_session_updated` (status change)

**Sandbox test values**: `destination_currency: 'usdc'`, `destination_exchange_amount: '13.37'`, `destination_network: 'ethereum'`

## Session Lifecycle States

`initialized` → `rejected` | `requires_payment` → `fulfillment_processing` → `fulfillment_complete`

## Quotes API

`GET /v1/crypto/onramp/quotes` — `source_amount` OR `destination_amount`, filter by `destination_currencies[]`/`destination_networks[]`. Response: per currency-network pair with `network_fee_monetary` + `transaction_fee_monetary`.

## Sandbox Test Values

OTP: `000000` | SSN: `000000000` | Address line 1: `address_full_match` | Card: `4242424242424242`

## Payment Methods and Delivery

- Credit, debit, Apple Pay, ACH (US only)
- All eligible for **instant crypto delivery** after KYC completion
- Returning users: faster checkout via [[stripe-link]] consumer account

Every session status change generates a webhook.

## Embedded Components (Headless) Mode

**Private preview** — distinct from the embedded iframe widget. Full custom UI via SDK methods; requires Link OAuth authentication. **US only, excluding New York** (stricter than embedded onramp which excludes Hawaii).

| | Embedded (iframe) | Embedded Components (headless) |
| --- | --- | --- |
| Auth | Session `client_secret` | Link OAuth → `crypto_customer_id` |
| SDK | `loadStripeOnramp` | `loadCryptoOnrampAndInitialize` |
| API version | Standard | `Stripe-Version: 2026-03-25.dahlia;crypto_onramp_beta=v2` |

**Customer setup state machine**: auth → kyc → identity verify → wallet → payment method → checkout

**Key SDK methods**: `registerLinkUser()`, `authenticate()`, `submitKycInfo()`, `verifyDocuments()`, `registerWalletAddress()`, `collectPaymentMethod()`, `performCheckout()`

**KYC tiers** (Embedded Components): L0 (name/phone/email/address) → L1 (+ DOB/SSN) → L2 (+ photo ID/selfie); L0 required before `collectPaymentMethod`; L0/L1 async — poll before creating session; L2 uses `verifyIdentity()`. Session creation returns 400 on pending verifications. Error codes: `crypto_onramp_missing_minimum_identity_verification`, `crypto_onramp_missing_identity_verification`, `crypto_onramp_missing_document_verification` — each has tier-specific next steps.

**Session**: `ui_mode: 'headless'` + `crypto_customer_id` + `payment_token`; checkout requires `mandate_data`; quote refresh needed before expiry.

**Access token TTL**: 1 hour; refresh token returned on each use — store the latest; use in `Stripe-OAuth-Token` header.

**Supported networks (13)**: bitcoin, ethereum, solana, polygon, stellar, avalanche, base, aptos, optimism, worldchain, xrpl, sui, tempo

**`performCheckout` last_error codes**: `action_required` (3DS — retry), `missing_kyc`, `missing_document_verification`, `charged_with_expired_quote`, `missing_consumer_wallet` (all retriable); `transaction_limit_reached`, `location_not_supported`, `transaction_failed` (terminal — do not retry).

## Relationship to Other Crypto Products

- [[stripe-stablecoin-payments]] — accepting stablecoin payments on Stripe (different from onramp: onramp helps customers *buy* crypto; stablecoin payments lets merchants *accept* crypto)

## Sources

- [[source-stripe-crypto-onramp]] — overview: merchant of record role, three integration modes, application process
- [[source-stripe-crypto-onramp-stripe-hosted]] — Stripe-hosted implementation: currencies, geo restrictions, frontend/backend customization paths, session API
- [[source-stripe-crypto-onramp-embedded]] — Embedded overview: payment methods (credit/debit/ApplePay/ACH), instant delivery, Link, webhooks per status change
- [[source-stripe-crypto-onramp-embedded-quickstart]] — Embedded quickstart: Node.js server, React client, OnrampSession API, events, dark mode, sandbox test values
- [[source-stripe-crypto-onramp-embedded-setup]] — Extended setup: session states, customer info pre-population, Quotes API, 14 error codes, mobile integration, session persistence, use-case configs
- [[source-stripe-crypto-onramp-embedded-components]] — Embedded Components (headless) quickstart: Link OAuth flow, state machine, SDK methods, headless session, quote refresh
- [[source-stripe-crypto-onramp-embedded-components-integration]] — Integration guide (Web/RN/Android): geo restriction, 13 networks, last_error codes, SDK reference, LinkAuthIntent APIs
- [[source-stripe-crypto-onramp-kyc-integration]] — KYC tier system: L0/L1/L2 requirements, verification status values, session error codes, tier detection
