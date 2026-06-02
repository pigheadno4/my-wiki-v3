---
title: "Stripe Terminal: BBPOS WisePOS E"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-bbpos-wisepos-e-2025.md"
tags: [stripe, stripe-terminal, wisepos-e, smart-readers, firmware, countertop]
---

## Summary

Detailed reference for the BBPOS WisePOS E — countertop smart reader. 24 countries (no JP). Internet connection. All 5 SDKs + server-driven (server-driven recommended). 4-component software (same structure as S700/S710).

## Key Details vs S700/S710

**Firmware**: `5.01.03.00` (AU has `.eftpos` suffix). PCI format: `WSC5x.11-WXYZZ-ABCDD`.

**ROM**: `1.8.4` (vs S700/S710's `2.2.22`).

**Latest reader app**: `2.41.2.0` (shared with S700/S710).

**Payment sounds**: tap success AND failure both = 1 long high-pitched beep (unlike S700/S710 where success/failure differ).

**Power on**: hold power button 2 seconds.

**Ethernet dock**: both cables must be connected before inserting reader into dock.

**Configurations by region**:

| Region | Config |
| --- | --- |
| US | `szzz_us_v19` |
| CA | `szzz_ca_v17` |
| AU | `szzz_prod_au_v11` |
| MY/NZ | `szzz_prod_apac_on_v4` |
| SG | `szzz_prod_apac_off_v4` |
| GB/IE/FI | `szzz_prod_eu_off_v11` |
| AT/BE/DK/FR/IT/DE/NL/ES/SE/CZ/LU/PT/CH/NO | `szzz_prod_eu_on_v7` |

**LED states**: left array = battery/charging; right array = reader status (bootloader, integrity fail, hard fault).

## Raw Sources

- [[stripe-terminal-bbpos-wisepos-e-2025]] — verbatim webpage content (LED tables, sounds, diagnostics, full changelog, firmware versions)
