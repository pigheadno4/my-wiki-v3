---
title: "Adyen Docs: M400 user manual"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/m400-user-manual"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/m400-user-manual/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, m400, user-manual]
---

## Overview

Adyen's M400 manual covers the physical terminal, delivered components, first setup, inspection, dongle/network connection, store boarding, connection diagnostics, power, menus, device information, and support. Its snapshot says the M400 is discontinued for new orders and that Adyen repairs existing M400 terminals until April 2029, recommending M450 or SFO1 for new orders. The page was last modified in 2019 and captured on 2026-09-15; this is dated model guidance, not a current stock, repair-policy, terminal-integrity, network, or payment-success check. [[adyen]] [[adyen-payment-terminals]]

## Key takeaways

- **Discontinued model:** the manual says M400 terminals are unavailable for new orders and gives an April 2029 repair endpoint for existing units. M450 and SFO1 are named as recommended alternatives, not established substitutes for a specific merchant deployment. See pinned raw lines 15–20.
- **First setup:** inspect the unit, connect the supplied Cube Ethernet dongle behind the terminal cover, power it, configure a network, then select **Board the terminal**, choose a store, and confirm. The guide says boarding can take up to 30 minutes; if the option is missing, wait for the next platform synchronization (on average three hours) and try again. Then run separate Adyen-platform and POS-system connection diagnostics. These estimates and tests do not prove boarding, ongoing connectivity, or payment authorization. See **Get started**, pinned raw lines 45–65.
- **Physical integrity:** compare package, order, and terminal serial numbers, check intact tamper-evident packaging, and inspect the device for missing screws, added wires/labels, holes, or attachments. If any check fails, contact Adyen Support immediately. Passing inspection is an intake check, not a security certification. See **Inspect the terminal**, pinned raw lines 67–82.
- **Network and damage risk:** the dongle's Ethernet LAN port is marked **ETH**; attaching the wrong cable type or using the RS232 port for Ethernet may severely damage the terminal. Wi-Fi can be configured at startup; changing Wi-Fi after boarding uses **Settings > Network** with a passcode. See **Connect to your network**, pinned raw lines 84–120.
- **Diagnostics:** **PSP connection** tests reachability of Adyen's payments platform; **Terminal API** and **Endpoints** are separate POS-system checks. The manual allows a red **Receiving data** cross with **No Error** on the PSP diagnostic while still calling the platform connection successful. A **Successful** diagnostic is a point-in-time connectivity result, not a transaction outcome. See pinned raw lines 122–140.
- **Protected controls:** the manual's Settings menu marks Configuration, Network, Software, and Power as Admin & Settings passcode controls; Transactions and some standalone actions have their own passcode rules. The catalog includes configuration removal, totals reset, and a standalone **Bypass PIN** menu entry. Their presence does not mean an operator should reset data, bypass a cardholder PIN, or that any transaction/account is eligible. From terminal software 1.90, the page says Android and non-Android menus share a structure; earlier versions may retain an older menu. See **Payment terminal menus**, pinned raw lines 161–197.
- After first power-on or long downtime, the manual says configuration/software synchronization can take 10–20 minutes. Reboot uses **Settings > Power** and a passcode; unplugging power turns the M400 off. See **Turn on/off**, pinned raw lines 142–159.

## Detail locators

- **M400 user manual** (pinned raw lines 15–43) — discontinuation, repair date, alternative models, keys, and supplied parts.
- **Get started** (pinned raw lines 45–65) — dongle, power, network, store boarding and separate diagnostics.
- **Inspect the terminal** (pinned raw lines 67–82) — tamper/serial verification and failed-check escalation.
- **Connect to your network** (pinned raw lines 84–120) — Ethernet-port damage warning, Wi-Fi setup, and boarded-device passcode.
- **Test the payments platform connection / Test the POS system connection** (pinned raw lines 122–140) — PSP, Terminal API and Endpoints diagnostic results.
- **Turn on/off / Payment terminal menus** (pinned raw lines 142–197) — power, synchronization, passcode boundaries and menu software qualifier.
- **Device info / Troubleshooting** (pinned raw lines 199–225) — identification and support inputs.

## Related

- [[adyen-payment-terminals]] — primary physical-device concept route.
- [[adyen-terminal-management]] — store and fleet administration.
- [[adyen-terminal-api]] — separate POS messaging context.

## Related raw API references

These linked guides are navigation, not behavioral evidence read for this entry:

- M450 manual — https://docs.adyen.com/point-of-sale/user-manuals/m450-user-manual
- SFO1 manual — https://docs.adyen.com/point-of-sale/user-manuals/sfo1-user-manual
- Passcode management — https://docs.adyen.com/point-of-sale/menu-access
- Connection tests — https://docs.adyen.com/point-of-sale/pos-troubleshooting/connection-tests

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/m400-user-manual/2026-09-15|Adyen M400 user manual, fetched 2026-09-15]]
