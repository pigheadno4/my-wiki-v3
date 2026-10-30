---
title: "Adyen Recurring API v68 POST /listRecurringDetails"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Recurring/latest/post/listRecurringDetails"
raw_files:
  - "adyen/api-explorer/Recurring/latest/post/listRecurringDetails/2026-09-15.md"
tags: [adyen, recurring, api, stored-payment-methods, classic]
---

## Overview

Captured **Recurring API v68** `POST /listRecurringDetails` reference on the `pal-test` server. It lists stored payment details for a shopper when available and returns summaries for shopper presentation. A `recurringDetailReference` identifies a legacy recurring detail that can be used with a separate regular authorization request; this lookup itself does not charge the shopper. See [[adyen]] and [[adyen-tokenization]].

## Key takeaways

- The request table marks `merchantAccount` and `shopperReference` required. The `recurring` object and its `contract` property are optional in the schema; the page does not separately label the request body as required.
- If filtering by contract, the value generally needs to match the original payment's recurring contract. For an original `ONECLICK,RECURRING` contract, the page says to request either `ONECLICK` or `RECURRING`, according to whether the shopper will enter the card security code. The table describes `PAYOUT` and `EXTERNAL` contract values too; consult the raw for their scopes.
- The 200 response may include an optional `details` array of `RecurringDetailWrapper` objects. Within a returned `RecurringDetail`, `recurringDetailReference` and `variant` are marked required; many other card, bank, contract and token-related fields are optional. The array's optional schema marking and “if available” purpose do not guarantee a stored detail for every shopper.
- The `recurringDetailReference` is a recurring-detail identifier, distinct from the shopper reference, merchant account and original payment's `firstPspReference`. A listed detail or a successful lookup is not a payment authorization, capture or settlement result, and does not prove the detail can currently be charged.
- The captured server is `https://pal-test.adyen.com/pal/servlet/Recurring/v68`, not Checkout API v72. `latest` in the canonical URL does not establish today's latest API version or live availability. Errors documented are 400, 401, 403, 422 and 500; this raw includes no response examples.

## Detail locators

- Raw lines 5–12: purpose, legacy authorization-reference statement and captured server.
- Raw lines 14–26: full request schema and contract-match exception.
- Raw lines 28–39: request example with `RECURRING` contract.
- Raw lines 40–70: optional response array, nested recurring-detail fields and identifier roles.
- Raw lines 73–140: error classes and response schema.

## Related

- [[adyen-tokenization]] — provider tokenization and stored-details concept.
- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-tokenization-retrieve-stored-details]] — related Classic guide for this lookup.

## Raw Sources

- [[raw/adyen/api-explorer/Recurring/latest/post/listRecurringDetails/2026-09-15|Captured Recurring API v68 POST /listRecurringDetails reference]]