---
title: "GitHub: braintree/braintree-android-drop-in"
type: source
date_ingested: 2026-08-13
original_format: github-repo
raw_files:
  - "github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/manifest.json"
tags: [braintree, android, mobile-sdk, drop-in, paypal, venmo, google-pay, cards, 3d-secure, github-repository]
---

## Overview

`drop-in@6.17.0` is the first retained exact-SHA baseline for Braintree's prebuilt Android payment-selection UI. It presents eligible cards, PayPal, Venmo, and Google Pay, then returns a payment-method nonce and device data for merchant-server processing.

Repository: <https://github.com/braintree/braintree-android-drop-in>

## Version and Dependency Boundary

The retained tag resolves to SHA `da8a702bb37e3a4567e5ba4dd8cbc2257acc37c7`. Its build targets Android API 35, compiles against API 34, requires API 21+, and exposes Java 8 bytecode compatibility. Exact `6.17.0` pins its Braintree Android modules to `4.50.0` and card form to `5.4.0`.

This repository is independently versioned from `braintree/braintree_android`. The separately retained `braintree-android@5.30.0` source is newer modular-SDK evidence and must not be attributed to this Drop-in release. In particular, v5 request, launcher, browser-fallback, and module behavior require separate verification before being applied to Drop-in.

## Grounding Excerpts

> "Braintree Android Drop-In is a readymade UI that allows you to accept card and alternative payments in your Android app."
>
> `raw/github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/files/README.md:5`

> "use the result to update your UI and send the payment method nonce to your server"
>
> `raw/github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/files/README.md:89`

> "A payment method will only be returned when using a client token created with a `customer_id`."
>
> `raw/github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/files/README.md:136`

## Launch, Result, and Server Handoff

Merchants create a `DropInClient` with a tokenization key, client token, or asynchronous `ClientTokenProvider`, attach a `DropInListener`, and launch a configured `DropInRequest`. A successful `DropInResult` normally contains the selected payment type, display description, payment-method nonce, and collected device data. The demo sends the nonce to its server together with the applicable merchant account and optional 3D Secure requirement; Drop-in does not create the server-side transaction itself.

`fetchMostRecentPaymentMethod` requires a client token and only returns a stored method when that token contains a customer ID. Google Pay is a special case: the result can identify it as the last-used type without returning a reusable nonce, so the buyer must perform Google Pay again at checkout.

## Payment Methods and Eligibility

- PayPal appears only when the request does not disable it and remote configuration enables it. Without an explicit PayPal request, Drop-in creates a PayPal vault request. Supplying a request without an amount selects billing-agreement vaulting; supplying an amount selects one-time checkout.
- Venmo appears only when the request does not disable it, remote configuration enables it, and Venmo app switch is available on the device. Without an explicit request, Drop-in uses single-use Venmo without vaulting. This exact Drop-in implementation does not establish the modular v5 mobile-browser fallback.
- Cards appear when not disabled and remote configuration has a supported card type. UnionPay is handled through the card flow only when remote UnionPay configuration is enabled.
- Google Pay appears only when not disabled and the device passes `isReadyToPay`; the merchant must supply an appropriate `GooglePayRequest`.

Source presence and a visible option do not prove merchant enablement, buyer eligibility, regional availability, or successful server processing.

## Vaulting and Vault Manager

A customer-scoped client token enables retrieval of saved card, PayPal, and Venmo methods. Card vaulting defaults on, but the merchant can change the default and optionally show a buyer override. Enabling the vault manager lets buyers remove eligible saved methods; deletion requires a client token associated with the customer.

Saved methods are filtered against the same request and remote-configuration gates as new methods. Selecting a saved method still returns a nonce and fresh device data; eligible saved cards can also be sent through 3D Secure before completion.

## 3D Secure, Risk Data, and Redirects

Attaching a `ThreeDSecureRequest` with an amount causes verification when remote 3D Secure is enabled and the selected nonce is a card or a non-network-tokenized Google Pay card. The merchant remains responsible for supplying useful customer and address data and enforcing server-side liability requirements.

Drop-in collects device data for successful payment selections. The `DropInRequest(boolean hasUserLocationConsent)` constructor communicates location-consent status to the collector; the no-argument constructor is deprecated and reports no consent. Device data is a server-side risk input, not proof that a fraud product is enabled.

PayPal and 3D Secure browser-switch returns are handled internally. A merchant only needs a custom URL scheme when its application ID or redirect setup cannot use the default manifest placeholder, in which case the manifest intent filter and `DropInRequest.customUrlScheme` must agree.

## Release Findings

Exact `6.17.0` adds no new Drop-in payment feature; it updates all pinned Braintree Android modules from the prior line to `4.50.0`. The repository README also warns that integrations must use `6.16.0+` for the 2025 certificate transition. Historical changelog entries establish prior v6 additions and fixes, including location-consent handling, custom URL schemes, payment-method deletion APIs, card-logo controls, client-token invalidation, and API migrations. Those entries are context, not separately retained exact-SHA baselines.

## Evidence Boundaries

The capsule retains public and implementation source, demo integration, layouts, localization, Gradle metadata, migration guidance, and the repository changelog. Tests, fixtures, CI, documentation output, and binary image assets are excluded. Repetitive localized and presentation resources were read and hash-audited; they establish UI and language coverage rather than payment behavior.

No prior exact-SHA Android Drop-in snapshot exists in the wiki. Version-to-version claims before `6.17.0` rely on the repository changelog rather than retained source comparisons.

## Related

- [[changelog-github-braintree-android-drop-in]] - package-qualified Android Drop-in release ledger
- [[source-github-braintree-android]] - independently versioned modular Braintree Android SDK
- [[braintree-android-sdk]] - native Android SDK and Drop-in concept boundary
- [[source-github-braintree-ios-drop-in]] - independently versioned iOS Drop-in implementation
- [[braintree-web-drop-in]] - independently versioned browser Drop-in
- [[braintree]] - company and knowledge-status page

## Raw Sources

- Snapshot manifest: `raw/github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/manifest.json`
- Release manifest: `raw/github/braintree/braintree-android-drop-in/releases/drop-in/6.17.0/2026-08-13/manifest.json`
- Release notes: `raw/github/braintree/braintree-android-drop-in/releases/drop-in/6.17.0/2026-08-13/release-notes.md`
- README: `raw/github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/files/README.md`
- Repository changelog: `raw/github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/files/CHANGELOG.md`
- Migration guide: `raw/github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/files/v6_MIGRATION_GUIDE.md`
- Build metadata: `raw/github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/files/build.gradle`
- Public and implementation API: `raw/github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/files/Drop-In/src/main/java/com/braintreepayments/api/`
- Demo integration: `raw/github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/files/Demo/src/main/java/com/braintreepayments/demo/`
