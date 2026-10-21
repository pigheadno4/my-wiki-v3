---
title: "Adyen Marketplace Balance Platform Statement report"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/reports-and-fees/statement-report"
raw_files:
  - "adyen/docs/marketplaces/reports-and-fees/statement-report/2026-09-15.md"
tags: [adyen, marketplaces, platforms, reporting, balance-accounts, reconciliation]
---

## Overview

This 2026-09-15-captured [[adyen]] Marketplace field guide describes the **daily Balance Platform Statement Report** in [[adyen-reporting]]. It presents starting balance, balance-changing transactions and ending balance for available currencies and included balance accounts, as an alternative way to track daily balance changes to the Balance Platform Accounting Report and to find transactions included in scheduled or on-demand payouts. A balance account with **both opening and ending balance zero is omitted**; absence from this report alone cannot prove no intraday activity or no account.

## Key takeaways

- Customer Area can generate the Statement Report automatically on a schedule or manually for a specific day. The linked sample CSV is illustrative; a report generated for a balance platform can contain extra data or columns according to its settings. This page does not specify a cutoff time, retrieval retention or a service role. See raw lines 19–32.
- The report columns identify Balance Platform, Account Holder and Balance Account separately. Category/Type/Status describe the balance-changing event; listed categories include bank, card, grants, internal, issuedCard, platformPayment, topUp and upgrade. **Transfer Id** identifies a pending debit/credit, while **Transaction Id** identifies a completed debit/credit. PSP payment and modification merchant/PSP references are distinct fields. `Reference` and `Description` both carry the same “unique identifier of a pending debit or credit” description in this raw table, so that repeated wording is not a reliable join rule by itself. See raw lines 38–58.
- **Booking Date** is when booking happened; **Value Date** is when funds become available. Each has its own time-zone field. `Amount` is typed **Alpha text** and described only as the transfer/transaction amount; separate starting/ending balance currencies and values define the balance frame. The page does not define amount sign semantics or numeric parsing guarantees. See raw lines 59–68.
- The report can help trace balance changes and payouts, but it does not show a beneficiary bank-credit status, a payout return outcome or a bank statement. A completed Transaction Id is completed balance-account debit/credit at this report grain, not proof that a recipient bank received funds. Reserved columns 25–34 have no current defined behavior. See raw lines 19–24 and 69–78.

## Detail locators

- Daily purpose, zero-to-zero account omission, generation and sample variation: raw lines 17–32.
- Account identifiers, event category/type/status, pending/completed IDs and PSP references: raw lines 34–58.
- Booking versus value dates/time zones, currencies, amount and balances: raw lines 59–68.
- Reserved future columns: raw lines 69–78.

## Related

- [[adyen]] — provider profile.
- [[adyen-reporting]] — canonical reporting and reconciliation concept.
- [[adyen-platforms]] — modern platform balance-account context.
- [[source-adyen-docs-platforms-reports-and-fees-statement-report]] — separate Platforms URL for the analogous field guide.
- [[source-adyen-docs-marketplaces-reports-and-fees-balance-platform-accounting-report]] — detailed balance-event report.
- [[source-adyen-docs-marketplaces-payout-webhooks]] — payout transfer and bank-status route.

## Raw Sources

- [[raw/adyen/docs/marketplaces/reports-and-fees/statement-report/2026-09-15|Marketplace Balance Platform Statement report — pinned 2026-09-15 raw snapshot]]
