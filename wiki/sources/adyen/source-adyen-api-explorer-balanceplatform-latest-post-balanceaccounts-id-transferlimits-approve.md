---
title: "Adyen Balance Platform API v2: approve pending balance-account transfer limits"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts/(id)/transferLimits/approve"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/post/balanceAccounts/(id)/transferLimits/approve/2026-11-03.md"
tags: [adyen, balance-platform, business-accounts, transfer-limits, sca, api]
---

## Overview

This 2026-11-03 API Explorer capture describes `POST /balanceAccounts/{id}/transferLimits/approve` on the Balance Platform API v2 **TEST** server (`https://balanceplatform-api-test.adyen.com/bcl/v2`). Its stated purpose is to approve transfer limits pending Strong Customer Authentication (SCA). The `latest` URL segment does not prove current version or live availability. See [[adyen]] and [[adyen-business-accounts]].

## Key takeaways

- Required path `id` identifies the balance account. The header table lists optional `WWW-Authenticate` for SCA authentication. The request-body table marks `transferLimitIds`, an array of IDs of pending transfer limits to approve, as required; the page does not separately state whole-body requiredness, an array size, or a batch atomicity rule. Its two-ID JSON example illustrates the shape, not a limit.
- `204` says the request succeeded and documents no response body or returned limit state. `401` requires SCA and says the client must resolve the provided challenge; the capture does not specify the challenge exchange, credential role, or an idempotency contract. `404` means one of the transfer limits could not be found; `422` denotes request validation error. The error schemas list optional problem fields and optional `invalidFields` entries whose present objects require `message`, `name`, and `value`.
- A successful approval request does not itself show when a limit becomes active or enforced, which limit IDs succeeded individually, or whether any transfer was approved, booked, settled or received by a bank. This endpoint capture gives no propagation, reversal, deletion, conflict/version or failure-retry rule. Consult the separate [[source-adyen-docs-business-accounts-use-transfer-limits|transfer-limits guide]] for broader dated context.

## Detail locators

- Purpose, TEST base URL, path and header parameters: raw lines 5–23.
- Request-body table and illustrative JSON: raw lines 26–41.
- `204` and `401`, `404`, `422` error meanings and schemas: raw lines 42–102.

## Related

- [[adyen-business-accounts]] — product context.
- [[source-adyen-docs-business-accounts-use-transfer-limits]] — broader transfer-limit guide.
- [[source-adyen-docs-business-accounts-how-sca-works]] — separate SCA guide.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/post/balanceAccounts/(id)/transferLimits/approve/2026-11-03|Transfer-limit approval API Explorer capture]]