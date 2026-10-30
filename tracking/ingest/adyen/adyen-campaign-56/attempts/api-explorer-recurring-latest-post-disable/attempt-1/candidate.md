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

This 2026-09-15-captured [[adyen]] Recurring API reference documents `POST /disable` on the listed `pal-test.adyen.com/pal/servlet/Recurring/v68` test server. It disables stored payment details to stop charging a shopper with the relevant recurring detail. The URL's `latest` segment does not establish the current API version.

## Key takeaways

- The body requires `merchantAccount` and `shopperReference`; the shopper reference must match the one used in the initial payment. `recurringDetailReference` is optional in the schema but determines scope: when supplied, it identifies a specific stored detail; when omitted, the shopper's whole recurring contract, including all recurring details, is disabled.
- Optional `contract` can limit disabling to a specified use: `ONECLICK`, `RECURRING`, `PAYOUT`, or a comma-separated combination. Do not infer how this selector interacts with omitted `recurringDetailReference` beyond the documented descriptions.
- The 200 response's optional `response` field is described as `[detail-successfully-disabled]` or `[all-details-successfully-disabled]`, depending on whether a detail was specified. This is a stored-detail disable response, not payment authorization or settlement evidence. The captured page does not describe propagation timing to other integrations or deletion of historical transactions.
- The page lists 400, 401, 403, 422 and 500 error response tables; no response examples are included.

## Detail locators

- Purpose and v68 test server: raw lines 5–12.
- Request conditions and example: raw lines 14–33.
- Success and error responses: raw lines 34–112.

## Related

- [[adyen-tokenization]] — stored payment detail and shopper reference context.

## Raw Sources

- [[raw/adyen/api-explorer/Recurring/latest/post/disable/2026-09-15|Recurring API POST /disable, captured 2026-09-15]]
