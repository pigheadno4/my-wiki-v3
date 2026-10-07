---
title: "Braintree JavaScript v2 Browser Support"
type: source
date_ingested: 2026-10-07
original_format: webpage
canonical_url: "https://developer.paypal.com/braintree/docs/reference/client-reference/javascript/v2/browser-support"
raw_files:
  - "braintree/docs/reference/client-reference/javascript/v2/browser-support-2026-09-16.md"
tags: [braintree, javascript-v2, client-sdk, browser-support, webviews]
---

## Overview

This collected [[braintree]] website snapshot documents the browser, mobile-browser, webview and runtime support statements for the historical Braintree JavaScript v2 SDK. It records a page-specific tested-platform inventory and consequential compatibility caveats for [[braintree-web-sdk]]; it is not evidence of current browser support, current package or hosted-runtime behavior, merchant eligibility, or successful payment execution.

## Key takeaways

- The page lists the desktop and mobile browsers against which the JavaScript v2 SDK was actively tested, while stating that it may also work in other browsers. Treat those lists as captured historical inventory, not a current compatibility matrix or proof for an exact retained GitHub package.
- Internet Explorer Quirks Mode is unsupported for every IE version. The page separately says Braintree ended TLS 1.0 and 1.1 support on June 26, 2018; because IE 9 and 10 do not enable TLS 1.2 by default, the v2 SDK works there only when the customer explicitly enables TLS 1.2 in IE settings.
- The page generally describes iOS and Android webviews as supported, but excludes Chrome for iOS before iOS 8. For PayPal specifically, it says Android webviews below Android 4.4 are unsupported and reports checkout-scrolling trouble in both iOS `UIWebView` and `WKWebView`.
- Braintree states that it does not intend to fix those known PayPal webview issues. The page recommends using an appropriate Braintree SDK or opening PayPal in the system browser or an approved browser-view mechanism such as Safari View Controller or Chrome Custom Tabs; this is historical page guidance, not proof that any named mechanism or SDK currently works.
- Hybrid runtimes including Cordova, PhoneGap, Ionic, React Native, Electron and Adobe AIR are neither tested nor developed for by this SDK. The page allows that some success may occur but warns that the browser-optimized SDK may not function correctly outside browser security policies.

## Detail locators

- `### Desktop`, raw lines 17-34 — tested desktop-browser inventory, the all-IE Quirks Mode exclusion, and the IE 9/10 TLS 1.2 condition.
- `### Mobile`, raw lines 35-52 — iOS and Android tested-platform inventory and the distinction between active testing and possible operation in other browsers.
- `### Webviews`, raw lines 53-66 — general mobile-webview statement, Chrome for iOS boundary, PayPal Android and iOS known issues, security/UX rationale, no-fix statement and recommended external-browser alternatives.
- `#### Runtime environments`, raw lines 67-69 — named hybrid runtimes and the untested/undeveloped, browser-optimized runtime boundary.

## Related

- Company: [[braintree]]
- Concept: [[braintree-web-sdk]]

## Raw Sources

- [[raw/braintree/docs/reference/client-reference/javascript/v2/browser-support-2026-09-16|Braintree JavaScript v2 Browser Support snapshot (2026-09-16)]]
