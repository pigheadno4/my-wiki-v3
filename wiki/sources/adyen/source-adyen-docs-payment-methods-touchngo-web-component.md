---
title: "Adyen Touch 'n Go Web Component guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/touchngo/web-component"
raw_files:
  - "adyen/docs/payment-methods/touchngo/web-component/2026-09-15.md"
tags: [adyen, touchngo, web, component, redirect]
---

## Overview

This [[adyen]] **Touch 'n Go Web Components** add-on guide starts from an existing Web Components integration, offers separate **Sessions** and **Advanced** server-side prerequisites, and gives different Component construction snippets for **v6.0.0 or later** and **v5.x.x or earlier**. It was recorded as last modified in 2019 and captured in 2026. The page does not document shopper redirect/return processing or a final webhook condition; linked Webhooks and integration guides are navigation, while Customer Area lookup and Support contact do not prove payment outcome or current enablement. [[adyen-online-payments]]

## Key takeaways

- **Flow-specific setup:** The Sessions tab requires an existing Sessions Web Components integration; the Advanced tab requires an existing Advanced Web Components integration. Both direct the merchant to contact Adyen Support to add Touch 'n Go in Customer Area. The page separately says Support must add it in **live** Customer Area before live acceptance. A contact request is not evidence of approval. See raw lines 21–37 and 78–82.
- **Server request scope:** It says no **additional Touch 'n Go-specific fields** are needed, while general optional fields depend on endpoint. It calls `/sessions` the default with **Components v5.0.0 or later**, and `/payments` an additional-use-case path. These are Web Components and endpoint descriptions, not a Checkout API minimum or proof that base request fields can be omitted. See raw lines 39–44.
- **Versioned client snippets:** The v6.0.0-or-later example mounts `new Redirect(checkout, { type: 'touchngo' })` into a `touchngo-container` DOM element; the v5.x.x-or-earlier example uses `checkout.create('touchngo')`. The page does not show an import for `Redirect` and leaves a stray `**` after the v6 snippet, so snippets are source examples rather than verified runnable code. See raw lines 46–76.
- **Status boundary:** It points to a TEST Customer Area payment list and separately requires Support for live Customer Area addition. It links a Webhooks guide but gives no event, result-code or settlement rule here. See raw lines 78–88.

## Detail locators

- Sessions/Advanced requirements and Support setup: raw lines 21–37.
- API-reference endpoint distinctions: raw lines 39–44.
- DOM element and v6/v5 Component snippets: raw lines 46–76.
- TEST status, live setup and See also links: raw lines 78–88.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-touchngo]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/touchngo/web-component/2026-09-15|Adyen Touch 'n Go Web Component snapshot]]
