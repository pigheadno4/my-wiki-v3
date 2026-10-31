---
title: "Adyen deprecated POS Terminal Management API v1: list stores under an account"
type: source
date_ingested: 2026-10-31
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/postfmapi/latest/post/getStoresUnderAccount"
raw_files:
  - "adyen/api-explorer/postfmapi/latest/post/getStoresUnderAccount/2026-09-15.md"
tags: [adyen, point-of-sale, stores, terminal-management, deprecated-api]
---

## Overview

This 2026-09-15-captured API Explorer reference documents `POST /getStoresUnderAccount` on the TEST POS Terminal Management API v1 server (`https://postfmapi-test.adyen.com/postfmapi/terminal/v1`). It lists stores associated with a company account or, when narrowed, a merchant account, including each store's status. The page states that this API was deprecated from January 1, 2025 and support stopped April 1, 2025; it directs fleet-management automation to the Management API.

## Key takeaways

- The request requires `companyAccount`. With only that field, the list spans stores of all merchant accounts associated with the company account. Optional `merchantAccount` narrows the list to that merchant's stores. The two request examples illustrate these scopes.
- Each returned store may include its `merchantAccountCode`, address, description, assigned-terminal ID list (`inStoreTerminals`), and status; `store` is the required code within a store object. The status values are `PreActive`, `Active`, `Inactive`, `InactiveWithModifications`, and `Closed`. The schema says an Active store can process payments and an inactive-with-modifications store can still support modifications such as refunds. These store-level descriptions and assigned-terminal IDs do not establish an individual terminal's boarding, configuration, connectivity, or completed payment.
- A 200 says the lookup succeeded and the examples return one Active store. That illustrative row does not prove any account's present store inventory or LIVE readiness. The page also lists 400, 401, 403, 422 and 500 errors, without naming a specific credential role.

## Detail locators

- Operation, deprecation notice and TEST v1 server: raw lines 5–12.
- Company-versus-merchant request scope and examples: raw lines 16–37.
- Store response fields/status values and errors: raw lines 38–123.
- Illustrative success and generic error examples: raw lines 125–215.

## Related

- [[adyen]] — provider.
- [[adyen-terminal-management]] — current fleet-management route and operational boundaries.

## Raw Sources

- [[raw/adyen/api-explorer/postfmapi/latest/post/getStoresUnderAccount/2026-09-15|POS Terminal Management API v1 POST /getStoresUnderAccount (captured 2026-09-15)]]
