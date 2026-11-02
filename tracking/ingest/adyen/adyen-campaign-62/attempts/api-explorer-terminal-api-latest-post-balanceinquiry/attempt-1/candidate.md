---
title: "Adyen Terminal API POST /balanceinquiry (API Explorer snapshot)"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/terminal-api/latest/post/balanceinquiry"
raw_files:
  - "adyen/api-explorer/terminal-api/latest/post/balanceinquiry/2026-09-15.md"
tags: [adyen, terminal-api, api-explorer, point-of-sale, balance-inquiry]
---

## Overview

Captured Adyen API Explorer reference for Terminal API `POST /balanceinquiry`, describing a BalanceInquiry request for account information and a response carrying the balance and identity of an associated payment, loyalty, or stored-value account. The captured server list has cloud **test** sync and async Device API v1 paths scoped by `{merchantAccount}` and `{deviceId}`, plus a local terminal IP placeholder. `latest` is the documentation URL segment; this page does not give a Nexo protocol version, live endpoint, or merchant-specific enablement. See [[adyen]], [[adyen-terminal-api]], and the separate [[source-adyen-docs-point-of-sale-alternative-payment-methods-gift-cards-terminal-api-query-the-balance|gift-card implementation guide]] for message-header details absent here.

## Key takeaways

- **Request identity and optional parents.** The request-body table lists optional `PaymentAccountReq` and `LoyaltyAccountReq`. Within an included `CardAcquisitionReference`, both `TransactionID` and `TimeStamp` are marked required; the timestamp describes transaction/event time and uniqueness, not an expiry or retry window. Within included payment-instrument data, `PaymentInstrumentType` is required. Within an included `LoyaltyAccountID`, `EntryMode`, `IdentificationType`, and `LoyaltyID` are required. These child requirements do not make either top-level account object mandatory. The page does not expose a request MessageHeader, `SaleID`, `ServiceID`, `POIID`, or full envelope. See raw lines 21–46.
- **Response result and conditional balance.** Under `200 Success`, `Response` and its `Result` are marked required, yet `Result` can be `Success`, `Failure`, or `Partial`; `ErrorCondition` is absent or unused for success and must be present in other cases. `PaymentAccountStatus` is optional and its description says it applies when `BalanceInquiryRequest. PaymentAccount` is present, while the request table names `PaymentAccountReq`. Do not silently equate those names. `CurrentBalance` and `Currency` are optional fields within `PaymentAccountStatus`; HTTP 200 or a success result alone is not a promise that both appear. See raw lines 48–70.
- **Other optional response detail.** `PaymentAcquirerData` and `PaymentReceipt` are optional. The former has required `MerchantID` and `AcquirerPOIID` only when that object appears; the latter has required `DocumentQualifier` and `OutputContent` per included receipt, with `OutputFormat` required inside the content. `OutputText` and `OutputXHTML` have format-specific mandatory/forbidden conditions. These receipt entries are display/print content, not evidence of bank receipt or settlement. See raw lines 71–87.
- **Outcome boundary.** This operation reports account balance information and request-processing status. Its `Failure`/`Partial` results and listed error conditions include `InProgress`, but this page gives no recovery, reversal, retry, expiry, or asynchronous callback procedure. The async cloud URL is a transport option, not proof of a final outcome at request acceptance. Optional CMS-protected card data is a field description, not a complete authentication or credential contract. The page does not establish payment authorization, capture, reconciliation, settlement, or a later usable balance. See raw lines 12–19, 31–34, 48–64 and 69–87.

## Detail locators

- Raw `## Servers` (lines 10–19): captured cloud test sync/async Device API v1 URLs and local IP placeholder.
- Raw `## Parameters` (lines 21–46): optional request parents and conditionally required transaction, payment-instrument, and loyalty-ID children.
- Raw `## Responses` (lines 48–87): HTTP 200 section, result/error semantics, optional account status/balance/acquirer data and receipt output conditions.

## Related

- [[adyen-terminal-api]] — Terminal API concept and transport context.
- [[adyen]] — provider context.
- [[source-adyen-docs-point-of-sale-alternative-payment-methods-gift-cards-terminal-api-query-the-balance]] — separate gift-card guide with a full request/response example.

## Raw Sources

- [[raw/adyen/api-explorer/terminal-api/latest/post/balanceinquiry/2026-09-15|Terminal API POST /balanceinquiry, fetched 2026-09-15]]
