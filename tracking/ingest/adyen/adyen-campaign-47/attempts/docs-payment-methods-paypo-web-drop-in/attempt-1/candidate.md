---
title: "Adyen PayPo Web Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypo/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/paypo/web-drop-in/2026-09-15.md"
tags: [adyen, paypo, web, drop-in, redirect, capture, online-payments]
---

## Overview

This captured [[adyen]] guide adds PayPo to an existing Web Drop-in integration. It separates Sessions and Advanced flows, gives method-specific request fields and redirect handling, and repeats PayPo's offer, authorization, full-capture and funding timing. It is an add-on to the linked base [[adyen-online-payments]] flows, not proof of current account enablement or an executed payment.

## Key takeaways

- **Prerequisites and request fields:** Sessions requires an existing Web Drop-in Sessions flow, Checkout API v68 or later, and PayPo added in Customer Area. Its `/sessions` table marks shopper first/last name and email required, while billing and delivery addresses have blank Required cells. Advanced requires an existing Web Drop-in Advanced flow, `redirect` action handling, and PayPo setup; its `/payments` table additionally marks `paymentMethod.type: paypo` required, with the same shopper/address distinction. Examples use PL/PLN and amount 1000; they do not establish a full eligibility matrix (raw lines 25–48, 451–487).
- **Redirect and optional import:** Advanced's example response has `resultCode: RedirectShopper` and a PayPo redirect `action`, an intermediate action rather than final authorization. Either flow may optionally import `Redirect` with Adyen Web/Drop-in for tree shaking; optional import is a performance choice, not a payment prerequisite (raw lines 423–433, 463–473, 859–873).
- **Offer, repayment and capture:** When created but not yet authorized, the PayPo offer/link lasts **up to 72 hours**. Shopper acceptance changes status to `Authorised`; the shopper's **30-day** PayPo payment term begins at authorization rather than capture. The merchant still must capture the authorized payment, and **only full-amount capture** is possible. Automatic capture can be configured at live-method setup and executes immediately after authorization. The guide says the merchant is funded the full amount after capture without waiting for shopper repayment to PayPo; this is the page's stated lifecycle, not evidence that a particular settlement occurred (raw lines 391–405, repeated 875–889).
- **Testing and live gate:** Test instructions give specific first/last-name and email values plus PayPo verification code `123456` after redirect, with test status in Customer Area. Live acceptance requires submitting a PayPo request in live Customer Area (raw lines 435–449, repeated 907–921).
- **Example/link cautions:** The Sessions curl example uses an Android-style custom-scheme `returnUrl` despite this Web guide, and both Sessions and Advanced curl samples have `-X POST` without a shell continuation before `-d`. The Advanced base-integration URL embeds an unresolved `{{getParameter('platform')}}` template. Treat those snippets/link as captured documentation defects, not copy-ready setup (raw lines 54–74, 455–460, 491–500).

## Detail locators

- Sessions prerequisites, fields and examples: pinned raw lines 25–389.
- Sessions capture, optional import and test/live: pinned raw lines 391–449.
- Advanced prerequisites, optional import, fields and examples: pinned raw lines 451–857.
- Advanced redirect action, capture and test/live: pinned raw lines 859–921.

## Related

- [[adyen-online-payments]] — online payment architecture and method routes.
- [[source-adyen-docs-payment-methods-paypo]] — captured PayPo method overview; use this guide for Web Drop-in details.

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypo/web-drop-in/2026-09-15|PayPo Web Drop-in, captured 2026-09-15]]
