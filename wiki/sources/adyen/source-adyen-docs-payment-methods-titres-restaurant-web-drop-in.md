---
title: "Adyen Titres-restaurant Web Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/titres-restaurant/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/titres-restaurant/web-drop-in/2026-09-15.md"
tags: [adyen, titres-restaurant, web, drop-in, meal-vouchers, partial-payments]
---

## Overview

This 2026-09-15-captured Adyen page adds French Titres-restaurant meal vouchers to an **existing Web Drop-in** integration. It distinguishes the default `/sessions` route from a `/payments` additional use case that needs balance and order callbacks. This is method-specific guidance, not a complete base integration or proof of current issuer/merchant enablement or live payment. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-titres-restaurant|the method overview]] for issuer, channel, activation, and historical usage qualifications.

## Key takeaways

- **Prerequisites and version:** The page requires an existing Web Drop-in integration at **version 5.4.0 or later**. Before setup, activate Titres-Restaurant to obtain the `Carte de domiciliation CONECS`, then add the meal voucher method in Customer Area with the merchant's SIRET and Conecs MID. For Web Drop-in v6, import `AdyenCheckout` and `MealVoucherFR` from `@adyen/adyen-web` (pinned raw lines 21–35).
- **Endpoint split:** The guide says no additional Titres-Restaurant request fields are needed. It identifies `/sessions` as the default with Drop-in v5.0.0 or later and `/payments` for an additional use case. The `/sessions` tab says there is no method-specific Drop-in configuration; the `/payments` tab instead marks the three callbacks below as required. Do not read the no-extra-fields statement as removing the `/payments` callback requirement (lines 37–66).
- **`/payments` callbacks:** `onBalanceCheck(resolve, reject, data)` calls `/paymentMethods/balance` when the shopper pays with Titres-Restaurant. If card balance is below the transaction amount, `onOrderRequest(resolve, reject, data)` calls `/orders` with the **total transaction amount**. On shopper cancellation, `onOrderCancel(order)` calls `/orders/cancel`. The examples assign one `mealVoucherConfiguration` to `mealVoucher_FR_natixis`, `mealVoucher_FR_sodexo`, and `mealVoucher_FR_groupeup`; the page says Apetiz and the Natixis key refer to Bimpli (lines 58–104).
- **Test and live:** Get test credentials **directly from the meal voucher issuer** (Bimpli, Sodexo, or Up Déjeuner). Before accepting live payments, contact Adyen Support to activate Titres-restaurant in the live environment. The captured Support hyperlink points to a test Customer Area URL, so verify the appropriate live-support route rather than treating that link as proof of live activation (lines 106–110).

> [!warning] Configuration examples are illustrative
> The fenced blocks at raw lines 72–102 are labeled `json` but contain JavaScript-style functions/comments, placeholder response names, and missing commas between callback entries and issuer keys. They show the callback and issuer-key arrangement, not a copy-ready configuration object. The method overview has separate issuer-contract and historical usage qualifications; follow it for those claims rather than inferring universal voucher acceptance from this page.

## Detail locators

- Existing Drop-in, minimum version and CONECS/SIRET setup: pinned raw lines 19–27.
- Web v6 import and API endpoint split: lines 29–42.
- Sessions versus additional-use-case `/payments` configuration: lines 44–66.
- Callback and issuer-key examples, including Bimpli naming: lines 68–104.
- Issuer-provided test credentials and live Support step: lines 106–110.

## Related

- [[adyen-online-payments]] — provider integration concept
- [[source-adyen-docs-payment-methods-titres-restaurant]] — meal-voucher overview and activation context

## Raw Sources

- [[raw/adyen/docs/payment-methods/titres-restaurant/web-drop-in/2026-09-15|Titres-restaurant Web Drop-in guide, captured 2026-09-15]]
