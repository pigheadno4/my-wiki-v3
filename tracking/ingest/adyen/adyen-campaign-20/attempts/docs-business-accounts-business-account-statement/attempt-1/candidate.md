---
title: "Account statements for business accounts | Adyen"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/business-accounts/business-account-statement"
raw_files:
  - "adyen/docs/business-accounts/business-account-statement/2026-09-15.md"
tags: [adyen, business-accounts, platforms, statements, camt053, reconciliation]
---

## Overview

This [[adyen]] Business Accounts guide, last modified and captured 2026-09-15, describes automatically generated ISO 20022 CAMT.053 account statements for a business account over a reporting period. Platforms can download them to reconcile balances and report transactions to users. Card transactions appear when an Adyen-issued card shares the balance account. See [[adyen-business-accounts]].

## Key takeaways

- The prerequisites are an Adyen for Platforms integration supporting business accounts, a balance-platform Report user API key with the Merchant Report Download role, a server subscribed to `balancePlatform.report.created`, and Adyen-contact enablement plus statement settings. This is a configured reporting flow, not evidence that a particular account is open, funded or producing statements. [Raw: lines 23–45]
- The settings cover daily, monthly or both frequencies; value versus booking date; optional BAI classification; transaction summary; and an optional extra daily summarized CAMT.053 file. The settings row calls the summary included by default, while the later comparison says a standard statement includes `TxsSummry` when configured. Preserve that configuration wording discrepancy rather than assuming universal presence. [Raw: lines 35–45, 473–484]
- When a statement is ready, `balancePlatform.report.created` provides the balance-account object, filename and `downloadUrl`; download the file with an authenticated GET request using the report-user API key. The live webhook and test URL in examples illustrate different environments and do not prove a successful download in either one. [Raw: lines 47–90]
- CAMT.053 has a group header and one or more statement blocks; each `Stmt` represents one account and currency. It describes account identity, booked or available balance according to configuration, booked debit/credit entries, optional summary totals and transfer references. Use the element tables and mapping tables for exact XML tags and ISO 20022/optional BAI codes. [Raw: lines 95–263, 318–469]
- The optional daily summarized file groups transactions sharing a BAI code into one `Ntry` with aggregated amounts; it does not preserve one entry per underlying transaction. Its `TxsSummry` is always included according to this page, and `ElctrncSeqNb` can cross-reference the detailed file. [Raw: lines 473–537]

## Detail locators

- Setup and settings: raw lines 23–45. Webhook/download flow and environment-specific examples: lines 47–90.
- CAMT.053 hierarchy, account identifiers, balances, entries, summaries and transfer references: lines 95–263.
- ISO 20022 code hierarchy, Transfers API mapping, optional BAI mappings and linked Issuing card activity: lines 318–469.
- Standard versus optional summarized file, aggregation and fields: lines 473–537.

## Related

- [[adyen-business-accounts]] — business-account product and evidence boundary.
- [[source-adyen-docs-platforms-compliance-financial-products-account-statements]] — separate user-facing statement compliance guidance for Business Accounts and Issuing; the CAMT.053 download flow does not establish that a user-facing template was approved or delivered.

## Raw Sources

- [[raw/adyen/docs/business-accounts/business-account-statement/2026-09-15|Adyen account statements for business accounts — collected 2026-09-15]]
