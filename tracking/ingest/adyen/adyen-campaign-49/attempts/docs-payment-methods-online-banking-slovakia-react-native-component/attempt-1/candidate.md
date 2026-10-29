---
title: "Online banking Slovakia React Native Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-slovakia/react-native-component"
raw_files:
  - "adyen/docs/payment-methods/online-banking-slovakia/react-native-component/2026-09-15.md"
tags: [adyen, online-banking-slovakia, react-native, component, redirect]
---

## Overview

This 2026-09-15-captured Adyen page is titled “Online banking Slovakia React Component” at a **React Native Component** URL. It says React Native Components **do not support Sessions flow** and provides Advanced-flow additions for the Slovakia bank redirect. It is a dated integration snapshot, not proof of current merchant enablement or transaction outcome. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-online-banking-slovakia]] for method-level SK/EUR context.

## Key takeaways

- The Sessions section is explicitly **Not Available**: “React Native Components do not support Sessions flow” (raw lines 25–29). Do not import requirements from another platform's Sessions guide into this page.
- Advanced flow requires an existing React Native Components integration, `action.type: redirect` handling, and Online banking Slovakia added in Customer Area (raw lines 31–42). **Documentation gaps:** the integration-type link in the Components row points to `integration=Drop-in`, and the Checkout API minimum reads “v or later” with no version number. Neither supplies a verified minimum API version or a correct Components base URL.
- No Slovakia-specific Component configuration parameters are added (raw lines 44–48). The Advanced `/payments` request requires `paymentMethod.issuer`, the issuing bank selected by the shopper (raw lines 50–58). Sample requests use `paymentMethod.type: onlineBanking_SK`, `issuer: cs`, EUR amount, and `returnUrl`; these are sample values, not an exhaustive issuer list or proof of merchant availability (raw lines 60–80 and 207–235).
- The page gives curl and several SDK request examples using test endpoint/environment and placeholder credentials. The Go example labels library **v10.4.0** while importing `/v9/` module paths; verify SDK-version syntax before reuse (raw lines 60–370, especially 237–246). Idempotency-key placeholders in examples are not a guarantee of payment outcome.
- The captured instructions say to test with real payment details and small amounts, check test status in test Customer Area **Payments > Payment list**, and add the method in Customer Area for live acceptance (raw lines 372–378). Redirect handling and a test instruction do not establish final payment status or live readiness.

## Detail locators

- React Native Sessions exclusion: raw `## Sessions flow Component`, lines 25–29.
- Advanced requirements and incomplete/misdirected prerequisite links: raw `## Advanced flow Component`, lines 31–42.
- No extra configuration and required selected issuer: raw lines 44–58.
- Curl/SDK request examples and Go version mismatch: raw lines 60–370.
- Test and live instructions: raw lines 372–378.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-slovakia]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-slovakia/react-native-component/2026-09-15|Online banking Slovakia React Native Component, captured 2026-09-15]]
