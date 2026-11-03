---
title: "Adyen Balance Platform API v2: get a specific mandate"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/mandates/(mandateId)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/mandates/(mandateId)/2026-11-03.md"
tags: [adyen, balance-platform, business-accounts, direct-debit, mandates, api]
---

## Overview

This 2026-11-03 API Explorer capture documents `GET /mandates/{mandateId}` on the Balance Platform API v2 **TEST** server (`https://balanceplatform-api-test.adyen.com/bcl/v2`). It returns details of the specified direct debit mandate. The `latest` URL segment does not prove current version or live availability. See [[adyen]] and [[adyen-business-accounts]].

## Key takeaways

- The sole documented input is required path parameter `mandateId`, the mandate's unique identifier. This GET reference lists no query parameter or request body. It does not name a credential role, idempotency mechanism, default, or rate limit.
- A `200` response is a successful read. Its top-level fields are marked optional: `id` (mandate), `balanceAccountId` (balance account linked to the payment instrument), `paymentInstrumentId`, `counterparty`, `createdAt`, `updatedAt`, `status`, and `type`. The listed statuses are `pending`, `approved`, and `cancelled`; the listed type is `bacs`. Inside an included `counterparty`, `accountHolder` and `accountIdentification` are marked required, and `accountIdentification.type` is marked required. Other required bank-identification fields depend on bank-account country and transfer currency. These are response-schema markings, not request inputs.
- Readback reports a mandate record and its reported status. It does not create, approve or cancel the mandate, prove current eligibility or approval, authorize or execute a debit, or establish a booking, settlement or bank receipt. The capture does not define status-transition timing, propagation, reversal or deletion behavior. See the separate [[source-adyen-docs-business-accounts-accept-direct-debits-uk|UK direct-debit guide]] for its own dated product context.
- Documented errors are `401` authentication required, `403` insufficient permissions, `404` mandate not found, `422` request validation error, and `500` server processing failure. Their response schemas list optional problem details and an optional `invalidFields` array whose present entries require `message`, `name`, and `value`.

## Detail locators

- Endpoint purpose, TEST base URL, and path input: raw lines 5–17.
- `200` response fields, nested counterparty markings, status and type: raw lines 19–38.
- Error meanings and problem-field schemas: raw lines 41–133.

## Related

- [[adyen-business-accounts]] — product and mandate context.
- [[source-adyen-api-explorer-balanceplatform-latest-get-mandates]] — separate mandate list reference.
- [[source-adyen-docs-business-accounts-accept-direct-debits-uk]] — separate UK Bacs guide.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/mandates/(mandateId)/2026-11-03|GET /mandates/{mandateId} API Explorer capture]]