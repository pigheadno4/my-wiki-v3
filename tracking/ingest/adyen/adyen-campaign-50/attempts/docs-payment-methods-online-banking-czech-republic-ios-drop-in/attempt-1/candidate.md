---
title: "Online banking Czech Republic iOS Drop-in"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-czech-republic/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/online-banking-czech-republic/ios-drop-in/2026-09-15.md"
tags: [adyen, online-banking-czech-republic, ios, drop-in, redirect]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Online banking Czech Republic to an existing iOS Drop-in integration** using Sessions or Advanced server-side flow. It identifies flow prerequisites, says no additional method configuration or request parameters are needed, and gives test/live steps. See [[adyen]], [[adyen-online-payments]], and [[source-adyen-docs-payment-methods-online-banking-czech-republic]] for the CZ/CZK bank-redirect shopper flow and method capability matrix.

## Key takeaways

- **Sessions flow:** requires an existing iOS Sessions Drop-in integration using Checkout API **v68 or later**, plus Online banking Czech Republic added in Customer Area (raw lines 25–34). The guide says no additional parameters for the payment session and no additional method configuration (raw lines 36–46). Those statements concern this method's additions; they do not remove base integration fields.
- **Advanced flow:** requires an existing iOS Advanced Drop-in integration, redirect handling for `action.type: redirect`, and Customer Area method addition (raw lines 58–68). It says no additional method configuration or `/payments` parameters (raw lines 70–80). Base integration requirements still apply; this page states no separate Advanced Checkout API minimum.
- Both flows instruct tests with real payment details and small amounts, checking test payment status under test Customer Area **Payments > Payment list**, and adding the method in Customer Area for live acceptance (raw lines 48–56, 82–90). The instructions do not establish current account enablement or a successful/final payment from the redirect alone.

## Detail locators

- Sessions requirements, no extra session fields and no extra method configuration: raw `## Sessions flow Drop-in`, lines 25–46.
- Sessions test/live instructions: raw lines 48–56.
- Advanced prerequisites including redirect, no extra configuration or payment fields: raw `## Advanced flow Drop-in`, lines 58–80.
- Advanced test/live instructions: raw lines 82–90.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-czech-republic]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-czech-republic/ios-drop-in/2026-09-15|Online banking Czech Republic iOS Drop-in, captured 2026-09-15]]
