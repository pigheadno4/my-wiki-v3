---
title: "Adyen Balance Platform API v2: DELETE /balanceAccounts/{id}/transferLimits/{transferLimitId}"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/delete/balanceAccounts/(id)/transferLimits/(transferLimitId)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/delete/balanceAccounts/(id)/transferLimits/(transferLimitId)/2026-11-03.md"
tags: [adyen, balance-platform, business-accounts, transfer-limits, api]
---

## Overview

This 2026-11-03-captured Balance Platform API v2 reference documents deletion of a scheduled or pending transfer limit for a balance account. An active limit cannot be deleted through this endpoint. The captured server is the TEST base `https://balanceplatform-api-test.adyen.com/bcl/v2`; `latest` is a documentation route, not proof of live availability or caller eligibility. See [[adyen]] and [[adyen-business-accounts]].

## Key takeaways

- `DELETE /balanceAccounts/{id}/transferLimits/{transferLimitId}` requires two string path IDs: `id` identifies the balance account and `transferLimitId` identifies its transfer limit. The page documents no body, query fields, idempotency key, caller role, conditional input, default or numeric limit.
- The 204 response says the request succeeded and has no documented response body. The endpoint's own prose confines deletion to scheduled or pending limits and explicitly excludes active limits. The page does not identify a specific error status for an attempted active-limit deletion.
- The documented failures are 404 when one of the transfer limits could not be found and 422 for a request validation error. Their top-level response fields are optional; the three `invalidFields` child properties are required within each validation item if that optional array appears.
- The capture specifies no authentication mechanism, retry/reversal behavior, asynchronous confirmation, propagation time or version/conflict rules. A successful configuration deletion does not prove a transfer was cancelled, funds returned, a bank received money, or a specific account remains eligible.

## Detail locators

- Endpoint scope, TEST server, both required path IDs and bodyless 204: pinned raw lines 5–23.
- 404 and 422 descriptions and error-body schemas: `## Responses`, lines 26–61. The capture has no response examples.

## Related

- [[adyen-business-accounts]] — Business Account transfer-limit context.
- [[source-adyen-docs-business-accounts-use-transfer-limits-balance-accounts]] — separate guide for balance-account limits and lifecycle.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/delete/balanceAccounts/(id)/transferLimits/(transferLimitId)/2026-11-03|Balance Platform DELETE balance-account transfer limit snapshot]]