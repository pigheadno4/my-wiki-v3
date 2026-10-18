---
title: "First year operational tasks | Adyen for Platforms"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/reconciliation-use-cases/first-year-focus"
raw_files:
  - "adyen/docs/platforms/reconciliation-use-cases/first-year-focus/2026-09-15.md"
tags: [adyen, platforms, reporting, reconciliation, operations]
---

## Overview

This 2026-09-15 [[adyen]] for Platforms page frames reporting and reconciliation use cases to prioritize during the first year of an embedded-payments offering. It separates platform product/finance stakeholders from SMB platform users, argues for early finance/product/engineering alignment, and routes to separate platform-level and user-level reporting guides. See [[adyen-reporting]] for the main reporting route. This is a planning guide, not a report schema, accounting opinion or evidence that any records have reconciled.

## Key takeaways

- The page distinguishes reporting (financial statements and activity summaries) from reconciliation (comparing record sets for discrepancies) and says reports support reconciliation. Its bank-reconciliation example describes comparison with bank records; the page itself does not supply a bank statement or proof of matched balances. [Raw: lines 19–27]
- At platform level, the product team builds industry-specific reporting features and may own embedded-payments P&L/pricing strategy; the finance team handles budgeting, accounting, reporting, reconciliation of revenue/fees against Adyen reports and invoices, cash-flow/payment-data monitoring, periodic settlement-versus-internal-record checks, statements and audits. These are stakeholder tasks, not a claim that one Adyen report contains every required grain. [Raw: lines 29–47]
- For SMB platform users, the page identifies daily review of financial reports and metrics plus discrepancy resolution, and periodic finance reconciliation, tax filing, statement review and comparison of bank statements with internal payment/fee records, sometimes with an external accountant. These are illustrative user needs, not instructions that the platform already supplies each report or completes its users' accounting. [Raw: lines 49–64]
- Because pricing models, funds flows, currencies and transaction statuses complicate reporting, the guide recommends involving finance early in requirements gathering, with product and engineering according to implementation/granularity. Its next-step links lead to separate platform-level and user-level reporting processes; those child pages own actual report choices, row grains, joins and limitations. The captured `[required]` link labels are navigation artifacts, not standalone eligibility or compliance requirements. [Raw: lines 66–88]

## Detail locators

- Purpose and reporting-versus-reconciliation distinction: raw lines 17–27.
- Platform product/finance stakeholder tasks: raw lines 29–47.
- SMB user daily and periodic reporting tasks: raw lines 49–64.
- Early cross-functional requirements and platform/user child routes: raw lines 66–88.

## Related

- [[adyen-reporting]] — provider reporting and reconciliation evidence boundary
- [Platform-level reporting](https://docs.adyen.com/platforms/reconciliation-use-cases/first-year-focus/platform-level-reporting) — linked detailed platform use cases
- [User-level reporting](https://docs.adyen.com/platforms/reconciliation-use-cases/first-year-focus/platform-user-level-reporting) — linked detailed user use cases
- [Reconciliation use cases](https://docs.adyen.com/platforms/reconciliation-use-cases) — parent navigation

## Raw Sources

- [[raw/adyen/docs/platforms/reconciliation-use-cases/first-year-focus/2026-09-15|Adyen Platforms first year operational tasks — collected 2026-09-15]]
