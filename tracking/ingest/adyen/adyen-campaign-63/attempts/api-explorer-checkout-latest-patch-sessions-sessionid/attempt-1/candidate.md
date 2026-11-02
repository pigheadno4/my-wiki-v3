---
title: "Adyen Checkout API PATCH /sessions/{sessionId} — Update a payment session"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/patch/sessions/(sessionId)"
raw_files:
  - "adyen/api-explorer/Checkout/latest/patch/sessions/(sessionId)/2026-11-02.md"
tags: [adyen, checkout, sessions, api-explorer]
---

## Overview

This 2026-11-02 API Explorer snapshot documents Checkout API `PATCH /sessions/{sessionId}` on the displayed test server `https://checkout-test.adyen.com/v72`. It updates an existing payment session's amount and payable state before the session is payable. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The path requires the existing `sessionId`. The request table marks `amount` and its `currency` (three-character ISO code) and `value` (integer in minor units) required; it also marks `sessionData` required, sourced from the Web Drop-in or Component `beforeSubmit` callback. These are table-level property marks; this snapshot does not separately declare request-body requiredness.
- Optional `payable` indicates whether the shopper can submit the payment. Set it to `true` once the amount is final; the session can then no longer be updated. If set to `false`, another update setting it to `true` is needed before the shopper can submit. The page does not state a default when the field is omitted.
- HTTP `200 Success` says the request succeeded, with an optional `sessionData` response field. This update response does not document a payment result or financial finality. The captured page does not specify authentication, idempotency, error responses, or an asynchronous outcome; use the corresponding integration and payment-result references for those separate questions. Its `latest` URL is a captured label, not proof of a current version or live availability.

## Detail locators

- Operation, update gate and displayed test server: raw lines 5–12.
- Path parameter and complete request table: raw lines 14–29.
- HTTP success and complete response table: raw lines 31–39.

## Related

- [[source-adyen-api-explorer-checkout-latest-post-sessions]] — separate session creation contract.
- [[source-adyen-docs-online-payments-build-your-integration-sessions-flow]] — separate integration flow and amount-update procedure.

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/patch/sessions/(sessionId)/2026-11-02|Checkout API PATCH /sessions/{sessionId} snapshot (2026-11-02)]]