---
title: "Adyen Rakuten Pay Flutter Component"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/rakutenpay/flutter-component"
raw_files:
  - "adyen/docs/payment-methods/rakutenpay/flutter-component/2026-09-15.md"
tags: [adyen, rakutenpay, flutter, components, recurring, japan]
---

## Overview

This [[adyen]] guide adds Rakuten Pay to an **existing Flutter Components** Sessions or Advanced integration. It covers redirect prerequisites, method-specific request/configuration scope, conditional recurring claims and TEST simulator steps. See [[adyen-online-payments]] and [[adyen-tokenization]]. The 2026-09-15 snapshot does not establish current enablement, actual authorization, capture or settlement.

## Key takeaways

- **Sessions** requires an existing Flutter Components Sessions flow, **Checkout API v68 or later**, handling `action.type: redirect`, and adding Rakuten Pay in Customer Area. The integration-type link is mismatched: its text says Sessions Flutter Components, but its URL points to **Advanced Flutter Drop-in**. The redirect/session-creation links point to Sessions Components. The page says no additional Rakuten Pay `/sessions` parameters or configuration. See raw lines 25–46.
- **Advanced** requires an existing Flutter Components Advanced flow, redirect action handling and Customer Area addition. Its integration-type link text names Flutter Components, but its URL likewise points to **Advanced Flutter Drop-in**; separate redirect/payment links target Advanced Components. It says no extra Rakuten Pay `/payments` parameters or configuration. No Advanced Checkout API minimum is stated. See raw lines 64–86.
- Each flow repeats the same **recurring** conditions: for a business model based on subscriptions and unscheduled card-on-file payments, one-off card-on-file transactions are permitted **after review**. Without a periodic charging cadence, the page prohibits initiating the card-on-file Recurring Processing Model (described as primarily allowed for Food & Beverage), and says to apply for **every Recurring Processing Model** when requesting Rakuten Pay. It links token creation separately and **strongly recommends**, rather than mandates in this page, explicit shopper permission plus schedule/amount transparency. See raw lines 48–54 and 88–94.
- TEST uses `DGFT_AcquirerAccount_RakutenPay_closedLoop`, redirects to a DGFT simulator without needing the Rakuten Pay app, and points to Customer Area for test-account status. Despite the “Test and go live” headings, this guide gives no separate live setup or final webhook/payment-result procedure. Simulator steps and status lookup are not live-payment proof. See raw lines 56–62 and 96–102.

## Detail locators

- **Sessions setup and wrong Advanced Drop-in prerequisite URL:** raw lines 25–46.
- **Advanced setup and wrong Drop-in prerequisite URL:** raw lines 64–86.
- **Recurring review/cadence/application and consent wording:** raw lines 48–54 and 88–94.
- **TEST acquirer, DGFT simulator and status:** raw lines 56–62 and 96–102.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-rakutenpay]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/rakutenpay/flutter-component/2026-09-15|Rakuten Pay Flutter Component guide — captured 2026-09-15]]
