---
title: "Adyen M450 payment terminal user manual"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/m450-user-manual"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/m450-user-manual/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminal, m450, hardware, security]
---

## Overview

Adyen's M450 user manual covers physical inspection, first setup and store confirmation, Ethernet/Wi-Fi, connection diagnostics, power, on-device menus and troubleshooting for the M450 **payment terminal**. It also warns that a nearby electronic security tag deactivator can freeze the terminal or affect its NFC reader. The page was captured 2026-09-15 and carries older source metadata; it does not establish current regional availability, account eligibility, certification, boarding or successful payment. [[adyen]] [[adyen-payment-terminals]] [[adyen-android-terminals]]

## Key takeaways

- The listed package contains an M450 with a region-specific power plug or PoE dongle; Ethernet accessories depend on the ordered package. The first-use sequence says to inspect the device, connect power, let its battery charge at least four hours, select a language, connect to a network and confirm or edit the displayed store. If **Confirm store** does not appear, wait for the next Adyen-platform synchronization (on average three hours) and retry. On first start or after a long power-off, a configuration/software maintenance call may take 10–20 minutes. See `### Supplied components`, `## Get started`, and `## Turn on/off`.
- Before use, inspect tamper-evident packing tape, match the order/box/device serial numbers where Customer Area access is available, and inspect for missing screws, added wires or labels, holes and attachments. If any check fails, contact Adyen Support immediately. Keep M450 at least **30.5 cm (12 inches)** from an electronic security tag deactivator, which the manual says can interfere and freeze the terminal; it repeats this check for a freeze or failed NFC reader. See `## Inspect the terminal`, `## Position the terminal`, and `## Troubleshooting`.
- Network choices are Ethernet LAN through the appropriate cube, gigabit-switch or PoE-splitter dongle, or Wi-Fi. The PoE splitter receives power through Ethernet; later Wi-Fi changes use passcode-protected **Settings > Network**. The manual's PSP diagnostic checks platform connectivity, while separate **Terminal API** and **Endpoints** diagnostics check the POS system route and four URLs. A **Successful** result is a point-in-time connection test, not evidence of authorization, settlement or continuing connectivity. See `## Connect to your network`, `## Test the payments platform connection`, and `## Test the POS system connection`.
- This M450 guide says to connect power to turn on, use protected **Settings > Power > Restart** to reboot, and disconnect the power supply to turn off. Its setup text also says to charge the battery for four hours; the page does not give a battery-removal or storage procedure. See `## Get started` and `## Turn on/off`.
- **Settings** exposes device info, diagnostics and display without a passcode; Apps, Configuration, Network, software-version controls and Power require Admin & Settings. **Transactions** History, Totals and New transaction require a Transactions passcode; **New transaction > Refund** needs a Refunds passcode. The **Payment** button starts a normal payment in standalone use without a passcode. Device info shows model, serial/IP, software/configuration, merchant account and store. See `## Payment terminal menus` and `## Device info`.
- Remote troubleshooting requires the operator to select **Start session** and enter a passcode before company staff or Adyen Support can see and interact with the screen. The duplicated freeze/NFC-deactivator warning in Troubleshooting does not describe a separate failure mode. See `## Troubleshooting`.

## Detail locators

- `### Supplied components`–`## Position the terminal`: package-dependent power/network accessories, first boarding, serial/tamper checks and 30.5 cm placement.
- `## Connect to your network`: Ethernet dongle/PoE details, Wi-Fi setup and protected later changes.
- `## Test the payments platform connection` and `## Test the POS system connection`: exact PSP, Terminal API and Endpoints diagnostic screens and their success interpretation.
- `## Turn on/off`–`## Device info`: M450-specific power directions, menu/passcode matrix, standalone Payment button and device identity fields.
- `## Troubleshooting`: NFC/freezing placement check and operator-mediated remote assistance.

## Related

- [[adyen-payment-terminals]] — physical-terminal model manuals and safety.
- [[adyen-android-terminals]] — on-terminal menus, apps and terminal operating context.
- [[adyen-terminal-api]] — POS-system message integration and connectivity route.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/m450-user-manual/2026-09-15|Adyen M450 user manual, fetched 2026-09-15]]
