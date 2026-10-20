---
title: "Adyen Issuing: Process customer payments to fund issued cards"
type: source
date_ingested: 2026-10-20
original_format: webpage
canonical_url: "https://docs.adyen.com/issuing/add-manage-funds/process-payments/make-a-payment"
raw_files:
  - "adyen/docs/issuing/add-manage-funds/process-payments/make-a-payment/2026-09-15.md"
tags: [adyen, issuing, payments, balance-platform]
---

## Overview

Adyen Issuing guide, last modified and captured 2026-09-15, for processing **payments from the platform's customers** through Adyen online or in-person payment processing in combination with Issuing. It says revenue from those payments is booked to the platform's balance platform and can fund Adyen-issued cards. The page does not identify a particular balance account, provide split instructions or prove any live payment, card load, settlement or card transaction. [[adyen]] [[adyen-issuing]]

## Key takeaways

- **Prerequisites differ by channel.** Online payments need an online payments integration and checkout UI; in-person payments need a POS app integrated with Terminal API plus terminals or a mobile solution, with standalone as a fallback. The requirements list Checkout API credentials for online, Terminal API for in-person, Transfers API and a server accepting standard webhooks. Account holders need `receivePayments`, `receiveFromPlatformPayments` and `sendToTransferInstrument` capabilities. **Webhook wording conflict:** the Requirements table says subscribe to **any of** Transfer or Transaction webhooks, while the final Webhooks section says subscribe to **Transfer and Transaction** webhooks; do not infer one unambiguous minimum from this page. See raw lines 21–35 and 177–179. These are the guide's stated prerequisites, not proof of a platform's current eligibility.
- **Online route:** POST Checkout `/payments` or `/sessions`, supplying amount, merchant account, payment method, reference and return URL as shown in the guide. Its amount value uses **minor units**; the example is a test-host `/v68/payments` request for EUR 200.00. Check the response for payment outcome. See raw **Online payments**, lines 37–79; use the current endpoint contract for implementation details.
- **In-person route:** POST Terminal API `PaymentRequest`, with `SaleToPOIRequest.MessageHeader` and `PaymentRequest` objects. The guide calls for `MessageClass: Service`, `MessageCategory: Payment`, and a `ServiceID` unique for the terminal in the prior 48 hours. Unlike the online amount, `PaymentTransaction.AmountsReq.RequestedAmount` uses a decimal amount, **not minor units**. The customer completes the payment at a terminal or mobile device; inspect the returned `PaymentResponse.Response.Result`, transaction ID and receipt data. See raw **In-person payments**, lines 81–148.
- **Example boundary:** The in-person request/response examples are titled “with split instructions” and “Payment split successful,” but the shown `PaymentRequest` has no split instruction field or account-allocation details. The request is for EUR 200.00 while the purported response's `AdditionalResponse` contains `posAuthAmountCurrency=USD` and `posAuthAmountValue=8000`; these are not a coherent amount/currency trace. The examples do not establish the requested payment, split configuration, a particular recipient balance account or an actual successful payment. The surrounding prose describes an approval as part of its illustrative flow; check real response and later events for an actual payment. See raw lines 108–173, especially 131–135 and 166.
- Transfer and Transaction webhooks provide payment-related balance-platform event/status tracking; the Customer Area payment list is another view. The page does not specify a guaranteed time when payment proceeds become spendable on an issued card. See raw **Webhooks**, lines 175–179.

## Detail locators

- Online field table and test curl example: raw lines 41–77.
- Terminal header, transaction reference and decimal amount fields: raw lines 85–107.
- Terminal request and response examples, including tender/PSP reference description: raw lines 108–173.
- Customer Area Payments → Payment list: raw line 175.

## Related

- [[adyen-issuing]] — Issuing concept and source route.
- [[adyen]] — provider context.

## Raw Sources

- [[raw/adyen/docs/issuing/add-manage-funds/process-payments/make-a-payment/2026-09-15|Make a payment — 2026-09-15 capture]]
