---
title: "Adyen Docs: Android Mobile system requirements"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/mobile-android/requirements"
raw_files:
  - "adyen/docs/point-of-sale/mobile-android/requirements/2026-09-15.md"
tags: [adyen, point-of-sale, mobile-pos, android, requirements, nyc1]
---

## Overview

Adyen's Android Mobile requirements page describes hardware and software gates for merchant POS applications on Android mobile devices. The POS app either embeds the Mobile SDK for Android or communicates with a separate Adyen Payments app that embeds it. The page also adds NYC1 reader and dock conditions for the card-reader solution. This 2026-09-15 snapshot is a requirements reference, not proof that any particular device, region, account, payment method, or integration is currently approved or working. [[adyen]] [[adyen-mobile-pos]]

## Key takeaways

- The Android mobile device can be a phone, handheld computer, tablet or similar, but the page requires **no integrated card reader**, an **integrated NFC reader** (detachable NFC is not MPoC-compliant in its wording), an integrated touchscreen, hardware key attestation, and Google certification. It recommends confirming attestation support with the manufacturer before purchase and setting a screen-lock passcode. The linked key-attestation demo app may rule out incompatibility; installing it or Google Play availability is not stated as an eligibility substitute. See **Hardware requirements → Mobile devices**, pinned raw lines 27–42.
- The page sets Android 12 as the minimum OS version and says the floor may change. It calls for the latest security patch and states a March 5, 2022 minimum patch, while recommending an OS version still supported by Google. These are dated floors, not a current security-patch or device-approval check. See **Software requirements**, pinned raw lines 68–76.
- For the card-reader solution, it names Adyen NYC1 models: **NYC1** is an SCRP reader certified for PIN transactions and requires Mobile SDK for Android 2.4.0 or later; **NYC1-SCR** handles transactions without PIN only. The page gives US NYC1 order availability from December 1, 2025 and an NYC1-SCR new-order end after February 1, 2026. Those order notices are snapshot claims, not current inventory. See **Hardware requirements → Card readers**, pinned raw lines 44–55.
- Disabling PIN support on an NYC1 is described for Mobile SDK for Android 2.9.0 or later and requires Adyen Support at company, merchant or store level. Do not infer that a non-PIN reader can process PIN transactions or that PIN support is automatically disabled. See pinned raw line 55.
- A countertop card-reader setup uses only Adyen's NYC1 dock and its Adyen power adapter; other readers and USB docks are unsupported in this guide. The dock path requires Android Mobile SDK 2.4.0 or later and card-reader firmware 3.X.00.76 or later. These conditions do not apply as a generic Android Payments app or Tap to Pay USB requirement. See **Card readers / Dock**, pinned raw lines 57–66.
- The page says the Mobile SDK expires every six months and directs SDK-integrated apps to regular latest-version updates. Card-reader software must also be updated and relates to SDK versions. The merchant POS app must integrate Terminal API; a separate Adyen Payments app embedding the Mobile SDK remains a distinct architecture, and this page does not spell out every credential or build step. See pinned raw lines 19–21 and **Software requirements**, lines 78–84.
- Country/region, payment-method and functionality availability is delegated to a separate linked page. This requirements snapshot alone does not establish those dimensions or a live payment outcome. See **See also**, pinned raw lines 91–94.

## Detail locators

- **Android system requirements** (pinned raw lines 15–21) — embedded Mobile SDK versus separate Payments app and page scope.
- **Hardware requirements → Mobile devices** (pinned raw lines 23–42) — device classes, integrated reader/NFC/touchscreen, attestation, certification and passcode recommendation.
- **Hardware requirements → Card readers** (pinned raw lines 44–57) — NYC1/SCR PIN split, SDK version gates, dated order notices and Support-enabled PIN disablement.
- **Hardware requirements → Dock** (pinned raw lines 59–66) — Adyen-only dock/adapter and SDK/firmware floors.
- **Software requirements** (pinned raw lines 68–89) — Android/security patch floor, SDK expiry and updates, reader software, Terminal API and Customer Area OS-version lookup.
- **See also** (pinned raw lines 91–94) — separate availability and management guides.

## Related

- [[adyen-mobile-pos]] — primary Mobile POS solution route.
- [[adyen-mobile-card-readers]] — paired reader hardware context.
- [[adyen-terminal-api]] — POS payment-message context.
- [[adyen-android-sdk]] — online-checkout SDK, a separate integration context.

## Related raw API references

These are links named by the snapshot, not additional evidence reviewed for this entry:

- Supported countries/regions, methods and functionality — https://docs.adyen.com/point-of-sale/ipp-mobile
- Keep Mobile SDK and card reader up to date — https://docs.adyen.com/point-of-sale/mobile-android/manage
- NYC1 card reader manual — https://docs.adyen.com/point-of-sale/user-manuals/nyc1/

## Raw Sources

- [[raw/adyen/docs/point-of-sale/mobile-android/requirements/2026-09-15|Adyen Android Mobile requirements, fetched 2026-09-15]]
