---
title: "Alipay React Native Drop-in"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipay/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/alipay/react-native-drop-in/2026-09-15.md"
tags: [adyen, alipay, react-native, drop-in, redirect]
---

## Overview

This 2026-09-15 Adyen guide gives Alipay-specific additions to an **existing React Native Drop-in integration**, split between Sessions and Advanced server-side flows. Base integration and redirect handling are delegated to linked main guides. The page describes preparation, not a completed wallet payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions:** requires an existing React Native Drop-in Sessions flow, **Checkout API v68 or later**, redirect handling for `action.type: redirect`, and Alipay added in Customer Area. It states no additional **Alipay-specific** `/sessions` parameters or configuration parameters are needed. The Sessions integration-type row links to an **advanced-flow** URL even though its label says Sessions; use the flow-specific Sessions redirect/session links and main guide with care. (raw lines 25–48)
- **Advanced:** requires an existing React Native Drop-in Advanced flow, redirect handling for `action.type: redirect`, and Alipay added in Customer Area. It states no additional Alipay-specific configuration or `/payments` parameters are needed. Its section does **not** state a Checkout API minimum; the v68 statement is in Sessions only. (raw lines 60–82)
- Both flow sections **recommend** live penny tests with an Alipay wallet app and viewing payment details in the **live Customer Area**. Separately, the guide says a request for Alipay must be submitted in the live Customer Area before live acceptance. Recommendation and request submission are distinct from method approval, actual authorization, capture or settlement. (raw lines 50–58, 84–92)
- The page supplies no React Native Drop-in code or result/webhook procedure for Alipay; a redirect action and test-payment-list instructions do not themselves establish the shopper's return or final payment status. (raw lines 25–92)

## Detail locators

- Sessions requirements and anomalous main-guide link: raw lines 25–36.
- Sessions no-extra request/configuration statements: raw lines 38–48.
- Advanced requirements and no-extra request/configuration statements: raw lines 60–82.
- Live test recommendation and live request gate: raw lines 50–58 and 84–92.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-alipay]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipay/react-native-drop-in/2026-09-15|Adyen Alipay React Native Drop-in, 2026-09-15 snapshot]]
