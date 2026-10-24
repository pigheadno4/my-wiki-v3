---
title: "Adyen Alipay iOS Drop-in"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipay/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/alipay/ios-drop-in/2026-09-15.md"
tags: [adyen, alipay, ios, drop-in, online-payments]
---

## Overview

This 2026-09-15 Adyen page gives **Alipay-specific additions** for an existing **iOS Drop-in** integration. It separates Sessions and Advanced server-side flows and points to their main integration guides. It is a method add-on, not a full shopper return, webhook, authorization, capture or settlement procedure. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions:** The page requires an existing Sessions iOS Drop-in integration using **Checkout API v68 or later** and Alipay added in Customer Area. It says no Alipay-specific additional `/sessions` parameters or Drop-in configuration are needed. The Sessions table does **not** have a separate redirect-handling row; do not attribute the Advanced row to Sessions without its base guide. (raw lines 25–46)
- **Advanced:** The page requires an existing Advanced iOS Drop-in integration, `action.type: redirect` handling, and Customer Area method setup. It says no Alipay-specific extra configuration or `/payments` parameters are needed. No explicit Advanced API minimum or iOS SDK version appears in this page. (raw lines 60–82)
- In both sections, Adyen **recommends** live penny tests with an Alipay wallet app and card, then inspection in **live Customer Area**. These are suggested real live payments, not TEST-environment fixtures or proof any transaction occurred. The page separately says a **request for Alipay in live Customer Area** is needed before accepting live Alipay payments; request submission alone is not approval or processing evidence. No live test was performed for this ingestion. (raw lines 48–58, 84–94)
- The method-specific “no additional parameters/configuration” statements do not waive the base iOS Drop-in integration's own requirements. The page does not show a response, shopper return, webhook or final payment status, so it does not prove authorization, capture, settlement or refund. (raw lines 19–23, 36–46, 72–94)

## Detail locators

- Sessions prerequisites, `/sessions` and configuration: raw lines 25–46.
- Sessions recommended live penny tests and live method request: raw lines 48–58.
- Advanced prerequisites, redirect, `/payments` and configuration: raw lines 60–82.
- Advanced recommended live penny tests and live method request: raw lines 84–94.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipay/ios-drop-in/2026-09-15|Adyen Alipay iOS Drop-in guide, 2026-09-15 snapshot]]
