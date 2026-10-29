---
title: "Adyen Cash App Afterpay Android Redirect Component v4.x.x"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cash-app-afterpay/android-component/earlier-versions"
raw_files:
  - "adyen/docs/payment-methods/cash-app-afterpay/android-component/earlier-versions/2026-09-15.md"
tags: [adyen, cash-app-afterpay, android, redirect-component, earlier-versions, capture]
---

## Overview

This 2026-09-15 capture is titled Cash App Afterpay Redirect Component **v4.x.x**. It describes adding the method to an existing Advanced Android Components integration, with US/USD discovery, server-side payment request, Redirect Component return, outcome handling, capture/refund limits and test/live setup. Its historical version label and examples do not establish current SDK behavior, merchant entitlement or executed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- The requirements call for an existing **Advanced flow Android Components** integration and Cash App Afterpay added in Customer Area. For `/paymentMethods`, the page pairs US with USD and says the response type is `afterpaytouch_US`. The form should collect full name, email, billing and delivery addresses for risk checks and purchased-item data for the payment request (pinned raw lines 15–56).
- From the server, `/payments` uses `paymentMethod.type=afterpaytouch_US`, shopper details, lineItems and a return URL. The page says to obtain that URL from `RedirectComponent.getReturnUrl(context)`, although its prose spells the request field `returnURL` while examples use `returnUrl` (lines 57–135). The response's redirect `action` is passed to the Android client to initialize Redirect Component (lines 532–548).
- When the shopper returns, the server POSTs `/payments/details` with `actionComponentData.details`; `resultCode` is used to present the outcome and `pspReference` identifies the transaction. `Pending` or `Received` may take minutes or hours and requires the AUTHORISATION webhook for finality. If the shopper does not return, wait for AUTHORISATION success true/false webhooks (lines 550–603).
- Capture is automatic or manual according to merchant account configuration. Delaying capture needs a capture delay or manual capture; partial capture needs manual capture. Capture must occur within **13 days** of authorisation or Cash App Afterpay cancels and refunds the first installment charged at authorisation. Test authorisations expire in **one day**. A first partial capture normally cancels the unclaimed balance, except when multiple partial captures are enabled through Support; each multiple partial capture creates a new invoice (lines 605–624).
- An uncaptured payment can be cancelled; after capture, returning funds requires a refund. Capture and refund requests take full/partial `amount.value` and optional lineItems. The negative line-item discount example calls itself “1 USD” on Item #2 but quantity 2 at -100 minor units implies one USD per unit and two USD total, consistent with total 800 from 1000; its ellipsis and missing comma make it illustrative, not valid JSON (lines 626–671).
- Testing uses a US Afterpay sandbox shopper account and test card. The page says to request Cash App Afterpay in the live Customer Area before live acceptance (lines 673–691).

> [!warning] Flow links and field spelling
> The requirements specify Advanced Android Components, but the Redirect Component links in the introduction, redirect section and See also point to Sessions-flow guidance (raw lines 19, 32, 552, 695). The prose calls the payment field `returnURL`; the example JSON uses `returnUrl` (lines 75, 99). Verify the correct Advanced flow redirect setup and request schema before implementing this older guide.

## Detail locators

- Identity, requirements and US/USD method discovery: pinned raw lines 15–56.
- Server payment request and language examples: lines 57–528; redirect action, return/details and result webhooks: lines 529–603.
- Capture window, partial-capture exception and cancellation/refunds: lines 605–636.
- Discount illustration and sandbox/live setup: lines 637–697.

## Related

- [[adyen-online-payments]] — provider online-payments concept
- [[source-adyen-docs-payment-methods-cash-app-afterpay]] — method overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/cash-app-afterpay/android-component/earlier-versions/2026-09-15|Cash App Afterpay Android Redirect Component v4.x.x guide, captured 2026-09-15]]
