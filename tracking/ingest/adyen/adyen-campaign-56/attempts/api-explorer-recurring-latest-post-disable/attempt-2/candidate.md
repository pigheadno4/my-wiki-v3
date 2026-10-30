---
title: "Adyen Recurring API POST /disable"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Recurring/latest/post/disable"
raw_files:
  - "adyen/api-explorer/Recurring/latest/post/disable/2026-09-15.md"
tags: [adyen, recurring-api, tokenization, stored-payment-methods, disable]
---

## Overview

This 2026-09-15-captured [[adyen]] Recurring API reference documents `POST /disable` on the listed `pal-test.adyen.com/pal/servlet/Recurring/v68` test server. It disables stored payment details to stop charging a shopper with the relevant recurring detail. The URL's `latest` segment does not establish the current API version. The linked [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-tokenization-disable-stored-details|Classic disable guide]] marks this endpoint inactive and unsupported for new integrations; it directs new builds to Checkout API and existing users to migration (guide raw lines 14–21).

## Key takeaways

- The API body requires `merchantAccount` and `shopperReference`; the shopper reference must match the one used in the initial payment. `recurringDetailReference` is optional in the API schema but determines scope: when supplied, it identifies a specific stored detail; when omitted, the shopper's whole recurring contract, including all recurring details, is disabled (API raw lines 19–22).
- The linked Classic guide's prose agrees that omitting `recurringDetailReference` selects all shopper details (guide raw line 27), but its example labeled “all the details” still includes that field (guide raw lines 76–85). Do not use that example as an all-details recipe; retain the API reference's selector rule.
- Optional `contract` can limit disabling to a specified use: `ONECLICK`, `RECURRING`, `PAYOUT`, or a comma-separated combination. Do not infer how this selector interacts with omitted `recurringDetailReference` beyond the documented descriptions.
- The 200 response's optional `response` field is described as `[detail-successfully-disabled]` or `[all-details-successfully-disabled]`, depending on whether a detail was specified. This is a stored-detail disable response, not payment authorization or settlement evidence. The captured API page does not describe propagation timing to other integrations or deletion of historical transactions.
- The API page lists 400, 401, 403, 422 and 500 error response tables; no response examples are included.

## Detail locators

- Purpose and v68 test server: API raw lines 5–12.
- Request conditions and example: API raw lines 14–33.
- Success and error responses: API raw lines 34–112.
- Inactive/migration notice and contradictory all-details example: linked Classic guide raw lines 14–21, 25–27, 76–85.

## Related

- [[adyen-tokenization]] — stored payment detail and shopper reference context.
- [[source-adyen-docs-online-payments-classic-integrations-classic-api-integration-tokenization-disable-stored-details]] — Classic guide with inactive status and conflicting all-details example.

## Raw Sources

- [[raw/adyen/api-explorer/Recurring/latest/post/disable/2026-09-15|Recurring API POST /disable, captured 2026-09-15]]
