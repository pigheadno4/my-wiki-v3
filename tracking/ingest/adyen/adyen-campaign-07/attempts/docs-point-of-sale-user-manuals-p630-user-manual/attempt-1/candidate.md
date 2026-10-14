---
title: "P630 user manual | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/p630-user-manual"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/p630-user-manual/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminal, p630, hardware]
---

## Overview

This dated Adyen manual covers initial setup and operation of the **P630 physical payment terminal**. It describes shipment/tamper inspection, placement, power, Ethernet or Wi-Fi connectivity, on-terminal store confirmation, protected menus, local totals, default kiosk mode, optional airplane mode, and support routes. The page was fetched 2026-09-15 and records a 2025-12-15 last-modified timestamp. It does not establish present regional supply, terminal software version, merchant configuration, network health, or a completed payment. [[adyen]] [[adyen-payment-terminals]] [[adyen-android-terminals]]

## Key takeaways

- Before using a received P630, verify the shipping seal and serial numbers across the box, terminal and (if available) Customer Area order, and inspect for tampering. If any check fails, contact Adyen Support immediately. Keep the terminal at least **30.5 cm (12 inches)** from electronic security tag deactivators; the manual warns they can freeze the terminal. See **Inspect the terminal** and **Position the terminal**, pinned raw lines 52–71.
- Initial setup is inspection and positioning, then power, language, internet connection, and **Confirm store** selection or correction. If the store screen does not appear, the manual says to wait for the next platform synchronization (on average three hours) and try again. A first start or long power-off may trigger a 10–20 minute maintenance call for configuration/software. These are instructions and approximate timing, not evidence that a specific terminal is boarded or payment-ready. See pinned raw lines 32–50 and 73–80.
- The manual offers Ethernet through an Ethernet dongle, PoE dongle or gigabit switch, depending on the supplied setup, or Wi-Fi. PoE supplies power through the Ethernet cable; Wi-Fi changes later require the Network menu and a passcode. The terminal must connect to the internet to communicate with Adyen and the merchant back end. See **Connect to your network**, pinned raw lines 111–152.
- **P630 menu icons are disabled:** Settings opens with keypad 9 then Confirm; Transactions opens with keypad 8 then Confirm. Protected options require the corresponding Admin & Settings, Transactions, or Refunds passcode; the table includes terminal configuration, software, apps, transaction history/totals and standalone transaction options. The manual gives a separate keypad 5 then Confirm route to Device info. Viewing/resetting local Totals uses the Transactions passcode, and resetting starts a new reporting period; these local totals do not establish settlement or reconciliation. See pinned raw lines 154–226.
- Kiosk mode is described as enabled by default on P630. Airplane mode needs Adyen Support enablement before its Network-menu option appears; turning it on disables network connections and turning it off restores previous connections. For a freeze or NFC issue, the troubleshooting section again points to deactivator proximity. See pinned raw lines 232–280.

## Detail locators

- **Supplied components; Get started** (pinned raw lines 26–50) — included terminal/cable/region-specific plug, optional ordered accessories, setup and store-confirmation sequence.
- **Inspect the terminal; Position the terminal** (pinned raw lines 52–71) — security checks, Support escalation, and interference clearance.
- **Turn on/off; Connect to your network** (pinned raw lines 73–152) — maintenance timing, power/reboot paths, Ethernet/PoE variants and Wi-Fi setup.
- **Payment terminal menus; Device info; View and reset totals** (pinned raw lines 154–230) — exact keypad routes, role/passcode matrix, device fields and local reporting-period reset.
- **Kiosk mode; Airplane mode; Troubleshooting** (pinned raw lines 232–280) — model default, Support prerequisite, connection effects and escalation information.

## Related

- [[adyen-payment-terminals]] — primary model-specific physical-terminal route.
- [[adyen-android-terminals]] — Android terminal feature and app context; this manual's hardware/menu claims remain P630-specific.
- [[adyen-terminal-management]] — fleet assignment and configuration context.
- [[adyen-standalone-terminals]] — separate standalone transaction guidance for menu options listed here.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/p630-user-manual/2026-09-15|P630 user manual, fetched 2026-09-15]]
