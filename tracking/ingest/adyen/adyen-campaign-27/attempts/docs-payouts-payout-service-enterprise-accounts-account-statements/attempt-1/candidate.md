---
title: "Adyen Payout Service enterprise-account CAMT.053 statements"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/payouts/payout-service/enterprise-accounts/account-statements"
raw_files:
  - "adyen/docs/payouts/payout-service/enterprise-accounts/account-statements/2026-09-15.md"
tags: [adyen, payout-service, enterprise-accounts, camt053, reporting]
---

## Overview

This 2026-09-15 [[adyen]] Payout Service guide covers CAMT.053 ISO 20022 account statements for an enterprise account. A statement summarizes account activity over a configured daily or monthly period for reconciliation and user transaction reporting; linked Adyen-issued-card activity can appear when the card shares the balance account. This is distinct from a Marketplace or Platforms Balance Platform Statement Report. See [[adyen-reporting]].

## Key takeaways

- **Product and access gates:** The guide requires a Payouts integration and enterprise account. An Adyen contact must enable the feature and configure its statement settings. The balance-platform Report user API key needs the Merchant Report Download role, and the server must receive/accept the subscribed `balancePlatform.report.created` webhook. Required settings choose daily, monthly or both timeframe and value-date or booking-date transaction basis; BAI codes and an extra summarized daily file are optional, while transaction summary is included by default. These are setup requirements, not proof of a particular account's eligibility or produced file. See pinned raw lines 23–45.
- **Availability and retrieval:** Adyen automatically generates statements and sends `balancePlatform.report.created` with `balanceAccount`, `fileName` and `downloadUrl`; download is a separate authenticated GET to that URL. The webhook example is live, whereas the curl example targets test and a different filename, so treat them as independent illustrations rather than one executed flow. A notification or URL does not establish that the file was fetched or its contents reconciled. See pinned raw lines 47–91.
- **Statement grain and balances:** A CAMT.053 file can contain multiple `<Stmt>` blocks; each block represents one account and one currency and identifies its reporting period. Balance blocks can report either booked opening/closing codes (`OPBD`/`CLBD`) or available ones (`OPAV`/`CLAV`) depending on configuration. Standard `<Ntry>` records are booked credit/debit entries with booking and value dates, and transaction details carry the Adyen transfer ID and platform/beneficiary references for matching. Do not equate available, booked and recipient-bank balances. See pinned raw lines 95–265.
- **Classification and aggregation:** Each entry has an ISO 20022 Bank Transaction Code; the guide maps Transfers API category/type/priority and direction to domain/family/subfamily codes, including bank, internal, top-up and issued-card cases. Optional BAI codes add another classification, including booked versus returned/rejected mappings. If enabled, an additional daily summarized CAMT.053 file replaces per-transaction entries with one `<Ntry>` per BAI-code group and date-only fields; use the detailed file for transaction-level reconciliation. See pinned raw lines 324–537.
- **Evidence boundary:** The sample XML is illustrative and shows an opening booked balance and one entry; its omission of other elements should not override the element definitions or selected configuration. A booked statement entry records enterprise-account activity, not proof of external beneficiary-bank receipt or final accounting sign-off. See pinned raw lines 267–322.

## Detail locators

- CAMT.053 purpose, Payout Service/enterprise-account requirements and configurable settings: pinned raw lines 15–45.
- Automatic generation, report-created fields and example GET: pinned raw lines 47–91.
- XML hierarchy, group header, account/currency statement, balances, entries, summaries and transfer references: pinned raw lines 95–265.
- Example XML and ISO/Transfers API code mapping: pinned raw lines 267–407.
- Optional BAI mapping and standard versus summarized statement grain: pinned raw lines 409–537.

## Related

- [[adyen-reporting]] — reciprocal reporting concept; this source is specifically Payout Service enterprise-account CAMT.053.
- [[adyen-business-accounts]] — nearby account-product context, not an interchangeable statement format.

## Raw Sources

- [[raw/adyen/docs/payouts/payout-service/enterprise-accounts/account-statements/2026-09-15|Payout Service enterprise-account statements, captured 2026-09-15]]
