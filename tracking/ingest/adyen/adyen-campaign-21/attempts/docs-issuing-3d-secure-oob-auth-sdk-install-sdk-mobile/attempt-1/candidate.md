---
title: "Adyen Issuing: Install mobile Authentication SDK for OOB"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/3d-secure/oob-auth-sdk/install-sdk-mobile"
raw_files:
  - "adyen/docs/issuing/3d-secure/oob-auth-sdk/install-sdk-mobile/2026-09-15.md"
tags: [adyen, issuing, authentication, 3d-secure, mobile-sdk]
---

## Overview

This Adyen guide (last modified 2023-07-12; captured 2026-09-15) describes installing the **client-side Authentication SDK** for Issuing out-of-band (OOB) cardholder authentication. It uses device binding as the possession factor and knowledge or inherence according to device access configuration. The SDK is described for checking SCA device eligibility, registering a cardholder's device and authenticating online card transactions with 3D Secure; its integration can also serve Adyen Business Accounts SCA. This is issuer/cardholder OOB tooling, distinct from merchant checkout 3DS2 SDK integration.

## Key takeaways

- Although the page sits under an Issuing URL, its requirements table says the feature is supported with an **Adyen for Platforms** integration (raw lines 29-35). The page does not establish that an Issuing-only or Business Accounts-only setup qualifies; verify account/product availability with Adyen.
- Native Android uses Kotlin or Java. The app must target Android API level **21+**, but the authentication feature works on devices running **API 26+** and needs **Google Play Services** on the cardholder's device (raw lines 37-50). Meeting the app target alone does not make a device authentication-eligible.
- Native iOS uses Swift; the captured prerequisites are **iOS 14+**, **Xcode 13.2+**, and **Swift 5.5+**. For the LIVE environment, Adyen requires a **TestFlight or App Store release build**, explicitly excluding Xcode debug builds (raw lines 52-57).
- The snapshot shows Gradle dependency `com.adyen.authentication:android-authentication:0.2.1` for Android and iOS package routes through Swift Package Manager (`adyen-authentication-ios`, minimum version `1.0.0`), Carthage, or CocoaPods (`AdyenAuthentication`) (raw lines 59-96). These are captured example/version instructions, not proof of the currently supported SDK release.
- Device registration and management are separate next steps linked at raw lines 98-110; installation alone does not bind a device, complete SCA, authenticate a particular transaction, or authorize/capture a card payment.

## Related

- [[adyen]] — provider.
- [[adyen-issuing]] — Issuing concept and source route.
- [[adyen-business-accounts]] — separate Business Accounts product context.

## Raw Sources

- [[raw/adyen/docs/issuing/3d-secure/oob-auth-sdk/install-sdk-mobile/2026-09-15|2026-09-15 capture of mobile Authentication SDK installation guide]]
