---
title: "Adyen Test Card Numbers"
type: source
date_ingested: 2026-10-12
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/test-cards-and-credentials/test-card-numbers"
raw_files:
  - "adyen/docs/development-resources/test-cards-and-credentials/test-card-numbers/2026-09-15.md"
tags: [adyen, test-cards, online-payments, testing, 3d-secure]
---

## Overview

This Adyen page is a catalog of card numbers, expiry values, and security codes for testing online-payment integrations on Adyen's test platform. It also points to browser and Android test-card tools, shows a server-side `test_` credential convention, and lists cards enrolled for 3D Secure 2 scenarios. Physical POS test cards are a separate route.

## Key takeaways

- The listed numbers work only on Adyen's test platform. They are test fixtures, not proof of live acceptance, issuer behavior, or production payment success. The page warns that RevenueProtect can block a test payment that appears fraudulent; its suggested trust-list step is temporary testing guidance.
- When the client-side integration is not ready, the page shows adding `test_` to test card credentials in a server `/payments` request's encrypted-card-detail fields. This is a test-platform shortcut, not a live encryption method. The shown Mastercard values and `/payments` body are examples.
- Brand and method tables provide exact card data in the raw. Some entries carry behavior qualifications: Bancontact/Visa routing depends on payment-method setup; online Maestro requires 3D Secure; the listed Russia-issued Visa test card is documented to be blocked with error 907 because Adyen does not process transactions within Russia.
- The separate 3D Secure 2 table identifies enrolled test cards and points to a scenario guide. The card list alone does not establish a particular authentication result.

## Detail locators

- Opening and `## Requirements` (raw lines 15–33): online versus POS test-card route, test-platform-only limit, and RevenueProtect qualification.
- `## Tools for testing` and `## Encrypted card details` (raw lines 35–69): Web/Android test-card tools and the server-side `test_` example.
- Card-brand tables (raw lines 71–251): American Express, Bancontact, Cartes Bancaires, China UnionPay, Dankort, Diners, Discover, Eftpos, Elo, Hipercard, JCB, Maestro, Mastercard, UATP, US Debit, Visa, Visa Electron, and V Pay fixtures; see raw for exact values, security-code exceptions, country codes, and footnotes.
- `## 3D Secure 2` (raw lines 253–273): enrolled cards and route to 3DS2 scenario testing.

## Related

- Company: [[adyen]]
- Concept: [[adyen-payment-testing]]

## Raw Sources

- [[raw/adyen/docs/development-resources/test-cards-and-credentials/test-card-numbers/2026-09-15|2026-09-15 Adyen online test-card catalog]]
