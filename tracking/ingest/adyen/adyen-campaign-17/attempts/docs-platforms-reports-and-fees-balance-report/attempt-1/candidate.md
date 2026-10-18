---
title: "Adyen Balance Platform Balance Report"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/reports-and-fees/balance-report"
raw_files:
  - "adyen/docs/platforms/reports-and-fees/balance-report/2026-09-15.md"
tags: [adyen, platforms, reporting, balances, reconciliation]
---

## Overview

This 2026-09-15 Adyen Balance Platform Balance Report guide describes opening and closing balance snapshots by account holder, balance account and currency for a selected day. The report includes an account/currency when the opening balance is nonzero or funds moved during the report window, even if the closing balance returns to zero. It is a balance reconciliation view, not a list of individual transfers or proof of external bank receipt. See [[adyen]], [[adyen-platforms]] and [[adyen-reporting]].

## Key takeaways

- **Selection rule:** Include a balance-account currency with a nonzero opening balance or any movement between the opening and closing dates. Thus a zero-opening/zero-closing account with offsetting movements is present, a nonzero opening with no movements is present, and zero opening/zero closing with no movements is absent. Absence from this report does not prove an account does not exist. A net opening-to-closing difference cannot reconstruct gross transfers when movements offset.
- **Generation and time window:** The report can be generated automatically on a schedule or manually in Customer Area for a specific day. It samples 00:00 opening and 00:00 the next day closing, in either the balance platform's configured time zone or CET. Compare periods only after matching their date and time-zone basis; the example rows use CEST. Report generation or a balance snapshot does not establish a live current balance or an individual transaction outcome.
- **Columns and sample limits:** Standard fields identify balance platform, account holder and balance account; opening/closing currency, amount, date and timezone; plus ten reserved future columns. The displayed sample headers say Opening Time and Closing Time, while the standard-column table calls those fields Opening TimeZone and Closing TimeZone. The page also says an actual generated report may add data or columns based on platform settings. Use the actual report header and time-zone values rather than assuming an exact sample schema.
- **Evidence boundary:** This report presents balance snapshots and inclusion examples. It does not expose individual transaction IDs, transfer status, payout settlement, legal fund ownership or beneficiary bank receipt. Use accounting/transaction evidence for movements and external bank evidence for a claimed payout arrival.

## Detail locators

- Purpose, row selection and schedule/manual generation: pinned raw lines 15-23.
- Zero/offsetting and no-movement inclusion examples: pinned raw lines 25-29.
- Sample rows, currencies and CEST labels: pinned raw lines 31-42.
- 00:00-to-next-00:00 period, selectable time zone and field definitions: pinned raw lines 44-70.

## Related

- [[adyen-reporting]] — main reporting concept and reciprocal source route.
- [[adyen-platforms]] — platform/account-holder context.
- [[source-adyen-docs-platforms-reports-and-fees-balance-platform-accounting-report]] — event-level balance-change report.
- [[source-adyen-docs-platforms-reports-and-fees-payout-report]] — payout report at a different grain.

## Raw Sources

- [[raw/adyen/docs/platforms/reports-and-fees/balance-report/2026-09-15|Adyen Balance Platform Balance Report, captured 2026-09-15]]
