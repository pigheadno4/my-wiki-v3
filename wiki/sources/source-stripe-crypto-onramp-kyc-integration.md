---
title: "Stripe — Crypto Onramp: KYC Tier Integration Guide"
type: source
date_ingested: 2026-11-09
original_format: webpage
canonical_url: "https://docs.stripe.com/crypto/onramp/kyc-integration-guide"
raw_files:
  - "stripe-crypto-onramp-kyc-integration-guide-2026-11-07.md"
  - "stripe-crypto-onramp-kyc-integration-2026.md"
tags: [stripe, crypto, onramp, kyc, embedded-components, identity-verification, private-preview]
---

## Overview

Stripe's Embedded Components onramp KYC guide describes L0/L1/L2 identity tiers, asynchronous verification, CryptoCustomer status checks, and how to respond to token or session errors. All customers must pass sufficient KYC before buying crypto; collecting a payment method, submitting information, creating a payment token, and completing a purchase are separate steps. The guide assumes the Embedded Components integration. Its November 2026 capture adds a **mobile Platform Pay collection-before-KYC path**, EU-customer qualifications, and a narrower meaning for the minimum-identity error.

> [!warning] Contradiction
> The 2026-05-11 guide said L0 information must be submitted before collecting payment methods. The 2026-11-07 guide explicitly permits **Apple Pay or Google Pay** collection before Link registration/authentication and KYC submission on **iOS, Android, and React Native**. This does not authorize the same order for every payment method. Registration or authentication and minimum identity submission still precede `createCryptoPaymentToken`; collection alone verifies no one and completes no purchase.

> [!warning] Contradiction
> A separate 2026-05-11 Embedded Components integration capture described headless access as private preview and US-only excluding New York. This November KYC guide says EU customers have additional identifier and attestation requirements, but links an EU guide not read for this update. The captures do not settle current region or merchant eligibility, nor remove the older access qualification.

## KYC tiers and API boundaries

| Tier | Customer information in guide's tier table | Verification route |
| --- | --- | --- |
| L0 | Name, phone, email, address | `attachKYCInfo` for first name, last name, address |
| L1 | L0 plus date of birth and SSN | `attachKYCInfo` adds `dateOfBirth`, `idNumber`, `idType` |
| L2 | L1 plus photo ID and selfie | Stripe-hosted `verifyIdentity` |

The tier table describes **customer information**, not one `attachKYCInfo` request body. In the new mobile Platform Pay path, wallet email and phone support **Link registration**; wallet name and address can prefill L0; submit `firstName`, `lastName`, and `address` through `attachKYCInfo` (`attachKycInfo` on Android/React Native). The guide explicitly says email and phone are **not** submitted through the KYC API (November lines 21–38).

L0 and L1 verification are asynchronous: after submission, retrieve/check status until no verification is pending before creating a CryptoOnrampSession; session creation returns HTTP 400 while verification is pending. L2 document/selfie verification is also asynchronous and its result is available from CryptoCustomer. See November lines 40–46.

## Payment-token and session errors

- **Minimum identity:** The November guide interprets `crypto_onramp_missing_minimum_identity_verification` as missing **minimum identity submission** before token/session creation, whereas the May error table said L0 verification failed. Complete Link registration/authentication and any missing contact details, then submit the name/address KYC fields. November line 131 loosely says to send all name/phone/email/address through `attachKYCInfo`, conflicting with the explicit API split at line 38; do **not** infer that phone or email belong in that KYC call. If minimum information was submitted but L0 verification failed, the guide says the customer may still use the onramp after completing L1, which supersedes L0 (November lines 48–52, 129–131; May lines 43–45, 126–129).
- **L1 required:** `crypto_onramp_missing_identity_verification` may mean an attempted L1 did not pass or a verified L0 transaction requires L1. Inspect `kyc_tiers`; from current L0 the guide gives a partial submission of only `dob`, `id_number`, `id_type`; from current L1, collect full L1 information. See November lines 132–136.
- **L2 required:** `crypto_onramp_missing_document_verification` can reflect an L2 failure, a transaction requiring L2 from verified L0/L1, **or a risk-rule identity challenge even below the current tier's amount limit**. Inspect `kyc_tiers`; use `verifyIdentity` for L1/L2, and the guide's partial L1 step before `verifyIdentity` for L0. See November lines 137–144.

## Status interpretation

Retrieve CryptoCustomer by `customerId` and inspect `kyc_tiers`. The guide defines **current tier** as the highest tier with status other than `not_available` or `not_started`; `pending` and `rejected` count as attempted, **not verified**. Verify a tier only when its own `verification_status` is `verified`. Other values are `not_available`, `not_started`, `pending`, and `rejected`. The guide also lists the deprecated `verifications` fallback and a `provided_fields` table; consult November lines 54–115 for the exact response schema and example.

## Related

- [[stripe-crypto-onramp]] — onramp modes, historical access scope, and related sources.
- [[stripe]] — Stripe provider.
- [[source-stripe-crypto-onramp-embedded-components-integration]] — separate Embedded Components integration guide with May 2026 regional/access qualifications.

## Raw Sources

- [[raw/stripe-crypto-onramp-kyc-integration-guide-2026-11-07|Embedded Components KYC guide, 2026-11-07]] — new Platform Pay sequencing, identity/error semantics, EU note and risk challenge.
- [[raw/stripe-crypto-onramp-kyc-integration-2026|Embedded Components KYC guide, 2026-05-11]] — earlier KYC sequence and tier/error table.
