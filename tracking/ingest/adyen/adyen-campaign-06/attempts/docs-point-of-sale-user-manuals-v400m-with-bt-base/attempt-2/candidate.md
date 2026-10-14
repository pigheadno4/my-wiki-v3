---
title: "V400m with Bluetooth base station | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/v400m-with-bt-base"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/v400m-with-bt-base/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, v400m, bluetooth-base]
---

## Overview

This Adyen V400m user manual, captured 2026-09-15, describes inspecting and boarding a V400m payment terminal, pairing it with a Bluetooth base station that carries Ethernet connectivity and charges the docked terminal, checking platform/POS connections, and maintaining the device. It covers physical terminal setup for integrated or standalone use, not current model availability or a successful payment. See [[adyen]], [[adyen-payment-terminals]], [[adyen-terminal-management]], and [[adyen-standalone-terminals]].

## Key takeaways

- The Bluetooth base provides Ethernet LAN access for the V400m while docked or undocked, and charges it while docked. On first setup, inspect the terminal and its shipment for tampering, match serial numbers against the box and, when available, the Customer Area order, and contact Adyen Support immediately if a check fails. The manual lists supplied power, SIM, receipt-paper and base components; model-specific details remain in the raw.
- First charge the battery for at least four hours while completing setup. Temporarily connect the V400m to Wi-Fi and board it to the selected store **before first docking or Bluetooth pairing**. Boarding may take up to 30 minutes; if the boarding option is missing, the manual says to wait for the next Adyen synchronization (on average three hours) and try again. The base obtains software from the terminal, and first docking before boarding risks the base becoming stuck.
- For base-station Ethernet use, turn off the terminal's Wi-Fi, power the base, connect Ethernet to its marked LAN port, dock, make the base discoverable, and pair over Bluetooth after matching the displayed base serial number. Confirm both terminal and base IP addresses; DHCP assignment can take time. With **local** POS communications, update the POS system to the terminal's Bluetooth IP address; the POS or terminal may need a restart. Keep each terminal paired with its intended base.
- The manual provides separate diagnostic checks for Adyen PSP connectivity and, when integrated rather than standalone, Terminal API/POS and endpoint connectivity. A successful connection test is a network diagnostic, not proof of an authorized, captured or settled payment. The V400m cellular failover passage says pre-2022 boarded terminals may lack an activated SIM subscription; contact Support when uncertain.
- Some terminal menu actions require Admin & Settings, Transactions, or Refunds passcodes; Device info and Diagnostics do not. Software version 1.90+ uses a common menu structure across Android and non-Android terminals; earlier versions may differ. On first power-on or after prolonged shutdown, configuration/software synchronization may take 10–20 minutes.
- The terminal's Totals report covers amounts since its last reset. Reset starts a new reporting period and the previous period's totals are no longer shown there, though the manual says the immediately previous report remains accessible. For battery care, the manual calls for periodic leakage/swelling checks and says **not** to include a faulty battery in a terminal return package because of leakage and thermal-discharge risk. It describes terminal History receipt reprinting and direct payment initiation in standalone mode without claiming any transaction outcome.

## Detail locators

- `V400m with Bluetooth base station` and `Supplied components`, lines 15–46: device/base roles, charging, paper and other supplied items.
- `Get started`, lines 48–72: ordered first-use inspection, charging, Wi-Fi, boarding, pairing and connection tests.
- `Inspect the terminal`, lines 74–89: tamper and serial checks, Support escalation.
- `Connect to your network`, lines 97–130: Wi-Fi entry, post-boarding passcode, cellular failover qualification.
- `Set up the base station and the Bluetooth connection`, lines 132–177: boarding-before-docking reason, pairing, marked LAN port, serial match, IP checks, local POS setting.
- `Test the payments platform connection` and `Test the POS system connection`, lines 179–197: separate diagnostic routes and standalone exception.
- `Payment terminal menus` through `Turn on/off`, lines 199–269: menu/passcode map, device info, software-version menu qualification, power/sync behavior.
- `Maintain battery performance`, lines 271–293: storage, battery inspection and return-package warning.
- `View, print, and reset totals` through `Standalone solution`, lines 295–331: report reset boundary, receipt reprint and terminal-initiated standalone use.

## Related

- [[adyen-payment-terminals]] — physical payment-terminal setup and maintenance hub.
- [[adyen-terminal-management]] — Customer Area and Management API fleet administration.
- [[adyen-standalone-terminals]] — terminal-initiated payment mode.
- [[adyen-terminal-api]] — integrated POS message context.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/v400m-with-bt-base/2026-09-15|V400m with Bluetooth base station manual (2026-09-15 snapshot)]]
