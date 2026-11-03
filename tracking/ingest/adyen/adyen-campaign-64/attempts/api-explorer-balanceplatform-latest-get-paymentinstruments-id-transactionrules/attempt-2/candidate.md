---
title: "GET /paymentInstruments/{id}/transactionRules — List payment-instrument transaction rules | Adyen"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstruments/(id)/transactionRules"
raw_files:
  - "adyen/api-explorer/balanceplatform/latest/get/paymentInstruments/(id)/transactionRules/2026-11-02.md"
tags: [adyen, balance-platform, issuing, payment-instruments, transaction-rules, api-explorer]
---

## Overview

This [[adyen]] Balance Platform API Explorer snapshot documents `GET /paymentInstruments/{id}/transactionRules`, which returns a list of transaction rules associated with a payment instrument. The captured server is TEST `https://balanceplatform-api-test.adyen.com/bcl/v2`; the URL says `latest` while the server path identifies `v2`. It reads rule configuration, not transaction decisions. See [[adyen-issuing]] for card and rule context.

## Key takeaways

- The only listed input is required string path `id`, the payment-instrument identifier. No query parameters, request body, GET default, pagination or list limit is specified. The 200 response is labeled request success; its `transactionRules` array is optional. Required properties inside an included rule object do not make that top-level array required. [Raw: lines 5–27]
- Within a returned rule, the table requires `description`, `entityKey`, `interval`, `reference`, `ruleRestrictions` and rule `type`; it marks rule `id`, `status`, `outcomeType`, dates and other fields optional. `entityKey` names a resource type and reference for the rule's scope, which can be a balance platform, account holder, balance account, payment-instrument group or payment instrument; it is distinct from the GET path ID. The nested `interval.type` is required if an interval object is included; `duration` is conditionally required for rolling or sliding intervals. [Raw: lines 27–47, 73–76]
- The schema covers `blockList`, `maxUsage`, `velocity` and `bypass` rule types; request types default to authorization and can include authentication, tokenization or bank transfer. `hardBlock` is the default outcome; `scoreBased` and `enforceSCA` have request-type restrictions, and a score-based outcome requires a score from -100 to 100. `aggregationLevel` defaults to payment-instrument level for relevant accumulation rules and must be at the same or a lower hierarchy than `entityKey`. Interval duration is capped at 90 days or equivalent. `matchingValues` and same-amount/counterparty restrictions have velocity-specific prerequisites. See the raw field table for the full condition and operation inventory. [Raw: lines 28–76]

> [!warning] Contradiction
> The `ruleRestrictions` description says the required object contains one or more condition objects [Raw: line 47], while the `bypass` rule description says to leave that object empty and supply `overridesRule` [Raw: line 76]. This GET snapshot does not reconcile the two instructions for a bypass rule; do not infer a valid bypass payload from either sentence alone.

- The example shows two active `blockList` rules under payment-instrument entity keys, one for point-of-sale processing and one for active network tokens. It illustrates schema shape and cannot establish that a real instrument has those rules, that `active` means a specific transaction was evaluated, or that an authorization was declined. [Raw: lines 180–238]
- The page lists 400 request-reading/understanding, 401 authentication, 403 permission, 422 validation and 500 server-processing failures. Generic 422 and 500 examples discuss payment-instrument update/creation, not a transaction-rule GET failure or a rule outcome. [Raw: lines 79–176, 240–304]

## Detail locators

- Purpose, TEST v2 server and required path ID: pinned raw lines 5–17.
- 200 response schema, scopes, conditions, intervals, outcomes, defaults and limits: lines 19–76; success example: lines 178–238.
- Error headings/schemas and generic examples: lines 79–176, 240–304.

## Related

- [[adyen-issuing]] — issuing card and transaction-rule context.

## Raw Sources

- [[raw/adyen/api-explorer/balanceplatform/latest/get/paymentInstruments/(id)/transactionRules/2026-11-02|GET payment-instrument transaction rules — captured 2026-11-02]]