---
title: "Adyen Payment API POST /voidPendingRefund — cancel pending POS unreferenced refund"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/api-explorer/Payment/latest/post/voidPendingRefund"
raw_files:
  - "adyen/api-explorer/Payment/latest/post/voidPendingRefund/2026-09-15.md"
tags: [adyen, payment-api, point-of-sale, unreferenced-refund, refund-cancellation]
---

## Overview

This 2026-09-15 Payment API Explorer snapshot describes `POST /voidPendingRefund` for requesting cancellation of a **pending in-person unreferenced refund before completion**. It addresses the original **refund request**, not the original shopper purchase or a general Checkout online refund. The captured server is Payment API **v68 test**, although the canonical URL says `latest`. The reference does not itself label this POS endpoint inactive or specify a Checkout replacement. See [[adyen-terminal-api]] and the detailed POS cancellation guide.

## Key takeaways

- The opening text allows identification of the original refund request by its `tenderReference` or `pspReference`, recommending the tender reference because it exists for offline and online transactions. The request table marks `merchantAccount` required. Its two examples show `merchantAccount` with either `originalReference` (PSP-reference route) or `tenderReference` plus `uniqueTerminalId` (terminal route). The table marks those selector fields optional individually; it does not make a request without a selector meaningful.
- The generic request-body description for `originalReference` says the original payment PSP reference, which conflicts in object identity with this endpoint's opening direction to reference the original **refund request**. Use the endpoint-specific POS cancellation guide to resolve the target before implementation; do not substitute the original purchase PSP reference merely from the reused field description. The `pspReference` returned in this endpoint's response identifies the new void request, not proof that the refund was cancelled.
- `200 Success` states the request succeeded at the API layer. The required response `response` field indicates only that the modification request was **received for processing**; examples show `[voidPendingRefund-received]`. This is not confirmation of successful cancellation, a reversal of funds, or a completed shopper-bank outcome. The detailed POS guide separately documents the later webhook outcome.
- The request schema includes broad generic modification fields such as `modificationAmount`, MPI data, and platform split/chargeback fields. Their table presence is not evidence that these are needed or meaningful for voiding this pending refund; the two endpoint examples use neither. Error sections document `400`, `401`, `403`, `422`, and `500` classes, with generic examples for `400`, `401`, and `500`.

## Detail locators

- Endpoint purpose, original-refund selector recommendation, and v68 test server: raw lines 5–15.
- Request schema, generic `originalReference` description, tender/terminal identifiers and incidental generic modification fields: raw lines 18–55.
- PSP-reference and tender-reference request examples: raw lines 57–74.
- `200` acknowledgement and response identity: raw lines 75–85 and examples at 157–175.
- Error schemas and generic examples: raw lines 88–155 and 177–212.

## Related

- Company: [[adyen]]
- Main POS concept: [[adyen-terminal-api]]
- Detailed cancellation guide: [[source-adyen-docs-point-of-sale-basic-tapi-integration-refund-payment-cancel-unreferenced]]

## Raw Sources

- [[raw/adyen/api-explorer/Payment/latest/post/voidPendingRefund/2026-09-15|Payment API POST /voidPendingRefund (2026-09-15)]]
