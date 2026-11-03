---
title: "Adyen Balance Platform API v2: PATCH network-token status"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/networkTokens/(networkTokenId)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/patch/networkTokens/(networkTokenId)/2026-11-03.md"
tags: [adyen, balance-platform, issuing, network-tokens, api]
---

## Overview

This 2026-11-03 Balance Platform API reference documents `PATCH /networkTokens/{networkTokenId}` to update a network token's status. Its captured server is the TEST endpoint `https://balanceplatform-api-test.adyen.com/bcl/v2`; `latest` is the documentation route, not evidence of current live availability or account eligibility. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- The required string path parameter `networkTokenId` identifies the network token, not a payment instrument or transaction. The request-body table marks `status` optional and lists `active`, `suspended`, and `closed`; `closed` is final and cannot be changed. The snapshot shows no other body field, conditional input, default, limit, query parameter, or idempotency contract.
- The page labels `202 Success` and says to check the actual response code for request status. It provides no success response schema or example. A `202` response alone does not prove that the requested token status has taken effect or that any card payment was authorized, captured, booked, settled, or received. The page does not specify completion timing, propagation, rollback, or a reversal path; closing is explicitly final.
- Documented errors are 401 authentication required, 403 insufficient permissions, 422 request validation error, and 500 server processing failure. Their shared problem schema includes required `detail`, `errorCode`, `status`, `title`, and `type`, with optional `instance`, `invalidFields`, `requestId`, and `response`. The generic 422 and 500 JSON examples mention changing a payment instrument's balance account and creating a payment instrument; they are not network-token transition examples. No specific role, authentication method, approval or activation workflow is given here.

## Detail locators

- Purpose, TEST server, path ID and request-body status values: pinned raw lines 5–23.
- `202` wording and error response schemas: pinned raw lines 25–108.
- Generic error examples and their payment-instrument wording: pinned raw lines 110–164.

## Related

- [[adyen-issuing]] — issued-card and network-token context.
- [[source-adyen-api-explorer-balanceplatform-latest-get-paymentinstruments-id-networktokens]] — separate captured API reference for listing a payment instrument's network tokens.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/patch/networkTokens/(networkTokenId)/2026-11-03|Balance Platform PATCH network-token snapshot]]