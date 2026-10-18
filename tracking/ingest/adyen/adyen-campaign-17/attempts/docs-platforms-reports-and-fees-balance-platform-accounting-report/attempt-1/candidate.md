---
title: "Balance Platform Accounting Report | Adyen Docs"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/reports-and-fees/balance-platform-accounting-report"
raw_files:
  - "adyen/docs/platforms/reports-and-fees/balance-platform-accounting-report/2026-09-15.md"
tags: [adyen, platforms, accounting-report, reconciliation, balance-accounts]
---

## Overview

Adyen's Balance Platform Accounting Report is a daily balance-platform report of balance changes across liable and user balance accounts. Customer Area can generate it on a schedule or for a selected day; the manually generated Interactive Report provides the same type of data with a date range and account/event filters. The page describes platform payments, internal movements, payouts, issuing and other financial events, and says API responses/webhooks are preferable for real-time individual-transaction tracking before daily report reconciliation. This 2026-09-15 capture reports `last_modified` 2023-06-14. Report rows describe Adyen balance-platform accounting events, not independent proof of beneficiary-bank receipt, current account state, legal fund ownership, or finalized financial statements. [[adyen]] [[adyen-reporting]] [[adyen-platforms]]

## Key takeaways

- **Grain and state:** The report includes events on the day their status update occurred, with `Category`, `Type` and `Status` identifying what changed. A `Transfer Id` identifies a pending debit/credit flow; a booked balance transaction has a `Transaction Id`. Within a flow, transactions can be linked to transfers by `Transfer Id`, but refunds start a new transfer flow and ID rather than reusing the original payment's transfer ID. A received or authorised row alone does not show a booked balance movement. Category/status mappings differ for `platformPayment`, `internal`, `bank`, `issuedCard`, `topUp` and other categories; use the exact mapping instead of treating every `booked` or `received` label as the same external outcome.
- **Period and dates:** The selected daily report covers balance mutations with a `Booking Date` from 00:00 to the next 00:00 in the page's stated CET window. `Booking Date` identifies when the event occurred; `Value Date` identifies the balance-effect/availability date, which can be later, equal, or earlier. The standard columns also expose booking/value-date time-zone fields, and the examples display CEST. Keep report-period selection, row time-zone values and value-date timing distinct; the source does not specify a conversion algorithm for reconciling those labels. Balance accounts with no transactions do not appear.
- **Amounts and joins:** Standard fields distinguish balance-platform/account-holder/balance-account IDs, pending `Transfer Id`, booked `Transaction Id`, category/type/status, payment and balance-account currencies, and movements in the `Received (PC)`, `Reserved (PC)` and `Balance (PC)` registers. The capture and refund examples show signed shifts across those registers and opposite directions for a sale credit versus refund debit; use the row's category/status/account and sign rather than assigning a universal sign meaning. The examples provide PSP payment and modification references, merchant references and a counterparty balance-account ID where applicable. These are separate identifiers; the source does not define a universal cross-report join or payout-bank confirmation algorithm.
- **Scope and configuration:** The standard-column table spans platform payments, payouts and issuing and notes service-specific columns. Additional columns are excluded by default and can be added in Customer Area. `Exchange Rate`, `Store`, `Payment Method` and `Platform Payment Split Type` are among them; the split-type table defines BalanceAccount, Commission, fees, Remainder, Surcharge, Tip, TopUp and DCCMarkup routes. Do not use the optional `Issued Card Scheme Fee` columns: the table explicitly marks them **Do not use this column**. Generated reports may contain extra data or columns beyond the downloadable sample, depending on balance-platform settings.
- **Outcome boundary and source tensions:** The page says the report can help confirm processed payments, internal transfers and payouts to users' bank accounts, but its bank `bankTransfer/booked` mapping describes a debit or credit of the balance account; that row alone does not establish the beneficiary bank credited an account. A bank transfer may also be returned. The top-up example's three rows all say `received` with blank Transaction Id, yet later rows display nonzero Reserved/Balance register changes; this conflicts with the page's general statement that a missing Transaction Id means no money movement. Treat the example as illustrative and verify live rows and related API/webhook evidence before applying a reconciliation rule. The page gives no Customer Area role list; its generation link is a separate access source.

## Detail locators

- Daily/interactive report purpose and real-time versus daily reconciliation: pinned raw lines 15–40.
- Pending transfer versus booked transaction identity, new refund transfer ID, category/type/status and status-date grain: pinned raw lines 42–69.
- Bank/internal/platform-payment/top-up event mappings, including returns and different status semantics: pinned raw lines 73–198.
- Value-date explanation/example and CET daily report window: pinned raw lines 200–220.
- Standard identifiers, dates/time zones, currencies, three PC register fields, PSP references, counterparty and optional columns: pinned raw lines 222–347.
- Split-type definitions and service-specific booking purposes: pinned raw lines 349–371.
- Signed capture, refund, chargeback, internal-transfer, payout and top-up examples: pinned raw lines 373–437.

## Related

- [[adyen-reporting]] — report discovery and evidence boundary.
- [[adyen-platforms]] — liable/user balance-account context.
- [[source-adyen-docs-reporting-platform-reports]] — platform report catalog and classic Marketplace distinction.
- [[source-adyen-docs-reporting-manually-get-reports]] — separate Customer Area generation/access route.

## Raw Sources

- [[raw/adyen/docs/platforms/reports-and-fees/balance-platform-accounting-report/2026-09-15|Balance Platform Accounting Report — 2026-09-15 snapshot]]
