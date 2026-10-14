---
title: "Adyen S1U2 unattended terminal user manual"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/s1u2-user-manual"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/s1u2-user-manual/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, s1u2, unattended, android]
---

## Overview

Adyen's S1U2 manual, last modified 2020-11-27 and captured 2026-09-15, describes an all-in-one Android payment terminal for unattended and outdoor use, mounted in a kiosk or other self-service machine. It has a camera and barcode scanner and accepts swipe, insert and tap presentation at the terminal. Its primary route is [[adyen-payment-terminals]]; its Android menus and kiosk mode also relate to [[adyen-android-terminals]]. This is a payment terminal, not the merchant-phone [[adyen-mobile-pos]] reader path. [[adyen]]

## Key takeaways

- Assign the S1U2 to a store **before boarding**; the manual says unattended terminals differ from most other terminals on this sequence. Initial setup then requires inspection, mounting, cabling, boarding to the assigned store, and software update. The statement that these steps make the device ready to process payments is the manual's setup sequence, not proof of a particular live account, connection or authorization.
- Before use, verify the unopened box and tamper tape, reconcile the box, Customer Area and device serial numbers, and inspect for missing screws, extra wires or labels, holes and attachments. If any check fails, contact Adyen Support immediately. Mounting relies on the kiosk manufacturer's instructions and a linked Castles installation guide; this page alone is not a mechanical installation specification.
- The MDB harness connects power and optionally audio; Ethernet connects directly to the terminal, not through that harness. The manual describes Ethernet or Wi-Fi, with a pre-installed eSIM for cellular 3G/4G failover when internet connectivity fails. It warns that an eSIM may be inactive on terminals boarded before 2022 when no SIM subscription had been set up; Support is the stated route when uncertain. This is a dated model statement, not proof of present SIM activation or uninterrupted transactions.
- The terminal boards only after store assignment and confirms the displayed store. A software update through **Settings > Device info > Software version** requires the Admin & Settings passcode and reboots the device. Protected menus distinguish Admin & Settings, Transactions and Refunds passcodes. Opening **Apps** can execute an app install or removal already scheduled; **Totals** can reset transaction totals. Neither menu action is described as a factory reset.
- Kiosk mode hides the navigation bar and bottom Settings/Transactions buttons to restrict shopper access to the default app and power controls; enabling it is delegated to a separate guide. Remote troubleshooting requires the operator to start a session on the terminal and enter a passcode. The manual does not establish current app eligibility, remote-session authorization, terminal availability, or payment outcome.

## Detail locators

- Raw `# S1U2 user manual` and `### Supplied components` (lines 15–34): unattended/outdoor identity, card presentation and supplied power, antenna, eSIM and mounting parts.
- Raw `## Get started` through `## Inspect the terminal` (lines 35–76): store assignment before boarding, setup sequence, security inspection and Support escalation.
- Raw `## Mount the terminal` through `## Connect to your network` (lines 77–136): external mounting instructions, MDB/Ethernet connection distinction, Wi-Fi setup/passcode and eSIM failover caveat.
- Raw `## Board the terminal` through `## Payment terminal menus` (lines 137–185): store confirmation, software update/reboot, menu access, scheduled Apps action and transaction totals reset.
- Raw `## Device info` through `## Troubleshooting` (lines 186–222): device/store details, kiosk-mode purpose, operator-assisted remote support and required support identifiers.

## Related

- [[adyen-payment-terminals]] — primary model-specific physical-terminal route.
- [[adyen-android-terminals]] — on-terminal Android menus, app actions and kiosk mode.
- [[adyen-terminal-management]] — store assignment and fleet administration.
- [[adyen-mobile-pos]] — separate merchant mobile-device route.

## Related raw API references

Navigation named by the manual, not further evidence reviewed for this entry:

- S1U2 installation reference guide — https://docs.adyen.com/point-of-sale/user-manuals/s1u2-user-manual/S1U2-installation-reference-guide.pdf
- Assign terminals — https://docs.adyen.com/point-of-sale/managing-terminals/assign-terminals
- Kiosk mode — https://docs.adyen.com/point-of-sale/android-terminals/kiosk-mode

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/s1u2-user-manual/2026-09-15|S1U2 user manual, fetched 2026-09-15]]
