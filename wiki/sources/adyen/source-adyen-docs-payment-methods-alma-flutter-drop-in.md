---
title: "Alma Flutter Drop-in integration"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/alma/flutter-drop-in"
raw_files:
  - "adyen/docs/payment-methods/alma/flutter-drop-in/2026-09-15.md"
tags: [adyen, alma, flutter, drop-in, redirect, installments]
---

## Overview

This 2026-09-15 [[adyen|Adyen]] guide adds Alma to an existing Flutter Drop-in integration through Sessions or Advanced flow. It gives method-specific request fields, configuration and redirect/test-live notes. See [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-alma|the Alma overview]] for the captured FR/EUR method scope. TEST examples do not prove current enablement, a completed return or payment success.

## Key takeaways

- Sessions requires an existing Flutter Drop-in Sessions integration and Checkout API v68 or later. Its setup row says to contact Support to add Alma in Customer Area; the Advanced setup row instead says to add Alma in Customer Area. The Sessions integration row is labeled Sessions but links to an Advanced-flow URL, so verify the matching base guide. Advanced also requires additional-action handling for `action.type: redirect`.
- Both Alma-specific endpoint tables list telephone number, shopper email, billing and delivery addresses with blank Required cells. Advanced additionally lists optional `additionalData.alma.installments_count`: set `3` or `4` to determine the installment count, or omit for shopper choice. The examples include those optional fields but do not make them mandatory. Both flow sections state that no extra Alma configuration parameters are needed.
- The Sessions FR/EUR TEST v71 sample uses an app-scheme `returnUrl` placeholder `adyencheckout://your.package.name` (raw line 64), while the Advanced FR/EUR TEST v72 sample uses an HTTPS return URL (line 144). The guide does not reconcile the difference or demonstrate a completed app return. Advanced shows a `RedirectShopper`/`action.type: redirect` response, not final authorization.
- Both curl examples split `-X POST` and `-d` across lines without a shell continuation (raw lines 52–58 and 132–138), so they are not verified copy-ready commands. Check TEST payment status in Customer Area; live acceptance requires submitting an Alma request in live Customer Area.

## Detail locators

- Sessions prerequisites, optional fields and FR/EUR v71 sample: pinned raw lines 25–84. No-extra-config and test/live: lines 86–96.
- Advanced prerequisites, optional installments field, FR/EUR v72 sample and redirect action: lines 98–184. Test/live route: lines 186–190.

## Related

- [[adyen-online-payments]] — provider integration concept
- [[source-adyen-docs-payment-methods-alma]] — method and feature overview

## Raw Sources

- [[raw/adyen/docs/payment-methods/alma/flutter-drop-in/2026-09-15|Alma Flutter Drop-in guide, captured 2026-09-15]]
