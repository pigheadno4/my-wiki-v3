---
title: "Stripe: Bank Redirects Overview"
type: source
date_ingested: 2026-05-03
original_format: webpage
raw_files:
  - "stripe-bank-redirects-2025.md"
tags: [stripe, bank-redirects, bancontact, blik, eps, fpx, ideal, p24, twint, pay-by-bank]
---

## Summary

Overview of Stripe's 8 bank redirect payment methods — Bancontact, BLIK, EPS, FPX, iDEAL|Wero, P24, TWINT, Pay by Bank. Covers product support matrix and API support matrix including SetupIntents, setup_future_usage, and redirect requirements.

## Key Details

**Product support matrix** (selected highlights):
- All 8 support Connect + Checkout + Payment Links + Payment Element + Mobile Payment Element
- Express Checkout Element: **unsupported for all**
- BLIK, TWINT: no Subscriptions or Invoicing
- iDEAL|Wero only: Subscriptions via `send_invoice` only (no `charge_automatically`); Invoicing supported
- Bancontact, EPS, FPX, P24: Subscriptions via `send_invoice` only; Invoicing invite-only (except FPX)
- Checkout setup mode: unsupported for BLIK, EPS, FPX, P24, TWINT
- Checkout subscription mode: unsupported for BLIK, EPS, FPX, P24, TWINT

**API support matrix**:

| Method | API enum | SetupIntents | setup_future_usage | Redirect required |
| --- | --- | --- | --- | --- |
| Bancontact | `bancontact` | Yes | Yes | Yes |
| BLIK | `blik` | No | No | No (only redirect-free) |
| EPS | `eps` | No | No | Yes |
| FPX | `fpx` | No | No | Yes |
| iDEAL\|Wero | `ideal` | Yes | Yes | Yes |
| P24 | `p24` | No | No | Yes |
| Pay by Bank | `pay_by_bank` | No | No | Yes |
| TWINT | `twint` | Yes | Yes | Yes |

**setup_future_usage note**: Only `off_session` is supported for bank redirect methods that support it. (Cards and bank debits support both `on_session` and `off_session`.)

**BLIK exception**: does not support the deferred intent creation integration path.

## Raw Sources

- [[stripe-bank-redirects-2025]] — verbatim webpage content; flow diagram in `raw/assets/stripe-bank-redirect-payment-flow.svg`
