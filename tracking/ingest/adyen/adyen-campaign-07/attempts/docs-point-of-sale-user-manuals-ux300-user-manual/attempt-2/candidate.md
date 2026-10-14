---
title: "Adyen UX300 unattended terminal user manual"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/user-manuals/ux300-user-manual"
raw_files:
  - "adyen/docs/point-of-sale/user-manuals/ux300-user-manual/2026-09-15.md"
tags: [adyen, point-of-sale, unattended, payment-terminal, ux300, hardware]
---

## Overview

This dated manual covers installation and operation of the Adyen UX300 unattended in-person terminal for kiosks, vending machines, ticket machines and other self-service equipment. The terminal consists of a UX300 card reader, UX100 PIN pad/display and UX400 NFC reader mounted in the machine. It is a three-device physical terminal, separate from a mobile POS card reader or an app installed on an Android payment terminal. See [[adyen]], [[adyen-payment-terminals]] and [[adyen-terminal-management]].

## Key takeaways

- The captured page says UX300 is discontinued for new orders except in the US and Canada, that Adyen repairs existing UX300 terminals until April 2029, and that S1U2 is its recommended alternative. These are statements in a 2026-09-15 snapshot of a page last modified in 2019, not confirmation of current ordering or repair policy.
- The three units have separate mounting/cutout dimensions; the self-service machine and Verifone installation instructions govern mounting. The guide says a drain tube and grounding cables or harness may also be needed. For ordering, the captured page says to select the UX300 model in Customer Area; for store assignment before boarding, use the UX300 card reader serial number. All three devices were described as included in the UX300 delivery at the time of the page.
- Assign this unattended terminal to the intended store **before boarding**; it boards to retrieve that store's configuration. Obtain the anti-removal switch (ARS) password from Adyen, inspect the shipment and each device for tampering, then mount, cable, reset ARS, configure the network if needed, board to the displayed store, and update software. A failed packaging, serial/delivery or device-tamper check calls for immediate Adyen Support contact.
- Cable topology matters: regular Ethernet only goes to the UX300 card reader's ETH (LAN) port; another cable or port such as RS232 can severely damage it. The UX400 NFC reader uses separate RF antenna and COMM RJ-45 cables; the UX100 PIN pad uses powered USB-1 with a USB Type A-B cable; power uses DC-in.
- Mounting triggers ARS and takes the terminal out of service. The UX100 PIN pad prompts for the Adyen-provided ARS password for Switch 1 and Switch 2. If ARS triggers **after boarding**, the display may not say Out of Service and a transaction may start, but PIN entry is prevented so it cannot complete; use the manual's service-switch/UX100 reset sequence. Do not treat this setup procedure as a substitute for investigating a failed tamper inspection.
- DHCP is enabled by default. If no DHCP server can be used, the UX100 Admin menu can disable DHCP and set static Ethernet information. Boarding requires prior store assignment and confirmation of the displayed store. Software update through the Admin menu downloads and installs software, then reboots the terminal. The Admin PIN gates network, software, configuration and transaction menus; the page directs unknown-PIN cases to POS troubleshooting.
- The Admin menu's **Test PSP connection** checks whether the terminal can establish a connection to Adyen's platform at test time. The manual's final ready-to-accept-payments statement follows the setup sequence, but neither it nor the diagnostic establishes actual authorization or settlement.

## Detail locators

- Opening notice and `## Supplied components`: dated availability/repair notice, three-device identity, physical and cutout dimensions.
- `## Get started`, `## Assign the terminal`, `## Inspect the terminal`: ordered setup, ARS password source, mandatory pre-boarding store assignment and tamper checks.
- `## Mount the UX devices`, `## Connect the cables`: external mounting instructions and exact ETH/RF/COMM/USB-1/DC-in connections.
- `## Reset the anti-removal switches`, `### Resetting anti-removal switches after boarding`: initial and post-boarding ARS symptoms and password-controlled reset.
- `## (Optional) Use a static IP address`, `## Board the terminal`, `## Update the terminal software`, `## Settings and transactions`: DHCP, UX100 Admin PIN, store confirmation, reboot and menu functions.

## Related

- [[adyen-payment-terminals]] — model-specific physical terminal manuals.
- [[adyen-terminal-management]] — store assignment and fleet administration.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/user-manuals/ux300-user-manual/2026-09-15|Adyen UX300 user manual, captured 2026-09-15]]
