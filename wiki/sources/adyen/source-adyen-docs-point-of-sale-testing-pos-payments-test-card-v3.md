---
title: "Adyen white-green v3 POS test card"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/testing-pos-payments/test-card-v3"
raw_files:
  - "adyen/docs/point-of-sale/testing-pos-payments/test-card-v3/2026-09-15.md"
tags: [adyen, point-of-sale, payment-testing, physical-test-card, test-card-v3, cardholder-verification, decline-simulation]
---

## Overview

This Adyen Docs page describes the physical white-green version 3 POS test card and its programmed card applications, cardholder-verification tests, and simulated Terminal API declines. See [[adyen]] and [[adyen-payment-testing]] for provider and test-evidence scope. These are test fixtures for POS app and terminal behavior, not live issuer, scheme, regional availability, authorization, capture, settlement, or funding outcomes; the page does not establish behavior for a different test-card version.

## Key takeaways

- The v3 card has applications simulating a payment method, locale, issuer country/region and currency. The snapshot's table lists five Visa chip applications in SGD, JPY, MXN, AED and EUR, plus a China UnionPay magnetic-stripe application in CNY, with an application-specific PIN and identifiers. The introduction says contactless is supported, while the detailed interface table names chip plus contactless for the JPY Visa application and gives a contactless/CVM entry for the SGD Visa application; do not generalize contactless support to every listed application. Japanese and Mexican applications are called out for installment tests.
- Use the corresponding request currency or select the application on the terminal to exercise a particular card application. Cardholder verification depends on that application, interface, amount and currency. The table describes CVM attempts above 100.00 or 200.00 in the application's currency, with fallback behavior; for dynamic currency conversion, the threshold is evaluated on the converted amount. The issuer-country and currency values are simulated card properties, not proof of present-day country acceptance or live currency support.
- For an inserted card, the test system accepts any online PIN; an invalid offline PIN declines the transaction. A contactless transaction above the terminal country/region's contactless reader limit prompts for PIN, and the page routes readers to Customer Area for current configured limits. Despite the offline-PIN CVM scenario, this v3 card cannot be used to test offline transactions because of Visa limitations; offline PIN verification in an online test must not be conflated with offline payment processing.
- Test payments are generally approved unless a simulated decline is requested by changing the last three digits of `RequestedAmount`. The raw table maps triggers to `Result`, `ErrorCondition`, `refusalReason` and `message`; some triggers instead prompt contactless fallback or mobile instructions, and 156, 160 and 161 are reserved for Adyen internal tests. Trigger 139 combined with `AllowPartialAuthorisation` yields a partial payment rather than the ordinary simulated failure. The table is a fixture-specific test map, not production decline behavior.
- The page warns that `refusalReason`, `message` and raw acquirer/issuer responses are for insight and should not be coded against because the raw responses can change. Classic library integrations can show a generic `DECLINED_ONLINE` `posResultCode` for many simulations; the page points to Customer Area or raw notification detail for inspection. Follow the linked response-handling guide for recovery rules; its content was not read here.

## Detail locators

- Card identity, programmed scenarios, test Customer Area and payment-method/interface scope: `# White-green Adyen point-of-sale test card`, raw lines 15–32.
- Application/currency/PIN/interface table and installments: `## Card applications`, raw lines 34–49. Table values are test-card fixtures, not live product eligibility.
- CVM thresholds, conversion condition, online/offline PIN distinction, contactless limit and offline-test exclusion: `## Testing CVMs`, raw lines 51–90.
- `RequestedAmount` triggers, partial-authorization exception, internal-only rows and noncanonical refusal text: `## Simulating declined payments`, raw lines 92–154.
- Raw-response volatility and optional inspection routes: `## Raw responses`, raw lines 156–165.

## Related

- [[adyen]] — provider context.
- [[adyen-payment-testing]] — test-fixture and production-outcome boundary.
- [[adyen-terminal-api]] — POS response context; this source is physical test-card evidence, distinct from versioned API examples.

## Related raw API references

- The raw page links to CVM details, Terminal API decline handling, refusal reasons, alternative test-card packs, installments and raw-response setup. Those linked pages are navigation until independently read; see raw lines 21–32, 49, 53, 87–108 and 167–172.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/testing-pos-payments/test-card-v3/2026-09-15|Adyen Docs: White-green v3 POS test card (2026-09-15 snapshot)]]
