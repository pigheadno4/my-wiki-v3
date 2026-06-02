---
title: "Stripe Terminal: Mail Order and Telephone Order (MOTO) Payments"
type: source
date_ingested: 2026-04-24
original_format: webpage
raw_files:
  - "stripe-terminal-moto-2025.md"
tags: [stripe, terminal, in-person, moto, card-not-present, cnp, compliance]
---

## Stripe Terminal: Mail Order and Telephone Order (MOTO) Payments

MOTO payments allow merchants to enter card details on a Terminal smart reader when the cardholder provides details over the phone or by mail.

## Key Takeaways

- **Supported readers**: S700/S710 and WisePOS E only
- **Access**: must request from Stripe support before use
- **CNP transactions**: MOTO = card-not-present — no liability shifts; different (higher) pricing than card-present
- **Reader UI**: prompts for card number, CVC, expiry, postal code → summary → confirmation
- **Two use cases**: (1) process MOTO payment immediately; (2) save card for future use
- **Not available in Malaysia**

### Compliance requirements

- Cardholder must NOT be physically present
- Transaction must be initiated by cardholder over phone or mail
- Merchant responsible for verifying cardholder identity
- Must obtain customer consent for saved cards
- PCI compliance required

## Relevant Wiki Pages

- [[stripe]] — Stripe company overview
- [[stripe-terminal]] — Stripe Terminal concept page

## Raw Sources

- [[stripe-terminal-moto-2025]] — verbatim MOTO overview page
