---
title: "Rakuten Pay Android Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/rakutenpay/android-drop-in"
raw_files:
  - "adyen/docs/payment-methods/rakutenpay/android-drop-in/2026-09-15.md"
tags: [adyen, rakuten-pay, android, drop-in, recurring]
---

## Overview

This 2026-09-15 Rakuten Pay Android Drop-in guide supplies method-specific additions to an existing Sessions-flow or Advanced-flow integration. It separates the two server-side flows and links back to their respective main integration guides; it does not specify a complete standalone payment flow. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- For Sessions, an existing Android Sessions-flow Drop-in integration and Checkout API v68 or later are required, plus Rakuten Pay setup in Customer Area. The guide says no additional `/sessions` parameters are needed. See raw lines 25–40.
- For Advanced, an existing Android Drop-in integration must handle `action.type: redirect`, and Rakuten Pay must be added in Customer Area. The guide says no additional `/payments` parameters are needed. The redirect prerequisite here should not be silently imposed on the separately described Sessions section. See raw lines 84–120.
- Both flow sections show `setSubmitButtonVisible` as optional configuration: setting false hides the submit button, whose default is true. The displayed Kotlin block is schematic, not a complete runnable integration. See raw lines 42–62 and 94–114.
- The duplicated recurring sections constrain card-on-file use: for the stated subscription and unscheduled card-on-file business models, one-off card-on-file transactions require review; without a periodic charging cadence, initiating the card-on-file Recurring Processing Model is prohibited. The guide says to apply for every Recurring Processing Model when requesting Rakuten Pay, and strongly recommends explicit shopper permission for future recurring payments. These statements do not confer tokenization or recurring approval. See raw lines 64–72 and 122–128.
- In TEST, the guide names acquirer account `DGFT_AcquirerAccount_RakutenPay_closedLoop` and a DGFT simulator redirect that does not require the Rakuten Pay app; it points to Customer Area Payment list for test transaction status. This simulator path is not evidence of a live app handoff or a successful real payment. See raw lines 74–82 and 130–136.

## Detail locators

- Sessions requirements, parameters and configuration: raw lines 25–62.
- Advanced requirements, redirect handling, parameters and configuration: raw lines 84–120.
- Recurring and testing qualifications: raw lines 64–82 and 122–136.

## Related

- [[adyen-online-payments]] — online payment integrations.
- [[source-adyen-docs-payment-methods-rakutenpay]] — Rakuten Pay method overview and its separate channel/capability context.
- [[adyen]] — provider entry.

## Raw Sources

- [[raw/adyen/docs/payment-methods/rakutenpay/android-drop-in/2026-09-15|Rakuten Pay Android Drop-in (2026-09-15)]]
