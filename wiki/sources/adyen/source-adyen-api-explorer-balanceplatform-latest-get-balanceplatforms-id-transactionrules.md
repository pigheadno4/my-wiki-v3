---
title: "Adyen Balance Platform API v2: GET /balancePlatforms/{id}/transactionRules"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balancePlatforms/(id)/transactionRules"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/balancePlatforms/(id)/transactionRules/2026-11-02.md"
tags: [adyen, balance-platform, issuing, transaction-rules, api]
---

## Overview

This 2026-11-02-captured Balance Platform API v2 reference describes `GET /balancePlatforms/{id}/transactionRules`: it returns a list of transaction rules associated with the balance platform named by the required path `id`. The only server shown is the TEST base `https://balanceplatform-api-test.adyen.com/bcl/v2`. The `latest` documentation route does not establish live deployment, current access or a platform's eligibility. See [[adyen]], [[adyen-issuing]] and [[adyen-platforms]].

## Key takeaways

- The 200 response table marks the `transactionRules` array optional. Within a listed rule object it marks `description`, `entityKey`, `interval`, `reference`, `ruleRestrictions` and `type` required, while `id`, `status` and many other fields are marked optional. This is a response schema, not a GET request body. The page lists no query parameters, pagination contract or request-body fields.
- A rule's `entityKey` identifies its scope by `entityType` and `entityReference`; those child fields are individually marked optional. The listed resource types are balance platform, payment-instrument group, account holder, balance account and payment instrument. `requestType` defaults to `authorization` when omitted and also lists `authentication`, `tokenization` and `bankTransfer`; do not read the list as card authorization alone.
- Rule types are `blockList`, `maxUsage`, `velocity` and `bypass`. The table describes `aggregationLevel` for velocity/maxUsage and its payment-instrument default; `bypass` calls for `overridesRule` and empty `ruleRestrictions`. `interval.type` is marked required within `interval`; rolling/sliding duration is conditionally required and capped at 90 days or equivalent. `outcomeType` defaults to `hardBlock`; `scoreBased` requires a score from -100 to 100 and is disallowed for bank transfers, while `enforceSCA` is limited to authentication.
- The response schema describes `startDate`, `endDate` and active/inactive `status`, including creation-time wording. These describe rule evaluation state; this GET does not create, activate, delete or execute a rule. A 200 list response is no proof that a specific rule applied, an authentication or authorization succeeded, or funds moved. The page documents 400, 401, 403, 422 and 500 responses; its generic 422 and 500 JSON examples concern payment-instrument operations and do not establish this list endpoint's specific failure conditions.

## Detail locators

- Endpoint, TEST server, required path `id` and 200 optional list parent: pinned raw lines 5–27.
- Rule identity, hierarchy, interval/defaults, outcomes, restrictions, lifecycle fields and types: `## Responses > ### 200 Success`, lines 28–76. The condition rows are response fields, not GET inputs.
- Error response schemas: `## Responses`, lines 79–176. Generic error examples, including payment-instrument-specific 422/500 text: `## Response examples`, lines 178–244.

## Related

- [[adyen-issuing]] — issuing transaction-rule context and source routes.
- [[source-adyen-api-explorer-balanceplatform-latest-post-transactionrules]] — separate 2026-09-15 create-rule contract.
- [[source-adyen-docs-issuing-authorisation-transaction-rules-create-and-manage]] — separate lifecycle guide with recorded conflicts.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/balancePlatforms/(id)/transactionRules/2026-11-02|Balance Platform GET transaction-rules snapshot]]