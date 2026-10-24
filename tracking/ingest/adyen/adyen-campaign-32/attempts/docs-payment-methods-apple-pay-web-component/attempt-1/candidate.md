---
title: "Adyen Apple Pay Web Component"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/apple-pay/web-component"
raw_files:
  - "adyen/docs/payment-methods/apple-pay/web-component/2026-09-15.md"
tags: [adyen, apple-pay, web-components, online-payments, wallets]
---

## Overview

This [[adyen]] page, last-modified metadata 2019-09-06 and captured 2026-09-15, describes adding Apple Pay to an existing **Web Components** integration using either Sessions `/sessions` or Advanced `/payments`. It covers component setup, certificate-dependent merchant validation, browser and iframe limits, recurring configuration, testing and live-domain setup. See [[adyen-online-payments]]. It is a historical setup guide, not proof of current method availability or a completed authorization, capture or settlement. See raw lines 15–47 and 437–498.

## Key takeaways

- The prerequisite is an existing Web Components flow: Sessions for `/sessions`, Advanced for `/payments`. The page calls for Apple Pay added in Customer Area, Apple Pay set up with Adyen's or the merchant's own certificate, and the **Change payment methods** Customer Area role. The **API Clientside Encryption Payments role** is specifically for live Apple Pay processing. The two requirements tabs differ: the Sessions tab calls for allowing Apple Pay IP addresses on the server; the Advanced tab additionally specifies Apple test cards and a Sandbox tester Apple ID for Adyen TEST, an Apple Developer account even with Adyen's certificate, and domain verification for each domain when using the merchant's own certificate. See raw lines 21–47.
- On Component **v6.10.0+**, the page says Apple Pay can be offered on supported third-party browsers/devices, including Windows and Chromebooks, with code-scanning completion. Earlier-version compatibility differs: macOS Safari; iOS/iPadOS all browsers including web views; no non-Apple devices. For Safari iframe embedding, Safari 17+ needs `allow="payment"`; Safari 16 or earlier requires matching iframe and top-level origin, including specified protocol, full host and port. These are browser/version conditions, not universal device eligibility. See raw lines 49–76.
- With **Adyen's certificate**, this Component page says neither Sessions nor Advanced needs extra Apple Pay Component configuration. With the **merchant's own certificate**, `onValidateMerchant` is required to display the payment sheet; the merchant's server uses the validation URL to request an Apple Pay session and resolves or rejects the callback. The guide directs mounting only after `isAvailable()` resolves. Certificate setup and availability checks precede payment execution. See raw lines 101–176.
- Optional component request data covers button properties, contacts, shipping, `merchantCapabilities`, `supportedCountries`, and `recurringPaymentRequest`; the last is required for this page's recurring setup. `shippingContactEditingMode` is marked v6.13.0+. `onAuthorized` is called after shopper authorization in Apple Pay and can continue/stop the flow; it is **not** Adyen payment authorization or settlement. `onApplePayCodeClose` only signals code-window closure. See raw lines 178–232.
- Wallet Order Tracking is marked **v6.0.0+**. The guide says its callback fires after payment completion in Sessions but after `onSubmit` resolves in Advanced; order-detail failure closes the overlay while payment can still complete without a Wallet order. Its prose names `onOrderTracking` while the sample uses `onOrderTrackingRequest`, and that JavaScript-shaped sample is fenced as `swift`; treat it as illustrative, not a verified copy-ready implementation. `applePayCapabilities` is marked **v6.10.0+** and is recommended here only for product-page display decisions. See raw lines 271–343.
- Apple Pay recurring tokenization is described for **v5.39.0+**. The page strongly recommends explicit shopper permission and transparency about schedule/amount, requires `recurringPaymentRequest` in Apple Pay configuration, then sends token creation and later payment handling to [[adyen-tokenization]]. Its v6 example omits a comma in `new ApplePay(checkout {`; sample dates and URLs are illustrative. A recurring request does not prove token creation or future charges. See raw lines 345–427.
- For live setup with **Adyen's certificate**, the page calls for an accessible, unprotected, unredirected domain-association file with `Content-Type: text/plain` at the specified `/.well-known/` path on every domain including subdomains, live Customer Area setup, and generic Apple Pay domain configuration. Domain edits require the Change payment methods role; scheme-specific Apple Pay variants are outside that domain-edit flow. Both certificate paths call for Apple IP access and `out.adyen.com`; the guide warns DNS-resolved IP allow lists can become stale. The own-certificate path points to a separate Apple Developer merchant-identifier setup. These are steps, not evidence of completed verification or live payments. See raw lines 437–498.

## Detail locators

- **Flow-specific requirement tables and Safari/device compatibility:** raw lines 21–76.
- **Sessions/Advanced certificate callback, mounting, optional request fields and events:** raw lines 78–269. The v6 and v5 mount examples use `applepay` despite naming the instance `applepayComponent` at raw lines 241–269.
- **Order tracking, capabilities and versioned recurring configuration:** raw lines 271–427.
- **Test and live certificate/domain/firewall setup:** raw lines 429–498.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-apple-pay]]
- [[source-adyen-docs-payment-methods-apple-pay-apple-pay-certificate]]
- [[source-adyen-docs-payment-methods-apple-pay-handle-apple-pay-errors]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/apple-pay/web-component/2026-09-15|Apple Pay Web Component — captured 2026-09-15]]
