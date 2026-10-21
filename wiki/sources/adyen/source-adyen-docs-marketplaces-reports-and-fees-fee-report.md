---
title: "Marketplace Balance Platform Fee Report"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/reports-and-fees/fee-report"
raw_files:
  - "adyen/docs/marketplaces/reports-and-fees/fee-report/2026-09-15.md"
tags: [adyen, marketplaces, reporting, fees, reconciliation]
---

## Overview

This 2026-09-15 [[adyen]] Marketplace reference describes the monthly Balance Platform Fee Report for payment and processing fees incurred on balance-platform users' transactions. Its documented row fields are billing month, platform, account holder, balance account, fee type/name, currency and fee amount. The report supports user-level fee and invoice comparison, but identifies where fees were **incurred**, not where they were billed or which account was debited. [[adyen-reporting]]

## Key takeaways

- The report covers transaction-related costs including processing, scheme, interchange, chargeback and refund fees. It is available monthly on the first day of the month and can be generated on a Customer Area schedule or manually for a chosen month; the stated filename pattern is `balanceplatform_fee_report_YYYY_MM.csv`. That schedule does not prove a specific file was generated or delivered. See raw lines 15–31.
- Fees that cannot be tied to a platform user are reported on the liable account. A row's account holder or balance account therefore identifies the incurred-fee reporting scope, not the account charged for billing. See raw lines 19–25.
- The page recommends API responses and webhooks for current individual fee status and ledgers, then monthly report-to-invoice reconciliation across all transaction fees. The sample contains positive and negative fee amounts, but the standard fields list no individual transaction ID; a row should not be treated as a transaction-level booking or final balance debit. See raw lines 33–73 and 83–92.
- Standard fields are Billing Month, BalancePlatform, AccountHolder, BalanceAccount, Fee Type, Fee Name, Currency Code and Fee Amount. Optional account-holder/account references and descriptions can be added. The example header says `Currency` while the standard-column table says `Currency Code`; generated files may have extra fields depending on platform settings. Inspect the actual exported header before mapping. See raw lines 43–45 and 75–105.

## Detail locators

- **Purpose, monthly timing, liable fallback and incurred-versus-billed boundary:** raw lines 15–31.
- **Monthly reconciliation recommendation and sample qualification:** raw lines 33–45.
- **Illustrative rows and signed fee amounts:** raw lines 47–73.
- **Standard and optional columns, including header-label discrepancy:** raw lines 75–105.

## Related

- [[adyen-reporting]]
- [[adyen-platforms]]
- [[source-adyen-docs-platforms-reports-and-fees-fee-report|Parallel Platforms-path fee-report reference]]
- [[source-adyen-docs-marketplaces-reports-and-fees-balance-platform-accounting-report|Balance Platform Accounting Report at a different grain]]

## Raw Sources

- [[raw/adyen/docs/marketplaces/reports-and-fees/fee-report/2026-09-15|Adyen Marketplace Balance Platform Fee Report — collected 2026-09-15]]
