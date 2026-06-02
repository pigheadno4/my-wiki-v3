---
title: "Stripe Terminal: Test Stripe Terminal"
type: source
date_ingested: 2026-04-24
original_format: webpage
raw_files:
  - "stripe-terminal-testing-2025.md"
tags: [stripe, terminal, in-person, testing, simulated-reader, test-cards, physical-test-card, pin]
---

## Stripe Terminal: Test Stripe Terminal

Complete testing reference for Stripe Terminal: simulated reader, test card numbers, physical test card amount codes, simulated update scenarios.

## Key Takeaways

### Testing stages

1. Simulated reader (no hardware required)
2. Physical test card (requires reader)

**Mobile wallets (Apple Pay, Google Pay) cannot be tested in test mode.**

### Simulated reader

- Built into all SDKs + server-driven integration
- No UI — works when SDK/API calls succeed
- SDK integrations: auto-simulate card presentment
- Server-driven: must call `stripe.testHelpers.terminal.readers.presentPaymentMethod('tmr_xxx')` explicitly
- SimulatorConfiguration: test card config persists **30 minutes** across collect + confirm steps

### Standard simulated test cards (20 cards)

Full table in [[stripe-terminal-testing-2025]] raw file. Key cards:

| Card number | Method | Brand |
| --- | --- | --- |
| 4242424242424242 | `visa` | Visa |
| 5555555555554444 | `mastercard` | Mastercard |
| 378282246310005 | `amex` | American Express |
| 6011111111111117 | `discover` | Discover |
| 4506445006931933 | `interac` | Interac |
| 6280000360000978 | `eftpos_au_debit` | eftpos Australia |
| 4000002500001001 | `cartes_bancaires_visa_debit` | Cartes Bancaires / Visa |
| 4711009900000316877 | `girocard_debit` | Girocard |

### PIN test cards (success cases)

| Card number | Method | Simulates |
| --- | --- | --- |
| 4001007020000002 | `offline_pin_cvm` | Offline PIN entry |
| 4000008260000075 | `offline_pin_sca_retry` | SCA retry → insert + offline PIN |
| 4001000360000005 | `online_pin_cvm` | Online PIN entry |
| 4000002760000008 | `online_pin_sca_retry` | SCA retry → online PIN |

### Error test cards

| Card number | Method | Result |
| --- | --- | --- |
| 4000000000000002 | `charge_declined` | Declined: `card_declined` |
| 4000000000009995 | `charge_declined_insufficient_funds` | Declined: `insufficient_funds` |
| 4000000000009987 | `charge_declined_lost_card` | Declined: `lost_card` |
| 4000000000009979 | `charge_declined_stolen_card` | Declined: `stolen_card` |
| 4000000000000069 | `charge_declined_expired_card` | Declined: `expired_card` |
| 4000000000000119 | `charge_declined_processing_error` | Declined: `processing_error` |
| 4000000000005126 | `refund_fail` | Charge succeeds; refund fails async (`expired_or_canceled_card`) |

### Physical test card (sandbox only)

- Works only with Stripe pre-certified readers in sandbox mode
- Chip + contactless; PIN: **`1234`** (unless otherwise stated)
- **Test by amount decimal**:

| Last two digits | Result |
| --- | --- |
| **00** | Approved |
| **01** | Declined: `call_issuer` |
| **02** | Offline PIN flow (requires screen reader) |
| **03** | Online PIN flow (any 4-digit PIN) |
| **05** | Declined: `generic_decline` |
| **55** | Declined: `incorrect_pin` |
| **65** | Declined: `withdrawal_count_limit_exceeded` |
| **75** | Declined: `pin_try_exceeded` |

For zero-decimal currencies (e.g. JPY), use those digits as the rightmost two digits of the full amount (e.g. 105 JPY → `generic_decline`).

### Regional physical test cards

- **Interac** (CA only): separate card from Dashboard; supports `interac_present` payments + refunds; no contactless
- **eftpos** (AU only): separate card from Dashboard; same test amounts as `card_present`

### Simulated reader update scenarios (7 options)

Configure before `connectReader`. Options: `None/NONE`, `Required/REQUIRED`, `RequiredForOffline/REQUIRED_FOR_OFFLINE`, `Available/UPDATE_AVAILABLE`, `LowBattery/LOW_BATTERY`, `LowBatterySucceedConnect/LOW_BATTERY_SUCCEED_CONNECT`, `Random/RANDOM`.

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page

## Raw Sources

- [[stripe-terminal-testing-2025]] — verbatim Terminal testing reference (simulated test cards, physical test card amounts, update scenarios)
