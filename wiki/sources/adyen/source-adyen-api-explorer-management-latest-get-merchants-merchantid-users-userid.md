---
title: "Adyen Management API v3: Get merchant user details"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/merchants/(merchantId)/users/(userId)"
raw_files:
  - "adyen/api-explorer/Management/latest/get/merchants/(merchantId)/users/(userId)/2026-11-03.md"
tags: [adyen, management-api, users, access-control]
---

## Overview

This 2026-11-03-captured Management API v3 reference describes `GET /merchants/{merchantId}/users/{userId}`, a read of user details for the merchant and user IDs in the path. The listed server is TEST `https://management-test.adyen.com/v3`. The `latest` URL and TEST server do not establish current Live availability or caller access. See [[adyen]], [[adyen-customer-area-iam]] and [[adyen-api-access]].

## Key takeaways

- The calling API credential must have `Management API—Users read and write`. Both string path IDs are required: `merchantId` identifies the merchant and `userId` identifies the user. The captured page specifies no query parameters, request body, default, numeric rate limit or idempotency behavior.
- A 200 says the request succeeded. The response requires user `email`, `id`, `roles` (the **user's** roles), `timeZoneCode` and `username`. Optional fields are `active`, `apps`, `accountGroups`, `name` and resource `_links`. If `name` is present, its `firstName` and `lastName` are marked required; if `_links` is present, `self` is marked required. A separate 204 says the request was processed without additional content.
- The caller's credential role is separate from any roles listed on the returned user. An optional `active` flag or app list is readback, not proof that a login succeeds, an app is reachable, or permissions are effective in another account. This GET does not create, activate, deactivate or modify a user or credential.
- Listed failures are 400, 401, 403, 422 and 500. The page does not describe deletion, propagation, asynchronous approval, reversal or version-conflict behavior for this read, and the user record does not establish merchant processing eligibility or a payment outcome.

## Detail locators

- Purpose, caller role, TEST server and required path IDs: pinned raw lines 5–22.
- 200 field requiredness and optional nested objects: lines 24–45; 204 no-content response: lines 48–49.
- Error descriptions and problem fields: lines 52–149.

## Related

- [[adyen-customer-area-iam]] — user access context.
- [[adyen-api-access]] — separate API credential scope and permissions.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/merchants/(merchantId)/users/(userId)/2026-11-03|Merchant user details GET snapshot]]
