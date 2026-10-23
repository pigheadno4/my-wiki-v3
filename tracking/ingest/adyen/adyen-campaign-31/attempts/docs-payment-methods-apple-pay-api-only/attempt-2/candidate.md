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
- After the shopper's Apple Pay authorization, the guide offers two **different decryption paths**. For **Adyen-managed decryption**, the merchant stringifies/Base64-encodes the framework `paymentData` and sends `paymentMethod.type: applepay` with `applePayToken` from the **server** to `/payments` (this page, raw lines 133–164). For **merchant-managed decryption**, the linked [[raw/adyen/docs/payment-methods/apple-pay/api-only/apple-pay-token-decryption/2026-09-15|token-decryption guide]] requires a merchant-owned Apple Pay certificate, Apple Developer account, PCI compliance and API-only integration; after local decryption its customer-initiated `/payments` example uses `scheme` card details and applicable `mpiData`, **not** `applePayToken` (related raw lines 693–767). That guide also directs a duplicate `transactionId` check before crediting (related raw lines 710–717). These are distinct request shapes, and neither snippet is a complete safe decryption implementation. The primary page's API examples use a Checkout test endpoint and language-library-specific versions; its `Authorised` JSON is illustrative.
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

## Related raw API references

- [[raw/adyen/docs/payment-methods/apple-pay/api-only/apple-pay-token-decryption/2026-09-15|Apple Pay token-decryption guide]] — cited sections distinguish Adyen-managed encoded-token submission from PCI-qualified merchant decryption and decrypted-card requests; this is related authority, not this page's pinned raw source.

## Raw Sources

- [[raw/adyen/docs/payment-methods/apple-pay/api-only/2026-09-15|Apple Pay API-only guide — captured 2026-09-15]]
