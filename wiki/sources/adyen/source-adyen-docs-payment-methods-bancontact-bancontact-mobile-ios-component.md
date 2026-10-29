---
title: "Adyen Bancontact Mobile iOS Component integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bancontact/bancontact-mobile/ios-component"
raw_files:
  - "adyen/docs/payment-methods/bancontact/bancontact-mobile/ios-component/2026-09-15.md"
tags: [adyen, bancontact, mobile, ios, components, app-switch, recurring]
---

## Overview

This captured Adyen guide adds Bancontact Mobile to an existing iOS Components integration. It describes app switching and QR presentation for mobile/tablet shoppers, version-specific Component construction, and a separately gated Bancontact Wallet Initiated Program (WIP) recurring path. It does not establish merchant eligibility, a working device return, successful payment, or a live test result. See [[adyen]], [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-bancontact|the Bancontact overview]].

## Key takeaways

- The iOS Component renders Bancontact in the payment form. On mobile, it switches to the Bancontact app, with QR as fallback if switching fails; on tablet, it shows both QR and an app-switch button. An existing iOS Components integration and Bancontact test Customer Area setup are listed as prerequisites. To receive `bcmcmobile.urlIntent` in the payment response, enable **3DS2 Additional Fields** under Customer Area **Developers → Additional data → 3D Secure**. The page does not specify an app-return/result implementation, so that remains with the base iOS integration.
- No Bancontact-specific additional request fields are stated. `/sessions` is described as the default for Components v5.0.0 or later; `/payments` is for an additional use case. With v5+, the Sessions and Advanced examples select `.other("bcmc_mobile")` and instantiate `InstantPaymentComponent`, but delegate it to `session` for Sessions and `self` for Advanced before `initiatePayment()`. The earlier v4.x.x sample instead presents a generic `Component` with `FormComponentStyle`. These are version-specific examples, not interchangeable instructions or Checkout API minimums.
- Recurring/tokenization is described through WIP, which requires signup and is not available to every company; contact support to enable it. WIP has transaction amount limits, but the capture gives no values. The guide strongly recommends explicit shopper permission. It says the first consent transaction receives SCA, subsequent transactions do not, and because the first has SCA there is no liability shift and the issuer remains liable. This is the page's qualified WIP description, not a general waiver of authentication or current eligibility proof.
- For WIP token creation, set `storePaymentMethod=true` with `shopperReference` (minimum three characters) in `/sessions` or `/payments`. After the first payment settles, a `recurring.token.created` webhook supplies `storedPaymentMethodId`; the server must receive recurring-token lifecycle events. Future `/payments` uses that ID in `paymentMethod.storedPaymentMethodId`, the same shopper reference, `shopperInteraction=ContAuth`, and `recurringProcessingModel=Subscription` or `UnscheduledCardOnFile`. The EUR/v72 `bcmc_mobile` Subscription body is an example, not a minimum API version.
- The guide simultaneously instructs test Customer Area setup and says support can configure a test environment for recurring, yet its Test and go live section says Bancontact Mobile has no test platform and recommends a EUR 0.01 live penny test. Preserve that distinction without claiming the example TEST request can execute an end-to-end Bancontact Mobile transaction. No live test is performed here. The NodeJS recurring samples also use `Config` and `EnvironmentEnum` without importing those names.

## Detail locators

- Mobile/tablet app-switch/QR behavior: pinned raw lines 15–24. iOS integration, Customer Area and `bcmcmobile.urlIntent` additional-data condition: lines 26–36. No extra method fields and endpoint distinction: lines 38–43.
- v5+ Sessions and Advanced `InstantPaymentComponent`/delegate examples: pinned raw lines 45–82. v4.x.x generic Component example and no further Bancontact-specific configuration: lines 84–100.
- WIP signup, eligibility, unspecified amount limits, consent and SCA/liability language: pinned raw lines 102–121. Support-configured recurring test environment and token creation/settlement webhook: lines 123–146. Future-token fields: lines 148–159; sample test v72/EUR Subscription request and SDK examples: lines 161–496. NodeJS undeclared configuration symbols: lines 315–327 and 459–469. No test platform and live penny-test recommendation: lines 498–502.

## Related

- [[adyen-online-payments]] — main provider payment integration concept
- [[source-adyen-docs-payment-methods-bancontact]] — method overview and card/mobile distinction

## Raw Sources

- [[raw/adyen/docs/payment-methods/bancontact/bancontact-mobile/ios-component/2026-09-15|Bancontact Mobile iOS Component guide, captured 2026-09-15]]
