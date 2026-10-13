---
title: "Adyen Docs: V400m Bluetooth base station troubleshooting"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/design-your-integration/network-and-connectivity/bt-base-station"
raw_files:
  - "adyen/docs/point-of-sale/design-your-integration/network-and-connectivity/bt-base-station/2026-09-15.md"
tags: [adyen, point-of-sale, v400m, bluetooth-base-station, connectivity]
---

## Overview

This Adyen troubleshooting page covers a V400m payment terminal paired by Bluetooth with a compatible base station that has an Ethernet uplink. It diagnoses Bluetooth discovery, pairing, Ethernet-port placement, DHCP/IP assignment, and connection errors for a Terminal API setup. It is specific to the V400m/base-station combination; it does not establish support for other terminal models, a Terminal API local-versus-cloud message path, software-version compatibility, or a successful payment.

## Key takeaways

- The base station connects to Ethernet and the V400m connects to the base by Bluetooth. In this setup the terminal uses that Ethernet connection whether docked or undocked. The page points to the V400m manual for pairing and says to change the base station's default credentials before live transactions; the manual's detailed steps are a linked route, not evidence read here. See **Bluetooth base station**.
- Prevent signal interference by keeping the base out of enclosed drawers and at least 20 inches from a Wi-Fi access point, phone, or radio. Wait for the steady white top LED before using the base; the blue middle LED indicates Bluetooth state. Connect the RJ-45 cable to the Ethernet port, not the Serial port. See **Location**, **Is the Bluetooth base station powered up?**, and **Is the Ethernet cable connected to the correct port?**.
- Press the base's front button to make it discoverable and match the serial number displayed on the terminal with the base's printed number during pairing. For *No devices found/available*, check discovery, disable terminal Wi-Fi, cycle Bluetooth, then restart the terminal/base if needed. See **Is the Bluetooth base station discoverable?** and **No devices found/available**.
- *Connection error* means pairing succeeded but a network connection did not. Check terminal DHCP under Bluetooth IP settings, verify the base's Ethernet port, and restart the base. A paired terminal without a Bluetooth IP address also needs DHCP; the page then directs a PSP connection diagnostic. Default DHCP gives dynamic terminal/base addresses, but a network may require static assignment. See **Connection error** and **Terminal doesn't have a Bluetooth IP address**.
- Restart instructions are specific to this base: disconnect power and Ethernet, wait 10 seconds, reconnect power until the white LED is steady, then reconnect Ethernet to the correct port. See **Restart the base station**.

## Detail locators

- **Bluetooth base station** — V400m/Ethernet/Bluetooth topology and V400m-manual routes for pairing and changing default credentials before live use.
- **Requirements** — Terminal API integration and V400m-compatible base hardware.
- **Location of the Bluetooth base station** — interference placement guidance.
- **Is the Bluetooth base station powered up?** — white and blue LED interpretation.
- **Is the Ethernet cable connected to the correct port?** — RJ-45 Ethernet versus Serial port.
- **Is the Bluetooth base station discoverable?** — front-button discovery and serial-number match.
- **No devices found/available** — Wi-Fi/Bluetooth toggles and terminal/base restart sequence.
- **Connection error** and **Terminal doesn't have a Bluetooth IP address** — pairing versus network distinction, DHCP, PSP diagnostic, and static-IP navigation.
- **Restart the base station** — power/Ethernet restart order.

## Related

- [[adyen]]
- [[adyen-terminal-api]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/design-your-integration/network-and-connectivity/bt-base-station/2026-09-15|Adyen Docs — Bluetooth base station (2026-09-15)]]
