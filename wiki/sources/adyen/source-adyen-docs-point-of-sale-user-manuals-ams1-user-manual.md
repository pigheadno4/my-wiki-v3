---
title: "Adyen AMS1 payment terminal user manual"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/ams1-user-manual"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/ams1-user-manual/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminal, ams1, hardware, security]
---

## Overview

Adyen's AMS1 user manual covers physical inspection, first power and store assignment, Wi-Fi/cellular connectivity, battery and USB-C care, on-device menus, reporting, operating modes and support. AMS1 is an Adyen **payment terminal**, not a merchant phone using the Mobile SDK or an attached card reader. The 2026-09-15 capture is model-specific operating guidance, not proof of current regional availability, certification, terminal boarding or payment success. [[adyen]] [[adyen-payment-terminals]] [[adyen-android-terminals]]

## Key takeaways

- The supplied kit lists an AMS1, USB cable with a region-specific charging plug, and eSIM. First setup powers the terminal from a supply, charges it for at least four hours, selects language and network, then confirms or edits the shown store. If the store screen is absent, the guide says to wait for the next Adyen-platform synchronization (on average three hours) and retry. A first start or start after prolonged power-off may make a maintenance call for configuration/software that takes 10–20 minutes. These are documented setup conditions, not evidence that this device is boarded. See `### Supplied components`, `## Get started`, and `## Turn on/off`.
- Before use, verify the box's tamper tape, reconcile box, Customer Area order (if accessible) and device serial numbers, and inspect for screws/wires/labels/holes/attachments indicating tampering. Contact Adyen Support immediately if any check fails. See `## Inspect the terminal`.
- The terminal uses Wi-Fi for platform and backend communication; changing Wi-Fi later uses the protected **Settings > Network** menu. The manual describes 3G/4G cellular failover and a preinstalled activated eSIM for boarding, but notes SIM activation may be absent on terminals boarded before 2022 without a subscription at that time; ask Support if uncertain. See `## Connect to your network`.
- Long storage can degrade or permanently damage the battery. The manual gives cool/dry storage, 40–70% charge bounds and six-month leakage/swelling checks. For a faulty battery, follow local disposal rules and **do not include it in a returned terminal package** because of leakage/thermal-discharge risk. It directs use of the supplied USB-C cable and region-specific plug, careful straight insertion/removal, and checks for foreign objects. See `### Maintain battery performance` and `## Use the USB-C charging cable`.
- The Settings and Transactions menus have action-specific passcodes: ordinary device info, diagnostics and display are unprotected; Apps, Configuration, Network, software-version controls and Power require Admin & Settings; history, totals and new transaction require Transactions, while a new refund requires Refunds. Device info exposes model, serial, network address, software/configuration, merchant account and boarded store. The Totals reset starts a new reporting period; the manual describes report totals since the last reset, without claiming payment data deletion. See `## Payment terminal menus`, `## Device info`, and `## View and reset totals`.
- Kiosk mode hides navigation and settings/transaction buttons for unattended use, with enablement in a separate Android-terminal guide. Airline airplane mode requires Support enablement, then a Network-menu passcode; turning it on disables Wi-Fi, Bluetooth and cellular, and turning it off restores previous connections. For remote troubleshooting, company staff or Adyen Support ask the operator to start a session and enter a passcode, allowing them to see and interact with the screen. See `## Kiosk mode`, `## Airplane mode`, and `## Troubleshooting`.

## Detail locators

- `## Get started` and `## Inspect the terminal`: first charge, store-screen synchronization caveat, serial and tamper checks.
- `## Connect to your network` and `## Turn on/off`: Wi-Fi setup, protected changes, 3G/4G eSIM caveat, maintenance-call timing.
- `### Maintain battery performance` and `## Use the USB-C charging cable`: storage thresholds, faulty-battery return hazard, approved cable and socket precautions.
- `## Payment terminal menus`–`## View and reset totals`: exact passcode/action matrix, device-info fields and reporting-period reset.
- `## Kiosk mode`–`## Troubleshooting`: unattended/airplane-mode boundaries and passcode-mediated remote assistance.

## Related

- [[adyen-payment-terminals]] — physical-terminal model manuals.
- [[adyen-android-terminals]] — Android-terminal on-device controls and app context.
- [[adyen-terminal-management]] — administrative fleet assignment and maintenance.
- [[adyen-security-incident-response]] — broader tamper and incident handling.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/ams1-user-manual/2026-09-15|Adyen AMS1 user manual, fetched 2026-09-15]]
