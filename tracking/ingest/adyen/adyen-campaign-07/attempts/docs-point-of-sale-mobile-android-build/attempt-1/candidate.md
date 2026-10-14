---
title: "Adyen Android Mobile build overview"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/mobile-android/build"
raw_files:
  - "adyen/docs/point-of-sale/mobile-android/build/2026-09-15.md"
tags: [adyen, point-of-sale, mobile-pos, android, terminal-api]
---

## Overview

Adyen's Android Mobile build overview, captured 2026-09-15, directs developers to three merchant-mobile-device routes: Tap to Pay on Android and Card reader on Android embed the Mobile SDK in a POS app, while the Android Payments app enables Tap to Pay without embedding that SDK. This is a routing and integration-effort page for [[adyen-mobile-pos]], not the detailed requirements or behavior of any child guide. It is separate from apps installed on [[adyen-android-terminals]] and from the native online-checkout [[adyen-android-sdk]]. [[adyen]]

## Key takeaways

- For either embedded-SDK route, the page calls for a backend server-to-server communication-session setup and a POS app integrated with Terminal API. The POS app **must** support `PaymentRequest`; the page **prefers** support for `ReversalRequest` rather than stating it is mandatory.
- For the separate Android Payments app route, the POS app still needs Terminal API `PaymentRequest` support, with `ReversalRequest` preferred. The Payments app must be boarded on every Android mobile device where installed. This page does not give its boarding protocol or imply it uses the embedded SDK session flow.
- The overview says a native Mobile SDK can be integrated into a cross-platform app, but calls that complex and says Adyen offered no cross-platform wrappers at this snapshot. Teams using a ready-made partner Mobile solution are directed to skip this build section.
- Its links to `Understand your solution` and the three build guides are navigation. They do not establish current OS/device/region support, account activation, SDK/API versions, reader model or PIN conditions, Payments app App Link details, or successful payment execution. Read the relevant child and requirements guides for those claims.

## Detail locators

- Raw `# Build your Android Mobile solution` (lines 15–23): scope, partner-solution exception and route to solution understanding.
- Raw `## Integration effort` / `### Tap to Pay or Card reader on Android` (lines 25–39): backend session, Terminal API obligation and cross-platform wrapper statement.
- Raw `### Android Payments app` (lines 41–49): separate Terminal API and per-device boarding work.
- Raw `## Choose a solution` (lines 51–65): exact child-guide links for Tap to Pay, card reader and Payments app.

## Related

- [[adyen-mobile-pos]] — common merchant-device Mobile POS route.
- [[adyen-mobile-card-readers]] — hardware context for the card-reader path.
- [[adyen-android-terminals]] — apps installed on payment-terminal hardware.
- [[adyen-android-sdk]] — separate native online-checkout SDK.

## Related raw API references

The following URLs are navigation named in the overview; no child-guide behavior is inferred from them here:

- Understand Android Mobile solutions — https://docs.adyen.com/point-of-sale/mobile-android/understand
- Tap to Pay on Android build — https://docs.adyen.com/point-of-sale/mobile-android/build/tap-to-pay
- Card reader on Android build — https://docs.adyen.com/point-of-sale/mobile-android/build/card-reader
- Android Payments app build — https://docs.adyen.com/point-of-sale/mobile-android/build/payments-app

## Raw Sources

- [[raw/adyen/docs/point-of-sale/mobile-android/build/2026-09-15|Build your Android Mobile solution, fetched 2026-09-15]]
