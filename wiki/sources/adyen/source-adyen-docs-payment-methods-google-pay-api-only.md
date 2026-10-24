---
title: "Adyen Google Pay API-only integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/google-pay/api-only"
raw_files:
  - "adyen/docs/payment-methods/google-pay/api-only/2026-09-15.md"
tags: [adyen, google-pay, wallet, api-only, online-payments]
---

## Overview

This Adyen guide (last-modified metadata 2023-05-31; captured 2026-09-15) adds Google Pay to an **existing API-only checkout integration** for a merchant-built payment form. It describes Google Pay API token collection on Web or Android and an Adyen Checkout server `/payments` request. Its specified tokenization method is **PAYMENT_GATEWAY** with Adyen as gateway; it does not provide a merchant-decryption flow, merchant key instructions or a PCI-level determination. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- The stated prerequisites are adding Google Pay in Customer Area, **Checkout API v67 or later**, and integrating Google's Web or Android Pay API with `gateway: adyen` and `gatewayMerchantId` set to the merchant or company account name. Google API setup remains a separate responsibility. (raw lines 21–43)
- Show the method where Google Pay is supported. An optional `/paymentMethods` discovery request uses supported `countryCode`, `amount.currency`, and `channel: Web` or `Android`; `NL`/`EUR` are examples. A response may identify `paymentMethod.type: googlepay`; this and a displayed payment sheet do not establish a payment result or universal region/currency support. (raw lines 45–57)
- Obtain `PaymentData.token` from Google Pay and send it **from the merchant server** as `paymentMethod.type: googlepay` and `googlePayToken` in Adyen `/payments`. The guide calls for `browserInfo` if triggering 3D Secure and a `returnUrl` for a post-3DS redirect. It does not instruct the merchant to decrypt the Google token or handle Google private keys on this gateway path. (raw lines 59–69)
- A payment response can carry `Authorised` or an `action` requiring further 3DS authentication; the text names `redirect` and `threeDS2` action types. The example `RedirectShopper` response and the linked redirect guide are authentication continuation, not final authorization, capture or settlement proof. Present the eventual `/payments` or `/payments/details` result code; the table distinguishes `Authorised`, `Error` with `refusalReason`, and bank `Refused`. (raw lines 482–529)
- For recurring, the page points to creating a shopper token first and making later token payments; it does not spell out consent or recurring request contracts. TEST setup uses a Google account/wallet and either Google's test-card suite or real wallet cards mapped to Adyen test cards. The stated test-suite DPAN cases are native Android/Chrome on Android only; without the suite, Amex or Discover is specified for 3DS2 tests. These are TEST examples, not live payment proof. (raw lines 531–560)
- Before LIVE, the guide lists the **API Clientside Encryption Payments role**, associating the Google Merchant ID with the Adyen merchant account, and Google's Web/Android production-deploy steps. It says production availability also depends on a shopper logged into Google with a valid payment method. This is a dated checklist, not proof of actual merchant enablement, PCI compliance or successful processing. (raw lines 562–577)

## Example qualifications

- The curl example shows a TEST v68 endpoint and rendered `{hint:...}` placeholders inside JSON field names; those annotations are not a literal executable request. Language-library versions vary, and the Go snippet labels library v10.4.0 while importing `/v9/` paths. Verify examples against the selected SDK/API version rather than treating them as a full production implementation. (raw lines 71–100, 102–479, especially 306–312)
- The page says a 3DS response may contain `redirect` **or** `threeDS2`, while its next numbered step broadly says to redirect on any `action`. Follow the action type and linked flow rather than assuming every action is a URL redirect. (raw lines 493–518)

## Detail locators

- Prerequisites, Google gateway specification, discovery and channel: raw lines 21–57.
- Server payment handoff and versioned examples: raw lines 59–480.
- Results and 3DS continuation: raw lines 482–529.
- Recurring, TEST and LIVE conditions: raw lines 531–577.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[adyen-3d-secure]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/google-pay/api-only/2026-09-15|Adyen Google Pay API-only guide, 2026-09-15 snapshot]]
