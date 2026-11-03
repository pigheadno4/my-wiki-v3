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
- The API page labels `202 Success` and says to check the actual response code for request status; it gives no success body or completion timing. The separate [[source-adyen-docs-issuing-manage-network-tokens|Issuing management guide]] says HTTP 202 means accepted for asynchronous processing and directs the caller to webhooks for the final result (guide raw lines 332–334). Acceptance alone does not prove the requested status took effect, token usability, or card authorization, capture, booking, settlement or receipt. The API page specifies no rollback or reversal path; closing is explicitly final.
- Documented errors are 401 authentication required, 403 insufficient permissions, 422 request validation error, and 500 server processing failure. Their shared problem schema includes required `detail`, `errorCode`, `status`, `title`, and `type`, with optional `instance`, `invalidFields`, `requestId`, and `response`. The generic 422 and 500 JSON examples mention changing a payment instrument's balance account and creating a payment instrument; they are not network-token transition examples. No specific role, authentication method, approval or activation workflow is given in this API reference.

> [!warning] Contradiction
> This API reference marks request-body `status` optional (pinned raw line 23), while [[source-adyen-docs-issuing-manage-network-tokens|the Issuing guide]] marks it required for PATCH (guide raw lines 304–316). This API operation is `/networkTokens/{networkTokenId}` (pinned raw line 5), matching the guide's linked operation (guide raw line 306), but the guide's curl sample uses `/paymentInstruments/{id}/networkTokens/{networkTokenId}` (guide raw lines 320–329). These sources do not resolve the requiredness or sample-path discrepancies.

## Detail locators

- Purpose, TEST server, path ID and request-body status values: pinned raw lines 5–23.
- `202` wording and error response schemas: pinned raw lines 25–108; separate guide's asynchronous-result instructions: guide raw lines 332–334.
- Generic error examples and their payment-instrument wording: pinned raw lines 110–164.
- Guide PATCH requiredness and path conflict: guide raw lines 304–329.

## Related

- [[adyen-issuing]] — issued-card and network-token context.
- [[source-adyen-docs-issuing-manage-network-tokens]] — separate Issuing guide for status transitions and asynchronous webhook confirmation; see contradiction above.
- [[source-adyen-api-explorer-balanceplatform-latest-get-paymentinstruments-id-networktokens]] — separate captured API reference for listing a payment instrument's network tokens.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/patch/networkTokens/(networkTokenId)/2026-11-03|Balance Platform PATCH network-token snapshot]]