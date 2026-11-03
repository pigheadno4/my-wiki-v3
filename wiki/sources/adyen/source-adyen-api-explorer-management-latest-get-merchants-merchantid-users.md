---
title: "Adyen Management API v3: List merchant-associated users"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/users"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/users/2026-11-03.md"
tags: [adyen, management-api, customer-area, users, merchant-account]
---

## Overview

The captured [[adyen]] Management API v3 TEST `GET /merchants/{merchantId}/users` returns a list of users associated with the merchant account identified by the required path `merchantId`. It is a readback of user records, separate from creating a user, changing roles, or proving a working login or effective access. See [[adyen-customer-area-iam]] and [[adyen-api-access]].

## Key takeaways

- The API credential needs the `Management API—Users read and write` role. The captured server is `https://management-test.adyen.com/v3`. The path `merchantId` is required; optional query parameters are partial or full `username` filtering, `pageSize` (default 10, maximum 100), and `pageNumber`. The page states no `pageNumber` default.
- A 200 response optionally includes `data` user records and `_links` pagination references; `itemsTotal` and `pagesTotal` are marked required at the response level. Within optional `data`, user `email`, `id`, `roles`, `timeZoneCode`, and `username` are marked required on each user object; `active`, `apps`, `accountGroups`, and other details are optional. Within optional `_links`, `first`, `last`, and `self` are marked required, with `next`/`prev` conditional on page availability. Nested requiredness does not make the parent fields required.
- A 204 indicates successful processing with no content. The returned `active` flag, role names, and app list describe a user record at capture time; this endpoint does not prove actual authentication, SSO/MFA completion, current permissions, or a successful action.
- The page states no request body, mutation, idempotency, deletion, propagation, asynchronous review/approval, or payment outcome. Its `latest` URL and 2026-11-03 snapshot do not establish present availability.

## Detail locators

- Purpose, credential role and TEST v3 server: pinned raw lines 5–14.
- Path and query filters/pagination limits: pinned raw lines 16–29.
- 200 response fields and nested requiredness; 204: pinned raw lines 31–69.
- 400, 401, 403, 422, and 500 errors, including optional nested `invalidFields`: pinned raw lines 72–169. Generic error `requestId`/`pspReference` language is not evidence of a payment.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/users/2026-11-03|2026-11-03 pinned API Explorer snapshot]]
