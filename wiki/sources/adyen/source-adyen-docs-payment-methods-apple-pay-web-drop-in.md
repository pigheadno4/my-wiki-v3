---
title: "Adyen Apple Pay Web Drop-in (historical guide)"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/apple-pay/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/apple-pay/web-drop-in/2026-09-15.md"
tags: [adyen, apple-pay, web, drop-in, online-payments, historical]
---

## Overview

This [[adyen]] guide adds Apple Pay to an **existing Web Drop-in integration**. It separates **Sessions `/sessions`** and **Advanced `/payments`** setup (raw lines 15–47), and belongs under [[adyen-online-payments]]. The page metadata says last modified **2021-12-17**, yet its captured 2026-09-15 body includes v6.10.0, v6.13.0 and a domain-association file named 2026 (raw lines 11, 29–47, 211, 409); treat its versioned instructions as this snapshot, not a consistent 2021 release or proof of present support.

## Key takeaways

- Both endpoint tabs require an existing matching Web Drop-in flow, Apple Pay added in Customer Area, and own or Adyen Apple Pay certificate setup. The page names **Change payment methods** as the Customer Area role and **API Clientside Encryption Payments** as the API credential role for live processing (raw lines 21–47, 403–405). The Sessions tab calls for server allowance of Apple Pay IP addresses; the Advanced tab additionally specifies Apple test cards plus Sandbox tester Apple ID in Adyen TEST, an Apple Developer account even with Adyen's certificate, and per-domain Apple verification when using the merchant's own certificate (raw lines 34–47). These tab-specific prerequisites should not be collapsed into one undocumented universal procedure.
- For Safari iframe display, the page calls for `allow="payment"` on Safari 17 or later; Safari 16 or earlier requires the iframe and top-level page to match protocol, full host and specified port (raw lines 53–66). Drop-in **v6.10.0+** is described as supporting compatible third-party browsers/devices, including Windows/Chromebooks with code scanning; older versions' table limits macOS to Safari, allows iOS/iPadOS browsers/web views, and excludes non-Apple devices (raw lines 68–76). Compatibility remains conditional on supported device/browser.
- Under either `/sessions` or `/payments`, **Adyen's certificate** needs no extra Apple Pay Drop-in configuration in this guide, while **own certificate** requires `onValidateMerchant` to display the sheet; its example sends the validation URL to the merchant server and resolves or rejects with the merchant session result (raw lines 91–163). This is merchant validation and UI configuration, not a completed payment. The page says no additional Apple Pay **API-request** fields are needed for the chosen endpoint, while its recurring-payment **client configuration** has a separate required `recurringPaymentRequest` (raw lines 78–83, 311–317).
- Optional Drop-in UI controls include instance-only `instantPaymentTypes`, Apple Pay button/request data, non-Safari code modal/window rendering, event callbacks and `applePayCapabilities` at **v6.10.0+**; it recommends the latter only for a product-page button (raw lines 165–235, 287–309). `onAuthorized` is called after **shopper authorization in Apple Pay** and resolves/rejects continuation of the flow (raw line 231); it is not Adyen authorization, capture or settlement proof. The capability sample's `switch` cases have no `break` statements (raw lines 295–309), so it should not be copied as validated display logic.
- Wallet Order Tracking is marked **v6.0.0+**. Its prose calls the callback `onOrderTracking`, while its fenced `swift` example uses JavaScript-like `onOrderTrackingRequest` and constructs `new ApplePay` (raw lines 237–271). The page says Sessions calls tracking after payment completion, whereas Advanced calls it after `onSubmit` resolves; it describes an order-detail error closing the overlay without an Apple Wallet order (raw lines 274–285). Neither callback timing nor the page's “successfully completed” wording substitutes for an observed payment outcome.
- Recurring tokenization is stated for **v5.39.0+**. The page **strongly recommends** explicit shopper permission for future charges and says `recurringPaymentRequest` is required for Apple Pay recurring configuration; actual token creation, later payment and token management are delegated to a separate tokenization guide (raw lines 311–317, 387–393). The v6 example visibly omits a separator in `new ApplePay(checkout {` (raw line 324); neither versioned snippet proves consent or a usable recurring charge.
- For LIVE with **Adyen's certificate**, the page requires a domain-association file for each domain/subdomain at the specified `/.well-known/` path, publicly accessible without password/proxy/redirect and with `text/plain`; live Customer Area method/domain updates require the named role and apply only to the **generic Apple Pay** method, not scheme-specific variants (raw lines 403–442). The **own-certificate** tab instead routes to Apple Developer live merchant-identifier setup (raw lines 453–455). Both tabs call for Apple domain-verification IP access and `out.adyen.com` allow-listing, warning that DNS-resolved IP fallbacks may change and disrupt service (raw lines 444–464). This historical checklist does not establish successful domain verification, firewall reachability or live payment enablement.

## Detail locators

- Endpoint-specific requirements, roles, certificate and TEST conditions: raw lines 21–47.
- Safari iframe and Drop-in browser/device version gates: raw lines 49–76.
- API endpoint reference and certificate-dependent merchant validation examples: raw lines 78–163.
- Optional button, payment-request, code and event configuration: raw lines 165–235.
- Wallet Order Tracking timing and example-name/language mismatch; capabilities sample: raw lines 237–309.
- Recurring permission, configuration and flawed v6 example: raw lines 311–393.
- TEST status lookup and LIVE role, domain, variant and firewall paths: raw lines 395–464.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-apple-pay]]
- [[source-adyen-docs-payment-methods-apple-pay-apple-pay-certificate]]
- [[source-adyen-docs-payment-methods-apple-pay-apple-pay-certificate-web]]
- [[adyen-tokenization]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/apple-pay/web-drop-in/2026-09-15|Full pinned Apple Pay Web Drop-in guide]]
