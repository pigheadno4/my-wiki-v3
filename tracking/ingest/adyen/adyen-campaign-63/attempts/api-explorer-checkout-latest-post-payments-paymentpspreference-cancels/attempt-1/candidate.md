---
title: "Adyen Checkout API: Cancel an authorised payment by PSP reference"
type: source
date_ingested: 2026-11-02
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/post/payments/(paymentPspReference)/cancels"
raw_files:
  - "adyen/api-explorer/Checkout/latest/post/payments/(paymentPspReference)/cancels/2026-11-02.md"
tags: [adyen, checkout-api, online-payments, cancellation, webhooks]
---

## Overview

This [[adyen]] Checkout API v72 TEST reference, captured on 2026-11-02, describes `POST /payments/{paymentPspReference}/cancels` for cancelling an authorised [[adyen-online-payments|online payment]] that has not yet been captured. It returns a unique reference for the cancellation request; the outcome arrives asynchronously in a `CANCELLATION` webhook. The captured API reference is a contract snapshot, not proof of live availability or a completed cancellation.

## Key takeaways

- The required path parameter `paymentPspReference` is the original payment's `pspReference`. The required body property `merchantAccount` identifies the merchant account used to process that payment. The raw request body table does not separately state whether the body container is required. `reference` is an optional merchant reference for the cancellation request, limited to 80 characters.
- The optional `Idempotency-Key` header is a unique message identifier with a 64-character maximum; the page recommends a UUID. This reference does not describe replay behavior or an idempotency guarantee.
- A 201 response contains `merchantAccount`, the original `paymentPspReference`, a distinct 16-character cancellation-request `pspReference`, and `status: received`; `reference` is optional. `received` acknowledges the request, not the cancellation outcome.
- If the original payment's `pspReference` is unavailable, this page routes to `POST /cancels`. If capture status is uncertain, it routes to `POST /payments/{paymentPspReference}/reversals`. Those are separate operations, not alternate schemas for this request.
- The listed 400, 401, 403, 422 and 500 responses cover request, authentication, permission, validation and server errors. Their shared optional error fields include `additionalData`, `errorCode`, `errorType`, `message`, `pspReference` and integer HTTP `status`. The 422 generic example mentions a missing return URL; it does not establish a return-URL input for this cancellation schema.

> [!warning] Cancellation outcome
> Use the `CANCELLATION` webhook to learn whether the cancellation succeeded. A 201 response with `status: received` and a cancellation-request PSP reference does not establish that the original authorization was cancelled, that funds were released, or that any post-capture action succeeded.

## Detail locators

- **Servers; Parameters → Path parameters, Header parameters, Request body** — v72 TEST host, original-payment reference, optional idempotency header, required and optional body properties, and nested optional `applicationInfo` metadata.
- **Request examples → cancel-with-psp-reference** — illustrative merchant account and merchant cancellation reference.
- **Responses → 201 Success; Response examples → 201 Success** — cancellation-request response fields and `received` example.
- **Responses → 400/401/403/422/500; Response examples** — listed errors and generic examples; example values do not add request requirements.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-online-payments-cancel]] — online-payment cancellation guide; distinct guide snapshot.

## Related raw API references

- `POST /cancels` — merchant-payment-reference cancellation when the PSP reference is unavailable (linked from the raw introduction; not read for this entry).
- `POST /payments/{paymentPspReference}/reversals` — route when capture status is uncertain (linked from the raw introduction; not read for this entry).

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/post/payments/(paymentPspReference)/cancels/2026-11-02|Adyen Checkout API cancellation by PSP reference (2026-11-02)]]