---
title: "Google Pay Drop-in integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/google-pay/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/google-pay/web-drop-in/2026-09-15.md"
tags: [adyen, google-pay, web-drop-in, wallets, checkout]
---

## Overview

This 2023-modified, 2026-09-15-captured [[adyen]] guide adds Google Pay to an **existing Web Drop-in** integration, routed through [[adyen-online-payments]]. It describes the Google Pay sheet, a possible Drop-in redirect for card 3D Secure verification, versioned Sessions/Payments configuration, optional wallet UI settings, testing and live prerequisites. Opening or approving the wallet sheet does not prove authorization, capture or settlement.

## Key takeaways

- Requirements are an existing Web Drop-in integration, Google's Google Pay Web setup steps, and adding Google Pay in Adyen Customer Area. The page says **no additional Google Pay API request fields** are needed; `/sessions` is the default at Drop-in **v5.0.0+**, while `/payments` is for an additional use case. For `/sessions`, it says no extra Google Pay configuration is needed. This does not prove the method is configured for any particular merchant or live shopper.
- On the `/payments` branch, the table marks minor-unit `amount.value`, `amount.currency`, **merchant-account** `countryCode` and `environment` required, with environment default **test** and **production** for live. `authenticationData.threeDSRequestData.nativeThreeDS: preferred` and `origin` are conditional when native 3DS2 applies. The later Google Pay transaction-info `countryCode` has a different meaning—the **acquiring-bank** country for EEA/other SCA-subject processing—so the two country fields must not be conflated. A Google Pay card may trigger a separate 3DS verification redirect; wallet approval is not completed authentication or payment.
- Preloading Google's `pay.js` is a recommendation. If Drop-in is inside an iframe, the page directs adding an `allow` attribute so Google Pay renders. `instantPaymentTypes` is a **Drop-in instance** option that moves the Google Pay button to the top; its `googlepay` value is said to be available from **v5.30.0**.
- Optional wallet configuration covers merchant display identity, button style, requested email/shipping data, allowed card authentication methods/networks, payment-method readiness, transaction display and events. Client configuration overrides corresponding backend Google Pay configuration. If merchant name is specified, Google Merchant ID and Adyen gateway merchant account ID are also required; a test Merchant ID may be arbitrary, whereas the live path requires a Google Merchant ID and production access. JWT use across multiple domains requires `merchantOrigin` and Google approval. The default `allowedAuthMethods` are `PAN_ONLY` and `CRYPTOGRAM_3DS`; the page does not assign token decryption or PCI responsibility here.
- The events table calls `onClick` before payment-sheet approval, `onChange`/`onSubmit` after approval with continuation/rejection callbacks and payment-request state, and `onAuthorized` after approval for Google's full response. The transaction-info row instead refers to an `onAuthorize` handler for Google's Authorize Payments feature. Those names differ in this snapshot; neither callback name should be treated as a final Adyen authorization result. Dynamic Price Updates is marked express-checkout-only, outside this Drop-in flow.
- Recurring payments point to creating a shopper token, then using it for subsequent transactions; this page delegates detailed token creation/use to the tokenization guide rather than supplying a token-result guarantee. TEST paths describe a Google account/wallet and either Google's test-card suite or real cards mapped to Adyen test cards (not charged); its non-suite 3DS2 challenge instruction is limited to American Express/Discover. Before live, the page calls for the API Clientside Encryption Payments role, live Customer Area Google Merchant ID configuration, and Google production-access/deployment steps. It also says live availability requires a logged-in shopper with a valid Google Pay funding method. These conditions do not prove current account enablement or any payment outcome.

## Detail locators

- [[raw/adyen/docs/payment-methods/google-pay/web-drop-in/2026-09-15|Pinned raw]], lines 15–36: identity, payment-sheet/3DS behavior, prerequisites and Sessions versus Payments route.
- Same raw, lines 38–112: preload/iframe conditions and Payments versus Sessions configuration; lines 114–130: Drop-in-only instant button option/version.
- Same raw, lines 132–214: optional merchant identity, JWT, button, payment/card/readiness and transaction-info fields, including country-code distinctions and Authorize Payments reference.
- Same raw, lines 216–245: event descriptions and illustrative optional configuration; lines 247–250: recurring tokenization navigation.
- Same raw, lines 252–290: test-card-suite versus mapped-card testing, live API role/Google Merchant ID/production access and logged-in/funding-method limits.

## Related

- [[source-adyen-docs-payment-methods-google-pay]] — Google Pay overview and channel chooser.
- [[adyen-tokenization]] — general token lifecycle context.

## Raw Sources

- [[raw/adyen/docs/payment-methods/google-pay/web-drop-in/2026-09-15|Google Pay Drop-in integration]]
