---
title: "Vipps Web Drop-in"
type: source
date_ingested: 2026-10-26
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/vipps/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/vipps/web-drop-in/2026-09-15.md"
tags: [adyen, vipps, web-drop-in, redirect, online-payments]
---

## Overview

This 2026-09-15 guide adds Vipps to an existing Adyen Web Drop-in integration, with separate Sessions and Advanced server-side instructions. It documents request additions, optional import, redirect handling and test/live setup. It does not establish current merchant eligibility or a completed payment. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions:** requires an existing Web Drop-in Sessions flow, Checkout API v68 or later, redirect handling for `action.type: redirect`, and Vipps added in Customer Area. Its `/sessions` table describes an optional `shopperStatement` shown in the Vipps app, falling back to the payment `reference` when omitted; Vipps has a stated minimum `amount.value` of 100 minor units (1.00 NOK). The request example uses NOK/NO and a custom-scheme `returnUrl` even though the guide is for Web Drop-in; it is an example, not a universal Web return URL prescription. (raw lines 25–68)
- **Optional browser import:** individual method import for tree shaking may include `Vipps` alongside `AdyenCheckout` and `Dropin`; this is explicitly optional in both flows. (raw lines 70–80, 124–134)
- **Advanced:** requires existing Web Drop-in Advanced flow, redirect handling and Customer Area addition. Its `/payments` table describes optional `paymentMethod.telephoneNumber` to prefill the Vipps-hosted page, `shopperStatement` with the same reference fallback, `channel`, and the 100-minor-unit minimum. The example uses `channel: Web`, NOK and a web return URL. Its `RedirectShopper` response with a GET redirect is an intermediate handoff, not final authorization or settlement. The Advanced integration-type link retains an unresolved encoded `getParameter('platform')` template even though the row names Web Drop-in. (raw lines 112–188)
- **Test and live boundary:** test instructions require the Vipps test app, merchant-account addition in the test Customer Area, a payment request and shopper authorization from an app notification. Live acceptance requires a separate request in the live Customer Area; after addition, the guide calls for low-amount live tests, an `AUTHORISATION` webhook carrying status on the merchant server, and a payment-list check. App authorization and a redirect response are distinct from server-side payment status. (raw lines 82–110, 190–218)

## Detail locators

- Sessions prerequisites, statement fallback, minimum and request example: raw lines 29–68.
- Optional `Vipps` import: raw lines 70–80 and 124–134.
- Advanced prerequisite-template issue, optional request fields and redirect-response example: raw lines 116–188. The `channel` and `amount.value` links in the `/payments` table point to `/paymentMethods` reference anchors; verify the API reference before using those locators.
- Test-app credentials and separate live Customer Area request/webhook checks: raw lines 82–110 and 190–218.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-vipps]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/vipps/web-drop-in/2026-09-15|Vipps Web Drop-in guide, 2026-09-15 snapshot]]
