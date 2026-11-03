---
title: "GET /transactionRules/{transactionRuleId} — Get a transaction rule | Adyen"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/transactionRules/(transactionRuleId)"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/transactionRules/(transactionRuleId)/2026-11-03.md"
tags: [adyen, balance-platform, issuing, transaction-rules, api-explorer]
---

## Overview

This [[adyen]] Balance Platform API Explorer snapshot documents `GET /transactionRules/{transactionRuleId}`, a read of one transaction rule's details. The captured server is TEST `https://balanceplatform-api-test.adyen.com/bcl/v2`; the URL says `latest` while the server path identifies `v2`. See [[adyen-issuing]] for issuing and transaction-rule context.

## Key takeaways

- The only listed input is required string path `transactionRuleId`, the rule identifier. The page specifies no query parameters or request body. It does not name a caller role; 401 and 403 describe authentication and permission failures without a role list. [Raw: lines 5–17, 99–120]
- A 200 labels the request successful and may return an optional top-level `transactionRule` object. Within an included rule object, `description`, `entityKey`, `interval`, `reference`, `ruleRestrictions` and rule `type` are table-required; `id`, `status`, `outcomeType`, dates and other fields are table-optional. `entityKey` contains the rule's resource type and reference, separate from the path rule ID, and can identify a balance platform, payment-instrument group, account holder, balance account or payment instrument. [Raw: lines 19–35, 43–47, 73–76]
- The returned configuration can describe `blockList`, `maxUsage`, `velocity` or `bypass` rules; authorization is the default `requestType`, and `hardBlock` the default `outcomeType`. `scoreBased` requires a score between -100 and 100 and is disallowed for bank transfers; `enforceSCA` is limited to authentication requests. For velocity/max-usage accumulation, `aggregationLevel` defaults to payment-instrument level and must be at or below the `entityKey` hierarchy. [Raw: lines 28, 42–46, 73–76]
- `interval.type` is required inside the table-required `interval` object. Rolling and sliding intervals conditionally require `duration`, capped at 90 days or equivalent; the table gives defaults for day, time and time zone. Some restrictions, including `matchingValues` and same-amount/counterparty checks, require velocity type, an interval and `matchingTransactions`. The full condition and operation inventory remains in the raw schema. [Raw: lines 35–41, 47–72]

> [!warning] Contradiction
> The `ruleRestrictions` description says this object contains one or more condition objects [Raw: line 47], while the `bypass` description says to supply `overridesRule` and leave `ruleRestrictions` empty [Raw: line 76]. This GET snapshot does not reconcile those instructions for constructing a bypass rule.

- The 200 example depicts an active `blockList` rule scoped to a payment instrument; it illustrates response shape, not a guarantee that a queried rule exists, was evaluated for a transaction, blocked an authorization, or produced a payment or funds outcome. The page lists 400, 401, 403, 422 and 500 errors. Its generic 422 and 500 examples concern payment-instrument update/creation, so their details should not be treated as transaction-rule GET semantics. [Raw: lines 79–176, 178–278]
- This read endpoint documents no idempotency key, mutation, deletion, propagation timing or asynchronous approval step. An `active` status and the date fields describe returned rule configuration; they do not prove current account eligibility, compliance, a particular transaction decision, capture, booking or settlement. The dated TEST snapshot does not establish a live environment's behavior. [Raw: lines 9–10, 19–76, 178–212]

## Detail locators

- Purpose, TEST v2 server and path parameter: pinned raw lines 5–17.
- 200 response schema, rule scopes, restrictions, intervals, outcomes, defaults and limits: lines 19–76; success example: lines 178–212.
- Error descriptions and response schemas: lines 79–176; generic error examples: lines 214–278.

## Related

- [[adyen-issuing]] — issuing card and rule context.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/transactionRules/(transactionRuleId)/2026-11-03|GET transaction rule — captured 2026-11-03]]