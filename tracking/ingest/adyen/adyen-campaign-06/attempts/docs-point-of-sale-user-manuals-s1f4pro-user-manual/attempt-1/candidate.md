---
title: "Adyen Docs: S1F4Pro user manual"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/s1f4pro-user-manual"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/s1f4pro-user-manual/2026-09-15.md"
tags: [adyen, point-of-sale, android-terminals, s1f4pro, device-manual]
---

## Overview

Adyen's S1F4Pro payment-terminal manual, captured 2026-09-15 and marked last modified 2024-12-16, covers the physical Android device's first-use inspection, paper roll, network connection, store confirmation, menus, power care, and support. It is a device-operation guide, not proof of current regional availability, merchant enablement, boarding, or payment execution. [[adyen]] · [[adyen-android-terminals]]

## Key takeaways

- Supplied items include the S1F4Pro terminal, a USB charging cable with region-specific power plug, eSIM, and receipt paper. Its barcode-scanner button is nonfunctional; camera scanning requires an implementation in the organization's on-terminal Android app. Do not assume the physical button scans.
- Before use, check the intact shipping tape, reconcile box, order and device serial numbers where Customer Area order access is available, confirm carrier delivery, and inspect the device for tampering. If any check fails, contact Adyen Support immediately. The guide then has the operator insert paper, power on, charge for at least four hours, choose language, connect to the network, and confirm or correct the shown store. If the store screen is absent, it says to wait for the next Adyen synchronization (on average three hours) and try again.
- Wi-Fi setup is through the Welcome screen; later changes use passcode-protected **Settings > Network**. The manual describes automatic cellular 3G/4G failover with a preinstalled eSIM, but notes that a terminal boarded before 2022 might lack SIM activation if no subscription existed at boarding; contact Support when uncertain. Its first power-on or return after a long shutdown may take 10–20 minutes for a maintenance call.
- For long storage, the manual advises cool/dry conditions, avoiding heat, keeping battery charge between 40% and 70%, checking for leakage/swelling every six months, and recharging as needed. Use Adyen's supplied USB-C cable and avoid damaging its connector. If returning a terminal with a faulty battery, dispose of the battery under local rules and do not put it in the return package because of leakage and thermal-discharge risk.
- **Settings** and **Transactions** menu functions have different passcode boundaries; **Payment** starts a normal transaction only when the device is used as a standalone terminal. The terminal's Totals report covers sales, refunds, tips, and cancellations since its last reset; resetting starts a new reporting period. The manual also points to kiosk mode and airline airplane mode: Support must enable airplane mode before its Network toggle is available, and turning it on disables Wi-Fi, Bluetooth, and cellular connections.

## Detail locators

- **Identity and first use:** raw `Supplied components` (lines 23–32), `Get started` (34–53), `Inspect the terminal` (55–70), and `Insert the receipt paper roll` (72–76). These contain the camera-scanning condition, serial/tamper procedure, store-screen timing, and paper insertion steps.
- **Connectivity:** `Connect to your network` (78–111) gives Welcome-screen Wi-Fi setup, later passcode-protected changes, and the eSIM exception. `Turn on/off` (113–125) gives power controls and possible maintenance delay.
- **Physical care:** `Maintain battery performance` (127–149) has charge/storage inspection and faulty-battery return guidance; `Use the USB-C charging cable` (151–164) gives model-specific cable and socket handling.
- **Menus and reports:** `Payment terminal menus` (166–201) has a menu/passcode table. `Device info` (203–217) lists model, serial, versions, merchant/store, and address. `View, print, and reset totals` (219–240) explains report period and reset; the daily auto-reset option refers to Support.
- **Modes and help:** `Standalone solution` (242–245), `Kiosk mode` (247–251), `Airplane mode` (253–277), and `Troubleshooting` (279–293). Remote troubleshooting requires selecting **Start session** and entering a passcode, allowing support staff to view and interact with the terminal screen.

## Related

- [[adyen-android-terminals]] — Android payment-terminal and installed-app scope
- [[adyen-terminal-management]] — fleet assignment and configuration context
- [[adyen-terminal-api]] — payment-message architecture, distinct from device operation

## Related raw API references

Linked Customer Area, cellular, battery, standalone, kiosk, menu-access, and troubleshooting guides were not read for this entry; treat them as navigation only.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/s1f4pro-user-manual/2026-09-15|Adyen S1F4Pro user manual, fetched 2026-09-15]]
