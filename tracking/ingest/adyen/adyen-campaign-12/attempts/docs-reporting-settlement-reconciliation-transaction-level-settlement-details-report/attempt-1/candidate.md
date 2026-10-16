---
title: "Adyen Settlement details report"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/settlement-reconciliation/transaction-level/settlement-details-report"
raw_files:
  - "adyen/docs/reporting/settlement-reconciliation/transaction-level/settlement-details-report/2026-09-15.md"
tags: [adyen, reporting, settlement, reconciliation, payouts]
---

## Overview

This [[adyen]] Settlement details report reference describes merchant-account settlement data for transaction-level reconciliation, including the costs of each transaction and entries for related batch activity. It covers payments Adyen says have been settled and paid out, but the report and its example payout row are reporting evidence, not independent proof that a particular bank account received final funds. See [[adyen-reporting]] for the provider reporting route.

## Key takeaways

- The report can cover one or multiple selected merchant accounts. The default generation is per merchant account, per batch; existing generation settings and schedules remain unchanged. Manual generation, scheduled generation, and downloading require either **Merchant Report** or **Generate key financial reports** for each merchant account included. Manual filtering offers a date or, only for the current account, a single batch; schedules offer daily, weekly, monthly, or batch close. [Raw: Generate and download reports, lines 31–103]
- Under the header, each line is a separate entry. The examples include transaction statuses such as **Settled** and **Chargeback**, monthly transaction-fee entries for months represented in the batch, deposit and Reserve corrections, invoice deductions/credits, and **MerchantPayout** entries. The payout entry carries a reference, batch number, and bank-account information; use the bank-statement message for reconciliation, without treating the example as a guarantee of receipt. [Raw: Report structure > Entries, lines 130–199]
- Standard columns identify company and merchant accounts, PSP and merchant references, method, creation date, journal **Type**, modification reference, transaction **Gross Currency** and gross debit/credit, settlement **Net Currency** and net debit/credit, fee fields, variant, and batch number. Gross amounts describe the submitted transaction; net debit/credit describe the payable batch. The report uses the account time-zone setting, while column-level date and time-zone fields have their own meanings. [Raw: Time zone, line 25; Standard columns, lines 204–244]
- Fee interpretation is conditional: when interchange-level information is provided, **Commission** is empty and **Markup**, **Scheme Fees**, and **Interchange** are populated; otherwise the total is in **Commission** and those component columns are empty. Commission can be negative for externally settled refunds, so automated reconciliation must handle negative values. For externally settled payments, **Exchange Rate** is Adyen's reference rate, not the external acquirer's actual rate. [Raw: Standard columns, lines 225–235]
- Additional columns and their order can be configured. A generated report may contain columns absent from the sample; changing configured columns can affect automated consumers. Journal **Type** supplies booking meanings and debit/credit direction, including return and reversal entries. A **MerchantPayout** debit from the payout batch and a **BankInstructionReturned** credit have different meanings; do not infer financial finality from a single row. [Raw: Sample report, lines 124–128; Configure report columns, lines 301–319; Journal types, lines 322–365]
- This is a 2026-09-15 raw snapshot with source metadata last modified in 2022. It does not establish current access, a particular account's report output, or completed bank settlement.

## Detail locators

- Account selection, roles, manual and scheduled generation, download, file types and naming: `Generate and download reports`, lines 31–122.
- Row grain and entry examples: `Report structure > Entries`, lines 130–199.
- Standard identity, date, gross/net, fee, and batch fields: `Report structure > Columns > Standard columns`, lines 200–244.
- Optional time-zone, balance-platform, payment-fee, split, installment and POS fields: `Additional columns`, lines 246–299; conditions remain field-specific.
- Column configuration roles and automated-consumer warning: `Configure report columns`, lines 301–319.
- Booking types, debit/credit direction, installment and Sales Day payout exceptions: `Journal types`, lines 322–365.

## Related

- [[adyen]] — provider page.
- [[adyen-reporting]] — reporting and reconciliation concept route.

## Raw Sources

- [[raw/adyen/docs/reporting/settlement-reconciliation/transaction-level/settlement-details-report/2026-09-15|Adyen Settlement details report (2026-09-15)]]
