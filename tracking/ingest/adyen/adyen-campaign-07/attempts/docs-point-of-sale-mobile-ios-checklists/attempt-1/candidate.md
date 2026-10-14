---
title: "iOS Mobile get-started and go-live checklists | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/mobile-ios/checklists"
raw_files:
  - "adyen/docs/point-of-sale/mobile-ios/checklists/2026-09-15.md"
tags: [adyen, point-of-sale, mobile-pos, ios, go-live, card-reader]
---

## Overview

Adyen's dated iOS Mobile checklist separates preparing to **build and test** from preparing to **go live** with Tap to Pay on iPhone, an NYC1 Card reader solution, or both, and adds a conditional NYC1 dock checklist. The page warns that Mobile solutions are not yet a replacement for traditional terminals and that geographic availability can differ by solution. This is a sequence of documented gates, not evidence that an Apple entitlement, Adyen account, credential, device, or payment has been approved or tested. [[adyen]] [[adyen-mobile-pos]] [[adyen-mobile-card-readers]]

## Key takeaways

- For testing, choose the iOS solution against supported countries/regions, payment methods, features and device/software requirements; arrange an Adyen test account, ask Support to configure it for iOS Mobile SDK use, obtain a test card and (for the reader path) test NYC1, use a supported iOS device, and have an iOS mobile POS app integrated with **Terminal API**. The page recommends SDK warm-up for SDK integrations and then testing, but does not itself supply an SDK version, minimum iOS version, or passing test result. See **Get-started checklist**, pinned raw lines 23–51.
- Go-live adds a live account if new to Adyen, a contract addendum/pricing with Adyen, live-account Mobile SDK configuration by Support, and update/distribution processes. **Tap to Pay on iPhone** specifically requires applying for an Apple LIVE entitlement in time (the page says approval can take weeks) and accepting Apple Terms of Use. The reader path calls for a rollout forecast. These are distinct path conditions, not blanket prerequisites for every iOS Mobile setup. See **Go-live checklist**, pinned raw lines 53–65 and 87–93.
- The checklist says each Mobile SDK version expires after six months and the minimum iOS version can change. It calls for software distribution and maintenance, Customer Area update notices, release-note checks, a mobile diagnosis request to inspect each installed SDK's expiry, and a card-reader Device Manager update alert where relevant. Device hardware/software compliance remains a separate requirements-guide check. See pinned raw lines 65–75.
- For live Tap to Pay or reader SDK integrations, the checklist calls for a **live** basic-auth API credential with **Allow SDK download for POS developers**, the live SDK, a separate live API-key credential with **Checkout webservice role**, and code pointing at the live API key and live endpoint for establishing a communication session. It then calls for penny tests of the live solution and staff training. The list does not prove a live session, authorization, settlement or reconciliation. See pinned raw lines 77–93.
- The conditional **NYC1 dock** checklist covers dock plus Adyen NYC1 adapter ordering, SDK/reader-firmware compatibility, dock-connection status UI, dock-firmware alerts/updates, an `Info.plist` USB-permission key, and an MFi PPID request when submitting the app to the App Store. The reader/dock path also needs a custom UI for the listed status/update actions if the Mobile SDK built-in screens are not used. Exact version and permission details live in linked guides. See pinned raw lines 95–120.

## Detail locators

- **Get-started checklist** (pinned raw lines 23–51) — solution selection, test account/Support, test hardware, Terminal API POS app, SDK dependency awareness, optional warm-up recommendation and test step.
- **Go-live checklist** (pinned raw lines 53–93) — path-specific Apple/reader/commercial gates, update lifecycle, live credential roles and communication-session endpoint, penny tests and staff readiness.
- **Checklist to add a dock** (pinned raw lines 95–120) — ordered equipment, version gates, connection UI, firmware/UI duties, USB permissions and conditional MFi PPID.
- **See also** (pinned raw lines 122–125) — build and maintenance guides for implementation details.

## Related

- [[adyen-mobile-pos]] — primary mobile in-person solution route.
- [[adyen-mobile-card-readers]] — NYC1 reader and optional dock hardware context.
- [[adyen-terminal-api]] — POS application integration named by the test checklist.
- [[adyen-ios-sdk]] — native online-checkout SDK; do not use its version or flows as Mobile POS SDK evidence.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/mobile-ios/checklists/2026-09-15|iOS Mobile get-started/go-live checklists, fetched 2026-09-15]]
