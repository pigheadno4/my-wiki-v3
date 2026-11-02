---
title: "Terminal API CardAcquisition request and response | Adyen API Explorer"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/terminal-api/latest/post/cardacquisition"
raw_files:
  - "adyen/api-explorer/terminal-api/latest/post/cardacquisition/2026-09-15.md"
tags: [adyen, terminal-api, card-acquisition, api-explorer, point-of-sale]
---

## Overview

This 2026-09-15 API Explorer snapshot describes a POST `/cardacquisition` CardAcquisition message pair: the Sale System asks the POI to read and analyse payment or loyalty card information, usually before a separate payment or loyalty message pair refers to it. It lists test cloud Device API `/v1/merchants/{merchantAccount}/devices/{deviceId}/sync` and `/async` server addresses and a local terminal-IP placeholder. The `latest` URL is a moving documentation label; this captured page does not identify a Terminal API protocol version, message-header fields, production endpoint, authentication method, or a complete HTTP envelope.

## Key takeaways

- The request-body table marks `SaleData` and `CardAcquisitionTransaction` required. Within `SaleData`, `SaleTransactionID.TransactionID` and `TimeStamp` are required; `TransactionID` identifies the Sale or POI transaction, and the timestamp supports uniqueness. The optional `CardAcquisitionTransaction.TotalAmount` allows contactless-card processing. Optional selectors include allowed payment/loyalty brands, loyalty handling, entry modes, customer selection, payment type, and a token request type. These are body-table requirements, not a complete top-level message schema.
- The 200 response table marks `Response`, `SaleData`, and `POIData` required, including `Response.Result`, `SaleData.SaleTransactionID`, and `POIData.POITransactionID` with their nested transaction IDs and timestamps. `Result` may be `Success`, `Failure`, or `Partial`. On non-success, the `Response` description says `ErrorCondition` must be present; on success it is absent or unused. `AdditionalResponse` is optional processing/logging detail. An HTTP 200 section and a successful acquisition result do not establish a subsequent payment authorization, capture, reconciliation, settlement, or bank receipt.
- Optional `PaymentBrand`, `PaymentInstrumentData`, and `LoyaltyAccount` data may appear. `PaymentInstrumentData.CardData.PaymentBrand` can support cashier selection among applications or co-brands; for that case the description says `CardAcquisitionRequest.ForceCustomerSelectionFlag` must be `False`. The page also describes masked PAN, PAR, tokens, and CMS-protected card data, but does not supply a blanket promise that any particular identifier is returned or usable for payment.
- The page gives no service-ID or request-header correlation rule, async delivery/result workflow, timeout, retry/reversal, cancellation, expiry, or deprecation rule. Consult separate Terminal API flow guidance for those behaviors; do not infer them from the two listed cloud transport paths or this body schema.

## Detail locators

- Operation purpose and captured server addresses: raw lines 5–19.
- Request body, parent and nested required fields, optional selectors, and contactless amount: raw lines 21–52.
- Response result, error and Sale/POI transaction identities: raw lines 54–88.
- Optional brand and payment-instrument data, sensitive-data protection, and loyalty-account fields: raw lines 89–131.

## Related

- [[adyen]] — provider context.
- [[adyen-terminal-api]] — Terminal API concept and integration boundaries.
- [[source-adyen-docs-point-of-sale-card-acquisition]] — separate Adyen POS flow guide for later payment referencing and abort/cancellation; its behavior is not supplied by this API Explorer page.

## Raw Sources

- [[raw/adyen/api-explorer/terminal-api/latest/post/cardacquisition/2026-09-15|Adyen API Explorer CardAcquisition request/response (2026-09-15 snapshot)]]
