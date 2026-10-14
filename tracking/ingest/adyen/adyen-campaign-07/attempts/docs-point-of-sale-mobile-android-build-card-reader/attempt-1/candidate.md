---
title: "Adyen Card reader solution for Android"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/mobile-android/build/card-reader"
raw_files:
  - "adyen/docs/point-of-sale/mobile-android/build/card-reader/2026-09-15.md"
tags: [adyen, point-of-sale, mobile-pos, android, card-readers, terminal-api]
---

## Overview

Adyen's Card reader on Android build guide, captured 2026-09-15, describes a merchant Android POS app using the Adyen Mobile SDK and Terminal API to initiate in-person payments on an NYC1 card reader. The Android device starts and displays the flow; the shopper presents a card or wallet at the reader, connected by Bluetooth or USB. This is the [[adyen-mobile-pos]] reader path, with [[adyen-mobile-card-readers]] covering the hardware; it is separate from apps installed on [[adyen-android-terminals]] and from the [[adyen-android-sdk]] for online checkout. [[adyen]]

## Key takeaways

- The app must already integrate with Terminal API. The documented hardware is an Android commercial off-the-shelf device that is not a payment terminal plus an Adyen NYC1 reader; PIN transactions require the NYC1 model identified by the guide. Test setup calls for Support to enable Mobile solutions on the test account, and a test reader assigned to a store. Country, payment-method and feature availability is routed to a separate support page; this dated guide alone does not establish current entitlement.
- The app requires `minSdkVersion` 26 or higher, but the SDK initializes only on Android 12 or later. A credential with only **Allow SDK download for POS developers** downloads the SDK; a different credential with an API key, client key and **Checkout webservice** role establishes a session. Debug artifacts access test and release artifacts access live. The backend calls SoftPOS Configuration `/auth/certificate` with the SDK setup token, then supplies `sdkData` to the app; `store` and `subMerchantData` have different merchant versus registered payment-facilitator conditions. For a facilitator, the guide says not to put sub-merchant data in Terminal API requests.
- The app or backend creates a Terminal API payment request with the SDK installation ID as `MessageHeader.POIID`; the app selects `CardReader` as the payment interface and passes the request to the SDK. The SDK returns a Terminal API response to the app. If the shopper does not present a payment method within 30 seconds, the request times out and another request is needed. A missing payment response calls for transaction-status checking, not an assumed success.
- Reader and dock firmware updates do not happen automatically. The app must check regularly, provide update flows, and prompt users; a returned required date can mark when transactions will be refused without an update. Some reader updates require Bluetooth, so USB connection alone cannot complete them. Bluetooth sleep can delay reconnection; frequent reconnect timers can reduce reader battery life.
- Referenced refunds use a reversal request; unreferenced refunds use a payment request with refund payment type. Refund responses usually acknowledge receipt, while Standard webhooks report the outcome (`CANCEL_OR_REFUND` or `REFUND_WITH_DATA`); some unreferenced refunds can return synchronous outcome information depending on scheme and country. Clear the SDK session when switching merchant account or store so a reassigned device does not keep attributing transactions to the previous store. Diagnosis can surface blocking security threats and SDK expiry; mandatory SDK updates can block transactions.

## Detail locators

- Raw `## Requirements` and `## How it works` (lines 23–67): POS app, credentials, NYC1/COTS hardware, test setup and reader payment sequence.
- Raw `## 1. Add the SDK to your project` and `## 2. Establish a session` (lines 68–291): Android/SDK gates, distinct credential roles, build variants, backend certificate request, facilitator/store conditions, response and regional endpoints. The old `/checkout/possdk/v68/sessions` endpoints are described as being deprecated.
- Raw `## 3. Enable transactions` through `## 6. Manage the Device Manager UI` (lines 292–752): authentication callback, SDK initialization by version, warm-up, reader preparation, pairing/USB connection and firmware update flows. Initialization advice changes at SDK 2.6.0; hiding built-in update indicators requires 2.18.0 or later.
- Raw `## 8. Handle a payment` through `## 12. (Optional) Clear the session token` (lines 815–1044): CardReader payment interface, response timeout, refund webhooks, transaction status, diagnosis and session clearing.
- Raw `## Other supported features` through `## Go live` (lines 1057–1140): dated feature table, test-card steps, live account, separate live SDK/session keys, regional live endpoint and app registration. The table marks store-and-forward offline payments, surcharge and tax-free shopping unsupported for this path.

## Related

- [[adyen-mobile-pos]] — merchant-device Mobile POS integration route.
- [[adyen-mobile-card-readers]] — NYC1 reader and dock hardware context.
- [[adyen-terminal-api]] — request and response model used by this SDK flow.
- [[adyen-android-terminals]] — apps installed on Adyen payment terminals.
- [[adyen-android-sdk]] — separate native online-checkout SDK.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/mobile-android/build/card-reader/2026-09-15|Card reader solution for Android, fetched 2026-09-15]]
