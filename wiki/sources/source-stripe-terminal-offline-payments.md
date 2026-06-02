---
title: "Stripe Terminal: Accept Offline Payments"
type: source
date_ingested: 2026-04-24
original_format: webpage
raw_files:
  - "stripe-terminal-offline-payments-2025.md"
tags: [stripe, terminal, in-person, offline, payment-methods, bluetooth, internet, eea]
---

## Stripe Terminal: Accept Offline Payments

Overview of offline payment support: supported payment methods, readers, and feature differences between Bluetooth and Internet readers.

## Key Takeaways

### Offline-supported payment methods (chip/NFC only, no swipe)

✓ Visa, Mastercard, Discover, Amex, China UnionPay, JCB, Maestro, eftpos, Cartes Bancaires

✗ **Not supported offline**: NYCE/PULSE/STAR, girocard, Interac, QR code payments (WeChat Pay, Affirm, PayNow)

**EEA requirement**: customers must insert card and enter PIN — contactless not allowed for offline payments in the European Economic Area.

**Co-branded (eftpos, Cartes Bancaires)**: routed through international scheme offline.

### Offline-supported readers

| Category | Readers | Connection | Integration |
| --- | --- | --- | --- |
| Bluetooth | Chipper 2X BT, M2, WisePad 3 | Bluetooth, USB (Android) | iOS, Android, React Native SDKs |
| Internet | S700/S710, WisePOS E | Internet | iOS, Android, React Native SDKs |

**No server-driven offline support** (confirmed).

### Feature differences offline: Bluetooth vs Internet readers

| Feature | Bluetooth | Internet |
| --- | --- | --- |
| Tipping | ✗ | ✓ |
| Custom POS app | ✗ | ✓ |
| Extended authorizations | ✓ | ✓ |
| Incremental authorizations | ✗ | ✗ |
| On-screen input collection | ✗ | ✓ |

### Behavior

- Payments stored to disk (survive reboot)
- Auto-forwarded to Stripe when connectivity restored
- SDK re-initialize after reboot → resumes forwarding stored payments

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page

## Raw Sources

- [[stripe-terminal-offline-payments-2025]] — verbatim offline payments overview
