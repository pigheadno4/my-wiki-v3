---
title: "Adyen Docs: Tipping from a POS app"
type: source
date_ingested: 2026-10-13
original_format: webpage
canonical_url: "https://docs.adyen.com/point-of-sale/tipping/tipping-from-cash-register"
raw_files:
  - "adyen/docs/point-of-sale/tipping/tipping-from-cash-register/2026-09-15.md"
tags: [adyen, point-of-sale, terminal-api, tipping, gratuity]
---

## Overview

This Adyen Docs guide covers tipping **from the cash register/POS app**. The POS calculates a proposed tip and includes `TipAmount` alongside the original `RequestedAmount` in a Terminal API payment request. The terminal shows both amounts; the shopper may accept, change, or decline the tip before completing payment. The amount later authorized and returned is based on the shopper's choice, not merely the POS proposal. See [[adyen-terminal-api]] and [[adyen]].

## Key takeaways

- **Scope and setup:** the stated integration is Terminal API with payment terminals; all terminal models except unattended terminals are supported. The merchant implements its own POS logic to choose a proposed tip, such as a percentage or fixed amount. This page names no separate Support enablement step, universal numeric maximum, or `TipAmount` field-type constraint beyond the illustrated amount; do not borrow such conditions from a different terminal-prompt tipping path. [Raw: Requirements; Set up tipping in your POS app]
- **Request and authorization:** send a `PaymentRequest` with `PaymentTransaction.AmountsReq.Currency`, original `RequestedAmount`, and proposed `TipAmount`. The terminal lets the shopper accept, change, or decline the tip, then sends the original transaction amount **plus the chosen tip** to the Adyen platform for authorization. The example uses EUR 142.50 and a proposed 10% tip; those values are illustrative. This is a payment flow, not a later separate capture adjustment. [Raw: Make a payment, request and routing]
- **Actual response and receipt:** for the successful illustrated flow, `PaymentResult.AmountsResp.TipAmount` is the tip amount actually added and is **absent if no tip was added**; `AuthorizedAmount` is the total original-plus-tip amount. `PaymentReceipt` can carry original, tip (omitted without tip), and total. `AdditionalResponse` has original, gratuity, and total-authorized amounts in **minor units**. Interpret the response rather than assuming the proposed tip was accepted. [Raw: Make a payment, PaymentResponse fields]
- **Reporting boundary:** the page says the Settlement details report can include a gratuity amount column. That reporting navigation does not establish that this example settled or paid out. [Raw: Add tip amounts to reporting]

## Detail locators

- Raw `Requirements` and `Set up tipping in your POS app` identify supported terminals and merchant-owned tip calculation.
- Raw `Make a payment` locates the Terminal API message/request fields, proposed-tip example, shopper choice, response amount fields, receipt behavior, and minor-unit additional data.
- Raw `Add tip amounts to reporting` locates the optional gratuity report column; the linked reporting instructions under it and `See also` are navigation only.

## Related

- [[adyen-terminal-api]] — existing in-person API concept, including a separate terminal-prompt tipping route
- [[adyen]] — company and knowledge-status page

## Raw Sources

- [[raw/adyen/docs/point-of-sale/tipping/tipping-from-cash-register/2026-09-15|Tipping from the POS app — Adyen Docs snapshot, 2026-09-15]]
