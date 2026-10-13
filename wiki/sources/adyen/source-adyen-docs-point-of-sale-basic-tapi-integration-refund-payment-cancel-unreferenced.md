---
title: "Adyen POS cancel an unreferenced refund"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/basic-tapi-integration/refund-payment/cancel-unreferenced"
raw_files:
  - "adyen/docs/point-of-sale/basic-tapi-integration/refund-payment/cancel-unreferenced/2026-09-15.md"
tags: [adyen, point-of-sale, unreferenced-refund, refund-cancellation, payment-api, webhooks]
---

## Overview

This unversioned Adyen website guide, captured on 2026-09-15, explains how a merchant can **cancel a pending POS unreferenced refund** before completion. The request is a backend **Payment API `/voidPendingRefund` call**, explicitly not a Terminal API request and not a Checkout API refund call. It targets the **original refund request**, not the shopper's original purchase or an already completed refund. See [[adyen-terminal-api]] for the POS boundary.

## Key takeaways

- Cancellation requires a **configured refund delay** set up through Adyen Support. The delay applies only to unreferenced refunds; a referenced refund cannot be cancelled through this flow. If no delayed POS refund is configured, or the delay has expired, the pending refund cannot be cancelled. The guide covers integrated or standalone terminals and Mobile solutions.
- The merchant needs an API key for the POS app and Standard webhooks for the cancellation outcome. For cloud-based terminal communications, the existing Terminal API request key can be reused. The page does **not** name a distinct API-credential role for this operation; do not import a role from the separate unreferenced-refund enablement guide.
- Preferred reference route: POST `/voidPendingRefund` with `merchantAccount`, the **tender reference of the refund request**, and `uniqueTerminalId` of the terminal that processed that refund. Adyen recommends this because a tender reference is generated for offline and online in-person transactions. The tender reference here is not the shopper's original purchase tender reference.
- Alternative route: POST the same endpoint with `merchantAccount` and `originalReference` set to the **PSP reference of the original unreferenced refund request**. This is neither the shopper's original payment PSP reference nor the PSP reference of the new void request. The response's `pspReference` belongs to the **`/voidPendingRefund` request** and its `[voidPendingRefund-received]` state acknowledges receipt, not successful cancellation.
- After processing, Adyen sends `VOID_PENDING_REFUND` in a Standard webhook; its `success` field states whether cancelling the refund succeeded. The example has `originalReference` and a distinct void `pspReference`, but the page only explicitly defines `eventCode` and `success` for this webhook. It does not establish a funds transfer or shopper-bank posting state from request receipt.

## Detail locators

- Purpose, delay requirement, backend API identity and tender-versus-PSP recommendation: raw lines 15-21.
- Integrated/standalone/Mobile scope, API key, cloud-key reuse, Standard webhooks, referenced-refund exclusion and expired-delay boundary: raw `## Requirements`, lines 23-32.
- Tender-reference route, original refund terminal ID and received response with its own PSP reference: raw `## Cancel with tender reference`, lines 34-61.
- Refund-request PSP reference in `originalReference` and separate void response PSP reference: raw `## Cancel with PSP reference`, lines 63-91.
- `VOID_PENDING_REFUND` event and `success` outcome: raw `## Webhooks`, lines 93-122.
- Linked unreferenced-refund, API reference and generic webhook pages: raw `## See also`, lines 124-128; use them as navigation for further details.

## Related

- Company: [[adyen]]
- POS concept and Terminal API boundary: [[adyen-terminal-api]]
- Unreferenced refund request and enablement: [[source-adyen-docs-point-of-sale-basic-tapi-integration-refund-payment-unreferenced]]
- Refund webhook outcome: [[source-adyen-docs-point-of-sale-basic-tapi-integration-refund-payment-refund-webhooks]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/basic-tapi-integration/refund-payment/cancel-unreferenced/2026-09-15|Adyen POS cancel an unreferenced refund]] — full captured cancellation guide
