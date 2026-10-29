---
title: "Adyen PaySafeCard React Native Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paysafecard/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/paysafecard/react-native-component/2026-09-15.md"
tags: [adyen, paysafecard, react-native, components, advanced-flow]
---

## Overview

This 2026-09-15-captured Adyen guide adds PaySafeCard to an existing React Native Components integration. It explicitly says React Native Components do **not** support Sessions, so this add-on covers Advanced flow with `shopperReference` and redirect handling. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-paysafecard]] for the separate method overview and its conditional EU gambling Customer Data Exchange note.

## Key takeaways

- Begin with an existing **Advanced React Native Components** integration, redirect handling for `action.type: redirect`, and PaySafeCard added in Customer Area. The requirements-table link is labeled Components but its URL selects `integration=Drop-in`; its redirect and payment links select Components. Confirm the intended Components base guide. Sessions is explicitly unavailable for React Native Components on this page. See raw lines 25–41 and 53.
- No additional PaySafeCard Component configuration parameters are specified. Add required `shopperReference` to `/payments` as a unique identifier for the shopper, such as a user or account ID. See raw lines 43–57.
- The TEST v72 `/payments` request snippets are abbreviated: they show EUR and an HTTPS `returnUrl` in a React Native guide but omit an explicit `paymentMethod`; the curl example also lacks a shell continuation after `-X POST`. Do not treat these as complete native-app or executable payment requests. Verify actual return handling and Drop-in/Component request assembly against the Advanced base guide. See raw lines 59–342.
- The example response has `resultCode: RedirectShopper` and `action.type: redirect` with `paymentMethodType: paysafecard`. That is an additional action, not final payment confirmation. The separate overview labels the method's capability row “Direct”; retain this page's redirect handling as its specific integration instruction rather than using that overview label to skip redirect. See raw lines 344–358 and [[source-adyen-docs-payment-methods-paysafecard]].
- Test with the page's 16-digit code `0000 0000 0990 3417` and check test payment status in Customer Area. Before live acceptance, contact Support to add PaySafeCard in the **live** Customer Area. These are setup/test instructions, not evidence of current account eligibility or a successful transaction. See raw lines 360–368.

## Detail locators

- Sessions exclusion and Advanced prerequisites: raw lines 25–41.
- No extra configuration and required shopper reference: raw lines 43–57.
- TEST v72 payment examples: raw lines 59–342.
- Redirect response example: raw lines 344–358.
- Test code, test status and live Support gate: raw lines 360–368.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-paysafecard]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paysafecard/react-native-component/2026-09-15|Fully read PaySafeCard React Native Component raw]]
