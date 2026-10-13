---
title: "Handle responses | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/error-scenarios"
raw_files:
  - "adyen/docs/point-of-sale/error-scenarios/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, error-handling, transaction-status]
---

## Overview

Adyen's "Handle responses" guide describes Terminal API response fields and how a POS integration can investigate malformed requests, missing transaction results, unavailable terminals, declined payments, and time-outs. It is a 2026-09-15 snapshot whose metadata reports `last_modified` 2019-08-20; it does not prove current terminal behavior or the outcome of any particular payment. [[adyen]] [[adyen-terminal-api]]

## Key takeaways

- A Terminal API `Response` uses `Result` (`Success`, `Partial`, or `Failure`), `ErrorCondition` on failure, and `AdditionalResponse` for further detail. `AdditionalResponse` may be form-encoded key/value text or a Base64-encoded JSON object. `MessageFormat` and `UnavailableService` failures call for diagnosing the cause and manually correcting the request; invalid JSON instead yields a `Bad JSON` HTTP reply with a line number.
- If a payment result is missing, the guide recommends checking transaction status. For local or cloud integrations with an intact internet connection, it specifies checking after a missing or timed-out response at 120 or 150 seconds respectively; mobile SDK solutions have no fixed wait. When neither synchronous nor asynchronous transaction result arrives, make a `TransactionStatusRequest`: `Success` means use `RepeatedResponseMessageBody` to process the transaction; `InProgress` calls for status checks every five seconds until processed; `NotFound` can reflect wrong original-transaction details or a request Adyen did not receive. For `NotFound`, the page lists verifying the **original** transaction in `MessageReference` and potentially retrying the original transaction. `NotFound` alone is not proof of its cause or permission for a blind duplicate payment.
- For a cloud payment request to an unavailable terminal, a Terminal API `Reject` event notification includes a Base64 `RejectedMessage` and `EventDetails`. The guide distinguishes a request sent without terminal response (check transaction status), failure to send to the POI (check cloud/WebSocket connection), and unknown `POIID` (check terminal ID and merchant/store assignment). A reject or missing response should be followed through the documented status/recovery path, not treated as an automatically final payment outcome.
- For declined `PaymentResponse` results, retry guidance depends on the **payment** `ErrorCondition` and, for `Cancel`, `InvalidCard`, and `Refusal`, the listed response details. `Busy` is not retryable in the table; a returned `serviceId` can be used in an `AbortRequest` to cancel the in-progress transaction. `Cancel` with `Approved` is marked do not retry. `NotAllowed` is also marked do not retry for `PaymentRequest`, while the comparison table gives different actions for `TransactionStatusRequest` and `ReversalRequest`. The guide says to code against `ErrorCondition`, not the `refusalReason` or `message` insight fields; raw acquirer responses can change without notice.
- A processing or device time-out returns `Failure` and cancels the transaction; a **request** time-out produces a `Reject` event while the terminal may still complete the payment, so check transaction status. Retry recommendations differ by time-out type. The comparison table is operation-specific, and an unresolved payment must not be collapsed into the same state as a documented failure response.

## Detail locators

- `Response` fields and invalid-message, Bad JSON, and unavailable-service handling: pinned raw, `## Response object format` through `## Unavailable service` (lines 25–103).
- Missing result timing and `TransactionStatusResponse` actions, including `RepeatedResponseMessageBody`, `InProgress`, and `NotFound`: pinned raw, `## No result received` (lines 105–123).
- Cloud `Reject` event shape and three `EventDetails` cases: pinned raw, `## Terminal unavailable (cloud integration)` (lines 125–200).
- Decline retry matrix, `serviceId`/abort route, and coding warning: pinned raw, `## Declined payment` (lines 202–306).
- Three time-out categories and operation-specific `ErrorCondition` comparison: pinned raw, `## Time-out` and `## Error condition comparison` (lines 308–339).
- `posEntryMode` and `ForceEntryMode` example: pinned raw, `## Unexpected card entry modes` (lines 341–445).

## Related

- [[adyen-terminal-api]] — Terminal API message architecture and in-person operation boundaries.
- [[adyen]] — provider hub.

## Related raw API references

- [[raw/adyen/docs/point-of-sale/error-scenarios/refusal-reasons-pos/2026-09-15|POS refusal reasons]] — linked reference navigation only; not read for this entry.
- [[raw/adyen/docs/point-of-sale/error-scenarios/pos-timeouts/2026-09-15|POS time-outs]] — linked reference navigation only; not read for this entry.
- [[raw/adyen/docs/point-of-sale/error-scenarios/raw-acquirer-responses/2026-09-15|Raw acquirer responses]] — linked reference navigation only; not read for this entry.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/error-scenarios/2026-09-15|Handle responses — 2026-09-15 snapshot]]
