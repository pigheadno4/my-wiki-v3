---
title: "Adyen Bancontact card iOS Component"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bancontact/bancontact-card/ios-component"
raw_files:
  - "adyen/docs/payment-methods/bancontact/bancontact-card/ios-component/2026-09-15.md"
tags: [adyen, bancontact, ios, components, online-payments]
---

## Overview

Adyen's add-on guide for **Bancontact card** in an existing **iOS Components** integration. It offers Sessions and Advanced server-side prerequisites; both require adding Bancontact card in the Customer Area. The page says the Component collects sensitive card information so it does not touch the merchant server; this statement concerns card information, not proof that no server-side payment work remains. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The page distinguishes Bancontact card from regular cards: no CVC for Bancontact, although a co-badged card can show a CVC field; mandatory 3D Secure authentication; and no separate captures. These describe the Bancontact **card** method, not every Bancontact mobile path. See raw lines 19–25.
- The base API reference says there are no additional Bancontact-card fields for the chosen integration. It identifies `/sessions` as the default with iOS Components v5.0.0+ and `/payments` for an additional use case. For v5+, the Swift snippets select a supported `.other("bcmc")` method and instantiate `InstantPaymentComponent`, with `session` as delegate in the Sessions snippet or `self` in Advanced. An earlier v4.x.x snippet uses a generic `Component` and `FormComponentStyle`. The page says no Bancontact-specific Component configuration is required. See raw lines 27–107.
- **Component/example qualification:** although the text says a Component renders Bancontact card and collects sensitive card data, the v5+ code shows `InstantPaymentComponent` and immediate `initiatePayment()`, with no card-entry fields shown. Preserve the snippet identity as source evidence; this page alone does not demonstrate how a card-entry form or 3DS return is handled in iOS. See raw lines 25, 52–107.
- Recurring use is through the **Bancontact Wallet Initiated Program (WIP)**: signup is required, not all companies qualify, amount limits apply, and the page strongly recommends explicit shopper permission. Its WIP discussion says SCA occurs on the first consented transaction, subsequent transactions do not require it, and there is no liability shift for that first transaction; the issuer remains liable. Testing recurring payments requires Support configuration. See raw lines 109–137.
- To create a token, include `storePaymentMethod: true` and a unique `shopperReference` in `/sessions` or `/payments`. After payment settlement, a `recurring.token.created` webhook supplies the `storedPaymentMethodId`; the server must receive token-lifecycle events. Future `/payments` use that ID and shopper reference with `shopperInteraction: ContAuth` and `recurringProcessingModel: Subscription` or `UnscheduledCardOnFile`. The example is a test `/payments` v72 Subscription request; it does not establish account eligibility. See raw lines 139–189.
- The test section provides co-badged card credentials and a forced-refusal example. It notes a Bancontact/Visa test card may route to Bancontact or Visa depending on setup. For live use, the page points to adding the method in the live Customer Area and configuring the Component with its live Client Key, without proving a live payment or furnishing a complete current key-handling procedure. See raw lines 505–540.

## Detail locators

- Card identity, 3DS/capture distinctions and iOS integration requirements: raw lines 15–50.
- v5+ Sessions/Advanced Swift snippets and v4.x.x snippet: raw lines 52–107.
- WIP conditions and token lifecycle: raw lines 109–166.
- Test recurring request examples across server libraries: raw lines 168–503.
- Test routing and live setup notes: raw lines 505–540.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/bancontact/bancontact-card/ios-component/2026-09-15|Bancontact card iOS Component documentation capture (2026-09-15)]]
