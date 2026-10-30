---
title: "Adyen Checkout API v72 POST /cancels"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Checkout/latest/post/cancels"
raw_files:
  - "adyen/api-explorer/Checkout/latest/post/cancels/2026-09-15.md"
tags: [adyen, checkout, api, cancellation]
---

## Overview

Captured Checkout API **v72** test-server reference for `POST /cancels`. It requests cancellation of an authorized payment that has **not yet been captured**, using the merchant's original payment `reference` as `paymentReference`. It returns a unique reference for the cancellation request; the outcome arrives asynchronously in a `TECHNICAL_CANCEL` webhook. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The request table marks `merchantAccount` and `paymentReference` required. `paymentReference` is the original payment's merchant `reference`, whereas optional `reference` is the merchant's reference for this cancel request (maximum 80 characters). The page does not separately label the request body as required. An optional `Idempotency-Key` header has a maximum of 64 characters.
- Use the separately linked `/payments/{paymentPspReference}/cancels` route to cancel by the original payment's PSP reference. The page directs an uncertain capture-state case to `/payments/{paymentPspReference}/reversals`; those linked endpoints' own contracts are outside this raw.
- A 201 response reports `status: received`, which the schema says is always that value, and gives the cancel request's `pspReference`. It acknowledges receipt, not successful cancellation or any capture, settlement or refund outcome. The `TECHNICAL_CANCEL` webhook supplies the later cancellation outcome.
- The documented server is `https://checkout-test.adyen.com/v72`. The canonical URL segment `latest` does not establish today's latest API version or a live endpoint. Error classes shown are 400, 401, 403, 422 and 500. The generic 422 example mentions a missing return URL although this endpoint's request table has no `returnUrl`; do not turn that example into a `/cancels` requirement.

## Detail locators

- Raw lines 5–16: purpose, uncaptured authorization boundary, asynchronous webhook, alternate PSP-reference and reversal routes, and captured server.
- Raw lines 20–53: optional idempotency header and full request body table.
- Raw lines 55–77 and 149–162: merchant-reference request example and 201 response schema/example.
- Raw lines 80–147 and 164–225: error classes, response schema and illustrative error examples.

## Related

- [[adyen-online-payments]] — provider online-payments concept.

## Raw Sources

- [[raw/adyen/api-explorer/Checkout/latest/post/cancels/2026-09-15|Captured Checkout API v72 POST /cancels reference]]