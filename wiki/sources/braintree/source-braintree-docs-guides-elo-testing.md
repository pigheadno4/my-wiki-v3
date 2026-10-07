---
title: "Braintree Elo Testing"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/elo/testing"
raw_files:
  - "braintree/docs/guides/elo/testing-2026-09-16.md"
tags: [braintree, elo, sandbox, testing, cards]
---

## Overview

This captured unversioned [[braintree|Braintree]] webpage is an Elo Sandbox test-fixture reference for select limited-release merchants using what the page calls the latest JavaScript v3 and server SDKs. It supplies Elo credit-card numbers and special expiration-field values for verification or enrollment error tests; those fixtures are not a Production card set or payment-execution evidence, and the snapshot's relative "latest" wording does not identify the currently latest SDK release or establish present merchant access. [[braintree-payment-methods]]

## Key takeaways

- The page conditions Elo access on a limited release for select merchants, requires its page-relative latest JavaScript v3 and server SDKs, and directs merchants to request access.
- In Sandbox, the three listed card numbers are labeled Elo credit cards. For verification or enrollment API calls, `expirationYear` value `2020` and `expirationDate` value `10` are documented as expired-card error fixtures.

> [!warning] Environment and access boundary
> Use these values only as the captured Elo Sandbox fixtures under the page's limited-release and SDK conditions; the page does not present them as Production card data or prove merchant enablement or a successful payment.

## Detail locators

- **Limited-release merchant and SDK conditions:** `AVAILABILITY`, raw lines 17-18.
- **Elo Sandbox credit-card fixtures:** `## Test card numbers`, raw lines 21-28.
- **Verification and enrollment expired-card triggers:** `## Testing other error cases`, raw lines 31-37.

## Related

- Company: [[braintree]]
- Main concept: [[braintree-payment-methods]]
- Brazil-path accepted-method scope: [[source-braintree-articles-br-transactions-accepted-payment-methods]]
- General card testing and go-live route: [[source-braintree-credit-cards-testing-go-live-node]]

## Raw Sources

- [[raw/braintree/docs/guides/elo/testing-2026-09-16|Braintree Elo Testing (2026-09-16 snapshot)]]
