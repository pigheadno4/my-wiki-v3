---
title: "Stripe Terminal: Set Up Verifone P630"
type: source
date_ingested: 2026-04-24
original_format: webpage
raw_files:
  - "stripe-terminal-setup-p630-2025.md"
tags: [stripe, terminal, in-person, card-reader, verifone, p630, hardware, setup, ethernet, preview]
---

## Stripe Terminal: Set Up Verifone P630

Setup guide for the Verifone P630 — mains-powered Android sPOS, 3.5" screen, in preview.

## Key Takeaways

### Availability

Public preview US/CA; private preview GB/IE/SG. Contact Sales to order.

### Integration support

All 5 integrations (JS, iOS, Android, React Native, server-driven). Server-driven recommended.

### Power

- Power cable connects to back of reader (remove back cover to access connection point)
- Requires 110-240W; Verifone adapter recommended (third-party may invalidate warranty)
- No battery

### Settings access

Swipe right from left edge → **Settings** → admin PIN `07139`.

### Network connectivity

Source states: "WiFi or cellular data" — however, the hardware spec table shows cellular = "–". The cellular reference may indicate an undocumented dongle-based option or a documentation error.

> [!info] Evolving — "Cellular data" mentioned in P630 setup source but cellular listed as "–" in hardware spec table. Treat cellular as uncertain/unconfirmed for P630.

### Ethernet

Via **Orange Dongle** accessory (named accessory, 10/100).

### Network priority

**WiFi first** — unlike all other Verifone/smart readers which prioritize Ethernet. P630 only switches to Ethernet when Ethernet is connected; switches back to WiFi if disconnected.

### Default UI theme

Light. Configurable via Appearance settings.

### Custom mounting

P630 can be mounted to a wall or flat surface (with or without a mounting plate). No other Verifone reader has this feature documented.

### Language

Configurable in settings; may require device restart.

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page

## Raw Sources

- [[stripe-terminal-setup-p630-2025]] — verbatim Verifone P630 setup guide
