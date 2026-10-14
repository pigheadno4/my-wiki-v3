---
title: "V400m user manual | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/v400m-user-manual"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/v400m-user-manual/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, v400m, user-manual]
---

## Overview

This 2026-09-15 Adyen Docs snapshot is a physical V400m payment-terminal manual: inspect the delivered device, power and network it, board it to a store, run connection diagnostics, and maintain its battery, receipt printer and menus. Its prominent discontinuation notice says V400m terminals are no longer available for new orders and that Adyen repairs existing units until April 2029. Those are dated page claims, not a live inventory, current repair commitment, or payment result. See [[adyen]] and [[adyen-payment-terminals]].

## Key takeaways

- The manual's V400m setup sequence is inspection, paper insertion, power and at least four hours of battery charging, network connection, store boarding, Adyen-platform diagnostics, and POS-system diagnostics when used with a POS. It says boarding can take up to 30 minutes; if the option is absent, wait for the next Adyen synchronization (on average three hours) and try again. A standalone terminal skips the POS-system connection test.
- Because the terminal handles card data, inspect the unopened box and tamper tape; compare serial numbers on the box, device and, if accessible, Customer Area order; examine the device for physical alterations. If a check fails, contact Adyen Support immediately. The manual does not establish that a particular device passed inspection.
- Initial Wi-Fi configuration uses network selection or manual SSID/password entry. After boarding, network changes require the appropriate passcode. The V400m section describes possible cellular failover and warns that terminals boarded before 2022 may lack an activated SIM subscription. For replacement of an old or defective **physical** SIM, power off the device, remove the battery and use the SIM tray without metal tools; this is separate from the page's eSIM availability wording.
- Adyen-platform PSP diagnostics and integrated POS Terminal API/endpoint diagnostics are separate checks. A successful connection check establishes only connectivity, not payment authorization or settlement. The manual's menu table gives Admin & Settings, Transactions and Refunds passcode boundaries; menus before software 1.90 may use an older structure.
- Long-idle or first power-on can trigger a 10–20 minute maintenance call for configuration/software synchronization. The manual recommends battery storage and inspection practices and says to dispose of a faulty battery under local regulations rather than include it in a terminal return package because of leakage and thermal-discharge risk.
- Resetting the terminal's Totals report starts a new reporting period: the old period is no longer shown as the current report, while the immediately previous report remains accessible. The manual also locates receipt reprinting under Transactions History and distinguishes terminal-initiated standalone payments from POS-initiated transactions. Optional charging or Bluetooth Ethernet bases are mentioned as accessories; the dedicated base manual owns their setup.

## Detail locators

- `V400m user manual`, lines 15–43: discontinuation/repair statement, supplied components and optional base accessories.
- `Get started`, lines 45–65: inspection, charging, networking, boarding and integrated-versus-standalone diagnostics.
- `Inspect the terminal`, lines 67–82: tamper, serial and delivery checks with Support escalation.
- `Connect to your network`, lines 90–123: Wi-Fi setup, post-boarding passcode and cellular failover qualification.
- `Replace physical SIM card`, lines 125–145: power-off, battery/SIM handling and no-metal-tool warning.
- `Test the payments platform connection` and `Test the POS system connection`, lines 147–165: PSP and Terminal API/endpoint checks.
- `Payment terminal menus` and `Device info`, lines 167–217: menu/passcode map, software 1.90 qualification and on-device identity/version fields.
- `Turn on/off` and `Maintain battery performance`, lines 219–261: synchronization window, power, battery storage/inspection and disposal warning.
- `View, print, and reset totals` through `Standalone solution`, lines 263–299: reset effect, receipt reprint and transaction initiation mode.

## Related

- [[adyen-payment-terminals]] — physical payment-terminal setup and maintenance.
- [[adyen-terminal-management]] — fleet ordering, assignment and configuration.
- [[adyen-terminal-api]] — integrated POS messages and connectivity context.
- [[adyen-standalone-terminals]] — terminal-initiated payment mode.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/v400m-user-manual/2026-09-15|V400m user manual (2026-09-15 snapshot)]]
