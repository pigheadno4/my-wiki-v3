---
title: "GCash iOS Component | Adyen Docs"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gcash/ios-component"
raw_files:
  - "adyen/docs/payment-methods/gcash/ios-component/2026-09-15.md"
tags: [adyen, gcash, ios, components, redirect, tokenization]
---

## Overview

[[adyen]]'s GCash iOS Component guide is a method-specific add-on to an existing iOS Components integration, with separate Sessions and Advanced server-side flows. It uses `InstantPaymentComponent` for the `gcash` payment method and requires the integration's redirect handling. The page is an implementation guide, not evidence of merchant enablement or a completed payment. See [[adyen-online-payments]] and the fully read raw snapshot.

## Key takeaways

- **Sessions:** An existing Sessions iOS Components integration, Checkout API v68 or later, redirect handling for `action.type: redirect`, and GCash setup in Customer Area are listed prerequisites. The page says no GCash-specific `/sessions` parameters or Component configuration are needed. The example obtains `gcash` from the session's payment methods, sets the session as delegate, then calls `initiatePayment()`. See raw lines 25–69.
- **Advanced:** The page lists an existing Advanced iOS Components integration, redirect handling and Customer Area GCash setup. It says no GCash-specific Component configuration or `/payments` parameters are needed; the example assigns the merchant Component delegate before `initiatePayment()`. See raw lines 320–363.
- **Recurring:** Both flow sections state that GCash supports recurring transactions. For token creation, the page asks for `storePaymentMethod: true` and a shopper-unique `shopperReference` of at least three characters in `/payments`. It places the `recurring.token.created` webhook after settlement, with `storedPaymentMethodId` for subsequent `/payments` requests, and says the server must receive recurring-token lifecycle events. Later requests specify the stored ID, matching shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel` of `Subscription` or `UnscheduledCardOnFile` according to schedule. Token-request instructions do not themselves prove settlement, token creation, or a successful later charge. See raw lines 72–109 and 365–402.
- **Testing and live gate:** The page says testing successful GCash live payments requires a real mobile number registered to a GCash account, gives a test-payment status route in Customer Area, and says a GCash request in the live Customer Area is needed before accepting live payments. This snapshot does not establish account eligibility or current availability. See raw lines 310–318 and 603–611.

> [!warning] Source link discrepancy
> The Advanced requirement calls for an iOS **Components** integration, but its linked main-guide URL uses `integration=Drop-in`; the redirect and payment-step links in that section use `integration=Components`. Treat the prerequisite label and URL as conflicting navigation, and verify the intended base guide before implementation. See raw lines 328–329 and 363.

## Detail locators

- Sessions initialization code: raw lines 50–69. Advanced initialization code: raw lines 338–357. These are client-side Component examples; merchant-server payment and webhook outcomes remain separate.
- Recurring request examples in curl, Java, PHP, C#, Node.js, Python and Ruby: raw lines 111–308 and 404–601. They use PHP currency in examples and several TEST environments; examples do not state a universal country, currency, SDK-version or live-eligibility rule.
- Shopper-return mechanics and final payment status are delegated to the linked main integration guides rather than specified here. See raw lines 21–35 and 324–329.

## Related

- [[adyen-online-payments]] — main online payment architecture and method routes.
- [[adyen-tokenization]] — recurring-token lifecycle and shopper-reference context.
- [[adyen-ios-sdk]] — version-qualified native iOS SDK context.

## Raw Sources

- [[raw/adyen/docs/payment-methods/gcash/ios-component/2026-09-15|GCash iOS Component, 2026-09-15 snapshot]]
