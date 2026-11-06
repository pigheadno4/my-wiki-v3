---
title: "Management API: List merchant billing entities"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/billingEntities"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/billingEntities/2026-11-05.md"
tags: [adyen, management-api, billing-entities, terminal-ordering]
---

## Overview

The captured Management API `GET /merchants/{merchantId}/billingEntities` lists billing entities of the merchant account identified by the required `merchantId` path ID. A billing entity is the legal entity to which Adyen charges orders, and a terminal-product order must contain a billing-entity ID. The page lists the Test `https://management-test.adyen.com/v3` server and requires the caller's API credential to have **Management API—Terminal ordering read** or **Management API—Terminal ordering read and write**. This is a merchant-scoped lookup, separate from company-wide lookup and from placing an order. [[adyen]] [[adyen-terminal-management]]

## Key takeaways

- The only documented query parameter is optional `name`, the billing-entity name. No request body or numeric response limit is specified. The page says Live calls are subject to rate limits but gives no figure in this capture.
- `200` means the read request succeeded. Its `data` array is optional; billing-entity item fields `id`, `name`, `taxId`, `email`, and `address` are optional, as are the address children. The item's `id` is the reference to supply as `billingEntityId` when creating a separate order. The single merchant-looking entity in the JSON example is illustrative, not a guaranteed response count or ID format.
- `204` is also listed: successful processing with no additional content, so it provides no billing-entity readback. The page documents 400, 401, 403, 422, and 500 errors.
- A successful lookup does not create or charge an order, verify the legal entity or `taxId`, prove Live ordering eligibility, deliver a terminal, or establish any payment, settlement, or bank-receipt result. This GET specifies no idempotency mechanism, lifecycle change, deletion/reversal, propagation delay, asynchronous approval, or Live server URL.

## Detail locators

- Purpose, billing-entity meaning, caller roles, Live rate-limit caveat, and Test server: raw lines 5–19.
- Required merchant path ID, optional name query, and `200` response schema: raw lines 21–54.
- `204` no-content status and error responses: raw lines 57–158. Illustrative `200` JSON example: raw lines 160–181.

## Related

- [[adyen-terminal-management]] — terminal ordering and management context.
- [[source-adyen-api-explorer-management-latest-get-companies-companyid-billingentities]] — separate company-path billing-entity lookup, including associated merchant accounts.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/billingEntities/2026-11-05|Pinned Management API merchant billing-entity list reference]]