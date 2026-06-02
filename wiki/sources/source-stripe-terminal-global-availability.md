---
title: "Stripe Terminal: Global Availability"
type: source
date_ingested: 2026-04-23
original_format: webpage
raw_files:
  - "stripe-terminal-global-availability-2025.md"
tags: [stripe, terminal, in-person, point-of-sale, card-reader, global, payment-methods, tap-to-pay, regional]
---

## Stripe Terminal: Global Availability

Country availability and payment method support matrix for Stripe Terminal.

## Key Takeaways

### Country availability

**GA (23 countries)**: AT, AU, BE, CA, CH, CZ, DE, DK, ES, FI, FR, GB, IE, IT, LU, MY, NL, NO, NZ, PT, SE, SG, US

**Preview (15 countries)**:
- **Full Terminal**: JP, PL
- **Tap to Pay only** (asterisk countries): BG, CY, EE, GI, HR, HU, LI, LT, LV, MT, RO, SI, SK

### Payment method availability

Terminal requires **local currency** for all in-person transactions. Readers auto-configure for their region.

| Payment method | Type | Countries | Notes |
| --- | --- | --- | --- |
| Visa | Card | All Terminal countries | All reader types |
| Mastercard | Card | All Terminal countries | All reader types |
| American Express | Card | All Terminal countries except Malaysia | All reader types |
| Discover & Diners | Card | US, CA, JP (preview), EMEA | Reader varies by region; Diners not in JP |
| China Union Pay | Card | US, CA | Over Discover network; WisePOS E + S700/S710 only; no contactless |
| eftpos | Card | Australia | WisePad 3, WisePOS E, S700, S710, Tap to Pay |
| girocard | Card | Germany | WisePad 3, S700 only |
| Cartes Bancaires | Card | France | WisePad 3, S700, S710, Tap to Pay (preview) |
| Interac | Card | Canada | WisePad 3, WisePOS E, Verifone P400, S700, S710, Tap to Pay (preview) |
| JCB | Card | US, CA, AU, NZ, JP | Via Discover (US) or Amex (CA/AU/NZ) network; WisePOS E contactless not supported |
| Maestro | Card | All non-US Terminal countries | Sunsetting: no new cards issued since July 2023; replacing with Debit Mastercard |
| WeChat Pay | Wallet | 20 countries (AU, AT, BE, CA, DK, FI, FR, DE, IE, IT, LU, NL, NO, PT, SG, ES, SE, CH, GB, US) | WisePOS E, S700, S710, Tap to Pay |
| Affirm | BNPL | US, CA, GB | WisePOS E, S700, S710, Tap to Pay |
| PayNow | Real-time payments | Singapore | WisePOS E, S700, S710, Tap to Pay |

NFC mobile wallets supported across Terminal: **Apple Pay, Google Pay, Samsung Pay**

### Reader hardware referenced

- **Verifone P400** — US legacy reader
- **Stripe M2** — compact mobile reader
- **Chipper 2X BT** — Bluetooth mobile reader
- **WisePad 3** — countertop reader
- **WisePOS E** — smart reader with screen
- **Stripe Reader S700** — smart reader
- **Stripe Reader S710** — smart reader (newer)
- **Tap to Pay on iPhone / Android** — no hardware required

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page

## Raw Sources

- [[stripe-terminal-global-availability-2025]] — verbatim country + payment method availability page
