---
title: "Adyen B2 physical POS test-card sets"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/testing-pos-payments/b2-test-cards"
raw_files:
  - "adyen/docs/point-of-sale/testing-pos-payments/b2-test-cards/2026-09-15.md"
tags: [adyen, point-of-sale, payment-testing, physical-test-cards, b2-test-cards, emv, offline-testing]
---

## Overview

This Adyen Docs page describes physical B2 Europe and North America EMV test-card sets used with Adyen test terminals for point-of-sale card-transaction testing. The stated integration scope includes Terminal API with payment terminals and standalone terminals. See [[adyen]] and [[adyen-payment-testing]]. The card sets are test fixtures for specific brands, locales, issuer regions, and currencies; a test response does not establish current production card acceptance, merchant eligibility, authorization, capture, settlement, or funding.

## Key takeaways

- The page points to a six-card Europe EMV set and a seven-card North America EMV set sold through B2. It says card details should be checked on the physical card because earlier or later sets may differ from the snapshot's tables. The B2 store links are purchase/navigation routes; this snapshot does not verify current inventory, pricing, or card-software revision.
- Both described sets have chip and magstripe cards that support EMV contact and contactless test transactions. The Europe table spans Visa, Mastercard, Maestro, American Express, Discover and Diners fixtures with listed locales, simulated issuing countries/regions and EUR/GBP currencies. The North America table includes U.S. Visa, Mastercard, American Express, Discover, Diners and Visa U.S. Common Debit fixtures in USD plus a Canadian Interac fixture in CAD. Table values identify these test cards, not live scheme or regional acceptance.
- Use a B2 card on an Adyen test terminal to check whether the integration handles that test method; the page gives a Visa example. It says declines can be tested similarly to the separate Adyen test-card guide, but the actual trigger instructions are linked and were not read for this entry. B2 cards cannot trigger a particular CVM solely by choosing a specific test amount, so do not transfer the other card's amount-to-CVM map to these fixtures.
- None of the described North America cards support testing offline payments. The page says offline-payment testing is unavailable with B2 cards except for the French Mastercard card from the Europe set, marked **Offline Capable** in that table. This is a test-card condition, not a statement that all real Mastercard cards or all merchant terminals can process offline.
- For Manual Key Entry with a B2 test card, use expiration **03/30** instead of the expiration printed on the card. The page provides no general PIN, software-version, terminal-model, or production rule beyond the table and this MKE instruction; do not infer them from the listed examples.

## Detail locators

- B2 fixture purpose, test-terminal condition and integration modes: `# B2 test cards` and `## Requirements`, raw lines 15–28.
- Set purchase/navigation and card-edition warning: `## How to get a B2 test card set` and `## Details of the test cards`, raw lines 30–41.
- Europe card table, chip/magstripe/contactless statement and French Mastercard offline marker: `### Tab: Europe EMV test card set`, raw lines 43–54. North America table and explicit offline exclusion: `### Tab: North America EMV test card set`, lines 56–68.
- Visa test example, linked decline instructions, amount/CVM and offline exceptions, MKE expiration: `## How to use B2 test cards`, raw lines 70–80.

## Related

- [[adyen]] — provider context.
- [[adyen-payment-testing]] — test-fixture and production-outcome boundary.
- [[adyen-terminal-api]] — relevant in-person integration context; this source also covers standalone testing.

## Related raw API references

- The raw page links to B2 store/set listings, Adyen's separate test-card decline/offline instructions, and response handling. Those targets are navigation until independently read; see raw lines 19, 32–37, 74–76 and 82–85.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/testing-pos-payments/b2-test-cards/2026-09-15|Adyen Docs: B2 test cards (2026-09-15 snapshot)]]
