---
title: "Adyen Google Pay Web Component"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/google-pay/web-component"
raw_files:
  - "adyen/docs/payment-methods/google-pay/web-component/2026-09-15.md"
tags: [adyen, google-pay, web-components, wallets, online-payments]
---

## Overview

This [[adyen]] guide, captured 2026-09-15 with page metadata last modified 2019-09-06, adds Google Pay to an **existing Web Components** integration. It covers Google Pay sheet presentation, versioned Component construction, shopper availability, optional wallet/card settings, testing and live prerequisites. Its body spans Web Component v4/v5/v6 guidance despite the old metadata; interpret each version gate literally rather than treating the metadata as a current SDK release. See [[adyen-online-payments]].

## Key takeaways

- **Prerequisites and flow split:** First complete the Web Components integration, Google's Web setup and Adyen Customer Area Google Pay addition. The page calls `/sessions` the default for Components **v5.0.0+** and links `/payments` for an additional use case. It says no Google-Pay-specific fields are added to those endpoint requests. For direct `/payments` Component configuration it marks amount in minor units, currency, merchant-account country and environment as required; `nativeThreeDS: preferred` and `origin` are only for native 3DS2 cases. The Google Pay sheet lets the shopper select a card and may redirect for card-specific 3D Secure verification; sheet choice or authentication does not establish authorization/capture. See pinned raw lines 19–38 and 94–105.
- **Web version and client availability:** Preloading Google's Pay JS library is **recommended**. The page gives `new GooglePay(checkout, ...)` for Web Component **v6+** and `checkout.create('googlepay', ...)` for **v5.x.x or earlier**; the Sessions v5 example passes `googlePayConfiguration` without defining it in that no-extra-configuration branch, so the snippet is not a complete implementation. Mount only after `isAvailable()` resolves, and handle rejection. The iframe paragraph says “Drop-in” inside this Component guide; apply it only to the embedded context described, not as a new Component requirement. A successful client availability check does not prove merchant enablement or payment success. See pinned raw lines 40–157 and 253–272.
- **Optional wallet and card controls:** Component-side `configuration` overrides backend Google Pay configuration. Supplying a displayed `merchantName` also requires a Google `merchantId` and Adyen `gatewayMerchantId`; a test ID can be arbitrary, whereas live requires a Google Merchant ID. Multi-domain `authJwt` additionally requires `merchantOrigin` and Google approval. The stated default `allowedAuthMethods` is `PAN_ONLY` plus `CRYPTOGRAM_3DS`; allowed card networks derive from account settings unless overridden. Email/shipping, billing, card-type, button and transaction-display settings have their own conditions. These are configuration options, not proof of token decryption responsibility, network acceptance or live wallet eligibility. See pinned raw lines 159–242.
- **Events and conditional features:** The event table says `onClick` and post-approval `onChange`/`onSubmit` can continue or stop the flow, and `onAuthorized` exposes Google's full response for extra shopper/shipping data. It also says `displayItems` is required when Google **Authorize Payments** or **Dynamic Price Updates** is implemented; Dynamic Price Updates is confined here to the linked Express Checkout flow. The row refers to an `onAuthorize` handler, but the page's event table lists `onAuthorized`, not `onAuthorize`; do not equate those names or infer a complete Authorize Payments implementation from this page. See pinned raw lines 229–251.
- **Recurring and environment boundary:** For recurring Google Pay payments, the page routes to creating a shopper token and then using it for subsequent transactions; the linked token guides own consent and lifecycle details. TEST can use Google's test-card suite, with DPAN cases restricted here to native Android or Chrome on Android; outside the suite, real wallet cards are mapped to Adyen test cards and are not charged. Its no-suite 3DS2 test instruction limits challenge fixtures to American Express or Discover. Before live, the page lists Adyen API credential **API Clientside Encryption Payments** role, live Google Merchant ID configuration, Google production-access request and Web deployment steps; the shopper must be logged in with a valid Google Pay method for live availability. None of this snapshot proves current production approval or a live payment outcome. See pinned raw lines 274–317.

## Detail locators

- Requirements, `/sessions` versus `/payments` and conditional native 3DS2 fields: pinned raw lines 19–36 and 94–105.
- Google Pay script recommendation, iframe wording, v6/v5 construction and availability-gated mount: pinned raw lines 40–157.
- Merchant-ID/JWT dependency, wallet payment data, card auth/network defaults and transaction settings: pinned raw lines 159–242.
- Event table and `onAuthorize`/`onAuthorized` documentation gap: pinned raw lines 243–251; optional sample uses the older `checkout.create` form at lines 253–272.
- Recurring token route, TEST fixtures and LIVE setup/availability: pinned raw lines 274–317.

## Related

- [[adyen-online-payments]] — main Web client/server/webhook route.
- [[adyen-tokenization]] — shopper-token creation and later charges.
- [[adyen-3d-secure]] — authentication separated from payment authorization and capture.

## Raw Sources

- [[raw/adyen/docs/payment-methods/google-pay/web-component/2026-09-15|Google Pay Web Component guide, captured 2026-09-15]]
