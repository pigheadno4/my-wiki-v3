---
title: "Adyen for Platforms in-person tip split"
type: source
date_ingested: 2026-10-18
original_format: webpage
canonical_url: "https://docs.adyen.com/platforms/in-person-payments/tipping"
raw_files:
  - "adyen/docs/platforms/in-person-payments/tipping/2026-09-15.md"
tags: [adyen, platforms, in-person-payments, tipping, terminal-api, split-payments]
---

## Overview

This 2023-modified Adyen for Platforms guide, captured 2026-09-15, describes sending a **Tip** split item in a Terminal API payment request so the whole in-person gratuity is booked to one of a user's balance accounts. Without that split item, the tip is booked to the platform liable account by default. Its two routes are a tip proposed by the POS app and a tip chosen at the terminal. This is tip booking guidance, not evidence that a payment was authorized or a balance account received funds. [[adyen]] [[adyen-platforms]] [[adyen-terminal-api]]

## Key takeaways

- **Supported path and limits:** the guide requires a Terminal API integration with payment terminals or an Adyen Mobile solution, in addition to its linked general Platforms in-person requirements. Standalone cannot add split instructions to individual authorization requests. Booking the tip to a user's balance account is not supported with tipping on the receipt. The method-specific POS-app and terminal setup guides remain separate prerequisites/navigation.
- **Tip allocation is distinct from sale, commission and fee allocation:** add a Tip item and increment `split.nrOfItems`; set its `account` to a user's `balanceAccountID`. The whole tip goes to one balance account; this page disallows dividing it among multiple balance accounts. Reference and description flow to the Balance Platform Accounting Report. Do not put a tip amount in that split item or include it in `split.totalAmount`. The example allocates the sale, platform commission and PaymentFee separately; those sample allocations do not define a required fee or commission policy.
- **POS-app tip:** provide the formatted split instructions in `SaleData.SaleToAcquirerData`, plus transaction currency, original requested amount and `PaymentTransaction.AmountsReq.TipAmount` in the Terminal API `PaymentRequest`. Split instructions may be form-encoded key-value pairs or a Base64-encoded JSON object.
- **Terminal-selected tip:** include `tenderOption=AskGratuity` with the split instructions in `SaleToAcquirerData`; the request supplies transaction currency and original requested amount while the tip is determined at the terminal. The response's `TipAmount` is absent when the shopper declines; `AuthorizedAmount` is original transaction amount plus tip. The response's additional fields report original amount, gratuity and total authorized amount in minor units.
- **Example and evidence limits:** the page's POS-app JSON request omits a comma between `RequestedAmount` and `TipAmount`; its terminal JSON request says `split.nrOfItems=3` while showing four split items and differs from the preceding four-item example. Treat snippets and sample Success responses as illustrative, not copy-ready payloads or proof of funds booking. This page gives no separate capture, partial-capture, refund, chargeback, surcharge, card-method or region rules, and its example `ProtocolVersion: "3.0"` is a message header, not a claimed current SDK baseline.

## Detail locators

- Raw lines 15–34: default liable booking, supported tipping methods, Terminal API/Mobile requirement and receipt/standalone limits.
- Raw lines 36–67: POS-app Tip split fields, single-account restriction, `split.totalAmount` exclusion and separate sale/commission/fee example.
- Raw lines 69–206: form-encoded/Base64 examples, Terminal API request/response fields and the missing-comma request snippet.
- Raw lines 238–269: terminal Tip split and amount handling; lines 271–360 add `AskGratuity` and encoding.
- Raw lines 363–408: terminal request item-count mismatch and response field definitions; lines 410–438 show an illustrative Success response.

## Related

- [[source-adyen-docs-platforms-in-person-payments-split-transactions-split-payments-at-authorization]] — general per-payment Terminal API split mechanics and failure/booking qualifications.
- [[source-adyen-docs-point-of-sale-tipping]] — general choice among POS app, terminal, receipt and standalone tipping.
- [[source-adyen-docs-point-of-sale-tipping-tipping-from-cash-register]] — POS-app gratuity request and shopper-choice details.
- [[source-adyen-docs-point-of-sale-tipping-tipping-from-terminal]] — terminal gratuity request and shopper-choice details.

## Raw Sources

- [[raw/adyen/docs/platforms/in-person-payments/tipping/2026-09-15|Adyen Platforms in-person tipping snapshot, fetched 2026-09-15]]
