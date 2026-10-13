---
title: "Adyen online payment reversal"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/reversal"
raw_files:
  - "adyen/docs/online-payments/reversal/2026-09-15.md"
tags: [adyen, online-payments, reversal, cancel, refund, webhooks]
---

## Overview

This [[adyen]] guide uses a reversal when the merchant is unsure whether an online payment has been captured. For an uncaptured payment, reversal cancels it; for a captured payment, reversal refunds it. This boundary connects the [[adyen-refunds]] and [[adyen-online-payments]] routes. The page documents request and webhook behavior in a 2026-09-15 snapshot, not an observed payment outcome.

## Key takeaways

- Reversal chooses between cancellation and refund based on capture state. It is unavailable after multiple partial captures or when the payment request or Adyen for Platforms capture request includes split data. In those cases, determine capture state and use the separate cancel or refund route.
- The documented Checkout API call is `POST /payments/{paymentPspReference}/reversals`, using the original payment PSP reference in the path and the processing `merchantAccount` in the body. A merchant `reference` is optional. The examples show a test endpoint and API version, so they do not establish a live endpoint for an account.
- The response contains a separate `pspReference` for the reversal request; its sample `status: received` records request receipt, not a confirmed cancellation or completed refund. Match the original payment through the webhook's `originalReference` and the reversal through its `pspReference`.
- The `CANCEL_OR_REFUND` webhook delivers the reversal-request outcome asynchronously. The page describes `success` specifically as the outcome of refund validations: `false` includes a reason to review; `true` means Adyen's validation succeeded and a refund request was sent to the card scheme. That usually succeeds, but a later scheme rejection or reversal remains possible and is documented through `REFUND_FAILED` or `REFUNDED_REVERSED`. Do not read `received` or `success: true` as final shopper fund receipt.
- The requirements table calls for listening to `CANCEL_OR_REFUND` events. Its Customer Area roles are described for editing capture settings; the page does not say those roles are all API reversal prerequisites.

## Detail locators

- `# Reversal`, raw lines 15–24 — uncertainty about capture and cancel-versus-refund choice.
- `## Requirements`, raw lines 26–36 — integration type, capture-setting roles, webhook, multiple-partial-capture and split-data exclusions.
- `## Reverse a payment`, raw lines 38–48 — endpoint, path and body fields, optional reference, and original PSP-reference routes.
- `## Reverse a payment`, raw lines 50–85 — test-environment examples and the response's reversal `pspReference` and sample `received` status.
- `## CANCEL_OR_REFUND webhook`, raw lines 88–129 — asynchronous outcome, reference correlation, refund-validation meanings and later exceptions; the JSON is an example with `modification.action: refund`.

## Related

- [[adyen]] — provider page.
- [[adyen-refunds]] — captured-payment refund behavior and later refund-failure routes.
- [[adyen-online-payments]] — online-payments integration and lifecycle routes.

## Raw Sources

- [[raw/adyen/docs/online-payments/reversal/2026-09-15|Adyen reversal (2026-09-15 snapshot)]]
