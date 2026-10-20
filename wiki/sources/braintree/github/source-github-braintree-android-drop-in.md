---
title: "GitHub: braintree/braintree-android-drop-in"
type: source
date_ingested: 2026-08-13
date_updated: 2026-10-20
original_format: github-repo
raw_files:
  - "github/braintree/braintree-android-drop-in/snapshots/2026-10-20-72c0586/manifest.json"
  - "github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/manifest.json"
tags: [braintree, android, mobile-sdk, drop-in, paypal, venmo, google-pay, cards, 3d-secure, github-repository]
---

## Overview

`drop-in@6.17.0` is the first retained exact-SHA baseline for Braintree's prebuilt Android payment-selection UI. It presents eligible cards, PayPal, Venmo, and Google Pay, then returns a payment-method nonce and device data for merchant-server processing.

Repository: <https://github.com/braintree/braintree-android-drop-in>

The later commit-qualified delta `default-branch@72c0586` is retained below for lifecycle notices and build metadata. It is not a new package release and does not replace the `drop-in@6.17.0` implementation baseline.

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

## `default-branch@72c0586` Lifecycle and Metadata Delta

Approved delta ingest on 2026-10-20: release SHA `da8a702bb37e3a4567e5ba4dd8cbc2257acc37c7` -> default-branch SHA `72c05861a0e903e19bc9baca8bc0740b0b1ed57c`, committed 2026-04-23. Collection date and ingest date are not the upstream release date. The stable release identity remains `drop-in@6.17.0`; no `6.17.1` release record is created.

### Lifecycle and Certificate Notices

The [pinned README](../../../../raw/github/braintree/braintree-android-drop-in/snapshots/2026-10-20-72c0586/files/README.md) adds deprecation on September 1, 2026 and unsupported status on September 1, 2027. It states that updates stop at deprecation, processing support continues for one year after that date, and processing for unsupported SDKs can be suspended at any time. Its recommendation is to migrate to the independently versioned [modular SDK source](source-github-braintree-android.md), not to assume Drop-in inherits modular v5 capabilities. These are policy statements captured at this commit, not a verified outage, guaranteed processing outcome, or a complete replacement-integration guide.

> [!warning] Contradiction
> The retained release README's Active/TBA lifecycle table and invalid June 31, 2025 certificate date are superseded by this later commit's notices. The later certificate warning identifies Drop-in versions 5.4.2 through 6.15.0 and March 30, 2026, directing upgrades to 6.16.0+; it also tells older versions to upgrade. As of the 2026-10-20 ingest the scheduled deprecation date has passed, even though this historical README still calls the SDK Inactive and uses future tense. Do not treat that stale label as a support extension. The original `6.17.0` findings above remain historical evidence; the same discrepancy is recorded in [[braintree-android-sdk]].

### Build and Migration Boundaries

The [root Gradle file](../../../../raw/github/braintree/braintree-android-drop-in/snapshots/2026-10-20-72c0586/files/build.gradle) changes project version `6.17.0` -> `6.17.1-SNAPSHOT` and version code 109 -> 110. The README changes its preview dependency from `6.16.1-SNAPSHOT` to `6.17.1-SNAPSHOT`, while its stable example remains `6.17.0`. A development snapshot string is not a published stable version. The Braintree Android module pin remains 4.50.0; compile/minimum/target API levels remain 34/21/35. Payment source, public APIs, demo logic and cumulative changelog do not change at this Git boundary.

The assigned [v6 migration guide](../../../../raw/github/braintree/braintree-android-drop-in/snapshots/2026-10-20-72c0586/files/v6_MIGRATION_GUIDE.md) retains the same upstream Git blob as the baseline: Drop-in v6 requires modular SDK v4, moves authorization into DropInClient, returns a nonce for server processing, and owns browser switching subject to the custom-scheme override. This is older v5-to-v6 Drop-in guidance, not new modular migration instructions. Do not present its existing APIs or examples as newly introduced here.

### Evidence Reconciliation and Reading Scope

