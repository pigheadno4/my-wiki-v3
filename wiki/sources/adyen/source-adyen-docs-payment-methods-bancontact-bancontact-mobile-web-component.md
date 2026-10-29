---
title: "Bancontact Mobile Web Component | Adyen Docs"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/bancontact/bancontact-mobile/web-component"
raw_files:
  - "adyen/docs/payment-methods/bancontact/bancontact-mobile/web-component/2026-09-15.md"
tags: [adyen, bancontact, mobile, web-components, app-switch, qr-code, tokenization]
---

## Overview

This 2026-09-15-captured page adds **Bancontact Mobile** to an existing Web Components integration. The Component presents a QR code on desktop, switches to the Bancontact app on mobile with a QR fallback if switching fails, and offers both QR and an app-switch button on tablet. It is separate from Bancontact card. The source metadata says `last_modified` 2019-09-06 even though the body includes Web Components v6 and Checkout v72 examples, so that metadata is not a reliable date for every instruction in this captured page (raw lines 5–25, 39–45, 143–165).

## Key takeaways

- The prerequisites are an existing Web Components integration and adding Bancontact Mobile in the test Customer Area. To receive `bcmcmobile.urlIntent` in the payment response, enable **3DS2 Additional Fields** under **Developers > Additional data > 3D Secure**. The page says no Bancontact-Mobile-specific additional fields are needed for the base `/sessions` or `/payments` request; it calls `/sessions` the default with Components v5.0.0 or later and `/payments` an additional-use-case route. The Customer Area setting conditions receipt of `urlIntent`, not a required extra request field (raw lines 27–52).
- Web Components **v6** imports `BcmcMobile` and mounts `new BcmcMobile(checkout, {type: "bcmc_mobile"})`; **v5.x.x or earlier** uses `checkout.create('bcmc_mobile')`. These snippets are version-scoped Component setup, not a payment outcome or current compatibility test (raw lines 39–45, 54–84).
- Recurring payments are a separate **Bancontact Wallet Initiated Program (WIP)** route. The page strongly recommends explicit shopper permission for future charges. WIP requires signup, eligibility and Support enablement, with transaction amount limits; the first consent transaction uses SCA, later WIP transactions do not, and the source says the issuer remains liable with no liability shift for the first transaction. Support must configure recurring tests (raw lines 86–115). This does not imply all Bancontact Mobile merchants can use recurring.
- Token creation includes `storePaymentMethod: true` and a shopper reference of at least three characters in `/sessions` or `/payments`. **After settlement**, the `recurring.token.created` webhook supplies `storedPaymentMethodId`; the server must receive token lifecycle events. Later `/payments` use that ID and shopper reference with `ContAuth` plus `Subscription` or `UnscheduledCardOnFile`. The v72 TEST and server-library snippets are examples only (raw lines 116–165, 168–480).
- The page expressly says Bancontact Mobile has **no test platform** and recommends a EUR 0.01 live penny test. It also documents test Customer Area setup and `checkout-test` recurring examples. Preserve that source-level no-platform versus TEST-example tension; neither those snippets nor the historical penny-test recommendation prove a live test, current eligibility or successful payment (raw lines 31–37, 147–165, 482–486).

## Detail locators

- Bancontact Mobile device behavior and Web Components prerequisite: raw lines 15–37.
- v6 import, base API reference and versioned mounting: raw lines 39–84.
- WIP consent/eligibility/SCA, token creation and subsequent recurring request: raw lines 86–165.
- Language-specific TEST recurring request examples: raw lines 168–480.
- No test platform and historical live penny-test recommendation: raw lines 482–486.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-bancontact|Bancontact card/mobile overview]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/bancontact/bancontact-mobile/web-component/2026-09-15|Bancontact Mobile Web Component, fetched 2026-09-15]]
