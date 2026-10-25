---
title: "Rakuten Pay React Native Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/rakutenpay/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/rakutenpay/react-native-drop-in/2026-09-15.md"
tags: [adyen, rakuten-pay, react-native, drop-in, recurring, online-payments]
---

## Overview

This 2026-09-15 guide adds Rakuten Pay to an existing React Native Drop-in integration, with separate Sessions and Advanced server-side flow sections. Both describe redirect handling and qualified recurring use. It is method-specific documentation, not evidence of a completed payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions path:** the page requires an existing React Native Drop-in Sessions integration, Checkout API v68 or later, redirect handling (`action.type: redirect`) and Rakuten Pay added in Customer Area. It says no Rakuten-specific `/sessions` request or Drop-in configuration parameters. The Sessions integration requirement links to an **Advanced** flow URL, while its heading, redirect link and request link identify Sessions; this source-link mismatch remains unresolved. (raw lines 25–48)
- **Advanced path:** requires an existing React Native Drop-in Advanced integration, redirect handling and Customer Area setup. The page says no additional Rakuten Pay Drop-in configuration or `/payments` parameters. It does not give an Advanced Checkout API minimum or a full redirect-return/outcome sequence. (raw lines 66–88)
- **Restricted recurring route:** for subscription and unscheduled card-on-file business models, the page says Rakuten Pay permits one-off card-on-file transactions only after review. Without a periodic charging cadence, it prohibits initiating the Recurring Processing Model for card-on-file; it says that model is primarily allowed for Food & Beverage. Merchants must apply for every Recurring Processing Model when requesting Rakuten Pay. It links Adyen token creation and strongly recommends explicit shopper permission and transparent schedule/amount; that recommendation is not phrased as a mandatory page requirement. The source does not show token request fields, token issuance or a successful recurring payment. (raw lines 50–56, 90–96)
- **TEST scope:** the page names TEST acquirer account `DGFT_AcquirerAccount_RakutenPay_closedLoop` and a DGFT simulator redirect, saying the Rakuten Pay app is unnecessary for this test. It directs status checks to Customer Area Payment list. These test instructions do not establish LIVE enablement, actual payment authorization, capture or settlement. (raw lines 58–64, 98–104)

## Detail locators

- Sessions requirements, link mismatch and no extra method fields: raw lines 25–48.
- Advanced requirements and no extra configuration/payment fields: raw lines 66–88.
- Recurring review, prohibition, per-model application and consent recommendation: raw lines 50–56, 90–96.
- TEST account, simulator and status lookup: raw lines 58–64, 98–104.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/rakutenpay/react-native-drop-in/2026-09-15|Adyen Rakuten Pay React Native Drop-in guide, 2026-09-15 snapshot]]
