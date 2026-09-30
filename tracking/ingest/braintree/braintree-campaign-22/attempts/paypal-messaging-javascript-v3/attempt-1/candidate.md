---
title: "Braintree PayPal Pay Later Messaging - JavaScript v3"
type: source
date_ingested: 2026-09-29
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/guides/paypal/messaging/javascript/v3"
raw_files:
  - "braintree/docs/guides/paypal/messaging/javascript/v3-2026-09-16.md"
tags: [braintree, paypal, pay-later, messaging, javascript-v3, ios, android]
---

## Overview

This collected Braintree page is stored at the PayPal Messaging JavaScript v3 route, but its retained body describes eligibility for PayPal Pay Later Messaging in native iOS and Android integrations. It says the feature is unavailable through Drop-in and gives merchant, country, integration and content restrictions. The snapshot contains no JavaScript v3 setup procedure, so use it as a route to the captured eligibility and warning text rather than as JavaScript implementation evidence.

## Key takeaways

- The page says PayPal Pay Later Messaging is available to merchants using the latest iOS and Android SDKs and is not available to merchants using Drop-in. That statement is native-SDK-scoped despite the JavaScript v3 URL.
- It lists eligible merchants in the US, GB, DE, FR, IT, ES and AU, then requires a current Braintree merchant using the latest Braintree integration to build native iOS or Android apps. It also requires a one-time payment integration where Pay Later options are available through PayPal checkout.
- The page requires compliance with the PayPal Acceptable Use Policy and prohibits adding or editing message content, wording or marketing to encourage use of Pay Later. PayPal reserves the right to act under the PayPal User Agreement.
- Real Money Gaming is given as an ineligible example, and the page warns that additional merchant categories may periodically be identified as ineligible to promote Pay Later offers.

## Evidence boundaries

> [!warning] Route and SDK mismatch
> The canonical path is a JavaScript v3 guide, but the collected body supplies native iOS/Android eligibility and excludes Drop-in. It does not document JavaScript v3 component loading, rendering, callbacks or another web integration step; do not reconstruct those details from the route name.

> [!warning] Eligibility is not enablement or approval
> The listed merchant, country and integration conditions do not establish current product availability, enablement for a particular merchant, buyer approval, authorization, tokenization or payment completion. Generic offer identity and merchant-enablement guidance belong to their separate authorities.

> [!warning] Messaging is presentment only
> Preserve the no-edit restriction and category exclusions as promotional-presentment rules. They do not describe Pay Later offer terms or payment execution.

## Detail locators

- Native iOS/Android availability and Drop-in exclusion: `**AVAILABILITY**`, line 18.
- Listed eligible merchant countries: `**ELIGIBILITY**`, line 24.
- Merchant, integration, native-app, one-time-payment, policy and message-editing conditions: `**ELIGIBILITY**`, lines 26-34.
- Real Money Gaming example and additional-category warning: `**ELIGIBILITY**`, line 36.
- Upstream next-page navigation, not evidence read for this source: `Next Page: Server-side`, line 40.

## Related

- Company: [[braintree]]
- Product concept: [[paypal-pay-later]]
- Payment-method context: [[braintree-payment-methods]]
- Separate JavaScript v3 offer implementation route: [[source-braintree-paypal-pay-later-offers-javascript-v3]]
- Separate generic offer identity and enablement route: [[source-braintree-payment-methods-paypal-pay-later-offers]]

## Raw Sources

- [[raw/braintree/docs/guides/paypal/messaging/javascript/v3-2026-09-16|Braintree PayPal Pay Later Messaging - JavaScript v3]] - complete collected page whose body contains native iOS/Android eligibility, Drop-in exclusion and messaging restrictions
