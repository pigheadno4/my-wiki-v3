---
title: "Adyen e355 Bluetooth pairing with a mobile device"
type: source
date_ingested: 2026-10-22
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/make-a-payment-on-the-e355-over-bluetooth/step-2-pair-the-e355-with-a-mobile-device"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/make-a-payment-on-the-e355-over-bluetooth/step-2-pair-the-e355-with-a-mobile-device/2026-09-15.md"
tags: [adyen, point-of-sale, e355, bluetooth, terminal-deprecation]
---

## Overview

This 2026-09-15-captured [[adyen]] e355 manual step explains Bluetooth pairing with an iOS or Android mobile device used as a cash register, followed by boarding where needed. The page is filed under **terminal deprecation** within [[adyen-payment-terminals]]; treat these model-specific menus and firmware notes as historical documentation, not current deployment approval (raw lines 14–20, 34–93).

## Key takeaways

- **Starting state and e355 frame exception:** The procedure says a mobile device can pair with an unboarded or previously boarded e355. If using the e355 frame with iOS, it says Bluetooth-menu connection is unnecessary; connect to the frame and restart the terminal instead (raw lines 16–20). Otherwise the terminal Admin → Network → Bluetooth menu selects iOS or Android by POS app; a boarded terminal skips that selection screen, and a mismatched displayed OS is a Support case (raw lines 22–32).
- **iOS pairing is separate from boarding:** Selecting iOS reboots the e355. The iOS device enables Bluetooth, the terminal scans and selects the device, and the user confirms the displayed code on terminal and mobile. On firmware through v36, a post-pair restart and iOS “not connected” Bluetooth label are documented; the instruction is to leave the Bluetooth menu and open the Adyen POS App, not to tap that label (raw lines 34–52). The app then shows “Not Boarded” when applicable and the user selects **Board Device**; after boarding and restart, the manual calls it ready to use (raw lines 54–72).
- **Android path:** The Adyen POS App uses merchant-account registration details, selects Payment device → Add new device → Bluetooth, chooses the scanned e355 and confirms the code on both devices. The page says an unboarded device then boards; the app identifies the terminal, synchronizes with Adyen's payments platform and verifies configuration before restart (raw lines 74–93). This is model-specific setup flow, not a payment result.
- **Safety of scope:** This page does not instruct a factory reset, credential disclosure to a third party, payment initiation or a change to terminal security settings. Pairing, boarding and being described as “ready” are distinct from a successful live payment or current terminal support.

## Detail locators

- Frame exception, Admin/Bluetooth menu and OS mismatch escalation: raw lines 18–32.
- iOS code confirmation, through-v36 behavior and POS App boarding: raw lines 34–72.
- Android account/app selection, code confirmation and boarding: raw lines 74–93.

## Evidence boundary

The manual's e355 and Adyen POS App screens are a dated terminal-deprecation path. A successful pairing or boarded-state message here does not establish present-day e355 availability, continuing platform connection, a payment authorization, or settlement. The firmware-through-v36 iOS “not connected” note applies only to that stated version range; do not generalize it to all firmware.

## Related

- [[adyen-payment-terminals]] — physical-terminal and historical-device route.
- [[source-adyen-docs-point-of-sale-user-manuals-terminal-deprecation]] — terminal-deprecation context.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/terminal-deprecation/e355-user-manual/make-a-payment-on-the-e355-over-bluetooth/step-2-pair-the-e355-with-a-mobile-device/2026-09-15|Pinned e355 Bluetooth-pairing manual step, captured 2026-09-15]]
