---
title: "Adyen P400 Plus payment terminal user manual"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/p400-plus-user-manual"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/p400-plus-user-manual/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, p400-plus, hardware, user-manual]
---

## Overview

Adyen's **P400 Plus** physical payment-terminal manual, captured 2026-09-15, describes shipment inspection, dongle cabling, network setup, store boarding, connection diagnostics, power, menus and support. It routes to [[adyen-payment-terminals]] as model-specific hardware guidance; it is not the merchant-phone Mobile POS path. The captured page states that P400 Plus is no longer available for new orders except in Brazil, that Adyen repairs existing units until April 2029, and recommends P630 for new orders. Those dated availability and repair claims require current confirmation before procurement or support decisions.

## Key takeaways

- Before use, verify the shipping box and tamper tape, reconcile the box serial number with the Customer Area order **when access is available** and use that order's track-and-trace link to verify that the carrier confirms delivery, match the terminal serial number to the box, inspect for physical tampering, and contact Adyen Support immediately if any listed check fails. The terminal processes sensitive card data; a failed inspection is a stop-and-escalate condition, not a cosmetic issue.
- Initial setup connects the rear dongle and power, configures Ethernet LAN or Wi-Fi, boards the terminal to a selected store, then runs Adyen platform and POS system connection tests. Tighten the rear-cover cam lock screw **if present** to help protect the connector from cable pulls. The Ethernet cable belongs in the dongle's Ethernet/ETH port; using a wrong cable or port such as RS232 may severely damage the terminal. The guide says boarding can take up to 30 minutes; if **Board the terminal** is absent, wait for the next synchronization, given as three hours on average in this snapshot, and try again.
- Before boarding, Wi-Fi is configured through **Configure network**. After boarding, change Wi-Fi at **Settings > Network** with a passcode; the raw points to the separate menu-access page for managing that passcode. The platform diagnostic is **Settings > Diagnostics > PSP connection**; the POS diagnostic is **Terminal API** followed by **Endpoints**, which tests four URLs. A **Successful** result is a point-in-time connection check, not payment authorization, settlement or continuing connectivity. The page gives a narrow exception: **Receiving data** may show a red cross with **No Error** while platform connection still succeeded.
- Power-on is by connecting supply and power-off by disconnecting it; a first start or long shutdown may trigger a 10–20 minute configuration/software maintenance call. Reboot through **Settings > Power > Restart** requires the passcode. The manual's menu table distinguishes unprotected Device info/Diagnostics and standalone **Payment** from passcode-protected Settings configuration/network/software/power and Transactions payment/refund options. Standalone-only payment actions and refund passcodes must not be generalized to every POS-integrated flow. From software version **1.90**, the page says Android and non-Android terminals share a menu structure; older software may use the linked old non-Android menus.
- **Device info** exposes model, serial/IP address, software/configuration versions, merchant account and store. For unresolved problems, the manual directs self-service troubleshooting first, then Support with merchant account, transaction PSP reference if applicable, and terminal serial number.

## Detail locators

- Raw `# P400 Plus user manual` and `## Get started` (lines 15–64): dated discontinued/repair/P630 notice, supplied parts, conditional cam lock, network/store boarding and synchronization times.
- Raw `## Inspect the terminal` (lines 66–81): box, security tape, order/serial comparison, tamper indicators and immediate Support escalation.
- Raw `## Connect to your network` (lines 83–119): Ethernet/RS232 damage warning, Wi-Fi setup, and passcode-protected post-boarding changes.
- Raw `## Test the payments platform connection` and `## Test the POS system connection` (lines 121–139): separate PSP, Terminal API and four-endpoint diagnostics, including the **Receiving data**/**No Error** exception.
- Raw `## Turn on/off`, `## Payment terminal menus`, `## Device info` and `## Troubleshooting` (lines 141–224): maintenance timing, protected actions, version-qualified menus, standalone-specific payment controls and escalation details. Linked menu and troubleshooting guides need their own reading for additional behavior.

## Related

- [[adyen-payment-terminals]] — physical-terminal model hub.
- [[adyen-terminal-management]] — fleet and configuration administration.
- [[adyen-terminal-api]] — POS messaging referenced by diagnostics.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/p400-plus-user-manual/2026-09-15|P400 Plus user manual, fetched 2026-09-15]]
