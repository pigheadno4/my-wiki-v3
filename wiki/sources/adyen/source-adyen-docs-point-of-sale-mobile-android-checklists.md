---
title: "Get-started and go-live checklists for Android | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/mobile-android/checklists"
raw_files:
  - "adyen/docs/point-of-sale/mobile-android/checklists/2026-09-15.md"
tags: [adyen, point-of-sale, mobile-pos, android, go-live, checklist]
---

## Overview

Adyen's Android Mobile POS checklists, captured 2026-09-15, separate build/test preparation from live-account, contract, credential, software-maintenance and penny-test steps. They cover merchant Android mobile devices using either an SDK-enabled POS app for Tap to Pay and/or NYC1 card reader, or the separate Adyen Payments app for Tap to Pay. Adyen says these Mobile solutions do not yet replace traditional terminals at feature parity and that geographic availability can differ by solution. This is a checklist, not evidence that any account, device, app, reader, transaction, or live rollout passed a gate. See [[adyen]], [[adyen-mobile-pos]], and [[adyen-mobile-card-readers]].

## Key takeaways

- For test preparation, choose the solution, check supported country/region, methods, features, Android hardware/software, and obtain a test account enabled by Adyen Support. The checklist calls for a test card and, only for the card-reader path, a test NYC1; it also calls for a supported Android mobile device, a POS app integrated with Terminal API, building the selected route and testing it. `warmUp` is recommended for an SDK integration, not stated as a universal Payments-app step.
- Going live separately calls for a live account if needed, a Mobile-solutions contract addendum and pricing with an Adyen contact, Support configuration of the live account, and card-reader rollout/quantity forecasting where relevant. Staff training and **live penny tests** are checklist steps. Their presence does not prove the contract was signed, a test ran, or funds were authorized, captured, settled or reconciled.
- The checklist says each **Mobile SDK version expires after six months** and Android minimum-version requirements may change. It calls for software distribution/update processes, system-message subscriptions, release-note monitoring, per-device diagnosis for installed SDK expiry, and reader firmware alerts for the card-reader path. It also calls for upgradeable compliant mobile hardware/software. The exact supported versions and regions live in linked requirement pages and must be checked separately.
- **SDK in your POS app:** the live branch calls for a dedicated live credential with only **Allow SDK download for POS developers**, a live SDK package, a separate live API-key/client-key credential with **Checkout webservice**, and live API key/endpoint for communication-session establishment. Google Play upload is optional; registration of the app with Adyen is listed. This branch applies to Tap to Pay or card-reader SDK solutions, not the separate Payments-app App Link flow.
- **Adyen Payments app:** its live branch also lists a live credential with only **Allow SDK download for POS developers**, then the Adyen app from Google Play, live **App Link URLs** and a live **Management API base URL**. Do not substitute the SDK branch's session setup or app registration for this branch from this checklist alone; check the linked build guide and current credentials before implementation.
- **Optional NYC1 dock:** order the dock plus Adyen's region-specific 12V/1.5A PD adapter, verify the required SDK and reader-firmware versions, show dock/Bluetooth/USB connection state in built-in or custom POS UI, and monitor/update dock firmware. The dock can charge the reader and, when USB-C connected, the mobile device; it can optionally replace Bluetooth with USB. The checklist does not establish present dock compatibility or successful reader operation.

## Detail locators

- Solution/region-feature choice, test enablement, supported device, Terminal API POS app, SDK-only warm-up and testing: [[raw/adyen/docs/point-of-sale/mobile-android/checklists/2026-09-15#Get-started checklist|Get-started checklist]] (raw lines 23–51). Linked support/requirements pages are navigation for exact eligibility.
- Live account, contract/pricing, Support configuration, SDK/OS/firmware maintenance, reader forecast, staff training and penny tests: [[raw/adyen/docs/point-of-sale/mobile-android/checklists/2026-09-15#Go-live checklist|Go-live checklist]] (raw lines 53–101).
- Two live credential/code branches: raw lines 75–97 under **Tab: SDK added to your POS app** and **Tab: Android Payments app**; the source does not verify today's role, endpoint or account availability.
- Optional dock order, Adyen adapter, version requirements, UI state and firmware duties: [[raw/adyen/docs/point-of-sale/mobile-android/checklists/2026-09-15#Checklist to add a dock|Checklist to add a dock]] (raw lines 103–126).

## Related

- [[adyen-mobile-pos]] — primary merchant Android-device in-person solution hub.
- [[adyen-mobile-card-readers]] — NYC1 reader and optional dock context.
- [[adyen-terminal-api]] — in-person POS request/response route.
- [[adyen-android-terminals]] — separate apps installed on Adyen payment terminals.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/mobile-android/checklists/2026-09-15|Adyen Android Mobile get-started and go-live checklists, captured 2026-09-15]]
