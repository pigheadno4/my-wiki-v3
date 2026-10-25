---
title: "Bank Transfer via KCP for Android"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bank-transfer-kcp/android"
raw_files:
  - "adyen/docs/payment-methods/bank-transfer-kcp/android/2026-09-15.md"
tags: [adyen, kcp, bank-transfer, android, navigation, online-payments]
---

## Overview

This 2026-09-15 Bank Transfer via KCP Android page is an integration chooser. It links Android Drop-in and Components method guides and the main Sessions and Advanced integration guides. It does not itself supply method setup or transaction-result evidence. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Method-guide choices:** the page presents Android Drop-in as an all-in-one UI route and Android Components as an `InstantPaymentComponent` route to handle the redirect to KCP bank transfer. This is a navigation label; the child guide governs exact action types, SDK/API versions, request fields and redirect outcome handling. (raw lines 19–27)
- **Main integration first:** the page instructs merchants to create their main integration before adding KCP bank transfer, linking Android Drop-in and Components with Sessions and Advanced flows. The four links are navigation and do not make every child combination equivalent. (raw lines 29–36)
- **Evidence limit:** this chooser contains no country/currency, merchant entity or bank-eligibility rule, test/live credential or certificate procedure, shopper authentication, final webhook, authorization, capture or settlement result. These require the selected child and base guides. (raw lines 15–36)

## Detail locators

- Android method-choice labels and child routes: raw lines 19–27.
- Main Sessions and Advanced Android guide links: raw lines 29–36.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-bank-transfer-kcp-android-drop-in|KCP bank-transfer Android Drop-in child]]
- [[source-adyen-docs-payment-methods-bank-transfer-kcp-android-component|KCP bank-transfer Android Components child]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/bank-transfer-kcp/android/2026-09-15|Adyen KCP bank-transfer Android chooser, 2026-09-15 snapshot]]
