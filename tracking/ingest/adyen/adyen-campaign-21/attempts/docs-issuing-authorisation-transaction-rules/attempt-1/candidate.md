---
title: "Adyen Issuing: Use transaction rules"
type: source
date_ingested: 2026-10-19
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/authorisation/transaction-rules"
raw_files:
  - "adyen/docs/issuing/authorisation/transaction-rules/2026-09-15.md"
tags: [adyen, issuing, transaction-rules, authorisation]
---

## Overview

This Adyen Issuing guide (last modified 2022-04-04; captured 2026-09-15) explains transaction-rule criteria, conditions and outcomes for Adyen-issued card activity, including payment authorizations and ATM withdrawals. It describes entity scope, accumulation and limits, outcome hierarchy, relayed authorisation ordering, and triggered-rule notifications. [[adyen]] [[adyen-issuing]]

## Key takeaways

- Rules specify request type (`authorization` by default, `authentication`, or `tokenization`), rule type, interval, one target entity, conditions, and outcome. Entity scope may be a balance account, account holder, payment instrument, payment instrument group, or balance platform; one rule targets one resource. Accumulation defaults to payment instrument and can occur only at or below the rule's entity level. See raw lines 23–38, 54–73, 75–119.
- The guide says **all conditions within a rule** must match before its outcome applies, while one or more rules may apply to an entity. This conflicts with the companion [[source-adyen-docs-issuing-authorisation-transaction-rules-create-and-manage]], which says **any** specified condition triggers the rule outcome (its raw line 86). Do not silently combine these into one rule-evaluation guarantee. See this raw's lines 121–135 and 174–184.
- The described outcomes are hard block, score-based, and enforce SCA. For authorization or tokenization, a matching hard block declines first; then score-based rules are evaluated, with totals above 100 declining. For authentication, the order adds enforce SCA and RBA/TRA exemption checks before the score step; a score above 100 prompts identity verification, and failed verification declines. Enforce SCA is restricted to `requestType=authentication`. The source's branch descriptions use above/below 100, so do not infer treatment at exactly 100. See raw lines 148–172 and 184–222.
- If transaction rules decline a transaction, Adyen says it does not send a relayed authorisation webhook for that transaction. Amount/count limits use authorized amounts/transactions, including uncaptured authorizations; an expired or canceled authorization releases that amount/count back to the available limit. This is the guide's accounting description, not evidence of a particular capture or settled payment. See raw lines 40–50 and 137–146.
- Blocklist, maximum usage, velocity and bypass are described rule types. Intervals include lifetime, per transaction, fixed, rolling and sliding. A bypass identifies the rule to skip for a specified entity. For payout declines, the page points to transfer webhooks (`transactionRulesResult`, reason `declinedByTransactionRule`) or Customer Area **Balances > Transfers**; that payout-monitoring section sits alongside Issuing/card framing and should be read within its own stated scope. See raw lines 64–89 and 224–229.

## Detail locators

- Criteria and request/rule types: raw lines 23–73.
- Interval table, entity hierarchy, and aggregation: raw lines 75–119.
- Restriction operations and authorization-based limits: raw lines 121–146.
- Outcomes and request-type-specific evaluation order: raw lines 148–222.
- Triggered-rule payout update routes: raw lines 224–229.

## Related

- [[adyen-issuing]] — main concept.
- [[source-adyen-docs-issuing-authorisation-transaction-rules-create-and-manage]] — creation and management guide with the conflicting condition statement.
- [[adyen-index]] — provider index.

## Raw Sources

- [[raw/adyen/docs/issuing/authorisation/transaction-rules/2026-09-15|Use transaction rules, captured 2026-09-15]]
