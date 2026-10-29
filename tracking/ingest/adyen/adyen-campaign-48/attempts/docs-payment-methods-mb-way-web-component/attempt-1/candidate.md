---
title: "Adyen MB WAY Web Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/mb-way/web-component"
raw_files:
  - "adyen/docs/payment-methods/mb-way/web-component/2026-09-15.md"
tags: [adyen, mb-way, web-component, sessions, advanced-flow, online-payments]
---

## Overview

This 2026-09-15-captured Adyen guide adds MB WAY to an existing Web Components integration. It separates Sessions and Advanced server-side flows, then describes an optional mobile App2App switch within the Advanced section. It is a method-specific supplement to [[adyen-online-payments]]; the captured examples do not prove current merchant enablement or payment completion. [[adyen]]

## Key takeaways

- **Sessions flow:** Start with an existing Sessions-flow Web Components integration, Checkout API v68 or later, and MB WAY added in Customer Area. The method-specific `/sessions` table requires `shopperStatement`, the bank-statement text. Import `MBWay` from `@adyen/adyen-web`, mount the component, and add no MB WAY-specific configuration. The PT/EUR, amount 1000, and app-scheme `returnUrl` in the sample are example values, not general eligibility or a Web return-URL rule. [Raw: lines 25–99]
- **Advanced flow:** Start with an existing Advanced-flow Web Components integration that handles an additional `action.type: await`, and add MB WAY in Customer Area. Import and mount `MBWay`. The method-specific `/payments` table requires `paymentMethod.type: mbway` and `paymentMethod.telephoneNumber`; `shopperStatement` is listed without a required mark. The example's EUR amount and HTTPS `returnUrl` are illustrations. [Raw: lines 123–195]
- **Waiting state:** The ordinary Advanced response is shown with `resultCode: Pending` and an `await` action. Display the waiting screen while the shopper completes payment in the MB WAY app; `Pending` is not final authorization. The page does not provide a definitive final-status callback or capture recipe, so follow the base flow's result handling rather than treating the initial response as success. [Raw: lines 197–213]
- **Optional mobile App2App switch:** The Advanced-flow section says an iOS or Android `channel` plus an app `returnUrl` can omit manual phone-number entry and produce an MB WAY deep link in `action.url`; missing `channel` or `Web` selects the standard phone-number flow. Redirect to the returned action URL and handle the return to the supplied app URL. This mobile variant is not a blanket omission of `telephoneNumber` for the standard Web request. The sample shows `Pending` with `action.type: await` and a URL; use the returned action rather than assuming every response has exactly that shape. [Raw: lines 216–271]
- **Test/live boundary:** The guide says any telephone number can be used for testing, with test payment status checked in test Customer Area. For live acceptance, add MB WAY in the live Customer Area. Its documented `shopperStatement` suffixes `-c1`, `-c3`, and `-c5` trigger Authorised, Pending, and Refused test `resultCode` values; this is a test fixture, not a live-payment guarantee. [Raw: lines 102–121, 273–292]

> [!WARNING] Sample request formatting
> Both shown curl requests place `-X POST` on a line without a continuation before `-d` (raw lines 50–65 and 176–195). They are documentation illustrations, not shell-ready copy-paste commands. The page's Sessions test section also refers to a `/payments` request for result-code triggers; preserve that endpoint wording rather than inferring a Sessions-specific trigger contract.

## Detail locators

- Sessions prerequisites, required `shopperStatement`, import/mount and no extra configuration: pinned raw lines 25–99.
- Advanced prerequisites, method-specific fields and pending/await response: pinned raw lines 123–213.
- Optional iOS/Android App2App channel, deep link and return: pinned raw lines 216–271.
- Test/live setup and result-code suffixes: pinned raw lines 102–121 and 273–292.

## Related

- [[adyen-online-payments]] — provider integration and method routes.
- [[source-adyen-docs-payment-methods-mb-way]] — approved overview for distinct Web/App2App shopper journeys and PT/EUR method capability context.

## Raw Sources

- [[raw/adyen/docs/payment-methods/mb-way/web-component/2026-09-15|MB WAY Web Component guide, captured 2026-09-15]]
