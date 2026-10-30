---
title: "Adyen Advanced flow integration guide"
type: source
date_ingested: 2026-10-30
original_format: webpage
canonical_url: "https://docs.adyen.com/online-payments/build-your-integration/advanced-flow"
raw_files:
  - "adyen/docs/online-payments/build-your-integration/advanced-flow/2026-09-15.md"
tags: [adyen, online-payments, advanced-flow, checkout, drop-in, components, api-only]
---

## Overview

Adyen's 2026-09-15-captured Advanced flow guide spans Web, iOS, Android, React Native and Flutter, each with Drop-in, Components and API-only variants. In the Advanced flow, the merchant server obtains available methods with `/paymentMethods`, creates payments with `/payments`, and supplies further details through `/payments/details` when needed. The client presents the chosen UI or an API-only merchant UI, submits payment data, and handles returned actions. A webhook server receives the asynchronous payment outcome. This is a base integration guide; payment-method-specific fields and behavior remain in individual method guides.

## Key takeaways

- Drop-in and Components supply client UI and action handling but delegate Advanced server requests to merchant code. API-only requires the merchant to build the client UI and handle actions. Web callback handling uses `onSubmit` and `onAdditionalDetails` with `actions.resolve` or `actions.reject`; mobile frameworks use their own delegate/callback/result contracts. Follow the variant's own section, rather than transferring a callback rule across platforms.
- A `/payments` response without `action` can proceed to current-status display. With `action`, handle the named action and submit details when available. Redirects can return to the merchant client with `redirectResult` or `MD`/`PaRes`; when the shopper does not return, details may be unavailable and the merchant must wait for the webhook. API-only redirect handling differs from Drop-in/Components handoff.
- Synchronous `resultCode` supports shopper-facing current status; the `AUTHORISATION` webhook supplies the final outcome for the order management system, matched by `merchantReference`. HTTP 200 with `Refused` or `Error` is a payment result, while a non-200 API response is an API error.
- Raw card collection in API-only variants is conditioned on PCI assessment and Adyen Account Manager eligibility confirmation; the guide recommends an encrypted Custom Card Component for card collection. Method, risk, 3DS, tokenization and recurring cases can require additional request fields. Go-live steps include live-account and payment-method setup, PCI assessment, live endpoint selection, and keeping `/payments` and `/payments/details` in the same live region for a payment.
- Source caveats: Web Drop-in and Components contain embedded Sessions-specific amount-update blocks; these are not a blanket Advanced-flow step. Several mobile `/paymentMethods` code examples use an iOS or Android `channel` that conflicts with adjacent platform prose. The tab headed **Flutter API only** gives `channel: Web` in its `/paymentMethods` table and curl sample, and requires an `http://` or `https://` `/payments` `returnUrl`; these are Web-shaped instructions under a Flutter heading, not verified native Flutter settings. Check the relevant platform-specific guide before applying them. API-only 3DS redirect examples use `PaReq` in `action.data` and POST samples while nearby field tables say `PaRes`; retain the discrepancy rather than copying a single normalized field rule.

## Detail locators

- Web Drop-in: raw lines 19-2087; Web Components: 2088-4086; Web API-only: 4087-5765. Web callback and action details are at 1175-1937; API-only redirects and details at 5148-5442.
- iOS Drop-in: 5766-7485; iOS Components: 7486-9326; iOS API-only: 9327-10655. Android Drop-in: 10656-12335; Android Components: 12336-14008; Android API-only: 14009-15339. Native return handling, callback/delegate contracts and API-only PCI conditions are in their respective sections.
- React Native Drop-in: 15340-17001; Components: 17002-18628; API-only: 18629-19959. React Native `component.hide(result)` callback obligation: 16243 and 17871. Flutter Drop-in: 19960-21442; Components: 21443-22949; API-only: 22950-24629. Flutter `AdvancedCheckout`, `PaymentEvent` and `PaymentAdvancedFinished` are at 20770-20820, 21091-21100 and 21290-21304.
- Outcome and live-region examples recur by variant; Web Drop-in lines 1939-2059 give a compact starting point. Web API-only PCI and redirect example conflicts are at 4100-4115, 4638-4643, 5197-5275. The Flutter API-only heading is at 22950, its Web `channel` table/curl at 23364-23400, and web-protocol `returnUrl` rule at 23623-23643; its PCI and redirect passages are at 23501-23506 and 24064-24138.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-ios-sdk]]
- [[adyen-android-sdk]]
- [[adyen-react-native-sdk]]

## Raw Sources

- [[raw/adyen/docs/online-payments/build-your-integration/advanced-flow/2026-09-15|Adyen Advanced flow integration guide (captured 2026-09-15)]]
