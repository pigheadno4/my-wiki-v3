---
title: "Adyen POS referenced refund"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/basic-tapi-integration/refund-payment/referenced"
raw_files:
  - "adyen/docs/point-of-sale/basic-tapi-integration/refund-payment/referenced/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, referenced-refund, reversal, offline-payments]
---

## Overview

This unversioned Adyen website guide, captured on 2026-09-15, explains a **referenced POS refund** connected to an original approved payment. Its basic full and partial paths send a Terminal API `ReversalRequest` through a POS terminal or Mobile solution, using the original payment's Terminal API `TransactionID` and timestamp. This is a [[adyen-terminal-api]] refund procedure; the cited online Checkout API refund concept is a separate integration path. The page does not prescribe a different referenced-refund procedure for local versus cloud Terminal API communications.

## Key takeaways

- A POS payment response identifies the original transaction as `tenderReference.pspReference`. For a basic referenced refund, the merchant places that full identifier and original UTC timestamp in `OriginalPOITransaction.POITransactionID`. The request has `MessageCategory: Reversal`, `ReversalReason: MerchantCancel`, and a terminal `POIID` in the message header. This reference lets Adyen validate against the original payment, including whether it was already refunded.
- Full refund returns the purchase total. Partial refund adds `ReversedAmount` as a number no larger than the initial payment amount, a `currency=ABC` value matching the original payment in `SaleData.SaleToAcquirerData`, and a merchant refund reference/time. The guide allows multiple partial refunds; it does not establish an account-specific or per-method allowance from that example.
- A successful `ReversalResponse.Response.Result` means Adyen **received** the request, while the refund is processed asynchronously. The refund request has its **own** PSP reference, distinct from the original payment identifier. A receipt can say **REFUND REQUESTED**. The merchant waits for the `CANCEL_OR_REFUND` webhook to learn the outcome; neither a response nor receipt proves completed refund.
- An offline payment response lacks a PSP reference until Adyen processes it. When back online, the merchant can use the PSP reference from a standard webhook or Customer Area for the regular referenced path, or use the original **tender reference and payment date**; the guide says an original device identifier is needed in most cases and marks `OriginalPOITransaction.POIID` required in the illustrated tender-reference forms. The device identifier may be a terminal ID, NYC1 card-reader ID, or Tap to Pay installation ID as documented. A tender-reference refund made before offline processing is queued and retried; the page describes `Authorised` → `Cancelled` before funds transfer and `Sent for Settle` → `Refunded` after that status. The offline-refund-when-back-online Mobile path is limited here to **iOS Mobile**; the page separately limits Tap to Pay on iPhone Store and Forward offline payments to the **US**.
- For a Terminal API refund of an **ecommerce** payment, there is no tender reference. The guide requires original PSP reference, date and currency, with `TransactionID` formatted as **`.pspReference` including the leading dot**; it warns that omission produces `unreachable host`. Its full-refund response reports zero original/refund amounts because those amounts are not yet known at that point. This is a special Terminal API reversal form, not the ordinary Checkout API refund call.

## Detail locators

- Purpose, `tenderReference.pspReference` identity, full/partial possibilities and requirements: raw lines 15-36.
- Full Terminal API `ReversalRequest`, header `POIID`, original transaction fields, `MerchantCancel`, response acknowledgement, own PSP reference and webhook outcome: raw `### Tab: Full refund`, lines 42-186.
- Partial amount, currency and merchant reference fields plus asynchronous result: raw `### Tab: Partial refund`, lines 188-356.
- Offline missing-PSP condition, webhook or tender-reference routes, queueing/status behavior, and original device ID variants: raw `## Refund an offline payment when back online`, lines 358-454.
- Ecommerce original-reference leading-dot syntax and zero amount fields: raw `## Refund an ecommerce payment`, lines 456-555.
- Further outcome/offline links: raw `## See also`, lines 557-561; use these as navigation only.

## Related

- Company: [[adyen]]
- Main concept: [[adyen-terminal-api]]
- Separate online Checkout refund concept: [[adyen-refunds]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/basic-tapi-integration/refund-payment/referenced/2026-09-15|Adyen POS referenced refund]] — full captured Terminal API refund guide
