---
title: "Adyen Management API v3: create a merchant user"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/post/merchants/(merchantId)/users"
raw_files:
  - "adyen/api-explorer/Management/latest/post/merchants/(merchantId)/users/2026-11-03.md"
tags: [adyen, management-api, merchant-users, customer-area, iam]
---

## Overview

This 2026-11-03 [[adyen]] Management API reference describes `POST /merchants/{merchantId}/users`, creating a user for the merchant account identified by required path string `merchantId`. The calling API credential needs `Management API—Users read and write`. The captured server is `https://management-test.adyen.com/v3`; no live server URL is supplied on this page. This creates a merchant user resource, distinct from an API credential and from proof of working login or effective permissions. [[adyen-customer-area-iam]]

## Key takeaways

- The request-body table marks `email`, `name` and `username` required. Required `name` has required `firstName` and `lastName` children and an allowed length of 1–80 characters. The table says `username` must be the same email address as `email`; the request examples conflict with that rule. Optional fields are `accountGroups`, `roles`, `timeZoneCode` and `loginMethod` (`Email` or `SSO`). SSO must already be configured with Adyen before creating an SSO user. The page does not declare a default login method, role or time zone.
- A `200` says the creation request succeeded. Its response table requires user `email`, `id`, `roles`, `timeZoneCode` and `username`; optional fields include `active`, `apps`, `accountGroups`, `name`, and `_links` with required `self` when `_links` is present. Required `firstName` and `lastName` are nested under optional response `name`. The returned user `id` differs from the merchant path ID. A sample `active: true` is illustrative, not proof of login or that every requested role is effective.
- The page also lists `204` success without content and `400`, `401`, `403`, `422` and `500` error schemas. It does not document an idempotency contract, duplicate-user behavior, propagation timing, deletion/reversal, approval workflow or account activation outcome for this POST. A user creation response is not payment or payout authorization.

> [!warning] Contradiction
> The request table requires `username` to equal `email`, but all three request examples set `username` to `johnsmith` while `email` is `john.smith@example.com`. The captured server is `/v3`, while the response example's `self.href` uses `/v1`. The snapshot does not reconcile either discrepancy; examples do not relax the stated username rule or establish the endpoint version for live use.

## Detail locators

- **Purpose, credential role and captured test server:** raw lines 5–14.
- **Path ID, request-body fields, conditional SSO and requiredness:** raw lines 16–35.
- **Three conflicting request examples:** raw lines 37–87.
- **200/204 response fields and nested optionality:** raw lines 88–113.
- **Error forms:** raw lines 116–213.
- **Illustrative active user and v1 self link:** raw lines 215–240.

## Related

- [[adyen-customer-area-iam]] — human user login and access context.
- [[adyen-api-access]] — distinct API credential role and account-scope context.
- [[adyen-account-structure]] — merchant-account scope.
- [[source-adyen-docs-account-user-roles]] — Customer Area user-role catalog.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/post/merchants/(merchantId)/users/2026-11-03|Management API v3 merchant-user POST — collected 2026-11-03]]