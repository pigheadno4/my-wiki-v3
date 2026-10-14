---
title: "Adyen Tap to Pay on Android Mobile SDK build"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/mobile-android/build/tap-to-pay"
raw_files:
  - "adyen/docs/point-of-sale/mobile-android/build/tap-to-pay/2026-09-15.md"
tags: [adyen, point-of-sale, mobile-pos, android, tap-to-pay, mobile-sdk]
---

## Overview

Adyen's Tap to Pay on Android build guide describes a Terminal API-integrated merchant POS app using the Mobile SDK and an Android commercial phone or other COTS device's integrated NFC reader to accept contactless in-person payments. It is the direct device tap path, distinct from an attached mobile card reader, an app installed on an Adyen Android payment terminal, and the separate Android online-checkout SDK. This 2026-09-15 documentation snapshot gives integration steps; it does not prove current country, model, merchant eligibility, app approval, or successful test/live payments. [[adyen]] [[adyen-mobile-pos]]

## Key takeaways

- The stated prerequisites are a POS app integrated with Terminal API, a COTS Android device with integrated NFC that is **not** a payment terminal, Adyen test-account Mobile enablement through Support, and supported-country/payment-method/functionality checks. The app needs `minSdkVersion` 26+, while the SDK runs only on Android 12+ devices; bypassing the minimum with `tools:overrideLibrary` can cause failure or unexpected behavior. The linked system-requirements and support pages are separate eligibility evidence. See `## Requirements` and `## 1. Add the SDK to your project`.
- SDK download uses a dedicated API key with only **Allow SDK download for POS developers**. Communication-session creation uses a different credential with API key, client key, and **Checkout webservice** role. Debug artifacts access test only; release artifacts access live only. The snapshot's repository, dependency and version examples are in `## 1. Add the SDK to your project` and `### Get the live SDK`; check release notes for the SDK version rather than treating `LATEST_SDK_VERSION` as a release.
- The merchant backend sends `/auth/certificate` with `merchantAccount` and the SDK's `setupToken`, returns `sdkData` to the POS app, and may retain `installationId` for backend-created Terminal API requests' `POIID`. For a non-facilitator, `store` is required unless merchant accounts act as stores; a registered payment facilitator instead supplies `subMerchantData` in session creation and must not put it in Terminal API requests. The guide calls the old `/checkout/possdk/v68/sessions` endpoints deprecated. See `## 2. Establish a session`, especially `#### Implement the request` and `#### Endpoints to use`.
- The app implements `AuthenticationProvider` and `MerchantAuthenticationService` so fresh `sdkData` can be supplied when a session is missing or expired. The SDK initializes automatically; manual initialization and state checks have a 2.6.0 version split, including a foreground/resumed Activity condition for 2.6.0+. Warm-up checks session, configuration changes and security as needed. See `## 3. Enable transactions` and `## 4. Use the warm-up function`.
- For payment, the POS app or backend forms a Terminal API request using the SDK installation ID as `MessageHeader.POIID`; the app selects `InPersonPayments.getPaymentInterface(TapToPay)`, registers for `PaymentResult`, and invokes `performTransaction()`. The shopper presents a contactless card or wallet to the mobile device's NFC reader. If no method is presented in 30 seconds, the request times out and another payment request is needed. Optional transaction and kiosk UI parameters, including the 2.16.0+ fractional NFC-position option, are in `## 5. Decide on transaction UI options` and `## 6. Handle a payment`.
- Referenced refunds use a Terminal API reversal; unreferenced refunds use a payment request with `paymentType=Refund`. Refund responses usually acknowledge receipt, with final outcomes sent through Standard webhooks; some unreferenced refunds can complete synchronously depending on scheme and country/region. If a payment response is missing, the guide recommends `getTransactionStatus()`; its quick `success=false` can mean either a failed original transaction or no match. See `## 7. Handle a refund` and `## 8. Check the transaction status`.
- The guide recommends diagnosis to detect transaction-blocking security threats and SDK expiry, with `HostDiagnosisFlag=true`; it says mandatory missed SDK updates block transactions. Clearing a session removes device session information and fetches new configuration on the next transaction or warm-up. After a merchant-account or store switch, failing to clear it can leave transactions attributed to the former store. See `## 9. Diagnose the device` and `## 10. (Optional) Clear the session token`.
- The dated feature table marks store-and-forward offline payments unsupported and surcharge AU/NZ only. Test instructions specify the test SDK and Adyen POS test cards. Going live requires live account access, separate live download and session keys, release SDK artifacts, a regional live session endpoint, and Adyen app registration; the page does not attest that these steps were completed. See `## Other supported features`, `## Test your solution`, and `## Go live`.

## Detail locators

- `## 1. Add the SDK to your project`: private repository and Gradle artifact examples, `minSdkVersion`, Android OS floor, key-role setup, debug/release distinction.
- `## 2. Establish a session`: backend request/response, non-facilitator versus payment-facilitator fields, `subMerchantData` field table, test and regional live v3 URLs, deprecated prior endpoint.
- `## 3. Enable transactions`–`## 6. Handle a payment`: authentication service, initialization/version split, warm-up, UI customization, Terminal API message and TapToPay interface flow.
- `## 7. Handle a refund`–`## 10. (Optional) Clear the session token`: refund outcome boundary, status recovery, security/expiry diagnosis, and session reassignment.
- `## Other supported features`–`## Go live`: dated feature matrix, test cards, release artifacts, regional live endpoints and app registration.

## Related

- [[adyen-mobile-pos]] — Mobile POS solution routes and boundary.
- [[adyen-terminal-api]] — in-person request and response message model.
- [[adyen-mobile-card-readers]] — separate attached-reader path.
- [[adyen-android-terminals]] — apps running on Adyen payment terminals.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/mobile-android/build/tap-to-pay/2026-09-15|Adyen Tap to Pay on Android build guide, fetched 2026-09-15]]
