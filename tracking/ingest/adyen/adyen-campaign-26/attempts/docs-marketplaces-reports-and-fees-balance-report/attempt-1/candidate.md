---
title: "Marketplace Balance Platform Balance Report"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/reports-and-fees/balance-report"
raw_files:
  - "adyen/docs/marketplaces/reports-and-fees/balance-report/2026-09-15.md"
tags: [adyen, marketplaces, reporting, balances, reconciliation]
---

## Overview

This 2026-09-15 [[adyen]] Marketplace guide describes a Balance Platform Balance Report of opening and closing balance snapshots by account holder, balance account and currency for a selected day. It can help reconcile account balances but is not a transaction ledger, proof of a current live balance or evidence that funds reached an external bank. [[adyen-reporting]]

## Key takeaways

- A balance-account currency appears when its opening balance is nonzero **or** funds moved during the report window. The examples include a zero-opening/zero-closing account with offsetting movements and a nonzero-opening account with no movement; a zero-opening/zero-closing account without movement is omitted. Absence therefore does not establish that the account does not exist, and net balance change does not reveal all gross movements. See raw lines 19–29.
- The report can be generated on a schedule or manually in Customer Area for a specific day. It uses 00:00 opening and 00:00 the next day closing balances, with either the balance platform's configured timezone or CET. The sample rows use CEST, so align the selected reporting timezone before comparing periods. See raw lines 21, 31–46.
- The field table identifies platform, account holder, balance account, opening/closing currency, amount, timestamp and timezone, plus reserved columns. The sample headers say `Opening Time` and `Closing Time`, while the structure table calls the corresponding fields `Opening TimeZone` and `Closing TimeZone`. Generated reports may contain additional data or columns depending on platform settings; inspect the actual export header. See raw lines 31–70.
- A snapshot row has no individual transaction ID or transfer-status field in the listed structure. Use event-level accounting or transaction evidence for particular movements; this report alone does not establish payout settlement or beneficiary bank receipt. See raw lines 44–70.

## Detail locators

- **Purpose, row-inclusion rule and generation choices:** raw lines 15–23.
- **Zero/offsetting movement examples:** raw lines 25–29.
- **Sample currencies and CEST-labelled headers:** raw lines 31–42.
- **Daily window, timezone choice, standard and reserved fields:** raw lines 44–70.

## Related

- [[adyen-reporting]]
- [[adyen-platforms]]
- [[source-adyen-docs-platforms-reports-and-fees-balance-report|Parallel Platforms-path balance-report reference]]
- [[source-adyen-docs-marketplaces-reports-and-fees-balance-platform-accounting-report|Event-level accounting report reference]]

## Raw Sources

- [[raw/adyen/docs/marketplaces/reports-and-fees/balance-report/2026-09-15|Adyen Marketplace Balance Platform Balance Report — collected 2026-09-15]]
