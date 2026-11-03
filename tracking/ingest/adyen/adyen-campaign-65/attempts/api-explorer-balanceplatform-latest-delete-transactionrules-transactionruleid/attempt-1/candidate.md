---
title: "Adyen Balance Platform API v2: DELETE /transactionRules/{transactionRuleId}"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/delete/transactionRules/(transactionRuleId)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/delete/transactionRules/(transactionRuleId)/2026-11-03.md"
tags: [adyen, balance-platform, issuing, transaction-rules, api]
---

## Overview

This 2026-11-03-captured Balance Platform API v2 reference documents `DELETE /transactionRules/{transactionRuleId}` to delete one transaction rule identified by its unique `transactionRuleId`. The captured server is the TEST base `https://balanceplatform-api-test.adyen.com/bcl/v2`. The `latest` documentation route and this snapshot do not establish live availability or a particular caller's access. See [[adyen]] and [[adyen-issuing]].

## Key takeaways

- The only documented request parameter is the required string path `transactionRuleId`. This page specifies no request body, query parameter, idempotency key, caller role, or endpoint-specific deletion precondition.
- The documented 200 response says the request succeeded and gives a transaction-rule representation, including its scope (`entityKey`), `id`, `reference`, `type`, restrictions, interval, optional status and outcome fields. The table marks `description`, `entityKey`, `interval`, `reference`, `ruleRestrictions` and `type` required in that **response**; `interval.type` is required within its object. They are not DELETE inputs. The success example depicts a velocity rule for a payment-instrument group and does not establish the pre-delete or subsequent state of any real rule.
- The response schema's rule configuration spans `blockList`, `maxUsage`, `velocity` and `bypass`; request types include authorization, authentication, tokenization and bank transfer. The schema describes conditional rolling/sliding duration, the 90-day equivalent maximum, aggregation default, outcome restrictions, and active/inactive evaluation dates. These describe returned rule fields and do not impose a DELETE payload or promise how deletion propagates to future evaluations.
- Authentication and authorization failures are documented as 401 and 403; 400, 422 and 500 are also listed. The generic 422 and 500 JSON examples describe payment-instrument operations, so they are not endpoint-specific deletion conditions. This page does not specify reversal, retry, asynchronous completion, propagation timing, version/conflict behavior or payment outcome. A 200 deletion response should not be read as evidence of a card authorization, settled funds, or current account eligibility.

## Detail locators

- Endpoint purpose, TEST base, required path ID and 200 response: pinned raw lines 5–27.
- Returned rule identity, scope, intervals, defaults, conditions, outcomes and lifecycle fields: `## Responses > ### 200 Success`, lines 27–127. These are response-schema fields.
- Error codes and shapes: `## Responses`, lines 130–227. Success and generic-error examples: `## Response examples`, lines 229–331.

## Related

- [[adyen-issuing]] — Issuing transaction-rule context.
- [[source-adyen-api-explorer-balanceplatform-latest-post-transactionrules]] — separate create-rule reference.
- [[source-adyen-docs-issuing-authorisation-transaction-rules-create-and-manage]] — separate lifecycle guide.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/delete/transactionRules/(transactionRuleId)/2026-11-03|Balance Platform DELETE transaction rule snapshot]]