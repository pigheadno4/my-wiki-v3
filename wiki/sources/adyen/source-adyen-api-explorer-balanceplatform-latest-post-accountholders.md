---
title: "Adyen Balance Platform API v2: POST /accountHolders"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/post/accountHolders"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/post/accountHolders/2026-09-15.md"
tags: [adyen, balance-platform, account-holders, api, verification]
---

## Overview

This 2026-09-15 capture of the Balance Platform Configuration API `POST /accountHolders` reference describes creating an account holder linked to an existing legal entity. The page shows the test server at `https://balanceplatform-api-test.adyen.com/bcl/v2`; `latest` in the URL is a documentation route, not an independently verified current version or live endpoint. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The request schema marks `legalEntityId` required. `balancePlatform` is marked optional in the table but is required when the API credential covers multiple balance platforms. The page does not separately state whether the entire request body is required; the JSON example supplies `legalEntityId`.
- `capabilities` is an optional request map. `requested` asks for a capability; the response `allowed` field indicates permission following verification. `enabled: false` temporarily disables it. Requested levels may require additional checks and monitoring.
- The 200 response includes a required account-holder `id` and `legalEntityId`; capability verification may still be pending. Its example shows `status: active` while requested capabilities have `allowed: false` and `verificationStatus: pending`. Creation and active status alone do not establish usable capabilities, completed legal-entity verification, a balance account, funds, or payout.
- The response schema describes `active`, `suspended` (payouts blocked), and irreversibly `closed` account-holder states. A primary balance account is assigned by default only when the first balance account is created. The metadata description warns that omitting existing key-value pairs **during an update** deletes them; this POST does not itself document an update.
- Documented responses are 200, 400, 401, 403, 422, and 500. The 422 and 500 JSON examples mention payment-instrument operations rather than account-holder creation; treat them as generic examples, not endpoint-specific error conditions.

## Detail locators

- Request field conditions and nested contact details: pinned raw `## Parameters > ### Request body`, lines 14–39.
- Request JSON: `## Request examples > ### createAccountHolder`, lines 41–50.
- Response identity, capabilities, statuses, verification deadlines and primary balance account: `## Responses > ### 200 Success`, lines 53–115.
- Error schemas and example bodies: `## Responses`, lines 118–215, and `## Response examples`, lines 217–331.

## Related

- [[adyen-platforms]] — platform account-holder and verification context.
- [[source-adyen-docs-platforms-manage-account-holders]] — separate lifecycle guide; this API reference is limited to creation.
- [[source-adyen-docs-platforms-verification-overview-capabilities]] — separate capability verification guide.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/post/accountHolders/2026-09-15|Balance Platform POST /accountHolders snapshot]]
