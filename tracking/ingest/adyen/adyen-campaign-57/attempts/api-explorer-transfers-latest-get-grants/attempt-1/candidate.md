---
title: "Adyen Transfers API GET /grants — grant list and balances"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/transfers/latest/get/grants"
raw_files:
  - "adyen/api-explorer/transfers/latest/get/grants/2026-09-15.md"
tags: [adyen, transfers-api, capital, grants, balances]
---

## Overview

This 2026-09-15 Transfers API Explorer capture documents `GET /grants` on the `/btl/v4` test server. Its body says it returns a list of grants with status and outstanding balances for [[adyen-capital]]. The only listed query parameter, `counterpartyAccountHolderId`, is optional. The page title says “Get a capital account,” but the path, description and response schema describe a grant list; a grant account is a separate identifier within each grant.

## Key takeaways

- The 200 response marks the `grants` array required. Within each grant, `balances`, `grantAccountId`, `grantOfferId`, `id` and `status` are required. The grant reference, grant account and selected grant offer have different IDs. Optional `counterparty` fields distinguish a receiving account holder, its balance account and a transfer instrument belonging to that holder's legal entity.
- The grant's optional `amount` has minor-unit currency/value fields when present. Required `balances` has currency, fee, principal and total fields; total is described as principal plus fee. Optional fee and repayment objects have nested required fields when present. The status enum is `Pending`, `Active`, `Repaid`, `WrittenOff`, `Failed` and `Revoked`; this page does not define their transitions.
- The `grants` array row describes “the unique identifier of the grant” despite being typed as an array of objects. The 404 label says “The payment was not found” on this grant endpoint. Neither phrase supplies a grant-list cardinality guarantee or a grant-specific not-found condition.
- This read contract lists 400, 401, 403, 404, 422 and 500 responses, but no named permission role or response examples. A successful read does not establish a new offer, accepted grant, approved financing, actual disbursement, booked repayment, payout or bank receipt. The capture provides no pagination, deletion procedure, live host or current `latest` version evidence.

## Detail locators

- `## Servers` and `## Parameters` → captured test base URL and optional holder filter.
- `## Responses` → 200 grant array, IDs, balances, optional counterparty and repayment fields, status enum and error schemas.

## Related

- [[adyen]] — provider.
- [[adyen-capital]] — financing, grant and offer context.
- [[source-adyen-docs-capital-get-grant-balances]] — separate Capital guide for grant and aggregate grant-account reads.

## Raw Sources

- [[raw/adyen/api-explorer/transfers/latest/get/grants/2026-09-15|2026-09-15 captured API Explorer reference]]
