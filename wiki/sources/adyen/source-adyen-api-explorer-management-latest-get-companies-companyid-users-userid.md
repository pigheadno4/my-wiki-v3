---
title: "Adyen Management API v3: get company user details"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/users/(userId)"
raw_files:
  - "adyen/api-explorer/Management/latest/get/companies/(companyId)/users/(userId)/2026-11-03.md"
tags: [adyen, management-api, company-users, iam]
---

## Overview

This 2026-11-03-captured Management API v3 reference describes `GET /companies/{companyId}/users/{userId}`, a read of one user under the company account named by the path. The listed TEST server is `https://management-test.adyen.com/v3`; the API credential requires **Management API—Users read and write**. Both `companyId` and `userId` are required path identifiers. See [[adyen]] and [[adyen-customer-area-iam]].

## Key takeaways

- A successful `200` response requires the user's `email`, `id`, `roles`, `timeZoneCode` and `username` in its table. It may also include `active`, apps, account groups, associated merchant accounts, name and resource links. If the optional `name` object appears, `firstName` and `lastName` are marked required within it; if `_links` appears, `self` is marked required within that object. These response fields are not request inputs.
- `companyId` identifies a company account; `userId` identifies a user. `associatedMerchantAccounts`, `accountGroups`, `apps` and `roles` have different meanings. The returned `active` flag is a readback, not evidence of a successful login, factor enrollment, effective access to every listed account or any API credential's permissions.
- The reference lists `400`, `401` (authentication required), `403` (insufficient permissions), `422` (validation), and `500` errors with a common problem-body shape. This GET does not document user creation/update/deactivation, idempotency, propagation timing, asynchronous approval or any payment outcome. The dated TEST capture does not prove current live authorization.

## Detail locators

- Raw lines 5–22 → operation, required credential role, TEST v3 server and both path IDs.
- Raw lines 24–46 → `200` user fields, required versus optional response properties and nested objects.
- Raw lines 49–146 → error categories and problem-body fields. No response example is present in this capture.

## Related

- [[adyen-customer-area-iam]] — Customer Area user and role context.
- [[adyen-api-access]] — distinct web service API credential context.
- [[source-adyen-docs-account-users]] — separate Customer Area user-management guide.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/users/(userId)/2026-11-03|2026-11-03 user-detail endpoint reference]]