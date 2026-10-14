---
title: "S1E and S1E Barcode payment terminal user manual"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/s1e-user-manual"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/s1e-user-manual/2026-09-15.md"
tags: [adyen, point-of-sale, android-terminals, s1e, hardware, user-manual]
---

## Overview

Adyen's S1E user manual, captured 2026-09-15, covers initial inspection, charging, networking, store confirmation, menus and maintenance for the S1E and S1E Barcode payment terminals. The Barcode variant has a scanning camera and larger battery. This is a dated device-operating guide, not evidence of current regional availability, production eligibility or a successful payment. [[adyen]] [[adyen-android-terminals]]

## Key takeaways

- Inspect the shipment and terminal before use because the device processes sensitive card data: verify unopened security tape, match the box and terminal serial numbers (and Customer Area order when accessible), and look for signs of tampering. If any check fails, contact Adyen Support immediately. See `## Inspect the terminal` in the pinned raw.
- Initial setup connects power, starts the terminal, selects a language, connects a network and confirms the correct store on the terminal. The manual says to charge for at least four hours; if the store screen is absent, wait for the next Adyen-platform synchronization (described as three hours on average) and retry. The manual's "ready to process payments" statement follows these steps and does not prove a particular account or transaction is ready. See `## Get started`.
- The S1E/S1E Barcode manual describes Wi-Fi and cellular 3G/4G failover, with a caveat that the SIM may be inactive on terminals boarded before 2022 without a SIM subscription at the time. It also gives physical SIM replacement steps and warns against metal tools in the slot. This dated connectivity description does not establish current carrier coverage or SIM status. See `## Connect to your network`.
- Storage outside the advised battery range can degrade or permanently damage the battery. Inspect for leakage or swelling every six months; dispose of a faulty battery under local rules and do not include it in a terminal return because of leakage and thermal-discharge risk. Use the Adyen-supplied USB-C cable and regional power plug, and inspect the cable/socket for foreign objects. See `### Maintain battery performance` and `## Use the USB-C charging cable`.
- Settings **Apps** shows installed apps/certificates and carries out a pending install/removal when opened; it requires the Admin & Settings passcode. The Payment button starts a normal payment only in standalone use. The Totals reset starts a new reporting period; kiosk mode has separate enablement instructions, and airplane mode needs Adyen Support enablement before its Network-menu toggle is available. See `## Payment terminal menus`, `## View and reset totals`, `## Kiosk mode`, and `## Airplane mode`.

## Detail locators

- `## Turn on/off`: first-start or long-off maintenance synchronization/software update may take 10–20 minutes; battery-charge and power-button instructions.
- `## Payment terminal menus` and `## Device info`: menu/passcode matrix and model, serial, software, configuration, merchant-account and boarded-store fields.
- `## Troubleshooting`: self-service route and a support remote session that requires the operator to select Start session and enter a passcode; support-identification fields are listed there.
- `## View and reset totals`: on-device sales, refunds, tip and cancellation totals since last reset, previous period access, and a Support route for automatic daily reset.

## Related

- [[adyen-android-terminals]] — Android payment terminal scope and app routes; this manual provides S1E-specific handling.
- [[adyen-terminal-api]] — separate integrated payment-message route; this manual also describes standalone operation.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/s1e-user-manual/2026-09-15|Adyen S1E user manual, fetched 2026-09-15]]
