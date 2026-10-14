---
title: "Manage your Android Mobile solution | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/mobile-android/manage"
raw_files:
  - "adyen/docs/point-of-sale/mobile-android/manage/2026-09-15.md"
tags: [adyen, point-of-sale, mobile-pos, android, mobile-sdk, lifecycle]
---

## Overview

This Adyen guide covers distribution and ongoing software maintenance for Android Mobile in-person payment solutions. Its instructions distinguish Android Tap to Pay and Card reader integrations using a merchant-built Mobile SDK app from the Android Payments app, and specify which tasks apply to all Android Mobile solutions. The pinned page was fetched 2026-09-15 and records a 2026-03-17 last-modified timestamp; exact current versions and eligibility need current product/account checks. [[adyen]] [[adyen-mobile-pos]]

## Key takeaways

- For Android Tap to Pay and Card reader, Google Play distribution of the Mobile SDK-enabled app is optional. A merchant-built app going live must instead be registered in the **live** Customer Area with its package name and signing-certificate SHA-256 fingerprint. The guide says Adyen blocks all live transactions from an unregistered or tampered registered app. Multiple signing certificates for versions of the same app can be registered. Deleting a fingerprint unregisters the linked app, can take up to ten minutes to take effect, and blocks transactions with that app. These registration instructions expressly do **not** apply to the Android Payments app. See **Upload your app to Google Play** and **Register your app with Adyen**, pinned raw lines 21–39 and 65–119.
- For Tap to Pay and Card reader Mobile SDK integrations, the guide says each SDK version expires six months after release and is removed twelve months after expiry (eighteen months after release). At expiry, Android Tap to Pay and card-reader PIN transactions are blocked, while card-reader transactions without PIN remain possible. At removal, all transactions are blocked and the version is removed from GitHub. Version-specific dates are routed to Customer Area and release notes; the page does not specify a currently supported SDK version. See **Keep the Mobile SDK up to date**, pinned raw lines 121–168.
- The **Android Payments app** has its own six-month version expiry rule. The page says an expired app version no longer permits Tap to Pay on Android transactions, while only card-reader transactions without PIN remain possible. It does not state a Payments-app removal deadline. Its app-version maintenance section expressly excludes the merchant-built Tap to Pay and Card reader integrations. See **Keep the Android Payments app up to date**, pinned raw lines 170–196.
- Device OS maintenance applies to **all Android Mobile solutions**. The guide says Mobile SDK transactions are blocked below the minimum required Android version and sends readers to the software-requirements page for that minimum. Card-reader firmware maintenance applies only to the Android Card reader solution; dock firmware maintenance applies only to a card reader with a dock. Both require regular update checks, and a custom UI must supply update alerts/start controls if the SDK's built-in screens are not used. See pinned raw lines 198–245.
- The page points to Customer Area system messages and release notes for SDK, reader, Payments app and minimum-OS changes. It also describes SDK-supported UI languages, fallback and selection hierarchy, and says receipt-language changes require Support. These are dated documentation instructions, not proof of account notification setup or live device state. See pinned raw lines 247–311.

## Detail locators

- **Upload your app to Google Play** (pinned raw lines 21–63) — applicability, optional distribution, SDK Data safety fields, and version-2.14.0-or-later foreground-service declaration text and transaction-sync rationale.
- **Register your app with Adyen** (pinned raw lines 65–119) — scope, certificate/package data, live Customer Area path, blocked live transactions, multiple certificates, and destructive unregister behavior.
- **Keep the Mobile SDK up to date** (pinned raw lines 121–168) — exact expiry/removal effects, semantic versioning, support policy, and version-specific expiry lookup.
- **Keep the Android Payments app up to date** (pinned raw lines 170–196) — distinct app scope, six-month expiry and resulting transaction limits, plus support policy.
- **Keep the device OS up to date; Keep the card reader up to date; Keep the dock up to date** (pinned raw lines 198–245) — applicability, minimum-OS block, firmware maintenance, and built-in versus custom update UI.
- **Stay informed about version changes; Change the language** (pinned raw lines 247–311) — notification path, dated language list, UI fallback/hierarchy, and receipt-language Support route.

## Related

- [[adyen-mobile-pos]] — shared merchant-mobile in-person payments route.
- [[adyen-mobile-card-readers]] — physical card-reader and dock context.
- [[adyen-android-terminals]] — Adyen payment-terminal app deployment, distinct from merchant mobile app registration.
- [[adyen-android-sdk]] — native online-checkout SDK, separate from this in-person Mobile SDK lifecycle.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/mobile-android/manage/2026-09-15|Adyen Android Mobile management guide, fetched 2026-09-15]]
