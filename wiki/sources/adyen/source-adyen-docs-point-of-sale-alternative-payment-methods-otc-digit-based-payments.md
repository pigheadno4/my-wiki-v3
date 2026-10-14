---
title: "One-time numeric code payments | Adyen Docs"
type: source
date_ingested: 2026-10-14
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/alternative-payment-methods/otc-digit-based-payments"
raw_files:
  - "adyen/docs/point-of-sale/alternative-payment-methods/otc-digit-based-payments/2026-09-15.md"
tags: [adyen, point-of-sale, alternative-payment-methods, blik, poland, numeric-codes]
---

## Overview

This Adyen Docs guide describes in-person BLIK payments with a one-time six-digit numeric code generated in a shopper's BLIK banking app and entered on a payment terminal in Poland. A POS-integrated merchant can start a brand-specific flow or let the shopper choose BLIK on the terminal; a standalone terminal supports only the shopper-initiated flow. The banking app asks the shopper to confirm after code entry. This is a BLIK code and app-confirmation flow, not card tap/insert/swipe or a card PIN flow. See [[adyen]], [[adyen-pos-alternative-payment-methods]], and [[adyen-terminal-api]].

## Key takeaways

- The guide limits BLIK one-time numeric code payments to Poland and requires adding BLIK to the Adyen account before use. Terminal API with payment terminals or a standalone solution is in scope; standalone supports only shopper initiation. These documentation conditions do not prove current regional availability, merchant enablement or a completed payment.
- For merchant initiation, store staff choose BLIK in their POS app. The Terminal API `PaymentRequest` sets `PaymentTransaction.TransactionConditions.AllowedPaymentBrand` to an array containing `blik_pos`, alongside a standard payment message header, merchant sale-transaction reference, `AmountsReq.Currency` and final `RequestedAmount`. The sample uses PLN 10.99 and example IDs; those are sample values, not a universal amount or currency rule. The shopper then enters the six-digit code on the terminal and confirms the prompt in their BLIK banking app.
- For shopper initiation, the POS sends a normal payment request without the brand-specific field; the shopper chooses **Scan** then BLIK on the terminal and enters the code. The overview names the terminal option **BLIK** and notes **Inne** as Polish for Scan, while the detailed steps say **BLIK Code**. Treat those labels as page-specific UI wording, not a guaranteed terminal menu across versions. This path needs BLIK added in Customer Area, but the guide says no POS integration change.
- Both paths say the payment result is received as for a card payment and the shopper receipt includes BLIK's payment reference in `Transaction ref`. That comparison concerns result delivery; it does not make the transaction a card-present card payment or prove success. The shopper's separate banking-app confirmation remains part of the documented flow.
- One-time numeric code payments support full and partial **referenced** refunds through a Terminal API `ReversalRequest`. The page does not establish an unreferenced refund or generic void path. Its test section gives `999000` as a BLIK test code; test data does not demonstrate live acceptance.

## Detail locators

- `One-time numeric code payments` / `Requirements`, pinned raw lines 15–29: BLIK app-code identity, Poland-only and account activation conditions, integrated/standalone scope.
- `One-time numeric code payment flows`, lines 31–37: merchant versus shopper initiation, brand field, UI choices and standalone limitation.
- `Merchant-initiated flow`, lines 39–120: Terminal API request fields and `AllowedPaymentBrand` example, code/app-confirmation steps, result and receipt reference. The table's `paymentBrand` row at lines 66–72 has an incongruent amount/currency description; use the explicit `AllowedPaymentBrand` row and JSON example at lines 100–104 for the brand field.
- `Shopper-initiated flow`, lines 122–164: ordinary request example, terminal menu/code entry, app confirmation and result.
- `Refunds` and `Test`, lines 166–176: referenced `ReversalRequest`, full/partial support, and test code.

## Related

- [[adyen-pos-alternative-payment-methods]] — main in-person alternative-method route.
- [[adyen-terminal-api]] — payment and reversal message context.
- [[adyen-payment-testing]] — testing evidence is distinct from live processing.

## Raw Sources

- [[raw/adyen/docs/point-of-sale/alternative-payment-methods/otc-digit-based-payments/2026-09-15|Adyen BLIK one-time-code guide, fetched 2026-09-15]]
