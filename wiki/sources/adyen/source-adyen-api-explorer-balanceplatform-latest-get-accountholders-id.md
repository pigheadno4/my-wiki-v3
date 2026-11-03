---
title: "Adyen Balance Platform API v2: GET /accountHolders/{id}"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/accountHolders/(id)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/accountHolders/(id)/2026-11-02.md"
tags: [adyen, balance-platform, account-holders, api, verification]
---

## Overview

This 2026-11-02 capture of the Balance Platform API `GET /accountHolders/{id}` reference returns an account holder by its unique path ID. The captured server is the TEST `/bcl/v2` endpoint. The `latest` URL is a documentation route, not proof of a currently available live version or account eligibility. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- The only listed input is the required string path parameter `id`, the account-holder identifier. The page lists no request body or query parameter. Its 200 response schema marks the account-holder `id` and associated `legalEntityId` required; the latter identifies the legal entity against which Adyen performs verification. The optional `balancePlatform` response-field description also says it is required **in the request** if credentials can access multiple balance platforms, although this GET parameter list exposes no such input; do not infer a GET request parameter from that response-field text.
- Optional `capabilities` maps capability names to settings. `requested` records a request; `allowed` indicates permission after verification, while `enabled: false` indicates temporary disablement. `verificationStatus` can be `pending`, `invalid`, `valid`, or `rejected`; supporting transfer-instrument capability entries have their own ID and status. Read these fields separately. The 200 example has `status: active` but requested capabilities are `allowed: false` and `pending`, so an active holder is not evidence that those capabilities are usable.
- The optional account-holder `status` description defines `active`, `suspended` (payouts blocked), and `closed` (holder and all capabilities permanently disabled; final). The optional `primaryBalanceAccount` defaults to the first balance account created for the holder, and can be reassigned by PATCH. A returned account-holder ID or primary-balance-account ID does not establish a balance, payment, transfer, payout, or bank receipt.
- The 200 response also describes optional contact details, description, metadata, migrated Classic account-holder code, merchant reference, time zone, and verification deadlines. The metadata deletion warning applies **during an update**, not to this read. `timeZone` defaults to the balance platform's time zone when unset. See the raw schema for nested field conditions and limits.
- Documented response classes are 200, 400, 401, 403, 422, and 500. The generic 422 and 500 example payloads mention payment-instrument changes/creation; they do not establish those operations or failure conditions for this GET. The page documents no GET idempotency key, specific caller role, state-propagation timing, or financial outcome.

## Detail locators

- TEST server and required path ID: pinned raw lines 5–17 (`## Servers`, `## Parameters > ### Path parameters`).
- 200 schema, including identities, capability levels/settings/statuses, supporting transfer instruments, nested contact details, status, defaults and verification deadlines: pinned raw lines 19–83 (`## Responses > ### 200 Success`).
- Error response schemas: pinned raw lines 86–183 (`## Responses`); example payloads, including the unrelated payment-instrument wording: lines 185–300 (`## Response examples`).

## Related

- [[adyen-platforms]] — platform account-holder and verification context.
- [[source-adyen-api-explorer-balanceplatform-latest-post-accountholders]] — separate creation reference captured 2026-09-15.
- [[source-adyen-docs-platforms-account-holder-status]] — separate status guide; use its dated context when reasoning about status propagation.
- [[source-adyen-docs-platforms-verification-overview-capabilities]] — separate capability-verification guide.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/accountHolders/(id)/2026-11-02|Balance Platform GET /accountHolders/{id} snapshot]]