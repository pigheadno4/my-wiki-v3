---
title: "Adyen Classic API native 3DS2 iOS SDK integration"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/ios-sdk-integration"
raw_files:
  - "adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/ios-sdk-integration/2026-09-15.md"
tags: [adyen, classic-api, ios, 3d-secure, 3ds2, authentication, sdk]
---

## Overview

This [[adyen]] guide describes a legacy Classic API `/authorise` integration that uses the Adyen 3DS2 iOS SDK to collect an encrypted device fingerprint and show a native shopper challenge. The merchant server sends the payment request, fingerprint, and challenge result to Adyen; the SDK does not itself authorize the payment. Adyen says it no longer accepts new Classic API integrations and recommends the newer native iOS 3DS2 integration with a Checkout API migration. Use [[adyen-3d-secure]] for the merchant flow and [[adyen-3ds2-ios-sdk]] for separately versioned SDK package evidence.

## Key takeaways

- In this guide's full payment flow, the server submits `/authorise` with card data, `threeDS2RequestData.deviceChannel=app`, `sdkVersion`, and `browserInfo` for possible 3DS1 redirect fallback. The guide recommends deriving `sdkVersion` with `ADY3DS2SDKVersion()` rather than hard-coding it. Its displayed v68 and library requests are examples, not evidence of a tested merchant result.
- An `IdentifyShopper` response supplies directory-server information, a 3DS message version, and a `threeDS2Token`. The app creates `ADYServiceParameters` and an `ADYTransaction`, keeps the transaction until completion, and sends SDK authentication request parameters through the merchant server to `/authorise3ds2` with the token. For SDK 2.2.0 or later, this guide says to create the transaction with the message version returned by `/authorise`.
- After fingerprint submission, `Authorised` represents the guide's frictionless authentication and successful payment authorization path. `ChallengeShopper` requires the app to present an SDK challenge using returned 3DS Server and ACS data; the app then sends the SDK's `transStatus` and token through the server to `/authorise3ds2`. The final example shows `Authorised` only when that payment succeeds. Initial `Authorised` may also occur when 3DS is exempted; `RedirectShopper` indicates possible 3DS1 fallback. These branches are response-dependent, not promised outcomes.
- The challenge section states that `threeDSRequestorAppURL` is supported in 3D Secure version 2.2.0 or later and calls for a universal-link app URL for out-of-band return; it says the field is ignored when an earlier 3DS version was selected. Keep that version condition attached to the guide's requirement.
- The setup text says SDK 2.3.0 or later is needed to trigger native 3DS2, but the Swift Package Manager tab says to select 2.2.1 or later. The page does not reconcile those minima. This older Classic guide does not establish support for every version admitted by that package-manager instruction or supersede the independently versioned SDK record.
- Authentication-only is a separate linked Classic route for authentication followed by later payment authorization. Do not treat a device fingerprint, challenge status, or authentication-only result as financial authorization; evaluate the actual payment `resultCode` in the chosen flow.

## Detail locators

- **Classic scope, deprecation, flow branches, and fallback:** raw lines 15–47.
- **Account/API prerequisites, SDK installation, and conflicting minima:** raw lines 49–98.
- **Initial `/authorise` parameters, SDK version, and illustrative requests:** raw lines 100–525.
- **`IdentifyShopper` response, transaction construction, and fingerprint `/authorise3ds2` handoff:** raw lines 527–848.
- **Post-fingerprint `Authorised` or `ChallengeShopper` response, universal-link condition, challenge result, and final `/authorise3ds2`:** raw lines 850–1193.
- **SDK UI customization, version helper, and test scenarios:** raw lines 1195–1354.

## Related

- [[adyen]]
- [[adyen-3d-secure]]
- [[adyen-3ds2-ios-sdk]]
- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration]]
- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-3d-secure-authentication-native-3ds2-api-reference-3d-secure-2]]
- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-3d-secure-authentication-native-3ds2-authentication-only-integration]]

## Raw Sources

- [[raw/adyen/docs/online-payments/classic-integrations/classic-api-integration/3d-secure-authentication/native-3ds2/ios-sdk-integration/2026-09-15|Adyen Classic API native 3DS2 iOS SDK integration — collected 2026-09-15]]
