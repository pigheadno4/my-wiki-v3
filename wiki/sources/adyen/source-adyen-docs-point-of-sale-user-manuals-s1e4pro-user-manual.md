---
title: "S1E4Pro user manual | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/s1e4pro-user-manual"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/s1e4pro-user-manual/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, android-terminals, s1e4pro]
---

## Overview

This Adyen S1E4Pro physical-terminal manual, captured 2026-09-15, covers first inspection, charging, Wi-Fi or cellular connection, store confirmation, passcode-controlled menus, battery and USB-C care, and device modes. The companion [[adyen-android-terminals]] overview identifies S1E4Pro as an Android payment-terminal model in its dated table. This manual is setup and operating guidance, not proof of current model availability, account enablement, a live device state, or payment success. See [[adyen]] and [[adyen-payment-terminals]].

## Key takeaways

- The first-use sequence is tamper inspection, power-on with at least four hours of battery charging, language selection, network connection, then confirmation of the displayed store; edit the store if it is wrong. If the store screen is absent, the manual says to wait for the next Adyen synchronization (on average three hours) and retry. This is the on-device store-confirmation step, not evidence of completed fleet assignment for any specific terminal.
- Because the device handles card data, inspect the sealed shipment and tamper tape, compare box and terminal serial numbers and, if accessible, Customer Area order/delivery details, and inspect for physical alterations. Contact Adyen Support immediately if any check fails. The manual does not establish that a particular device passed those checks.
- Wi-Fi setup uses the Welcome flow; later Wi-Fi changes require a passcode under Settings > Network. The manual describes cellular 3G/4G failover and an eSIM, but warns that terminals boarded before 2022 may have an inactive SIM if no subscription was arranged. Its first-use or long-idle software/configuration maintenance call may take 10–20 minutes.
- Use the Adyen-supplied USB-C charging cable and avoid bending, side-loading, excessive force, or foreign objects in its socket. Battery storage guidance includes periodic leakage/swelling checks. Dispose of a faulty battery under local regulations; **do not include it in a returned terminal package** because of leakage and thermal-discharge risk.
- The Settings menu gives Device info, Diagnostics and Display without a passcode, while Apps, Configuration, Network, Software version and Power have an Admin & Settings passcode boundary. The Apps entry says a scheduled app installation/removal is carried out when that menu is opened, so merely opening it can trigger a planned device action. Transactions History, Totals and New transaction require a Transactions passcode; Refund has an additional Refunds passcode. The menu's standalone payment entries are conditional on standalone use and do not alone prove this model is enabled or eligible for that solution.
- Totals reset starts a new reporting period and the previous period's report remains accessible. Kiosk mode hides navigation and Settings/Transactions buttons for unattended use; the manual routes enablement details to another guide. Airplane mode is described for the airline industry and requires Adyen Support enablement before its Network menu option appears; turning it on disables Wi-Fi, Bluetooth and cellular connections, and turning it off restores the previous connections as described. A remote troubleshooting session requires the operator to select Start session and enter a passcode, after which support staff can see and interact with the terminal screen.

## Detail locators

- `S1E4Pro user manual` and `Supplied components`, lines 15–28: model identity, hand strap, charging equipment and eSIM.
- `Get started`, lines 30–47: inspection, charge, language, network and store confirmation/synchronization sequence.
- `Inspect the terminal`, lines 49–64: tamper, serial/order checks and immediate Support escalation.
- `Connect to your network`, lines 66–99: Wi-Fi setup, later passcode and pre-2022 cellular/SIM qualification.
- `Turn on/off` and `Maintain battery performance`, lines 101–137: maintenance call, power and faulty-battery return warning.
- `Use the USB-C charging cable`, lines 139–152: Adyen cable requirement and connector-care details.
- `Payment terminal menus` and `Device info`, lines 154–205: Apps-on-open action, credential boundaries, conditional standalone menu and current-device information route.
- `View and reset totals`, lines 207–226: reporting period reset and previous-report access.
- `Kiosk mode`, lines 228–232; `Airplane mode`, lines 234–258: UI restrictions versus network shutdown and Support enablement.
- `Troubleshooting`, lines 260–274: remote screen-interaction session and support-identification fields.

## Related

- [[adyen-payment-terminals]] — physical payment-terminal setup and upkeep.
- [[adyen-android-terminals]] — Android model and on-terminal app context.
- [[adyen-terminal-management]] — fleet assignment and configuration.
- [[adyen-terminal-api]] — POS integration message context.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/s1e4pro-user-manual/2026-09-15|S1E4Pro user manual (2026-09-15 snapshot)]]
