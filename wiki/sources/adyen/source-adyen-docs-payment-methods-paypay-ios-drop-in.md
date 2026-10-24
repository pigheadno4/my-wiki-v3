---
title: "Adyen PayPay iOS Drop-in"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/paypay/ios-drop-in"
raw_files:
  - "adyen/docs/payment-methods/paypay/ios-drop-in/2026-09-15.md"
tags: [adyen, paypay, ios, drop-in, online-payments]
---

## Overview

This [[adyen]] guide, modified and captured 2026-09-15, adds PayPay to an existing **iOS Drop-in** integration under Sessions or Advanced. It gives method-specific field/configuration scope, TEST DGFT simulator routes and a LIVE PayPay app/Japan-local-IP condition. See [[adyen-online-payments]] and [[source-adyen-docs-payment-methods-paypay|PayPay overview]] for the dated JP/JPY redirect matrix (related raw lines 23–27). These are setup and testing descriptions, not proof of current merchant eligibility, a completed return, authorization, capture or settlement. See primary raw lines 15–34 and 48–100.

## Key takeaways

- **Sessions:** the existing iOS Drop-in Sessions flow must use **Checkout API v68 or later** and have PayPay added in Customer Area. The page says no *additional PayPay-specific* `/sessions` request or Drop-in configuration parameters. The Sessions requirements table does not restate a redirect-handling requirement, but its TEST section says the shopper is redirected to the DGFT simulator; the base integration still owns action/return handling. The v68+ gate is stated here only; the Advanced table does not give an API minimum. See raw lines 25–46 and 50–59.
- **Advanced:** the existing iOS Drop-in Advanced flow explicitly requires handling `action.type: redirect` and adding PayPay in Customer Area. It says there are no *additional PayPay-specific* configuration or `/payments` parameters. This does not waive the base Advanced request and redirect/return work. See raw lines 63–85.
- For **TEST**, the guide names two DGFT acquirer accounts, with `AUTHFlow` and `SALEFlow` in their identifiers, and says the shopper is redirected to a DGFT simulator to complete the test without the PayPay app. It points to the TEST Customer Area payment list for status. These identifiers label test paths; the page does not establish an actual authorization, capture or sale from the names. See raw lines 50–59 and 87–98.
- For **LIVE**, both branches say an **activated PayPay smartphone app** must be accessed through a **Japan-local IP address**. The guide does not demonstrate app activation, shopper authentication, provider approval, a final result webhook or settlement. See raw lines 61 and 100. The linked overview's JP/JPY capability marks are separate high-level scope, not proof of this merchant's live availability.

## Detail locators

- **Sessions version, Customer Area setup and no-extra-method-fields:** raw lines 25–46.
- **Advanced redirect and no-extra-method-fields:** raw lines 63–85.
- **TEST DGFT simulator accounts, redirection and status route:** raw lines 50–59, 87–98.
- **LIVE app and Japan-local-IP condition:** raw lines 61 and 100.

## Related

- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-paypay]]
- [[adyen-payment-testing]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/paypay/ios-drop-in/2026-09-15|PayPay iOS Drop-in — captured 2026-09-15]]
