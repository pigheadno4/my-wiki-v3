---
title: "Adyen Docs: Cancel an online payment"
type: source
date_ingested: 2026-10-10
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/cancel"
raw_files:
  - "adyen/docs/online-payments/cancel/2026-09-15.md"
tags: [adyen, online-payments, cancellation, checkout-api, webhooks]
---

## Overview

This [[adyen]] website-guide snapshot explains how to cancel an eligible [[adyen-online-payments|Adyen online payment]] before capture, either in Customer Area or through Checkout API. It applies when the payment method supports capture separately from authorization; the page says cancellation causes the financial institution to release the funds back to the shopper's bank account.

## Key takeaways

- A payment must still be uncaptured, and the payment method must support separate authorization and capture. After capture, this cancellation path is no longer available.
- Customer Area cancellation requires **View Payments** plus either **Merchant manage payments** or **Cancel payments**. The page also documents Checkout API routes using either Adyen's PSP reference or the merchant's original payment reference.
- The merchant-reference route is available only up to 24 hours after authorization. The page recommends it only when each payment request has a unique reference and the PSP reference is unavailable.
- When using the PSP-reference route, the page directs merchants who do not know whether the payment was captured to use the reversal endpoint instead of the cancellation endpoint.
- The request route determines the outcome webhook: a PSP-reference request is reported through **CANCELLATION**, while a merchant-reference request is reported through **TECHNICAL_CANCEL**. For **CANCELLATION**, `success: false` includes a reason; the raw page lists common failure reasons and remediation guidance.

> [!warning] Capture state and outcome
> Do not treat this page as a post-capture cancellation path. Verify that the payment is uncaptured, use reversal when the capture state is unknown as directed by the guide, and use the corresponding webhook to determine the cancellation request's outcome.

## Detail locators

- **Requirements** — online-payments integration, Customer Area roles, required webhook event codes, and the post-capture limitation.
- **Ways to cancel a payment** — Customer Area and Checkout API routes.
- **Cancel a payment using the Customer Area** — operational steps and the uncaptured-state UI condition.
- **Cancel a payment using the Checkout API → Cancel with PSP reference** — request route, required identifiers, reversal guidance, examples, SDK snippets, response fields, and CANCELLATION outcome route.
- **Cancel a payment using the Checkout API → Cancel with your reference** — 24-hour limit, uniqueness recommendation, request and response fields, and TECHNICAL_CANCEL outcome route.
- **Webhooks for cancellations** — route-specific webhook payload fields, success interpretation, examples, and common CANCELLATION failure reasons.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/online-payments/cancel/2026-09-15|Adyen Docs — Cancel (2026-09-15)]]
