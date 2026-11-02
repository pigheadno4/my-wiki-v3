---
title: "Adyen Terminal API POST /payment (API Explorer snapshot)"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/terminal-api/latest/post/payment"
raw_files:
  - "adyen/api-explorer/terminal-api/latest/post/payment/2026-09-15.md"
tags: [adyen, terminal-api, api-explorer, point-of-sale, payments]
---

## Overview

Captured Adyen API Explorer reference for Terminal API `POST /payment`: a `PaymentRequest` sent to a terminal to initiate a payment, with a `PaymentResponse` describing processing by the POI system. The listed cloud **test** servers use Device API v1 sync and async paths with `{merchantAccount}` and `{deviceId}`; local hosting is shown only as a terminal IP placeholder. `latest` is a documentation URL segment, not a specified Nexo protocol version or proof of live availability. The page does not show the current request's outer MessageHeader or its SaleID, ServiceID, or POIID; optional `OriginalPOITransaction.SaleID` and `.POIID` identify a previous transaction (raw lines 54–56). It also does not specify a caller credential or session identifier. See [[adyen]] and [[adyen-terminal-api]] for separately sourced integration context.

## Key takeaways

- **Required request core and transaction identity.** `SaleData` and `PaymentTransaction` are marked required. Within `SaleData`, `SaleTransactionID` and its `TransactionID` and `TimeStamp` are required; this identifies the sale-system transaction. Within `PaymentTransaction`, `AmountsReq` and its `Currency` and `RequestedAmount` are required. The response separately requires `POIData.POITransactionID.TransactionID` and `.TimeStamp`, identifying the POI transaction. `OriginalPOITransaction` is an optional reference to a previous transaction, including card reuse; it is not the current sale or POI ID. The timestamp descriptions establish transaction/event time and uniqueness, not a retry deadline or idempotency rule. See raw lines 27–47, 54–62 and 121–141.
- **Conditional request detail.** Optional `PaymentData` can state a `PaymentType` such as Normal, Refund, reservations, Completion, Recurring, or Instalment; the enum does not itself define those operation lifecycles. An included `CardAcquisitionReference` requires its nested `TransactionID` and `TimeStamp`; an included `PaymentInstrumentData` requires `PaymentInstrumentType`. Optional `LoyaltyData` items likewise have conditionally required reference fields and, within an included `LoyaltyAccountID`, `EntryMode`, `IdentificationType` and `LoyaltyID`. Optional amounts include cashback, tip, paid split amount and minimum/maximum controls; `TransactionConditions` can restrict brand, acquirer or entry mode. These nested requirements do not make their optional parents required. See raw lines 45–106.
- **Processing result is separate from transport and authorization.** The `200 Success` section requires `Response.Result`, `SaleData`, and `POIData`; `Result` can be `Success`, `Failure`, or `Partial`. Its description says `ErrorCondition` is absent or unused on Success and must be present otherwise; `AdditionalResponse` is optional logging detail. `PaymentResult` is optional. If `PaymentResult.AmountsResp` is present, `AuthorizedAmount` is marked required within it, while response `Currency` is optional. Inspect the actual result and amount rather than treating HTTP 200, request submission, or the async URL as an approved payment. See raw lines 108–158.
- **Authorization and later-state boundaries.** `PaymentResult.OnlineFlag` indicates whether processing required host approval; `AuthenticationMethod` reports customer-authentication method. Neither field alone proves issuer approval. `MerchantOverrideFlag` explicitly marks that the merchant forced a successful result, so even a success label needs that qualification when present. Optional acquirer approval/reconciliation identifiers and `POIData.POIReconciliationID` identify approval or periods when supplied; they do not establish capture, completed reconciliation, settlement, or bank receipt. Optional `PaymentReceipt` contains customer/merchant display or print material. The page gives no reversal, status-recovery, retry, timeout, capture or settlement procedure. See raw lines 142–143, 152–158 and 177–212.
- **Scope of credentials and versions.** The page describes optional CMS-protected card data and output signatures, but no request authentication setup, card-data handling procedure or complete security design. It states neither a live server nor a deprecation policy. Its captured `/v1` paths are cloud transport addresses, not a Nexo protocol version or a guarantee that every listed `PaymentType` is enabled for a merchant. See raw lines 11–20, 73–97 and 177–185.

## Detail locators

- Raw `## Servers` (lines 11–20): cloud test Device API v1 sync/async paths and local placeholder.
- Raw `## Parameters` (lines 22–106): required sale and amount core; optional conditions, references, payment/loyalty data and their nested requirements.
- Raw `## Responses` (lines 108–158): result/error rules, separate sale and POI IDs, optional payment result and authorized amount.
- Raw response continuation (lines 159–212): conversion, merchant override, online/authentication flags, acquirer/loyalty identifiers and print/display receipt schema.

## Related

- [[adyen-terminal-api]] — Terminal API message architecture and other operation routes.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/api-explorer/terminal-api/latest/post/payment/2026-09-15|Terminal API POST /payment, fetched 2026-09-15]]
