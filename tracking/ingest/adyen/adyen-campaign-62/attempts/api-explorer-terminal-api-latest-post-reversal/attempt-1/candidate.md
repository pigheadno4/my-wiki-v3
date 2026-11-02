---
title: "Adyen Terminal API: POST /reversal reversal request"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/terminal-api/latest/post/reversal"
raw_files:
  - "adyen/api-explorer/terminal-api/latest/post/reversal/2026-09-15.md"
tags: [adyen, terminal-api, reversal, point-of-sale, api]
---

## Overview

This 2026-09-15 API Explorer capture describes Terminal API `POST /reversal` for reversing a previous payment or loyalty transaction. It lists cloud device **test** sync and async servers under `/v1/merchants/{merchantAccount}/devices/{deviceId}/` and a local terminal IP server. The `latest` Explorer path and cloud `v1` transport path do not specify a numbered Terminal API protocol version. See [[adyen]] and [[adyen-terminal-api]].

## Key takeaways

- The request table requires `OriginalPOITransaction` and `ReversalReason`; valid reason values are `CustCancel`, `MerchantCancel`, `Malfunction`, and `Unable2Compl`. Within the required original-transaction object, `SaleID`, terminal `POIID` (when the original transaction is from another POI), `POITransactionID`, `AcquirerID`, `HostTransactionID`, and other listed fields are marked optional. `TransactionID` and `TimeStamp` are required **within** either supplied nested transaction-ID object. The schema does not itself make `OriginalPOITransaction.POITransactionID` mandatory.
- `ReversedAmount` is optional and, when omitted, is implicitly the `AuthorizedAmount`. This is the reversal amount rule in the reference; the page gives no currency field or amount cap. Optional `SaleData` holds sale-side data; its `SaleTransactionID` is required only within a supplied `SaleData` object, with required nested `TransactionID` and `TimeStamp`. Other sale/operator, token, order, terminal, and acquirer fields remain in the raw table.
- The `200 Success` response table requires a `Response` object and its `Result` (`Success`, `Failure`, or `Partial`). `ErrorCondition` is absent or unused for Success and must be present otherwise. Optional `POIData` contains a required `POITransactionID` if that object appears; `POIReconciliationID` is optional and described for Success. `OriginalPOITransaction`, copied `ReversedAmount`, and `PaymentReceipt` are optional response fields. Receipt content/format conditions are detailed in raw lines 91–100.
- The reference calls this information about a reversal processed by the POI system. HTTP 200, a `Response.Result`, a reconciliation-period identifier, or a receipt should not be expanded into proof of completed refund, settlement, or bank receipt. The separately captured [[source-adyen-docs-point-of-sale-basic-tapi-integration-refund-payment-referenced|referenced POS refund guide]] says a successful ReversalResponse acknowledges **receipt of a refund request**, with asynchronous outcome reported later by `CANCEL_OR_REFUND`; that operational rule belongs to the guide, not this schema table.
- This page does not state authentication/security steps, a request-correlation or callback contract for the listed async transport, deprecation, retry timing, reversal completion timing, or account-specific eligibility. A payment reversal and a loyalty reversal share this operation's stated scope; the table alone does not select a particular merchant refund route.

## Detail locators

- Purpose and cloud test sync/async plus local server list: raw lines 5–19.
- `SaleData` parent and nested requiredness; sale/operator/acquirer fields: lines 21–42.
- Original-transaction identifiers, conditional other-POI field, amount default and reason enum: lines 43–57.
- HTTP 200 response result/error semantics and conditional POI identifiers: lines 59–90.
- Optional receipt and conditional output content formats: lines 91–100.

## Related

- [[adyen]] — provider route.
- [[adyen-terminal-api]] — Terminal API concept.
- [[source-adyen-docs-point-of-sale-basic-tapi-integration-refund-payment-referenced]] — separate guide for a referenced POS refund's original reference, asynchronous outcome, and special offline/ecommerce forms.

## Raw Sources

- [[raw/adyen/api-explorer/terminal-api/latest/post/reversal/2026-09-15|POST /reversal API Explorer capture]]
