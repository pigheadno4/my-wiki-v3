---
title: "Adyen Classic API Android 3D Secure 2 SDK integration"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/android-sdk-integration"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/android-sdk-integration/2026-09-15.md"
tags: [adyen, online-payments, classic-api, android, 3ds2, authentication]
---

## Overview

This Adyen webpage snapshot describes native 3D Secure 2 authentication in an Android app using the Classic Payment API `/authorise` integration and the Adyen 3DS2 Android SDK. It is a legacy integration guide: Adyen says it no longer accepts new Classic API integrations and recommends the newer Android native 3DS2 route with migration to the Checkout API. Authentication and payment authorization remain distinct outcomes; this guide's full flow includes an authorization request and later authorization result. See [[adyen-3d-secure]] and the separately versioned runtime evidence in [[adyen-3ds2-android-sdk]].

## Key takeaways

- The Android SDK gathers encrypted device fingerprint data and presents issuer challenges; the merchant server sends payment, fingerprint and completed challenge data to Adyen. The initial Classic `/authorise` call uses card data, `threeDS2RequestData.deviceChannel=app`, `sdkVersion`, and `browserInfo` for possible 3DS1 fallback. Set `sdkVersion` to the version of the SDK actually in use; Adyen recommends `ThreeDS2Service.INSTANCE.getSDKVersion()` to determine it and warns not to hard-code it. Separately, the page says SDK 2.2.9 or later is needed to trigger native 3DS2.
- The `resultCode` controls the branch: `IdentifyShopper` starts fingerprinting; `ChallengeShopper` requires issuer interaction; `RedirectShopper` indicates possible 3DS1 routing; `Authorised` can occur on an exemption or after a frictionless result. A challenge or authentication step alone does not establish payment authorization.
- For `IdentifyShopper`, build an SDK transaction from directory-server data and, with SDK 2.2.0+, pass the response `messageVersion` into `createTransaction`. Send the SDK fingerprint fields from the server to Classic `/authorise3ds2`, retaining the returned 3DS2 token for the later request.
- For `ChallengeShopper`, present the SDK challenge and send the completed SDK transaction status and 3DS2 token from the server to `/authorise3ds2`. The page treats `ThreeDSRequestorAppURL` as optional; for SDK 2.2.12+ it says the value should be an Android App Link and the app must handle it for out-of-band return. This snapshot's `ChallengeStatusReceiver` example should be read with its historic SDK scope.
- Every SDK transaction is single-use. Close it and clean up `ThreeDS2Service.INSTANCE` after success or failure; the page warns that skipping cleanup can cause subsequent transactions to fail.

## Detail locators

- Legacy scope, migration and full-flow distinction: raw lines 19–33.
- Initial request fields, version requirement and result branches: raw lines 41–46, 61–100 and 515–549.
- Fingerprint transaction, SDK version and server handoff: raw lines 551–610 and 952–966.
- Challenge callback, server submission and Android App Link: raw lines 991–1080 and 1315–1344.
- Cleanup, customization and test scenarios: raw lines 1346–1497.

## Related

- [[adyen]] — provider.
- [[adyen-3d-secure]] — merchant authentication routes.
- [[adyen-3ds2-android-sdk]] — separately versioned native SDK evidence; do not transfer this Classic page's API and callback examples to that baseline.

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/android-sdk-integration/2026-09-15|Adyen Classic API Android 3DS2 SDK integration (2026-09-15 snapshot)]]
