---
title: "Adyen Bancontact mobile Web Drop-in"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bancontact/bancontact-mobile/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/bancontact/bancontact-mobile/web-drop-in/2026-09-15.md"
tags: [adyen, bancontact, mobile, web, drop-in, tokenization]
---

## Overview

Adyen's Bancontact mobile guide describes adding the mobile-app/QR payment route to an existing Web Drop-in integration. Desktop shoppers see a QR code; mobile shoppers switch to the Bancontact app with a QR fallback if switching fails; tablet shoppers see both QR and an app-switch button. This is Bancontact *mobile*, not Bancontact card-entry guidance. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The page requires an existing Web Drop-in integration and Bancontact mobile added in the test Customer Area. To receive `bcmcmobile.urlIntent` in the payment response, enable **3DS2 Additional Fields** under **Developers > Additional data** in Customer Area. This is a conditional response-field setup, not a universal requirement for rendering the method (raw lines 19-37).
- No Bancontact-mobile-specific fields are needed for the base API request, and no method-specific Drop-in configuration is required. The page names `/sessions` as the default for Drop-in v5.0.0 or later and `/payments` for an implemented additional use case; the parent integration's ordinary fields and flow still apply (raw lines 39-48).
- Recurring is a distinct Bancontact Wallet Initiated Program (WIP) route. The page recommends explicit shopper permission. WIP requires signup and Support enablement, is not available to every company, and has transaction amount limits. It describes initial shopper consent/SCA and later transactions without SCA, with issuer liability stated for that WIP scenario; these are source-scoped claims, not a general current guarantee (raw lines 50-78).
- To create a WIP token, request `storePaymentMethod: true` and a unique `shopperReference` of at least three characters in `/sessions` or `/payments`. After the initial payment settles, the `recurring.token.created` lifecycle webhook supplies `storedPaymentMethodId`, which the server must receive. Later `/payments` use the stored ID, same shopper reference, `ContAuth`, and `Subscription` or `UnscheduledCardOnFile`; the example selects `paymentMethod.type: bcmc_mobile` and `Subscription`. Recurring tests need Support configuration (raw lines 78-130; language examples through line 444).
- The page explicitly says Bancontact mobile has no test platform and recommends a EUR 0.01 penny test in the live environment. This is a testing recommendation, not permission to initiate a live charge or proof of live operation. The page does not give a payment-outcome flow for the shopper app/QR path; use a relevant payment-flow source for result handling (raw lines 446-450).

## Detail locators

- Device-dependent QR/app-switch behavior and Customer Area setup: raw lines 15-37.
- Base request and Drop-in configuration boundaries: raw lines 39-48.
- WIP eligibility, consent, SCA and amount limits: raw lines 50-78.
- Token creation, after-settlement webhook and subsequent recurring request: raw lines 80-107; request examples 109-444.
- No test platform and live penny-test recommendation: raw lines 446-450.

## Raw Sources

- [[raw/adyen/docs/payment-methods/bancontact/bancontact-mobile/web-drop-in/2026-09-15|Bancontact mobile Web Drop-in guide (2026-09-15 capture)]]
