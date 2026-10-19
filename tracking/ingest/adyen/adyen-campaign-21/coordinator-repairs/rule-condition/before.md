---
title: "Adyen Issuing: Create and manage transaction rules"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/authorisation/transaction-rules/create-and-manage"
raw_files:
  - "adyen/docs/issuing/authorisation/transaction-rules/create-and-manage/2026-09-15.md"
tags: [adyen, issuing, transaction-rules, authorisation]
---

## Overview

This Adyen Issuing guide (last modified 2025-01-07; captured 2026-09-15) describes creating and managing transaction rules in Customer Area or via the Balance Platform Configuration API. It covers rule conditions and outcomes, listing rules, entity-specific overrides or bypasses, updates, and activation status. [[adyen]] [[adyen-issuing]]

## Key takeaways

- The stated setup requires Configuration API access with the **Bank Manage TransactionRules** role, subscriptions to transfer and transaction webhooks, and familiarity with transaction-rule behavior. The page's integration type is Adyen Issuing. See raw lines 27–35.
- In Customer Area, rule details include an entity type/key, aggregation level where relevant, and rule type. The page says at most five conditions per rule and that meeting any specified condition applies the outcome. Review can test a rule against previous platform transactions; this is a historical test, not proof of live authorization. See raw lines 53–90.
- The API creation table describes `entityKey`, `interval`, `requestType`, `type`, `ruleRestrictions`, `outcomeType`, and other fields; it lists `hardBlock`, `scoreBased`, and `enforceSCA` outcomes and `authorization`, `authentication`, or `tokenization` request types. The allowed restriction/type/operation/interval combinations are tabulated at raw lines 538–557. The sample POST and response illustrate a country block for one payment instrument and a returned rule ID, not an executed payment. See raw lines 92–113 and 503–535.
- Rules can be viewed in Customer Area or fetched by rule ID or by balance account, account holder, balance platform, payment instrument, or payment instrument group. Entity-specific POST rules can override a higher-ranked rule through `overridesRule`; a `bypass` rule with empty restrictions skips that rule for the entity. PATCH updates a rule by ID; PATCH status `inactive` stops its application and `active` resumes it. See raw lines 559–602, 668–679, 726–751, and 997–1226.
- **Source boundary/conflicts:** The opening describes suspicious payout requests and every external payout, while the same page is labeled Issuing and its rule parameters and primary example describe card authorization, authentication, tokenization, and a payment instrument. The skip example also switches between a balance-account/bank-transfer request and a payment-instrument/authorization response. Treat these as inconsistent examples rather than a unified payout/card rule guarantee. The Customer Area maximum-usage description says the card is deactivated after its lifetime threshold; the API `maxUsage` description says a transaction is declined when limits are met. Check the exact context in raw lines 19, 27–35, 70, 106–109, 668–723.

## Detail locators

- Customer Area creation and testing: raw lines 37–90.
- API request field table and sample, including dates/status: raw lines 92–535.
- Valid rule restriction combinations: raw lines 538–557.
- Listing, override, skip, update, deactivate and activate: raw lines 559–1226.

## Related

- [[adyen-issuing]] — main concept.
- [[adyen-index]] — provider index.

## Raw Sources

- [[raw/adyen/docs/issuing/authorisation/transaction-rules/create-and-manage/2026-09-15|Create and manage rules, captured 2026-09-15]]
