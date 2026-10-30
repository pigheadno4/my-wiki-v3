---
title: "Adyen Balance Platform API v2: Create a payment instrument group"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/post/paymentInstrumentGroups"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/post/paymentInstrumentGroups/2026-09-15.md"
tags: [adyen, issuing, balance-platform, payment-instrument-groups, api]
---

## Overview

Captured API Explorer reference for `POST /paymentInstrumentGroups`, shown on the Balance Platform API test server at `https://balanceplatform-api-test.adyen.com/bcl/v2`. It creates a payment instrument group to associate payment instrument resources; a transaction rule can be applied to a group. The group belongs to a `balancePlatform`, not to an account holder, balance account, or individual card by virtue of this request alone. See [[adyen]], [[adyen-issuing]], and [[adyen-platforms]].

## Key takeaways

- The request-body table marks `balancePlatform` (the balance platform identifier) and `txVariant` as required properties. `description`, `properties`, and `reference` are optional. The page does not separately state whether the body itself is required, define permitted `txVariant` values, or specify a named role.
- A 200 response documents `balancePlatform` and `txVariant` as required response fields and `id` as optional in the schema, although the success example includes a group ID. It establishes a successful group-creation response, not attachment of a card, activation of a transaction rule, authorization of a payment, or movement of funds.
- Errors listed are 400 malformed/unreadable request, 401 authentication, 403 insufficient permissions, 422 validation, and 500 server failure. The generic 422 and 500 examples describe a payment-instrument change/creation, not this group-creation operation; do not reuse their detail or code as a group-specific contract.

## Detail locators

- Purpose and test server: pinned raw, lines 5–10.
- Request-body properties and example: `## Parameters` → `### Request body`, lines 12–21; `## Request examples`, lines 23–31.
- 200 response schema and example: `## Responses` → `### 200 Success`, lines 32–45; `## Response examples`, lines 147–158.
- Error schemas and examples: `## Responses`, lines 48–145; `## Response examples`, lines 160–225.

## Related

- [[adyen-issuing]] — card-program context.
- [[source-adyen-docs-issuing-authorisation-transaction-rules]] — transaction-rule scope and behavior; group creation alone does not apply a rule.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/post/paymentInstrumentGroups/2026-09-15|Captured POST /paymentInstrumentGroups API Explorer reference (2026-09-15)]]
