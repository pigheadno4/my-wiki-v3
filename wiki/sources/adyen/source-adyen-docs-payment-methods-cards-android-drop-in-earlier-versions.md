---
title: "Adyen Android Cards Drop-in v4.x.x integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/cards/android-drop-in/earlier-versions"
raw_files:
  - "adyen/docs/payment-methods/cards/android-drop-in/earlier-versions/2026-09-15.md"
tags: [adyen, cards, android, drop-in, earlier-versions]
---

## Overview

This [[adyen]] page, captured 2026-09-15, is the **earlier-version Android Cards Drop-in v4.x.x** guide for adding cards to an existing Drop-in integration. Its explicit requirement is an **Advanced flow** Android Drop-in integration and card addition in the Customer Area. Introductory, configuration and See also links point to a Sessions-flow guide despite that requirement; do not infer the two flows are interchangeable from those links. See [[adyen-android-sdk]] for the separately versioned Android SDK route and [[source-adyen-docs-payment-methods-cards-android-drop-in]] for the v5.0.0+ cards page.

## Key takeaways

- **Card display and client/server split:** The server sends `countryCode` plus `amount.currency` to `/paymentMethods`; Drop-in uses the response to show available cards. Optional `CardConfiguration` controls cardholder name and postal-code fields. Drop-in collects and encrypts sensitive card details in the app, then returns `paymentComponentData.paymentMethod`; the merchant sends component data to its server for a Checkout `/payments` request. The page's shorthand that sensitive information does not touch the server means unencrypted fields are not supposed to reach it: the separate [[adyen-pci-dss-compliance]] guide expressly says encrypted cardholder data is sent through the merchant server. See pinned raw lines 19–88 and PCI guide raw lines 215–225.
- **Server request and outcomes:** The illustrated request uses the Checkout **test** v72 `/payments` endpoint, encrypted card fields, merchant account and Android return URL. Language examples use distinct historical API-library versions; the Go example labels v10.4.0 while importing `/v9/` paths. The response example's `Authorised` is a sample result, not a live transaction. `resultCode` is for shopper presentation and a webhook separately reports the outcome; `Cancelled`, `Error`, `Refused` and additional 3D Secure result codes are possible. If manual capture applies, capture remains a separate step. This guide does not document a complete action callback or prove capture, settlement or payout. See pinned raw lines 83–471.
- **Stored-card example and wording conflicts:** For token creation the page describes a shopper storage switch, passes `storePaymentMethod` and a unique `shopperReference` in server `/payments`, and uses the same shopper reference in `/paymentMethods` to show stored cards. It calls the switch-containing object `actionComponentData` while referencing `paymentComponentData.storePaymentMethod`; preserve that inconsistency rather than treating either as verified field wiring. To hide the save-card switch, prose says `showStoredPaymentMethods: false`, but the adjacent Kotlin code uses `.setShowStorePaymentField(false)`; these appear to be different controls and the example does not resolve the wording. A shopper-present stored-card example sends `paymentComponentData.paymentMethod` through the server and uses `ContAuth` plus `UnscheduledCardOnFile` in its illustrative request; do not generalize those values to all shopper-initiated reuse. The page points elsewhere for shopper-not-present subscription or contract payments. See pinned raw lines 473–809.
- **Live boundary:** The guide describes `test_`-prefixed test details while a client integration is unfinished, then lists test cards, live Customer Area card addition, a live client key and PCI assessment/SAQ A before live cards. SAQ A is conditional on actual mobile Drop-in eligibility in the PCI guide; these steps do not attest compliance, present merchant enablement or a successful payment. See pinned raw lines 811–823 and PCI guide raw lines 215–237.

## Detail locators

- v4.x.x identity, Advanced-flow requirement and Sessions-link inconsistency: pinned raw lines 15–38.
- Optional `CardConfiguration`, test environment and postal-code policy: pinned raw lines 36–81.
- Component-to-server `/payments` request and historical SDK snippets: pinned raw lines 83–437. Go v10.4.0 label and `/v9/` imports occur at lines 289–295.
- Response fields, result codes, webhook and separate manual capture: pinned raw lines 439–471.
- Token creation, switch-name/object-name inconsistencies, stored-card retrieval and use: pinned raw lines 473–809.
- Test and live checklist: pinned raw lines 811–823.

## Related

- [[adyen-android-sdk]] — main SDK route; its current retained v5 baseline must not be attributed to this v4.x.x guide.
- [[adyen-online-payments]] — broader Advanced client/server/webhook architecture.
- [[adyen-tokenization]] — current token lifecycle and shopper-reference scope.
- [[adyen-3d-secure]] — authentication pathway distinct from authorization/capture.
- [[adyen-pci-dss-compliance]] — mobile Drop-in SAQ A eligibility and encrypted-data path.

## Raw Sources

- [[raw/adyen/docs/payment-methods/cards/android-drop-in/earlier-versions/2026-09-15|Android Cards Drop-in v4.x.x guide, captured 2026-09-15]]
