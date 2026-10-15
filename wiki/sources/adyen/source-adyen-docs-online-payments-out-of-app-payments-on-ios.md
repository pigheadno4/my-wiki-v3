---
title: "Out-of-app payments on iOS | Adyen Docs"
type: source
date_ingested: 2026-10-15
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/out-of-app-payments-on-ios"
raw_files:
  - "adyen/docs/online-payments/out-of-app-payments-on-ios/2026-09-15.md"
tags: [adyen, ios, out-of-app-payments, hosted-checkout, web-checkout]
---

## Overview

This 2026-09-15 snapshot of an Adyen page last modified in 2023 describes sending an iOS app shopper to a **mobile browser** to pay for an in-app purchase, then returning to the app. It offers either the merchant's Web Drop-in/Components checkout or Adyen Hosted Checkout. The payment is completed on a website, rather than through native iOS Drop-in/Components. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Adyen frames this route around an Apple guideline update but recommends it only for merchants based in the US, or merchants elsewhere accepting US App Store payments for digital goods and services. For other purchase types, the page directs readers to native iOS Drop-in/Components. This dated provider recommendation is not evidence of current Apple rules, regional legal permission, an app's entitlement or review approval, or merchant eligibility.
- The listed setup needs a Web Advanced flow using Drop-in/Components or API-only, a Web Sessions flow using Drop-in/Components, or Hosted Checkout. The merchant API credential needs the **Checkout webservice role**, and the integration must subscribe to Standard webhooks.
- With a merchant Web checkout, the app opens its existing checkout in a mobile browser and the merchant implements the return to the app. Sessions uses `/sessions`; Advanced uses `/paymentMethods`, `/payments`, and `/payments/details`. With Hosted Checkout, the merchant creates a session with an app URL in `returnUrl`, opens the Adyen-hosted page URL, and Adyen's flow redirects back to the app after the hosted payment flow.
- The page says to take the payment outcome from an `AUTHORISATION` webhook for either route. Returning to the app or showing a confirmation screen does not independently prove authorization. If using the browser route for subscriptions, the merchant must manage subscriptions itself.
- Before live use, Adyen directs the merchant to test an out-of-app payment with test card numbers. The source has no live acceptance evidence and no specific Apple entitlement or App Review procedure.

## Detail locators

- Stated purpose, Apple policy reference, and page age: lines 15–19 and frontmatter line 11.
- Integration modes, credential role, webhook requirement, US recommendation, other-purchase native route, and subscription management: `Requirements`, lines 21–33.
- App-to-browser-to-app sequence: `How it works`, lines 35–43.
- Merchant Web versus Adyen Hosted Checkout return responsibilities: `Redirect your shoppers for an out-of-app payment`, lines 47–54.
- Web Sessions/Advanced API paths, return handling, and AUTHORISATION webhook: lines 56–73.
- Hosted Checkout session `returnUrl`, hosted URL, return, and AUTHORISATION webhook: lines 75–85.
- Pre-live test route: `Test and go live`, lines 87–89.

## Related

- [[adyen-online-payments]] — provider online-payment integration route.
- [[adyen-ios-sdk]] — separate native iOS SDK route; this page describes browser checkout from an iOS app.

## Raw Sources

- [[raw/adyen/docs/online-payments/out-of-app-payments-on-ios/2026-09-15|Out-of-app payments on iOS (2026-09-15)]]
