---
title: "DOKU payment methods Web Drop-in integration"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/doku/drop-in"
raw_files:
  - "adyen/docs/payment-methods/doku/drop-in/2026-09-15.md"
tags: [adyen, doku, indonesia, web, drop-in]
---

## Overview

This 2026-09-15 capture of a page last modified in 2019 describes adding partner **DOKU** payment methods to an existing **Web Drop-in** integration for Indonesia. It covers bank-transfer virtual accounts and convenience-store vouchers, Sessions or Advanced prerequisites, method-specific configuration scope, and TEST/live routing. It does not document an executed bank transfer, cash payment, authorization webhook or settlement. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Method and flow scope:** the page distinguishes Indonesian DOKU bank-transfer and convenience-store methods. Its Sessions tab requires an existing Sessions-flow Web Drop-in; its Advanced tab requires an existing Advanced-flow Web Drop-in. Both say to add DOKU payment methods in Customer Area first. It states no Checkout API minimum in either tab. (raw lines 17–39)
- **Versioned resource and API routing:** Web Drop-in **v6** users are shown an `AdyenCheckout` and `Doku` import from `@adyen/adyen-web`. The API section says no extra DOKU-specific fields, calls `/sessions` the default with Drop-in **v5.0.0 or later**, and points `/payments` to additional-use-case integrations. It also says no DOKU-specific Drop-in configuration steps. These statements concern the method add-on, not the whole base integration or every DOKU variant's eligibility. (raw lines 41–58)
- **Expiry and voucher language:** the page says the default validity period for a bank-transfer virtual account or convenience-store voucher is **48 hours** and directs merchants to Support to customize that period. It says voucher language can be Indonesian when the checkout page specifies `locale: id-ID`. These are configuration statements, not proof that a particular account, voucher or order remains valid for a measured period. (raw lines 60–64)
- **TEST/LIVE boundary:** the page routes simulated payments to test vouchers and card-number credentials and points to the test Customer Area payment list for status. That generic test-resource label does not recast DOKU as a card method. For live acceptance it requires a request in **live Customer Area** for one or more Indonesian DOKU online-banking or convenience-store methods; the page uses “bank transfer” earlier and “online banking” in the live-request sentence without further explaining the relationship between those labels. No outcome is observed here. (raw lines 66–72)

## Detail locators

- Indonesia variant identity and Sessions/Advanced prerequisites: raw lines 17–39.
- v6 import, endpoint routing and no method-specific configuration: raw lines 41–58.
- Virtual-account/voucher validity and voucher language: raw lines 60–64.
- Test-resource route, status lookup and live request: raw lines 66–72.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[source-adyen-docs-payment-methods-doku]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/doku/drop-in/2026-09-15|Adyen DOKU Web Drop-in, 2026-09-15 snapshot]]
