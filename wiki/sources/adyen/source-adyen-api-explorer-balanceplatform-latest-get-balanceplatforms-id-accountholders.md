---
title: "Adyen Balance Platform API v2: GET /balancePlatforms/{id}/accountHolders"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balancePlatforms/(id)/accountHolders"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/balancePlatforms/(id)/accountHolders/2026-11-02.md"
tags: [adyen, balance-platform, account-holders, api, pagination]
---

## Overview

This 2026-11-02 capture of the Balance Platform API v2 `GET /balancePlatforms/{id}/accountHolders` reference describes listing account holders belonging to one balance platform. The captured server is `https://balanceplatform-api-test.adyen.com/bcl/v2`; `latest` is the documentation route and does not establish the current live version or account eligibility. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The balance-platform `id` is the required **path** parameter. Optional query parameters are `limit` (10 items by default, maximum 100) and `offset` (items to skip). The page shows no request body or idempotency contract for this read operation.
- A 200 response returns an `accountHolders` array and required `hasNext` and `hasPrevious` pagination flags. Each listed account holder has a required `id` and `legalEntityId` in the response schema; optional fields include its `balancePlatform`, reference, status, primary balance account, capabilities, and verification deadlines. These are resource identifiers and reported state, not evidence of a payment or funds movement.
- Capability `requested` is distinct from `allowed`, which reports permission after successful verification; `enabled: false` denotes temporary disablement. Verification can be pending, invalid, valid, or rejected. The account-holder `status` description distinguishes active, suspended (payouts blocked), and permanently closed. A listed `active` holder alone does not prove any specific capability is allowed or that a payout occurred.
- The response table's optional `balancePlatform` field description says it is required **in the request** when credentials span multiple platforms. This GET's parameter table lists only path `id` and query `limit`/`offset`; do not infer an additional request field from that response-field description.
- Documented errors are 400, 401 (authentication required), 403 (insufficient permissions), 422, and 500. The 422 and 500 JSON examples discuss payment-instrument operations unrelated to this list endpoint; they do not establish endpoint-specific failure conditions.

## Detail locators

- Purpose, captured test server, path and pagination parameters: pinned raw lines 5–26.
- 200 response fields, holder/legal-entity IDs, capability and lifecycle descriptions, and pagination flags: pinned raw lines 28–68.
- Error schemas and illustrative response bodies: pinned raw lines 71–270.

## Related

- [[adyen-platforms]] — platform account-holder and verification context.
- [[source-adyen-docs-platforms-manage-account-holders]] — separate account-holder management guide.
- [[source-adyen-api-explorer-balanceplatform-latest-post-accountholders]] — separate account-holder creation endpoint.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/balancePlatforms/(id)/accountHolders/2026-11-02|Balance Platform account-holder list snapshot]]