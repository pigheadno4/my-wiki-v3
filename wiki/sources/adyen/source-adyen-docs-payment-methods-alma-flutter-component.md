---
title: "Alma Flutter Component | Adyen Docs"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alma/flutter-component"
raw_files:
  - "adyen/docs/payment-methods/alma/flutter-component/2026-09-15.md"
tags: [adyen, alma, flutter, components, installments, redirect]
---

## Overview

This 2026-09-15 [[adyen|Adyen]] guide describes Alma-specific additions to an existing Flutter Components integration using Sessions or Advanced server-side flow. It covers request fields, Advanced redirect handling and an optional installment-count choice. See [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-alma|the Alma method overview]] for broader method scope. The TEST examples do not establish merchant eligibility or a completed payment.

## Key takeaways

- Sessions requires an existing Flutter Components Sessions integration, Checkout API v68 or later, and Alma added in Customer Area (raw lines 25–33). The added `/sessions` table lists `telephoneNumber`, `shopperEmail`, `billingAddress` and `deliveryAddress` with blank **Required** cells (lines 35–46); this page does not mark these additions mandatory. Its v71 TEST sample uses FR/EUR and an app-scheme `adyencheckout://your.package.name` return URL (lines 48–82).
- The Advanced section requires an existing Flutter Components Advanced integration, redirect action handling and Customer Area setup (lines 96–106). Its `/payments` table lists the same four shopper/contact/address additions with blank **Required** cells. `additionalData.alma.installments_count` may be set to `3` or `4`; omit it if the shopper should choose (lines 114–126). The v72 TEST example sets `4` for FR/EUR (lines 128–166).
- The Advanced sample response has `resultCode: RedirectShopper` and `action.type: redirect` (lines 168–182). This is a shopper handoff, not proof of final authorisation, capture or settlement. Neither flow requires additional Alma configuration parameters on this page (lines 84–88, 108–112). The page does not give an Alma-specific final-result, capture or refund procedure.
- Both **Integration type** prerequisite URLs point to an Advanced **Drop-in** guide, although their labels name Flutter Components and the first row says Sessions (lines 31, 104). Follow the flow and integration labels, then verify the base Flutter Components guide rather than treating those URLs as matching prerequisites. The two curl examples also omit shell continuation between `-X POST` and `-d` (lines 55–56, 135–136), so they are not copy-ready.
- The TEST sections direct status checks in Customer Area. Before live Alma acceptance, the page says to submit an Alma request in live Customer Area (lines 90–94, 184–188); this is an enablement step, not evidence of a particular merchant's live status.

## Detail locators

- Scope and Sessions requirements: raw lines 15–33; mismatched prerequisite URL at line 31.
- Sessions added fields, v71 FR/EUR TEST request and return URL: lines 35–82; shell continuation issue at lines 55–56.
- Sessions configuration and test/live route: lines 84–94.
- Advanced requirements and redirect prerequisite: lines 96–106; mismatched prerequisite URL at line 104.
- Advanced request additions and optional installment count: lines 114–126; v72 TEST request and shell issue at lines 128–166.
- Advanced redirect sample and test/live route: lines 168–188.

## Related

- [[adyen-online-payments]] — provider online-payment integration concept.
- [[source-adyen-docs-payment-methods-alma]] — Alma method overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/alma/flutter-component/2026-09-15|2026-09-15 Alma Flutter Component guide]]
