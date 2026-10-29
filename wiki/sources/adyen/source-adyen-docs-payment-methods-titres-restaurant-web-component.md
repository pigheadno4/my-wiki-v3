---
title: "Adyen Titres-Restaurant Web Component integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/titres-restaurant/web-component"
raw_files:
  - "adyen/docs/payment-methods/titres-restaurant/web-component/2026-09-15.md"
tags: [adyen, titres-restaurant, meal-voucher, web, components, partial-payments]
---

## Overview

This Adyen guide, last modified 2022-05-10 and captured 2026-09-15, adds Titres-Restaurant to an **existing Web Components integration**. It covers issuer selection, a balance-dependent split-payment path, and different `/sessions` versus `/payments` Component callbacks. It is historical implementation guidance, not proof of current issuer or merchant eligibility, live activation, or payment completion. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Setup and version gates:** The base Web Components integration requires version **5.4.0 or later**. Before integration, activate Titres-Restaurant to obtain a `Carte de domiciliation CONECS`, then add the meal-voucher method in Customer Area with SIRET and Conecs MID. The `/sessions` tab states support from Components **v5.18.0**; its own-Pay-button variant states **v5.21.0**. The general API-reference line calls `/sessions` the default from v5.0.0, which is broader than these method-specific tab gates; use the tab's stated minimum for its features. The `/payments` tab covers an additional use case or integrations before v5.18.0 (raw lines 21–42, 66–68, 150–152, 250–252).
- **Issuer and Component choice:** Configure `mealVoucher_FR_natixis` for Bimpli, `mealVoucher_FR_sodexo` for Sodexo, or `mealVoucher_FR_groupeup` for Up Dejeuner; the page also says Apetiz and the Natixis type refer to Bimpli. Web Components v6 imports `MealVoucherFR` and creates it with `new MealVoucherFR(checkout, configuration)`; the v5.x path uses `checkout.create(...)`, within the overall v5.4.0 minimum. Mount after `isAvailable()` confirms availability. The v6 import link on this Components page points to a **Drop-in** integration route, so follow the Components integration context when resolving imports (raw lines 29–35, 44–52, 114–147).
- **Sessions balance path:** No additional Titres-Restaurant request fields are specified. The ordinary `/sessions` path requires `onOrderCreated(orderStatus)` when the voucher balance is below the transaction; `orderStatus.remainingAmount` can drive another payment Component for the balance. With a merchant-owned Pay button, call `balanceCheck()`; if the balance covers the full amount, the shopper must confirm via `onRequiringConfirmation` before `submit()`. This variant has its own v5.21.0 gate (raw lines 37–42, 66–93, 150–168).
- **`/payments` and optional partial payments:** The `/payments` tab requires `onBalanceCheck` to call `/paymentMethods/balance`. For partial payments, optional `onOrderRequest` creates an order for the total amount when balance is low, and `onOrderCancel` cancels it. The page says no payment is made when the balance is insufficient; after the order is created, use `/payments` **outside the Component** with the order data to make partial payments and complete the order. Do not treat order creation or the example `resultCode: Success` as final payment completion (raw lines 250–271, 332–360).
- **Test and live:** Test credentials must come directly from Bimpli, Sodexo, or Up Déjeuner. Before live acceptance, contact Adyen Support to activate Titres-Restaurant in the live environment (raw lines 362–366). The examples show EUR order amounts, not a complete eligibility or currency matrix.

## Detail locators

- Requirements, account setup, v6 import route and issuer identifiers: pinned raw lines 21–52.
- Sessions event, order-status example, versioned Component creation and availability check: lines 66–147.
- Own Pay button, balance check, confirmation and versioned Component setup: lines 150–248.
- `/payments` balance/order callbacks, optional partial payments and outside-Component payment: lines 250–360.
- Test issuer credentials and live Support activation: lines 362–366.

## Related

- [[source-adyen-docs-payment-methods-titres-restaurant]] — method overview for separate regional and capability context
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/titres-restaurant/web-component/2026-09-15|Titres-Restaurant Web Component guide, captured 2026-09-15]]
