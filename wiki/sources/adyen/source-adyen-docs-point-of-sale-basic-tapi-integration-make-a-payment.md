---
title: "Adyen Docs: Make an in-person Terminal API payment"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/basic-tapi-integration/make-a-payment"
raw_files:
  - "adyen/docs/point-of-sale/basic-tapi-integration/make-a-payment/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, in-person-payments, payment-response]
---

## Overview

This Adyen guide describes a basic in-person card payment request from a merchant POS app through Terminal API to a boarded payment terminal or, for a Mobile solution, a test mobile device. It covers the request header and payment data, shopper interaction, response fields, and missing/failure response handling. The page documents request and authorization-result handling; its examples do not prove merchant eligibility, a particular card or wallet's availability, capture or settlement, current SDK behavior, or successful execution in a reader's environment. See [[adyen-terminal-api]].

## Key takeaways

- Before testing, the merchant must have scoped and designed the applicable terminal or Android/iOS Mobile solution, followed its checklist to the test-payment step, and have a POS test card plus a boarded test terminal or test mobile device. A POS app sends the payment request; the shopper presents a card or NFC wallet and may enter PIN or signature; Adyen attempts authorization and the terminal/device displays approval or decline. These presentation examples are not a payment-method eligibility promise. See **Requirements** and **How it works**.
- A payment uses `SaleToPOIRequest.MessageHeader` with protocol 3.0, service/payment/request classifications, a POS-component `SaleID`, terminal `POIID` in model–serial form, and a `ServiceID` of 1–10 alphanumeric characters unique over the last 48 hours for that `POIID`. `PaymentRequest` includes a merchant-side `SaleTransactionID` reference and UTC timestamp, plus currency and final requested decimal amount. Adyen recommends a unique merchant reference per payment. Exact fields and the USD 10.99 example are at **Make a payment request**; the example is not a current SDK or schema guarantee.
- The POS checks `PaymentResponse`, or receives it through an event notification for asynchronous cloud communications with terminals. `POIData.POITransactionID.TransactionID` is the returned terminal transaction identifier to save for lookup, reconciliation, or later requests; it differs from the POS-provided merchant reference. `Response.Result` can be `Success` for approved, `Failure` for declined, or `Partial` for partial authorization. On failure, `ErrorCondition` and possibly `AdditionalResponse` help identify the cause. The response may also contain receipt data. See **How it works** and **Make a payment request → PaymentResponse**.
- `AdditionalResponse` may be form-encoded key/value pairs or Base64-encoded JSON; the page says Support can be asked to ensure one format. Its approved and shopper-cancelled response bodies are illustrative, not proof that every payment returns the same fields or that approval establishes capture/settlement. See **Make a payment request → PaymentResponse**.
- If no direct or asynchronous response arrives, the page strongly recommends automatic transaction-status verification before staff risk an unnecessary refund or duplicate charge. A failure response calls for inspecting `Result`, `ErrorCondition`, and `AdditionalResponse` and following the separate response/refusal guidance before retry decisions. The test-only example says requested amounts ending in 123 cents can simulate a decline; it is not a live-acquirer rule. See **Troubleshooting** and **Testing**.

## Detail locators

- **Requirements** — terminal versus Android/iOS Mobile test paths, POS test card, boarded terminal/device, and applicable setup checklists.
- **How it works** — POS request, shopper interaction, authorization attempt, response ownership, and asynchronous cloud event route.
- **Make a payment request** — header identity and classification fields; merchant reference, UTC timestamp, currency/amount; JSON and Java examples.
- **Make a payment request → PaymentResponse** — terminal transaction ID, `Success`/`Failure`/`Partial`, error and additional-response formats, receipts, and illustrative approved/declined payloads.
- **Troubleshooting → No response** — status verification for missing or long-running responses and duplicate-action risk.
- **Troubleshooting → Failure** — failure/error fields and navigation to response/refusal-reason guidance.
- **Testing** — test card and boarded terminal/mobile-device requirements and decline simulation example.

## Related

- [[adyen]]
- [[adyen-terminal-api]]

## Raw Sources

- [[raw/adyen/docs/point-of-sale/basic-tapi-integration/make-a-payment/2026-09-15|Adyen Docs — Make a payment (2026-09-15)]]
