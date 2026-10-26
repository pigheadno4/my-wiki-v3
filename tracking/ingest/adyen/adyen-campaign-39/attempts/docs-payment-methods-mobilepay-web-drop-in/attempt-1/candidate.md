---
title: "Adyen MobilePay Web Drop-in integration guide"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/mobilepay/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/mobilepay/web-drop-in/2026-09-15.md"
tags: [adyen, mobilepay, web, drop-in, redirect, payouts]
---

## Overview

This 2026-09-15 Adyen page adds MobilePay to an existing Web Drop-in integration, separately for Sessions and Advanced flows. It covers redirect and Customer Area prerequisites, optional Web imports, an experimental Advanced-flow payout-token route, and qualified testing instructions. It provides method-specific additions; the main integration guides own the full payment flow. Its snapshot does not establish current merchant eligibility or an actual payment or payout outcome. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Sessions requires an existing Sessions Web Drop-in integration, Checkout API v68 or later, redirect handling for `action.type: redirect`, and MobilePay added in Customer Area. It says no MobilePay-specific parameters need to be added to `/sessions`. Advanced requires an existing Advanced Web Drop-in integration, redirect handling and Customer Area setup. Its section does not state an API minimum. For ordinary Advanced `/payments`, it likewise says no extra MobilePay parameters are needed.
- For either flow, individual `Redirect` import from `@adyen/adyen-web` is optional for tree shaking. The import example is not a Web SDK version requirement.
- The guide says ordinary MobilePay payments cannot be tested in Adyen's test environment. It directs merchants to request MobilePay in the live Customer Area, make low-amount LIVE payments after addition, receive the `AUTHORISATION` webhook on their server, and inspect the payment in the live Customer Area. The webhook and list carry payment status; neither proves capture or settlement.
- Wallet payouts are marked experimental and supported only through `/payments`, not the Sessions route. For an Advanced-flow payment intended to create a future payout token, the prose requires a recurring lifecycle webhook and `/payments` fields `telephoneNumber`, `shopperReference`, and `enablePayout: true`. Save the resulting webhook's `storedPaymentMethodId` against `shopperReference`; a later Transfers API POST `/transfers` specifies the token in `counterparty.card.cardIdentification`. Token creation, future transfer request and payout outcome are separate steps. The page offers a Vipps MobilePay test-app procedure to simulate the customer, receive/process the recurring lifecycle webhook and submit a Transfers API request. This sits alongside the broad statement that MobilePay payments cannot be tested in Adyen's test environment; keep the ordinary-payment and experimental-payout-test scopes distinct without claiming the page resolves their environment relationship.
- The Advanced request examples contain blank `currency`, `paymentMethod.type`, and `returnUrl` values. The curl sample has hint markup in its JSON property names and spells the payout field `enablePayOut`, whereas the payout-token prose says `enablePayout`; several language samples omit `shopperReference` and the payout flag. These examples are incomplete and should not be copied as validated requests. The Advanced prerequisite hyperlink also contains an unresolved encoded template token, although its visible text specifies Web Drop-in.

## Detail locators

- Scope and Sessions prerequisites: pinned raw lines 15–36; no-extra-parameter statement and optional import: lines 38–54.
- Ordinary LIVE test procedure: pinned raw lines 56–68 and 341–353; experimental payout test-app procedure: lines 70–91 and 355–376.
- Advanced prerequisites, optional import and no-extra-parameter exception: pinned raw lines 93–121; incomplete request examples and markup: lines 123–305.
- Payout-token payment, recurring webhook and later Transfers API request: pinned raw lines 307–339.

## Related

- [[adyen-online-payments]] — main concept and Web integration architecture
- [[source-adyen-docs-payment-methods-mobilepay]] — method overview; separate authority for availability and payout scope

## Raw Sources

- [[raw/adyen/docs/payment-methods/mobilepay/web-drop-in/2026-09-15|MobilePay Web Drop-in guide, 2026-09-15]]
