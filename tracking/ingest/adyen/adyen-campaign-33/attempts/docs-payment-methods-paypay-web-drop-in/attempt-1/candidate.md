---
title: "Adyen PayPay Web Drop-in integration"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypay/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/paypay/web-drop-in/2026-09-15.md"
tags: [adyen, paypay, web, drop-in, redirect]
---

## Overview

This [[adyen]] guide adds PayPay to an existing **Web Drop-in** integration, splitting PayPay-specific additions between **Sessions** and **Advanced** server-side flows. The linked main integration supplies the base payment and redirect lifecycle. PayPay appearing in Drop-in, a simulator redirect, or a Customer Area status view does not itself prove final authorization, capture or settlement. [[adyen-online-payments]]

## Key takeaways

- **Sessions:** The guide requires an existing Sessions Web Drop-in integration, **Checkout API v68 or later**, `action.type: redirect` handling and PayPay added in Customer Area. It says no additional PayPay parameters are needed when creating `/sessions`; the base Sessions request still applies. Importing individual methods for tree shaking is **optional**, and if used the import includes `Redirect`. See raw lines 25–54.
- **Advanced:** The section requires an existing Advanced Web Drop-in integration, redirect handling and PayPay added in Customer Area. It likewise presents an optional individual-method import including `Redirect`, and says no additional PayPay parameters are needed for `/payments`. It does **not** restate the Sessions v68+ minimum as an Advanced requirement. The Advanced integration-type link contains the encoded unresolved `{{getParameter('platform')}}` placeholder; use the text's intended Advanced Web Drop-in route rather than relying on that literal URL. See raw lines 71–99.
- **TEST and LIVE:** The page names the TEST acquirer accounts `DGFT_AcquirerAccount_Adyen_closedLoop_AUTHFlow` and `DGFT_AcquirerAccount_Adyen_closedLoop_SALEFlow`; it says the test route redirects to a DGFT simulator, without a PayPay app, and test transactions can be viewed in Customer Area. The LIVE instruction says to access an activated PayPay smartphone app through a Japan local IP address. These are historical test/live instructions, not evidence of current merchant enablement or a successful payment. See raw lines 56–69 and 101–114.

## Detail locators

- Scope and Sessions prerequisites/parameters/optional import: raw lines 15–54.
- Advanced prerequisites/optional import/parameters: raw lines 71–99.
- Duplicated TEST account, simulator and LIVE app/IP guidance: raw lines 56–69 and 101–114.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-paypay]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypay/web-drop-in/2026-09-15|Adyen PayPay Web Drop-in guide]]
