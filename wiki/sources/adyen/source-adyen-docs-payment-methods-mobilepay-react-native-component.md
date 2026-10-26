---
title: "MobilePay React Native Component"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/mobilepay/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/mobilepay/react-native-component/2026-09-15.md"
tags: [adyen, mobilepay, react-native, components, online-payments, payouts]
---

## Overview

This 2026-09-15 Adyen method guide, headed “MobilePay React Component” at a React Native Components URL, describes adding MobilePay to an existing React Native Components integration. It expressly excludes Sessions flow for this method and documents only an Advanced redirect flow. A separate section covers an experimental token-generation path for future MobilePay-wallet payouts. It is a historical documentation snapshot, not proof of current enablement or executed payments or transfers. See [[adyen]], [[adyen-online-payments]], [[adyen-react-native-sdk]], and [[adyen-payouts]].

## Key takeaways

- The Sessions section says React Native Components do not support Sessions flow for MobilePay (raw lines 25–29). The Advanced section requires an existing React Native Components Advanced integration, redirect handling for `action.type: redirect`, and MobilePay addition in Customer Area (lines 31–41). This method-specific exclusion should not be generalized to all React Native Components or interpreted as a universal SDK limitation.
- The guide says no extra MobilePay Component configuration and no extra `/payments` parameters for an ordinary payment. The latter has an exception for a payment that creates a future payout token (lines 43–53).
- For that payout path, the guide says to set up a recurring lifecycle webhook, include `telephoneNumber`, `shopperReference` and a true payout flag in `/payments`, save webhook `storedPaymentMethodId` for the shopper, and pass that token as `counterparty.card.cardIdentification` in POST `/transfers` (lines 239–271). The page labels the payout feature experimental and limits token creation to `/payments` (lines 285–287). A token or submitted transfer request is not evidence of payout completion.
- For ordinary MobilePay payments, the page says Adyen TEST cannot be used; it directs low-amount LIVE payments after a live Customer Area request, checking the AUTHORISATION webhook and Payment list status (lines 273–283). Its separate payout-test section describes a Vipps MobilePay test app, simulated payment, token webhook and Transfers API request (lines 285–306). Do not merge those distinct test scopes.
- Source conflicts and example limits: the payout-flag prose spells `enablePayout` (line 249), while the annotated curl example spells `enablePayOut` (line 74). The prerequisite labels a React Native Components integration but links to `integration=Drop-in` (line 39). The example uses a TEST endpoint plus blank currency, payment-method type and return URL (lines 55–76) although ordinary-payment testing is directed to LIVE; it is not a ready-to-run request. The guide's page title says “React Component” while its canonical path and prerequisites say React Native (lines 6–10, 15, 39).

## Detail locators

- Sessions exclusion and Advanced prerequisites: raw lines 25–41.
- Standard Advanced configuration and `/payments` exception: raw lines 43–53.
- Language-specific `/payments` examples and placeholders: raw lines 55–237. Their Node and other library version comments do not establish a React Native SDK version or combined compatibility.
- Payout-token request, webhook example and Transfers API handoff: raw lines 239–271. The webhook payload is illustrative, not an observed event.
- Ordinary LIVE payment testing and separate experimental payout-app test: raw lines 273–306. Phone and NIN fixtures remain in the raw.

## Related

- [[adyen-online-payments]]
- [[adyen-react-native-sdk]]
- [[adyen-payouts]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/mobilepay/react-native-component/2026-09-15|MobilePay React Native Component, fetched 2026-09-15]]
