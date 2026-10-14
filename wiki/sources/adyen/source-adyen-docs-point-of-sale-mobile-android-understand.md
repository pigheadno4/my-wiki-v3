---
title: "Adyen Android Mobile solution choices and flows"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/mobile-android/understand"
raw_files:
  - "adyen/docs/point-of-sale/mobile-android/understand/2026-09-15.md"
tags: [adyen, point-of-sale, mobile-pos, android, tap-to-pay, card-reader, payments-app, terminal-api]
---

## Overview

This dated Adyen comparison helps choose among Android Mobile in-person payment solutions. A merchant POS app can embed the **POS Mobile SDK** for Tap to Pay on the Android device, an NYC1 card reader, or both. Alternatively, the POS app can hand off Tap to Pay through App Links to the separate **Adyen Payments app**, which contains the Mobile SDK. Both integration shapes require Terminal API and merchant frontend and backend work. See [[adyen-mobile-pos]] for the solution map; this is separate from apps installed on Adyen Android payment terminals and from the native online [[adyen-android-sdk]].

## Key takeaways

- The Mobile SDK route gives the merchant in-app experience control and supports both Tap to Pay and card readers. The source's comparison says to update the SDK every six months and lists PCI MPoC compliance requirements. The Payments app route uses Links and API with app switching and per-device boarding; the source describes lower integration effort, Adyen-managed updates, no PCI MPoC compliance requirements for that route, and **Tap to Pay only**. These are the source's dated comparative claims, not a current eligibility determination. See raw § SDK or Payments app (lines 24–44).
- In the embedded SDK route, the POS app calls its backend to initiate a server-to-server `POST /auth/certificate` and obtain session data for secure SDK communication with Adyen; the SDK checks session validity and refreshes when needed. The POS app creates or receives a Terminal API request, passes it to the SDK, and receives the Terminal API response from it. Optional warm-up is recommended, not required. See raw §§ Communication session and SDK transaction flow (lines 46–70).
- In the Payments app route, the POS app sends an **encrypted, Base64URL-encoded** Terminal API payment request with a return URL through an Android App Link. The separate app presents the NFC Tap to Pay screen, routes through the POS Mobile SDK to Adyen, then returns an encrypted, encoded response via the return URL. The diagrammed flow is a message and UI route, not proof of authorization, capture or settlement. See raw § Payments app transaction flow (lines 72–82).
- PIN can be part of Tap to Pay or card-reader solutions, with randomized on-screen PIN-pad placement under the cited PCI MPoC requirement. For US NYC1 card readers, PIN requires a PIN-capable model and Mobile SDK 2.4.0 or later; `connectedDevice.model` distinguishes **SCRP** (PIN) from **SCR** (no PIN). The source routes full reader requirements elsewhere. See raw § PIN transactions (lines 84–111).
- For an NYC1 reader, the SDK offers built-in UI or permits merchant-built UI for Bluetooth or supported USB connections, reader details and firmware. Reader firmware must be checked and updated; a custom UI must implement the update flow. A dock adds USB connection and dock-firmware operations, with built-in or custom UI. See raw §§ UI for card reader operations and UI for dock operations (lines 113–181); see also [[adyen-mobile-card-readers]].
- Kiosk mode is a Tap to Pay UI option for larger screens. The source says **do not use it in an unattended environment** under PCI MPoC requirements. It activates automatically from 9-inch screen width, with a documented option for smaller devices. See raw § Kiosk mode (lines 183–194).

## Detail locators

- Raw § SDK or Payments app: comparative table and shared Terminal API requirement (lines 24–44).
- Raw §§ Communication session, SDK transaction flow and Payments app transaction flow: separate session and payment-message paths (lines 46–82).
- Raw §§ PIN transactions, card reader and dock UI, Kiosk mode: model, firmware, custom UI and attended-use qualifications (lines 84–194).

## Related

- [[adyen-mobile-pos]] — Android Mobile POS hub and sibling build guides.
- [[adyen-terminal-api]] — in-person request and response message family.
- [[adyen-mobile-card-readers]] — NYC1 reader hardware and pairing evidence.
- [[adyen-android-terminals]] — distinct payment-terminal app route.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/mobile-android/understand/2026-09-15|Understand the Android Mobile solutions, fetched 2026-09-15]]
