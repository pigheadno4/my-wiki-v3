---
title: "Adyen Bancontact card Android Drop-in v4.x.x integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bancontact/bancontact-card/android-drop-in/earlier-versions"
raw_files:
  - "adyen/docs/payment-methods/bancontact/bancontact-card/android-drop-in/earlier-versions/2026-09-15.md"
tags: [adyen, bancontact, android, drop-in, earlier-versions, online-payments]
---

## Overview

An **earlier-versions v4.x.x** guide for adding **Bancontact card** to an existing Android Drop-in integration. It requires an **Advanced flow** Android Drop-in integration and Bancontact card enabled in the Customer Area. This is a Bancontact **card** path, not a general Bancontact mobile-app guide or evidence of current merchant eligibility. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The page distinguishes Bancontact card from a regular card payment: no CVC for Bancontact (though a co-badged card can show a CVC field), mandatory 3D Secure authentication, and no separate captures. To show the method, the `/paymentMethods` request specifies `countryCode: BE` and `amount.currency: EUR`. See raw lines 19–41.
- The Requirements table specifies Advanced-flow Android Drop-in, but the opening, optional-configuration and See also links point to Sessions-flow guides; those links are not verified Advanced base routes (raw lines 25, 33, 45, 909). In this v4.x.x flow, Android Drop-in collects card details and returns `paymentComponentData`; the app passes it to the merchant server. The server is instructed to send `/payments` with the returned `paymentMethod`, required `channel: Android`, and a return URL from `RedirectComponent.getReturnUrl(context)`. Every illustrated `/payments` request omits `channel`; use the prose requirement and treat the examples as incomplete request templates (raw lines 69–72, 75–401). The illustrated response has a `redirect` action; the server returns that action to the client. After the shopper returns, Drop-in supplies `actionComponentData.details` for the server's `/payments/details` request. Present the result from its `resultCode`; the outcome also arrives asynchronously by webhook. Possible result codes listed here are `Authorised`, `Cancelled`, `Error`, and `Refused`. See raw lines 63–74, 403–472.
- **Redirect wording conflict:** the opening says the shopper returns to a “website,” while the dedicated redirect section says the shopper returns to the Android app. Treat the Android app return flow as the platform-specific description, and verify the return URL against the Android integration. The `/payments` curl snippet has markup-like hint text embedded in the `paymentMethod` key; it is an annotated example, not literal request JSON. See raw lines 25–27, 73, 87–95, 426–445.
- The optional Kotlin `BcmcConfiguration` example is labeled as making cardholder name required, but the shown builder only sets the test environment and adds the configuration to Drop-in; it does not show a cardholder-name requirement setting. Do not infer that behavior from the snippet. See raw lines 43–61.
- Recurring use is qualified by Bancontact Wallet Initiated Program (WIP) signup and eligibility, with amount limits; the page recommends explicit shopper permission. The first consented transaction uses SCA, while its WIP discussion says subsequent transactions do not and states no liability shift for the initial transaction. Token creation calls for `storePaymentMethod: true` and a unique `shopperReference`; after settlement, a `recurring.token.created` webhook supplies `storedPaymentMethodId`. Future `/payments` use that ID, the reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` or `UnscheduledCardOnFile`. Test-environment recurring setup requires Support. This is a conditional WIP path, not general recurring availability. See raw lines 474–531.
- The test section has co-badged card examples and warns one BCMC/Visa test card may route to Bancontact or Visa depending on method setup. Its live section says to add Bancontact card in the live Customer Area and mentions a Client Encryption Public Key, but gives no complete current live-key procedure. See raw lines 870–905.

## Detail locators

- v4.x.x identity, method distinctions, Advanced prerequisite versus Sessions links: raw lines 15–34, 45, 909.
- BE/EUR method display and optional configuration: raw lines 36–61.
- `/payments` Android-channel requirement, omission in examples, and redirect action: raw lines 63–424.
- Redirect details, shopper result, asynchronous webhook: raw lines 426–472.
- WIP enrollment, token creation, recurring payment request: raw lines 474–868.
- Test credentials, co-badge routing caveat, live notes: raw lines 870–905.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/bancontact/bancontact-card/android-drop-in/earlier-versions/2026-09-15|Bancontact card Android Drop-in earlier-versions capture (2026-09-15)]]
