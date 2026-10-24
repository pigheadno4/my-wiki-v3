---
title: "DANA React Native Component integration"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/dana/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/dana/react-native-component/2026-09-15.md"
tags: [adyen, dana, react-native, components, recurring]
---

## Overview

This 2026-09-15 Adyen page adds **DANA** to an existing **React Native Components** integration using **Advanced flow**. Its page title says “DANA React Component,” while the path and requirement text say React Native Components; the Sessions section explicitly says that React Native Components do **not** support Sessions. It documents an add-on and examples, not an observed payment or live eligibility. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Flow boundary:** despite introducing additions by server-side flow, the Sessions section consists of “Not Available” and explicitly excludes React Native Components Sessions. The Advanced requirement is an existing React Native Components integration, `action.type: redirect` handling, and DANA added in Customer Area. Its integration-type link is labeled Components but has `integration=Drop-in`; the separate redirect and payment links use `integration=Components`. Use the labeled Advanced Components requirement and verify the base guide, rather than treating the mismatched link as Drop-in authority. (raw lines 23–41, 51–53)
- **Ordinary Advanced scope:** no DANA-specific configuration parameters or additional ordinary `/payments` parameters are listed. The section gives no Checkout API minimum; the v68 TEST curl request later is an example version rather than a stated minimum. (raw lines 43–53, 94–114)
- **Conditional recurring route:** token creation sends `storePaymentMethod: true` and a unique `shopperReference` in `/payments`. Only **after the initial payment has settled** does the page say a `recurring.token.created` webhook carries shopper identity, initial-payment `eventId` and `storedPaymentMethodId`; the server must receive token lifecycle events. Later token payments use `paymentMethod.storedPaymentMethodId`, the same shopper reference, `shopperInteraction: ContAuth`, and `Subscription` for fixed intervals or `UnscheduledCardOnFile` for non-fixed contracts. These conditional fields qualify the ordinary no-extra-parameter statement. (raw lines 55–92)
- **Example and environment limits:** multi-language examples show `dana`, IDR and TEST-oriented placeholder credentials and token IDs. The Java example uses IDR 15000 while most others use IDR 1000; neither amount establishes a required minimum or a successful token charge. (raw lines 94–291)
- **TEST/LIVE wording:** under “Test and go live,” the page says testing **successful DANA live payments** needs a real DANA-registered mobile number, but also directs readers to a **test** Customer Area payment list and Support for testing issues. It separately says live acceptance needs a request in **live** Customer Area. This wording does not prove TEST success, live approval, authorization, capture or settlement. (raw lines 293–301)

## Detail locators

- Title, Sessions unsupported boundary and Advanced requirements/link mismatch: raw lines 15–41.
- Ordinary Advanced configuration and request statements: raw lines 43–53.
- Recurring token sequence and later request fields: raw lines 55–92.
- TEST-oriented examples and differing amounts: raw lines 94–291.
- Test/live wording and live request: raw lines 293–301.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-dana]]
- [[adyen-tokenization]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/dana/react-native-component/2026-09-15|Adyen DANA React Native Component, 2026-09-15 snapshot]]
