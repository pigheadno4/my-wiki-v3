---
title: "GitHub: Adyen/adyen-3ds2-android"
type: source
date_ingested: 2026-08-19
original_format: github-repo
raw_files:
  - "github/adyen/adyen-3ds2-android/snapshots/2026-08-17-de845e6/manifest.json"
tags: [adyen, android, 3d-secure, 3ds2, authentication, mobile-sdk, github-repository]
---

## Overview

`Adyen/adyen-3ds2-android` contains Adyen's standalone native Android runtime for EMV 3-D Secure transactions and challenges. This cumulative page begins with package-qualified release `adyen-3ds2-android@2.2.27` at exact SHA `de845e67488b6aecb1ff57ea7908b662f5ee2d40`.

Repository: <https://github.com/Adyen/adyen-3ds2-android>

## Evidence boundary

- The snapshot proves retained public integration behavior and generated API documentation for `2.2.27`. It does not prove current merchant enablement, issuer behavior, authentication success, liability shift, or regional eligibility.
- The capsule contains the public documentation surface rather than the SDK's implementation source. Internal cryptography, device-data collection logic, and challenge rendering behavior cannot be deep-dived from this snapshot.
- The SDK is a delegated runtime used by Adyen Android. Adyen Android's adapter and this repository remain independently versioned evidence histories.
- Release notes claim a new `DATA_SAFETY_GUIDE.md`, but that file is absent from the exact `2.2.27` snapshot. Its contents are therefore an unresolved evidence gap, not retained knowledge.
- The README compatibility table stops at `2.2.26`; the exact Android compatibility row for `2.2.27` is not established by this snapshot.

## Grounding excerpts

> "With this SDK, you can accept 3D Secure 2.0 payments via Adyen."
>
> `raw/github/adyen/adyen-3ds2-android/snapshots/2026-08-17-de845e6/files/README.md:3`

> "When the transaction is created successfully use the `transaction`'s `authenticationRequestParameters` in your call to `/authorise3ds2`."
>
> `raw/github/adyen/adyen-3ds2-android/snapshots/2026-08-17-de845e6/files/README.md:75-76`

> "When the transaction is finished successfully or not it must be closed."
>
> `raw/github/adyen/adyen-3ds2-android/snapshots/2026-08-17-de845e6/files/README.md:82`

> "We strongly recommend that you provide the `threeDSRequestorAppURL` parameter as an Android App Link instead of custom link."
>
> `raw/github/adyen/adyen-3ds2-android/snapshots/2026-08-17-de845e6/files/README.md:91-93`

> "Data Safety Guide: Added `DATA_SAFETY_GUIDE.md`"
>
> `raw/github/adyen/adyen-3ds2-android/releases/adyen-3ds2-android/2.2.27/2026-08-17/release-notes.md:2`

## Distribution and version

The artifact is available from Maven Central as `com.adyen.threeds:adyen-3ds2:2.2.27`; the README also documents manual AAR installation. The retained README's compatibility table identifies `2.2.26` with Android API 36/Android 16 but omits `2.2.27`, so compatibility for the retained release should be verified independently rather than inferred from the previous row.

## Transaction and server flow

The app builds `ConfigParameters` from the directory-server ID, public key, and root certificates returned by Adyen. `ThreeDS2Service.initialize` performs security checks and device-information collection, after which `createTransaction` creates a single-use `Transaction` for the selected protocol message version.

`AuthenticationRequestParameters` contains encrypted JWE device data, an SDK transaction UUID, SDK App ID, SDK reference number, ephemeral public key, and message version. The merchant app submits those values through its server to `/authorise3ds2`. Initialization or transaction-creation failures instead expose `transactionStatus` and `additionalDetails` for the follow-up call.

## Challenge flow and outcomes

When Adyen requires a challenge, the app builds `ChallengeParameters` from the 3DS Server transaction ID, ACS transaction ID, ACS reference number, ACS signed content, and `threeDSRequestorAppURL`. The SDK strongly recommends an Android App Link for app-return handling; the older embedded URL helper is deprecated.

`Transaction.doChallenge` hands control to the SDK and accepts a timeout in minutes. The current callback is `ChallengeStatusHandler`, which receives one of four results:

| Result | Meaning | Follow-up evidence |
| --- | --- | --- |
| `Completed` | Challenge completed | Submit `transactionStatus` to `/authorise3ds2` |
| `Cancelled` | Shopper cancelled | Submit `transactionStatus` and `additionalDetails` |
| `Timeout` | Challenge exceeded the configured timeout | Submit `transactionStatus` and `additionalDetails` |
| `Error` | Protocol or runtime failure | Submit `transactionStatus` and `additionalDetails` |

