---
title: "Adyen Apple Pay React Native Drop-in add-on"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/apple-pay/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/apple-pay/react-native-drop-in/2026-09-15.md"
tags: [adyen, apple-pay, react-native, drop-in, recurring]
---

## Overview

This [[adyen]] guide adds **Apple Pay** to an existing **React Native Drop-in** integration, with separate Sessions (`/sessions`) and Advanced (`/payments`) prerequisite tabs. Both require Apple Pay set up with **the merchant's own iOS payment-processing certificate** and added in Adyen Customer Area; live processing additionally requires the **API Clientside Encryption Payments role**. It is a method-specific add-on and does not pin a React Native wrapper or native SDK version, describe full server payment handling, or prove payment outcome. [[adyen-react-native-sdk]]

## Key takeaways

- The guide says there are no extra **Apple-Pay-specific** API fields to send, but the `AdyenCheckout` configuration **must** provide `applepay.merchantID` (Apple Pay merchant identifier) and `merchantName` (used for the payment summary). The TEST example also contains client key, return URL, NL country and EUR amount; those sample values are not universal eligibility or a complete server request. See raw lines 21–75.
- Optional Apple Pay settings include wallet onboarding if no supported cards, summary items, billing/shipping contacts and methods, shipping type, supported issuing countries and recurring metadata. The page says the **last summary item must match the amount sent in `/payments`**; that wording appears on a page with both Sessions and Advanced tabs, and no Sessions-specific amount-alignment procedure is supplied here. A client summary alone does not prove the merchant server charged that amount. See raw lines 77–92.
- For recurring Apple Pay, the page requires `recurringPaymentRequest` in the Apple Pay configuration and separately routes token creation and later token payments to Adyen tokenization guides. Its table marks **`paymentDescription`**, **`regularBilling`** and **`managementURL`** required; `trialBilling`, Apple merchant-token `tokenNotificationURL`, and localized `billingAgreement` are listed as optional. The Apple Pay sheet displays the described billing information, but this page does not show token creation, actual shopper authorization, a billing schedule, or successful later charges. See raw lines 92–111. [[adyen-tokenization]]
- The recurring example conflicts with its table: it uses `description` instead of required `paymentDescription` and lacks a comma before `regularBilling`. Its `startDate` is an example literal and the snippet is not copy-ready. Keep the table's field name separate from the malformed sample. See raw lines 104–111 and 115–139.
- The test route uses Apple's sandbox card numbers and Adyen Customer Area test-payment status. LIVE separately requires the credential role and Apple Pay setup in the merchant's Apple Developer account for the live merchant identifier. Test-card use, configuration and wallet authorization are not evidence of final Adyen authorization, capture or settlement. See raw lines 141–153.

## Detail locators

- Sessions/Advanced prerequisites and own-certificate setup: raw lines 21–41.
- Required merchant identifier/name and TEST configuration example: raw lines 43–75.
- Optional contact/amount and recurring-property tables: raw lines 77–111.
- Conflicting recurring snippet and test/live routes: raw lines 115–153.

## Related

- [[adyen-react-native-sdk]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/apple-pay/react-native-drop-in/2026-09-15|Adyen Apple Pay React Native Drop-in snapshot]]
