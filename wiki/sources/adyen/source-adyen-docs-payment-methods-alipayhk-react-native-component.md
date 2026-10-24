---
title: "Adyen Alipay HK React Native Component"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipayhk/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/alipayhk/react-native-component/2026-09-15.md"
tags: [adyen, alipayhk, react-native, components, online-payments]
---

## Overview

This [[adyen]] page, modified and captured 2026-09-15, describes adding Alipay HK to **React Native Components** with an existing Advanced flow. Its raw title says “React Component,” but the URL and requirement body identify **React Native**; do not route it as a generic Web React component. It explicitly says React Native Components do **not** support Sessions flow in this snapshot. See [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-alipayhk|Alipay HK overview]] for separate HK/HKD scope. These setup statements do not prove current SDK support, live eligibility, completed redirect, authorization, capture or settlement. See primary raw lines 15–41 and 55–65.

## Key takeaways

- The Sessions section is labeled **Not Available** and says React Native Components do not support Sessions flow. The Advanced branch requires an existing React Native Components integration, `action.type: redirect` handling and Alipay HK added in Customer Area. No Checkout API or React Native SDK minimum version is stated here. See raw lines 23–41.
- The Advanced integration-type row **says Components but links to `integration=Drop-in`**; its redirect and `/payments` links use `integration=Components`. Keep the written Components scope primary, and use the correctly scoped main-flow references for implementation. This page gives no React Native wrapper implementation details beyond those links. See raw lines 37–53.
- The page says there are no *additional Alipay HK-specific* configuration parameters or `/payments` parameters. The existing Advanced integration still owns its base request, client redirect/return and payment-state handling; no-extra-method-fields is not a completed request. See raw lines 43–53.
- TEST instructions publish credentials and point to TEST Customer Area's payment list. Before live acceptance, the page says to submit an AlipayHK request in live Customer Area. It does not show credential use, a returned action, `/payments/details`, final webhook or any successful payment. See raw lines 55–65.

## Detail locators

- **Explicit Sessions unavailability and Advanced prerequisites:** raw lines 23–41.
- **Components-versus-Drop-in requirement URL, redirect and no-extra-parameter sections:** raw lines 37–53.
- **Published TEST credentials, status route and live request:** raw lines 55–65.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-alipayhk]]
- [[adyen-payment-testing]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipayhk/react-native-component/2026-09-15|Alipay HK React Native Component — captured 2026-09-15]]
