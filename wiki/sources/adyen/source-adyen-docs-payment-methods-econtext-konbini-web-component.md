---
title: "Japanese convenience stores Web Component"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/econtext-konbini/web-component"
raw_files:
  - "adyen/docs/payment-methods/econtext-konbini/web-component/2026-09-15.md"
tags: [adyen, econtext, konbini, web, components, voucher, japan]
---

## Overview

This Adyen Web Component guide, captured on 2026-09-15 and marked last modified 2020-06-12 in the raw, adds Japanese convenience-store payments to an **existing Components integration**. It covers method-specific Customer Area setup, store type/Component choices, optional personal-detail UI, and test/live voucher status. It does not itself establish current merchant eligibility, voucher redemption, or a completed payment. See [[adyen]], [[adyen-online-payments]] and the [[source-adyen-docs-payment-methods-econtext-konbini|method overview]].

## Key takeaways

- The guide requires an existing Web Components integration and **separate Customer Area additions**: `eContext Convenience Stores` for Lawson, Mini Stop, Family Mart and Seicomart; `eContext PayEasy ATM` for Pay-easy ATM; `eContext PayEasy Online Banking` for Pay-easy online banking; and `eContext 7Eleven` for 7-Eleven. The overview additionally marks **7-Eleven as local-entity-required**; Customer Area selection alone does not establish that eligibility (child raw lines 21–29; overview raw lines 23–30).
- The API reference says **no additional Japanese convenience-store fields** are needed beyond the integrated endpoint's base request; it directs to `/sessions` for the default Components v5.0.0-or-later path and `/payments` for an additional use case. This is relative to the existing integration, not a claim that base request or shopper data requirements vanish (raw lines 39–44).
- The Component section distinguishes `econtext_seven_eleven` (**7-Eleven redirect to voucher page**) from `econtext_stores` (**Lawson/Mini Stop/Family Mart/Seicomart native voucher**). Its examples mount `econtext_stores`: Web Components **v6** imports `AdyenCheckout` and `Econtext` and constructs `new Econtext(checkout)`; **v5.x.x or earlier** uses `checkout.create('econtext_stores')`. The page does not demonstrate a Pay-easy-specific Component type in these examples (raw lines 31–37, 46–83).
- Optional `personalDetailsRequired: false`, added in **v5.2.0**, hides shopper name, email and telephone input fields; its default is **true**. This is a UI visibility option, not a waiver of the method overview's stated shopper full-name, phone and email requirement. The sample configuration line contains rendered HTML markup inside a JavaScript comment; use the parameter description rather than treating the snippet as a validated copy-ready recipe (raw lines 85–120; overview raw lines 32–40).
- **Testing conflict:** the page says 7-Eleven voucher payments can **only be tested in the live environment**, with Support setup for penny testing, but its later econtext-simulator instructions include selecting **7-Eleven**. Preserve both source statements; the latter does not resolve whether a test-environment 7-Eleven voucher payment is supported. The simulator steps use an acquirer reference constructed from a `pspReference` in an `AUTHORISATION` webhook and say to wait 15 minutes for a webhook; this is a test procedure, not a payment-finality guarantee. The raw includes simulator credentials; use the pinned raw for those test-only details rather than reproducing them here (raw lines 122–150).
- Pending/expired vouchers are listed under **test Customer Area > Payments > Offers**, while paid vouchers appear under **Payment list**. Live acceptance requires a request to add 7-Eleven or other Japanese convenience stores in **live Customer Area**. Voucher issue remains distinct from the later in-store cash payment described by the overview (child raw lines 152–157; overview raw lines 32–42).

## Detail locators

- Existing Components integration and method-specific Customer Area setup: raw lines 15–29.
- v6 import, endpoint scope and store-specific type/presentation: raw lines 31–53.
- Component mounting by v6 versus v5.x.x/earlier: raw lines 55–83.
- Optional personal-detail UI and configuration examples: raw lines 85–120.
- Live-only 7-Eleven test statement, simulator steps and conflicting 7-Eleven option: raw lines 122–150.
- Pending/expired versus paid test Customer Area status and live request: raw lines 152–157.
- Method-level local-entity condition, shopper data, later cash payment and default offer expiry: [[source-adyen-docs-payment-methods-econtext-konbini]] and its pinned raw lines 23–47; this entry's raw_files remains child-only.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-econtext-konbini]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/econtext-konbini/web-component/2026-09-15|Japanese convenience stores Web Component guide, captured 2026-09-15]]
