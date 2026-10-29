---
title: "Adyen Atome Android Drop-in"
type: source
date_ingested: 2026-10-29
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/atome/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/atome/android-drop-in/2026-09-15.md"
tags: [adyen, atome, android, drop-in, redirect, online-payments]
---

## Overview

This captured [[adyen]] page describes Atome-specific additions to an existing Android Drop-in integration. It separates Sessions and Advanced server-side flows, request fields, redirect handling, partial refunds, and test/live setup. The page explicitly defers the base integration to linked guides. [[adyen-online-payments]]

## Key takeaways

- **Prerequisites and flow:** Sessions requires an existing Android Sessions Drop-in integration, Checkout API v68 or later, and Atome added in Customer Area. Advanced requires an existing Android Advanced Drop-in integration, redirect handling for `action.type: redirect`, and Atome setup. Neither flow needs additional Atome Drop-in configuration parameters (raw lines 25–34, 730–734, 768–782).
- **Request data and geography:** Both `/sessions` and `/payments` tables mark `shopperName`, `shopperEmail`, `telephoneNumber`, `billingAddress`, `lineItems`, and `countryCode` required; Advanced also marks `paymentMethod.type: atome` required. `deliveryAddress` has a blank Required cell and is described as optional when billing and delivery addresses match. The stated country/currency combinations are Malaysia/MYR and Singapore/SGD. The examples use SG/SGD and a 1000-minor-unit amount with item lines totaling 1000 (raw lines 38–50, 786–799; examples 52–113 and 801–864).
- **Redirect and outcome:** Advanced shows `resultCode: RedirectShopper` and an Atome redirect `action`, despite labeling the snippet “successful payment.” That response calls for redirect handling; it is not evidence of final payment success or a real transaction. The page's Advanced requirements link to the base Android redirect-handling guide (raw lines 770–776, 1516–1528).
- **Refund, testing and live:** For a partial refund, the guide says to specify `amount` in `/payments/{paymentPspReference}/refunds`; the “Refunds and cancellations” heading provides no separate cancellation procedure. Testing needs an Atome sandbox shopper account requested from an Adyen contact, and a different account for each country/region tested. The page lists MY/SG QR test apps and test Customer Area status; live acceptance requires contacting Support to add Atome in live Customer Area (raw lines 736–766, 1530–1558).
- **Example caveats:** Both curl examples have `-X POST` without a trailing shell continuation before `-d`. The Sessions JSON duplicates `countryCode`. The Advanced example uses a web URL `returnUrl` in this Android guide, while the Sessions example uses `adyencheckout://your.package.name`. Treat example return URLs as examples requiring the base Android return configuration; neither curl block is copy-ready (raw lines 54–78, 803–827).

## Detail locators

- Identity and Sessions prerequisites/fields: pinned raw lines 15–50; Sessions examples: lines 52–728.
- Sessions no-extra-configuration, refund and test/live: pinned raw lines 730–766.
- Advanced prerequisites/fields and examples: pinned raw lines 768–1514.
- Advanced redirect response, refund and test/live: pinned raw lines 1516–1558.

## Related

- [[adyen-online-payments]] — online payment architecture and method routes.
- [[source-adyen-docs-payment-methods-atome]] — captured Atome method overview; use this page for Android Drop-in details.

## Raw Sources

- [[raw/adyen/docs/payment-methods/atome/android-drop-in/2026-09-15|Atome Android Drop-in, captured 2026-09-15]]
