---
title: "Adyen Balance Platform API v2: PATCH /transactionRules/{transactionRuleId}"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/transactionRules/(transactionRuleId)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/patch/transactionRules/(transactionRuleId)/2026-11-03.md"
tags: [adyen, balance-platform, issuing, transaction-rules, api]
---

## Overview

This 2026-11-03 snapshot of the Balance Platform API reference describes `PATCH /transactionRules/{transactionRuleId}` for updating an existing transaction rule. It shows the v2 TEST server `https://balanceplatform-api-test.adyen.com/bcl/v2`; the `latest` URL does not establish live access or a current deployed version. A rule can apply to a balance platform, payment-instrument group, account holder, balance account or payment instrument, and `requestType` also includes bank transfers. See [[adyen]], [[adyen-issuing]] and [[adyen-platforms]].

## Key takeaways

- `transactionRuleId` is the required path identifier of the rule being updated. To change only `status`, send only `status`; unspecified parameters stay unchanged. For any other update, the page says to send all existing resource parameters, because omitted parameters are removed. This special status-only instruction must be read alongside the request table's required-property labels; the page does not separately state whole-body requiredness.
- The request table marks `description`, `entityKey`, `interval`, `reference`, `ruleRestrictions` and `type` required. The `entityKey` object scopes the rule and its `entityReference` and `entityType` children are individually labeled optional. Within `interval`, `type` is required; each present restriction object marks `operation` required while its `value` is labeled optional. Consult the raw table for the individual restriction operations and values.
- Rule types are `blockList`, `maxUsage`, `velocity` and `bypass`. For `bypass`, provide the overridden rule `id` in `overridesRule` and leave `ruleRestrictions` empty, qualifying the general description that it contains conditions. `aggregationLevel` applies to `velocity` and `maxUsage`, must be at or below `entityKey` in the hierarchy, and defaults to `paymentInstrument`.
- `requestType` defaults to `authorization` and can be `authentication`, `tokenization` or `bankTransfer`. `outcomeType` defaults to `hardBlock`; `scoreBased` needs `score` between -100 and 100 and is unavailable for `bankTransfer`; `enforceSCA` is limited to `authentication`. Rolling/sliding intervals require `duration`, capped at 90 days or equivalent; minutes/hours are allowed only for sliding. The fixed-reset descriptions use CET while `timeZone` defaults to UTC, so do not infer one universal reset instant.
- `startDate`, `endDate` and `status` describe rule evaluation timing/state. The page says a provided `startDate` makes a rule active and otherwise evaluation can continue until `status` becomes inactive when no `endDate` is supplied. The 200 response is a returned rule configuration with optional `id` and `status`; 400, 401, 403, 422 and 500 are documented failures. The 422 and 500 generic JSON examples describe payment-instrument operations, so they do not define a transaction-rule-specific failure. A 200 update or the inactive sample does not establish a particular rule evaluation, authorization, authentication, transfer, booking or settlement.

## Detail locators

- Endpoint purpose, replacement behavior, TEST base and path ID: pinned raw lines 5–21.
- Request properties, scope, intervals, outcomes and defaults: `## Parameters > ### Request body`, lines 24–47 and 123–126.
- All restriction objects, their operations and conditional velocity prerequisites: same request-body table, lines 48–122.
- Illustrative request, which includes fields beyond `status`: `## Request examples > ### updateTransactionRuleStatus`, lines 128–153. This does not negate the status-only instruction or prescribe every update payload.
- Success response and rule fields: `## Responses > ### 200 Success`, lines 154–262. Error schemas: lines 265–362; illustrative success and generic failure payloads: `## Response examples`, lines 364–468.

## Related

- [[adyen-issuing]] — issuing and transaction-rule context.
- [[source-adyen-api-explorer-balanceplatform-latest-post-transactionrules]] — separately captured create operation.
- [[source-adyen-docs-issuing-authorisation-transaction-rules]] — separate conceptual guide.
- [[source-adyen-docs-issuing-authorisation-transaction-rules-create-and-manage]] — separate lifecycle guide.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/patch/transactionRules/(transactionRuleId)/2026-11-03|PATCH transaction rule, 2026-11-03 capture]]