---
title: "Adyen native 3D Secure 2 authentication"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/3d-secure/native-3ds2"
raw_files:
  - "adyen/docs/online-payments/3d-secure/native-3ds2/2026-09-15.md"
tags: [adyen, 3d-secure, 3ds2, authentication, web, ios, android, flutter, react-native]
---

## Overview

Adyen's 2026-09-15 webpage snapshot (metadata last modified 2023-05-10) guides native 3D Secure 2 for existing Web, iOS, Android, Flutter, and React Native checkout integrations. It covers Web/iOS/Android Drop-in and Components, Flutter Drop-in and Components, and React Native Drop-in. These are Checkout `/payments` and `/payments/details` merchant integration routes, not standalone authentication or the separately versioned native 3DS2 SDK runtime. [[adyen]] [[adyen-3d-secure]]

## Key takeaways

- For the Advanced flow, the merchant server sends the `/payments` request with the channel-specific 3DS2 data; the client handles a returned authentication `action` through Drop-in or a Component, then passes authentication details for a server `/payments/details` request. Sessions-flow sections say no additional 3DS2 configuration is needed. Flutter and React Native Advanced-flow sections specify Checkout API v71 or later. See the respective integration and action sections below.
- Checkout API v69 or later tables set `authenticationData.threeDSRequestData.nativeThreeDS` to `preferred`; v68 or earlier tables use `additionalData.allow3DS2`. iOS and Android sections distinguish `threeDS2` actions for v67+ from `threeDS2Fingerprint`/`threeDS2Challenge` for v66 and earlier, including the older `paymentData` handoff. Follow the exact platform and API-version section.
- A returned `action` can be native 3DS2 or redirect. A response with no `action` is described as exempted or outside 3DS2 scope; use its `resultCode` for the payment result. Authentication and challenge completion do not by themselves establish an authorized payment. The guide also directs readers to the asynchronous payment webhook.
- Web native challenges can be blocked by a strict Content Security Policy; Adyen says it does not maintain a complete list of challenge URLs and offers redirect as an alternative. Mobile return and redirect handling is platform-specific. All requests for one live payment session should use the same live endpoint region.
- The tables distinguish required fields from Visa/JCB conditional fields and recommendations. For example, `shopperEmail` can be replaced by a phone-number path in the stated Visa/JCB case; mobile `shopperIP` is conditional for redirect fallback. Do not generalize Web `browserInfo` requirements to native mobile.

## Detail locators

- **Web Drop-in:** raw lines 19-903; requirements and CSP 27-36, `/payments` table 102-130, action cases 770-795, details and result 797-885. **Web Components:** lines 904-2035; Card Component versus own-form tabs 935-978, request variants 980-1030, action/component handling 1696-1790, details and result 1790-2027.
- **iOS Drop-in:** lines 2036-2904; requirements 2044-2053, request fields and SDK version 2097-2135, v67+/v66- action tables 2622-2682, details transition 2684-2850. **iOS Components:** lines 2905-3940; requirements 2913-2922, request fields 2958-2993, action/version handling 3480-3540, Action Component, details, and redirect 3542-3880.
- **Android Drop-in:** lines 3941-4808; requirements 3949-3958, request fields 4005-4032, action and details 4515-4770. **Android Components:** lines 4809-5670; requirements 4817-4826, request fields 4862-4890, action/component and redirect 5372-5632.
- **Flutter Drop-in and Components:** lines 5671-6451 and 6452-7241 respectively; both Advanced-flow prerequisites and return handling 5675-5785 and 6456-6557; action/details/result 6280-6444 and 7052-7234. **React Native Drop-in:** lines 7242-8060; v71+ prerequisite 7246-7255, request and platform-select values 7331-7355 and 7854-7874, details/result 7876-8054.
- The request examples are language-specific illustrations (curl, Java, PHP, C#, JavaScript, Go, Python, Ruby, TypeScript) and must be read within their surrounding platform/API-version tables. Web request examples show empty `returnUrl` in several SDK snippets although the adjacent tables mark it required and describe a usable return URL (for example raw lines 123, 250, 335, 424, 486). Flutter request tables say `channel` Android while also documenting iOS return handling (lines 5774-5776 and 6545-6549); do not infer that Android applies to iOS. The React Native narrative's `onSubmit` link points to Flutter (line 7333), while its own section describes React Native.

## Related

- [[source-adyen-docs-online-payments-3d-secure]] — high-level 3DS2 purpose and route selection.
- [[source-adyen-docs-online-payments-3d-secure-api-reference]] — detailed 3DS2 request parameter reference.
- [[source-adyen-docs-online-payments-3d-secure-redirect-3ds2]] — redirect route.
- [[source-adyen-docs-online-payments-3d-secure-standalone-authentication]] — separate authentication and authorization flow.
- [[adyen-3ds2-ios-sdk]] and [[adyen-3ds2-android-sdk]] — separately versioned SDK implementation evidence.

## Raw Sources

- [[raw/adyen/docs/online-payments/3d-secure/native-3ds2/2026-09-15|Native 3D Secure 2 authentication (2026-09-15 snapshot)]]
