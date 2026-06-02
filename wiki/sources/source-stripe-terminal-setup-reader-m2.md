---
title: "Stripe Terminal: Set Up Stripe Reader M2"
type: source
date_ingested: 2026-04-24
original_format: webpage
raw_files:
  - "stripe-terminal-setup-reader-m2-2025.md"
tags: [stripe, terminal, in-person, card-reader, m2, hardware, setup, bluetooth, mobile]
---

## Stripe Terminal: Set Up Stripe Reader M2

Setup guide for the Stripe Reader M2 — compact Bluetooth/USB mobile reader, US only.

## Key Takeaways

### Availability

All 50 US states and Puerto Rico.

### SDK compatibility

iOS, Android, React Native only. **No server-driven, no JavaScript SDK.**

### Power behavior

- Press and release power button to turn on; beeps twice; waits 5 minutes for Bluetooth connection before shutting off
- Automatic off after **10 hours of inactivity** when connected
- Manual off: hold power button 4 seconds
- Reset: hold power button **14 seconds**
- No need to turn off to conserve power

### Battery

- Charge once per day with typical usage
- USB 2.0 cable (included); standard cable compatible
- LED indicator: 4 LEDs = full, 3 = 75%, 2 = 50%, 1 = 25%, flashing = charging

### Accessories

- **Dock** (optional) — countertop checkout
- **Mount** (optional) — roaming checkout
- Custom mechanical design files (.STP) available under Terminal Design File License

### No on-device UI

Unlike smart readers (S700/S710, WisePOS E), the M2 has no settings menu, no admin passcode, and no screen. All configuration is through the SDK and mobile app.

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page

## Raw Sources

- [[stripe-terminal-setup-reader-m2-2025]] — verbatim Stripe Reader M2 setup guide
