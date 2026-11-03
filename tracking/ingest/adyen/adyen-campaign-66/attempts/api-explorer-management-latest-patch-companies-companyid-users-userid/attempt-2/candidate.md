---
title: "Adyen Management API: update company user details"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/patch/companies/(companyId)/users/(userId)"
raw_files:
  - "adyen/api-explorer/Management/latest/patch/companies/(companyId)/users/(userId)/2026-11-03.md"
tags: [adyen, management-api, users, api-access]
---

## Overview

This 2026-11-03 Management API reference documents `PATCH /companies/{companyId}/users/{userId}`, which updates details of a user under the company account identified in the path. The calling API credential needs the `Management API—Users read and write` role. The listed server is TEST v3. A successful user update does not by itself prove login, account or payment access, merchant activation, or financial outcomes. [[adyen]] [[adyen-customer-area-iam]] [[adyen-account-structure]] [[adyen-api-access]]

## Key takeaways

- Both `companyId` and `userId` are required string path identifiers (raw lines 16–22).
- The request-body table lists optional `accountGroups`, `active`, `associatedMerchantAccounts`, `email`, `loginMethod`, `name`, `roles`, and `timeZoneCode`; `name.firstName` and `name.lastName` are also optional. `loginMethod` values are `Email` and `SSO`; the text requires SSO configuration with Adyen before using SSO (raw lines 25–37). No defaults or limits are specified.
- In the 200 response, `email`, `id`, `roles`, `timeZoneCode`, and `username` are marked required. `_links` is optional, with required `self` only inside a present `_links`; `name` is optional, with required first and last names only inside a present `name`. `active`, `apps`, account-group and merchant associations are optional (raw lines 39–61).

## Detail locators

- Purpose, credential role, TEST v3 server, path parameters, and request schema: raw lines 5–37.
- 200 user-response schema: raw lines 39–61.
- 400 request, 401 authentication, 403 permission, 422 validation, and 500 server-error schemas: raw lines 64–161. No response example is supplied.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/patch/companies/(companyId)/users/(userId)/2026-11-03|Management API PATCH company user, captured 2026-11-03]]
