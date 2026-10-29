---
title: "Adyen Bancontact mobile iOS Drop-in integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bancontact/bancontact-mobile/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/bancontact/bancontact-mobile/ios-drop-in/2026-09-15.md"
tags: [adyen, bancontact, mobile, ios, drop-in, online-payments]
---

## Overview

Adyen's add-on guide for **Bancontact mobile** in an existing **iOS Drop-in** integration. Drop-in renders the method; a phone shopper switches to the Bancontact app with QR fallback if switching fails, while a tablet shopper sees both a QR code and app-switch button. This is the mobile app/QR route, not Bancontact card acceptance or proof of a completed payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The page requires an existing iOS Drop-in integration and says to add Bancontact in the **test Customer Area**. To receive `bcmcmobile.urlIntent` in the payment response, it instructs enabling **3DS2 Additional Fields** under Developers → Additional data. This is a stated response-data prerequisite, not a guarantee that a particular app switch succeeds. See raw lines 21–36.
- The base API reference says no extra Bancontact fields are needed; `/sessions` is the default with Drop-in v5.0.0+, while `/payments` is for an additional use case. For both v5.0.0+ and v4.x.x, it says no Bancontact-specific Drop-in integration is required. See raw lines 38–53.
- Recurring transactions are described through the **Bancontact Wallet Initiated Program (WIP)**. Signup and eligibility are required, amount limits apply, and the page strongly recommends explicit shopper permission. It says the first consented transaction uses SCA, subsequent transactions do not, and there is no liability shift for that first transaction; the issuer remains liable. Support is needed to configure recurring testing. See raw lines 55–83.
- To create a token, send `storePaymentMethod: true` and a unique `shopperReference` in `/sessions` or `/payments`. Once the initial payment settles, a `recurring.token.created` webhook provides `storedPaymentMethodId`; the server must receive token-lifecycle events. Future `/payments` use that ID, the shopper reference, `shopperInteraction: ContAuth`, and `recurringProcessingModel: Subscription` or `UnscheduledCardOnFile`. The example uses `bcmc_mobile`, EUR and test Checkout API v72 for a Subscription payment; it does not establish WIP eligibility. See raw lines 85–135.
- **Testing scope tension:** the requirements refer to a test Customer Area and WIP testing needs Support setup, yet the final section says Bancontact mobile has **no test platform** and recommends a EUR 0.01 penny test in live. Preserve these as the page's distinct statements; do not infer a usable mobile test payment or perform a live payment from this source. See raw lines 31–36, 83, 451–455.

## Detail locators

- Mobile/tablet app-switch and QR presentation: raw lines 15–24.
- iOS prerequisites and `urlIntent` additional-data switch: raw lines 26–36.
- Base API and Drop-in version scopes: raw lines 38–53.
- WIP eligibility and token lifecycle: raw lines 55–112.
- `bcmc_mobile` recurring test examples across server languages: raw lines 114–449.
- Test-platform statement and live penny-test recommendation: raw lines 451–455.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/bancontact/bancontact-mobile/ios-drop-in/2026-09-15|Bancontact mobile iOS Drop-in documentation capture (2026-09-15)]]
