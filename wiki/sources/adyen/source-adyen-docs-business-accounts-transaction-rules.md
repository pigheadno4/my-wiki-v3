---
title: "Use transaction rules | Adyen Business Accounts"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/transaction-rules"
raw_files:
  - "adyen/docs/business-accounts/transaction-rules/2026-09-15.md"
tags: [adyen, business-accounts, transaction-rules, outgoing-transfers, risk-controls]
---

## Overview

This Business Accounts transaction-rules overview (last modified 2022-04-04; captured 2026-09-15) describes automatic evaluation of outgoing third-party bank-transfer requests against configured criteria and conditions. It labels the feature limited availability and pilot-phase, directs interested platforms to an Adyen contact, and describes a hardBlock decline outcome. It does not establish present availability, live configuration, a transfer's final state or bank receipt. See [[adyen]], [[adyen-business-accounts]] and [[source-adyen-docs-business-accounts-send-funds-make-transfer-request]].

## Key takeaways

- **Rule decision:** The platform defines criteria (request type, rule type, time interval and one target entity), restrictions/conditions, and an outcome. For third-party transfers the described request type is bankTransfer. Adyen evaluates a transfer only when rule criteria apply, and a rule's outcome applies when all its conditions match. The overview says the only selectable outcome in this snapshot is hardBlock, which declines the matching transaction; it does not specify a scoring outcome. Across multiple applicable rules, one matching hardBlock suffices to decline.
- **Rule types and scope:** Blocklist checks current transfer data; velocity uses accumulated prior transfers within an interval; bypass skips a named rule for a specified entity and requires that rule's ID. Each rule targets one balance account, account holder or balance platform. Velocity aggregation is always at balance-account level even when a rule applies more broadly, with amount conversion to the account holder's or platform's default currency. The page describes per-transaction, fixed, rolling and sliding intervals; use the raw table for their reset and continued-decline distinctions.
- **Limits and reporting:** The restrictions table names counterparty account/bank/country/name, descriptions, matching transaction count, percentage of available balance, action priority, source-account type and total amount, with same-amount/same-counterparty restrictions usable only with matchingTransactions. The page says authorized amount/count consumes a configured limit and expires/cancellations release it. That authorization/capture wording sits awkwardly within a third-party bank-transfer guide; do not infer a card-capture lifecycle or transfer settlement from it. Declines can be examined through Transfer webhooks' transactionRulesResult and declinedByTransactionRule reason, or Customer Area transfer detail.
- **Boundary:** The overview defines evaluation logic and outcome, not rule-creation API roles, webhook setup or the active/inactive status lifecycle. It links a separate create-and-manage guide for those procedures. A rule definition, status or reported decline is not proof of a successful outgoing transfer.

## Detail locators

- Pilot warning and static-condition recommendation: pinned raw lines 15–26.
- Criteria, all-conditions evaluation and hardBlock decision: pinned raw lines 28–54 and 141–159.
- Blocklist, velocity, bypass, four interval types, target entities and balance-account aggregation: pinned raw lines 55–96.
- Restriction names/operations and authorized-limit accounting: pinned raw lines 98–139; the authorization/capture wording conflict is lines 130–137.
- Triggered-rule reporting and navigation to create/manage and available-limit guides: pinned raw lines 161–178.

## Related

- [[adyen-business-accounts]] — main Business Accounts concept and reciprocal source route.
- [[source-adyen-docs-business-accounts-use-transfer-limits-balance-accounts]] — separate balance-account transfer-limit controls.
- [[source-adyen-docs-business-accounts-send-funds-make-transfer-request]] — outgoing transfer request lifecycle, distinct from rule evaluation.

## Raw Sources

- [[raw/adyen/docs/business-accounts/transaction-rules/2026-09-15|Transaction rules overview, captured 2026-09-15]]
