---
title: "Adyen Business Accounts: Create and manage transaction rules"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/transaction-rules/create-and-manage"
raw_files:
  - "adyen/docs/business-accounts/transaction-rules/create-and-manage/2026-09-15.md"
tags: [adyen, business-accounts, transaction-rules, bank-transfers, risk-controls]
---

## Overview

This Business Accounts procedure page (last modified 2021-05-31; captured 2026-09-15) shows Configuration API creation, lookup, override, bypass and update of transaction rules for outgoing external bank transfers. Rules can hard-block matching transfers, so changes to scope, restrictions, activation or bypass affect payout controls. It supplies test examples rather than evidence of a live rule or transfer. See [[adyen]], [[adyen-business-accounts]] and [[source-adyen-docs-business-accounts-transaction-rules]] for the separately documented evaluation hierarchy and pilot availability boundary.

## Key takeaways

- The stated setup calls for Adyen Payouts, Configuration API access with the **Bank Manage TransactionRules** role, Transfer and Transaction webhook subscriptions, and familiarity with the transaction-rules overview. These rules are expressly unsupported for internal transfers.
- Create a rule with POST `/transactionRules`. The create table specifies `entityKey`, `interval`, `outcomeType: hardBlock`, `requestType: bankTransfer`, `ruleRestrictions`, `type`, description and reference; `aggregationLevel` can only be `balanceAccount` for velocity rules. A returned `transactionRule.id` identifies the configuration resource. The EUR 500K daily velocity limit is an illustration, not an asserted default.
- Status and dates control evaluation: `active` starts evaluation and automatically sets `startDate` to current time; the guide also describes a future `startDate` on a rule whose status is `active`. An optional future `endDate` stops evaluation; without one, evaluation continues until status becomes `inactive`. Do not equate an `active` field alone with a rule already evaluated.
- An override is a **new** rule for a specified entity with `overridesRule` pointing to an existing rule. The example raises one balance account's daily maximum from EUR 500K to EUR 800K. A bypass is likewise a new entity-specific rule with `type: bypass`, empty `ruleRestrictions` and `overridesRule`; it skips the named rule entirely for that entity. Removing a hard-block this way changes protection, so the example is not merely a display or readback operation.
- Read one rule by ID or list rules for a balance account, account holder or balance platform. PATCH `/transactionRules/{id}` updates named parameters and restrictions, including `status: active|inactive`. The PATCH example puts `totalAmount` at the body root while its response nests it under `ruleRestrictions`; treat the example as a documentation inconsistency and verify the intended request shape against the relevant API reference before using it.

## Detail locators

- Requirements, role, webhooks and internal-transfer exclusion: raw lines 26–35.
- POST creation field table, dates/status and EUR 500K test example: raw lines 37–141. The table's general required fields and the shorter bypass payload (lines 250–307) should not be merged into an unverified schema claim.
- GET scope/list endpoints: raw lines 143–152.
- Override by new rule and `overridesRule`: raw lines 154–248; bypass with `type: bypass` and empty restrictions: lines 250–307.
- PATCH and active/inactive values: raw lines 310–374; compare request lines 327–340 with response lines 360–367 for the `ruleRestrictions` nesting mismatch.

## Related

- [[adyen-business-accounts]] — Business Accounts product context.
- [[source-adyen-docs-business-accounts-transaction-rules]] — evaluation criteria, rule hierarchy and pilot qualification.
- [[source-adyen-docs-business-accounts-use-transfer-limits-balance-accounts]] — separate balance-account transfer-limit control.

## Raw Sources

- [[raw/adyen/docs/business-accounts/transaction-rules/create-and-manage/2026-09-15|Adyen Docs: Create and manage rules (2026-09-15 snapshot)]]
