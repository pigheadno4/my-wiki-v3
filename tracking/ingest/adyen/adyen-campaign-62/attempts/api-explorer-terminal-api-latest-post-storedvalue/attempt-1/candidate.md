---
title: "Adyen Terminal API POST /storedvalue — StoredValue Request"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/terminal-api/latest/post/storedvalue"
raw_files:
  - "adyen/api-explorer/terminal-api/latest/post/storedvalue/2026-09-15.md"
tags: [adyen, terminal-api, api-explorer, stored-value]
---

## Overview

Captured API Explorer contract for `POST /storedvalue`, a Terminal API request carrying information for a stored-value transaction. The request can specify `Reserve`, `Activate`, `Load`, `Unload`, `Reverse`, or `Duplicate`; the page does not describe these as interchangeable with a payment reversal. The URL uses `latest` and does not pin a numbered Terminal API schema version. [[adyen]] [[adyen-terminal-api]]

## Key takeaways

- The captured server forms are cloud test `/sync` and `/async` routes at `device-api-test.adyen.com/v1/merchants/{merchantAccount}/devices/{deviceId}`, plus a local terminal IP. This operation page does not identify the caller, session, authentication method, or a message header. The `SaleData` and `OriginalPOITransaction` field descriptions mention Sale System and NEXO Sale-to-POI identities, but do not supply a complete header contract. See raw lines 10–19, 26–32, 54–62.
- Request `SaleData` and `StoredValueData` are required. `SaleData.SaleTransactionID` requires `TransactionID` and `TimeStamp`. Each `StoredValueData` item requires `StoredValueTransactionType`; `StoredValueAccountID` is optional, but when present it requires `StoredValueAccountType`, `EntryMode`, `IdentificationType`, and `StoredValueID`. Provider identity, original POI transaction reference, item amount, and currency are conditional/optional in this table. See raw lines 23–66 for all nested fields and enum values.
- The `200 Success` response body requires `Response`, `SaleData`, and `POIData`. `Response.Result` can be `Success`, `Failure`, or `Partial`; non-success requires `ErrorCondition`. `POIData.POITransactionID` requires its own transaction ID and timestamp. `StoredValueResult` is optional, and described for successful or partial loading/activation with one entry per requested stored-value item loaded or activated. Its account status and `CurrentBalance` are optional; balance is supplied only if relevant and known. Receipts are also optional. See raw lines 68–124. HTTP 200 alone does not prove a successful stored-value operation or a known balance.

## Detail locators

- Test cloud and local route forms: raw lines 10–19.
- Sale reference, required sale transaction identity, optional token/order/acquirer fields: raw lines 23–42.
- Stored-value transaction types, account ID conditions, optional original POI reference, amount and currency: raw lines 43–66.
- Message result/error, separate POI transaction identity, optional reconciliation ID, stored-value results/account status and receipt output: raw lines 68–124. The `POIReconciliationID` condition says only `If Result is Success`; this is not settlement or bank receipt evidence.

## Related

- [[adyen-terminal-api]] — provider concept and integration context.

## Raw Sources

- [[raw/adyen/api-explorer/terminal-api/latest/post/storedvalue/2026-09-15|POST /storedvalue captured API Explorer page]]
