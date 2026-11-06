---
title: "Adyen Management API v3: list merchant terminal models"
type: source
date_ingested: 2026-11-06
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/terminalModels"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/terminalModels/2026-11-05.md"
tags: [adyen, management-api, terminal-management, terminal-models]
---

## Overview

This 2026-11-05-captured Management API reference describes `GET /merchants/{merchantId}/terminalModels`, a merchant-account-scoped lookup for payment terminal models accessible to the API credential. A returned model ID can be used as a query parameter when listing terminals or products for ordering. The listed server is `https://management-test.adyen.com/v3`; the caller needs **Management API—Terminal ordering read** or **Management API—Terminal ordering read and write**. See [[adyen]] and [[adyen-terminal-management]].

## Key takeaways

- The required string path parameter `merchantId` identifies the merchant account. This GET reference specifies no query parameters or request body.
- The `200` response schema marks `data` optional; it is an array of terminal-model objects whose `id` and `name` are each optional in the table. A `204` means successful processing with no additional content. Neither result places an order, assigns or boards a terminal, proves physical inventory or establishes current Live eligibility.
- The reference says Live requests to this endpoint have rate limits, without a numerical limit here. It lists `400` request, `401` authentication, `403` permission, `422` validation and `500` server errors. No default, pagination, idempotency behavior, asynchronous state or lifecycle transition is specified.
- The long `200` JSON example lists named Verifone and Castles models. It illustrates a possible response, not current availability for this merchant, a regional support matrix, device certification or a payment result.

## Detail locators

- Raw opening paragraphs, `## Servers` and `## Parameters > ### Path parameters`: purpose, ordering roles, Live rate-limit notice, TEST host and merchant ID.
- Raw `## Responses > ### 200 Success` and `### 204 Success`: optional model data and no-content outcome.
- Raw `## Responses > ### 400/401/403/422 Client Error` and `### 500 Server Error`: failure classes and problem fields.
- Raw `## Response examples > ### 200 Success`: illustrative model IDs and names.

## Related

- [[adyen-terminal-management]] — terminal ordering and fleet-administration routes.
- [[source-adyen-api-explorer-management-latest-get-companies-companyid-terminalmodels]] — separate company-scoped terminal-model lookup.
- [[source-adyen-docs-point-of-sale-automating-terminal-management-order-terminals-api]] — separate terminal-ordering workflow.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/terminalModels/2026-11-05|GET merchant terminal models, captured 2026-11-05]]