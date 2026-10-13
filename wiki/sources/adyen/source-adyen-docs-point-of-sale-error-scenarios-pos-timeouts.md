---
title: "Adyen POS Transaction Time-outs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/error-scenarios/pos-timeouts"
raw_files:
  - "adyen/docs/point-of-sale/error-scenarios/pos-timeouts/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, timeouts, transaction-status, recovery]
---

## Overview

This Adyen POS guide distinguishes **processing**, **device-interaction**, and **request** time-outs. They do not have the same effect on the payment: issuer processing can be automatically canceled, many device waits end the transaction but some screens advance, and a timed-out request can leave the shopper able to complete payment on the terminal. The source is a 2026-09-15 webpage snapshot with `last_modified` 2025-12-15. Its local/cloud durations and terminal interaction table are guide-scoped; the page does not describe Mobile SDK behavior or an account-specific configurable value.

## Key takeaways

- **Processing time-out:** After terminal verification, if the issuer has not processed the payment within **120 seconds for local** or **150 seconds for cloud** Terminal API integration, Adyen says the platform cancels the transaction. The terminal shows Declined, and `PaymentResponse` reports `Result: Failure` and `ErrorCondition: Communication timeout`. After this confirmed result, the guide permits retry with another card/payment method. If no payment result or time-out is received by that interval, send `TransactionStatusRequest` to learn whether payment processed before taking another action.
- **Device time-out:** This is a wait for shopper interaction. The raw table gives different durations and configurability by screen (for example card presentation 120 seconds, PIN entry 60, signature check 900, authorization-in-progress 200, Giving 30, tipping 60, final-state display 4); configurable items are routed through Support. The guide says most such time-outs cancel with `Result: Failure`, `ErrorCondition: Cancel` and an `AdditionalResponse` indicating type. It also explicitly says some time-outs only change the screen and the transaction continues, such as tipping advancing to payment. Do not treat every screen timeout as final cancellation or apply the table's seconds to unrelated steps. Retry advice applies when a transaction **was canceled** by a device time-out.
- **Request time-out:** A request can time out at various tender steps after **120 seconds local** or **150 seconds cloud**, while the terminal may still await input and the shopper may still complete payment. The page shows an `EventNotification` with `EventToNotify: Reject` and `EventDetails: message=Timed+out+waiting+for+response+from+POI.`; this notification is not a final payment response. Send a transaction-status request to determine whether the payment remains in progress or has completed. The cloud tipping example (60 seconds on tipping, then 90 on payment screen) illustrates why the request and device timers are distinct; it is not a universal sequence.
- This page distinguishes local/cloud timing but does not specify mobile-app session limits, retry counts, or transport-specific delivery guarantees beyond its shown event. Do not infer approval, decline, reversal, or safe repeat from a missing response or timeout event alone.

## Detail locators

- `# Time-outs`, raw lines 19-25 — the three categories and why request timeout may still leave the transaction running.
- `## Processing time-out` — issuer processing trigger, local/cloud 120/150 seconds, failure result, conditional alternative-method retry and missing-result status check.
- `## Device time-out` — interaction-duration/configurability table, typical canceled response and tipping-screen continuation exception.
- `## Request time-out` — timed request versus active terminal payment, Reject notification example and transaction-status follow-up.

## Related

- Company: [[adyen]]
- Terminal API operation and status recovery: [[adyen-terminal-api]]
- Missing-result status procedure: [[source-adyen-docs-point-of-sale-basic-tapi-integration-verify-transaction-status]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/error-scenarios/pos-timeouts/2026-09-15|2026-09-15 Adyen POS time-outs snapshot]]
