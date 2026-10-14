---
title: "Adyen Tap to Pay on iPhone with iOS Mobile SDK"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/mobile-ios/build/tap-to-pay"
raw_files:
  - "adyen/docs/point-of-sale/mobile-ios/build/tap-to-pay/2026-09-15.md"
tags: [adyen, point-of-sale, mobile-pos, ios, tap-to-pay, terminal-api]
---

## Overview

Adyen's Tap to Pay on iPhone build guide, captured 2026-09-15, explains how a merchant's iOS POS app uses the **iOS Mobile SDK** and Terminal API to accept contactless in-person payments on an iPhone as the payment interface. This is the phone payment path within [[adyen-mobile-pos]], separate from the paired card-reader path, apps installed on Adyen Android payment terminals, and the [[adyen-ios-sdk]] for native online checkout. The dated guide describes integration steps; it does not establish current Apple entitlement, device or regional eligibility, App Store approval, or a successful payment.

## Key takeaways

- The POS app must integrate with Terminal API. The guide points to separate iOS system requirements and supported countries/regions, payment methods and functions; it does not enumerate those eligibility sets here. Account setup by Adyen Support, an iPhone, Apple Tap to Pay entitlement, and the relevant test/live setup are gates. Apple TEST and LIVE entitlements are separate; the dated guide says LIVE approval can take several weeks. It lists an Organization-level Apple Developer account and Account Holder role for entitlement requests.
- Downloading the SDK uses a basic-auth credential with **Allow SDK download for POS developers**; session establishment uses a distinct API-key credential with **Checkout webservice** role and a client key. The guide says not to expose the SDK-download password publicly, to store it in `.netrc` with permission `0600`, and that the session client key is a setup prerequisite but is not used later. The app must use separate TEST and LIVE targets and environment-specific SDK packages; the live SDK requires a new live download credential.
- The app's `PaymentServiceDelegate.register(with:)` callback supplies a `setupToken`; the merchant backend calls `/auth/certificate` and returns `sdkData` to the app. The backend uses the applicable test or regional live endpoint and live API key when going live. The request carries `merchantAccount` and `setupToken`; a non-facilitator supplies `store` except when merchant accounts act as stores, while a registered payment facilitator supplies `subMerchantData` instead and must not put that data in Terminal API requests. The older `/checkout/possdk/v68/sessions` route is described as deprecated but still usable in this snapshot.
- Before the first payment, the merchant account or store must accept Apple's Tap to Pay terms. The guide says the Customer Area acceptance route is LIVE-only, while the SDK's link-account prompt can be used on the phone. `warmUp()` is a best-practice preparation step, not a payment. For the payment, use the SDK installation ID as Terminal API `POIID`, create `Payment.Request`, select `.tapToPay` through `getPaymentInterface`, choose SwiftUI or UIKit presentation, invoke `performTransaction`, and inspect the Terminal API response. The iPhone's **Done** screen after card reading is not authorization; the **Approved** screen indicates authorization.
- Referenced refunds use a Terminal API reversal through `performReversal`; unreferenced refunds use a payment request with `PaymentData.PaymentType: Refund`. Refund requests are usually acknowledged synchronously but their outcomes arrive by webhook (`CANCEL_OR_REFUND` or `REFUND_WITH_DATA`); the guide notes a card-scheme/region-dependent synchronous exception for some unreferenced refunds. Diagnosis can inspect stored offline payments, security threats and SDK expiry; mandatory updates can block transactions. Clear the session with `resetSession()` when reassigning a device between merchants/stores or forcing configuration refresh, or transactions can remain attributed to the prior store.

## Detail locators

- Raw `## Requirements` and `## 1. Get an entitlement from Apple` (lines 21–88): account, hardware, region and entitlement prerequisites. Linked requirement/support pages require their own reading for current model, OS, country and payment-method coverage.
- Raw `## 2. Add the SDK to your project` and `### Compatibility with Objective-C` (lines 90–155): credential and package setup, separate environment targets, Objective-C `ADY` symbols and package variants. The guide's tutorial link references version `2.0.1`; it is a linked tutorial version, not a claim that this snapshot's SDK is version 2.0.1.
- Raw `## 3. Establish a session` through `#### Endpoints to use` (lines 157–310): backend request, facilitator versus non-facilitator fields, response fields and test/regional live endpoints. The exact endpoint examples use `/softposconfig/v3/auth/certificate`; `## Go live` repeats regional URL templates with `v{version}`.
- Raw `## 4. Enable transactions` through `## 7. Handle a payment` (lines 311–534): delegate lifetime, Apple terms, optional warm-up/progress observer (SDK 3.18+; callback off main thread), payment-interface selection and presentation. The education-screen example is scoped to SDK 3.9.0+ and iOS 18+, with an `@available(iOS 18.4, *)` sample annotation; do not generalize it to every iOS version.
- Raw `## 8. Handle a refund` through `## 10. (Optional) Clear the session token` (lines 536–661): refund acknowledgement/outcome distinction, diagnosis, SDK expiry and session reset.
- Raw `## Other supported features`, `## Follow UI guidelines`, `## Test your solution` and `## Go live` (lines 663–775): dated feature table (including surcharge marked AU/NZ only), UI/approval distinction, test SDK plus Sandbox Apple Account and Adyen test-card steps, and live setup. The test flow is an instruction, not evidence that a transaction was executed.

## Related

- [[adyen-mobile-pos]] — merchant-device Mobile POS concept and sibling iOS interface route.
- [[adyen-terminal-api]] — in-person request/response boundary.
- [[adyen-mobile-card-readers]] — separate paired-reader hardware path.
- [[adyen-ios-sdk]] — separate online-checkout native SDK.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/mobile-ios/build/tap-to-pay/2026-09-15|Tap to Pay on iPhone build guide, fetched 2026-09-15]]
