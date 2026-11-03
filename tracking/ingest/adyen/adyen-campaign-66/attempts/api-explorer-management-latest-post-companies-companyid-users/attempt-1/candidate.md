---
title: "POST /companies/{companyId}/users — create a company user | Adyen"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/companies/(companyId)/users"
raw_files:
  - "adyen/api-explorer/Management/latest/post/companies/(companyId)/users/2026-11-03.md"
tags: [adyen, management-api, customer-area, users, sso, roles]
---

## Overview

This 2026-11-03-captured [[adyen]] Management API reference describes creating a user under the company account identified by required path `companyId`. The listed server is TEST `https://management-test.adyen.com/v3`, and the calling API credential needs **Management API—Users read and write**. The company-account path ID, the new user's username/email and the returned user ID are distinct identities. See [[adyen-customer-area-iam]]. [Raw: lines 5–21, 29–36, 116–123]

## Key takeaways

- The request-body table marks `email`, `name` and `username` required; `name` has a 1–80 character allowed length and required `firstName` and `lastName` children. It says `username` must be the same as `email`. The table does not separately state whole-body requiredness. [Raw: lines 24–36]
- Optional inputs are account-group IDs, associated merchant-account IDs, role names, a time-zone database name and `loginMethod` (`Email` or `SSO`). The stated condition for requesting SSO is that SSO is already configured with Adyen before creating the user. The account and role arrays are grants associated with this user, not identities of the calling API credential. [Raw: lines 27–35]
- A `200` reports request success and a user response. Its schema marks returned `email`, `id`, `roles`, `timeZoneCode` and `username` required, while `active`, account groups, associated merchant accounts, apps and `name` are optional. The example has `active: true`, but this does not guarantee that every created user is immediately active, has a working SSO/login session, or has a particular role/account entitlement. [Raw: lines 101–123, 225–253]
- The listed error cases are `400` request, `401` authentication, `403` permission, `422` validation and `500` server errors, each with a problem-body table. The page states no idempotency, retry, propagation or user-notification rule. It lists no live server. [Raw: lines 13–14, 126–223]

> [!warning] Contradiction
> The request table requires `username` to equal `email`, but all three request examples use `"username": "johnsmith"` with `"email": "john.smith@example.com"`. The response example repeats `johnsmith`. The examples do not resolve whether that mismatched input is valid. [Raw: lines 36, 40–100, 229–253]

> [!warning] Contradiction
> The listed TEST server is `/v3`, while the `200` response example's `_links.self.href` uses `/v1/companies/.../users/...`. The snapshot does not reconcile the version difference. [Raw: lines 13–14, 245–248]

## Detail locators

- Purpose, credential role, TEST server and company-account ID: raw lines 5–21.
- Request fields, SSO condition and username rule: raw lines 24–36.
- Three request examples and username/email mismatch: raw lines 38–100.
- `200` response-field requiredness: raw lines 101–123.
- Errors and problem-body schemas: raw lines 126–223.
- `200` example, optional active flag and `/v1` self link: raw lines 225–253.

## Related

- [[adyen-customer-area-iam]] — Customer Area user and SSO context
- [[adyen-api-access]] — separate web-service credential identity and permissions

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/companies/(companyId)/users/2026-11-03|Management API company-user creation — captured 2026-11-03]]