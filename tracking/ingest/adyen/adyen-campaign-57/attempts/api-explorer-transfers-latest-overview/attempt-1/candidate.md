---
title: "Adyen Transfers API v4 overview"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/transfers/latest/overview"
raw_files:
  - "adyen/api-explorer/transfers/latest/overview/2026-09-15.md"
tags: [adyen, transfers-api, platforms, payouts, balance-platform]
---

## Overview

Captured API Explorer overview headed **Transfers API v4**. It presents a cross-product endpoint catalog for payouts to transfer instruments, third-party sends for users with business bank accounts, grant-offer payouts, transaction queries, and outstanding grant balances. Versions 1 and 2 are stated to be deprecated; the page directs new implementations to the latest version. This is an overview and route catalog, not an endpoint request/response schema. See [[adyen]], [[adyen-platforms]], [[adyen-payouts]], [[adyen-business-accounts]], and [[adyen-capital]].

## Key takeaways

- Each Transfers API request must use an API key in the `X-API-Key` header. The page distinguishes generation in Customer Area for Platforms or Marketplace setup from Balance Platform Customer Area for Issuing. It also says an additional API-credential role is needed and transfers must be enabled for the **source balance account**, with Adyen-contact setup of roles and permissions. It does not name the role or establish that any account is enabled.
- Endpoint versioning uses a `vXX` URL suffix. The shown test base is `https://balanceplatform-api-test.adyen.com/btl/v4`; the separate going-live passage requires a live Customer Area key and identifies `https://balanceplatform-api-live.adyen.com/btl/v4`. These are documented environments, not evidence of current eligibility or a live operation.
- The catalog routes to GET/POST grants, GET transactions, GET/POST transfers, transfer approval/cancellation/returns, and POST cashouts. A listed method and short summary do not establish required fields, approval conditions, response codes, status transitions, settlement or bank receipt. Follow the exact endpoint reference and relevant product guide for those claims.

## Detail locators

- Version/deprecation, use cases, key and role prerequisites, and environment: pinned raw lines 5–41.
- Endpoint catalog: `## Endpoints` → `### General`, lines 43–59.

## Related

- [[adyen-platform-internal-transfers]] — internal balance-account movement is one narrower transfer context.
- [[adyen-api-access]] — API credential context.

## Raw Sources

- [[raw/adyen/api-explorer/transfers/latest/overview/2026-09-15|Captured Transfers API v4 overview (2026-09-15)]]
