---
title: "Online banking Czech Republic Web Drop-in"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/online-banking-czech-republic/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/online-banking-czech-republic/web-drop-in/2026-09-15.md"
tags: [adyen, online-banking-czech-republic, web, drop-in, redirect]
---

## Overview

This 2026-09-15-captured Adyen guide adds **Online banking Czech Republic to an existing Web Drop-in integration** through Sessions or Advanced server-side flow. It lists redirect and Customer Area prerequisites, optional `OnlineBankingCZ` import, and test/live instructions. It does not specify a completed-payment result. See [[adyen]], [[adyen-online-payments]], and the method overview [[source-adyen-docs-payment-methods-online-banking-czech-republic]] for CZ/CZK shopper flow and capability context.

## Key takeaways

- **Sessions flow** requires existing Web Drop-in Sessions, Checkout API **v68 or later**, `action.type: redirect` handling and Online banking Czech Republic added in Customer Area (raw lines 25–36). The guide says no **additional Czech-specific** `/sessions` parameters are needed (raw lines 38–42); base integration request fields still apply.
- An optional `OnlineBankingCZ` import alongside `AdyenCheckout` and `Dropin` supports tree shaking for Web Drop-in; this is a performance choice, not a required method field or a complete Component setup (raw lines 44–54).
- **Advanced flow** requires existing Web Drop-in Advanced, redirect handling and Customer Area method addition (raw lines 66–76). Its prerequisite URL contains encoded unresolved `{{getParameter('platform')}}` rather than a concrete Web platform value; verify the actual Advanced Web Drop-in base guide. No Advanced Checkout API minimum is stated in this page.
- Advanced likewise offers optional `OnlineBankingCZ` import for tree shaking and says no **additional Czech-specific** `/payments` parameters are needed (raw lines 78–94). This is scoped to method additions; it does not mean a base `/payments` request needs no fields.
- Both flows instruct testing with real payment details and small amounts, checking test status in test Customer Area **Payments > Payment list**, and adding the method in Customer Area for live acceptance (raw lines 56–64, 96–104). A redirect action and test-status instruction are not evidence of final paid status or current merchant enablement.

## Detail locators

- Sessions requirements and no extra method fields: raw `## Sessions flow Drop-in`, lines 25–42.
- Sessions optional import and test/live instructions: raw lines 44–64.
- Advanced requirements and unresolved platform template: raw `## Advanced flow Drop-in`, lines 66–76.
- Advanced optional import, no extra method fields and test/live instructions: raw lines 78–104.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-online-banking-czech-republic]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/online-banking-czech-republic/web-drop-in/2026-09-15|Online banking Czech Republic Web Drop-in, captured 2026-09-15]]
