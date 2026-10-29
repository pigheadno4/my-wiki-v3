---
title: "Adyen Titres-restaurant iOS Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/titres-restaurant/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/titres-restaurant/ios-drop-in/2026-09-15.md"
tags: [adyen, titres-restaurant, meal-voucher, ios, drop-in, partial-payments]
---

## Overview

This captured Adyen guide adds Titres-restaurant to an existing iOS Drop-in integration. It distinguishes the default `/sessions` path, which needs no method-specific iOS Drop-in configuration, from an additional-use-case `/payments` path with balance and order callbacks for split tender. It is documentation, not proof of current merchant or issuer eligibility, live activation, or a completed payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Setup and version qualification:** The requirements table sets a minimum iOS Drop-in version of **5.4.0**. Activate Titres-restaurant to obtain a *Carte de domiciliation CONECS*, then add the meal-voucher method in Customer Area with SIRET and Conecs MID. The API reference and Sessions tab also call `/sessions` the default from v5.0.0; that broader statement does not remove this page's 5.4.0 requirement. The page says no additional Titres-restaurant request fields are needed. [Raw: lines 21–44]
- **Sessions result:** For the `/sessions` tab, the page says no Titres-restaurant-specific iOS Drop-in integration is required. The payment result is returned in `didComplete`. This is distinct from the `/payments` callback configuration below. [Raw: lines 40–52]
- **Balance and order callbacks for `/payments`:** For the additional-use-case `/payments` path, configure `checkBalance` to call `/paymentMethods/balance` when the shopper pays with the meal voucher. When balance is below the transaction total, `requestOrder` calls `/orders` for the **total transaction amount** so the voucher and another method can fund a partial-payment order. If the shopper cancels the meal-voucher transaction, `cancelOrder` calls `/orders/cancel`. The Swift `PartialPaymentDelegate` block is an illustrative callback sketch, not evidence that an order or payment succeeded. [Raw: lines 50–81]
- **Outcome and capture boundary:** On the `/payments` path, use its `resultCode` to show the shopper a result and expect the outcome asynchronously by webhook. The listed outcomes are `Authorised`, `Cancelled`, `Error`, and `Refused`. If manual capture is used, an `Authorised` payment still needs capture. A low-balance order request or balance check is not itself payment authorization. [Raw: lines 83–94]
- **Test and live gate:** Test credentials must come directly from Bimpli, Sodexo, or Up Déjeuner. Live acceptance requires contacting Adyen Support to activate Titres-restaurant in the live environment. [Raw: lines 96–100]

## Detail locators

- iOS Drop-in purpose, CONECS/SIRET/MID setup, version and endpoint statements: pinned raw lines 15–44.
- Sessions `didComplete` result and `/payments` conditional callbacks with Swift sketch: pinned raw lines 46–81.
- `/payments` result codes, asynchronous webhook, manual capture, and test/live steps: pinned raw lines 83–106.

## Related

- [[adyen-online-payments]] — provider online payment architecture and method routes.
- [[source-adyen-docs-payment-methods-titres-restaurant]] — separate meal-voucher method overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/titres-restaurant/ios-drop-in/2026-09-15|Titres-restaurant iOS Drop-in, captured 2026-09-15]]
