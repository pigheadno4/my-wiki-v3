---
title: "Online banking Poland React Native Drop-in"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-poland/react-native-drop-in"
raw_files:
  - "adyen/docs/payment-methods/online-banking-poland/react-native-drop-in/2026-09-15.md"
tags: [adyen, online-banking-poland, react-native, drop-in, redirect]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Online banking Poland** to an existing React Native Drop-in integration in Sessions or Advanced server-side flow. It covers shopper email, redirect handling, an unmarked bank-issuer field, and test/live Customer Area steps. A returned redirect action or test example does not establish completed payment or current merchant availability. See [[adyen]], [[adyen-online-payments]], and the separate [[source-adyen-docs-payment-methods-online-banking-poland|method overview]] for Przelewy24, PL/PLN and method capability context.

## Key takeaways

- **Sessions** requires an existing React Native Drop-in flow, Checkout API **v68 or later**, redirect-action handling and Customer Area addition. Its integration prerequisite links to an **Advanced-flow** base guide despite the Sessions heading; the session-creation and redirect links point to Sessions. Check the actual React Native Sessions base guide instead of treating the mismatched link as a flow change (raw lines 25–42).
- The only listed method-specific `/sessions` addition is **`shopperEmail`**, required and limited to **50 characters**. The TEST v71 request examples use PL/PLN and an `adyencheckout://` app-style `returnUrl`. No extra method configuration is needed. The curl snippet omits a continuation after `-X POST`, and some language snippets leave the session request object undeclared; the examples are not complete copy-ready recipes (raw lines 40–69, 71–274).
- **Advanced** requires an existing React Native Drop-in integration, redirect-action handling and Customer Area addition. No extra method configuration is listed. Its `/payments` table requires `shopperEmail` at up to 50 characters; `paymentMethod.issuer` is shown **without a required mark** and described as the shopper-selected bank ID. Examples use `paymentMethod.type: onlineBanking_PL` and issuer `141`. Do not turn the sample issuer into a universal value or make the unmarked table field unconditional (raw lines 282–335).
- Advanced TEST v72 examples use an HTTPS website `returnUrl`, while the Sessions example uses an app-style URL. The page does not establish that the HTTPS sample is a valid callback for every React Native app; use the applicable base integration's return handling. The sample response has `resultCode: RedirectShopper` and `action.type: redirect`, which is a redirect step, not final payment authorization. The v68 minimum is stated in the Sessions requirements, not the Advanced requirements (raw lines 316–335, 643–657).
- The page directs checking test payment status under test Customer Area **Payments > Payment list**. Before live acceptance, it says to request Online banking Poland in live Customer Area. This captured instruction is not evidence of current enablement or a successful live transaction (raw lines 276–280, 659–663).

## Detail locators

- Sessions prerequisites, required email and test request: raw `## Sessions flow Drop-in`, lines 25–69.
- Sessions language examples, configuration and test/live: raw lines 71–280.
- Advanced prerequisites, email/issuer table and payment examples: raw `## Advanced flow Drop-in`, lines 282–641.
- Advanced redirect response and test/live: raw lines 643–663.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-poland]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-poland/react-native-drop-in/2026-09-15|Online banking Poland React Native Drop-in, captured 2026-09-15]]
