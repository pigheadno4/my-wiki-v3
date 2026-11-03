---
title: "Balance Platform API: Delete a recurring top-up configuration"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/delete/balanceAccounts/(balanceAccountId)/recurringTopUps/(topUpId)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/delete/balanceAccounts/(balanceAccountId)/recurringTopUps/(topUpId)/2026-11-02.md"
tags: [adyen, balance-platform, recurring-top-ups, api]
---

## Overview

This captured Balance Platform API v2 `DELETE /balanceAccounts/{balanceAccountId}/recurringTopUps/{topUpId}` reference deletes the identified recurring top-up configuration from a balance account. The only listed server is `https://balanceplatform-api-test.adyen.com/bcl/v2`. The action concerns configuration, not a direct-debit request, credited balance or completed funds transfer. [[adyen]] [[adyen-issuing]]

## Key takeaways

- Both path identifiers are required: `balanceAccountId` identifies the balance account and `topUpId` identifies the recurring top-up configuration to delete. The reference specifies no query parameters or request body. See **Parameters**, lines 14–20.
- The documented success is HTTP 204: the request was successfully processed with no additional content. It returns no resource fields, amount or transfer status. The page does not specify when deletion propagates to scheduling or how an already initiated direct debit is affected; do not treat 204 as a reversal or evidence of a booked debit/credit. See **204 Success**, lines 22–25.
- Listed errors are 400 request problem, 401 authentication required, 403 insufficient permissions, 404 recurring top-up not found, 422 validation error and 500 server failure. The error-body fields are mostly optional; the nested invalid-field properties are required only when that optional array appears. The 404 example instead says a balance account was not found, and the 422 example refers to a sweep route; those examples do not redefine the endpoint's stated deletion target. See **Responses** and **Response examples**.
- This is a 2026-11-02 snapshot of the TEST server. The `latest` URL does not establish live availability, caller-specific permission, or account eligibility. The endpoint says nothing about idempotent repeat deletion, asynchronous outcome, reversal, or version conflict.

## Detail locators

- **Parameters**, lines 14–20: required balance account and top-up path IDs.
- **Responses**, lines 22–139: bodyless 204 and error statuses/schema.
- **Response examples**, lines 141–223: illustrative errors, including mismatched 404/422 details.

## Related

- [[adyen-issuing]] — recurring balance-account top-up context.
- [Manage recurring top-ups](https://docs.adyen.com/issuing/add-manage-funds/top-ups/manage-recurring-top-ups) — guide linked by the captured API reference; not used as evidence here.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/delete/balanceAccounts/(balanceAccountId)/recurringTopUps/(topUpId)/2026-11-02|Captured recurring top-up deletion API reference (2026-11-02)]]
