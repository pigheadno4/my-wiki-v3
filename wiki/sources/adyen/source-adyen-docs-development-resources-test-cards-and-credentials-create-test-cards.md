---
title: "Adyen Create Test Cards"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/development-resources/test-cards-and-credentials/create-test-cards"
raw_files:
  - "adyen/docs/development-resources/test-cards-and-credentials/create-test-cards/2026-09-15.md"
tags: [adyen, test-cards, payment-testing, customer-area, api]
---

## Overview

This Adyen guide describes creating custom card-number ranges for test-platform payment simulations, through Customer Area or the `/createTestCardRanges` API endpoint. The pinned documentation was fetched 2026-09-15 and carries 2026-02-27 last-modified metadata. Generated cards are test fixtures: transactions with them do not credit or debit live accounts, and creation does not establish production card, issuer, merchant or payment-method eligibility.

## Key takeaways

- The Customer Area flow requires the **Manage test cards** role. The guide routes a user to the test Customer Area's **Settings > Test cards > Add new range** form; it also documents an API request to `/createTestCardRanges`. Its API examples are JSON and SOAP, with response and error examples. The SOAP request example reverses start and end in both ranges, even though the page says a start greater than an end fails generation; treat that SOAP sample as illustrative, not a working creation request. The examples also do not prove that a new range was created: both shown success-format responses contain `ALREADY_EXISTS`.
- A generated range uses card numbers of the same length, between 6 and 19 digits, with a valid six-digit BIN and card-number constraints suited to the intended brand. Billing address data must include at least a street address; ZIP is optional. The range bounds are not checked for Luhn compliance at creation, but a card used in a test payment undergoes normal card checks including Luhn verification. Avoid treating acceptance of a range as proof that every number in it can complete a test payment.
- The guide identifies generation failures for reversed or mismatched ranges, length, BIN and AVS constraints, and provides service-exception examples. A submitted API call returns processing confirmation, HTTP status and a response message; inspect the result code or fault before treating a range as created. The guide gives `901 Invalid Merchant Account` as an example security error and `101 Invalid card number` for a Luhn fault.
- For failure-scenario testing, the page points to result-code and refusal-reason guidance rather than requiring custom-card generation. Cardholder name, expiry, CVC, address and 3D-related values in request examples are fixture fields, not a claim about real card data or production authorization.

## Detail locators

- `## Requirements` and `## Test card requirements` — role, numeric range, BIN, Luhn-stage and AVS qualifications.
- `## Generating test cards in Customer Area` — test Customer Area UI path.
- `## Generating test cards via API` / `### Request`, `### Response`, `### Response with an error` — endpoint, JSON/SOAP examples, `ALREADY_EXISTS` and merchant-account error example.
- `## Error handling` / `### Test card response handling` / `### Service exceptions` — processing response, generation failures, Luhn fault and exception messages.

## Related

- Company: [[adyen]]
- Provider testing route: [[adyen-payment-testing]]
- Preset test-card catalog: [[source-adyen-docs-development-resources-test-cards-and-credentials-test-card-numbers]]

## Raw Sources

- [[raw/adyen/docs/development-resources/test-cards-and-credentials/create-test-cards/2026-09-15|2026-09-15 Adyen create-test-cards snapshot]]
