---
title: "List company account users | Adyen Management API v3"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/users"
raw_files:
  - "adyen/api-explorer/Management/latest/get/companies/(companyId)/users/2026-11-03.md"
tags: [adyen, management-api, company-accounts, users, customer-area]
---

## Overview

This [[adyen]] Management API reference, captured 2026-11-03, describes `GET /companies/{companyId}/users`, a paged list of users for a company account. Its listed server is `https://management-test.adyen.com/v3`. The calling API credential must have **Management API—Users read and write**, even though this operation is a GET. The returned user records are distinct from the caller's API credential. See [[adyen-customer-area-iam]] for the user-access context and [[adyen-api-access]] for API credential scope.

## Key takeaways

- The required `companyId` path string identifies the company account. Optional queries are `username` for partial or complete matching, `pageSize` (default 10, maximum 100), and `pageNumber` with no stated default. The page specifies no request body. [Raw: lines 16–29]
- The `200` response contains optional pagination `_links` and optional `data` array, with required `itemsTotal` and `pagesTotal`. Within each returned user object, `email`, user `id`, `roles`, `timeZoneCode`, and `username` are marked required; optional fields include `active`, apps, account groups, associated merchant accounts, and name. Nested required flags apply to an item or optional parent when present, not to the entire optional `data` array or `_links` object. [Raw: lines 31–66]
- The response describes listed account associations and roles, plus an `active` boolean. A list response is a captured read of user records; it does not demonstrate a particular user's working login, SSO/MFA enrollment, effective current access, API-key authority, or a completed account or payment operation. [Raw: lines 50–66]
- The reference lists `400` request interpretation, `401` authentication, `403` permission, `422` validation, and `500` server failures. Error bodies use problem-detail fields, including `requestId`; see the raw tables for exact requiredness. [Raw: lines 69–166]

## Detail locators

- Purpose, API credential role and TEST v3 server: raw lines 5–14.
- Company path and optional filters/pagination: raw lines 16–29.
- Response pagination and user-record fields: raw lines 31–66.
- Error categories and schemas: raw lines 69–166.

## Related

- [[adyen-customer-area-iam]] — human user and role context.
- [[adyen-api-access]] — separate API credential identity, roles and scope.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/users/2026-11-03|Management API company users list — captured 2026-11-03]]