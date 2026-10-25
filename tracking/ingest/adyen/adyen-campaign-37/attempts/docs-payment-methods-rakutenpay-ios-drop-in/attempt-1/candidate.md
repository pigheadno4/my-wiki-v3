---
title: "Rakuten Pay iOS Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/rakutenpay/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/rakutenpay/ios-drop-in/2026-09-15.md"
tags: [adyen, rakuten-pay, ios, drop-in, recurring, online-payments]
---

## Overview

This 2026-09-15 guide adds Rakuten Pay to an existing Adyen iOS Drop-in integration through separate Sessions and Advanced server-side paths. It includes qualified card-on-file restrictions and a TEST simulator route; it does not show a completed live payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions path:** the page requires an existing iOS Drop-in Sessions integration with Checkout API v68 or later and Rakuten Pay added in Customer Area. It says no Rakuten-specific `/sessions` or Drop-in configuration parameters are needed. The Sessions requirement section does not itself specify an `action.type` prerequisite; its test section does describe redirect to a DGFT simulator. (raw lines 25–46, 58–66)
- **Advanced path:** the page requires an existing iOS Drop-in Advanced integration, redirect handling (`action.type: redirect`) and Customer Area setup. It says no extra Rakuten-specific Drop-in configuration or `/payments` parameters, and gives no Advanced Checkout API minimum or final redirect/webhook outcome procedure. (raw lines 68–90)
- **Restricted recurring use:** for subscription and unscheduled card-on-file business models, the page says one-off card-on-file transactions are permitted only after review. Without a periodic charging cadence, Rakuten Pay prohibits initiating a card-on-file Recurring Processing Model, which it says is primarily allowed for Food & Beverage. Merchants must apply for every model when requesting Rakuten Pay. The page links Adyen token creation and strongly recommends explicit shopper permission and transparency about schedule and amount; these links and recommendations do not establish an issued token, approved model or successful recurring payment. (raw lines 48–56, 92–100)
- **TEST and outcome limit:** it names `DGFT_AcquirerAccount_RakutenPay_closedLoop` for TEST and says the shopper is redirected to a DGFT simulator without needing the Rakuten Pay app. It identifies Customer Area Payment list for checking test transaction status. This is a test route, not evidence of production enablement, authorization, capture or settlement. (raw lines 58–66, 102–110)

## Detail locators

- Sessions prerequisites and no extra method parameters: raw lines 25–46.
- Advanced prerequisites, redirect and no extra method parameters: raw lines 68–90.
- Card-on-file review, cadence restriction, per-model application and shopper-permission recommendation: raw lines 48–56, 92–100.
- DGFT TEST account, simulator and status lookup: raw lines 58–66, 102–110.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/rakutenpay/ios-drop-in/2026-09-15|Adyen Rakuten Pay iOS Drop-in guide, 2026-09-15 snapshot]]
