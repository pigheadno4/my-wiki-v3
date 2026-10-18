---
title: "Adyen Platforms: view transfer details"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/view-transfers-details"
raw_files:
  - "adyen/docs/platforms/view-transfers-details/2026-09-15.md"
tags: [adyen, platforms, transfers, customer-area, reconciliation]
---

## Overview

This 2026-09-15 snapshot of Adyen for Platforms guidance shows how to inspect balance-platform transfers through Customer Area or the Transfers API, with webhooks recommended for recurring monitoring. It spans transfers related to payments and movements between balance accounts, as well as bank transfers in its examples. Transfer status and event history describe balance-platform operations; a displayed record alone does not prove beneficiary-bank receipt, legal ownership or a completed payout. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- **Transfer grain and states:** The page defines a transfer as a credit or debit involving a balance account. It sketches initiation by payment processing or movement between balance accounts, Adyen authorization, then capture for payment-related events or booking for other transfer events. The `GET /transfers/{id}` response table highlights amount/currency, incoming/outgoing direction, event history, internal reference and current status such as `received`, `authorised` or `booked`. These are distinct stages; a booked bank-transfer record does not establish that a recipient bank credited funds.
- **Access and viewing:** An Adyen for Platforms integration is required. The guide lists **TransferService Webservice Retrieve role** for Transfers API retrieval and **Balance platform base role** for Customer Area viewing. In Customer Area, use **Balances > Transfers** and filter one balance platform at a time; date, status and references help investigate. For payment-related transfers, filter with the PSP payment reference. A listed role or filter is not proof of access or a transaction outcome for a specific account.
- **API list and details:** `GET /transfers` returns matching records in `data` and next/previous pagination links in `_links`; the guide lists date, balance-account, account-holder and limit fields, says the date range must be less than six months, and says at least one unique identifier must be provided. Use `GET /transfers/{id}` to inspect one transfer by its transfer ID, or search by ID/description in Customer Area. The page's prose example spans May 2025 to May 2026 despite the six-month rule, while its curl example uses May 12–13, 2026 and no account identifier; consult the current API schema for an executable request rather than treating the example as resolving those conditions.
- **Example boundaries:** The `GET /transfers` sample includes a bank transfer and an internal transfer; the specific `GET /transfers/{id}` sample is an internal transfer. Its bank-transfer list item has `status=booked` alongside `reason=counterpartyAccountNotFound` and an estimated arrival time. These sample fields do not establish a normal final bank outcome or a canonical link to the separate detail example. Use actual transfer/webhook events and bank evidence for a real case.
- **Version and currency boundary:** Curl examples target test Balance Platform Transfers API v4; SDK snippets name Java 33.0.0, PHP 24.0.0, .NET 27.0.0, Node 23.3.0, Go 16.3.0, Python 13.3.0 and Ruby 10.1.1. Some snippets contain placeholders or malformed generated syntax. Their EUR/USD amounts and IDs are illustrative, not fee, exchange-rate or account-specific proof. The raw metadata says last modified in 2019 despite 2026-styled examples, so verify current behavior in the linked API reference.

## Detail locators

- Webhook preference, transfer definition and payment capture versus other booking: raw lines 19–34. Integration and role requirements: lines 35–43. Customer Area filters and PSP payment reference: lines 45–69.
- `GET /transfers` query fields, date/identifier constraints and inconsistent prose/curl examples: lines 71–100. Test v4/SDK snippets: lines 102–262. Pagination and list sample including bank and internal records: lines 264–474.
- Customer Area search and `GET /transfers/{id}` route: lines 476–641. Detail response fields and internal-transfer example: lines 643–737.

## Related

- [[adyen]] — provider context.
- [[adyen-platforms]] — platform, account-holder and balance-account context.
- [[source-adyen-docs-platforms-view-payout-transfers-details]] — payout-specific viewing route and role-gated confirmation letter.
- [[source-adyen-docs-platforms-payout-webhooks]] — payout transfer webhook lifecycle, tracking, failure and return context.

## Related raw API references

- The raw page links to Transfers API list/get operations, webhook setup, internal fund transfers and payment reconciliation. Check those sources independently for current schema and process details.

## Raw Sources

- [[raw/adyen/docs/platforms/view-transfers-details/2026-09-15|Adyen Docs: View transfer details (2026-09-15 snapshot)]]
