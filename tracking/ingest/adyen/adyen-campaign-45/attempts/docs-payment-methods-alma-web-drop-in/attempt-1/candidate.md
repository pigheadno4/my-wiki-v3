---
title: "Alma Web Drop-in | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alma/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/alma/web-drop-in/2026-09-15.md"
tags: [adyen, alma, web, drop-in, installments]
---

## Overview

This 2026-09-15 Adyen Docs page gives **Alma-specific additions** to an existing Web Drop-in integration for Sessions and Advanced server-side flows. The linked Alma overview describes a France/EUR, three- or four-instalment BNPL redirect method; this child gives request and import details, not a live-eligibility guarantee. See [[adyen-online-payments]], [[source-adyen-docs-payment-methods-alma]] and [[adyen]].

## Key takeaways

- Sessions requires an existing Web Drop-in Sessions flow, **Checkout API v68 or later**, and Alma added in Customer Area (raw lines 25–35). Its added `/sessions` fields are telephone number, shopper email, billing address and delivery address; the table's **Required** cells are blank, so the child does not mark these Alma additions mandatory (lines 39–48). The FR/EUR v71 TEST curl sample uses an app-style `adyencheckout://your.package.name` return URL despite this being a Web guide (lines 50–84); verify a Web-appropriate return URL in the base integration. It also lacks a shell continuation between `-X POST` and `-d` (lines 53–58), so it is not copy-ready.
- In both flows, importing individual Adyen Web methods is **optional** for tree shaking; the page's example includes `Redirect` with `AdyenCheckout` and `Dropin` (Sessions lines 86–96; Advanced lines 118–128). The page does not specify a Web SDK version.
- Advanced requires an existing Web Drop-in Advanced flow, redirect action handling and Alma added in Customer Area (lines 106–116). Its added `/payments` table again leaves phone, email, billing/delivery addresses unmarked as required. `additionalData.alma.installments_count` is also optional: set **3** or **4** to determine instalments, or omit it to let the shopper choose (lines 130–142). The FR/EUR v72 TEST example sets `alma.installments_count: 4`, which is an example, not a mandatory count or proof of financing approval (lines 144–182). That curl also lacks a continuation between `-X POST` and `-d` (lines 147–152). The Advanced base-integration link includes an unresolved encoded `{{getParameter('platform')}}` placeholder at line 114; the adjacent explicit Web links are safer navigation.
- Advanced's sample initial response is `RedirectShopper` with a redirect `action` (lines 184–198), not a final authorisation, capture or settlement result. The page links the base integration for action handling and gives no Alma-specific capture/refund or final webhook path. Product and lifecycle features are separately scoped in the linked overview.
- The test/live sections direct checking Alma test payments in Customer Area and require submitting an Alma request in live Customer Area before accepting live payments (lines 98–104 and 200–206). Neither instruction proves a particular merchant has live enablement or a successful transaction.

## Detail locators

- Page scope and Sessions requirements: raw lines 15–35.
- Sessions added field table and FR/EUR v71 TEST example: lines 39–84; app-style return URL at line 64, shell continuation at lines 53–58.
- Sessions optional import and test/live: lines 86–104.
- Advanced requirements, optional import and added field/installment table: lines 106–142; unresolved base-guide template at line 114.
- Advanced FR/EUR v72 TEST request and redirect response: lines 144–198; shell continuation at lines 147–152.
- Advanced test/live: lines 200–206.
- Related Alma overview France/EUR and three/four instalments: `raw/adyen/docs/payment-methods/alma/2026-09-15.md` lines 23–29.

## Related

- [[adyen-online-payments]] — provider online-payment architecture.
- [[source-adyen-docs-payment-methods-alma]] — product/country/currency and lifecycle overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/alma/web-drop-in/2026-09-15|2026-09-15 Alma Web Drop-in Sessions and Advanced add-on]]
