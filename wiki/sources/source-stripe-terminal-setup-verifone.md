---
title: "Stripe Terminal: Set Up Verifone Readers"
type: source
date_ingested: 2026-04-24
original_format: webpage
raw_files:
  - "stripe-terminal-setup-verifone-2025.md"
tags: [stripe, terminal, in-person, card-reader, verifone, hardware, setup, p2pe, preview]
---

## Stripe Terminal: Set Up Verifone Readers

Overview and comparison of the four Verifone readers supported by Stripe Terminal (all in preview).

## Key Takeaways

### Preview status

| Countries | Models available |
| --- | --- |
| US, CA | Public preview — all 4 models (V660p, UX700, P630, M425) |
| GB, IE | Private preview — V660p, UX700, P630 only |
| SG | Private preview — V660p, P630 only |

Must contact Sales to order.

### Model comparison

All 4 models share: Android 13, quad-core Cortex A53, 2GB RAM, 32GB storage, E2EE + P2PE capable (individual PCI listings).

| | V660p | UX700 | P630 | M425 |
| --- | --- | --- | --- | --- |
| Display | 5.5" 1280×720, 580 nit | 5.5" 1280×720, 450 nit | 3.5" 320×480, 350 nit | 3.5" 320×480, 350 nit |
| Battery | Yes — ~10h active (72h standby, 3h charge); initial 8h charge required; don't go below 10% | No | No | No |
| Weight | 456g | 575g | 305g | 470g |
| Charging | USB-C + dock | 4-PIN plug | Verifone Custom | USB-C |
| Connectivity | WiFi, Ethernet (optional dock) | WiFi, Ethernet | WiFi, Ethernet (dongle) | WiFi, Ethernet (dongle) |
| Audio jack | Yes | Yes | No | Yes |
| Camera | Front + rear (not supported) | Front + facial scanner (not supported) | Downward barcode scanner (not supported) | Front (not supported) |

### Key differentiators

- **V660p**: only model with battery (mobile use); brightest display (580 nit)
- **UX700**: heaviest (575g); no battery but built-in Ethernet; 4-PIN proprietary charging
- **P630**: lightest at 305g; Verifone Custom charging; requires dongle for Ethernet; no audio jack
- **M425**: tablet form factor (179×170mm, 470g); USB-C; dongle for Ethernet

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page

## Raw Sources

- [[stripe-terminal-setup-verifone-2025]] — verbatim Verifone reader setup overview and comparison table
