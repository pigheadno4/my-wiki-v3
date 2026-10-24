---
title: "Adyen Touch'n Go Web Drop-in guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/touchngo/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/touchngo/web-drop-in/2026-09-15.md"
tags: [adyen, touchngo, web, drop-in, wallets, online-payments]
---

## Overview

This [[adyen]] Touch'n Go Web Drop-in add-on, captured 2026-09-15, says how to add the method to an **existing** Web Drop-in Sessions or Advanced integration. Both flow requirements direct the merchant to Adyen Support for Customer Area method setup; the page says there are no Touch'n Go-specific API fields or Drop-in configuration steps. See [[adyen-online-payments]]. It is not a base integration, merchant-eligibility proof, or an executed payment/result procedure. See raw lines 15–48.

## Key takeaways

- The Sessions tab requires an existing Sessions Web Drop-in integration; the Advanced tab requires an existing Advanced Web Drop-in integration. **Both** say to contact Support before adding Touch'n Go in Customer Area. A separate Support contact is required to add it in **live** Customer Area for live acceptance. These are setup instructions, not confirmation of account activation. See raw lines 21–37 and 50–54.
- No Touch'n Go-specific additional API fields or Drop-in configuration are required according to this page. It routes general optional fields to `/sessions` or `/payments` according to the existing integration. The page calls `/sessions` the default with Drop-in **v5.0.0 or later** and `/payments` a route when an additional use case is implemented; do not turn that default statement into a method-wide SDK minimum or conclude that base request requirements disappear. See raw lines 39–48.
- Test-payment status can be checked in test Customer Area. The page does not itself describe redirect action handling, shopper return, webhook finality, country/currency scope, recurring or refund behavior; those need separate guides. A test status lookup or Support request is not payment-outcome evidence. See raw lines 50–60 and [[source-adyen-docs-payment-methods-touchngo]].

## Detail locators

- Existing Sessions/Advanced Web Drop-in and Support prerequisites: raw lines 21–37.
- API endpoint routing and no extra method-specific fields/configuration: raw lines 39–48.
- Test status and separate live Support step: raw lines 50–54.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-touchngo]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/touchngo/web-drop-in/2026-09-15|Touch'n Go Web Drop-in — captured 2026-09-15]]
