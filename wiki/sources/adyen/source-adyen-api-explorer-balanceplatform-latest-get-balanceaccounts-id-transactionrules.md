---
title: "Adyen Balance Platform API v2: GET /balanceAccounts/{id}/transactionRules"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)/transactionRules"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)/transactionRules/2026-11-02.md"
tags: [adyen, balance-platform, balance-accounts, transaction-rules, api]
---

## Overview

This 2026-11-02-captured Balance Platform API v2 reference describes `GET /balanceAccounts/{id}/transactionRules`: it returns a list of transaction rules associated with the balance account named by the required path `id`. The only server shown is the TEST base `https://balanceplatform-api-test.adyen.com/bcl/v2`. The `latest` documentation route does not establish live deployment, current access or an account's eligibility. See [[adyen]], [[adyen-platforms]], [[adyen-issuing]] and [[adyen-business-accounts]] for product context.

## Key takeaways

- The path `id` identifies the balance account, not a transaction rule. The 200 response table marks the `transactionRules` array optional. Within a listed rule object it marks `description`, `entityKey`, `interval`, `reference`, `ruleRestrictions` and `type` required; the rule's own `id`, `status` and many other fields are marked optional. These are response fields, not GET inputs. The page lists no query parameters, pagination contract or request body.
- A rule's `entityKey` describes the resource scope with `entityType` and `entityReference`, although those child fields are individually optional in the table. Listed types include balance platform, payment-instrument group, account holder, balance account and payment instrument. `requestType` defaults to `authorization` when omitted and also lists `authentication`, `tokenization` and `bankTransfer`; association with a balance account does not make every listed rule a bank-transfer rule.
- The rule types are `blockList`, `maxUsage`, `velocity` and `bypass`. The response-field descriptions give a payment-instrument default for `aggregationLevel` on velocity/maxUsage, a conditionally required rolling/sliding `duration` capped at 90 days or equivalent, and `overridesRule` plus empty restrictions for bypass. `outcomeType` defaults to `hardBlock`; `scoreBased` requires a score from -100 to 100 and is disallowed for bank transfers, while `enforceSCA` is limited to authentication. Consult the raw table for the complete conditions and operations.
- The table describes `startDate`, `endDate` and active/inactive `status`, including creation-time wording. This GET does not create, activate, delete or execute a rule. A 200 list response does not establish that a rule applied to a transaction, a transfer was approved, or funds moved. The page documents 400, 401, 403, 422 and 500 responses; its generic 422 and 500 JSON samples concern payment-instrument operations and do not define this list endpoint's specific failure conditions.

## Detail locators

- Endpoint, TEST server, required balance-account path `id` and optional 200 list parent: pinned raw lines 5–27.
- Rule identity/scope, intervals, defaults, conditions, outcomes and status fields: `## Responses > ### 200 Success`, lines 28–76. Conditional descriptions there are response-field semantics, not GET input requirements.
- Error response schemas: `## Responses`, lines 79–176. Generic error examples, including unrelated payment-instrument 422/500 text: `## Response examples`, lines 178–244.

## Related

- [[adyen-platforms]] — balance-platform resource context.
- [[adyen-issuing]] and [[adyen-business-accounts]] — separate product contexts for transaction rules.
- [[source-adyen-api-explorer-balanceplatform-latest-post-transactionrules]] — separate 2026-09-15 rule-creation contract.
- [[source-adyen-docs-issuing-authorisation-transaction-rules-create-and-manage]] — separate Issuing rule lifecycle guide.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/balanceAccounts/(id)/transactionRules/2026-11-02|Balance-account transaction-rules GET snapshot]]