---
title: "Multibanco React Native Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/multibanco/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/multibanco/react-native-component/2026-09-15.md"
tags: [adyen, multibanco, react-native, components, payments]
---

## Overview

This 2026-09-15 captured Adyen page describes Multibanco-specific additions for a **React Native Components Advanced flow** integration. The raw page title says “Multibanco React Component,” while its URL and body identify React Native Components. It is an add-on to the main integration, with a separate Multibanco overview at [[source-adyen-docs-payment-methods-multibanco]]. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions flow is unavailable:** the page explicitly says React Native Components do **not** support Sessions flow. Do not apply the React Native Drop-in Sessions guidance to this Component route. See raw lines 25–29.
- **Advanced flow:** requires an existing React Native Components Advanced integration, setup of Multibanco in Customer Area, and handling an additional `action.type: voucher`. The guide says no extra Multibanco-specific configuration or `/payments` parameters are needed; the base integration requirements still apply. See raw lines 31–53.
- Before testing, request Multibanco in the **test Customer Area**. A pending payment can be manually promoted to sale in **Payments → Offers** to simulate payment and test reconciliation; paid/promoted test offers appear in **Payment list**. This is a test simulation, not proof of shopper voucher redemption or live settlement. A separate request in the **live Customer Area** is required before live acceptance. See raw lines 55–70.

> [!warning] Base-guide navigation
> The Advanced requirement text says **React Native Components**, but its URL contains `integration=Drop-in` (raw line 39). The action-handling link uses `integration=Components` but a `#handle-the-redirect` anchor while the stated action type is `voucher` (line 40). The `/payments` step's link at line 53 uses `integration=Components`. Follow the stated Advanced Components flow and voucher action; these link labels do not establish redirect behavior.

## Detail locators

- Sessions unavailability: raw lines 25–29.
- Advanced requirements, no extra method configuration or request fields: raw lines 31–53.
- Test offer promotion and live request: raw lines 55–70.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-multibanco]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/multibanco/react-native-component/2026-09-15|Multibanco React Native Component, captured 2026-09-15]]
