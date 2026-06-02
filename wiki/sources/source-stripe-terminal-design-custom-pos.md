---
title: "Stripe Terminal: Design a Custom POS Integration"
type: source
date_ingested: 2026-04-24
original_format: webpage
raw_files:
  - "stripe-terminal-design-custom-pos-2025.md"
tags: [stripe, terminal, in-person, integration, architecture, pos, locations, sdks, simulated-reader]
---

## Stripe Terminal: Design a Custom POS Integration

Architecture guide for all Terminal reader × SDK combinations. Covers integration patterns, architecture diagrams, and development workflow.

## Key Takeaways

### Architecture types by reader category

| Reader type | Integration model | Connection |
| --- | --- | --- |
| Mobile readers (M2, WisePad 3) | Terminal SDK on POS device; SDK bridges to reader | Bluetooth or USB |
| Smart readers (WisePOS E, S700, S710) | SDK on POS device talks to smart reader over LAN; reader talks to Stripe directly | WiFi or Ethernet (LAN) |
| Server-driven (S700, S710, WisePOS E, Verifone) | POS uses REST API; reader receives commands and handles payment UI independently | Internet |
| Tap to Pay (iPhone, Android) | Phone IS the reader; Terminal SDK on the phone | None (NFC) |

### Locations: required for all readers

Every Terminal reader — **including the simulated reader** — requires a Location object to be associated with it. Create one or more Locations (via Dashboard or API) before connecting any reader.

Locations represent physical places where readers operate. For mobile businesses, use a primary place of business address.

### Development workflow

1. **Simulated reader**: start with a simulated reader and simulated cards — no hardware required. Full integration verification without physical devices.
2. **Physical reader**: order reader + physical test cards → connect → test with physical test cards.
3. **Production**: deploy, ensure all real-world cases handled.

### SDK constraints by reader type

| SDK | Mobile readers (M2, WisePad 3) | Smart readers (WisePOS E, S700/S710) | Tap to Pay |
| --- | --- | --- | --- |
| iOS SDK | ✓ (M2: Bluetooth only) | ✓ | ✓ (iPhone) |
| Android SDK | ✓ (M2: BT or USB) | ✓ | ✓ (Android) |
| React Native SDK | ✓ | ✓ | ✓ |
| JavaScript SDK | – | ✓ (requires LAN/same-network) | – |
| Server-driven | – | ✓ | – |

### JavaScript SDK note

When using the JavaScript SDK with smart readers, the reader and POS app must be on the same local network. Network requirements apply.

### Tap to Pay iOS publishing

Requires Apple Publishing Entitlement + Apple app review before publishing. Market using the Tap to Pay on iPhone Marketing Guide and Toolkit.

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page

## Raw Sources

- [[stripe-terminal-design-custom-pos-2025]] — verbatim custom POS design guide (all readers × all SDKs)
