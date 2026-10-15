---
title: "Adyen Classic API authentication-only 3D Secure 2 integration"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/authentication-only-integration"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/authentication-only-integration/2026-09-15.md"
tags: [adyen, 3d-secure, 3ds2, classic-api, authentication-only]
---

## Overview

Adyen's dated Classic Payment API guide describes standalone 3D Secure 2 authentication through `/authorise` and `/authorise3ds2` for web, Android, and iOS. With `threeDSAuthenticationOnly: true`, the merchant authenticates the shopper separately, then uses the returned authentication data to seek a later payment authorization from another PSP or acquirer. Authentication completion alone is neither payment authorization nor proof of a successful charge.

This is the Classic API (`/authorise`) route. Adyen says it no longer accepts new Classic integrations and recommends migrating to the Checkout API standalone-authentication route. The raw page reports `last_modified: 2023-03-07`; it was captured 2026-09-15. Treat API/library examples, scheme cryptogram periods, and support status as dated snapshot guidance.

## Key takeaways

- The merchant needs a test account, API key, library connection, and the relevant web, iOS, or Android 3DS2 integration guide before using this Classic route. The authentication request sends the relevant 3DS2 objects plus `threeDSAuthenticationOnly: true`. See **Before you begin** and the channel-specific **Submit a payment authentication request** sections.
- Issuer-directed results include fingerprinting (`IdentifyShopper`), a challenge (`ChallengeShopper`), a possible 3DS1 redirect (`RedirectShopper`), or `AuthenticationNotRequired`. A frictionless or completed challenge can return `AuthenticationFinished`; merchants must handle the actual result rather than assume success. See the web, Android, and iOS sections and **3D Secure 1 authentication-only fallback**.
- For a successful authentication, the guide identifies `authenticationValue`, `dsTransID`, and `eci` as data needed for a later 3DS2 authorization. It points to the last `AuthenticationFinished` response, `/getAuthenticationResult` (which requires additional Adyen configuration), or `/retrieve3ds2Result` for Cartes Bancaires. See **Get the 3D Secure 2 authenticated data**; verify the exact response field mapping before implementation.
- For later authorization through another acquirer, Adyen strongly recommends matching acquirer enrollment data in authentication and authorization; a mismatch can cause issuer refusal. The extra data is conditional on that cross-acquirer path, and some fields have API-version or scheme-specific requirements. See **Optional: Provide additional acquirer-related data**.
- The merchant may instead choose to continue authorization with Adyen through a separate server-side `/authorise3ds2` request with `threeDSAuthenticationOnly: false` and the appropriate token/status. The guide's `Authorised` response is conditional on payment success, not an authentication-only outcome. See **Optional: Authorise the payment with Adyen**.
- Authentication data and cryptograms expire by card scheme; the page's dated scheme table must not be treated as a universal or current lifetime. See **Authentication data expiry**.

## Detail locators

- **Web-based authentication only** — browser request, result-code branching, device fingerprint, challenge, and Classic `/authorise3ds2` handoff.
- **Android 3D Secure 2 SDK authentication only** and **iOS 3D Secure 2 SDK authentication only** — channel-specific request and fingerprint/challenge paths; language examples are dated illustrations, not validated executable payloads.
- **Get the 3D Secure 2 authenticated data** — field descriptions, response options, Cartes Bancaires route, and extra configuration for `/getAuthenticationResult`.
- **Optional: Provide additional acquirer-related data** — `acquirerBIN`, `acquirerMerchantID`, merchant name, MCC, and Visa/Mastercard requestor identifiers.
- **Optional: Authorise the payment with Adyen** — separate authorization request, token/status selection, and conditional `Authorised` response.
- **Authentication data expiry** and **Testing 3D Secure 2** — dated scheme periods and test-only credentials/scenarios.

## Related

- [[adyen]]
- [[adyen-3d-secure]]
- [[source-adyen-docs-online-payments-3d-secure-standalone-authentication]] — newer Checkout API standalone-authentication route.

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/authentication-only-integration/2026-09-15|Classic API authentication-only integration (2026-09-15 snapshot)]]
