---
title: "Adyen Cancel an In-Progress POS Transaction"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/basic-tapi-integration/cancel-a-transaction"
raw_files:
  - "adyen/docs/point-of-sale/basic-tapi-integration/cancel-a-transaction/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, abort, transaction-status, cancellation, refund]
---

## Overview

This Adyen guide covers stopping an **in-progress** terminal payment from a merchant POS app with Terminal API `AbortRequest`, or from the terminal's Cancel control. An abort received before terminal approval can cancel that attempt; a completed payment cannot be aborted. The guide distinguishes a later authorized-payment cancellation under delayed/manual capture from this in-progress action, and sends an approved payment after failed cancellation to the refund path. It applies to Terminal API or standalone terminal solutions, though the POS-app AbortRequest procedure specifically requires Terminal API. The 2026-09-15 webpage snapshot lists `last_modified` 2023-09-13.

## Key takeaways

- The POS sends a **new** Service-class `Abort` request with its own unique header `ServiceID` (1–10 alphanumeric characters, unique for that terminal over the preceding 48 hours), `SaleID`, and terminal `POIID`. `AbortRequest.MessageReference` points to the **original Payment** request's `SaleID` and `ServiceID`, with `AbortReason: MerchantAbort`; the example's current abort `ServiceID` differs from its referenced payment `ServiceID`. An HTTP `200 OK` with no body is the abort-request response, while the original payment should report `Result: Failure` and `ErrorCondition: Aborted`; use `TransactionStatusRequest` referencing the original payment to double-check the actual state. Do not treat the HTTP acknowledgement alone as payment finality.
- The POS may abort before card presentation or after presentation while payment is unfinished (for example before PIN). After payment completion, the abort operation is unavailable. If an authorized payment was on delayed/manual capture, the source points to cancellation of that authorization; if cancellation fails and the payment was approved, it points to refund. It does not describe a ReversalRequest contract or prove that a refund has completed.
- If a communication/technical issue leaves a payment or card acquisition in progress and the original `ServiceID` is unavailable to the POS, the guide uses a new `TransactionStatusRequest` with an **empty** request object to recover the original `MessageReference`. This empty-object form is limited to still-in-progress payment/card-acquisition requests. The source says a stuck terminal normally times out after about 150 seconds; this is an approximate observation, not a safe retry schedule or a guarantee that a payment failed. Use the recovered original IDs and category for the relevant cancellation route.
- Cancel on the terminal yields `ErrorCondition: Cancel` in the original payment response if successful, distinct from POS Abort's `Aborted`. A signature-screen Cancel is exceptional: where shoppers sign on screen, authorization already occurred, and the terminal approves the signature even if Cancel is selected. The merchant must use the linked signature-check guidance rather than treating that button as payment cancellation.
- This guide does not distinguish local versus cloud delivery, mobile SDK behavior or account-specific support for the linked authorized-cancel/refund routes. Follow the architecture and operation-specific sources for those details.

## Detail locators

- `# Cancel an in-progress transaction` and `##### Want to cancel an authorized payment?` — action boundary before terminal approval and separate delayed/manual-capture authorization cancellation.
- `## Cancel from your POS app`, steps 1–3 — Abort header/current IDs, original Payment `MessageReference`, HTTP acknowledgement, original payment result and status verification. JSON request/status examples are illustrative.
- `### Cancel when you do not know the ServiceID` — empty-object status lookup only while Payment/CardAcquisition remains in progress and follow-up with recovered original reference.
- `## Cancel from the terminal`, `### Canceling a signature on the display`, `## Handling failed cancel requests` — terminal Cancel result, already-authorized signature exception and refund route after failed cancel of an approved payment.

## Related

- Company: [[adyen]]
- Terminal API operation and recovery context: [[adyen-terminal-api]]
- Separate card acquisition cancellation: [[source-adyen-docs-point-of-sale-card-acquisition]]
- Separate signature behavior: [[source-adyen-docs-point-of-sale-cardholder-verification-methods]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/basic-tapi-integration/cancel-a-transaction/2026-09-15|2026-09-15 Adyen in-progress cancellation guide snapshot]]
