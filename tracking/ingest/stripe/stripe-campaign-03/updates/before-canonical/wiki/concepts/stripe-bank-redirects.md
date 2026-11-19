---
title: "Bank Redirects (Stripe)"
type: concept
category: technology
tags: [stripe, bank-redirects, bancontact, blik, eps, fpx, ideal, p24, twint, pay-by-bank]
---

## Definition

Bank redirects let customers pay online by being redirected to their bank's portal, logging in, and approving the transaction. Dominant payment method in Germany, Netherlands (iDEAL), and Malaysia (FPX). Covers 8 methods: Bancontact, BLIK, EPS, FPX, iDEAL|Wero, P24, Pay by Bank, TWINT.

Not suitable for subscriptions with `charge_automatically` — most bank redirect methods are single-use or require redirect-based approval each time.

## Methods and API Enums

| Method | Enum | SetupIntents | setup_future_usage | Redirect |
| --- | --- | --- | --- | --- |
| Bancontact | `bancontact` | Yes | Yes (`off_session` only) | Yes |
| BLIK | `blik` | No | No | No |
| EPS | `eps` | No | No | Yes |
| FPX | `fpx` | No | No | Yes |
| iDEAL\|Wero | `ideal` | Yes | Yes (`off_session` only) | Yes |
| P24 | `p24` | No | No | Yes |
| Pay by Bank | `pay_by_bank` | No | No | Yes |
| TWINT | `twint` | Yes | Yes (`off_session` only) | Yes |

BLIK is the only bank redirect that does **not** require a browser redirect.

## Product Support Notes

- **Express Checkout Element**: unsupported for all bank redirects
- **Checkout setup/subscription mode**: unsupported for BLIK, EPS, FPX, P24, TWINT
- **Subscriptions**: only iDEAL|Wero, Bancontact, EPS, FPX, P24 — all via `send_invoice` only (not `charge_automatically`)
- **Invoicing**: FPX full support; iDEAL|Wero full support; Bancontact/EPS/P24 invite-only; BLIK/TWINT unsupported
- **BLIK**: does not support deferred intent creation path

## Sources

- [[source-stripe-bank-redirects]] — primary source: product support matrix, API support matrix, payment flow
