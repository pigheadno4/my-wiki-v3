---
title: "Adyen Docs: Third-party authentication"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/3d-secure/authorize-mpidata"
raw_files:
  - "adyen/docs/online-payments/3d-secure/authorize-mpidata/2026-09-15.md"
tags: [adyen, 3d-secure, 3ds2, authentication, authorization, mpi-data]
---

## Overview

This Adyen guide explains how a merchant can authenticate with a third-party 3D Secure 2 provider and then submit the resulting authentication data to Adyen in a separate payment-authorization request. It covers the Checkout API `/payments` route; merchants using the classic `/authorise` endpoint are directed to a separate classic-integration guide.

The snapshot documents request construction and testing guidance. It does not prove current merchant or scheme eligibility, successful third-party authentication, Adyen authorization, capture, settlement, or liability shift for a particular transaction.

## Key takeaways

- The merchant first obtains 3DS2 authentication data from the third-party provider, maps that data to Adyen parameters, and includes it in an `mpiData` object in a POST `/payments` request. Authentication evidence is an input to authorization, not proof that Adyen authorized the payment.
- The documented Checkout route requires `/payments` v46 or later, an Adyen test account, and an API key stored securely. See **Before you begin**.
- Required authentication and request fields vary by card scheme. The guide identifies a common set for all schemes and additional Cartes Bancaires fields; use **Step 1: Get third-party authentication data** and **Step 2: Make a payment with third-party authentication data** for the field-by-field tables.
- For a co-badged card, `paymentMethod.type` must be `scheme` and `paymentMethod.brand` must identify the scheme that performed authentication; the guide warns that a mismatch can lead to refusal.
- For Cartes Bancaires authentication on a co-badged card, the authorization request must carry the same `threeDSRequestorChallengeInd` value as the authentication request; the guide warns that a mismatch can lead to decline.
- An `Authorised` `resultCode` means the payment authorization succeeded; other result codes require their documented follow-up actions. This authorization result remains distinct from the third-party authentication outcome.

## Material qualifications

- This page applies to Checkout API `/payments`; classic `/authorise` integrations are routed elsewhere.
- Field requirements are scheme-dependent, with extra Cartes Bancaires data and conditions.
- Co-badged-card authorization depends on preserving the authenticating scheme and, for Cartes Bancaires, the challenge-indicator value across authentication and authorization.
- The sample request is illustrative and does not establish universal field values, merchant configuration, or a successful live payment.
- End-to-end testing uses test cards created from the authentication provider's card ranges in Adyen's test environment; it is not live-provider or production proof.

## Detail locators

> [!warning] Snapshot field-name conflict
> The Step 2 table and co-badged-card guidance name `threeDS2RequestData.threeDSRequestorChallengeInd` (raw lines 72 and 85), but the sample uses `threeDS2RequestData.challengeIndicator` (lines 121–123). This snapshot does not establish that the fields are equivalent. Verify the Checkout schema for the intended API version before choosing a property; do not normalize the sample into a current contract.

- **Before you begin** — test-account setup, secure API-key handling, and the `/payments` v46-or-later prerequisite.
- **Step 1: Get third-party authentication data** — authentication-result fields and scheme applicability.
- **Step 2: Make a payment with third-party authentication data** — third-party-to-Adyen mapping, `mpiData`, scheme-qualified request fields, recurring/shopper-interaction fields, and the challenge-indicator field-name conflict with the sample (raw lines 72, 85 and 121–123).
- **Co-badged cards** — authenticating-scheme selection and Cartes Bancaires challenge-indicator consistency warnings.
- **Sample request** and **Sample response** — illustrative Checkout v72 payload and authorization-result interpretation.
- **Testing** — test-card creation and the two-step third-party authentication plus Adyen payment sequence.

## Related

- [[adyen]]
- [[adyen-3d-secure]]
- [[co-badged-cards]]

## Raw Sources

- [[raw/adyen/docs/online-payments/3d-secure/authorize-mpidata/2026-09-15|Adyen Docs — Third-party authentication (2026-09-15)]]
