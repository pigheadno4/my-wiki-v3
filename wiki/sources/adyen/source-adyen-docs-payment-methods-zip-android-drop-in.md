---
title: "Adyen Zip Android Drop-in v5 integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/zip/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/zip/android-drop-in/2026-09-15.md"
tags: [adyen, zip, android, drop-in, sessions, advanced-flow]
---

## Overview

This [[adyen|Adyen]] page, fetched and marked last modified 2026-09-15, is a short **Zip add-on for existing Android Drop-in v5.0.0 or later** integrations. It routes both Sessions and Advanced flows to their base guides. The page says v5.0.0 was released in October 2023 and directs earlier versions to [[source-adyen-docs-payment-methods-zip-android-drop-in-earlier-versions|the earlier-version guide]]. See [[adyen-online-payments]]. The captured page is not evidence of current Zip eligibility or a completed transaction.

## Key takeaways

- **Prerequisites:** Build an Android Drop-in integration in the chosen server-side flow, with minimum Android Drop-in version 5.0.0, and add Zip in Customer Area. The page links separate Android Sessions and Advanced base guides.
- **Method-specific additions:** The Sessions tab says Zip needs **no additional fields** in `/sessions`; the Advanced tab says **no additional fields** in `/payments`. Both tabs likewise say Zip needs **no additional Drop-in configuration**. These are Zip-specific additions to an existing integration, not a waiver of the base flow's required request fields, redirect/result handling or configuration.
- **Continue base flow:** After configuration, the Sessions route creates the checkout session; the Advanced route launches and shows Drop-in. The page does not provide a standalone request, redirect action, capture, refund or recurring procedure; consult the linked base and other Zip method pages for those topics rather than infer them from silence here.
- **Testing and live:** Create Zip test accounts using Zip's linked test credentials, make test payments in the test environment, and check their status in Adyen test Customer Area. Before accepting live Zip payments, submit a request for Zip in the live Customer Area. A test payment or this guide does not show live approval.

## Detail locators

- Identity, Android v5.0.0 scope and earlier-version route: pinned raw lines 15–21. Sessions/Advanced prerequisites and Customer Area: lines 23–39.
- No extra `/sessions` or `/payments` fields: lines 41–49. No extra Drop-in configuration and flow continuation links: lines 51–67. TEST account/status and live request: lines 69–80.

## Related

- [[adyen-online-payments]] — provider integration concept
- [[source-adyen-docs-payment-methods-zip-android-drop-in-earlier-versions]] — older Android Drop-in guide

## Raw Sources

- [[raw/adyen/docs/payment-methods/zip/android-drop-in/2026-09-15|Zip Android Drop-in guide, fetched 2026-09-15]]
