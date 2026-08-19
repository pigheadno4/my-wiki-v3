---
title: "Adyen 3DS2 Android SDK"
type: concept
category: technology
tags: [adyen, android, 3d-secure, 3ds2, authentication, sdk, challenge-flow]
---

## Adyen 3DS2 Android SDK

Adyen's standalone Android 3DS2 SDK supplies the native EMV 3-D Secure transaction and challenge runtime used by Adyen Android's 3DS2 adapter. The retained baseline is package-qualified release `com.adyen.threeds:adyen-3ds2@2.2.27` at exact SHA `de845e67488b6aecb1ff57ea7908b662f5ee2d40`.

## Integration flow

The merchant app builds `ConfigParameters` from directory-server values returned by Adyen, initializes `ThreeDS2Service`, and creates a single-use `Transaction`. Its `AuthenticationRequestParameters` contain encrypted device data and SDK identifiers that the app submits to `/authorise3ds2` through the merchant server.

When Adyen requires a challenge, the app builds `ChallengeParameters` from the returned 3DS Server transaction ID, ACS transaction ID, ACS reference number, signed ACS content, and an app-return URL. An Android App Link is strongly recommended for the return URL. `transaction.doChallenge` reports one consolidated `ChallengeResult`: completed, cancelled, timeout, or error. Every result must be sent back to `/authorise3ds2`; non-completed outcomes also carry `additionalDetails`.

## Lifecycle and failure handling

Each `Transaction` is single-use and must be closed after either success or failure. The README also requires cleanup of `ThreeDS2Service` when the flow finishes. Initialization and transaction-creation failures expose a `transactionStatus` and `additionalDetails` for the follow-up server call.

The generated `ThreeDS2Service` API is internally inconsistent: its initialization text says to call `cleanup` after every transaction, while the method detail says cleanup is called only once during an app session. Until Adyen clarifies this, integrations should follow the retained README's per-flow cleanup example and verify behavior against the merchant application's lifecycle tests.

## Security and UI surface

Initialization performs device-information collection and security checks. Optional builder settings cover app-signature validation, trusted app stores, malicious-app detection, and a device-parameter block list; warnings are available with low, medium, or high severity. The app signature should be obtained securely from a server rather than embedded in the app.

Challenge UI can be customized by theme or with `UiCustomization` for toolbar, screen, labels, text boxes, selection items, expandable information, and challenge buttons. Status-bar color customization is deprecated because it has no effect from Android 15. The older `ChallengeStatusReceiver`, its callback overload, the embedded requestor URL helper, and the already-initialized exception are also deprecated in the retained API.

## Release boundary

Release `2.2.27` documents a Data Safety Guide, compound-button text-color correction, `FLAG_ACTIVITY_NEW_TASK` for out-of-band issuer-app launch, and Bouncy Castle `1.84`. However, the exact tag does not contain the referenced `DATA_SAFETY_GUIDE.md`, and the README compatibility table stops at `2.2.26`. Those omissions prevent this snapshot from proving the guide's contents or an explicit Android-version row for `2.2.27`.

## Related

- [[source-github-adyen-3ds2-android]] - cumulative exact-SHA SDK evidence
- [[changelog-github-adyen-3ds2-android]] - package-qualified release ledger
- [[adyen-android-sdk]] - parent checkout SDK and adapter boundary
- [[source-github-adyen-android]] - independently versioned parent repository evidence
- [[adyen]] - company and knowledge-status page

## Sources

- `raw/github/adyen/adyen-3ds2-android/snapshots/2026-08-17-de845e6/manifest.json` - exact-SHA source capsule
- `raw/github/adyen/adyen-3ds2-android/snapshots/2026-08-17-de845e6/files/README.md` - installation, transaction, challenge, lifecycle, and UI flow
- `raw/github/adyen/adyen-3ds2-android/snapshots/2026-08-17-de845e6/files/docs/com/adyen/threeds2/ThreeDS2Service.html` - initialization, transaction creation, cleanup, and warnings
- `raw/github/adyen/adyen-3ds2-android/snapshots/2026-08-17-de845e6/files/docs/com/adyen/threeds2/Transaction.html` - challenge and transaction lifecycle
- `raw/github/adyen/adyen-3ds2-android/releases/adyen-3ds2-android/2.2.27/2026-08-17/release-notes.md` - exact release claims
