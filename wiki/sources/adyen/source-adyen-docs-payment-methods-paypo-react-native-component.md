---
title: "Adyen PayPo React Native Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypo/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/paypo/react-native-component/2026-09-15.md"
tags: [adyen, paypo, react-native, component, advanced-flow]
---

## Overview

This 2026-09-15-captured Adyen guide adds PayPo to an existing React Native Components integration. It covers the Advanced server-side flow; the page explicitly says React Native Components do not support Sessions. It is method-specific guidance, so use the main Advanced React Native Components guide for the complete integration. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- Begin with an existing Advanced React Native Components integration, redirect action handling, and PayPo enabled in Customer Area. No additional PayPo Component configuration parameters are specified. The requirements table's integration link is labeled Components but its URL selects `integration=Drop-in`; the payment and redirect links select Components. Resolve that mismatch against the intended Components integration before using the linked base guide. See raw lines 35–53.
- The `/payments` addition requires `paymentMethod.type: paypo`, `shopperName.firstName`, `shopperName.lastName`, and `shopperEmail`; billing and delivery addresses are shown without a required mark. The page's TEST v72 request is a PL/PLN example, not a statement of all eligible markets or production settings. See raw lines 55–89.
- A `/payments` response can return `resultCode: RedirectShopper` and `action.type: redirect`; handle that action and the return path through the existing integration. The example redirect response is an additional action, not final payment confirmation. See raw lines 40, 433–447.
- Before authorization, the PayPo offer/payment link is available for up to 72 hours. Once the shopper accepts, status becomes `Authorised` and the 30-day shopper payment term starts at authorization. Merchant capture follows authorization and can only capture the full authorized amount. Automatic capture immediately after authorization can be configured when adding PayPo in live Customer Area; manual capture uses `/payments/{paymentPspReference}/captures` with the original payment PSP reference. The merchant need not wait for the shopper to pay PayPo before capture. See raw lines 449–479.
- Test instructions give the required field values, verification code `123456`, and test Customer Area payment-list route. Live acceptance requires submitting a PayPo request in live Customer Area. These are setup/test instructions, not evidence of current availability or a completed live payment. See raw lines 481–493.

## Detail locators

- Requirements, redirect setup, and no additional configuration: raw lines 25–53.
- Payment-field table and TEST request/code examples: raw lines 55–431. The curl sample at lines 68–89 has a missing shell continuation after `-X POST`, and its HTTPS `returnUrl` is an example in a React Native guide; configure the actual app return handling rather than treating it as a universal mobile callback.
- Redirect action example: raw lines 433–447.
- Offer, authorization, capture, and funding description: raw lines 449–479.
- Test and live steps: raw lines 481–493.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-paypo]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypo/react-native-component/2026-09-15|Fully read PayPo React Native Component raw]]
