---
title: "Adyen e280 payment terminal user manual"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/e280-user-manual"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/e280-user-manual/2026-09-15.md"
tags: [adyen, point-of-sale, payment-terminals, e280, hardware]
---

## Overview

Adyen's e280 user manual, captured 2026-09-15, describes inspection, charging, Wi-Fi setup, store boarding, connection diagnostics, battery care, menus and support for this physical payment terminal. The page marks e280 **discontinued and unavailable for new orders** and recommends AMS1 instead. This model-specific [[adyen-payment-terminals]] guide is distinct from merchant-phone [[adyen-mobile-pos]] solutions and mobile card-reader pairing. Its dated operational instructions do not prove current account/device availability, certification status, or payment authorization.

## Key takeaways

- **Inspect before use.** Check the shipping seal, order/box/device serial numbers, carrier delivery confirmation where available, and signs of physical tampering. If any check fails, contact Adyen Support immediately.
- **Power and battery are model-specific.** The manual lists a supplied USB cable but no charger, specifies a 5V DC, 1A charger, and says the e280 battery cannot be replaced. Let it charge for at least four hours during initial setup. Use the Adyen-provided charging cable; improper insertion or strain can damage the USB-C socket. For long storage, the page recommends cool, dry conditions, 40–70% charge, and six-month leakage/swelling checks. A faulty battery must not be packed in the terminal return and should be disposed of under local rules.
- **Board after connecting Wi-Fi.** Select a store when boarding; the page says boarding can take up to 30 minutes. If the Board option is absent, wait for the next platform synchronization (given as an average of three hours) and try again. After boarding, changing Wi-Fi through Settings > Network requires a passcode. After long downtime, maintenance synchronization or software update at startup can take 10–20 minutes.
- **Connection checks are point-in-time diagnostics.** The PSP connection test checks the terminal's Adyen platform link. The Terminal API and Endpoints tests check the POS-system path; the Endpoints test covers four URLs. A successful diagnostic is not proof of payment success or continuing connectivity.
- **Menu and access scope matter.** Settings for Configuration, Network, Software and Power require Admin & Settings passcode, while Device info and Diagnostics do not. Standalone Normal payment, special payment options and refunds have their own stated passcode gates; the manual places the Payment button under a no-passcode row. The described common Android/non-Android menu structure applies from terminal software 1.90; earlier devices may show the old non-Android menu. Totals can be reset from Transactions, so treat that menu action as changing the terminal's totals report.

## Detail locators

- Raw opening and `## Get started` (lines 15–64): discontinued notice, supplied items, charger and nonreplaceable battery, charging, Wi-Fi, boarding and tests.
- Raw `## Inspect the terminal` (lines 66–81): shipment and device tamper checks and immediate Support escalation.
- Raw `## Connect to your network` and diagnostic sections (lines 83–130): Wi-Fi, post-boarding passcode, PSP/Terminal API/Endpoints tests and their status fields.
- Raw `## Turn on/off`, `### Maintain battery performance`, and `## Use the USB-C charging cable` (lines 132–189): startup synchronization, passcode to power off, storage, faulty battery handling and cable care.
- Raw `## Payment terminal menus` and `## Device info` (lines 191–241): passcode table, standalone payment controls, transaction-history and totals actions, software 1.90 menu boundary and device identification fields.
- Raw `## Troubleshooting` (lines 243–255): self-service route and information to supply Adyen Support.

## Related

- [[adyen-payment-terminals]] — physical terminal hardware hub.
- [[adyen-terminal-management]] — fleet ordering, boarding and configuration route.
- [[adyen-terminal-api]] — POS messaging and diagnostics context.
- [[adyen-mobile-pos]] — separate merchant-device payment route.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/e280-user-manual/2026-09-15|e280 user manual, fetched 2026-09-15]]
