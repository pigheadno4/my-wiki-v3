---
title: "Adyen FPX Online Banking Malaysia React Native Drop-in guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/fpx-online-banking-malaysia/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/fpx-online-banking-malaysia/react-native-drop-in/2026-09-15.md"
tags: [adyen, fpx, malaysia, react-native, drop-in, redirect]
---

## Overview

This 2026-09-15 Adyen page gives FPX Online Banking Malaysia-specific additions to an existing React Native Drop-in integration, split into Sessions and Advanced server-side flows. Both sections mention redirect handling and Customer Area method setup; neither reports an actual test or payment outcome. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Sessions requires an existing React Native Drop-in Sessions flow, Checkout API v68 or later, handling `action.type: redirect`, and adding FPX Online Banking Malaysia in Customer Area. Its prerequisite text says Sessions, but the linked integration URL points to an **Advanced** flow; retain that source mismatch. The page says no additional method-specific `/sessions` parameters or Drop-in configuration are needed.
- Advanced requires an existing React Native Drop-in Advanced flow, redirect handling, and Customer Area method addition. It says no additional method-specific configuration or `/payments` parameters are needed. No Advanced Checkout API minimum is stated on this page.
- For testing, both sections instruct using an issuer ID available for the “Online banking Malaysia Component” for the respective country/region, then checking test payment status in the test Customer Area. The page gives no issuer-ID list and uses **Component** wording inside this **Drop-in** guide; do not silently treat it as a Drop-in-specific ID source. Before accepting live payments, it says to submit an Online banking Malaysia request in the live Customer Area. None of those instructions proves test success or live approval.

## Detail locators

- Sessions requirements and mismatched prerequisite link: pinned raw lines 25–36; no additional `/sessions` parameters/configuration: lines 38–48; testing/live instructions: lines 50–56.
- Advanced requirements: lines 58–68; no additional configuration or `/payments` parameters: lines 70–80; repeated testing/live instructions: lines 82–88.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-fpx-online-banking-malaysia]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/fpx-online-banking-malaysia/react-native-drop-in/2026-09-15|FPX Online Banking Malaysia React Native Drop-in, 2026-09-15]]
