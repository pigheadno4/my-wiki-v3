---
title: "Stripe Terminal: Set Up BBPOS WisePad 3"
type: source
date_ingested: 2026-04-24
original_format: webpage
raw_files:
  - "stripe-terminal-setup-wisepad3-2025.md"
tags: [stripe, terminal, in-person, card-reader, wisepad3, hardware, setup, bluetooth, mobile, pin-pad]
---

## Stripe Terminal: Set Up BBPOS WisePad 3

Setup guide for the BBPOS WisePad 3 — Bluetooth/USB handheld reader with PIN pad, non-US markets.

## Key Takeaways

### Country availability

25 countries: all GA Terminal countries **except US** + PL and JP (preview). The WisePad 3 is the non-US counterpart to the M2.

### SDK compatibility

iOS, Android, React Native only. **No server-driven, no JavaScript SDK.**

### Distinguishing feature

Physical display + PIN pad — designed for markets where PIN-authenticated transactions are common (non-US).

### Power behavior

- Hold power button to turn on; splash screen displays
- Display dims after a few seconds of inactivity
- Auto-off: **5 minutes of inactivity while disconnected** (beeps then powers off)
- Manual off: hold power button until "Power off?" prompt, then press green Enter

### Battery

- Charge once per day with typical usage
- **~600 contact transactions or ~800 contactless transactions per charge**
- USB-A to USB-C cable

### Language configuration

- On-device language selection via Power/Settings button → arrow keys → green Enter
- After registering to a Location, reader auto-installs region language pack if not already present

### Accessories

Custom mechanical design files (.STP) available under Terminal Design File License. No first-party dock or mount listed (unlike M2).

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page

## Raw Sources

- [[stripe-terminal-setup-wisepad3-2025]] — verbatim BBPOS WisePad 3 setup guide
