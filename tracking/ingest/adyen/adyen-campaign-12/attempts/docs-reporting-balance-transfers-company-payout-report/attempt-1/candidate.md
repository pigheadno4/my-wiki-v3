---
title: "Adyen Company Payout report"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/balance-transfers/company-payout-report"
raw_files:
  - "adyen/docs/reporting/balance-transfers/company-payout-report/2026-09-15.md"
tags: [adyen, reporting, company-account, merchant-payouts, balance-transfers]
---

## Overview

Adyen's Company Payout report is available at the company-account level and summarizes merchant payout events: successful, returned and non-executed payouts, with status as of report generation. It is a company-account reporting view of merchant payouts, not a single company-level payout or proof that a particular bank account received funds. See [[adyen]], [[adyen-reporting]] and [[adyen-account-structure]] for provider, reporting and account-scope context.

## Key takeaways

- The Overview sheet records company account and generation time, counts by journal type, and MerchantPayout counts by executing partner bank, payout currency and status. The MerchantPayout sheet has one payout per row and includes merchant Account Code, bank, Currency, numeric Amount, Payable Number/batch, bank-instruction reference, Status, Status Date and optional Store Code. Adyen says the report's entries have a one-to-one relationship with merchant-account Settlement detail report entries; that is a reconciliation route, not a bank statement.
- Merchant payout statuses move through Created, Sent and Debit Confirmed toward Credited; Adyen calls Credited the final status for a successful payout. Forwarded is handed to another party; Rejected is final and rare; Failed means an attempt failed and the transfer will be returned or retried, so check a later report. The report records the status at generation time. A report status or bank-instruction reference should be checked against the actual bank statement when bank receipt matters.
- BankInstructionReturned has one returned merchant payout per row. Its Returned Date is when funds were booked back to Payable and is usually when they reached Adyen's bank account; Reason Code appears only when a partner bank provides one, and codes vary by currency and region. BalanceTransfer has one non-executed payout per row with a reason-code field. Here BalanceTransfer is the report's non-executed-payout journal type; the page does not make it evidence of an executed inter-account transfer.
- Each detailed sheet has its own Currency and numeric Amount columns; the source does not specify signed-amount conventions or monetary subunits, so interpret values with journal type and payout currency. Status Date and Returned Date mean different events. The report uses the account's configured reporting time zone; it does not state a universal CET/CEST rule.
- The page routes manual and automatic generation to separate guides and gives no role requirement on this page. Those linked procedures must be checked for access conditions.

## Detail locators

- Company-account availability, payout uses, snapshot status, retrieval and account time zone: raw lines 17–30. Sheet list and one-to-one Settlement detail route: `## Report structure`, lines 36–45.
- Overview counts, bank/currency/status grouping and status definitions: `## Overview sheet`, lines 47–100. One-payout row and field definitions: `## MerchantPayout sheet`, lines 102–125.
- Returned-payout grain, Returned Date and conditional reason code: `## BankInstructionReturned sheet`, lines 127–149. Non-executed-payout grain and fields: `## BalanceTransfer sheet`, lines 151–171.

## Related

- [[adyen]] — provider context.
- [[adyen-reporting]] — reporting and reconciliation routes.
- [[adyen-account-structure]] — company-account versus merchant-account scope.
- [[source-adyen-docs-reporting-settlement-reconciliation-transaction-level-settlement-details-report]] — merchant-account Settlement detail counterpart.

## Related raw API references

- The raw page links to manual and automatic report retrieval, the account time-zone setting, balance-transfer reasons and the merchant-account Settlement detail report. Details of those linked guides require their own source evidence.

## Raw Sources

- [[raw/adyen/docs/reporting/balance-transfers/company-payout-report/2026-09-15|Adyen Docs: Company Payout report (2026-09-15 snapshot)]]
