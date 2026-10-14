---
title: "Adyen POS gift-card refunds"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/alternative-payment-methods/gift-cards-terminal-api/refund-gift-cards"
raw_files:
  - "adyen/docs/point-of-sale/alternative-payment-methods/gift-cards-terminal-api/refund-gift-cards/2026-09-15.md"
tags: [adyen, point-of-sale, gift-cards, terminal-api, refunds, stored-value]
---

## Overview

This Adyen point-of-sale guide distinguishes refunding value **to a shopper's gift card** with or without the original payment reference. A referenced refund uses a Terminal API `ReversalRequest` tied to the original payment transaction; an unreferenced refund uses a `PaymentRequest` with `PaymentType=Refund` and supplies gift-card details. The guide explains the latter request in detail and links away for referenced-refund steps. Its last-modified field is 2019-11-14 and raw capture is 2026-09-15, so its instructions and examples are historical snapshot evidence. [[adyen]] [[adyen-pos-gift-cards]] [[adyen-pos-alternative-payment-methods]]

## Key takeaways

- Use the referenced path when refunding a payment made with the gift card and the original transaction identifier is available. The original identifier carries the card association, so this guide says gift-card details need not be repeated; it also says multiple partial referenced refunds are possible. Detailed referenced-refund behavior is delegated to a separate guide. The source does not establish a generic cancel, void, or automatic load operation.
- Use the unreferenced path when the refund cannot be connected to the gift-card payment, such as a merchandise return. It is a Terminal API `PaymentRequest` with `MessageCategory=Payment`, `PaymentType=Refund`, a `StoredValue` instrument and `GiftCard` account identity, plus the amount and currency to be returned **to the card**. This action differs from cashing out the card balance to the shopper; the page directs that to a separate cashback request. The stated setup assumes a Terminal API integration with payment terminals, the method added to the Adyen account, and provider onboarding.
- For an unreferenced refund, choose card entry before sending: scan and include obtained number/expiry in the request, or send first for terminal swipe/manual-key prompts. The request includes a terminal-scoped `ServiceID` unique for the preceding 48 hours, POS `SaleID`, terminal `POIID`, refund transaction reference/timestamp and `SaleReferenceID` order reference. The optional `SaleToAcquirerData` can carry long-number manual-entry display fields or an SVS-specific secondary security code (`ssc`), not a universal PIN rule.
- Check the `PaymentResponse` transaction ID, receipt data and `Response.Result=Success`; the example also displays `AmountsResp.AuthorizedAmount`, currency and `PaymentType=Refund`. Do not infer a refund outcome from request submission or assume the illustrative GBP 30, IDs, provider and card details apply to other transactions. The sample response uses a different provider, entry mode, card number and `SaleReferenceID` than the sample request, so they are not a matching end-to-end transaction record.
- This page does not specify provider-specific current eligibility, live account state, a universal partial-refund rule for unreferenced refunds, an idempotent retry contract, or a cancellation/void lifecycle. Its referenced path supports multiple partial refunds only in the stated original-payment context.

## Detail locators

- Raw `# Make a refund to a gift card` (lines 15–25): referenced versus unreferenced action, original-payment link, partial referenced refunds and cashback boundary.
- Raw `## Requirements` (lines 27–35): terminal integration, account method and provider onboarding.
- Raw `## Make an unreferenced refund` (lines 37–111): card entry, request header, identifiers, optional MKE/SVS tender options, currency/amount, refund payment type and stored-value card details.
- Raw request examples (lines 112–208): illustrative GBP 30 scanned-card JSON/Java; values are examples and do not create retry or provider guarantees.
- Raw response checks and example (lines 209–283): `Success`, transaction ID, receipt and response fields; request/response illustrations have mismatched provider and card/order details.

## Related

- [[adyen-pos-gift-cards]] — POS gift-card lifecycle and provider-specific actions.
- [[adyen-pos-alternative-payment-methods]] — in-person alternative-method umbrella.
- [[adyen-terminal-api]] — request/response context.

## Related raw API references

Navigation named by the guide, not further behavior reviewed for this entry:

- Referenced refund — https://docs.adyen.com/point-of-sale/basic-tapi-integration/refund-payment/referenced
- Gift-card cashback — https://docs.adyen.com/point-of-sale/gift-cards-terminal-api/deactivate#cashing-back-gift-card
- Terminal API PaymentRequest — https://docs.adyen.com/api-explorer/terminal-api/latest/post/payment

## Raw Sources

- [[raw/adyen/docs/point-of-sale/alternative-payment-methods/gift-cards-terminal-api/refund-gift-cards/2026-09-15|Make a refund to a gift card, fetched 2026-09-15]]
