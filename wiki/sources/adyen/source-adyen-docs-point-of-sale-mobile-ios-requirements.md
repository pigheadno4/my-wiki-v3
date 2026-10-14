---
title: "Adyen iOS Mobile system requirements"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/mobile-ios/requirements"
raw_files:
  - "adyen/docs/point-of-sale/mobile-ios/requirements/2026-09-15.md"
tags: [adyen, point-of-sale, mobile-pos, ios, requirements, nyc1]
---

## Overview

Adyen's iOS Mobile requirements page, captured 2026-09-15, gives device, passcode, reader/dock, iOS, SDK and development gates for a merchant iOS POS app with the iOS Mobile SDK. Tap to Pay on iPhone and Card reader on iOS use that same Mobile SDK under the [[adyen-mobile-pos]] route. The page's version and ordering statements are historical snapshot evidence; it does not establish current country, payment-method, account, Apple-entitlement or merchant eligibility, certification, or live-payment success.

## Key takeaways

- **Device scope differs.** Tap to Pay requires an iPhone; Card reader on iOS permits an iPhone or iPad. The mobile device must not itself be a payment terminal or have an integrated card reader, and it needs a screen-lock passcode. The stated iPhone model floor is iPhone XS. This is a merchant mobile-device path, distinct from apps on [[adyen-android-terminals]] and from the native online-checkout [[adyen-ios-sdk]].
- **Passcode removal has a consequential effect.** From iOS Mobile SDK 3.18.0, the SDK requires a device passcode before any `PaymentService` function can be called. Removing the passcode stops transactions on that device and makes store-and-forward offline payments made while it had a passcode unrecoverable. The page suggests Never display lock or a simple staff passcode if the lock behavior is inconvenient; these are workarounds stated in the page, not a waiver of the passcode requirement.
- **Reader models have different PIN scope.** The NYC1 secure card reader for PIN needs iOS Mobile SDK 3.8.0 or later. NYC1-SCR is for transactions without PIN. The page dates US NYC1 ordering from 2025-12-01 and NYC1-SCR order discontinuation after 2026-02-01; these dates are not proof of present inventory. From SDK 3.12.0, Adyen Support can disable NYC1 PIN support at company, merchant or store level. Other readers and USB docks are not supported by this page.
- **Dock conditions are additional.** The countertop reader setup uses Adyen's NYC1 dock with Adyen's power adapter; the page lists Mobile SDK 3.9.0 and reader firmware 3.X.00.76 as minimums for that setup.
- **Software requirements are snapshot-qualified.** The page lists iOS 18.4 as its minimum: iOS 13.0–18.3 can run the POS app but not SDK functionality, while iOS 12.x or earlier cannot run the app with the SDK integrated. For Tap to Pay on iPhone it separately gives one-year iOS-version support/deprecation dates for MPoC and recommends iOS 18.4 or later. The current SDK and reader software floors depend on release notes; the page also calls for Xcode 16+ for development and Terminal API integration in the POS app. Mandatory update messages are sent by Adyen.

## Detail locators

- Raw introduction and `### Mobile devices` (lines 19–55): shared SDK, phone/tablet path split, device exclusions, passcode gate, SDK 3.18.0 enforcement, offline store-and-forward loss and suggested display-lock workarounds.
- Raw `### Card readers` and `### Dock` (lines 57–79): NYC1 versus NYC1-SCR PIN scope, dated US order notices, SDK floors, Support-managed PIN disablement and dock/firmware conditions.
- Raw `## Software requirements` (lines 81–115): iOS version behavior table, Tap to Pay MPoC deprecation table, release-note routes for current SDK/reader software, Xcode and Terminal API. The deprecation table is a dated list, not a current support determination.
- Raw `## See also` (lines 117–120): separate supported-country/region, payment-method and functionality source; read that source before asserting such availability.

## Related

- [[adyen-mobile-pos]] — shared merchant-device in-person payment hub.
- [[source-adyen-docs-point-of-sale-mobile-ios]] — iOS solution overview.
- [[adyen-mobile-card-readers]] — NYC1 device family and hardware route.
- [[adyen-terminal-api]] — required POS API integration context.
- [[adyen-ios-sdk]] — separately versioned online-checkout SDK.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/mobile-ios/requirements/2026-09-15|iOS system requirements, fetched 2026-09-15]]
