---
title: "Adyen Apple Pay API-only integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/apple-pay/api-only"
raw_files:
  - "adyen/docs/payment-methods/apple-pay/api-only/2026-09-15.md"
tags: [adyen, apple-pay, api-only, online-payments, certificates, wallets]
---

## Overview

This [[adyen]] guide, last modified 2025-03-05 and captured 2026-09-15, describes adding Apple Pay to an existing **Advanced-flow API-only** online integration with a merchant-built payment form. It covers web and iOS app channels, certificate choice, merchant validation, Apple Pay token handoff and result display. See [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-apple-pay|Apple Pay overview]]. The steps and sample `Authorised` response are not evidence of current country/account eligibility, live payment authorization, capture or settlement. See raw lines 15–30 and 131–466.

## Key takeaways

- The page says Adyen did **not** support China UnionPay cards through Apple Pay in this dated snapshot and says not to send Apple `merchantCapability: supportsEMV`. Its prerequisites are an existing Advanced API-only flow, Customer Area **Change payment methods** role, Apple Pay added in Customer Area, and a certificate. The **API Clientside Encryption Payments role** is specifically stated for *live* Apple Pay processing. It offers Adyen's certificate for web, while mobile integrations use the merchant's own Apple Developer account and certificate. These are page-specific conditions, not a current eligibility or compliance determination. See raw lines 19–32 and 487–491.
- The server `/paymentMethods` request uses supported `countryCode` and currency and sets `channel: Web` for Safari or `iOS` for in-app payments. The response can identify `applepay`; `merchantId` and `merchantName` are needed for the Adyen-certificate **web** validation route. Shopper Touch ID/Face ID or companion-device confirmation is Apple Pay authentication, separate from Adyen's payment result. See raw lines 34–76.
- Apple Pay **session validation is web-only**, triggered by `onvalidatemerchant` and completed through `completeMerchantValidation`. With Adyen's certificate, the merchant calls `/applePay/sessions` using the returned name/ID and a registered domain matching `window.location.hostname`, then decodes the returned Base64 data. With its own certificate, the merchant obtains an Apple session. The guide states the session data expires after **five minutes**. In-app payments skip this web validation step. See raw lines 78–129.
- After the shopper's Apple Pay authorization, the guide points to Adyen-managed token decryption or merchant-managed decryption, allowing the latter only if PCI-compliant. It then instructs the merchant to stringify/Base64-encode the entire framework `paymentData` and send `paymentMethod.type: applepay` with `applePayToken` from the **server** to `/payments`. The text is a route, not a full safe decryption implementation; consult the separate token-decryption guide before choosing ownership. The API examples use a Checkout test endpoint and language-library-specific versions; the shown `Authorised` JSON is illustrative. See raw lines 131–164 and 166–462.
- The page names `Authorised` and `Refused` as Apple Pay `resultCode` cases for shopper messaging, with a different-method retry recommendation on refusal. It points to separate token creation and reuse guides for recurring payments. Authentication, API response and displayed result do not themselves show capture or settlement. See raw lines 464–477.
- Its live Adyen-certificate **web** setup requires an externally accessible, unprotected, unredirected domain-association file at the stated `/.well-known/` path with `Content-Type: text/plain`, on each domain including subdomains, followed by live Customer Area setup. Domain editing requires the Change payment methods role and applies only to generic Apple Pay, not scheme-specific variants. Both certificate routes mention Apple IP and `out.adyen.com` firewall access; the page warns that resolved IP allow-listing can break when addresses change. These are configuration instructions, not evidence the domain was verified. See raw lines 487–550.

## Detail locators

- **Versioned snapshot, API-only prerequisites, certificate/channel scope and China UnionPay limit:** raw lines 15–32.
- **Apple Pay method lookup, channel and returned configuration:** raw lines 34–76.
- **Web-only session validation, own-versus-Adyen certificate and five-minute limit:** raw lines 78–129.
- **Apple Pay token/decryption boundary, server `/payments` and versioned TEST examples:** raw lines 131–462. The Go snippet says library v10.4.0 but imports `/v9/` paths at raw lines 323–328; do not treat snippets as verified build recipes.
- **Result codes, recurring route, test and live/domain/firewall prerequisites:** raw lines 464–550.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-apple-pay]]
- [[adyen-tokenization]]
- [[adyen-pci-dss-compliance]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/apple-pay/api-only/2026-09-15|Apple Pay API-only guide — captured 2026-09-15]]
