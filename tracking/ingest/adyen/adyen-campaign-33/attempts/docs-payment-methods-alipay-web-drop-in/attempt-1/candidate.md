---
title: "Adyen Alipay Web Drop-in"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alipay/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/alipay/web-drop-in/2026-09-15.md"
tags: [adyen, alipay, web, drop-in, online-payments]
---

## Overview

This [[adyen]] guide, modified and captured 2026-09-15, describes Alipay-specific additions to an **existing Web Drop-in** integration under Sessions or Advanced. It does not replace the main flow's request, client, redirect or outcome handling. See [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-alipay|Alipay overview]] for the separate dated outside-China processing boundary. This page's setup and test instructions are not proof of current merchant eligibility, successful return, authorization, capture or settlement. See primary raw lines 15–36 and 74–120.

## Key takeaways

- **Sessions:** the existing Web Drop-in integration must use Sessions and **Checkout API v68 or later**, handle `action.type: redirect`, and have Alipay added in Customer Area. The guide says there are no *additional Alipay-specific* `/sessions` parameters or Drop-in configuration parameters. The base Sessions request and redirect flow remain governed by the main integration. The v68+ gate appears in the Sessions requirements table only; the Advanced table does not state a Checkout API minimum. See raw lines 23–42, 56–60 and 74–84.
- **Advanced:** the existing Web Drop-in Advanced flow must handle `action.type: redirect` and have Alipay added in Customer Area. It says there are no *additional Alipay-specific* `/payments` parameters or configuration parameters; this is not permission to omit base request fields. Its integration-type link has an unresolved encoded `{{getParameter('platform')}}` value, while the redirect and optional-import links explicitly use Web. Read the text requirement and resolved Web links rather than relying on the templated URL. See raw lines 74–108.
- Both branches call the individual-method import optional for tree shaking and say to include `Redirect`, but the displayed import snippet is `import { AdyenCheckout, Dropin, Alipay } from '@adyen/adyen-web';`. The prose and code name different imports. Do not treat the snippet alone as a verified recipe for this version. See raw lines 44–54 and 86–96.
- Both branches recommend **live penny tests** with an Alipay wallet/card and checking those payments in the **live** Customer Area. They state that a request for Alipay in live Customer Area is needed before live acceptance. This page does not give a separate TEST-mode procedure or webhook/final-status instruction, and a submitted request or visible test payment does not prove live enablement, authorization, capture or settlement. See raw lines 62–72 and 110–120.

## Detail locators

- **Sessions prerequisite, v68+ gate, redirect and no-extra-field statements:** raw lines 23–42, 56–60.
- **Optional import prose/snippet conflict:** raw lines 44–54, 86–96.
- **Advanced prerequisites, unresolved URL and no-extra-field statements:** raw lines 74–108.
- **Live penny-test recommendation and Customer Area request:** raw lines 62–72, 110–120.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-alipay]]
- [[adyen-payment-testing]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/alipay/web-drop-in/2026-09-15|Alipay Web Drop-in — captured 2026-09-15]]
