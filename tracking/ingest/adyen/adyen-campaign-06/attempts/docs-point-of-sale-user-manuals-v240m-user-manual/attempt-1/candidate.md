---
title: "Adyen Docs: V240m Plus user manual"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/v240m-user-manual"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/v240m-user-manual/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, v240m-plus, user-manual]
---

## Overview

Adyen's V240m Plus model manual, captured 2026-09-15, covers physical inspection, power and paper, network configuration, store boarding, connection diagnostics, menu access, battery care, totals, receipts, and standalone use. It is a historical device-specific procedure, not a universal setup sequence for every Adyen terminal or proof of current hardware availability, connectivity, security status, or payment success. [[adyen]] · [[adyen-payment-terminals]]

## Key takeaways

- The V240m Plus does **not** support 4G or later. The manual describes cellular failover and a pre-installed SIM/eSIM, but warns that devices boarded before 2022 might lack an activated SIM; its 2G/3G coverage warning means the presence of cellular hardware does not establish usable current service. A deployment relying on cellular connectivity needs a currently supported device and network.
- Before setup, inspect the sealed shipment and terminal for tampering; compare serial numbers on the box, device, and Customer Area order where available. Contact Adyen Support immediately if a check fails. The V240m Plus startup sequence then inserts receipt paper, connects power, charges the battery for at least four hours while setup continues, configures Wi-Fi, boards to a selected store, and checks connections. The manual says boarding can take up to 30 minutes and the board option may await a platform synchronization averaging three hours.
- A `Successful` PSP connection diagnostic verifies the device's connection to Adyen at that point. For POS-integrated use, the separate Terminal API and four endpoint checks test the POS connection; the POS test is skipped for standalone use. These diagnostics do not guarantee continuing network service, transaction authorization, or settlement.
- Settings/menu functions differ by passcode: Device info and Diagnostics are listed without a passcode, while Configuration, Network, Software, and Power need Admin & Settings access. Transaction menu operations have their own access requirements. The menu table is qualified from software version 1.90, with older non-Android menu structures possible.
- Long storage can damage the battery; the manual gives temperature, charge-level, and six-month inspection advice. For a faulty battery return, dispose of the battery under local rules and do not include it in the return package because of leakage and thermal-discharge risk. Resetting Totals starts a new report period and stops showing the previous period in the current report, although the prior period report remains accessible through the menu.

## Detail locators

- **Model and physical start:** opening warning (line 21), “Supplied components” (33–40), “Get started” (42–62), “Inspect the terminal” (64–79), and “Insert the receipt paper roll” (81–85). The terminal, power supply, SIM card, and 57 × 40 mm paper roll are listed; an optional base or new rolls are Customer Area orders.
- **Network and boarding:** “Connect to your network” (87–120), including Wi-Fi setup, post-boarding passcode and IP settings, and cellular-failover caveats. “Get started” has the store-selection/boarding sequence and timing; these are this model's snapshot instructions.
- **Connection checks and power:** “Test the payments platform connection” (122–129), “Test the POS system connection” (131–140), and “Turn on/off” (142–160). The PSP diagnostic has a stated `Receiving data` red-cross/`No Error` exception; see the exact screen conditions in raw. POS checks apply only to POS-connected use.
- **Battery and menus:** “Maintain battery performance” (162–184), “Payment terminal menus” (186–222), and “Device info” (224–236) for storage and return cautions, software-qualified menu layout, passcodes, and current device/account/store identifiers.
- **Local reporting and mode:** “View, print, and reset totals” (238–258), “Reprint transaction receipt” (260–269), and “Standalone solution” (271–274). Standalone payments start on the terminal rather than a POS; this manual links to a separate standalone transaction guide.

## Related

- [[adyen-payment-terminals]] — model-specific physical hardware and setup
- [[adyen-terminal-management]] — separate ordering, assignment, and fleet administration
- [[adyen-terminal-api]] — POS-to-terminal messaging and diagnostics boundary

## Related raw API references

The linked end-of-3G, network-configuration, boarding, standalone-payment, menu-access, and troubleshooting guides were not read for this entry; use them as navigation only.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/v240m-user-manual/2026-09-15|Adyen V240m Plus user manual, fetched 2026-09-15]]
