---
title: "Adyen External settlement detail report"
type: source
date_ingested: 2026-10-16
original_format: webpage
canonical_url: "https://docs.adyen.com/reporting/settlement-reconciliation/transaction-level/external-settlement-detail-report"
raw_files:
  - "adyen/docs/reporting/settlement-reconciliation/transaction-level/external-settlement-detail-report/2026-09-15.md"
tags: [adyen, reporting, external-acquirer, settlement, reconciliation]
---

## Overview

Adyen's External settlement detail report describes transactions for which Adyen is not the acquirer. The page gives direct American Express or PayPal funding arrangements as examples. It is a transaction-entry report for reviewing externally acquired settlement activity; a listed transaction does **not** confirm that the external acquirer has paid the merchant. This scope differs from the Adyen [[source-adyen-docs-reporting-settlement-reconciliation-transaction-level-settlement-details-report|Settlement details report]]. [[adyen]] [[adyen-reporting]]

## Key takeaways

- A report is available for company and merchant accounts, with a date selected in Customer Area. The report uses the account's time-zone setting; `Creation Date` has its own `TimeZone` field. The page links manual and automatic retrieval without specifying a generation schedule here.
- Each line under the header is a separate entry. The standard fields include company and merchant account, PSP and merchant references, payment method, creation date, journal `Type`, gross transaction currency and debit/credit amounts, exchange rate, net settlement currency and debit/credit amounts, acquirer fee fields, acquirer, MID, and matching references. One report can contain entries for multiple merchant accounts.
- Gross and net debit/credit values are separate fields; the net descriptions subtract acquirer fees from the submitted amount. Fee detail is conditional on information from the external acquirer: `Commission` holds the total when interchange-level detail is unavailable; when it is supplied, `Commission` is empty and `Markup`, `Scheme Fees`, and `Interchange` are populated. Do not infer a universal amount sign from a journal name alone; use the field and journal occurrence.
- Journal types distinguish externally settled payments, refunds, chargebacks, acquirer payouts, and unmatched entries, with debit, credit, or debit/credit occurrence as listed. An `AcquirerPayout` reference can be an acquirer settlement batch number found on a bank statement, but neither that row nor another listed transaction proves funds arrived.
- The sample is illustrative: a generated report can have additional data or columns based on account settings. Optional columns and order can be configured in Customer Area; changing them can affect automated consumers. The listed Merchant admin, Merchant report, Merchant financial, and Merchant POS Report roles are for configuring columns, not a stated universal prerequisite for receiving a report.

## Detail locators

- `## Structure > ### Entries`, line 39: row grain and explicit external-funding warning.
- `### Columns > #### Standard columns`, lines 49–78: account, reference, date/time-zone, type, gross and net amount/currency, fee, acquirer/MID, and installment fields. `Psp Reference` has different meanings for unmatched transactions and `AcquirerPayout`; `Modification Reference` may contain an acquirer reference for unmatched transactions.
- `#### Additional columns`, lines 80–92: optional store, merchant order, acquirer auth, card, submerchant, and metadata fields. The acquirer auth code is not unique and must not be used for reconciliation.
- `## Configure report columns`, lines 94–113: configuration steps, role list, and automated-system impact.
- `## Journal types`, lines 115–134: exact booking labels and debit/credit occurrences, including matched and unmatched external-acquirer entries.

## Related

- [[adyen-reporting]] — Adyen reporting route.
- [[source-adyen-docs-reporting-settlement-reconciliation-transaction-level-settlement-details-report]] — separate Adyen Settlement details report.

## Raw Sources

- [[raw/adyen/docs/reporting/settlement-reconciliation/transaction-level/external-settlement-detail-report/2026-09-15|Adyen External settlement detail report, fetched 2026-09-15]]
