---
title: "Stripe Terminal: Select Your Reader"
type: source
date_ingested: 2026-04-23
original_format: webpage
raw_files:
  - "stripe-terminal-select-reader-2025.md"
tags: [stripe, terminal, in-person, card-reader, point-of-sale, hardware, sdks, tap-to-pay, verifone, offline-payments]
---

## Stripe Terminal: Select Your Reader

Comprehensive comparison of all Stripe Terminal readers: device categories, SDK compatibility, payment input types, features, and physical specs.

## Key Takeaways

### Reader lineup

| Reader | Category | Availability |
| --- | --- | --- |
| Stripe Reader S700/S710 | sPOS (smart POS) | GA — all supported countries |
| BBPOS WisePOS E | sPOS | GA — all supported countries |
| Stripe Reader M2 | mPOS (mobile POS) | GA — **US only** |
| BBPOS WisePad 3 | mPOS | GA — all supported countries except US |
| Tap to Pay on iPhone/Android | Software (no hardware) | GA — all supported countries |
| Verifone (V660p, UX700, P630, M425) | sPOS | Public preview (US, CA); Private preview (GB, IE, SG) |

### SDK / integration compatibility

| SDK | S700/S710 | WisePOS E | M2 | WisePad 3 | Tap to Pay | Verifone |
| --- | --- | --- | --- | --- | --- | --- |
| iOS | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Android | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| React Native (Preview) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Server-driven | ✓ | ✓ | – | – | – | ✓ |
| JavaScript | ✓ | ✓ | – | – | – | ✓ |

### Payment input support

| Input type | S700/S710 | WisePOS E | M2 | WisePad 3 | Tap to Pay | Verifone |
| --- | --- | --- | --- | --- | --- | --- |
| Contactless (NFC) + digital wallets | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| EMV chip | ✓ | ✓ | ✓ | ✓ | – | ✓ |
| Magstripe | ✓ | ✓ | ✓ | – | – | ✓ |
| Offline mode | ✓ | ✓ | ✓ | ✓ | – | ✓ |

### Additional features

| Feature | S700/S710 | WisePOS E | M2 | WisePad 3 | Tap to Pay | Verifone |
| --- | --- | --- | --- | --- | --- | --- |
| Tipping | ✓ | ✓ | Receipt only | ✓ | App-implemented | ✓ |
| On-screen input collection | ✓ | ✓ | – | – | App-implemented | ✓ |
| Custom splash screen | ✓ | ✓ | – | ✓ | – | ✓ |
| Custom POS app | ✓ (paid) | – | – | – | App-implemented | ✓ (paid) |
| Cellular | S710 only | – | – | – | – | – |

### Key physical specs

| | S700 | S710 | WisePOS E | M2 | WisePad 3 |
| --- | --- | --- | --- | --- | --- |
| Display | 5.5" IPS LCD 1920×1080 | 5.5" IPS LCD 1920×1080 | 5" IPS capacitive touch | None | 2.4" color LCD 320×240 |
| Weight | 318g | 318g | 318g | 85g | 130g |
| RAM | 4GB | 4GB | 2GB | 128kb | 128kb |
| Storage | 64GB | 64GB | 16GB | 1MB | 1MB |
| OS | Android 10 | Android 10 | Android 9 | Proprietary | Proprietary |
| Charging | USB-C / dock | USB-C / dock | Micro-USB / dock | USB-C | USB-C / dock |
| Connectivity | WiFi, Ethernet (hub) | WiFi, Ethernet (hub) | WiFi, Ethernet (dock) | Bluetooth, USB | Bluetooth 4.2, USB |
| Battery standby | 140h | 140h | 250h | 42h | 20h |

### Operational rules

- **One reader per SDK instance**: each reader connects to one SDK instance at a time. Four mobile readers in a store needs four devices running the SDK.
- **Pre-certification**: all Terminal readers are PCI/EMV pre-certified. Readers encrypt card data and return a token — raw card data never reaches your app.
- **Automatic software updates**: smart readers (S700/S710, WisePOS E) update automatically when powered on, charged, and idle. Bluetooth readers (M2, WisePad 3) update automatically on SDK connection.
- **Simulated reader**: available for development without physical hardware — no setup required.

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page

## Raw Sources

- [[stripe-terminal-select-reader-2025]] — verbatim "Select your reader" page with full comparison tables and device specs
