---
title: "Adyen Transfers API transaction detail"
type: source
date_ingested: 2026-11-07
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/transfers/latest/get/transactions/(id)"
raw_files:
  - "adyen/api-explorer/transfers/latest/get/transactions/(id)/2026-11-07.md"
tags: [adyen, transfers-api, transactions, balance-platform]
---

## Overview

Captured Transfers API v4 TEST `GET /transactions/{id}` reference for reading one balance-account transaction by its transaction ID. This is a transaction record, distinct from a transfer request and from recipient-bank receipt. Versions 1 and 2 of the Transfers API are marked deprecated in this reference. See [[adyen]] and [[adyen-platforms]].

## Key takeaways

- Required path `id` is the unique transaction identifier. The captured server is `https://balanceplatform-api-test.adyen.com/btl/v4`. This GET reference gives no request body, query inputs, defaults, limits, idempotency rule, or operation-specific API role.
- The `200` schema requires `accountHolder`, `amount` (currency and signed numeric value in minor units), `balanceAccount`, `balancePlatform`, `bookingDate`, transaction `id`, `status`, and `valueDate`. Nested holder/account IDs are optional in the table. Optional `paymentInstrument`, `transfer`, beneficiary reference, creation date and description provide context when present; the optional transfer object's `reference` is marked required within that object.
- Transaction `status` is `pending` or `booked`; booked means booked to the balance account. `bookingDate` names the booking date and `valueDate` the date the transfer amount becomes available in the balance account. The schema lists both dates as required even though `pending` is possible; it does not explain their values for a pending record. A booked balance-account transaction is not proof of external recipient-bank receipt.
- Documented errors are 401 authentication required, 403 insufficient permissions, 422 request validation, and 500 server processing failure. Consult the raw tables for error-body requiredness and nested validation fields. The `200` example is illustrative, not a guarantee of transfer category, amount, status or optional identifiers.

## Detail locators

- Identity, deprecation notice and TEST v4 server: raw lines 5–12.
- Required transaction path ID: raw lines 14–19.
- Success schema, identity, status and dates: raw lines 21–56.
- Error schemas and conditions: raw lines 59–136.
- Illustrative booked transaction: raw lines 138–168.

## Related

- [[adyen-platforms]] — balance-account and transfer context.
- [[adyen]] — provider index.

## Raw Sources

- [[raw/adyen/api-explorer/transfers/latest/get/transactions/(id)/2026-11-07|Transfers API transaction detail, captured 2026-11-07]]
