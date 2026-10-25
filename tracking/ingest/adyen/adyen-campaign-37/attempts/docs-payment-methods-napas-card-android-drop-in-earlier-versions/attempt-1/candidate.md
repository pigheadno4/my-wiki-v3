---
title: "Napas card Android Drop-in v4.x.x | Adyen Docs"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/napas-card/android-drop-in/earlier-versions"
raw_files:
  - "adyen/docs/payment-methods/napas-card/android-drop-in/earlier-versions/2026-09-15.md"
tags: [adyen, napas-card, vietnam, android, drop-in, earlier-versions]
---

## Overview

This [[adyen]] page documents **Napas card Android Drop-in v4.x.x** in an existing **Advanced-flow** integration. It covers VN/VND payment-method discovery, client-to-server payment handoff, redirect and `/payments/details`, plus result-code and webhook outcomes. Its v4.x.x scope is historical; the page does not establish current support or live merchant eligibility. See [[adyen-online-payments]] and [[adyen-android-sdk]].

## Key takeaways

- **Prerequisites and discovery:** The requirements call for an Advanced Android Drop-in integration and Napas card added in Customer Area. The `/paymentMethods` request uses `countryCode: VN`, `amount.currency: VND` and an amount value so Drop-in can show eligible methods. This is a documented discovery input, not a guarantee that a particular merchant/shopper sees Napas card. See raw lines 21–36.
- **Client/server redirect sequence:** Drop-in returns `paymentComponentData.paymentMethod`; the client passes it to the merchant server, which sends it in `/payments` with a `returnUrl` obtained from `RedirectComponent.getReturnUrl(context)`. The merchant passes the response `action` back to Drop-in. After the shopper returns, Drop-in provides `actionComponentData.details`, which the server sends to `/payments/details`; its `resultCode` is used to present a result and `pspReference` identifies the transaction. A redirect or app return is not itself a final authorization result. See raw lines 38–47 and 150–205.
- **Outcome boundaries:** The page lists `Authorised`, `Cancelled`, `Pending`/`Received`, and `Refused`. For `Pending` or `Received`, it says the final result is unknown and to wait for the **AUTHORISATION** webhook. If the shopper does not return, it also directs the merchant to webhooks: `AUTHORISATION` success true/false or `OFFER_CLOSED` success true for an incomplete, timed-out payment. The page's result table is the outcome authority here; the illustrated `Authorised` response is only an example. See raw lines 203–222.
- **Testing and live gate:** The page supplies test-card scenarios for success, blocked card, insufficient funds and exceeded amount, a Customer Area route for test-payment status, and a live Customer Area request before live Napas acceptance. These are historical test fixtures and setup instructions, not evidence of live execution. See raw lines 224–237.

> [!warning] Contradiction
> Despite the Napas card title and VN/VND discovery instructions, the `/payments` examples in curl, Node.js, Python and Ruby use `paymentMethod.type: momo_atm`; the redirect response example also says `paymentMethodType: momo_atm`. The page does not reconcile this MoMo type with Napas. Do not copy that type as a validated Napas identifier or treat the response as observed Napas behavior. See raw lines 15, 32–35, 62–64, 87–90, 115–118, 141–144 and 154–163.

> [!warning] Flow and example versions
> The requirement names **Advanced** Android Drop-in, while the introductory and See also links point to **Sessions** guides. The example payment call uses Checkout v68 and its later `/payments/details` example uses v72; the page does not demonstrate a single tested API-version sequence. Follow the stated v4.x.x/Advanced scope and verify the relevant base guide and API version separately. See raw lines 19, 25, 51–52, 178–185 and 239–243.

## Detail locators

- `/payments` curl and Node.js, Python, Ruby examples: raw lines 49–148. The return URL and TEST environments are examples, not a guaranteed redirect callback contract.
- Redirect action and `/payments/details` examples: raw lines 150–205. The illustrated `Authorised` response is not a live-payment result.
- Test-card values and OTP fixture: raw lines 224–233. Keep these within the page's test context; do not use them as live credentials.

## Related

- [[adyen-online-payments]] — online payment architecture and method routes.
- [[adyen-android-sdk]] — native Android versioned SDK context; its retained 5.x code baseline is separate from this v4 guide.

## Raw Sources

- [[raw/adyen/docs/payment-methods/napas-card/android-drop-in/earlier-versions/2026-09-15|Napas card Android Drop-in v4.x.x snapshot]]
