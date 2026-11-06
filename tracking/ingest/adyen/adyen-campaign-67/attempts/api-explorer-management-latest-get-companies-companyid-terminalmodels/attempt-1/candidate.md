---
title: "Adyen Management API v3: list company terminal models"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/terminalModels"
raw_files:
  - "adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalModels/2026-11-05.md"
tags: [adyen, management-api, terminal-management, terminal-models]
---

## Overview

This 2026-11-05-captured Management API reference describes `GET /companies/{companyId}/terminalModels`, a company-scoped lookup for payment terminal models accessible to the API credential. A returned model ID can be used as a query parameter when listing terminals or products for ordering. The listed server is `https://management-test.adyen.com/v3`; the caller needs **Management API—Terminal ordering read** or **Management API—Terminal ordering read and write**. See [[adyen]] and [[adyen-terminal-management]].

## Key takeaways

- The required string path parameter `companyId` identifies the company account. This GET reference specifies no query parameters or request body.
- The `200` response schema has optional `data`, an array of terminal-model objects whose `id` and `name` are both optional in the table. A listed model ID is a lookup/filter value; the response does not place an order, assign or board a device, prove inventory or establish that a model is currently available to this company in Live.
- The reference says Live requests to this endpoint have rate limits, but gives no numeric limit here. It lists `400` request, `401` authentication, `403` permission, `422` validation and `500` server errors. No default, pagination, idempotency contract, asynchronous state or lifecycle transition is specified.
- The long `200` JSON example lists named Verifone and Castles models. It illustrates a possible response, not a current order catalog, regional support matrix, device certification or deployment result.

## Detail locators

- Raw opening paragraphs, `## Servers` and `## Parameters > ### Path parameters`: purpose, caller roles, Live rate-limit notice, TEST server and company ID.
- Raw `## Responses > ### 200 Success`: optional `data`, `id` and `name` schema.
- Raw `## Responses > ### 400/401/403/422 Client Error` and `### 500 Server Error`: failure classes and problem fields.
- Raw `## Response examples > ### 200 Success`: illustrative model IDs and names.

## Related

- [[adyen-terminal-management]] — terminal ordering, fleet administration and operational boundaries.
- [[source-adyen-docs-point-of-sale-automating-terminal-management-order-terminals-api]] — separate ordering workflow and prerequisites.
- [[source-adyen-api-explorer-management-latest-get-terminals]] — separate terminal inventory list.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/terminalModels/2026-11-05|GET company terminal models, captured 2026-11-05]]