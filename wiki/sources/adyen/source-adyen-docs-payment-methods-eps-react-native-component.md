---
title: "Adyen EPS React Native Component"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/eps/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/eps/react-native-component/2026-09-15.md"
tags: [adyen, eps, react-native, components, redirect, recurring]
---

## Overview

This 2026-09-15 guide gives EPS-specific steps for an existing React Native Components integration. It explicitly says React Native Components do not support Sessions flow on this page; the described route is Advanced flow with redirect handling and EPS setup. It also describes future recurring payments through SEPA Direct Debit. This method page is not a complete integration guide or evidence of current merchant enablement, payment success or general React Native SDK Sessions capability. See [[adyen]], [[adyen-online-payments]], [[adyen-react-native-sdk]], [[adyen-tokenization]] and [[source-adyen-docs-payment-methods-eps|the EPS overview]].

## Key takeaways

- The Sessions section says React Native Components do not support Sessions flow. For Advanced, the prerequisites are an existing React Native Components Advanced integration, `action.type=redirect` handling, and EPS added in Customer Area. The integration-type cell calls this Components but links to a React Native Drop-in base URL; the redirect and make-payment links target Components. Resolve the intended base guide by the named integration before using that prerequisite link.
- The guide says EPS needs no additional Component configuration and no EPS-specific fields in the ordinary Advanced `/payments` request. General request construction and redirect completion remain in the linked base integration.
- Recurring transactions for EPS are described through SEPA Direct Debit. The guide strongly recommends explicit shopper permission and clarity about payment schedule and amount. Token creation uses `storePaymentMethod=true` and a unique `shopperReference` of at least three characters in `/payments`. After the initial payment settles, the configured recurring-token lifecycle webhook delivers `recurring.token.created`; its `storedPaymentMethodId` is used in later `/payments` with the same shopper reference, `shopperInteraction=ContAuth`, and `recurringProcessingModel=Subscription` or `UnscheduledCardOnFile`. The webhook's `eventId` is the initial `pspReference`.
- Test status can be checked in the test Customer Area. Before accepting live EPS, submit an EPS request in the live Customer Area. The page does not state a Checkout API or React Native SDK minimum version and does not establish current bank availability, authorization, settlement or recurring success.

## Detail locators

- EPS add-on scope and explicit Sessions unavailability: pinned raw lines 15–29. Advanced prerequisites and Drop-in URL in the Components integration-type cell: lines 31–41. No extra configuration or ordinary `/payments` fields: lines 43–53.
- SEPA recurring permission, initial `/payments` token request, post-settlement webhook and later stored-token request: pinned raw lines 55–94. Test and live Customer Area gates: lines 96–100.

## Related

- [[adyen-online-payments]] — primary provider payment-integration route
- [[adyen-react-native-sdk]] — platform wrapper context; this page's Sessions limit is method/Component scoped
- [[adyen-tokenization]] — stored-method and recurring concepts
- [[source-adyen-docs-payment-methods-eps]] — EPS method overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/eps/react-native-component/2026-09-15|EPS React Native Component guide, captured 2026-09-15]]