The README uses a five-minute timeout, and the generated result documentation describes five minutes as the minimum. The older `ChallengeStatusReceiver` overload and its separate completion, cancellation, timeout, protocol-error, and runtime-error callbacks are deprecated.

## Lifecycle and error model

Each `Transaction` is usable once and must be closed whether the flow succeeds or fails. The README then calls `ThreeDS2Service.cleanup` after the flow. The generated service documentation contains contradictory lifecycle text: initialization says cleanup should follow every transaction, while the cleanup method says it is called only once during an app session. The retained README's explicit per-flow example is the clearer integration evidence, but applications should test cleanup against their actual Activity and process lifecycle.

Invalid mandatory values, formats, lengths, or limits raise `InvalidInputException`; internal failures use `SDKRuntimeException`. The older already-initialized exception is deprecated, while use before initialization has a dedicated `SDKNotInitializedException`.

## Security controls and device data

Initialization exposes low-, medium-, and high-severity security warnings. `AdyenConfigParameters.Builder` can validate an app-signing SHA-256 fingerprint, add trusted app-store package names, check configured malicious applications, and block selected device parameters from collection. The API warns against storing the app signature in the app and recommends retrieving it securely from a server.

The retained public API proves the configuration and warning contracts, but it does not expose the internal device-data inventory or cryptographic implementation. Because the release's claimed Data Safety Guide is missing, privacy and disclosure decisions require authoritative Adyen documentation or a focused recollection.

## UI customization and deprecations

The SDK supplies a default challenge UI and lets the app customize toolbar, screen, labels, text boxes, selection items, expandable information, and verify, continue, next, cancel, resend, or out-of-band-app buttons. Global helpers can set text, border, tint, and highlighted-background colors. Status-bar color customization is deprecated and has no effect starting with Android 15.

The retained package also exposes test-harness challenge listener interfaces and screenshot scrolling hooks. Their presence documents validation support, not merchant-facing checkout APIs.

## `2.2.27` release finding

Release `2.2.27` claims four changes: a new Data Safety Guide, corrected text-color application for the merchant-whitelisting compound button, `Intent.FLAG_ACTIVITY_NEW_TASK` when launching the out-of-band issuer app, and Bouncy Castle `1.84`.

Only the release note proves those change claims. The absent guide prevents content-level ingestion, and no retained implementation source is available to verify the three code or dependency changes independently.

## Related

- [[changelog-github-adyen-3ds2-android]] - package-qualified release ledger
- [[adyen-3ds2-android-sdk]] - durable integration concept
- [[source-github-adyen-android]] - parent Android checkout SDK and adapter boundary
- [[adyen-android-sdk]] - parent Android SDK concept
- [[adyen]] - company and knowledge-status page

## Raw sources

- Snapshot manifest: `raw/github/adyen/adyen-3ds2-android/snapshots/2026-08-17-de845e6/manifest.json`
- Release manifest: `raw/github/adyen/adyen-3ds2-android/releases/adyen-3ds2-android/2.2.27/2026-08-17/manifest.json`
- Release notes: `raw/github/adyen/adyen-3ds2-android/releases/adyen-3ds2-android/2.2.27/2026-08-17/release-notes.md`
- README: `raw/github/adyen/adyen-3ds2-android/snapshots/2026-08-17-de845e6/files/README.md`
- API entry point: `raw/github/adyen/adyen-3ds2-android/snapshots/2026-08-17-de845e6/files/docs/index.html`
- Transaction APIs: `raw/github/adyen/adyen-3ds2-android/snapshots/2026-08-17-de845e6/files/docs/com/adyen/threeds2/`
- Configuration and challenge parameters: `raw/github/adyen/adyen-3ds2-android/snapshots/2026-08-17-de845e6/files/docs/com/adyen/threeds2/parameters/` and `raw/github/adyen/adyen-3ds2-android/snapshots/2026-08-17-de845e6/files/docs/com/adyen/threeds2/util/`
- UI customization: `raw/github/adyen/adyen-3ds2-android/snapshots/2026-08-17-de845e6/files/docs/com/adyen/threeds2/customization/`
- Deprecated API list: `raw/github/adyen/adyen-3ds2-android/snapshots/2026-08-17-de845e6/files/docs/deprecated.html`
