---
title: "Adyen Titres-restaurant API-only integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/titres-restaurant/api-only"
raw_files:
  - "adyen/docs/payment-methods/titres-restaurant/api-only/2026-09-15.md"
tags: [adyen, titres-restaurant, meal-vouchers, france, api-only, balance-check, partial-payments]
---

## Overview

This [[adyen|Adyen]] page, fetched 2026-09-15 and marked **last modified 2022-12-20**, adds French Titres-restaurant payments to an existing **Web API-only** integration. The merchant builds a payment form, checks meal-voucher balance, optionally uses an order for split tender, sends `/payments`, and handles result/webhook outcomes. See [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-titres-restaurant|method overview]]. The old examples do not prove current issuer/account eligibility, credential safety or payment execution.

## Key takeaways

- **Activation and channel:** Begin with an API-only integration. The page directs merchants to activate Titres-restaurant for a *Carte de domiciliation CONECS*, then add the meal-voucher method in Customer Area with the merchant's **SIRET** and **Conecs MID**. The overview separately says issuer contracts are needed; this page's test credentials must come directly from Bimpli, Sodexo or Up Déjeuner. Live activation requires Adyen Support. Do not infer that Customer Area configuration alone replaces issuer authorization/contracts.
- **Discovery and issuer names:** If using `/paymentMethods`, request **FR/EUR** and display the available brands. Its example lists `mealVoucher_FR_groupeup` (Up), `mealVoucher_FR_natixis` (Apetiz/Bimpli, commercial brand of Natixis), and `mealVoucher_FR_sodexo` (Sodexo). These are illustrative issuer-branded discovery types, not a promise that all are available for every shopper. The displayed “API response” is malformed JSON with a double opening brace and no `paymentMethods` wrapper; use the stated response structure rather than copy it literally.
- **Balance and split tender:** After collecting meal-voucher details, use `/paymentMethods/balance` with generic `paymentMethod.type: mealVoucher_FR`, card number, expiry month/year and a unique reference; the example includes merchant account. The example balance response has EUR 25.00 and `resultCode: Success`, a balance-check result, not a payment authorization. If balance covers the full amount, continue to payment. If it is insufficient, **create an order** and ask for partial payments using the voucher and another method. This is split tender through an order, not partial capture of one voucher payment.
- **Payment and outcome:** From the server, `/payments` requires generic type `mealVoucher_FR`, voucher number without separators, expiry month/year and **CVC**. The `/payments` response has PSP reference, result code and merchant reference; present the result to the shopper and expect the outcome asynchronously by webhook. The page lists `Authorised`, `Cancelled`, `Error` and `Refused`; `Authorised` is successful authorization and, if manual capture is used, the payment still needs capture. Handle card number/CVC through the applicable secure base integration; this source gives no standalone card-data security or PCI procedure.
- **Historical sample boundary:** The balance example uses TEST Checkout v72 and expiry year 2023; the payment example uses TEST Checkout v68 and the same historical expiry year. Treat these as old illustrative values, not runnable test credentials or current API guidance. The separate method overview's feature matrix marks separate capture supported but partial capture and refunds unsupported; do not confuse those marks with this page's order-based partial payments.

## Detail locators

- API-only purpose and activation with SIRET/Conecs MID: pinned raw lines 15–27. FR/EUR discovery, issuer-brand sample and Bimpli naming: lines 29–59.
- Balance request fields and historical TEST examples: lines 61–355. Sufficient versus insufficient balance/order branch: lines 357–359.
- Server `/payments` required voucher credentials and TEST v68 examples: lines 361–484. Payment result, asynchronous webhook and result codes: lines 486–503. Issuer test credentials and Support live activation: lines 505–515.

## Related

- [[adyen-online-payments]] — provider integration concept
- [[source-adyen-docs-payment-methods-titres-restaurant]] — issuer and feature overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/titres-restaurant/api-only/2026-09-15|Titres-restaurant API-only guide, fetched 2026-09-15]]
