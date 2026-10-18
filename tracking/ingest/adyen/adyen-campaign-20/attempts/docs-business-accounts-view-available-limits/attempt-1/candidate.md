---
title: "View available limits | Adyen Business Accounts"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/view-available-limits"
raw_files:
  - "adyen/docs/business-accounts/view-available-limits/2026-09-15.md"
tags: [adyen, business-accounts, transaction-rules, transfer-limits, available-limits]
---

## Overview

This Business Accounts guide (last modified 2025-01-07; captured 2026-09-15) describes GET /balanceAccounts/{id}/limits for reading amount and count limits regulating outgoing transfers from a user's balance account. It introduces limits from transaction rules or transfer limits, but its stated setup and supported-rule restrictions center on transaction rules. Returned figures are calculated at a response timestamp for the selected balance account; the example is not a current account balance, live entitlement, transfer approval or bank receipt. See [[adyen]], [[adyen-business-accounts]], [[source-adyen-docs-business-accounts-transaction-rules]] and [[source-adyen-docs-business-accounts-use-transfer-limits-balance-accounts]].

## Key takeaways

- **Access and supported limit:** The page requires an Adyen for Platforms integration with Business Accounts and Configuration API access with Bank Manage TransactionRules role. Its setup row calls for a transaction rule with totalAmount or matchingTransactions. Available-limit calculation is documented only for those restrictions, with balance-account-level aggregation. A matchingValues plus matchingTransactions combination is excluded, higher-level aggregation is omitted, and blockList has no limits to report. These exclusions mean an empty or incomplete response cannot prove that no other rule or transfer control exists.
- **Read request and result:** GET /balanceAccounts/{id}/limits takes the balance-account ID; optional transactionRuleId selects a rule. Without it, the page says the limit applying to the balance account is returned according to a transaction-rule hierarchy, but links to an Issuing hierarchy from this Business Accounts guide. The response has calculatedAt, amountLimits and countLimits arrays. Each returned limit includes total limit, spent, remaining, source and interval; source identifies the rule or transfer limit. The timestamp makes it a read-time calculation, not a guarantee for a later transfer.
- **Accounting and interval boundary:** The guide says authorized amount/count consumes available limit and canceled or expired authorizations restore it, regardless of capture. This authorization/capture language is the same card-style wording seen in the related outgoing-transfer transaction-rules overview; do not infer settlement or bank receipt. The response interval table enumerates perTransaction, daily, weekly, monthly, lifetime, rolling and sliding forms plus conditional duration/start fields. Its fixed-interval descriptions use CET while the timezone field says default UTC; preserve the response's explicit interval data rather than assuming a universal reset timezone.
- **Scope tension:** The introduction and source field mention transfer limits as well as transaction rules, while the requirements/limitations and optional query selector are framed around transaction rules. The page does not establish that every configured transfer limit is returned. The sample amount and count values, currencies and timezone are illustrative.

## Detail locators

- Purpose, two limit types and readout fields: pinned raw lines 15–38.
- Integration, API role, supported restrictions and exclusions: pinned raw lines 40–49.
- Authorized-limit accounting: pinned raw lines 51–58.
- GET path/query semantics, hierarchy link and response fields: pinned raw lines 60–100.
- Interval types, conditional fields, timezone and example response: pinned raw lines 102–188.

## Related

- [[adyen-business-accounts]] — main Business Accounts concept and reciprocal source route.
- [[source-adyen-docs-business-accounts-transaction-rules]] — rule evaluation and hardBlock context.
- [[source-adyen-docs-business-accounts-use-transfer-limits-balance-accounts]] — separately configured balance-account transfer limits.

## Raw Sources

- [[raw/adyen/docs/business-accounts/view-available-limits/2026-09-15|View available limits guide, captured 2026-09-15]]
