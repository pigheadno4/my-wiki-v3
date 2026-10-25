---
title: "Adyen Rakuten Pay React Native Component guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/rakutenpay/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/rakutenpay/react-native-component/2026-09-15.md"
tags: [adyen, rakuten-pay, react-native, components, redirect, online-payments]
---

## Overview

This 2026-09-15 Adyen page gives **Rakuten Pay-specific additions** for React Native Components. It explicitly says **Sessions flow is unsupported** for React Native Components on this page, then covers an existing Advanced-flow Components integration, redirect handling, conditional recurring-model guidance and a DGFT TEST simulator. It is not proof of merchant recurring approval or a successful live payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Flow boundary:** Under “Sessions flow Component,” the guide says React Native Components **do not support Sessions flow**. Do not borrow Sessions prerequisites or behavior from React Native Drop-in or another platform for this Component guide. The usable integration route described here is **Advanced flow Component**. (raw lines 23–31)
- **Advanced prerequisites and ordinary additions:** The page calls for an existing Advanced React Native Components integration, redirect handling for **`action.type: redirect`**, and Rakuten Pay added in Customer Area. It says no extra Rakuten Pay configuration or ordinary `/payments` fields are needed. Its Integration type link, however, points to **React Native Drop-in**, while its redirect/payment links point to Components; resolve the base route against the actual Advanced Components guide. This page does not state an API or SDK minimum version. (raw lines 31–53)
- **Recurring restrictions:** For subscription and unscheduled card-on-file business models, the page says Rakuten Pay permits **one-off card-on-file transactions only after review**. Without periodic charging cadence, it prohibits initiating the card-on-file Recurring Processing Model, described as primarily allowed in Food & Beverage. The merchant must **apply for every Recurring Processing Model** when requesting Rakuten Pay. It routes token implementation elsewhere and **strongly recommends**, rather than mandates in this wording, explicit shopper permission for future charges. The no-extra ordinary `/payments` statement is not blanket recurring authorization. (raw lines 49–61)
- **TEST versus live:** The guide names `DGFT_AcquirerAccount_RakutenPay_closedLoop` for TEST, directs the shopper to a DGFT simulator without requiring the Rakuten Pay app, and points to Customer Area status checks. Despite the “Test and go live” heading, it gives no separate live enablement procedure or final result/webhook semantics. Simulator completion and status navigation do not prove actual authorization or settlement. (raw lines 63–69)

## Detail locators

- Explicit Sessions-flow unavailability and Advanced-only section: raw lines 23–35.
- Components/Drop-in prerequisite URL conflict, redirect setup and Customer Area gate: raw lines 37–41.
- No extra ordinary configuration/payment fields: raw lines 43–53.
- Recurring review/cadence/category/per-model application and permission recommendation: raw lines 55–61.
- DGFT TEST simulator/status route: raw lines 63–69.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-rakutenpay]]
- [[source-adyen-docs-payment-methods-rakutenpay-react-native-drop-in]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/rakutenpay/react-native-component/2026-09-15|Adyen Rakuten Pay React Native Component, 2026-09-15 snapshot]]
