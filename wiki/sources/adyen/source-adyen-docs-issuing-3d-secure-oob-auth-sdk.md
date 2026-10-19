---
title: "Adyen Issuing: Out-of-band Authentication SDK"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/3d-secure/oob-auth-sdk"
raw_files:
  - "adyen/docs/issuing/3d-secure/oob-auth-sdk/2026-09-15.md"
tags: [adyen, issuing, 3d-secure, authentication, mobile-sdk]
---

## Overview

This Adyen Issuing-path guide (last modified 2023-07-12; captured 2026-09-15) introduces **out-of-band (OOB) cardholder authentication** for Adyen-issued cards in the EEA or UK. It describes a separate channel on an eligible cardholder device and a client-side Authentication SDK for iOS and Android. This is issuer-side cardholder authentication; it is distinct from the merchant acquirer's checkout and from the later Issuing payment authorisation and capture decisions. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- **Purpose and prerequisite:** OOB Strong Customer Authentication directs a transaction-authentication request to the platform's application on an eligible cardholder device. For the guide's EEA/UK issued-card flow, the cardholder's device must be **registered**, then used to authenticate a transaction. The user provides two factors: the SDK uses **possession** through device binding plus **knowledge or inherence**, depending on device access configuration. Installing the SDK alone is not device registration or a successful authentication.
- **Implementation route:** Add the Authentication SDK to the iOS/Android app, register the cardholder's Android or iOS mobile device for SCA, and use the SDK for cardholder authentication when a payment requires it. The linked installation, registration and authentication pages own the detailed steps; this overview does not specify request/response contracts, device-platform version requirements, or SDK release versions.
- **Scope qualification:** This overview speaks of Adyen-issued cards in EEA/UK, but its linked [[source-adyen-docs-issuing-3d-secure-oob-auth-sdk-install-sdk-mobile|installation guide]] says in its requirements table that the feature is supported with an **Adyen for Platforms** integration (companion raw lines 29–35). The two pages do not establish Issuing-only account eligibility; check the applicable product setup with Adyen. The parent [[source-adyen-docs-issuing-3d-secure|3D Secure enrollment guide]] also says some online payments are out of SCA scope or exempt and proceed directly to authorisation. Thus the overview's “each time” implementation step does not prove an OOB challenge is required for every card payment.
- Neither device registration nor a completed OOB challenge proves that a particular Issuing payment was authorised, captured, settled, or refunded.

## Detail locators

- OOB channel, EEA/UK issued-card context, registration before authentication, and SCA factors: pinned raw lines 19–27.
- SDK possession/device-binding plus knowledge/inherence behavior: pinned raw line 29.
- Install, register-device and authenticate-cardholder route: pinned raw lines 31–37.
- Installation next-step navigation: pinned raw lines 39–47.

## Related

- [[source-adyen-docs-issuing-3d-secure]] — conditional card enrollment, out-of-scope and exempt payments, later authorisation.
- [[source-adyen-docs-issuing-3d-secure-oob-auth-sdk-install-sdk-mobile]] — detailed mobile SDK prerequisites and conflicting integration-type label.
- [[source-adyen-docs-issuing-payment-stages]] — separate authorisation/capture balance effects.

## Raw Sources

- [[raw/adyen/docs/issuing/3d-secure/oob-auth-sdk/2026-09-15|Adyen Issuing OOB Authentication SDK overview, captured 2026-09-15]]
