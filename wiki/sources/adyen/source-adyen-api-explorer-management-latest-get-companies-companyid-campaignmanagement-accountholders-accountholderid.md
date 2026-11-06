---
title: "Adyen Management API: List an account holder's donation campaigns"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Management/latest/get/companies/(companyId)/campaignManagement/accountHolders/(accountHolderId)"
raw_files:
  - "adyen/api-explorer/Management/latest/get/companies/(companyId)/campaignManagement/accountHolders/(accountHolderId)/2026-11-07.md"
tags: [adyen, management-api, giving, donation-campaigns, platforms]
---

## Overview

This 2026-11-07 Management API `latest` reference documents `GET /companies/{companyId}/campaignManagement/accountHolders/{accountHolderId}` on the listed TEST `https://management-test.adyen.com/v3` server. It reads a paginated list of donation campaigns associated with the account holder identified in the path, with an optional campaign-status filter. The required `companyId` identifies a company account; `accountHolderId` identifies an account holder, distinct from each campaign's Adyen-generated `id` and nonprofit cause `causeId`. See [[adyen]] and [[adyen-giving]].

## Key takeaways

- The API credential needs Campaign Management read or read and write. Optional `pageSize` defaults to 10 and has a maximum of 100; `pageNumber` selects a page; `status` filters by `inactive`, `active` or `ended`.
- A `200` means the list request succeeded. The response requires `itemsTotal` and `pagesTotal`; `_links` and `campaigns` are optional. Within a returned campaign, `id`, `name`, `nonprofitCause` and `status` are marked required; the nested in-person and online settings and most nonprofit metadata are optional. Do not infer that a listed campaign has processed a donation.
- The documented `503` says managing donation campaigns is temporarily impossible for this account, while donations themselves are unaffected. That service boundary is not a donation outcome or settlement report.

## Detail locators

- Purpose, roles, TEST server, required path IDs and pagination/status filters: raw lines 5–32.
- `200` pagination, campaign, account-holder, merchant/store, nonprofit and channel fields: raw lines 34–86.
- Error schemas for 400, 401, 403, 422, 500 and the specific 503 management-service condition: raw lines 89–200.

## Related

- [[adyen-giving]] — Giving campaign and donation flow.
- [[adyen-platforms]] — account-holder platform context.

## Raw Sources

- [[raw/adyen/api-explorer/Management/latest/get/companies/(companyId)/campaignManagement/accountHolders/(accountHolderId)/2026-11-07|Pinned account-holder donation campaign list reference (2026-11-07)]]
