---
title: "GET /paymentInstrumentGroups/{id}/transactionRules — List payment-instrument-group rules | Adyen"
type: source
date_ingested: 2026-11-03
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstrumentGroups/(id)/transactionRules"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/paymentInstrumentGroups/(id)/transactionRules/2026-11-03.md"
tags: [adyen, balance-platform, issuing, payment-instrument-groups, transaction-rules, api-explorer]
---

## Overview

This [[adyen]] Balance Platform API Explorer snapshot documents `GET /paymentInstrumentGroups/{id}/transactionRules`: it returns a list of transaction rules associated with a payment instrument group. The captured server is TEST `https://balanceplatform-api-test.adyen.com/bcl/v2`; the URL uses `latest`, while the server path identifies v2. This is rule-configuration readback, not a transaction decision. See [[adyen-issuing]] for Issuing context. [Raw: lines 5–10]

## Key takeaways

- The only listed input is required string path `id`, the payment instrument group identifier. No query parameter, request body, GET-specific idempotency contract, pagination or list limit is documented here. The 200 response marks the request successful, but its top-level `transactionRules` array is marked optional. [Raw: lines 12–27]
- An included rule may carry its own rule `id` and `entityKey` resource type/reference; these are distinct from the GET path group ID. The rule table marks `description`, `entityKey`, `interval`, `reference`, `ruleRestrictions` and rule `type` required within a returned rule object, while the rule ID, `status`, dates and many configuration fields are marked optional. `entityKey.entityType` can identify a balance platform, account holder, balance account, payment instrument group or payment instrument. Required nested fields do not make the top-level array required. [Raw: lines 25–47, 73–76]
- Rule types are `blockList`, `maxUsage`, `velocity` and `bypass`. `requestType` defaults to `authorization` when omitted; its listed alternatives are `authentication`, `tokenization` and `bankTransfer`. `hardBlock` is the default outcome; `scoreBased` is disallowed for bank transfers and needs a score between -100 and 100, while `enforceSCA` is allowed only for authentication requests. For velocity/maxUsage, `aggregationLevel` defaults to payment-instrument level and must not be higher in hierarchy than `entityKey`. Rolling/sliding intervals require `duration`, capped at 90 days or equivalent. See the field table for condition operations and interval defaults. [Raw: lines 28–76]

> [!warning] Contradiction
> The response table says `ruleRestrictions` contains one or more condition objects [Raw: line 47], but the `bypass` rule description says to leave `ruleRestrictions` empty and provide `overridesRule` [Raw: line 76]. This GET snapshot does not reconcile those instructions; do not infer a valid bypass payload from either statement alone.

- The success example shows two `inactive` velocity rules with `paymentInstrumentGroup` entity keys and payment-instrument aggregation. These are illustrative records, not proof of current rule activation, evaluation, a decline, or any card or funds outcome. The example's descriptions and restriction bodies should not be treated as a guarantee for a real group. [Raw: lines 178–250]
- Listed failures are 400 request-understanding, 401 authentication, 403 permission, 422 validation and 500 processing errors. The generic 422/500 samples mention payment-instrument changes/creation, not this GET's rule-list result. The page gives no caller-role name, rule creation/update/deletion action, propagation timing, asynchronous review/approval/activation signal, reversal, or current eligibility evidence. [Raw: lines 79–176, 252–316]

## Detail locators

- Purpose, TEST v2 server, and path parameter: pinned raw lines 5–17.
- 200 list schema, rule scopes, intervals, outcomes, defaults and limits: lines 19–76; example: lines 178–250.
- Error headings, schemas and illustrative samples: lines 79–176, 252–316.

## Related

- [[adyen-issuing]] — Issuing and transaction-rule context.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/paymentInstrumentGroups/(id)/transactionRules/2026-11-03|GET payment-instrument-group transaction rules — captured 2026-11-03]]