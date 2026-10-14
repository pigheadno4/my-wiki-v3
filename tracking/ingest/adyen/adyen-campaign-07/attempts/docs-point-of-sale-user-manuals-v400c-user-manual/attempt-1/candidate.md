---
title: "V400c Plus user manual | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/v400c-user-manual"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/v400c-user-manual/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, v400c-plus, hardware]
---

## Overview

Adyen's V400c Plus physical-terminal manual, captured 2026-09-15, covers inspection, receipt-paper and power setup, Ethernet/Wi-Fi connection, store boarding, point-in-time connectivity diagnostics, menus, totals and receipts. Its captured discontinuation notice says V400c Plus is unavailable for new orders, existing-device repairs continue until April 2029, and P630 is the suggested replacement. These are dated statements, not proof of present ordering, repair eligibility, device support, certification or successful payment execution. See [[adyen]], [[adyen-payment-terminals]], and [[adyen-terminal-management]].

## Key takeaways

- Before use, inspect the unopened shipping box and intact tamper tape; compare box and terminal serial numbers, and, if Customer Area access is available, compare the order's serial number and carrier delivery record. Inspect the device for missing screws, extra wires or labels, holes, or attached/inserted items. Adyen says to contact Support immediately if any check fails.
- Initial setup inserts a 57 × 40 mm receipt-paper roll, connects the supplied dongle at the terminal's rear, powers the unit from its supply, configures Ethernet LAN or Wi-Fi, then uses **Board the terminal** to choose and confirm a store. The guide says boarding can take up to 30 minutes; if the option is absent, wait for the next Adyen synchronization (average three hours in this snapshot). A setup instruction is not evidence that a particular device is assigned, boarded or ready to accept payments.
- Ethernet uses the dongle's **ETH** port. The guide warns that wrong cable/port choices, including the RS232 port, may severely damage the terminal. After boarding, Wi-Fi changes use **Settings > Network** and a passcode. First power-on or power-on after a long outage may trigger maintenance/configuration/software synchronization lasting 10–20 minutes; power-on uses the supply, reboot uses protected **Settings > Power**, and power-off disconnects the supply.
- The **PSP connection** diagnostic checks connection to Adyen's platform. For POS-integrated use, separate **Terminal API** and four-URL **Endpoints** diagnostics check the POS path; standalone use skips that POS-system test. A displayed **Successful** is a result at test time, not proof of sustained connectivity, payment authorization or settlement. Device info exposes model, serial, IP, software/configuration versions, merchant account and store for diagnosis.
- The captured menu table says Settings network/software/configuration/power need Admin & Settings passcode, while Transactions history/totals and standalone special payments use the Transactions passcode; standalone Refund or MOTO refund can require Refunds passcode. Those menu labels do not establish feature enablement. A **Totals** reset starts a new reporting period and previous-period totals are no longer shown as current; automatic daily reset requires Support. The manual also gives receipt reprint steps. It notes common Android/non-Android menu structure from software 1.90, with older non-Android menus possible.

## Detail locators

- Discontinuation notice and supplied components: raw lines 15–43; [[raw/adyen/docs/point-of-sale/user-manuals/v400c-user-manual/2026-09-15#Get started|Get started]] gives the initial sequence.
- Shipment/device tamper checks and Support escalation: [[raw/adyen/docs/point-of-sale/user-manuals/v400c-user-manual/2026-09-15#Inspect the terminal|Inspect the terminal]] (raw lines 69–84).
- Paper, dongle Ethernet/RS232 damage warning, Wi-Fi and post-boarding passcode: raw lines 86–128 under **Insert the receipt paper roll** and **Connect to your network**.
- PSP, Terminal API and Endpoints diagnostics: raw lines 130–148; [[raw/adyen/docs/point-of-sale/user-manuals/v400c-user-manual/2026-09-15#Turn on/off|Turn on/off]] for maintenance and power effects.
- Menus and passcodes, Device info, Totals reset and receipt reprint: raw lines 169–252. The separate menu-access and standalone guides linked there remain navigation for detailed eligibility and passcode administration.

## Related

- [[adyen-payment-terminals]] — physical-terminal model and safety hub.
- [[adyen-terminal-management]] — assignment, boarding and fleet configuration.
- [[adyen-standalone-terminals]] — separately documented terminal-initiated transaction scope.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/v400c-user-manual/2026-09-15|Adyen V400c Plus user manual, 2026-09-15 snapshot]]
