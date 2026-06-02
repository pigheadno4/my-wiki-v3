---
title: "Stripe — Crypto Onramp: Embedded Components Integration Guide"
type: source
date_ingested: 2026-05-11
original_format: webpage
raw_files:
  - "stripe-crypto-onramp-embedded-components-integration-2026.md"
tags: [stripe, crypto, onramp, embedded-components, headless, link-auth, oauth, mobile, react-native, android, private-preview]
---

## Summary

Comprehensive step-by-step integration guide for the Embedded Components (headless) onramp across Web, React Native, and Android. Includes full SDK reference, all error codes, 13 supported networks, testing guide, and LinkAuthIntent API documentation.

## Geo Restriction

**US only, excluding New York** (stricter than embedded iframe onramp which only excludes Hawaii).

## Supported Networks (13)

bitcoin, ethereum, solana, polygon, stellar, avalanche, base, aptos, optimism, worldchain, xrpl, sui, tempo

## Key Differences from Quickstart

Full SDK reference with typed params/returns, `verifyKycAndUpdateAddress()` step (React Native only), Seamless Sign-In for returning customers, `deleteWalletAddress()`, `destroy()`, Android native SDK setup.

## Access Token

TTL: **1 hour**. Refresh token returned on each use — always store the latest. Use in `Stripe-OAuth-Token` header.

## `performCheckout` last_error Codes

| Code | Handle by |
| --- | --- |
| `action_required` | SDK handles 3DS; call checkout again |
| `missing_kyc` | `submitKycInfo()` then retry |
| `missing_document_verification` | `verifyDocuments()` then retry |
| `charged_with_expired_quote` | Refresh quote then retry |
| `missing_consumer_wallet` | `registerWalletAddress()` then retry |
| `transaction_limit_reached` | Show error, do not retry |
| `location_not_supported` | Show regional unavailability, do not retry |
| `transaction_failed` | Show generic error, do not retry |

## Identity Flow Differences

- **Web**: `submitKycInfo()` → `verifyDocuments()`
- **React Native**: adds `verifyKycAndUpdateAddress()` step between KYC and document verification

## Seamless Sign-In (React Native)

For returning customers who have already consented — skip full auth flow using Seamless Sign-In (server-side token exchange only, no OTP screen).

## LinkAuthIntent APIs

- **Create**: `POST https://login.link.com/v1/link_auth_intent` with email, oauth_client_id, oauth_scopes
- **Retrieve access tokens**: `POST https://login.link.com/v1/link_auth_intent/:id/tokens`
- **Refresh**: `POST https://login.link.com/auth/token` with `grant_type=refresh_token`

## Related Pages

- [[stripe-crypto-onramp]] — concept page (updated with geo restriction, networks, error codes)
- [[source-stripe-crypto-onramp-embedded-components]] — embedded components quickstart

## Raw Sources

- [[stripe-crypto-onramp-embedded-components-integration-2026]] — verbatim integration guide, Web + React Native + Android (3,189 lines)
