---
title: "Stripe Terminal: BBPOS WisePOS E"
type: source
date_ingested: 2026-05-01
date_updated: 2026-11-24
original_format: webpage
canonical_url: "https://docs.stripe.com/terminal/readers/bbpos-wisepos-e"
raw_files:
  - "stripe-terminal-readers-bbpos-wisepos-e-2026-11-07.md"
  - "stripe-terminal-bbpos-wisepos-e-2025.md"
tags: [stripe, stripe-terminal, wisepos-e, smart-readers, firmware, countertop]
---

## Summary

The May 1 and November 7, 2026 guides cover the BBPOS WisePOS E countertop reader, its diagnostics, and its Stripe-managed software. They list JavaScript, iOS, Android and React Native SDKs plus the recommended server-driven integration, which uses the Stripe API.

The reader software communicates directly with Stripe. The separate November model setup guide explains that the POS app uses the same local network as the reader with a Terminal SDK, or communicates over the internet with server-driven integration. See [[source-stripe-terminal-setup-wisepos-e]] and its November raw lines 63–65.

## WisePOS E Software Versions

| Capture | Reader app | Firmware | ROM |
| --- | --- | --- | --- |
| 2026-11-07 | `2.46.4.0` | `5.01.06.01` (AU `5.01.06.01.eftpos`) | `1.8.9.4` |
| 2026-05-01 | `2.41.2.0` | `5.01.03.00` (AU `5.01.03.00.eftpos`) | `1.8.4` |

These releases are listed in the dated WisePOS E tables. Check the reader’s installed version in Diagnostics. Stripe describes the software as four components (reader app, firmware, configuration and key identifier) and gives the PCI firmware ID format `WSC5x.11-WXYZZ-ABCDD`.

| Region in the documentation | Configuration |
| --- | --- |
| US | `szzz_us_v19` |
| CA | `szzz_ca_v17` |
| AU | `szzz_prod_au_v11` |
| MY/NZ | `szzz_prod_apac_on_v4` |
| SG (May), HKSG (November firmware table) | `szzz_prod_apac_off_v4` |
| GB/IE/FI | `szzz_prod_eu_off_v11` |
| AT/BE/DK/FR/IT/DE/NL/ES/SE/CZ/LU/PT/CH/NO | `szzz_prod_eu_on_v7` |

> **Hong Kong deployment (2026-11-07).** The firmware row says `HKSG`. The device and model setup banners list the same 24 markets, including SG and omitting HK, MX and JP. The same-day [[source-stripe-terminal-collect-tips]] guide includes HK and MX in a combined S700/S710 and WisePOS E **on-reader tipping** row. The device banners, firmware grouping and tipping feature list have separate scopes. General WisePOS E deployment in Hong Kong remains unresolved. See November device raw lines 5–14 and 128–136, setup raw line 8, and tipping raw lines 22–25.

The November changelog adds five dated entries from May 26 through October 20, 2026. Version `2.45.7.0` (September 8) fixes truncated long translated tip-selection text and occasional countertop-mode auto-disconnects. Version `2.46.4.0` (October 20) and the other three new entries describe general fixes and improvements.

The May capture directs software-acceptance users to the [Terminal bundle release notes](https://docs.stripe.com/terminal/fleet/software-acceptance/release-notes.md). The November reader capture omits this route, leaving software-acceptance status unresolved.

## Reader Operation

- **Diagnostics.** Check reader-to-Stripe connectivity for payments and software updates. For a docked reader using Ethernet, connect both cables before inserting the reader. Reinsert the reader. Run Diagnostics if the connection still fails.
- **Updates and restarts.** Stripe sends automatic updates while the reader is idle. Keep it on and connected to power for updates at midnight in the assigned location’s time zone. The reader restarts daily at midnight for PCI compliance and disconnects from the POS app every morning. Reboot to check manually. A missed required update can prevent the reader from accepting payments.
- **Power and LEDs.** Hold the power button for two seconds. The left array reports battery or charging and the right array reports reader status. The captured text tables omit the visual patterns. For an integrity or tamper indication, Stripe directs readers under warranty to the warranty claim route and purchases through a Connect platform to that provider.
- **Payment sounds.** The expected-sounds table lists one long high-pitched beep for both tap success and tap failure. Chip and swipe are silent in that table.

## Related Pages

- [[stripe]] — company page
- [[stripe-terminal]] — Terminal concept
- [[source-stripe-terminal-setup-wisepos-e]] — WisePOS E setup and networking
- [[source-stripe-terminal-collect-tips]] — tipping methods and feature-specific market coverage
- [[source-stripe-terminal-s700-s710]] — separate S700/S710 reader operations and firmware reference

## Raw Sources

- [[raw/stripe-terminal-readers-bbpos-wisepos-e-2026-11-07|November 7, 2026 BBPOS WisePOS E reference]]
- [[stripe-terminal-bbpos-wisepos-e-2025]] — May 1, 2026 verbatim webpage (LED tables, sounds, diagnostics, full changelog and firmware versions)
