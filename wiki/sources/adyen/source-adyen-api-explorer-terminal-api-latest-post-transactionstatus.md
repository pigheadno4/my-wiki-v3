---
title: "Adyen Terminal API POST /transactionstatus — TransactionStatus Request"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/terminal-api/latest/post/transactionstatus"
raw_files:
  - "adyen/api-explorer/terminal-api/latest/post/transactionstatus/2026-09-15.md"
tags: [adyen, terminal-api, pos, transaction-status]
---

## Overview

This captured **Terminal API latest** API Explorer page describes `POST /transactionstatus`, which requests information about the last or current Payment, Loyalty, or Reversal transaction. Its listed servers are cloud **test** device sync and async endpoints with `merchantAccount` and `deviceId`, and a local terminal IP address. The page does not state a numeric Terminal API version or authentication scheme. [[adyen]] [[adyen-terminal-api]]

## Key takeaways

- The request body's `MessageReference` is optional in this table; it identifies the prior request message header for an in-progress abort or a status check when no response was received. The shared field description also mentions abort, but this endpoint establishes status inquiry, not an abort action. Its `MessageCategory`, `ServiceID`, `DeviceID`, `SaleID`, and `POIID` are each marked optional. `SaleID` and `POIID` default to the corresponding `MessageHeader` values. Optional `ReceiptReprintFlag` requests receipt reprinting; `DocumentQualifier` selects document/recipient qualifications. See raw lines 23–33. The page gives no numeric field limits or retry deadline.
- A documented `200 Success` response carries required `Response.Result` with `Success`, `Failure`, or `Partial`. For results other than `Success`, `ErrorCondition` must be present; optional `AdditionalResponse` is logged by the POI. See raw lines 35–47.
- The response can include `MessageReference` and, if processing completed with `Result=Success`, optional `RepeatedMessageResponse` containing the requested message's header and body. Its header has required class, category, type, `SaleID`, and `POIID`; `ServiceID` and `DeviceID` have conditional descriptions, while `ProtocolVersion` is described for Login or Diagnosis. Body variants include Loyalty, Payment, Reversal, StoredValue, CardAcquisition, and CardReaderAPDU responses; this page does not expand their outcome schemas. See raw lines 48–70.
- A successful **status-request processing** result and presence of a repeated message are separate from the original transaction's financial outcome. Inspect the relevant repeated response and its own result before inferring authorization or reversal. This page does not establish capture, reconciliation, settlement, or bank receipt.

## Detail locators

- Purpose and transport URL forms: raw lines 5–19.
- Request reference/default and receipt-printing fields: raw lines 23–33.
- Status response result/error fields and repeated response structure: raw lines 35–70.

## Related

- [[adyen-terminal-api]] — Terminal API concept, including missing-result recovery.
- [[source-adyen-docs-point-of-sale-basic-tapi-integration-verify-transaction-status]] — separate website guide for POS status recovery; do not substitute its flow for this API Explorer schema.

## Raw Sources

- [[raw/adyen/api-explorer/terminal-api/latest/post/transactionstatus/2026-09-15|Captured TransactionStatus API Explorer page]]
