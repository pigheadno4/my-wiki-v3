---
title: "Adyen Payout Service: create and manage transaction rules"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/transaction-rules/create-and-manage"
raw_files:
  - "adyen/docs/payouts/payout-service/transaction-rules/create-and-manage/2026-09-15.md"
tags: [adyen, payout-service, transaction-rules, external-payouts, controls]
---

## Overview

This 2021-modified, 2026-09-15-captured [[adyen]] Payout Service guide uses the Balance Platform Configuration API to create, inspect, override, skip, and update transaction rules for outgoing **external payouts** from balance accounts. It requires an Adyen Payouts integration, the **Bank Manage TransactionRules** API role, and Transfer and Transaction webhook subscriptions. The page expressly excludes internal transfers. See [[adyen-payouts]].

## Key takeaways

- **Create and effect:** POST `/transactionRules` targets an `entityKey` and specifies an interval, restrictions, `requestType: bankTransfer`, and `outcomeType: hardBlock`. The described `blockList` and `velocity` types decline a transfer when their respective conditions apply; velocity accumulates previous transactions within its interval, with `aggregationLevel` limited here to `balanceAccount`. Although the page introduction says rules can automatically approve or decline, its concrete creation table prescribes `hardBlock`; do not treat a nonblocked payout or rule creation response as separate human approval, booking, or bank receipt. See pinned raw lines 17–19 and 37–57.
- **Activation and limits:** `status: active` starts evaluation and sets `startDate` to the current time; a future `startDate` creates an active rule scheduled for that date. A future `endDate` stops evaluation; without it, evaluation continues until `status` becomes inactive. The EUR 500,000 daily velocity rule is an example using EUR minor units (`50000000`), not an observed live limit. See pinned raw lines 45–57 and 59–140.
- **Inspect and narrow override:** GET routes retrieve one rule or list rules for a balance account, account holder, or balance platform. The hierarchy can be overridden for a specific entity by POSTing a new rule with `overridesRule`, as illustrated by raising one balance account's daily threshold from EUR 500,000 to EUR 800,000. This changes the control applied to that entity. See pinned raw lines 143–248.
- **Skip and update controls:** A `bypass` rule with empty `ruleRestrictions` and `overridesRule` skips the named rule for a specified entity; the example removes that daily maximum for one balance account. PATCH `/transactionRules/{id}` changes restrictions or `status` between active and inactive; the example raises a platform-wide threshold to EUR 800,000. Skipping or weakening a rule removes that rule's block, but does not itself establish that an external transfer is authorized, processed, or received. See pinned raw lines 250–367.

## Detail locators

- Integration, role, webhook, and internal-transfer scope: pinned raw lines 17–35.
- POST fields, lifecycle dates, rule types, and example response: pinned raw lines 37–140.
- GET routes and entity-specific override: pinned raw lines 143–248.
- Bypass and PATCH examples: pinned raw lines 250–367.

## Related

- [[adyen-payouts]] — Payout Service versus legacy Payout API context.
- [[source-adyen-docs-payouts-payout-service-payout-lifecycle]] — separate transfer lifecycle and webhook boundaries.

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/transaction-rules/create-and-manage/2026-09-15|Payout Service transaction-rule guide, captured 2026-09-15]]
