---
title: "Stripe Terminal: Stripe Reader M2"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/terminal/readers/stripe-m2"
raw_files:
  - "stripe-terminal-readers-stripe-m2-2026-11-07.md"
  - "stripe-terminal-stripe-m2-2025.md"
tags: [stripe, stripe-terminal, m2, mobile-readers, firmware, bluetooth]
---

## Summary

[[stripe]]'s [[stripe-terminal|Terminal]] reader reference lists the Stripe Reader M2 for the US. This screenless mobile reader connects to the iOS, Android, or React Native Terminal SDK via Bluetooth Low Energy, with USB limited to Android. See the separate [[source-stripe-terminal-setup-reader-m2|setup guide]] for setup, charging, and regional detail.

## Software Versions

The software version contains the firmware version, configuration name, and key identifier. The captures report these exact strings in the field labeled **Latest Version**.

| Capture date | Listed software string |
| --- | --- |
| 2026-05-01 | `2.01.01.00-SZZZ_Prod_US_v12-480001` |
| 2026-11-07 | `2.01.04.00-SZZZ_Prod_US_v12-481001` |

> [!note] November software field, firmware changelog, and key history
> The November software field contains firmware `2.01.04.00` and key token `481001`. The newest dated firmware changelog entry is `2.01.07.01` (2026-10-21). The separate key table in both captures lists only the initial identifier `480001`, dated 2021-07-01. The captures leave rollout, installed versions, and use of `481001` beyond the software field unresolved.

> [!note] Software string separators in both captures
> The prose describes underscore separators. Both listed strings use hyphens between the three components and underscores within the configuration token. The general format remains unresolved.

The configuration history in both captures lists `SZZZ_Prod_US_v12` (2025-04-30) and earlier production and test entries. The guides route to `deviceSoftwareVersion` on iOS and `softwareVersion` on Android.

**PCI note**. The firmware ID suffix `ABCDD` maps to `AA.BB.CC.DD`. The published example `CHB3x.01-21021` maps to `2.01.00.21`.

## Firmware Changelog

| Firmware | Release date | Documented change |
| --- | --- | --- |
| `2.01.07.01` | 2026-10-21 | General bug fixes and improvements |
| `2.01.06.00` | 2026-09-08 | General bug fixes and improvements |
| `2.01.05.00` | 2026-08-03 | General bug fixes and improvements |
| `2.01.04.00` | 2026-06-30 | General bug fixes and improvements |
| `2.01.01.00` | 2026-02-11 | Hold the power button for four seconds and release to power off, or hold for 14 seconds and release to reset |
| `2.01.00.38` | 2025-09-10 | Updated the LEDs to scan while awaiting a Bluetooth or USB connection and reliably clear when connected |
| `2.01.00.31` | 2025-04-30 | Added an NFC UID configuration to `Terminal.collectData` for reading an NFC instrument's UID |

## LED Status

On a powered reader, press and release the power button once to check the battery. The captured table lists full, 75%, 50%, 25%, and flashing while charging. The connection table describes a back-and-forth scan while awaiting Bluetooth or USB, and separate bootloader and standby states. It lists a tamper indication flashing every 0.1 seconds for 30 seconds and a failed integrity check indication lasting 30 seconds. The captured icon cells are blank.

> [!note] Bluetooth connection flashes
> The May 1 and November 7, 2026 firmware-reference tables describe three flashes for a Bluetooth or USB connection. The April 24 and November 7, 2026 [[source-stripe-terminal-setup-reader-m2|setup guides]] describe four flashes when the reader connects over Bluetooth to the app device, then the first LED flashes every five seconds. The documents leave the overlapping Bluetooth count unresolved.

## Accessories

The reference lists an optional dock for countertop checkout and a mount for roaming checkout. Stripe requires reviewing and accepting the Terminal Design File License Agreement before downloading mechanical design files (.STP). Downloading indicates agreement to the license.

## Raw Sources

- [[raw/stripe-terminal-readers-stripe-m2-2026-11-07|2026-11-07 reader reference]]
- [[raw/stripe-terminal-stripe-m2-2025|2026-05-01 reader reference]]
