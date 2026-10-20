---
title: "Adyen Balance Platform Accounting Report cash-management examples"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/report-types/balance-platform-accounting-report/cash-management"
raw_files:
  - "adyen/docs/issuing/report-types/balance-platform-accounting-report/cash-management/2026-09-15.md"
tags: [adyen, issuing, accounting-report, cash-management, transfers]
---

## Overview

This 2026-09-15-captured Issuing-path guide uses Balance Platform Accounting Report rows to illustrate balance-account cash management and bank versus internal-transfer classification. It describes filtering events affecting balance accounts and examining cardholder spending trends as possible cash-management uses; the sample does not prove a live transfer or an actual cash-flow forecast. [[adyen]] [[adyen-issuing]]

## Key takeaways

- The page calls `Balance (PC)` the current balance, affected by funding, captures and refunds, and describes cardholder available balance as the sum of `Balance (PC)` and signed authorized `Reserved (PC)` in this report context (raw lines 21–24). Keep that report-column statement separate from the generic balance-type definitions in [[source-adyen-docs-issuing-balance-types]]; the page gives no account-wide calculation procedure.
- It distinguishes external-bank `bankTransfer` activity from balance-account-to-balance-account `internalTransfer` activity using `Category`, `Type` and `Status`. It says internal transfers have transfer and transaction parts like payments (raw lines 26–32). The shown rows are an internal EUR 15 debit from one balance account and credit to another, with `received`, `authorised`, then `booked` statuses and distinct Transfer Ids for the two sides (raw lines 40–47).
- The prose says to reconcile internal-transfer rows with the same `Reference For Beneficiary`, and bank-transfer rows using `Description`, `Reference` or `Reference For Beneficiary` (raw line 38). But in the internal-transfer sample, the shared user-supplied reference is in `Reference` on the outgoing side and `Description` on the incoming side; incoming `Reference For Beneficiary` is not shown as a common value (raw lines 42–47). Do not implement a join that assumes the printed sample matches the stated same-field rule.
- The text announces a bank-transfer flow before the diagram, but the only detailed table below it has `Category: internal` and `Type: internalTransfer` (raw lines 34–47). The table therefore does not provide bank-transfer row evidence or show bank receipt.

## Detail locators

- Cash-management purpose and report balance-column statements: raw lines 19–24. Bank/internal categories, event types and reconciliation instruction: raw lines 26–38.
- Internal-transfer two-account row example, signed Received/Reserved/Balance (PC), references, booking/value dates and IDs: raw lines 40–47.

## Related

- [[adyen-issuing]] — Issuing and balance-platform context.
- [[source-adyen-docs-issuing-report-types-balance-platform-accounting-report]] — parent report scope and field reference.
- [[adyen-reporting]] — broader reporting context.

## Raw Sources

- [[raw/adyen/docs/issuing/report-types/balance-platform-accounting-report/cash-management/2026-09-15|Cash management report guide, captured 2026-09-15]]
