---
title: "Adyen PayPay React Native Component"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypay/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/paypay/react-native-component/2026-09-15.md"
tags: [adyen, paypay, react-native, components, redirect]
---

## Overview

This 2026-09-15 PayPay method add-on has a `react-native-component` URL but a captured title of **PayPay React Component**. It explicitly says **React Native Components do not support Sessions flow**, then gives only an Advanced-flow Components path. The existing integration and Adyen Customer Area PayPay setup remain prerequisites; this method-specific page does not establish current SDK support, merchant availability or a successful payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Advanced only in this guide:** start with an existing React Native Components Advanced integration, configure redirect handling for `action.type: redirect`, and add PayPay in Adyen Customer Area. The Integration type row's label says Components but its URL points to `integration=Drop-in`; the redirect and payment-step URLs point to Components. Treat that as a link mismatch rather than converting this page into Drop-in guidance.
- No additional **PayPay-specific** client configuration or `/payments` request parameters are specified. This does not mean the base Advanced request, server processing, return handling or result verification can be omitted. The page gives no SDK, wrapper or Checkout API version gate and no detailed return/webhook or final authorization/capture/settlement steps.
- **TEST:** the page lists `DGFT_AcquirerAccount_Adyen_closedLoop_AUTHFlow` and `DGFT_AcquirerAccount_Adyen_closedLoop_SALEFlow` as test acquirer accounts. It says the shopper is redirected to a DGFT simulator and does not need the PayPay app; test transaction status can be inspected in Adyen TEST Customer Area. Simulator completion or a status-list entry is not live-payment proof.
- **LIVE:** the guide says an activated PayPay smartphone app must be accessed through a Japan local IP address. This is separate from TEST simulator behavior and does not prove present merchant/device eligibility or payment success.

## Detail locators

- URL/title metadata and add-on scope: raw lines 1–23. Sessions unsupported statement: raw lines 25–29. Advanced Components label, Drop-in URL mismatch, redirect and Customer Area setup: raw lines 31–41.
- No additional PayPay-specific configuration or payment parameters: raw lines 43–53. TEST acquirer/simulator/status and LIVE app/IP condition: raw lines 55–66.

## Related

- [[adyen-online-payments]] — parent payment-flow and outcome context.
- [[adyen-react-native-sdk]] — React Native wrapper and base integration context; its general architecture does not override this PayPay page's Sessions exclusion.
- [[source-adyen-docs-payment-methods-paypay-react-native-drop-in]] — distinct Drop-in route with Sessions and Advanced branches.

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypay/react-native-component/2026-09-15|PayPay React Native Component guide, captured 2026-09-15]]
