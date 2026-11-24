---
title: "Stripe Terminal: Stripe Reader S700/S710"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-s700-s710-2025.md"
tags: [stripe, stripe-terminal, s700, s710, smart-readers, firmware, android]
---

## Summary

Detailed reference for the Stripe Reader S700/S710 — Android-based smart reader for countertop and handheld use. Connects via internet/LAN/handoff mode. All 5 SDKs + server-driven.

## Software Components (4)

S700/S710 has 4 software components (vs 3 for mobile readers): reader app, firmware, configuration, key identifier.

**Latest versions** (2026-04-20): reader `2.41.2.0`, firmware `1.00.03.00`, ROM `2.2.22`.

**Configuration by region**:

| Region | Config |
| --- | --- |
| US | `szzz_us_v11` |
| CA | `szzz_ca_v4` |
| AU | `szzz_prod_au_v11` |
| MY/NZ/SG | `szzz_prod_apac_on_v5` |
| GB/IE/FI | `szzz_prod_eu_off_v3` |
| AT/BE/DK/FR/IT/DE/NL/ES/SE/CZ/LU/PT/CH/NO | `szzz_prod_eu_on_v5` |

**PCI firmware format**: `STR7x-11-WXYZZ-ABCDD` → ROM `W.X.Y.ZZ`, firmware `AA.BB.CC.DD.SZZZ.07`.

## Hardware Notes

**Battery**: 5 LED states; requires 12W (USB-A insufficient); slow-charge recovery ≤30 min for deeply discharged; stops charging below 0°C or above 60°C.

**Payment sounds**: tap success = 1 long high beep; tap failure = 2 short low beeps; chip = silent; swipe failure = 2 short beeps.

**Diagnostics**: Settings → admin passcode (07139) → Diagnostics. Tests: DNS resolution, Stripe connectivity, Terminal events connectivity, WiFi info, battery/hardware status.

## Notable Changelog Items

- `2.41.2.0` / `1.00.03.00` (2026-04-20): general fixes
- `2.39.3.0` (2026-02-24): PIN failure UI improved
- `2.38.5.0` (2026-01-13): audio tone volume fix
- `2.33.3.0` / `1.00.00.29` (2025-06-30): girocard + CB cobranded card choice support
- `2.31.6.0` / `1.00.00.25` (2025-04-28/29): NFC UID collectData added; Cartes Bancaires support
- `2.29.6.0` (2025-03-12): offline mode SDI fix; PIN sounds; server-driven poor-network improvements
- `2.28.3.0` (2025-01-29): Doze mode IoT fix; pre-insert card support; handoff mode bug fixes
- `2.22.3.0` (2024-04-18): hidden Enterprise WPA/WPA2-EAP; 50% battery for config/key updates

## Raw Sources

- [[stripe-terminal-s700-s710-2025]] — verbatim webpage content (battery LEDs, sounds, diagnostics, full changelog, firmware table)
