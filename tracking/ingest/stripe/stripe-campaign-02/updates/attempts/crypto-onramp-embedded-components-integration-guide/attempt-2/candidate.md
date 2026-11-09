---
title: "Stripe — Crypto Onramp: Embedded Components Integration Guide"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide"
raw_files:
  - "stripe-crypto-onramp-embedded-components-integration-2026.md"
tags: [stripe, crypto, onramp, embedded-components, headless, link-auth, oauth, web, react-native, android, ios, private-preview]
---

## Overview

The May 2026 capture is the full Embedded Components (headless) onramp integration guide for Web, React Native, Android, and iOS. The November 7 capture of the same base URL is a 16-line **platform variant index** linking to those four platform-specific URLs. It does not contain their current guide bodies. The base-page rendering change alone does not establish deprecation, current feature availability, API changes, or continued eligibility. The implementation details below are dated to the May capture.

## Key takeaways from the May guide

- **Access and geography:** The May guide describes a private preview for US users excluding New York. Onboarding and the required Embedded Components and Link OAuth feature gates, Link payment method, and provisioned OAuth credentials are prerequisites; even sandbox API calls depend on onboarding. These are May qualifications, not a November eligibility check.
- **Platform identity:** Web uses `@stripe/crypto` and `loadCryptoOnrampAndInitialize`; React Native uses `useOnramp`; Android uses `OnrampCoordinator` and a Presenter; iOS uses `CryptoOnrampCoordinator` with the alpha import. Methods in one platform section should not be transferred to another.
- **Authentication and tokens:** A back end creates a `LinkAuthIntent` and exchanges it after customer consent. Subsequent onramp requests use `Stripe-OAuth-Token`. The May token response gives the access token a one-hour life; refresh can return a replacement refresh token, which must be stored securely. The May iOS section separately documents returning-customer seamless sign-in: retain the consented LinkAuthIntent token, exchange it for a `linkAuthTokenClientSecret` through the back end, then call `authenticateUserWithToken(_:) `; invalid tokens fall back to `authorize`. This is not established as a React Native flow by the assigned guide.
- **Conditional identity checks:** Check the CryptoCustomer verification state before collecting KYC and identity documents. Web uses `submitKycInfo` and `verifyDocuments` when needed. React Native uses `attachKycInfo`, `presentKycInfoVerification` to review existing KYC or update only an address, and `verifyIdentity` when required. Android uses `verifyKycInfo`; iOS uses `verifyKYCInfo(updatedAddress:from:)`. The prior summary's `verifyKycAndUpdateAddress()` name is not the React Native method in the May guide.
- **Checkout sequence:** Register a valid customer wallet, collect a payment method, create a payment token, have the back end create a headless `CryptoOnrampSession`, then perform checkout. Supply `source_amount` or `destination_amount`, not both; the May examples require the destination network array to match the singular pinned network when a wallet address is set. For ACH in the May **Web** section, checkout also requires `mandate_data` plus collection of the user's IP address and user agent (old raw line 430). The **React Native, Android, and iOS** sections instead say the API may report `mandate_data` missing; collect acceptance and send it on a later checkout call if required (old raw lines 1423, 2093, 2878).
- **A response can still need action:** The May guide says a checkout HTTP `200` or `202` can include `transaction_details.last_error` while the purchase is incomplete. `action_required` calls for authentication and another checkout call; missing KYC, document verification, or consumer wallet requires the relevant platform step; an expired charged quote needs a back-end refresh. `transaction_limit_reached`, `location_not_supported`, and `transaction_failed` call for the stated limit, regional, or failure handling. These are checkout remedies, not evidence of a completed purchase or onchain delivery.
- **Networks and tests:** The May Web `CryptoNetwork` type lists 13 enum values: bitcoin, ethereum, solana, polygon, stellar, avalanche, base, aptos, optimism, worldchain, xrpl, sui, tempo. This is a type list, not a guarantee that every currency, network, region, account, or mode is enabled. The iOS section has a separate livemode currency-network table. Sandbox uses test keys and no real charges or KYC; mobile SDK calls require trusted-app registration, including in sandbox. Live testing uses live keys, real charges and KYC, and a physical iOS or Android device.

## Detail locators in the May capture

- Web setup, Link authorization, KYC, wallet/payment/session/checkout, errors, and `CryptoNetwork`: old raw lines 8–758.
- React Native `useOnramp`, KYC review/address flow, checkout errors, and device/test conditions: old raw lines 759–1577, especially 1153–1210, 1423–1475, and 1560–1576.
- Android coordinator, KYC, checkout, and troubleshooting: old raw lines 1578–2195, especially 1897–1926 and 2093–2149.
- iOS coordinator, retained-token sign-in, KYC, checkout, currency-network tables, and testing: old raw lines 2196–3038, especially 2425–2444, 2652–2674, 2878–2922, and 2975–3037.
- LinkAuthIntent create, token exchange, and refresh APIs, scopes and response fields: old raw lines 3039–3189.

## Related

- [[stripe-crypto-onramp]] — concept and related onramp source routes.
- [[source-stripe-crypto-onramp-embedded-components]] — Embedded Components quickstart.
- The May capture and November index do not establish account-specific gates, current platform API signatures, a successful live checkout, final onchain delivery, or current regional/currency eligibility.

## Raw Sources

- [[raw/stripe-crypto-onramp-embedded-components-integration-2026|May 2026 full Web, React Native, Android, and iOS guide]]

## Related raw API references

- [[raw/stripe-crypto-onramp-embedded-components-integration-guide-2026-11-07|November 7 platform variant index]] — navigation only; the linked variant bodies were not captured in this job.
- [Web](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md?platform=web)
- [React Native](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md?platform=react-native)
- [Android](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md?platform=android)
- [iOS](https://docs.stripe.com/crypto/onramp/embedded-components-integration-guide.md?platform=ios)
