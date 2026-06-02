---
title: "Stripe Terminal: Set Up BBPOS WisePOS E"
type: source
date_ingested: 2026-04-24
original_format: webpage
raw_files:
  - "stripe-terminal-setup-wisepos-e-2025.md"
tags: [stripe, terminal, in-person, card-reader, wisepos-e, hardware, setup, wifi, ethernet]
---

## Stripe Terminal: Set Up BBPOS WisePOS E

Setup guide for the BBPOS WisePOS E — Android-based smart countertop reader.

## Key Takeaways

### Country availability

24 countries: all 23 GA Terminal countries + PL (preview). **No JP** (unlike S700 which includes JP preview).

### Integration support

All 5 integrations supported (JavaScript, iOS, Android, React Native, server-driven). Server-driven recommended.

### Battery

- ~8 hours active use (vs S700's ~15 hours)
- User-removable/installable battery; units shipped Jan 2026 or later may have pre-installed battery
- Leave plugged in when idle for automatic software updates

### Settings access

Swipe right from left edge → tap **Settings** → admin passcode `07139` (same as S700/S710).

### Default UI theme

**Dark** (vs S700/S710 which defaults to light). Configurable via Appearance settings.

### Network architecture

Same smart reader architecture as S700/S710: firmware talks directly to Stripe; POS app connects via LAN (Terminal SDK) or internet (server-driven).

### Network priority

Ethernet → WiFi (no cellular — WisePOS E does not have cellular connectivity).

### Ethernet dock

Optional dock (sold separately; 10/100 Ethernet port, rubber feet):
- Minimum power: 5V-2A (10W)
- Ships with wall plug to USB-C cable AND USB-A to USB-C cable (for own USB-A adapter)
- DHCP; switches to Ethernet automatically when docked; reverts to WiFi when undocked

### Screen timeout

Default 1 hour off charger (same as S700/S710). Configurable via Appearance settings.

### Custom accessories

Mechanical design files (.STP) available under Terminal Design File License.

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page

## Raw Sources

- [[stripe-terminal-setup-wisepos-e-2025]] — verbatim BBPOS WisePOS E setup guide
