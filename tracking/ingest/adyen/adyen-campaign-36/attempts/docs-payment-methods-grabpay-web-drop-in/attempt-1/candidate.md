---
title: "GrabPay Web Drop-in integration | Adyen Docs"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/grabpay/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/grabpay/web-drop-in/2026-09-15.md"
tags: [adyen, grabpay, web, drop-in, paylater, wallet]
---

## Overview

This [[adyen]] guide adds GrabPay to an existing **Web Drop-in** integration. It separates Sessions and Advanced base-flow prerequisites, then gives GrabPay **PayLater** request fields for `/sessions` and `/payments`. It also distinguishes those fields from GrabPay **Wallet**, for which the same information is recommended but not stated as required. See [[adyen-online-payments]] and the pinned raw. The guide does not provide a final payment-outcome procedure.

## Key takeaways

- **Base prerequisites:** Sessions requires an existing Sessions Web Drop-in integration; Advanced requires an existing Advanced Web Drop-in integration. Both require adding GrabPay in Customer Area before proceeding. These are integration/setup conditions, not proof of present merchant enablement. See raw lines 21–37.
- **PayLater versus Wallet:** PayLater, whether postpaid or installment, needs the delivery address and purchased-item information. The page marks `deliveryAddress` and `lineItems` required for PayLater in both endpoint tables. It highly recommends sending those fields for an initial GrabPay Wallet integration to ease a possible later PayLater enablement, but calls them needed **only for PayLater**. Do not convert the Wallet recommendation into a requirement. See raw lines 39–57 and 510–517.
- **Endpoint/version split:** `/sessions` is described as the default with Web Drop-in v5.0.0 or later. The `/payments` tab is for an additional use case or an integration made before Web Drop-in v5.0.0. Both tables identify the PayLater address/item fields; the SG/SGD `grabpay_SG` requests are examples, not proof of every supported country or currency. See raw lines 48–57, 61–93 and 510–555.
- **Drop-in and live scope:** The guide says there are no GrabPay-specific Drop-in configuration steps. For testing, it directs merchants to Support for test wallet credentials and describes a simulator login using a registered phone number and one-time password. Before live acceptance it says to submit a GrabPay request in the live Customer Area. No example request, simulator step or return URL proves authorization, capture or settlement. See raw lines 811–824.

> [!warning] Example amount mismatch
> The PayLater `/sessions` curl example has an order amount of **1000 SGD minor units** while its sole line item has quantity `1` and `amountIncludingTax: 400`. The `/payments` curl example repeats this 1000-versus-400 pattern. The page does not explain the difference, so do not treat these sample totals as a validated itemization rule. See raw lines 65–91 and 525–554.

## Detail locators

- `/sessions` PayLater fields and curl, Java, PHP, C#, Node.js, Go, Python, Ruby and TypeScript examples: raw lines 50–508. The examples name library versions and TEST environments independently; they do not define a universal SDK minimum.
- `/payments` PayLater fields and curl, Java, PHP, C#, Node.js, Python and Ruby examples: raw lines 510–809. The `grabpay_SG` type appears in these examples, not in a method-wide country matrix on this page.
- No token/recurring, capture, refund, cancellation, callback or webhook outcome procedure is specified here; the See also links at raw lines 826–831 are navigation to separate authority.

## Related

- [[adyen-online-payments]] — main online payment architecture and method routes.

## Raw Sources

- [[raw/adyen/docs/payment-methods/grabpay/web-drop-in/2026-09-15|GrabPay Web Drop-in guide, 2026-09-15 snapshot]]
