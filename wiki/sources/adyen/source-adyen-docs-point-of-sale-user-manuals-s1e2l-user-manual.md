---
title: "Adyen S1E2L payment terminal user manual"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/s1e2l-user-manual"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/s1e2l-user-manual/2026-09-15.md"
tags: [adyen, point-of-sale, android-terminals, s1e2l, user-manual]
---

## Overview

Adyen's S1E2L manual describes inspection, first boarding to a store, Wi-Fi/cellular connection, battery and cable care, terminal menus, totals, and troubleshooting for this payment-terminal model. This is a device-operation snapshot fetched 2026-09-15 (raw metadata last modified 2024-12-16), not current model/market availability, Android OS or firmware certification, merchant enablement, terminal security attestation, or payment-success proof. The separate Adyen Android-terminals overview lists S1E2L in its dated model table. [[adyen]] · [[adyen-android-terminals]]

## Key takeaways

- **Inspect and board:** Before use, check the shipping seal, matching box/terminal serial numbers and any accessible Customer Area order, and signs of tampering. If a check fails, contact Adyen Support immediately. First setup powers and charges the terminal, selects language and network, then confirms the displayed store; if the store screen does not appear, the manual says wait for the next platform synchronization (on average three hours) and try again. This is a setup sequence, not proof that a specific terminal has boarded or processed a payment.
- **Network and failover:** The terminal needs internet access to communicate with Adyen and the merchant back end. Wi-Fi setup and later passcode-protected Network settings are described. The page says S1E2L can switch to cellular when internet fails and that Adyen terminals have preinstalled activated eSIMs, but notes terminals boarded before 2022 might lack SIM activation if the merchant had no SIM subscription then; contact Support when unsure. A cellular path does not establish connectivity or payment outcome for a particular device/outage.
- **Power and return hazard:** Initial setup asks for at least four hours' charging. Long storage can permanently degrade the battery; the manual gives storage/inspection guidelines. For battery failure it links a return/replace route and says to dispose of a faulty battery under local rules and **not put that battery in the terminal return package**, due to leakage and thermal-discharge risk. Use the supplied USB-C cable and region-specific plug. The manual does not establish that every model has an orderable spare battery or define the full return process.
- **Menus and access:** Settings, Transactions and Payment menus expose different actions. Device info, diagnostics and display are listed without a passcode; Network, Configuration, Apps, software-version and Power actions need the Admin & Settings passcode. Transactions history/totals/new-transaction actions need the Transactions passcode, and a new refund additionally needs the Refunds passcode. The standalone Payment button is listed without a passcode. These are staff-menu gates, not a claim about shopper PIN support or eligibility of MOTO, MKE, refunds or standalone operation for a particular account.
- **Totals and operating modes:** The terminal's Totals report shows amounts since its last reset; resetting starts a new period, with a previous-period report accessible. This is a terminal operating report, not settlement proof. Kiosk mode is described as hiding navigation/controls for unattended use, with enablement delegated to its guide. Airline airplane mode requires Support enablement; when switched on it turns off Wi-Fi, Bluetooth and cellular, and the manual says previous connections return when turned off.

## Detail locators

- **Components and first setup:** raw lines 15–47, `# S1E2L user manual` and `## Get started`. The supplied plug is region-specific; initial charge is at least four hours.
- **Tamper inspection and escalation:** raw lines 49–64, `## Inspect the terminal`.
- **Wi-Fi, cellular and boarded-before-2022 caveat:** raw lines 66–99, `## Connect to your network`.
- **Power, stored-battery limits, return hazard and USB-C care:** raw lines 101–152, `## Turn on/off`, `### Maintain battery performance`, `## Use the USB-C charging cable`.
- **Menu/passcode matrix and device info:** raw lines 154–205, `## Payment terminal menus` and `## Device info`. Follow the matrix's particular action/passcode rows; it does not document a shopper PIN feature.
- **Totals, kiosk, airplane mode and Support gate:** raw lines 207–258. See `## View and reset totals`, `## Kiosk mode`, `## Airplane mode`.
- **Troubleshooting escalation:** raw lines 260–274. The linked repair/return, battery-management, kiosk, menu-access and troubleshooting guides are navigation from this manual, not authority read for this entry.

## Related

- [[adyen-android-terminals]] — dated Android-terminal model catalog and app boundary
- [[adyen-terminal-management]] — separate fleet administration and return/order routes
- [[adyen-standalone-terminals]] — solution path mentioned by the Payment menu, subject to separate standalone eligibility

## Related raw API references

The linked return/replace, battery management, kiosk, network and menu-access guides were not read for this entry. Their procedures and current support conditions require those sources.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/s1e2l-user-manual/2026-09-15|S1E2L user manual, fetched 2026-09-15]]
