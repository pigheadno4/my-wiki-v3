---
title: "Adyen Online banking Czech Republic React Native Drop-in"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-czech-republic/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/online-banking-czech-republic/react-native-drop-in/2026-09-15.md"
tags: [adyen, online-banking-czech-republic, react-native, drop-in, redirect]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Online banking Czech Republic** to an existing React Native Drop-in integration. It describes Sessions and Advanced prerequisites, no method-specific request/configuration additions, and test/live guidance. It is a short method add-on, not a full React Native integration or proof of current merchant enablement. See [[adyen]], [[adyen-online-payments]], and the separate CZ/CZK overview [[source-adyen-docs-payment-methods-online-banking-czech-republic]].

## Key takeaways

- **Sessions:** the page assumes an existing React Native Drop-in Sessions flow, **Checkout API v68 or later**, redirect handling for `action.type: redirect`, and the method added in Customer Area. It says no additional parameters are needed when creating the payment session and no additional method configuration parameters. These are method-specific additions, not a claim that the base `/sessions` request is empty. See raw lines 25–48.
- **Sessions navigation warning:** the integration-type row is labeled Sessions but links to an **Advanced-flow** React Native Drop-in base guide (raw line 33); the redirect and create-session links point to **Sessions-flow** guides (lines 35 and 42). Keep the flow identity and use the verified Sessions routes rather than selecting the base guide solely from the first link.
- **Advanced:** the page assumes an existing React Native Drop-in Advanced flow, redirect handling, and method setup in Customer Area. It says no additional method configuration parameters and no additional parameters for `/payments` in this Drop-in guide. The v68 minimum is stated only in the Sessions requirements on this page. See raw lines 58–80.
- The separate API-only guide describes merchant-side bank issuer selection and example `paymentMethod.type`/`issuer` fields. This Drop-in add-on's no-additional-parameters statement does not override the API-only flow or establish a universal API schema rule. The linked overview supplies CZ/CZK redirect context; this page has no request samples establishing currency or final authorisation. See raw lines 38–48 and 76–80, plus [[source-adyen-docs-payment-methods-online-banking-czech-republic-api-only]].
- For both flows, the page says to test with **real payment details and small amounts**, check test-payment status in Customer Area > Payments > Payment list, and add the method in Customer Area to accept live payments. These are instructions in the captured guide, not evidence that a payment ran or a merchant is enabled. See raw lines 50–56 and 82–88.

## Detail locators

- Sessions prerequisites and mismatched base-guide link targets: raw lines 25–36.
- Sessions no-additional-parameters/configuration statements: raw lines 38–48.
- Sessions test and live guidance: raw lines 50–56.
- Advanced prerequisites and no-additional-configuration/payment-parameter statements: raw lines 58–80.
- Repeated test and live guidance: raw lines 82–88.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-czech-republic]]
- [[source-adyen-docs-payment-methods-online-banking-czech-republic-api-only]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-czech-republic/react-native-drop-in/2026-09-15|Fully read Online banking Czech Republic React Native Drop-in raw]]
