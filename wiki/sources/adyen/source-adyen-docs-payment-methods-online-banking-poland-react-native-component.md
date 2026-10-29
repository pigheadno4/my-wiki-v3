---
title: "Online banking Poland React Native Component"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-poland/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/online-banking-poland/react-native-component/2026-09-15.md"
tags: [adyen, online-banking-poland, react-native, component, redirect]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Online banking Poland to React Native Components** through **Advanced flow only**; the Sessions section explicitly says React Native Components do not support Sessions. It covers required shopper email, redirect handling and test/live setup. RedirectShopper is an intermediate handoff, not proof of completed payment. See [[adyen]], [[adyen-online-payments]], and the method overview [[source-adyen-docs-payment-methods-online-banking-poland]] for Przelewy24 branding and PL/PLN capability context.

## Key takeaways

- The `## Sessions flow Component` section is **Not Available** and states that React Native Components do not support Sessions flow (raw lines 25–29). Do not infer a React Native Components Sessions path from the general server-side-flow introduction.
- **Advanced flow** requires an existing React Native Components integration, `action.type: redirect` handling, and Online banking Poland added in Customer Area (raw lines 31–41). Its “Components integration” link points to `integration=Drop-in`, while its redirect link points to `integration=Components`; verify the appropriate base Components guide. The requirements table does not state a Checkout API minimum.
- No additional Poland-specific Component configuration parameters are needed (raw lines 43–47). Advanced `/payments` requires `shopperEmail` of **50 or fewer characters**. It lists `paymentMethod.issuer` as the selected bank's issuer ID **without a required mark** (raw lines 49–58). Do not treat the sample issuer value as a universal required field.
- The curl and SDK examples send `paymentMethod.type: onlineBanking_PL`, `issuer: 141`, PLN amount and `returnUrl` (raw lines 60–390). These are test/placeholder examples, not an exhaustive issuer list or live eligibility evidence. The curl snippet omits a shell continuation after `-X POST` before `-d` (raw lines 64–84), so it is not copy-ready as shown.
- The sample response has `resultCode: RedirectShopper` and `action.type: redirect` (raw lines 392–406). Test payment status is checked in test Customer Area **Payments > Payment list**. Before live acceptance, submit a method request in live Customer Area (raw lines 408–412). Neither the redirect nor a test status lookup proves successful live payment.

## Detail locators

- Sessions exclusion: raw `## Sessions flow Component`, lines 25–29.
- Advanced requirements and Drop-in link mismatch: raw `## Advanced flow Component`, lines 31–41.
- No extra configuration, required email and unmarked issuer: raw lines 43–58.
- Advanced sample requests and curl caveat: raw lines 60–390.
- Redirect response and test/live request: raw lines 392–412.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-poland]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-poland/react-native-component/2026-09-15|Online banking Poland React Native Component, captured 2026-09-15]]
