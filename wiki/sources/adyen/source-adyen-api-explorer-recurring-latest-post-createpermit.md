---
title: "Adyen Recurring API v68 POST /createPermit — Create recurring permits"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Recurring/latest/post/createPermit"
raw_files:
  - "adyen/api-explorer/Recurring/latest/post/createPermit/2026-09-15.md"
tags: [adyen, recurring-api, permits, tokenization]
---

## Overview

This captured Recurring API v68 reference documents `POST /createPermit`: creating permits linked to an existing recurring contract, with optional permit restrictions. A permit is distinct from the recurring contract, shopper, merchant account, and any later payment. See [[adyen]] and [[adyen-tokenization]].

## Key takeaways

- The request body table requires `merchantAccount`, a `permits` array, `recurringDetailReference` identifying the recurring contract, and a shopper-unique `shopperReference`. No individual permit property is marked required in the table. Optional `partnerId` applies to the permit-per-partner sharing model; optional `profileReference` applies to the shared-permits model.
- Optional permit restrictions include `maxAmount` across one or more permit payments, `singleTransactionLimit`, and `singleUse`; `validTillDate` supplies permit expiry. `resultKey` can link requests to results.
- A 200 response has optional `permitResultList` entries with an optional partner-payment permit `token` and `resultKey`; `pspReference` is an optional request reference. The response schema does not guarantee that each requested permit appears, or establish any later payment authorization, capture, or settlement.
- The captured page lists 400, 401, 403, 422 and 500 errors, including authentication and permission failures. Its `latest` URL shows a `https://pal-test.adyen.com/pal/servlet/Recurring/v68` server in this 2026-09-15 snapshot; current/live availability and account enablement are not established.

## Detail locators

- Purpose and captured test server: raw lines 5–10.
- Required identifiers, permit models, restrictions and expiry: raw lines 14–28.
- 200 result fields and optionality: raw lines 30–41.
- Error status and response tables: raw lines 44–111.

## Related

- [[adyen-tokenization]] — provider token and recurring-payment concept.

## Raw Sources

- [[raw/adyen/api-explorer/Recurring/latest/post/createPermit/2026-09-15|Captured Recurring API POST /createPermit reference]]
