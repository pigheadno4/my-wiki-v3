---
title: "Adyen Advancements Detail Report"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/settlement-reconciliation/transaction-level/advancements-detail-report"
raw_files:
  - "adyen/docs/reporting/settlement-reconciliation/transaction-level/advancements-detail-report/2026-09-15.md"
tags: [adyen, reporting, advancements, installments, reconciliation]
---

## Overview

Adyen's Advancements Detail Report identifies the installments used to determine an amount advanced to a merchant and presents transaction-level funding details where Adyen can identify the installments. The report is available only where Adyen offers the Advancement Product, is generated for a merchant account and advancement code, and can also contain bulk entries when individual installments cannot be identified. See [[adyen]] and [[adyen-reporting]] for provider and reporting context. This report is advancement evidence; its rows alone do not establish payment settlement or independently verify a bank deposit.

## Key takeaways

- The report is merchant-account scoped even though one advancement operation code may cover merchant accounts under the same legal-entity number. Consult each relevant merchant account's report to obtain the operation total; do not treat one report's total as the legal entity's total. The filename embeds the code, first accounting-registration date and report-request date; separately requested days do not overwrite older versions.
- Transaction entries are AdvancedInstallment or AdvancedInstallmentCancelled. AdvancedBulk and AdvancedBulkCancelled represent amounts Adyen cannot attribute to individual installments; bulk entries therefore cannot be treated as complete transaction-level linkage and have no estimated commission in the Commission column. The final Advancement row totals gross (in Advanced (NC)), net and advancement cost for that code and merchant account; Adyen describes this row as where the amount received in the related bank account appears.
- Keep Gross Currency and Gross Debit/Credit (GC, payment currency) separate from Net Currency and Net Debit/Credit (NC, settlement currency). Debit and credit have separate columns; cancellation rows describe amounts no longer advanced. Net credit/debit examples account for advancement fee. The installment advancement cost is calculated and can round; the Advancement row gives actual total cost and carries a rounding-difference correction. Do not infer a universal signed amount or convert these report fields into a settlement result.
- Commission (NC) is an aggregated estimated amount for an identifiable installment. Markup, Scheme Fees and Interchange columns are empty because the report's events are not settlement events. Additional columns and order can vary with account settings; changing report column configuration may affect automated consumers.
- The report is currently CET/CEST only, including Creation Date's TimeZone field. Access is limited to merchant accounts: generating or downloading requires the See installments reports role on every merchant account included. An unrecognized advancement code in manual generation may yield an empty report.

## Detail locators

- Eligibility, time zone and merchant-account availability: raw lines 17–29. Filename, legal-entity code scope and date meanings: `## File name format`, lines 31–48.
- Manual/automatic generation, role and empty-code warning: `## Generate and download reports`, lines 55–103. Sample and account-dependent columns: lines 105–109.
- Transaction, bulk and total row grains: `### Entries`, lines 113–127. Standard currency, debit/credit, fee, time-zone and rounding fields: `#### Standard columns`, lines 133–169. Optional partial-advancement fields and configuration impact: lines 171–195.
- Exact journal meanings, cancellation conditions, bulk attribution limit and Advancement total: `## Journal types`, lines 197–207.

## Related

- [[adyen]] — provider context.
- [[adyen-reporting]] — reporting concept and other report routes.
- [[adyen-account-structure]] — merchant-account scope and access hierarchy.

## Related raw API references

- The raw See also section links to installments and advancements in Brazil, transaction-level reconciliation, balance transfers, DCC and sales-day closing (lines 209–215). Those destinations are navigation until read separately.

## Raw Sources

- [[raw/adyen/docs/reporting/settlement-reconciliation/transaction-level/advancements-detail-report/2026-09-15|Adyen Docs: Advancements detail report (2026-09-15 snapshot)]]
