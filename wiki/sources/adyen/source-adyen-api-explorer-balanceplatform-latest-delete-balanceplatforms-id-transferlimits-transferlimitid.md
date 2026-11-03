---
title: "Adyen Balance Platform API DELETE /balancePlatforms/{id}/transferLimits/{transferLimitId} — delete a pending or scheduled limit"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/delete/balancePlatforms/(id)/transferLimits/(transferLimitId)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/delete/balancePlatforms/(id)/transferLimits/(transferLimitId)/2026-11-03.md"
tags: [adyen, business-accounts, balance-platform-api, transfer-limits]
---

## Overview

This 2026-11-03 Balance Platform API Explorer capture describes `DELETE /balancePlatforms/{id}/transferLimits/{transferLimitId}` for deleting a scheduled or pending **balance-platform** transfer limit. Both the balance platform `id` and the `transferLimitId` are required path strings. The listed server is `https://balanceplatform-api-test.adyen.com/bcl/v2`; this is a configuration operation in the [[adyen-business-accounts]] context.

## Key takeaways

- The reference expressly says an active limit cannot be deleted. It gives a 204 success response with no response-body fields; the documented operation is deletion of the identified eligible limit, not deletion of the balance platform or a balance-account-specific limit.
- The listed errors are 404 when a transfer limit cannot be found and 422 for a request validation error. Both error schemas describe optional problem fields and conditional nested validation details. The page does not specify which invalid state produces which error, a credential role, an SCA step, an idempotency rule, or a replacement/override operation.
- Deleting a pending or scheduled limit does not itself establish a change to an active limit, propagation timing to other limits or accounts, any transfer approval, booking, settlement, reversal or bank receipt. The captured reference lists only a test server; its `latest` URL is not proof of current live availability or version.

## Detail locators

- `## Servers` and `## Parameters > ### Path parameters` — test base and the two required IDs.
- `## Responses > ### 204 Success` — success semantics without a body.
- `## Responses > ### 404 Client Error` and `### 422 Client Error` — described failures and problem schemas.

## Related

- [[adyen]] — provider.
- [[adyen-business-accounts]] — product and transfer-limit context.
- [[source-adyen-docs-business-accounts-use-transfer-limits-balance-platform]] — separate platform-wide transfer-limits guide.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/delete/balancePlatforms/(id)/transferLimits/(transferLimitId)/2026-11-03|2026-11-03 captured API Explorer reference]]
