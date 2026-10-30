---
title: "Adyen Balance Platform API v2: list mandates"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/mandates"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/mandates/2026-09-15.md"
tags: [adyen, balance-platform, business-accounts, direct-debit, mandates, api]
---

## Overview

This 2026-09-15-captured API Explorer reference documents `GET /mandates` on the **Balance Platform API v2 test server** (`https://balanceplatform-api-test.adyen.com/bcl/v2`). It returns a list of direct debit mandates created for a business account. The URL's `latest` segment does not establish a current API version or live availability. See [[adyen]] and [[adyen-business-accounts]].

## Key takeaways

- The three query parameters are optional: `cursor` from a previous list request, `paymentInstrumentId` for the instrument linked to a mandate, and `balanceAccountId` for the balance account linked to that instrument. The response's `link` and `mandates` fields are marked required; page links are present only where applicable.
- Each mandate entry may carry its own `id`, `balanceAccountId`, `paymentInstrumentId`, `counterparty`, timestamps, `status` (`pending`, `approved`, or `cancelled`) and `type` (`bacs`). Within a returned `counterparty`, the table marks `accountHolder` and `accountIdentification` required; it says the latter's required fields depend on bank-account country and transfer currency. These are response-schema markings, not required request fields.
- A successful list response reads mandate records; it neither creates nor approves a mandate, changes its status, authorizes a collection, nor proves a debit or downstream funds receipt. The separate [[source-adyen-docs-business-accounts-accept-direct-debits-uk|UK Bacs Business Accounts guide]] describes limited-availability eligibility, capability checks and external confirmation for mandate changes; do not infer those outcomes from this list read.
- The captured error sections are `401` authentication required, `403` insufficient permissions, `422` request validation error and `500` server processing failure. The page specifies no credential role, live endpoint, response example, status-transition timing or collection outcome.

## Detail locators

- Purpose, method and test-server base path: raw lines 5–10.
- Optional filters and pagination cursor: lines 12–19.
- `200` result and conditional page links: lines 21–40.
- Mandate object identities, counterparty detail, status and type: lines 40–50.
- Error meanings and problem-body fields: lines 53–126.

## Related

- [[adyen-business-accounts]] — Business Accounts product context.
- [[source-adyen-docs-business-accounts-accept-direct-debits-uk]] — separate dated UK Bacs pilot and mandate/collection flow.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/mandates/2026-09-15|GET /mandates API Explorer capture]]
