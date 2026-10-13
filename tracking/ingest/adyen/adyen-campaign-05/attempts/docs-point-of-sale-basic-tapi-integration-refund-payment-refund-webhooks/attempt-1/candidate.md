---
title: "Adyen POS refund webhook outcomes"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/basic-tapi-integration/refund-payment/refund-webhooks"
raw_files:
  - "adyen/docs/point-of-sale/basic-tapi-integration/refund-payment/refund-webhooks/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, refunds, standard-webhooks, refund-outcomes]
---

## Overview

This Adyen website guide, captured on 2026-09-15, explains **platform Standard webhook validation outcomes** for POS Terminal API referenced and unreferenced refunds. A Terminal API response usually confirms only request receipt; the relevant Standard webhook reports Adyen's validation result. It applies to Terminal API with payment terminals or a Mobile solution and requires Standard webhooks to be configured. This source routes through [[adyen-terminal-api]] and [[adyen-webhooks]]; it is distinct from a terminal-generated event notification and from the separate online Checkout API refund flow.

## Key takeaways

- Referenced POS refund requests produce **`CANCEL_OR_REFUND`**. Its `originalReference` is the **original payment PSP reference**, while its `pspReference` identifies the reversal/refund modification. The webhook table links a Checkout reversal response for that modification reference; the POS referenced-refund guide obtains the request reference in a Terminal API `ReversalResponse`. That cross-link does not make Checkout API a required second refund call.
- Unreferenced POS refund requests produce **`REFUND_WITH_DATA`**. Here `originalReference` is the **unreferenced refund request's PSP reference**, not the unknown original payment PSP reference; `pspReference` is generated when the refund is captured. The available `additionalData` depends on enabled Standard-webhook settings. Do not join an unreferenced refund to an original purchase by treating this `originalReference` as an original-payment ID.
- For both event types, `success: true` means **Adyen's refund validations passed and the request was sent to the card scheme**. The guide says this usually leads to a successful refund, but rare later card-scheme rejection or reversal remains possible and points to `REFUND_FAILED` and `REFUNDED_REVERSED` exception routes. `success: false` reports validation failure with a `reason` to investigate. Neither generic Terminal API `Success` nor a validation-success webhook alone is irrevocable final settlement evidence.
- Unreferenced refunds can sometimes be processed **synchronously**, depending on card scheme and country/region; then `acquirerResponseCode` in the Terminal API response indicates the outcome. The page still frames the Standard webhook as the asynchronous outcome route for usual processing. It says a processed refund is deducted from the merchant's in-process funds and appears in the shopper's account within a few days; this is guidance, not proof of a particular bank's posting time.
- The failed-validation table includes requested refund exceeding remaining original-payment balance after refunds/chargebacks, insufficient merchant in-process funds, refund before capture, method expiry, too-small amount, and currency mismatch. The table's **balance on the payment** is the remaining original-payment amount; do not mechanically apply that referenced-payment balance identity to an unreferenced refund, whose original payment is not identified here.

## Detail locators

- Terminal API request-receipt versus webhook outcome, event-code split, conditional synchronous unreferenced exception and funds timing: raw lines 15-28.
- Terminal/Mobile integration and Standard webhook setup: raw `## Requirements`, lines 30-37.
- Referenced `CANCEL_OR_REFUND` validation, original versus modification PSP references, `success` meanings and example: raw `## CANCEL\_OR\_REFUND webhook`, lines 39-80.
- Unreferenced `REFUND_WITH_DATA` references, optional `additionalData`, `success` meanings and example: raw `## REFUND\_WITH\_DATA webhook`, lines 82-128.
- Failure reasons and defined remaining-payment balance: raw `## Reasons for failed refund validation`, lines 130-148. Follow cited linked exception pages for their full contracts; they are navigation from this page.

## Related

- Company: [[adyen]]
- Main POS concept: [[adyen-terminal-api]]
- Webhook concept: [[adyen-webhooks]]
- Referenced Terminal API procedure: [[source-adyen-docs-point-of-sale-basic-tapi-integration-refund-payment-referenced]]
- Unreferenced Terminal API procedure: [[source-adyen-docs-point-of-sale-basic-tapi-integration-refund-payment-unreferenced]]
- Separate online Checkout refund concept: [[adyen-refunds]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/basic-tapi-integration/refund-payment/refund-webhooks/2026-09-15|Adyen POS refund webhook outcomes]] — full captured webhook guide
