---
title: "PATCH /merchants/{merchantId}/users/{userId} — Update a user | Adyen"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/merchants/(merchantId)/users/(userId)"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/users/(userId)/2026-11-03.md"
tags: [adyen, management-api, customer-area, users, iam]
---

## Overview

This 2026-11-03 Management API v3 reference describes `PATCH /merchants/{merchantId}/users/{userId}` on the listed `https://management-test.adyen.com/v3` server. It updates details of the user identified by required `userId` under required merchant `merchantId`. The caller's API credential needs `Management API—Users read and write`. A merchant user is distinct from the API credential making the request. See [[adyen]], [[adyen-customer-area-iam]] and [[adyen-api-access]].

## Key takeaways

- Every listed request-body field is optional: `accountGroups`, `active`, `email`, `loginMethod`, `name` with optional first/last names, `roles`, and `timeZoneCode`. The page does not specify a whole-body requiredness rule, default values, or whether omitted fields remain unchanged.
- `active: true` requests an active user; `false` requests inactive. `loginMethod` can be `Email` or `SSO`; the page says SSO must already be configured with Adyen before creating the user. That wording is a stated SSO prerequisite, not evidence that this PATCH enrolls a user in SSO or completes login.
- A `200` response says the request succeeded and its schema includes user `id`, `username`, `email`, `roles`, `timeZoneCode`, optional `active`, `accountGroups`, `apps`, `name`, and a self link. A separate `204` success has no additional content. Returned roles or an active flag are API readback, not proof of effective access, an authenticated session, or a completed SSO login.
- The reference lists `400`, `401` authentication required, `403` insufficient permissions, `422` validation error, and `500`. It gives no idempotency, propagation timing, asynchronous approval, or conflict/version semantics for this update. No live server is listed in the snapshot.

## Detail locators

- Endpoint purpose, credential role and TEST v3 server: raw lines 5–14.
- Required path IDs and optional request-body fields, including `active`, `loginMethod` and SSO wording: raw lines 16–36.
- `200` response fields and `204` status: raw lines 38–63.
- Error descriptions and repeated response schemas: raw lines 66–163.

## Related

- [[source-adyen-docs-account-users]] — Customer Area user-management guidance.
- [[source-adyen-docs-account-single-sign-on-set-up-sso]] — SSO setup guidance.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/merchants/(merchantId)/users/(userId)/2026-11-03|Pinned Adyen merchant-user update reference (2026-11-03)]]
