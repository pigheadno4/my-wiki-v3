---
title: "Adyen Payout Service common reconciliation processes"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/reconciliation-use-cases"
raw_files:
  - "adyen/docs/payouts/payout-service/reconciliation-use-cases/2026-09-15.md"
tags: [adyen, payout-service, reporting, reconciliation, balance-platform]
---

## Overview

This 2026-09-15 [[adyen]] **Payout Service** navigation guide groups report-based reconciliation processes for accounts in a balance platform. It routes from general preparation to pay-in reconciliation, balance spot-checks, fund-transfer cash management and fee reconciliation. It gives no report-row matching procedure or proof that a real payment, transfer, payout or bank receipt was reconciled. See [[adyen-reporting]] and [[adyen-payouts]].

## Key takeaways

- Before building a process, the guide asks readers to understand the payment lifecycle, balance-platform account structure and fund flows; select report types relevant to the use case; configure, download and combine reports; and understand fee types. These are preparation routes, not evidence that the reports were generated or accurately joined. See raw lines 21–28.
- The four child tasks have distinct scope: reconcile **pay-ins processed to balance-platform accounts**; spot-check balance positions; use the **Balance Platform Accounting Report** for fund-transfer cash management; and track/reconcile **pay-in and payout fees**. The overview supplies routes only. Follow each child guide for report grain, fields, timing and matching logic before using it to support an accounting conclusion. See raw lines 30–44.
- Its opening wording says “payout transactions,” but the listed child processes also cover incoming pay-ins and account balances. Treat this as a Payout Service reconciliation hub, not a claim that every linked report row is an outbound payout. See raw lines 15–19 and 30–44.

## Detail locators

- **Purpose and prerequisite routes:** raw lines 15–28.
- **Pay-in and balance processes:** raw lines 30–36.
- **Transfer and fee processes:** raw lines 38–44.

## Related

- [[adyen-reporting]]
- [[adyen-payouts]]

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/reconciliation-use-cases/2026-09-15|Payout Service reconciliation use-case hub — collected 2026-09-15]]
