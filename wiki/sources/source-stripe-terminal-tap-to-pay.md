---
title: "Stripe Terminal: Tap to Pay (iPhone + Android)"
type: source
date_ingested: 2026-04-24
original_format: webpage
raw_files:
  - "stripe-terminal-tap-to-pay-2025.md"
tags: [stripe, terminal, in-person, tap-to-pay, iphone, android, nfc, contactless, pin, mobile]
---

## Stripe Terminal: Tap to Pay (iPhone + Android)

Complete guide for Tap to Pay on iPhone and Android — software-only contactless acceptance using compatible mobile devices.

## Key Takeaways

### Payment methods supported (both platforms)

Visa, Mastercard, American Express, Discover (contactless), NFC wallets, QR-based payment methods, PIN entry. Regional: eftpos (AU), Interac (CA), Cartes Bancaires (FR).

### Country availability comparison

| Status | iPhone | Android |
| --- | --- | --- |
| GA (20/18) | AT, AU, BE, CA, CH, CZ, DE, DK, ES, FR, GB, IE, IT, NL, NZ, PL, PT, SE, SG, US | AT, AU, BE, CH, DE, DK, FI, FR, GB, IE, IT, MY, NL, NZ, PL, SE, SG, US |
| Preview | BG, CY, EE, FI, HR, HU, JP, LI, LT, LU, LV, MT, MY, NO, RO, SI, SK | BG, CA, CY, CZ, EE, ES, GI, HR, HU, LI, LT, LU, LV, MT, NO, PT, RO, SI, SK |

Key differences:
- **iPhone GA, Android preview**: CA, CZ, ES, PT
- **Android GA, iPhone preview**: FI, MY
- **iPhone not available**: Puerto Rico (explicitly excluded)

### iPhone setup requirements

- Apple Developer entitlement required: `com.apple.developer.proximity-reader.payment.acceptance = true`
- Development + distribution entitlements needed separately
- App must be submitted to Apple for review (complex process)
- SDKs: Terminal iOS SDK and Terminal React Native SDK
- Minimum device: iPhone XS or later; non-beta iOS; requirements change — subscribe to terminal-announce list
- PIN entry: iOS 16.4+ required
- "How to Tap" instructional overlay: **required by Apple** before app submission; implement via `ProximityReaderDiscovery` API (iOS 18+, provide fallback UI for earlier versions)

### Android setup requirements

- Separate dependency: `com.stripe:stripeterminal-taptopay` (not the standard `stripeterminal` package)
- SDKs: Terminal Android SDK and Terminal React Native SDK
- Minimum: Android 13, NFC + ARM processor, not rooted, GMS certified (Google Play Store), hardware keystore ECDH v100+, security patch within 12 months, developer options disabled
- Emulators not supported (same requirements enforced in simulated reader for realistic testing)
- PIN entry: Android SDK v4.3.0+
- Custom UX: `TapToPayUxConfiguration` — colors, dark mode, tap zone position (can be called multiple times during app lifetime)
- PIN pad appears at random position on screen (security by design)

### CVM / PIN regional gotchas (both platforms)

- **UK**: some issuers require Strong Customer Authentication via card insertion — if card not inserted, payment declined with `offline_pin_required`
- **Canada & Finland**: many cards are offline PIN only (requires physical insertion) — Tap to Pay cannot fulfill this requirement
- Recommendation: ask customer to try different card or use a Terminal card reader / Payment Link

### Android supported device requirements

- NFC sensor + ARM processor; not rooted; locked bootloader
- Android 13+; security update within 12 months
- GMS certified + Google Play Store installed
- Hardware keystore ECDH (`FEATURE_HARDWARE_KEYSTORE` ≥ 100)
- Internet connection; unmodified manufacturer OS; developer options disabled
- Device types: phones, tablets, handheld, kiosk, countertop (Sunmi, Samsung, Google Pixel, Motorola, Xiaomi, Honeywell, Zebra, and many more)

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page

## Raw Sources

- [[stripe-terminal-tap-to-pay-2025]] — verbatim Tap to Pay iPhone + Android combined guide
