---
title: "Online banking Thailand React Native Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-thailand/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/online-banking-thailand/react-native-component/2026-09-15.md"
tags: [adyen, online-banking-thailand, react-native, components, redirect, online-payments]
---

## Overview

This 2026-09-15-captured guide describes Online Banking Thailand additions to an existing **React Native Components** integration. It explicitly excludes Sessions flow and covers only the Advanced-flow redirect add-on. It is a setup reference, not evidence of current eligibility, a completed redirect, authorization or settlement. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Flow boundary:** the Sessions section states that React Native Components do **not** support Sessions flow. The Advanced section requires an existing React Native Components Advanced integration, redirect handling for `action.type: redirect`, and the payment method added in Customer Area. It gives no Checkout API or SDK version floor on this page. (raw lines 23–41)
- **Method-specific additions:** the page says no extra configuration parameters for Online Banking Thailand and no additional parameters to `/payments` when following the linked Advanced payment step. This does not remove the base integration's ordinary payment-request requirements. (raw lines 43–53)
- **Base-link mismatch:** the Advanced integration-type row labels **React Native Components** but its URL sets `integration=Drop-in`; the redirect and payment links set `integration=Components`. Retain the row's conflict rather than treating the Drop-in URL as evidence for Component behavior. (raw lines 37–40, 51–53)
- **Test and live boundary:** the page says to use issuer IDs available for the relevant country/region, inspect test payments in test Customer Area, and submit a separate request in **live Customer Area** before accepting live payments. It does not list issuer IDs or show an observed test or live result. (raw lines 55–61)

## Detail locators

- Sessions unsupported and Advanced prerequisites: raw lines 23–41.
- No method-specific configuration or payments parameters; mislabeled integration URL: raw lines 37–53.
- Issuer-ID test guidance and separate live request: raw lines 55–61.

## Related

- [[adyen]]
- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-thailand/react-native-component/2026-09-15|Adyen Thailand online banking React Native Component guide, 2026-09-15 snapshot]]
