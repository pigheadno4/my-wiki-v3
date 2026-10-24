---
title: "Adyen Apple Pay React Native Component"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/apple-pay/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/apple-pay/react-native-component/2026-09-15.md"
tags: [adyen, apple-pay, react-native, components, online-payments]
---

## Overview

This 2026-09-15 Adyen page adds Apple Pay to an existing **Advanced-flow React Native Components** integration. It requires Apple Pay setup with the merchant's **own certificate** and Customer Area method addition, while linking the underlying iOS certificate instructions separately. It describes client Component configuration and says no Apple Pay-specific additional `/payments` fields are needed; it does **not** specify a merchant-side token-decryption flow or prove a payment result. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The integration prerequisite is Advanced React Native Components, with the merchant-owned Apple Pay certificate and Apple Pay method setup completed first. The **API Clientside Encryption Payments role** is specified for LIVE processing. The page does not state a React Native SDK or Checkout API minimum version. Its certificate link is to the separate iOS guide, not a set of certificate/key steps reproduced here. (raw lines 21–34, 157–161)
- The React Native `AdyenCheckout` configuration must add `applepay.merchantID` (Apple merchant identifier) and `merchantName` (used in a `PKPaymentSummaryItem`). The test example also carries `environment`, `clientKey`, `returnUrl`, `countryCode: NL`, and `amount: EUR 1000`; those country/amount values are illustrative, not a global acceptance list. A UI element can call `start('applepay')` using the Components wrapper. (raw lines 36–61, 81–100)
- Optional client configuration includes `allowOnboarding` (false by default, hiding Apple Pay when no wallet cards), contact/shipping fields, `shippingType`, `supportedCountries` as an **issuer-country card filter**, and `summaryItems`. The last summary item must equal the amount sent in server `/payments`; a payment-sheet display or shopper selection does not prove the server amount or authorization outcome. (raw lines 64–79)
- For recurring Apple Pay, the page says `recurringPaymentRequest` is required in configuration, followed by shopper-token creation and later token transactions. Its property table marks `paymentDescription`, `regularBilling` and `managementURL` required; trial billing, token lifecycle notification URL and a displayed billing agreement are optional in the table. The example instead uses `description` and lacks a comma after it; it is not an executable or authoritative required-property schema. A payment-sheet billing agreement is a displayed term, not proof of consent capture or a successful recurring charge. (raw lines 79, 102–147)
- TEST uses Apple's sandbox test cards and test Customer Area payment lookup. LIVE requires the credential role and Apple Pay setup for the **live merchant identifier** in the merchant's Apple Developer account. Test lookup, Component launch, wallet authorization and linked tokenization instructions do not establish actual live account readiness, payment authorization, capture or settlement. (raw lines 149–161)

## Detail locators

- Advanced wrapper prerequisites, certificate/Customer Area and no-extra-field API note: raw lines 21–34.
- Required client config and launch call: raw lines 36–61, 81–100.
- Optional wallet/contact/country and summary-amount settings: raw lines 64–79.
- Recurring properties and inconsistent example: raw lines 102–147.
- Sandbox versus LIVE role and identifier: raw lines 149–161.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-apple-pay-apple-pay-certificate-ios]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/apple-pay/react-native-component/2026-09-15|Adyen React Native Apple Pay Component guide, 2026-09-15 snapshot]]
