---
title: "Stripe Terminal: Set Up Verifone V660p"
type: source
date_ingested: 2026-04-24
original_format: webpage
raw_files:
  - "stripe-terminal-setup-v660p-2025.md"
tags: [stripe, terminal, in-person, card-reader, verifone, v660p, hardware, setup, ethernet, preview]
---

## Stripe Terminal: Set Up Verifone V660p

Setup guide for the Verifone V660p — Android sPOS with battery, in preview.

## Key Takeaways

### Availability

Public preview US/CA; private preview GB/IE/SG. Contact Sales to order.

### Integration support

All 5 integrations (JS, iOS, Android, React Native, server-driven). Server-driven recommended.

### Power and battery

- Requires **11W** (vs S700's 12W)
- **Charge 8 hours before initial use**
- **Do not let battery fall below 10%** — can permanently reduce capacity
- ~10h active use / 72h standby
- Leave plugged in when idle for automatic software updates

### Settings access

Swipe right from left edge → **Settings** → admin PIN `07139` (same as S700/WisePOS E).

### Default UI theme

Light (same as S700/S710).

### Ethernet

Via optional **Full Feature Base** (sold separately via Dashboard):
- 10/100 Ethernet + 2× USB-A for peripherals
- Barrel connector power (use included V660p adapter)
- Network priority: Ethernet → WiFi; DHCP

### Network architecture

Smart reader: firmware talks directly to Stripe. POS app connects via LAN (SDK) or internet (server-driven).

### Screen timeout

1 hour off charger (same as S700/WisePOS E). Configurable via Appearance settings.

### Language

Configurable in settings; may require device restart.

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page

## Raw Sources

- [[stripe-terminal-setup-v660p-2025]] — verbatim Verifone V660p setup guide
