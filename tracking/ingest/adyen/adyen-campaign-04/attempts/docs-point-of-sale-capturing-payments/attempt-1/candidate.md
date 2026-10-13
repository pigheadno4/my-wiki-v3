---
title: "Capture in-person payments | Adyen Docs"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/capturing-payments"
raw_files:
  - "adyen/docs/point-of-sale/capturing-payments/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, capture, authorization, webhooks]
---

## Overview

Adyen's point-of-sale capture guide explains automatic immediate, delayed automatic, and manual capture of in-person payments made through a Terminal API integration. It describes capture and cancellation after authorization, using Checkout API payment-modification requests from a POS app. The page is a 2026-09-15 website snapshot, not a merchant eligibility check, a current Checkout API schema, a library-version authority, or proof of a particular payment outcome.

## Key takeaways

- Immediate automatic capture after authorization is the default. For payment methods that support separate capture, delayed automatic capture gives the merchant time to cancel an uncaptured authorization; manual capture requires a later capture request. Adyen recommends a delay for POS payments so a mistake can be cancelled before capture rather than refunded afterward.
- Capture mode or delay can be configured per merchant account in Customer Area or per Terminal API payment request through `SaleData.SaleToAcquirerData` (`captureDelayHours` or `manualCapture`). A per-payment API setting overrides the merchant-account setting. The Customer Area configuration calls for Merchant admin, View Payments, and Merchant manage payments roles; capture and cancellation requests require an API key, and asynchronous outcomes require webhooks.
- Separate capture depends on the in-person payment method. Most wallets do not support it; Alipay and WeChat Pay are captured immediately and cannot use delayed capture. Single partial capture cancels the unclaimed amount. Multiple partial captures retain the balance but are disabled by default and require Adyen Support enablement. Card-scheme authorization type and capture-period limits can matter; inspect the relevant raw sections and failed-request reasons.
- For manual capture, obtain the authorization `pspReference` from the Terminal API payment response `transactionID`, then call Checkout API `POST /payments/{paymentPspReference}/captures` with the authorization reference, merchant account, and amount in matching currency. Its separate capture `pspReference` and `status: received` identify an asynchronously accepted request, not final capture or settlement. Await the `CAPTURE` webhook. A successful `CAPTURE` event means a valid request was submitted onward; a rare later `CAPTURE_FAILED` can report scheme or issuer rejection, even days later.
- With delay or manual capture, an uncaptured authorization can be cancelled through Checkout API `POST /payments/{paymentPspReference}/cancels`; the `CANCELLATION` webhook gives the asynchronous result. When capture status is uncertain, this page points to the reversal route instead of an ordinary cancel request. A received cancel response is not the cancellation result.

## Detail locators

- `Requirements` and `Types of capture` — Terminal API prerequisite, Customer Area roles, wallet restrictions, partial-capture behavior and Support enablement.
- `Delayed automatic capture` — account-level POS capture delay, per-payment `captureDelayHours`, override precedence, and special delayed-capture webhook settings; automatic capture does not normally emit a separate `CAPTURE` webhook.
- `Manual capture` > `Enable manual capture` — Customer Area setting, API key, Standard webhooks, and per-payment `manualCapture` flag with Base64 JSON and key-value examples.
- `Manual capture` > `Capture a payment` — Terminal API response reference, Checkout capture path, amount/currency fields, example test request, distinct response references and `received` status. Example library versions and test endpoint are illustrative within this snapshot.
- `Webhooks for captures` — CAPTURE validity and refusal reasons, later CAPTURE_FAILED, and the remaining authorized balance.
- `Cancel an authorization` and `CANCELLATION webhook` — uncaptured-payment condition, cancel versus reversal, API key, response identifiers and asynchronous outcome.

## Related

- Company: [[adyen]]
- Concept: [[adyen-terminal-api]]
- Related capture concept: [[adyen-payment-capture]] (currently covers the online-payments guide; use this page for POS specifics)
- Related webhook concept: [[adyen-webhooks]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/capturing-payments/2026-09-15|2026-09-15 Adyen POS capture guide]]
