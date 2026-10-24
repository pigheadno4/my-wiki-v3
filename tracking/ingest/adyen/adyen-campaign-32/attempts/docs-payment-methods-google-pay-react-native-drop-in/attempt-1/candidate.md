---
title: "Adyen Google Pay React Native Drop-in add-on"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/google-pay/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/google-pay/react-native-drop-in/2026-09-15.md"
tags: [adyen, google-pay, react-native, drop-in, wallets]
---

## Overview

This [[adyen]] page adds **Google Pay** to an **existing React Native Drop-in integration**. It says Drop-in opens the Google Pay sheet and handles a redirect for a selected card requiring 3D Secure verification. It requires the separate Google Pay setup steps and adding Google Pay in Adyen Customer Area. The guide does not pin a React Native wrapper version, native SDK version, or Checkout API minimum, and its add-on text is not a complete client/server payment or final-outcome flow. [[adyen-react-native-sdk]]

## Key takeaways

- The page says no additional **Google-Pay-specific** `/payments` fields or required Drop-in configuration are needed beyond the existing integration. Optional `AdyenCheckout` settings cover allowed networks/auth methods, price status, card types, billing/shipping/email collection and button availability. Its `PAN_ONLY` and `CRYPTOGRAM_3DS` descriptions are Google Pay card/auth-method options, not proof of 3DS completion or a settled payment. See raw lines 23–59.
- The optional table calls `merchantAccount` **“Your Google Merchant ID”**, with a default from the `brands` array of `/paymentMethods`, and says to obtain a Google Merchant ID before live use. That wording needs verification against the applicable React Native SDK configuration because it is easy to confuse a Google Merchant ID with an Adyen merchant account. See raw line 45 and the separate live checklist at raw lines 92–103.
- The `googlePayEnvironment` row says the value can be `WalletConstants.ENVIRONMENT_TEST` **for both test and live**, an internal contradiction; its stated default follows the `AdyenCheckout` environment. Do not use the repeated TEST constant as production configuration guidance without the version-matched Google Pay/SDK reference. See raw line 57.
- Recurring payments are only **routed** to separate token-creation and token-payment guides: the page gives no shopper-consent, token payload, or later-charge result procedure. Drop-in showing a Google Pay sheet or handling a 3DS redirect does not establish payment authorization, capture, or settlement. See raw lines 19–21 and 61–64. [[adyen-tokenization]]
- TEST instructions distinguish Google's test-card suite (FPAN, Android/Chrome-on-Android DPAN and 3DS2 scenarios) from real wallet cards mapped to Adyen test cards; for 3DS2 without the suite, it specifies American Express or Discover. The page says a real card is not charged by that mapped test route. LIVE calls for the **API Clientside Encryption Payments role**, Google Merchant ID configuration, Google's Android production-deployment steps, and a logged-in shopper with a valid Google Pay method. These are source-stated setup/availability gates, not evidence of actual merchant enablement or a completed live payment. See raw lines 66–103.
- The guide is labeled React Native but several optional-property links point to **Google Pay Web** request-object references while TEST/LIVE links point to **Android** documentation. Preserve these as linked references, not an assertion that every native platform or wrapper version exposes identical fields. See raw lines 43–59 and 66–103.

## Detail locators

- Existing Drop-in and provider/Customer Area prerequisites: raw lines 17–29.
- API note and full optional `AdyenCheckout` table: raw lines 31–59.
- Recurring navigation and TEST/LIVE checklist: raw lines 61–103.

## Related

- [[adyen-react-native-sdk]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/google-pay/react-native-drop-in/2026-09-15|Adyen Google Pay React Native Drop-in snapshot]]
