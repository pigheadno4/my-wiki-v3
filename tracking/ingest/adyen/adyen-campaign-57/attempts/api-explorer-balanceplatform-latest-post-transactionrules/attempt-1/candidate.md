---
title: "Adyen Balance Platform API v2: POST /transactionRules"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/post/transactionRules"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/post/transactionRules/2026-09-15.md"
tags: [adyen, balance-platform, issuing, transaction-rules, api]
---

## Overview

This 2026-09-15 Balance Platform Configuration API v2 reference describes `POST /transactionRules`, which creates a scoped rule whose conditions and outcome can affect a user's Adyen-issued-card transaction. The request schema also lists `bankTransfer` among `requestType` values; that wider schema scope should not be silently collapsed into card authorization. The only displayed server is the test host `https://balanceplatform-api-test.adyen.com/bcl/v2`. The `latest` documentation URL does not establish current live version or access. See [[adyen]], [[adyen-issuing]] and [[adyen-platforms]].

## Key takeaways

- The request table marks `description`, `entityKey`, `interval`, `reference`, `ruleRestrictions` and `type` required. `entityKey` identifies the resource scope: balance platform, payment-instrument group, account holder, balance account or payment instrument; its two child fields are individually marked optional in the table. The page does not separately state whole-body requiredness.
- `blockList`, `maxUsage`, `velocity` and `bypass` are rule types. For `velocity` or `maxUsage`, `aggregationLevel` must be at or below the `entityKey` hierarchy and defaults to payment-instrument accumulation. `bypass` requires the overridden rule ID in `overridesRule` and an empty `ruleRestrictions` object, despite that field's general description saying it contains one or more conditions.
- `interval.type` is required within `interval`; rolling/sliding intervals require `duration`, with a 90-day maximum (or equivalent). Minutes and hours are only allowed for sliding intervals. The request table describes fixed daily/weekly/monthly resets in CET while `interval.timeZone` defaults to UTC; consult the precise schema and companion guide before assuming a reset instant. `interval.dayOfWeek` omits Saturday from its listed values, although the separate `ruleRestrictions.dayOfWeek` includes Saturday.
- Default `requestType` is `authorization`. Default `outcomeType` is `hardBlock`; `scoreBased` requires a `score` from -100 to 100 and is disallowed for `bankTransfer`; `enforceSCA` is only allowed for `authentication`, with failed or timed-out authentication declining the transaction. The three transfer-pattern restrictions `matchingValues`, `sameAmountRestriction` and `sameCounterpartyRestriction` each specify velocity, interval and matching-transaction prerequisites.
- The page says a supplied `startDate` creates the rule active; without one, `startDate` is set when status becomes active. An omitted `endDate` leaves evaluation until status is inactive. A 200 response reports rule data and an `id`, while 400, 401, 403, 422 and 500 errors are documented. The 422/500 JSON samples concern payment-instrument operations, so they do not define this endpoint's specific failures. A successful create response or illustrative rule payload does not prove that any particular authorization, authentication, bank transfer or funds movement occurred.

## Detail locators

- Scope, defaults, interval and outcome conditions: pinned raw `## Parameters > ### Request body`, lines 14–37 and 113–116.
- All available rule restrictions and supported operations: same request-body table, lines 38–112. Note the separate `operation` and `value` rows inside each restriction.
- Four illustrative request payloads: `## Request examples`, lines 118–237; these are examples, not universal rule requirements or transaction-outcome evidence.
- Response fields and statuses: `## Responses`, lines 238–447; response payload examples and generic errors: `## Response examples`, lines 448–654.

## Related

- [[adyen-issuing]] — issuing authorization and transaction-rule context.
- [[source-adyen-docs-issuing-authorisation-transaction-rules]] — separate rule-concept guide.
- [[source-adyen-docs-issuing-authorisation-transaction-rules-create-and-manage]] — separate lifecycle guide, with its own recorded condition and example conflicts.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/post/transactionRules/2026-09-15|Balance Platform POST /transactionRules snapshot]]
