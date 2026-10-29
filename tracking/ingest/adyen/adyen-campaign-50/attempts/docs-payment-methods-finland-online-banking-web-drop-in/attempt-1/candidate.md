---
title: "Online banking Finland Web Drop-in"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/finland-online-banking/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/finland-online-banking/web-drop-in/2026-09-15.md"
tags: [adyen, finland-online-banking, web, drop-in, redirect]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Online banking Finland to an existing Web Drop-in integration** through Sessions or Advanced server-side flow. It covers required shopper email, optional `Redirect` import, Advanced conditional issuer, redirect action and Paytrail testing. A redirect response is not evidence of completed payment. See [[adyen]], [[adyen-online-payments]], and the method overview [[source-adyen-docs-payment-methods-finland-online-banking]] for Paytrail/FI/EUR context and bank-selection/refund-note qualifications.

## Key takeaways

- **Sessions flow** requires existing Web Drop-in Sessions, Checkout API **v68 or later**, `action.type: redirect` handling, and method addition in Customer Area. Its `/sessions` addition is required `shopperEmail` (raw lines 25–46). Examples use FI/EUR test requests but show `adyencheckout://your.package.name`, an iOS-style return URL on this **Web** page, and `s.hopper@@example.com`; do not copy those placeholders as a verified Web return URL or valid email (raw lines 48–339).
- Sessions optionally imports `Redirect` with `AdyenCheckout` and `Dropin` from `@adyen/adyen-web` for tree shaking (raw lines 342–352). This is an optional performance import, not a required separate Finland Component configuration.
- **Advanced flow** requires existing Web Drop-in, redirect handling, and Customer Area setup (raw lines 362–372). The prerequisite's base-guide URL contains encoded unresolved `{{getParameter('platform')}}` text rather than a concrete Web platform value; verify the actual Web Advanced guide. It likewise offers an optional `Redirect` import (raw lines 374–384). No Advanced Checkout API minimum is stated in this page's requirements.
- Advanced `/payments` marks **`paymentMethod.type: ebanking_FI`** and `shopperEmail` required. `paymentMethod.issuer` is relevant and required **only for Issuer redirect flow**; `returnUrl` is listed without a required mark, with a **1024-character maximum** (raw lines 386–397). The curl and SDK request examples omit `paymentMethod` entirely despite the required type (raw lines 399–682). They are incomplete illustrations; do not infer that issuer is always required or never required.
- The Advanced sample response gives `resultCode: RedirectShopper` and `action.type: redirect` (raw lines 684–698). Before live acceptance, both sections advise testing with Paytrail's test environment/sample data and state **testing multiple partial refunds is currently unavailable** (raw lines 354–360, 700–706). This is a test limitation in the captured child guide, distinct from the method overview's matrix mark for multiple partial refunds.

> [!warning] Advanced request examples omit a required field
> The Advanced table marks `paymentMethod.type: ebanking_FI` required (raw line 394), but the displayed curl and SDK requests omit `paymentMethod` (raw lines 399–682). Follow the field table and relevant API contract; supply `issuer` only when the Issuer redirect flow applies (raw line 395). The curl examples also omit a shell continuation after `-X POST` before `-d` (raw lines 53–69, 403–419).

## Detail locators

- Sessions prerequisites, required email and sample requests: raw `## Sessions flow Drop-in`, lines 25–339.
- Optional `Redirect` import and Paytrail testing limit: raw lines 342–360.
- Advanced prerequisites and unresolved base-guide link: raw `## Advanced flow Drop-in`, lines 362–372.
- Advanced optional import, conditional issuer and incomplete requests: raw lines 374–682.
- Redirect response and test-refund limit: raw lines 684–706.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-finland-online-banking]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/finland-online-banking/web-drop-in/2026-09-15|Online banking Finland Web Drop-in, captured 2026-09-15]]
