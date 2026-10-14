---
title: "Adyen iOS Mobile SDK card-reader solution"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/mobile-ios/build/card-reader"
raw_files:
  - "adyen/docs/point-of-sale/mobile-ios/build/card-reader/2026-09-15.md"
tags: [adyen, point-of-sale, mobile-pos, ios, card-reader, terminal-api]
---

## Overview

This dated Adyen guide describes building an iOS POS app with the POS Mobile SDK and an NYC1 card reader as the payment interface. The POS app initiates Terminal API requests; the reader accepts tap, insert, swipe or wallet presentation and connects by Bluetooth or by USB through an optional dock. This in-person SDK and reader route is distinct from online Adyen iOS Checkout SDKs, an app installed on an Adyen Android payment terminal, and the separate Tap to Pay on iPhone mobile path. See [[adyen]], [[adyen-mobile-pos]] and [[adyen-mobile-card-readers]].

## Key takeaways

- Prerequisites include a Terminal API-integrated POS app, supported iOS device and region/payment functionality, a test NYC1 reader assigned to the store, a basic-auth credential with **Allow SDK download for POS developers**, and a separate API-key/client-key credential with **Checkout webservice** for the backend session. PIN transactions require an NYC1 model. The guide says US NYC1 PIN support can be disabled through Support from iOS Mobile SDK 3.12.0. Check current support and eligibility separately.
- The backend exchanges the SDK's setup token at `/auth/certificate` and returns `sdkData` to the app; use the installation ID as Terminal API `MessageHeader.POIID`. A non-payment facilitator supplies `store` unless merchant accounts are used as stores. A registered payment facilitator instead supplies `subMerchantData` in the session request and must not place it in Terminal API requests. The guide recommends migration from deprecated `/checkout/possdk/v68/sessions` endpoints.
- SDK test and live packages need separate Xcode app targets. Keep the download password out of publicly accessible code; the `.netrc` setup calls for mode `0600`. Going live requires a live SDK/basic-auth credential, a distinct live API key for sessions, and the applicable regional live `/auth/certificate` endpoint. This snapshot does not establish current endpoint availability.
- The app must configure Bluetooth and camera permissions for pairing; a dock additionally needs the external-accessory protocol and, for App Store submission, Adyen's MFi PPID in Review Notes. To prevent the POS device's own Apple Pay passes from responding to a nearby reader, the guide requires an Apple entitlement and foreground pass-presentation suppression.
- Operators need reader/dock management and firmware updates through the SDK's built-in screens or a custom UI. Check for updates regularly and prompt users; after a `requiredDate`, transactions are refused until required firmware is installed. Reader Bluetooth-layer updates require Bluetooth and cannot complete over USB. Optional periodic reconnects can significantly reduce reader battery life.
- For a payment, create a Terminal API `Payment.Request`, select `.cardReader`, use the SwiftUI or UIKit presentation mode, and inspect the Terminal API response. A referenced refund uses `Reversal.Request`/`performReversal`; an unreferenced refund uses a payment request with `PaymentData.PaymentType=Refund`. Refund requests are usually asynchronous acknowledgments: use `CANCEL_OR_REFUND` or `REFUND_WITH_DATA` webhook outcomes, with the documented scheme/region exception for synchronous unreferenced refunds. The guide gives no general cancellation flow.
- Diagnosis can surface stored offline payments, security issues and SDK expiry; mandatory SDK updates can block transactions. Clear the session with `PaymentService.resetSession()` after a store or merchant reassignment so subsequent transactions do not remain associated with the prior store, and re-establish a session. The support table lists store-and-forward, partial/pre-authorization and refunds, but marks surcharge and tax-free shopping unsupported for this reader solution.
- The simulated reader tests device-management UI only in test builds. It cannot run transactions and should be disabled before test payments; actual test transactions use the test SDK and Adyen POS test cards. None of the guide's examples proves a completed payment.

## Detail locators

- `## Requirements`, `## 1. Add the SDK to your project`, `### Compatibility with Objective-C`: hardware, account permissions, Swift Package products and separate environments.
- `## 2. Establish a session`, `#### Implement the request`, `#### Endpoints to use`: backend setup token exchange, facilitator/store fields, installation ID and regional endpoint examples.
- `## 3. Enable transactions` through `## 7. Manage the Device Manager UI`: SDK delegate, warm-up, iOS permissions and Apple Pay suppression, reader/dock pairing and required firmware behavior.
- `## 8. Handle a payment`, `## 9. Handle a refund`, `## 10. Diagnose the device`, `## 11. (Optional) Clear the session token`: Terminal API calls, asynchronous refund outcomes, offline/security/expiry diagnosis and reassignment.
- `## Other supported features`, `## Test your solution`, `## Go live`: feature table, simulator boundary, test cards, live credentials and regional endpoints.

## Source caveat

The `## How it works` summary unexpectedly describes a Tap to Pay on iPhone component and tapping on the iPhone, while the page's title, opening, requirements and detailed payment step explicitly select a `.cardReader` payment interface. Treat that summary as an apparent editorial conflict; do not infer a Tap to Pay flow for this reader integration from it.

## Related

- [[adyen-mobile-pos]] — planned primary route for the SDK mobile POS paths, pending coordinator approval.
- [[adyen-mobile-card-readers]] — NYC1 hardware and dock context.
- [[adyen-terminal-api]] — in-person request and response structure.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/mobile-ios/build/card-reader/2026-09-15|Adyen card reader solution for iOS, captured 2026-09-15]]
