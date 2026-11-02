---
title: "Adyen Checkout API POST /payments/{paymentPspReference}/reversals"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference)/reversals"
raw_files:
  - "adyen/api-explorer/Checkout/latest/post/payments/(paymentPspReference)/reversals/2026-11-02.md"
tags: [adyen, checkout, online-payments, reversal, refund, cancel]
---

## Overview

This [[adyen]] Checkout API v72 endpoint reference, captured 2026-11-02, describes a test-server reversal request for an existing payment. It refunds a captured payment or cancels an uncaptured one, for the full payment amount. The outcome arrives later through a `CANCEL_OR_REFUND` webhook. The page says not to use this request for payments with multiple partial captures. This is an endpoint contract, not proof of an account's live availability or a completed reversal. See [[adyen-online-payments]] for the integration route.

## Key takeaways

- Call `POST /payments/{paymentPspReference}/reversals` with the **original payment's** `pspReference` in the required path parameter and `merchantAccount` in the request body. The body table marks `merchantAccount` required; `reference` (maximum 80 characters) and `applicationInfo` are optional. The optional `Idempotency-Key` header has a maximum of 64 characters; the reference recommends a UUID. The reference does not specify a default or an amount field for a partial reversal.
- A 201 response has required `merchantAccount`, original `paymentPspReference`, distinct 16-character reversal-request `pspReference`, and `status: received`; the merchant `reference` is optional. `received` identifies request receipt, not confirmed cancellation, completed refund, settlement, or final financial outcome. Use the asynchronous `CANCEL_OR_REFUND` outcome route rather than treating the response as finality.
- The captured server is `https://checkout-test.adyen.com/v72`. The listed error responses are 400 (request parsing/understanding), 401 (authentication required), 403 (insufficient permissions), 422 (validation), and 500 (server unable to process). Their response fields are optional in the table; example error codes and messages do not define universal conditions.

## Detail locators

- `# POST /payments/{paymentPspReference}/reversals - Refund or cancel a payment`, raw lines 5–13 — operation, full amount, multiple-partial-capture exclusion, asynchronous outcome.
- `## Servers` and `## Parameters`, raw lines 15–58 — v72 test server, required original-payment path reference and merchant account, optional header/body fields and length limits; `applicationInfo` nested fields.
- `## Request examples`, raw lines 60–68 — illustrative request.
- `### 201 Success`, raw lines 69–81; `## Response examples`, raw lines 153–166 — response contract, distinct references, `received` example.
- `### 400 Client Error` through `### 500 Server Error`, raw lines 84–151; `## Response examples`, raw lines 168–228 — error descriptions, optional error fields and illustrative payloads.

## Related

- [[adyen]] — provider page.
- [[adyen-online-payments]] — online-payments integration and source routes.
- [[source-adyen-docs-online-payments-reversal]] — companion reversal guide with lifecycle and webhook context.

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/post/payments/(paymentPspReference)/reversals/2026-11-02|Checkout reversal endpoint (2026-11-02 snapshot)]]