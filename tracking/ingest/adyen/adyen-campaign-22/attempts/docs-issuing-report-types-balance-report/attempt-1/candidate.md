---
title: "Adyen Issuing: Balance Platform Balance Report"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/report-types/balance-report"
raw_files:
  - "adyen/docs/issuing/report-types/balance-report/2026-09-15.md"
tags: [adyen, issuing, balance-platform, reporting, reconciliation]
---

## Overview

This 2022-modified, 2026-09-15-captured Issuing-path guide describes the Balance Platform Balance Report: a selected-day view of opening and closing balances by account holder, balance account and currency. It is used to reconcile balance snapshots across a platform; it is not an event-level transfer ledger or proof of external bank receipt. [[adyen]] [[adyen-reporting]] [[adyen-issuing]]

## Key takeaways

- The report includes an account-holder/balance-account/currency combination if its opening balance is nonzero or it has any movement between report opening and closing. Thus offsetting movements that return a zero opening balance to zero still appear; a nonzero opening with no movement appears; a zero opening and no movement does not. Absence of a row therefore does not prove the account does not exist. See raw lines 19 and 23-29.
- The report can be scheduled automatically or generated manually in Customer Area for a specific day. Its opening snapshot is 00:00 and closing snapshot is 00:00 the next day. The guide allows the balance platform's configured time zone or CET; comparison requires aligned dates and time zones. A generated report does not establish a current live balance or an individual transfer outcome. See raw lines 21 and 36-38.
- The standard column table identifies balance platform, account holder, balance account, and opening/closing balance currency, amount, date and time-zone fields, followed by ten reserved columns. The raw guide has incomplete descriptions for Opening Date and Closing Date, so rely on the stated day window and actual generated report fields for implementation. See raw lines 40-62.
- The linked sample CSV is a navigation target, not included in this pinned raw. The guide says the report generated for a specific balance platform can have additional data or columns beyond that sample. See raw lines 31-34.

## Detail locators

- Report grain and inclusion rule: raw lines 15-29.
- Generation modes, sample link, day boundary and time-zone selection: raw lines 21 and 31-38.
- Standard column names and types, including account identifiers and reserved columns: raw lines 40-62.

## Related

- [[adyen-reporting]] — main reporting concept and reciprocal source route.
- [[adyen-issuing]] — Issuing platform context.
- [[source-adyen-docs-platforms-reports-and-fees-balance-report]] — related Platforms-path guide to the same report type.

## Raw Sources

- [[raw/adyen/docs/issuing/report-types/balance-report/2026-09-15|Adyen Issuing Balance Report, captured 2026-09-15]]
