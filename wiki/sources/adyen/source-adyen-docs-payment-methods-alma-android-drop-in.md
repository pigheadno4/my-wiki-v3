---
title: "Alma Android Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alma/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/alma/android-drop-in/2026-09-15.md"
tags: [adyen, alma, android, drop-in, redirect, installments]
---

## Overview

This 2026-09-15 [[adyen|Adyen]] guide adds Alma to an existing Android Drop-in integration using Sessions or Advanced flow. It covers method-specific request additions, redirect handling and test/live routes. See [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-alma|the Alma overview]] for captured FR/EUR method scope. The examples do not establish current eligibility, completed app return or payment success.

## Key takeaways

- Sessions requires an existing Android Drop-in Sessions integration, Checkout API v68 or later and Alma added in Customer Area. Advanced requires its Android Drop-in base integration, additional-action handling for `action.type: redirect` and Customer Area setup. Both flow sections say no Alma-specific configuration parameters are needed.
- The Alma-specific `/sessions` and `/payments` tables list telephone number, shopper email, billing and delivery addresses with blank Required cells. Advanced also lists optional `additionalData.alma.installments_count`: `3` or `4` selects the installment count, while omission lets the shopper choose. Fields included in an example are not thereby mandatory.
- The Sessions FR/EUR TEST v71 example uses the Android app-scheme `returnUrl` placeholder `adyencheckout://your.package.name` (raw line 63); the Advanced FR/EUR TEST v72 example uses an HTTPS return URL (line 143). The guide does not reconcile the return-route difference or show a completed app return. Advanced shows `RedirectShopper`/`action.type: redirect`, not final authorization.
- Both curl examples split `-X POST` and `-d` without a shell continuation (raw lines 51–57 and 131–137), so they are not verified copy-ready commands. TEST status is checked in Customer Area; accepting live Alma requires a request in live Customer Area.

## Detail locators

- Sessions prerequisites, optional fields and FR/EUR v71 example: pinned raw lines 25–83. No-extra-config and test/live: lines 85–97.
- Advanced prerequisites, optional installments field, FR/EUR v72 example and redirect action: lines 99–183. Test/live route: lines 185–189.

## Related

- [[adyen-online-payments]] — provider integration concept
- [[source-adyen-docs-payment-methods-alma]] — method and feature overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/alma/android-drop-in/2026-09-15|Alma Android Drop-in guide, captured 2026-09-15]]
