---
title: "Adyen Docs: White POS test card v1"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/testing-pos-payments/test-card-v1"
raw_files:
  - "adyen/docs/point-of-sale/testing-pos-payments/test-card-v1/2026-09-15.md"
tags: [adyen, point-of-sale, test-card, payment-testing, terminal-api]
---

## Overview

Adyen's 2026-09-15 page documents the white version 1 physical POS test card. Its programmed applications simulate Mastercard and Maestro brands, locale, issuing country/region, currency, and cardholder-verification methods (CVMs) for test-terminal payment and reconciliation checks. This is version-specific test behavior, not a live authorization, card-network guarantee, or evidence that a terminal/software setup currently accepts the card. The pinned page does **not** say that v1 is retired; it directs contactless and mobile Tap to Pay tests to the green-blue Adyen test card version 2.4 or later. [[adyen]] · [[adyen-payment-testing]] · [[adyen-terminal-api]]

## Key takeaways

- To exercise a particular white-card application, use its corresponding currency in the payment request or choose the application after inserting the card at the terminal. The table lists application-specific Mastercard/Maestro, currency, locale, country/region, PIN and PAN fixtures; those values are test fixtures, not live card capabilities.
- Transaction amount **and currency** select the CVM scenario in the card's table. Repeated wrong PIN attempts block the physical test card permanently. In the card-inserted test scenarios, the test system accepts any entered online PIN; invalid offline PIN declines. “Offline PIN” here is a CVM condition, not proof of offline-payment eligibility or store-and-forward behavior.
- To simulate a decline, use a `RequestedAmount` whose last three digits match a row in the raw table. The Terminal API table maps test outcomes to `Result`, `ErrorCondition`, `refusalReason`, and `message`. Adyen explicitly says not to code against the latter two insight fields or unstable raw acquirer/issuer responses. A classic-library integration may instead show a generic `DECLINED_ONLINE` `posResultCode` for most simulations.
- The white v1 card cannot test contactless payments or mobile Tap to Pay; the page points to green-blue v2.4+ for those. Rows 142/143, 154, and 155 describe tap/contactless/mobile interactions in the shared decline table, but their presence does not make those scenarios executable with white v1. Rows 156, 160, and 161 are marked for Adyen internal testing and should not be used for merchant test cases.
- Exceptions in the table matter: ending 139 with `AllowPartialAuthorisation` returns a partial payment rather than the listed failure; rows 134 and 166 need terminal cancellation steps to yield the shown failure. These are simulation conditions only. Test details can be inspected in test Customer Area; the page does not demonstrate live issuer, fraud, capture, or settlement outcomes.

## Detail locators

- **Card identity and unsupported paths:** raw lines 15–33. The separate v2.4+ link is navigation; this entry does not import that page's full behavior.
- **Applications:** “Card applications,” lines 35–47. Inspect the table for exact application, brand, country/region, currency, expiry, locale, PIN and PAN; no single row describes every currency or CVM.
- **CVM and card-blocking:** “Testing CVMs,” lines 49–69. The amount bands differ by application; online versus offline PIN statements are conditional on card insertion in the test reader.
- **Decline simulation:** “Simulating declined payments,” lines 71–133. The table is the authoritative locator for suffix-to-test-result mapping and row-specific remarks, including partial authorization, contactless-only rows, cancellation, and internal-only cases. Do not promote it into a general live refusal-code contract.
- **Raw responses:** lines 135–144. Adyen says raw acquirer/issuer responses can change without notice, so they are not a stable failure-handling key; the page lists optional webhook/Terminal API navigation for accessing them.

## Related

- [[adyen-payment-testing]] — provider test-fixture and outcome boundary
- [[adyen-terminal-api]] — POS message result context
- [[source-adyen-docs-point-of-sale-testing-pos-payments]] — POS testing overview

## Related raw API references

Linked green-blue v2 card, contactless/Mobile Tap to Pay, CVM, classic-library deprecation, tender-option, refusal-handling, and raw-response pages are navigation only; their details were not used to claim white-v1 support.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/testing-pos-payments/test-card-v1/2026-09-15|Adyen white POS test card v1, fetched 2026-09-15]]
