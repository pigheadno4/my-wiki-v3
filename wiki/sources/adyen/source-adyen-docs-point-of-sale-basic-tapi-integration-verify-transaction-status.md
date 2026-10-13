---
title: "Adyen Docs: Verify a missing Terminal API transaction response"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/basic-tapi-integration/verify-transaction-status"
raw_files:
  - "adyen/docs/point-of-sale/basic-tapi-integration/verify-transaction-status/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, transaction-status, timeout-recovery]
---

## Overview

This Adyen Docs guide explains how a POS integration checks an **original transaction's status** when a communication or technical issue leaves its response missing. Staff should not infer a failed or successful payment and immediately repeat, cancel, or refund it: a Terminal API `TransactionStatusRequest` can distinguish **processed**, **in progress**, and **not found**. When processed, the original transaction response is returned and must be read for the original result. See [[adyen-terminal-api]] and [[adyen]].

## Key takeaways

- **Applicable solutions and timing:** the guide covers Terminal API with payment terminals, Android/iOS Mobile SDK Tap to Pay or card-reader solutions, and Android Payments app. For a missing payment response or timeout, with internet connectivity intact, it recommends an automatic status check after **120 seconds local** or **150 seconds cloud**. Mobile SDK has no fixed wait and can check as soon as the response is noticed missing; its request must come from the POS app **on the mobile device**, not the backend. The mobile SDK and Android Payments app paths are marked beta in this snapshot. If normally using asynchronous cloud communication, use a `/sync` endpoint for this check; otherwise await the event notification with the response. [Raw: Requirements; Check the transaction status]
- **Request identity:** send a new `TransactionStatus` Service request with its **own** unique `ServiceID` and terminal `POIID`. `TransactionStatusRequest.MessageReference` names the **original** `SaleID`, `ServiceID`, and category (`Payment`, `Reversal`, or `StoredValue`). A status request without `MessageReference` returns `Failure/NotFound` with the most recent terminal transaction's `SaleID` and `ServiceID` in `AdditionalResponse`; that is a lookup aid, not proof the intended original transaction was absent. [Raw: Check the transaction status, request parameters]
- **Processed is not payment approval:** `TransactionStatusResponse.Response.Result=Success` means the original reached an end state such as approved, cancelled, or declined. Inspect `RepeatedMessageResponse.RepeatedResponseMessageBody` for the original `PaymentResponse.Response` or other original message and its result; the status-response `Success` alone does not mean a payment succeeded. [Raw: Check the transaction status; Transaction processed]
- **In progress:** `Failure` with `ErrorCondition=InProgress` means processing continues, often while shopper input is pending. The guide permits repeated status requests without an added polling delay because the terminal handles it. For terminal integrations, `AdditionalResponse` can include `tenderReference` and `detailedStatus`; those two fields are absent for Android/iOS Mobile SDK or Android Payments app in-progress responses. [Raw: Transaction in progress; Requirements]
- **Not found and retry boundary:** `Failure/NotFound` may mean the original `POIID`, `SaleID`, or `ServiceID` was wrong **or** Adyen did not receive the original request due to connectivity or power loss. Check the original identifiers before considering a retry of the original transaction; a `NotFound` result by itself does not disambiguate those causes. Frequent status checks may signal a network problem. [Raw: Transaction not found; introduction]

## Detail locators

- Raw `Check the transaction status` specifies the MessageHeader, `MessageReference`, optional receipts and reprint, timeout timing, and solution-specific endpoint/device requirements. `ReceiptReprintFlag` is unsupported for Android Mobile SDK or Payments app.
- Raw `Transaction processed` has examples where the **status** response is Success but the embedded original payment response is either Success or Failure after cancellation.
- Raw `Transaction in progress` and `Transaction not found` give the two Failure/ErrorCondition branches, qualifiers, and examples.
- Linked donation, response-handling, and timeout guides under `See also` are navigation only.

## Related

- [[adyen-terminal-api]] — existing Terminal API hub and response-recovery context
- [[adyen]] — company and knowledge-status page

## Raw Sources

- [[raw/adyen/docs/point-of-sale/basic-tapi-integration/verify-transaction-status/2026-09-15|Verify transaction status — Adyen Docs snapshot, 2026-09-15]]
