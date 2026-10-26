---
title: "Adyen GoPay React Native Component guide"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/gopay/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/gopay/react-native-component/2026-09-15.md"
tags: [adyen, gopay, react-native, components, redirect, recurring, tokenization]
---

## Overview

This 2026-09-15 Adyen guide adds GoPay to an existing React Native Components integration. It explicitly says React Native Components do **not** support Sessions flow, then gives Advanced-flow redirect, tokenization and recurring-payment instructions. The snapshot does not establish current merchant eligibility, an issued token or a completed payment. See [[adyen]], [[adyen-online-payments]] and [[adyen-tokenization]].

## Key takeaways

- **Flow and initial payment:** Sessions flow Components are marked unavailable. Advanced requires an existing React Native Components integration, `action.type: redirect` handling and GoPay added in Customer Area, with no extra Component configuration. The initial `/payments` table marks `paymentMethod.type: gopay_wallet`, `browserInfo` and `channel` required; channel is the applicable Web, Android or iOS value. The example is IDR, `channel: web`, Windows/Chrome browser data and a web return URL on this React Native page, so its values are not React Native defaults. It also has `-X POST` without a trailing line continuation and wraps nested `browserInfo` as a quoted JSON-like string with unescaped inner quotes; do not copy it as a validated request. Its `RedirectShopper` response with redirect action is intermediate. The Advanced integration-type row points to a Drop-in URL while the text and redirect/make-payment links say Components. The page does not pin a React Native SDK version or Checkout API minimum. (raw lines 25–108)
- **Token creation:** for the first shopper payment, the guide requires `storePaymentMethod: true`, a unique `shopperReference` of at least three characters and a `recurringProcessingModel`. After that payment **settles**, a `recurring.token.created` webhook carries the initial payment's `pspReference` as `eventId` and the `storedPaymentMethodId`; the merchant server must receive recurring-token lifecycle events. A request or redirect response alone does not establish a usable token. (raw lines 110–131)
- **Subscription:** later `Subscription` requests use the stored method ID, shopper reference, `shopperInteraction: ContAuth` and `recurringProcessingModel: Subscription`. The sample code has blank currency, payment-method type and return URL fields, so it is an incomplete template rather than an executable GoPay request. The `/payments` resultCode can be shown to the shopper, but the final processed payment status arrives in an `AUTHORISATION` webhook. (raw lines 133–357)
- **CardOnFile challenge:** unlike Subscription, `CardOnFile` requires redirecting the shopper to GoPay for PIN entry. A `RedirectShopper` response carries a redirect URL; after shopper return, call `/payments/details` with `redirectResult`. The guide places final processed status in an `AUTHORISATION` webhook. PIN entry, the redirect and details call do not themselves establish final authorization. (raw lines 358–383)
- **Environment:** the page directs GoPay testing questions to Adyen Support and separately requires a request in the live Customer Area before accepting live GoPay payments. Neither instruction proves a particular account is enabled or that a test or live payment succeeded. (raw lines 385–391)

## Detail locators

- Sessions unavailability and Advanced requirements/link mismatch: pinned raw lines 25–47.
- Advanced required fields, malformed IDR/web sample and redirect response: pinned raw lines 49–108.
- Settlement-gated token creation and webhook responsibility: pinned raw lines 110–131.
- Subscription fields, incomplete examples and final webhook boundary: pinned raw lines 133–357.
- CardOnFile shopper PIN redirect, details call and final webhook: pinned raw lines 358–383; TEST/LIVE setup: lines 385–391.

## Related

- [[adyen-online-payments]] — main provider payment and redirect context
- [[adyen-tokenization]] — token lifecycle and recurring paths
- [[source-adyen-docs-payment-methods-gopay]] — GoPay method overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/gopay/react-native-component/2026-09-15|GoPay React Native Component guide, 2026-09-15]]
