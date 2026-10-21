---
title: "Adyen Marketplace payout transfer details"
type: source
date_ingested: 2026-10-21
original_format: webpage
canonical_url: "https://docs.adyen.com/marketplaces/view-payout-transfers-details"
raw_files:
  - "adyen/docs/marketplaces/view-payout-transfers-details/2026-09-15.md"
tags: [adyen, marketplaces, payouts, transfers, customer-area]
---

## Overview

This 2026-09-15 Marketplace-path [[adyen]] guide explains how an Adyen for Platforms operator views payout-related transfer records in Customer Area or with the Transfers API and obtains a bank-transfer confirmation letter. It recommends webhooks for recurring transfer tracking. A balance-platform transfer records funds credited or debited to a balance account; a list can include bank and internal transfers, so a viewed record must be interpreted by its own type and state. See [[adyen-platforms]].

## Key takeaways

- **Prerequisites and sequence:** The guide requires an Adyen for Platforms integration and the `TransferService Webservice Retrieve role` for API reads. Customer Area transfer viewing requires the Balance platform base role; downloading a letter requires the Download transfer confirmation letter role, and unmasked letter PII additionally requires View bank transfers PII. Payout-related transfers are initiated by a payout schedule, cashout or on-demand request, then authorized by Adyen and booked; initiation or authorization alone does not establish booking or bank receipt. See pinned raw lines 19–45.
- **List and inspect:** Customer Area uses Balances > Transfers and shows one balance platform at a time, with date/status/reference filters; the page illustrates a Failed + Bank transfer filter to investigate rejected payouts. `GET /transfers` returns matching data and pagination links, with creation-time and account-holder/balance-account filters. For a particular transfer, search Customer Area by ID/description or call `GET /transfers/{id}`. The response highlights amount/currency, direction, events, reference and status such as received, authorised or booked. See pinned raw lines 47–82, 263–268 and 475–650.
- **List-request contradiction:** The query table states that `createdSince` and `createdUntil` must be less than six months apart, and the text says to provide at least one unique identifier. Its example prose instead describes May 2025 to May 2026, while the test curl request uses a one-day interval and no account-holder or balance-account identifier. Do not treat the examples as an executable validation of those stated requirements; check the versioned Transfers API contract. See pinned raw lines 74–98.
- **Transfer identity and bank boundary:** The list response samples one `bankTransfer` and one `internalTransfer`, while the detailed `GET /transfers/{id}` example is an `internalTransfer`. A `booked` balance-account debit and the example's estimated arrival time are not evidence that a beneficiary bank credited funds. For a booked bank transfer, an authorized Customer Area user can download a PDF letter; it confirms that Adyen sent the instruction to carry out the transfer, not that the beneficiary received it. Without View bank transfers PII, letter PII is masked. See pinned raw lines 270–473, 642–740 and 754–779.
- **Example boundary:** Curl samples use test Balance Platform Transfers API v4. SDK snippets identify library versions and contain placeholders, so treat them as illustrative and verify request syntax and roles against the linked API reference. See pinned raw lines 91–260 and 500–640.

## Detail locators

- Transfer lifecycle, viewing channels and roles: pinned raw lines 19–45.
- Customer Area listing, failure filter and API list-request constraints/examples: pinned raw lines 47–98.
- SDK list samples, pagination and bank/internal response examples: pinned raw lines 101–473.
- Customer Area search, single-transfer API call, response fields and internal-transfer example: pinned raw lines 475–736.
- Letter meaning, contents, PII/role gates and download procedure: pinned raw lines 738–779.

## Related

- [[adyen-platforms]] — reciprocal platform concept.
- [[source-adyen-docs-platforms-view-payout-transfers-details]] — same dated guide under the Platforms path.
- [[source-adyen-docs-marketplaces-payout-webhooks]] — separate webhook states for payout tracking and return.

## Raw Sources

- [[raw/adyen/docs/marketplaces/view-payout-transfers-details/2026-09-15|Marketplace payout transfer details, captured 2026-09-15]]
