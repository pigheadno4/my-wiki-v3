---
title: "Adyen Issuing: Register a mobile SCA device"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/3d-secure/oob-auth-sdk/register-devices"
raw_files:
  - "adyen/docs/issuing/3d-secure/oob-auth-sdk/register-devices/2026-09-15.md"
tags: [adyen, issuing, 3d-secure, sca, authentication-sdk, devices]
---

## Overview

This 2023-modified, 2026-09-15-captured Issuing-path guide registers an iOS or Android cardholder device for out-of-band Strong Customer Authentication (SCA) with Adyen's Authentication SDK. Registration binds a device to an Adyen-issued card identified by `paymentInstrumentId`; it is separate from authenticating a later card transaction and from payment authorisation. See [[adyen-issuing]] and [[adyen]].

## Key takeaways

- Before registration, the device OS must support SCA, the Authentication SDK must be installed, and the server API credential needs **Bank SCA Webservice Role**. Checking SCA eligibility additionally requires configuration by Adyen through its Support Team. The companion [[source-adyen-docs-issuing-3d-secure-oob-auth-sdk-install-sdk-mobile|installation guide]] labels its supported integration type **Adyen for Platforms** despite this page's Issuing path; these snapshots alone do not establish eligibility for an Issuing-only setup.
- The client checks device availability (`checkAvailability()` on Android; `checkSupport()` on iOS) and sends the resulting `sdkOutput` to the server. The server initiates registration with Balance Platform POST `/registeredDevices`, supplying the card's `paymentInstrumentId` and `strongCustomerAuthentication.sdkOutput`. The response provides `sdkInput` for the SDK and a registered-device `id` (prefix `BSDR` or `RD`) for finalization. The example endpoint is `bcl/v2` in the test environment.
- The client app authenticates the cardholder with two factors, passes `sdkInput` into SDK registration, and returns the successful SDK's Base64-encoded `sdkOutput` to the server. Android examples expose cancellation, unexpected error and authentication-error branches; the iOS example notes DeviceCheck, device biometric/passcode access and an `NSFaceIDUsageDescription` setting for Face ID.
- The server finalizes with PATCH `/registeredDevices/{id}`, the same card `paymentInstrumentId`, and the SDK registration `sdkOutput`. Verify `success: true` in the final response. Only then does the guide describe the registered device ID as connected to the payment instrument and listed by GET `/registeredDevices`; an initiation response example showing `success: true` does not replace finalization.
- Registration is one-off. Only **one device per payment instrument** can be registered; registering a new one for that card deregisters the previous device. A registered device can later be associated with multiple payment instruments through a separate association API, while the guide says the device cannot be registered more than once. Neither registration nor later SCA authentication establishes a card payment outcome.

## Detail locators

- Pinned raw lines 17–35: purpose, four-step sequence, OS/SDK/role prerequisites; lines 37–39: Adyen-side eligibility configuration.
- Pinned raw lines 41–103: Android/iOS availability checks and client-to-server `sdkOutput`; lines 105–120: replacement limit, server POST and required request fields.
- Pinned raw lines 125–346: test `bcl/v2` and language-specific request examples with pinned SDK/library versions; lines 348–363: initiation response `sdkInput`, device ID and illustrative `success`.
- Pinned raw lines 366–417: cardholder 2FA, SDK registration, Android result branches and iOS device behavior; lines 419–445: final PATCH request.
- Pinned raw lines 448–656: versioned finalization examples; lines 658–662: check final response, resulting association and one-time registration boundary. Companion installation raw lines 29–35 contain the integration-type qualification.

## Related

- [[source-adyen-docs-issuing-3d-secure-oob-auth-sdk]] — OOB Authentication SDK overview.
- [[source-adyen-docs-issuing-3d-secure-oob-auth-sdk-install-sdk-mobile]] — installation and Adyen for Platforms integration-type qualification.
- [[adyen-issuing]] — Issuing resource and payment boundary.

## Raw Sources

- [[raw/adyen/docs/issuing/3d-secure/oob-auth-sdk/register-devices/2026-09-15|Adyen mobile SCA device-registration guide, captured 2026-09-15]]
