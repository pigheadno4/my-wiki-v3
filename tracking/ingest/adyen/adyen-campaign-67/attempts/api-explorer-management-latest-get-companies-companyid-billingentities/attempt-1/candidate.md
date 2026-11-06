---
title: "Management API: List company billing entities"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/billingEntities"
raw_files:
  - "adyen/api-explorer/Management/latest/get/companies/(companyId)/billingEntities/2026-11-05.md"
tags: [adyen, management-api, billing-entities, terminal-ordering]
---

## Overview

The captured Management API `GET /companies/{companyId}/billingEntities` lists billing entities for the company account identified by `companyId` and its merchant accounts. A billing entity is the legal entity to which Adyen charges orders; terminal-product orders must contain its ID. The reference lists the Test `https://management-test.adyen.com/v3` server and requires the caller's API credential to have **Management API—Terminal ordering read** or **Management API—Terminal ordering read and write**. This is a lookup for terminal ordering, not an order or payment operation. [[adyen]] [[adyen-terminal-management]]

## Key takeaways

- `companyId` is the required path identifier of the company account. Optional query `name` is a billing-entity name filter. No request body is described.
- The `200` response says the request succeeded. Its `data` array is optional in the response schema; its billing-entity objects have optional `id`, `name`, `taxId`, `email`, and `address` fields, with optional address children. The `id` is the value to use as `billingEntityId` when creating a separate order. The example's company- and merchant-looking IDs are illustrative and do not establish a universal ID format or a mandatory number of entries.
- The page says Live requests are subject to rate limits, but gives no numeric limit in this capture. It lists 400, 401, 403, 422, and 500 errors. A successful listing does not create an order, verify a tax number or legal entity, charge an invoice, establish current Live ordering eligibility, or prove terminal delivery or payment.
- No idempotency header, state transition, deletion, asynchronous review/approval, propagation timing, or Live server URL is specified by this read-only endpoint. These are evidence limits of the captured page.

## Detail locators

- Purpose, billing-entity definition, caller roles, Live rate-limit caveat, and Test server: raw lines 5–19.
- Required company path ID, optional name query, and `200` response-field schema: raw lines 21–54.
- Error statuses and payloads: raw lines 57–154. The `200` example with two illustrative company/merchant entity entries: raw lines 156–189.

## Related

- [[adyen-terminal-management]] — terminal ordering and management context.
- [[adyen-account-structure]] — company versus merchant-account hierarchy.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/billingEntities/2026-11-05|Pinned Management API billing-entity list reference]]