---
title: "Online banking Slovakia Web Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-slovakia/web-component"
raw_files:
  - "adyen/docs/payment-methods/online-banking-slovakia/web-component/2026-09-15.md"
tags: [adyen, online-banking-slovakia, web-component, redirect, issuer]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Online banking Slovakia** to an existing Web Components integration using either Sessions or Advanced server-side flow. Both require redirect handling and Customer Area setup. It is a dated integration guide, not evidence of current merchant enablement or payment execution. See [[adyen]], [[adyen-online-payments]], and the method overview [[source-adyen-docs-payment-methods-online-banking-slovakia]] for the SK/EUR method and capability matrix.

## Key takeaways

- **Sessions flow** requires an existing Web Components Sessions integration, Checkout API **v68 or later**, `action.type: redirect` handling, and Online banking Slovakia added in Customer Area. The guide says no additional `/sessions` parameters and no additional Component configuration are needed (raw lines 23–40, 54–58).
- **Advanced flow** requires an existing Web Components Advanced integration, redirect handling, and Customer Area setup (raw lines 86–94). The `/payments` request must include `paymentMethod.issuer`, the bank selected by the shopper (raw lines 132–140). The examples use `paymentMethod.type: onlineBanking_SK`, `issuer: cs`, EUR amount, and `returnUrl`; those are sample request values, not proof of a merchant's issuer eligibility or a universal fixed issuer list (raw lines 146–162, 299–317).
- The Web package import is `OnlineBankingSK`; both flows say to initialize that Component class (raw lines 42–75, 96–130). **Warning:** both displayed constructor snippets spell `newOnlineBankingSK` as one token rather than `new OnlineBankingSK`, and the Go example labels library v10.4.0 while importing `/v9/` paths (raw lines 68–75, 122–130, 321–327). Treat samples as locators, not copy-ready recipes; verify against the relevant SDK version.
- The Advanced examples show test API endpoints/environment and `ADYEN_API_KEY` placeholders, with several library examples including an idempotency-key placeholder (raw lines 146–198, 289–317, 360–451). These examples do not authorize live use or establish a general idempotency guarantee.
- For both flows, the page instructs testing with real payment details and small amounts, checking test payment status in test Customer Area **Payments > Payment list**, and adding the method in Customer Area for live acceptance (raw lines 78–84, 454–460). A test instruction and redirect action do not establish authorization, final status, or live readiness.

## Detail locators

- Sessions requirements and no extra request parameters: raw `## Sessions flow Component`, lines 23–40.
- Sessions import/configuration/initialization: raw lines 42–75.
- Advanced requirements, class setup, and required selected issuer: raw `## Advanced flow Component`, lines 86–140.
- Advanced curl and SDK request examples: raw lines 142–452; inspect exact library/version context before reuse.
- Test and live instructions repeated for both flows: raw lines 78–84 and 454–460.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-slovakia]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-slovakia/web-component/2026-09-15|Online banking Slovakia Web Component, captured 2026-09-15]]
