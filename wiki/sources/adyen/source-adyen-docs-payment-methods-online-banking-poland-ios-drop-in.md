---
title: "Online banking Poland iOS Drop-in"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-poland/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/online-banking-poland/ios-drop-in/2026-09-15.md"
tags: [adyen, online-banking-poland, ios, drop-in, redirect]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Online banking Poland to an existing iOS Drop-in integration** through Sessions or Advanced server-side flow. It covers required shopper email, Advanced redirect action and selected-bank issuer field, and test/live setup. RedirectShopper is an intermediate handoff, not proof of completed payment. See [[adyen]], [[adyen-online-payments]], and the method overview [[source-adyen-docs-payment-methods-online-banking-poland]] for Przelewy24 branding and PL/PLN capability context.

## Key takeaways

- **Sessions flow** requires an existing iOS Drop-in Sessions integration, Checkout API **v68 or later**, and Online banking Poland added in Customer Area (raw lines 25–34). Its `/sessions` addition is required `shopperEmail`, maximum **50 characters** (raw lines 36–44). The examples show PL/PLN and an app-style `adyencheckout://` return URL as sample values (raw lines 46–266); they do not prove a live payment.
- No Poland-specific Drop-in configuration parameters are needed for Sessions or Advanced (raw lines 268–272, 294–298).
- **Advanced flow** requires an existing iOS Drop-in Advanced integration, `action.type: redirect` handling, and Customer Area setup (raw lines 282–292). Its `/payments` addition requires `shopperEmail`, also with a **50-character maximum**, and lists `paymentMethod.issuer` as the selected bank's issuer ID **without a required mark** (raw lines 300–309). Do not turn the issuer value in examples into a universal required-field claim. The Advanced requirements table does not state the Sessions v68 API minimum.
- Advanced examples use `paymentMethod.type: onlineBanking_PL`, `issuer: 141`, PLN and a website-style `https://your-company.com/checkout...` return URL (raw lines 311–641). The website URL is a placeholder in an **iOS** guide; verify the app's return/deep-link setup in the base integration rather than copying it as a verified iOS return URL. The curl snippets omit a line continuation after `-X POST` before `-d` (raw lines 50–67, 315–335), and some SDK examples omit request-object construction, so these are not complete copy-ready commands/programs.
- The Advanced response includes `action.type: redirect` and example `resultCode: RedirectShopper` (raw lines 643–657). Check test payment status in test Customer Area **Payments > Payment list**; before live acceptance, submit a method request in live Customer Area (raw lines 274–280, 659–665). Neither redirect nor test lookup establishes successful live payment.

## Detail locators

- Sessions prerequisites, email field and request examples: raw `## Sessions flow Drop-in`, lines 25–266.
- No extra configuration and Sessions test/live gate: raw lines 268–280.
- Advanced prerequisites, no extra configuration and email/issuer fields: raw `## Advanced flow Drop-in`, lines 282–309.
- Advanced examples, website-style return URL and redirect response: raw lines 311–657.
- Advanced test/live gate: raw lines 659–665.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-poland]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-poland/ios-drop-in/2026-09-15|Online banking Poland iOS Drop-in, captured 2026-09-15]]
