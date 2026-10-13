---
title: "Adyen Bluetooth PAN and Tethering for POS Terminals"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/design-your-integration/network-and-connectivity/bluetooth-pan"
raw_files:
  - "adyen/docs/point-of-sale/design-your-integration/network-and-connectivity/bluetooth-pan/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, bluetooth-pan, tethering, mobile-pos, connectivity]
---

## Overview

This Adyen webpage guide describes pairing an Android or iOS mobile POS device with a supported Adyen payment terminal over Bluetooth Personal Area Network (PAN). The PAN carries POS-to-terminal requests and terminal-to-POS responses; a separate internet path carries the terminal's online authorization traffic to Adyen. It distinguishes using the terminal's internet connection from tethering through the mobile device. The pinned snapshot was fetched 2026-09-15 and lists `last_modified` 2020-09-22, so its terminal-model, software, 2G/3G and mobile-OS connectivity claims need current confirmation before deployment.

## Key takeaways

- The requirements table says Terminal API with terminal software **1.60 or later** and hardware limited to **e280 and e285p**. The subsequent setup table and instructions instead say **e280 or e285**. Preserve that model-name discrepancy; this snapshot alone does not resolve whether `e285` and `e285p` are interchangeable or establish support for other terminals. It also cautions to check regional 3G availability, citing European 2G/3G shutdowns.
- Pairing forms an ad hoc Bluetooth PAN between terminal and Android/iOS mobile POS. The mobile POS sends a payment request across PAN; the terminal sends it to Adyen for online authorization, displays the result and returns a response across PAN. This guide describes that direct device link and internet forwarding; it does not specify a cloud Terminal API transport, mobile permission API, or Bluetooth security protocol. Verify the matching pairing code on both devices before accepting.
- With **terminal internet access**, the e280 procedure uses terminal Wi-Fi; the e285 procedure allows terminal Wi-Fi and optional 2G/3G SIM fallback. With **mobile-device tethering**, the guide says Android can share its Wi-Fi or cellular connection, while iOS shares cellular. These are configuration alternatives, not guarantees of carrier, OS or hardware support beyond the dated source.
- For tethering, keep the mobile hotspot active despite battery saving or time-outs. After pairing, check that the terminal has an IP address, run the linked PSP connection test, and then initiate a test payment from the mobile POS. An IP address alone is insufficient to establish Adyen reachability or successful payment. The guide says paired devices reconnect automatically on later use; that is a documented behavior in this snapshot, not proof of a particular installation.

## Detail locators

- `## Requirements` — Terminal API, software version, e280/e285p hardware claim and region-dependent legacy cellular caution.
- `## Concepts and setups` — PAN request/response path, terminal-versus-mobile internet alternatives and the table that uses e285 rather than e285p.
- `## Bluetooth PAN using the terminal for internet access` — terminal Wi-Fi/SIM variants, Bluetooth enablement, matching-code pairing and test payment.
- `## Bluetooth tethering using the mobile device for internet access` — Android Wi-Fi/cellular versus iOS cellular sharing, active-hotspot requirement, pairing, IP/PSP connectivity/test-payment checks.
- `## Bluetooth menu on the terminal` and `## See also` — menu animation and navigation to beacons/user manuals; linked pages are navigation only.

## Related

- Company: [[adyen]]
- POS message and architecture context: [[adyen-terminal-api]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/design-your-integration/network-and-connectivity/bluetooth-pan/2026-09-15|2026-09-15 Adyen Bluetooth PAN and tethering snapshot]]