Both snapshots retain 165 files; all 330 stored hashes and sizes were verified. Git reports only two modified paths, README.md and build.gradle. The packet reports three stored-content changes and 162 unchanged files because the older migration guide was locally credential-redacted and lacks the final extra newline; its upstream blob is unchanged. The old root Gradle credential value was also locally redacted, but the upstream patch changes only version and version code there. These representation differences do not prove credential rotation, a new migration, or implementation changes. Existing raw evidence remains untouched, and upstream credential values are not reproduced in this wiki summary.

Under the user's explicit focused-reading exception, the three assigned changed files, affected prior files, cumulative source/changelog and comparison were read fully; manifests were mechanically verified and only relevant company/index/log sections read. Credential values were omitted from display, not modified in raw. This is not a whole-repository semantic reread, Android build, dependency resolution, browser/app-switch test or payment execution. No cross-company comparison is warranted. No evidence gaps or unclassified changes were reported by the packet.

### Grounding Excerpts for the Commit Delta

> `Processing for unsupported SDKs can be suspended at any time.`
>
> [README, line 8](../../../../raw/github/braintree/braintree-android-drop-in/snapshots/2026-10-20-72c0586/files/README.md#L8)

> `Please migrate to the [Braintree SDK](https://github.com/braintree/braintree_android) to continue processing and receiving updates.`
>
> [README, line 10](../../../../raw/github/braintree/braintree-android-drop-in/snapshots/2026-10-20-72c0586/files/README.md#L10)

> `version '6.17.1-SNAPSHOT'`
>
> [Root Gradle file, line 39](../../../../raw/github/braintree/braintree-android-drop-in/snapshots/2026-10-20-72c0586/files/build.gradle#L39)

> `ext.brainTreeVersion = "4.50.0"`
>
> [Root Gradle file, line 10](../../../../raw/github/braintree/braintree-android-drop-in/snapshots/2026-10-20-72c0586/files/build.gradle#L10)

## Related

- [[changelog-github-braintree-android-drop-in]] - package-qualified Android Drop-in release ledger
- [[source-github-braintree-android]] - independently versioned modular Braintree Android SDK
- [[braintree-android-sdk]] - native Android SDK and Drop-in concept boundary
- [[source-github-braintree-ios-drop-in]] - independently versioned iOS Drop-in implementation
- [[braintree-web-drop-in]] - independently versioned browser Drop-in
- [[braintree]] - company and knowledge-status page

## Raw Sources

- [Commit snapshot manifest](../../../../raw/github/braintree/braintree-android-drop-in/snapshots/2026-10-20-72c0586/manifest.json)
- [Exact-SHA comparison](../../../../tracking/github/repos/braintree/braintree-android-drop-in/comparisons/default-branch/da8a702--72c0586/comparison.json), [comparison notes](../../../../tracking/github/repos/braintree/braintree-android-drop-in/comparisons/default-branch/da8a702--72c0586/comparison.md) and [upstream patch](../../../../tracking/github/repos/braintree/braintree-android-drop-in/comparisons/default-branch/da8a702--72c0586/diff.patch)
- [Commit README](../../../../raw/github/braintree/braintree-android-drop-in/snapshots/2026-10-20-72c0586/files/README.md), [build metadata](../../../../raw/github/braintree/braintree-android-drop-in/snapshots/2026-10-20-72c0586/files/build.gradle) and [unchanged upstream migration guide](../../../../raw/github/braintree/braintree-android-drop-in/snapshots/2026-10-20-72c0586/files/v6_MIGRATION_GUIDE.md)

- Snapshot manifest: `raw/github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/manifest.json`
- Release manifest: `raw/github/braintree/braintree-android-drop-in/releases/drop-in/6.17.0/2026-08-13/manifest.json`
- Release notes: `raw/github/braintree/braintree-android-drop-in/releases/drop-in/6.17.0/2026-08-13/release-notes.md`
- README: `raw/github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/files/README.md`
- Repository changelog: `raw/github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/files/CHANGELOG.md`
- Migration guide: `raw/github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/files/v6_MIGRATION_GUIDE.md`
- Build metadata: `raw/github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/files/build.gradle`
- Public and implementation API: `raw/github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/files/Drop-In/src/main/java/com/braintreepayments/api/`
- Demo integration: `raw/github/braintree/braintree-android-drop-in/snapshots/2026-08-13-da8a702/files/Demo/src/main/java/com/braintreepayments/demo/`
