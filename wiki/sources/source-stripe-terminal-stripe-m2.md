---
title: "Stripe Terminal: Stripe Reader M2"
type: source
date_ingested: 2026-05-01
original_format: webpage
raw_files:
  - "stripe-terminal-stripe-m2-2025.md"
tags: [stripe, stripe-terminal, m2, mobile-readers, firmware, bluetooth]
---

## Summary

Detailed reference for the Stripe Reader M2 — small screenless reader for US only. BLE or USB (Android only). iOS/Android/React Native SDKs. LED status indicators.

## Key Details

**Latest version**: `2.01.01.00-SZZZ_Prod_US_v12-480001` (2026-02-11)

**Software version format**: `{firmware}-{config}-{key_identifier}` (hyphens, unlike WisePad 3 which uses underscores).

**Power button** (updated in 2.01.01.00): hold 4s to power off; hold 14s to reset.

**NFC UID collectData**: added in `2.01.00.31` (2025-04-30).

**LED states**: 4 LEDs for battery (full/75%/50%/25%/charging); 6 connectivity states including tampered (flashing 0.1s/30s) and integrity check failed (30s solid).

**Key identifier**: `480001` (single identifier for US).

**Accessories**: dock (countertop) + mount (roaming) available; mechanical design files under license.

**PCI note**: firmware ID `ABCDD` = `AA.BB.CC.DD` (e.g., `CHB3x.01-21021` = `2.01.00.21`).

## Raw Sources

- [[stripe-terminal-stripe-m2-2025]] — verbatim webpage content (LED tables, firmware changelog, configurations)
