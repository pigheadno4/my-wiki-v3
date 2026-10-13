---
title: "Adyen Docs: Implement the Terminal API payment flow"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/basic-tapi-integration"
raw_files:
  - "adyen/docs/point-of-sale/basic-tapi-integration/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, payment-flow, refunds]
---

## Overview

This Adyen documentation hub outlines a basic payment flow for a merchant POS system integrated with Terminal API. It names three core actions—payment, refund, and cancellation in progress—and three additional features Adyen thinks belong in a basic integration: receipts, application details, and transaction-status recovery. It routes to detailed pages for each. This page addresses an integrated Terminal API POS flow; it does not define standalone-terminal or mobile-SDK setup, Management/Checkout API operations, merchant eligibility, exact API schema, or successful payment execution.

## Key takeaways

- The hub maps making a payment to `PaymentRequest`, issuing a refund to `ReversalRequest`, and canceling an in-progress payment to `AbortRequest`. These are links to operation references, not full request/response specifications; the broad refund mapping here does not establish how every referenced or unreferenced refund is represented. See **Implement the payment flow**, opening paragraphs.
- Adyen also recommends receipt generation from a dedicated `PaymentResponse` object, adding application details in `PaymentRequest`, and using `TransactionStatusRequest` when a payment response is missing. The page calls these six features a viable integration and marks their next-step links as required, while its prose frames the latter three as what Adyen thinks should be included. It does not establish a runtime enforcement rule. See **Implement the payment flow** and **Next steps**.
- Hospitality tipping, pay-at-table, pre-authorization/authorization adjustment, and retail cashback, currency conversion, and donations are examples of further business features. Their implementation details and API ownership are not established by this hub; follow the linked feature-specific evidence before making an API-family claim. See **Implement the payment flow**, optional-feature paragraph.

## Detail locators

- **Implement the payment flow** — three POS actions and their linked Terminal API request types; receipt, application-info, and status-recovery recommendations; six-feature viability statement.
- **Implement the payment flow → optional-feature paragraph** — hospitality and retail examples without implementation ownership.
- **Next steps** — links to make-payment, pass-application-info, generate-receipt, refund, cancel-in-progress, and verify-transaction-status pages. Linked pages are navigation until independently read.

## Related

- [[adyen]]
- [[adyen-terminal-api]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/basic-tapi-integration/2026-09-15|Adyen Docs — Implement the payment flow (2026-09-15)]]
