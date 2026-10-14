---
title: "Adyen Android payment terminals"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/android-terminals"
raw_files:
  - "adyen/docs/point-of-sale/android-terminals/2026-09-15.md"
tags: [adyen, point-of-sale, android-terminals, terminal-apps]
---

## Overview

Adyen's Android terminals overview describes Adyen-provided payment terminals that can run Android apps while accepting in-person payments. It applies to Android terminals in Terminal API or standalone integrations. A payment can be initiated by a POS app installed on the terminal, a POS app on another device, or directly on an eligible standalone terminal. This is terminal hardware and on-terminal app guidance, distinct from merchant-phone Mobile SDK use and the native Android online-checkout SDK. [[adyen]] [[adyen-android-terminals]] [[adyen-terminal-api]]

## Key takeaways

- To make an app available on Adyen-provided Android terminals, first check the linked app requirements, including specifications, permissions and debugging-related security restrictions; then upload the app to Adyen and distribute it to terminals on a schedule, through profiles, or through API requests. The overview names these routes but leaves their detailed conditions to the linked guides.
- The dated model table lists AMS1, M450, P630, S1E, S1E Barcode, S1E2L, S1E4Pro, S1F2, S1F2 Barcode, S1F4Pro, S1U2 and SFO1, with hardware descriptions and Android versions. It identifies built-in scanners for specific models and printers for S1F2/S1F4Pro; S1F2 is expressly described as usable standalone. Treat the table as a 2026-09-15 documentation snapshot, not a current model, Android OS, firmware, certification or account-eligibility guarantee.
- The page warns that not all models are available in all regions and directs readers to their live Customer Area for regional availability. Android 9 versus 10 on S1F2/S1F2 Barcode is region-dependent in the table.
- Its next-step links route to menu access, terminal setup, app requirements and deployment, accessibility, barcode scanning, kiosk mode, remote troubleshooting and themes. These link labels are navigation, not proof that every feature works on every listed model.

## Detail locators

- Purpose, payment initiation modes and integration scope: pinned raw lines 15–35.
- App prerequisites and deployment sequence: pinned raw lines 37–44.
- Exact model, manufacturer, hardware and Android-version table: pinned raw lines 46–63.
- Regional availability warning and live Customer Area route: pinned raw lines 65–66.
- Feature-specific next-step routes: pinned raw lines 68–108.

## Related

- [[adyen-android-terminals]] — dedicated terminal-app and model route.
- [[adyen-terminal-api]] — POS-to-terminal payment-message integration.
- [[adyen-android-sdk]] — separately versioned native Android online-checkout SDK; it does not define these terminal models or app-deployment rules.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/android-terminals/2026-09-15|Adyen Android terminals overview, fetched 2026-09-15]]
