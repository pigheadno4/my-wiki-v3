---
title: "Stripe Terminal: Set Up Stripe Reader S700/S710"
type: source
date_ingested: 2026-04-23
original_format: webpage
raw_files:
  - "stripe-terminal-setup-reader-s700-s710-2025.md"
tags: [stripe, terminal, in-person, card-reader, s700, s710, hardware, setup, wifi, ethernet, cellular]
---

## Stripe Terminal: Set Up Stripe Reader S700/S710

Setup guide for the Stripe Reader S700/S710 — Android-based smart readers for countertop and handheld use.

## Key Takeaways

### Country availability difference

- **S700**: 25 countries — all 23 GA Terminal countries + CZ, PL, JP (preview)
- **S710**: 16 countries — US, CA, GB, IE, SG, AU, NZ, FR, BE, AT, ES, SE, NO, PT, FI, MY

### Recommended integration

Server-driven integration (Stripe API directly, no Terminal SDK) is recommended for S700/S710. All 5 integration types are supported.

### S710 minimum SDK versions

| SDK | Minimum version |
| --- | --- |
| iOS | v4.7.3 |
| Android | v3.8.0 |
| React Native | v0.0.1-beta.28 |

### Network architecture

The S700/S710 is a **smart reader**: its firmware communicates directly with Stripe. Your POS app communicates with the reader via:
- **LAN** — using a Terminal SDK (reader must be on same local network as POS)
- **Internet** — using the server-driven integration

### Network priority (S710)

Ethernet → WiFi → Cellular (managed at Android level, no manual switching needed). Plugging in an Ethernet cable while on WiFi automatically switches to Ethernet; removing from dock reverts to WiFi.

### Ethernet hub setup

Ethernet requires an optional hub (sold separately in Dashboard):
- Provides 10/100 wired Ethernet + 2× USB-A ports (for barcode scanner, printer)
- Hub requires 27W power (use included S700/S710 adapter)
- Compatible with S700/S710 Dock for countertop deployments
- Reader obtains IP via DHCP

### Settings access

- Swipe right from left edge → tap **Settings** → admin passcode `07139`
- From settings: WiFi configuration, pairing code for device registration, language, theme, screen timeout

### Power

- Requires 12W minimum; Stripe adapters recommended (third-party may invalidate warranty)
- Battery: ~15 hours active use; leave plugged in when idle to receive automatic software updates
- Screen timeout: default 1 hour off charger (configurable in Appearance settings)

### Custom accessories

Mechanical design files (.STP) available under Terminal Design File License for custom mounts and accessories.

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page

## Raw Sources

- [[stripe-terminal-setup-reader-s700-s710-2025]] — verbatim S700/S710 setup guide
