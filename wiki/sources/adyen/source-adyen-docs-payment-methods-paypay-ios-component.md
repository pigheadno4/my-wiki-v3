---
title: "Adyen PayPay iOS Component"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypay/ios-component"
raw_files:
  - "adyen/docs/payment-methods/paypay/ios-component/2026-09-15.md"
tags: [adyen, paypay, ios, components, redirects]
---

## Overview

This 2026-09-15 Adyen page describes PayPay-specific additions to an **existing iOS Components** integration, with separate Sessions and Advanced flow tabs. It does not supply the complete client/server flow or a payment-outcome procedure; those remain in the linked main integration guides. [[adyen]] [[adyen-ios-sdk]]

## Key takeaways

- Sessions requires an existing iOS Components Sessions flow, Checkout API v68 or later, redirect-action handling (`action.type: redirect`), and PayPay added in Customer Area. Advanced requires an existing iOS Components Advanced flow, redirect handling and PayPay added in Customer Area; this page gives no separate Advanced API minimum. Both tabs say there are no additional PayPay-specific configuration parameters; Sessions says none for `/sessions`, and Advanced says none for `/payments`. These are only PayPay-specific additions, not a waiver of the main flow's request and server requirements.
- Both tabs describe initializing the PayPay Component with a `None` class and checking for a returned supported payment method before showing it. The Sessions snippet assigns `session` as delegate; the Advanced snippet assigns `self`. The code is internally awkward: it passes `payPayConfiguration` while the prose says no PayPay-specific configuration is needed, and the Advanced requirement text says Components while its integration-type link uses `integration=Drop-in`. Treat these as unresolved documentation/example mismatches and verify the actual SDK type and configuration in the selected version before coding.
- For TEST, the guide lists two DGFT acquirer-account names for closed-loop authorization or sale flows. It says the shopper is redirected to a DGFT simulator and does not need the PayPay app. For LIVE, it says an activated PayPay smartphone app must be accessed through a Japan local IP address. Test-simulator completion and the live app/IP condition do not establish current merchant eligibility, a successful authorization, capture or settlement.
- The page describes redirect handling as a prerequisite but gives no result-code, return/callback or webhook-outcome instructions here. Complete redirect return and authoritative payment-outcome handling must be taken from the linked main flow and applicable webhook guidance, not inferred from presenting the Component or reaching the simulator. No PayPay currency or recurring-payment rule is stated on this page.

## Detail locators

- Identity, scope and flow selection: [[raw/adyen/docs/payment-methods/paypay/ios-component/2026-09-15|PayPay iOS Component raw]], lines 15–23.
- Sessions prerequisites, no extra `/sessions` parameters or configuration, and `None` initialization/delegate example: [[raw/adyen/docs/payment-methods/paypay/ios-component/2026-09-15|PayPay iOS Component raw]], lines 25–73.
- Sessions TEST acquirer accounts, DGFT redirect simulator and LIVE Japan-IP/app condition: [[raw/adyen/docs/payment-methods/paypay/ios-component/2026-09-15|PayPay iOS Component raw]], lines 75–86.
- Advanced Components text versus Drop-in link, redirect prerequisite, no extra `/payments` parameters or configuration, and `None` example: [[raw/adyen/docs/payment-methods/paypay/ios-component/2026-09-15|PayPay iOS Component raw]], lines 88–134.
- Repeated Advanced TEST and LIVE conditions: [[raw/adyen/docs/payment-methods/paypay/ios-component/2026-09-15|PayPay iOS Component raw]], lines 136–147.

## Related

- [[adyen-ios-sdk]] — native Components, Sessions/Advanced and redirect-action context.
- [[adyen-online-payments]] — server and webhook outcome boundaries.

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypay/ios-component/2026-09-15|Adyen PayPay iOS Component guide (2026-09-15 snapshot)]]
