---
title: "GrabPay Android Component v4.x.x integration"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/grabpay/android-component/earlier-versions"
raw_files:
  - "adyen/docs/payment-methods/grabpay/android-component/earlier-versions/2026-09-15.md"
tags: [adyen, grabpay, android, components, wallet, paylater]
---

## Overview

Adyen's GrabPay **Android Component v4.x.x** earlier-version guide (last-modified 2019-09-06; captured 2026-09-15) covers an existing **Advanced-flow Android Components** integration. The Component renders GrabPay and sends the shopper to GrabPay's webpage. This historical versioned page is not evidence of current SDK behavior, country availability, merchant eligibility, or executed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Discovery and scope:** Add GrabPay in Customer Area. For `/paymentMethods`, the page maps Malaysia to MY/MYR, Singapore to SG/SGD, and Philippines to PH/PHP, and says to select a `grabpay_XX` country-suffixed method object. The Philippines footnote excludes **GrabPay PayLater**, not GrabPay Wallet. The examples mainly use `grabpay_SG`; they do not prove merchant enablement or other market behavior. [Raw lines 26–47]
- **Wallet versus PayLater:** Wallet passes `paymentComponentState.data.paymentMethod` from Android client to server and sends it with `returnUrl`, reference and amount in server `/payments`. The return URL is obtained using `RedirectComponent.getReturnUrl(context)`. PayLater (postpaid or installment) additionally needs shopper `deliveryAddress` and `lineItems`, collected client-side and sent to the server for GrabPay risk checks. The guide recommends collecting these early for Wallet only to ease a possible future PayLater integration; it does **not** require them for Wallet. [Raw lines 49–75, 396–410]
- **Redirect and outcome:** A `/payments` example returns `RedirectShopper` and an `action.type: redirect`; pass the action to the client Redirect Component. After the shopper returns to the app, the server posts the Component's `actionComponentData.details` to `/payments/details`. Its `resultCode` and `pspReference` support shopper-facing status. `Pending` or `Received` still lack a final result; use the later `AUTHORISATION` webhook. If the shopper never returns, wait for webhooks; `OFFER_CLOSED` indicates timeout/incompletion. A redirect or example `Authorised` response is not proof of a real transaction or settlement. [Raw lines 378–394, 882–969]
- **TEST/live:** The page directs merchants to Support for test-wallet credentials, then a simulator login with a registered phone and one-time password; live acceptance needs a GrabPay request in live Customer Area. Example API calls use TEST and versioned library snippets; several say a live endpoint URL prefix is additionally needed for live. No actual credential or payment operation is evidenced here. [Raw lines 77–376, 971–980]

## Detail locators

- PayLater variants in `additionalData.paymentMethodVariant` are listed only after `/payments/details`: Wallet and PayLater values for SG/MY, Wallet values for PH. See raw lines 933–947. Treat them as response possibilities, not all enabled variants for a merchant.
- The redirect section's link to a **Sessions-flow** Android Components guide appears inside this Advanced-flow v4.x.x page; the page's own stated prerequisite remains Advanced. See raw lines 26–31, 900–904. The `/payments` examples use v68 while the `/payments/details` curl uses v72; these are example endpoint versions, not an express minimum Checkout API requirement. [Raw lines 80, 414, 909]
- `/payments/details` result table distinguishes Authorised, Cancelled, Refused, and non-final Pending/Received, with `AUTHORISATION` and `OFFER_CLOSED` webhook paths: raw lines 950–969. It does not establish capture, settlement, refund, or recurring support for this route.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/grabpay/android-component/earlier-versions/2026-09-15|GrabPay Android Component v4.x.x (2026-09-15 capture)]]
