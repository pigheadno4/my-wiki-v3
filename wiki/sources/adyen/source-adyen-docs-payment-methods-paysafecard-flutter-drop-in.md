---
title: "Adyen PaySafeCard Flutter Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paysafecard/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/paysafecard/flutter-drop-in/2026-09-15.md"
tags: [adyen, paysafecard, flutter, drop-in, sessions, advanced-flow]
---

## Overview

This 2026-09-15-captured Adyen guide adds PaySafeCard to an existing Flutter Drop-in integration. It gives separate Sessions and Advanced flow additions: shopper reference, redirect handling, no method-specific configuration, and test/live account steps. The method page is an add-on to the main integration, not a complete executable recipe. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions:** use an existing Flutter Drop-in Sessions flow with **Checkout API v68 or later**, redirect handling for `action.type: redirect`, and PaySafeCard added through Adyen Support in Customer Area. The requirements-table link is labeled Sessions but its URL selects `advanced-flow`; the nearby redirect and session-creation links select Sessions. Use the intended Sessions base guide rather than silently following the mismatched link. See raw lines 25–42.
- Add required `shopperReference` to `/sessions`, described as a unique shopper identifier such as a user or account ID. No extra PaySafeCard configuration parameters are specified. The TEST `/sessions` example uses v71, EUR/NL and a custom-scheme `returnUrl`; those values are examples rather than general eligibility or callback guarantees. See raw lines 40–69 and 270–274.
- **Advanced:** start with an existing Flutter Drop-in Advanced flow, handle the redirect action, and add PaySafeCard in Customer Area. Add required `shopperReference` to `/payments`; no extra method configuration is specified. The example response has `resultCode: RedirectShopper` and `action.type: redirect`, an additional action rather than final payment confirmation. The v68 API minimum is stated only in the Sessions requirements table on this page; do not extend it to Advanced without separate evidence. See raw lines 286–312 and 599–613.
- The TEST `/payments` examples use v72, EUR and an HTTPS `returnUrl` even though this is a Flutter guide; the sample request objects omit an explicit `paymentMethod`. The curl samples at lines 53–69 and 319–334 also omit a continuation after `-X POST`, while several library snippets leave request variables or initializer types undefined. Treat these snippets as illustrations, verify the actual Drop-in request and app return handling against the base guide. See raw lines 48–268 and 314–597.
- The page gives a 16-digit test code `0000 0000 0990 3417` and a test Customer Area payment-list check. Before accepting live PaySafeCard payments, contact Support to add it in **live** Customer Area. These instructions do not prove current enablement or successful live processing. See raw lines 276–284 and 615–623.

## Detail locators

- Sessions prerequisites, v68 requirement, redirect setup and source link mismatch: raw lines 25–36.
- Sessions shopper reference and TEST examples: raw lines 38–268.
- Sessions no extra configuration and test/live steps: raw lines 270–284.
- Advanced prerequisites, shopper reference and no extra configuration: raw lines 286–312.
- Advanced TEST request examples and redirect response: raw lines 314–613.
- Repeated test/live steps: raw lines 615–623.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paysafecard/flutter-drop-in/2026-09-15|Fully read PaySafeCard Flutter Drop-in raw]]
