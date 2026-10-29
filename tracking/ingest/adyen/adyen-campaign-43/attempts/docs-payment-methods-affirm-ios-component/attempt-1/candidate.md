---
title: "Adyen Affirm iOS Component integration"
type: source
date_ingested: 2026-10-27
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/affirm/ios-component"
raw_files:
  - "adyen/docs/payment-methods/affirm/ios-component/2026-09-15.md"
tags: [adyen, affirm, ios, components, financing, capture]
---

## Overview

Adyen's 2026-09-15 guide adds Affirm to an existing iOS Components integration, covering Sessions and Advanced server flows, Checkout request data, native `AffirmComponent` creation, capture and test/live setup. Its mixed native and Web examples require scope-aware reading. See [[adyen]] and [[adyen-ios-sdk]].

## Key takeaways

- The merchant first needs an iOS Components Sessions or Advanced integration and Affirm added in Customer Area. Both prerequisite base-guide URLs contain an unresolved encoded `getParameter('platform')` placeholder, though the later Sessions link explicitly targets iOS; those placeholder URLs are not verified iOS base-guide routes (raw lines 21-45). The page labels `/sessions` the default for Components v5.0.0 or later; `/payments` is the other tab (raw lines 39-45, 758-760).
- Both endpoint tables mark `shopperName`, `telephoneNumber` and `shopperEmail` required. `countryCode` is required for Canada or the UK because omission defaults to US. When supplying billing or delivery address, `stateOrProvince` is required for Canada and US and optional for UK; missing delivery address defaults to billing. `lineItems` is optional but recommended to improve approval rates; `shopperReference` is optional with minimum length three (raw lines 47-56, 762-771). TEST request examples use US/USD and an app return URL; they do not establish country, currency or financing eligibility beyond the table statements (raw lines 58-117, 773-835).
- In iOS Components v5.0.0 or later, the Swift examples check for `AffirmPaymentMethod`, create `AffirmComponent`, keep a reference and present it. Sessions assigns the session as delegate; Advanced assigns the merchant object. The v4.x.x example uses an earlier `apiContext` and `FormComponentStyle` initializer. The page says no Affirm-specific Component configuration is required (raw lines 1251-1308).
- Later sections under “Optional configuration” show TypeScript/JavaScript `affirm: { ... }`, `AdyenCheckout`, `checkout.create('affirm', ...).mount('#affirm-container')`, and a malformed v6 constructor example. These are Web-style snippets inside an iOS page and do not establish equivalent native Swift `AffirmComponent` properties or a native v6 integration route. Likewise some `/payments` SDK examples set `channel: Web` despite the iOS title, and the curl examples contain literal `{hint:...}` address keys; use the prose tables and native Swift section for the iOS route, and verify request/example syntax independently (raw lines 79-93, 797-812, 855, 938, 1010, 1251-1437).
- Capture after goods are sent is required within 28 days or the Affirm authorization expires. Capture triggers the shopper's installment schedule. If fulfillment is less than the authorized amount, this page instructs capture of the authorized amount then refund of the difference, rather than a lesser capture (raw lines 1439-1443).
- TEST credentials come from Affirm, and Affirm provides live credentials after reviewing test transactions. Live use also requires a live Customer Area request and supplying Adyen with Affirm live credentials. TEST examples or test-payment status do not prove live approval or successful financing (raw lines 1445-1451).

## Detail locators

- Flow prerequisites, endpoint field tables and examples: raw lines 21-1249.
- Native Swift Component versions and delegate assignments: raw lines 1251-1308.
- Mixed Web-style optional configuration/code and copy limitations: raw lines 1310-1437.
- Capture, refund difference and 28-day expiry: raw lines 1439-1443.
- Test credentials and live enablement: raw lines 1445-1451.

## Raw Sources

- [[raw/adyen/docs/payment-methods/affirm/ios-component/2026-09-15|Affirm iOS Component integration (2026-09-15 snapshot)]]
