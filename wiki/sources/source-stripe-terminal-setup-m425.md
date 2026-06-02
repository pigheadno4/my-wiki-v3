---
title: "Stripe Terminal: Set Up Verifone M425"
type: source
date_ingested: 2026-04-24
original_format: webpage
raw_files:
  - "stripe-terminal-setup-m425-2025.md"
tags: [stripe, terminal, in-person, card-reader, verifone, m425, hardware, setup, ethernet, preview]
---

## Stripe Terminal: Set Up Verifone M425

Setup guide for the Verifone M425 — mains-powered Android sPOS, tablet form factor, US/CA public preview only.

## Key Takeaways

### Availability

Public preview US/CA **only**. No private preview in any other country. Contact Sales to order.

### Integration support

All 5 integrations (JS, iOS, Android, React Native, server-driven). Server-driven recommended.

### Power

- USB-C cable into back of reader, connected via dongle + power adapter
- 100-240V AC power
- **Power button is on the back left side** of the reader
- Power on: hold 2 seconds; power off: hold 5 seconds
- No battery — mains-powered only; Verifone adapter recommended

### Settings access

Swipe right from left edge → **Settings** → admin PIN `07139`.

### Ethernet

Via **Orange Dongle** (same accessory name as P630); 10/100.

### Network priority

No explicit priority stated in source — does not specify whether WiFi or Ethernet takes precedence.

### Default UI theme

Light. Configurable via Appearance settings.

### Source error noted

The "Change the UI appearance" section header in the Stripe source doc says "By default, the UI of the **P630** reader uses a light theme" — this is a copy-paste error in Stripe's docs; should read M425. Content is otherwise accurate for M425.

### Language

Configurable in settings; may require device restart.

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page

## Raw Sources

- [[stripe-terminal-setup-m425-2025]] — verbatim Verifone M425 setup guide
