---
title: "Adyen Rakuten Pay iOS Component guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/rakutenpay/ios-component"
raw_files:
  - "adyen/docs/payment-methods/rakutenpay/ios-component/2026-09-15.md"
tags: [adyen, rakuten-pay, ios, component, redirect, recurring]
---

## Overview

This [[adyen]] page adds **Rakuten Pay** to an existing **iOS Components** integration under separate **Sessions** and **Advanced** server-side flows. It uses `InstantPaymentComponent` and requires `redirect` action handling. It also gives unusually conditional card-on-file/recurring language and a **DGFT simulator** TEST route. The page itself states no merchant-country/currency eligibility, final webhook condition, live enablement result or proven payment outcome. [[adyen-online-payments]]

## Key takeaways

- **Sessions base path:** The Sessions section requires an existing iOS Components integration, **Checkout API v68 or later**, redirect handling and Rakuten Pay added in Customer Area. It says no additional Rakuten Pay-specific /sessions parameters or configuration. Its Swift example checks for `.other("rakutenpay")`, creates `InstantPaymentComponent`, sets the session as delegate and initiates payment. Those client steps do not confirm an authorization or final outcome. See raw lines 25–69.
- **Advanced base path and link mismatch:** The Advanced section requires existing iOS Components and redirect handling, with Customer Area addition. However, its Integration type link points to `integration=Drop-in` despite its Components text. It says no extra method-specific configuration or ordinary /payments parameters. Its Swift example sets the Component's delegate to `self`, versus the Sessions sample's `session`; code fragments depend on main integration context. No Advanced API minimum is stated here. See raw lines 88–131.
- **Narrow recurring/card-on-file claim:** Both sections say that when the business model is based on **subscription and unscheduled card-on-file**, Rakuten Pay permits **one-off card-on-file** transactions only **after review**. Without a periodic charging cadence, the page says initiating the card-on-file Recurring Processing Model is prohibited; it says this is primarily allowed for the **Food & Beverage** category. It also says to apply for **each Recurring Processing Model** when requesting Rakuten Pay. The wording should not be flattened into broad recurring or token eligibility. The page links token creation and strongly recommends explicit shopper permission plus transparent schedule/amount for future recurring payments; it does not document an obtained consent or token. See raw lines 72–78 and 133–139.
- **TEST scope:** The page identifies `DGFT_AcquirerAccount_RakutenPay_closedLoop` for **TEST** and says a **DGFT simulator**, not the Rakuten Pay app, completes the test route. It points to Customer Area payment-list status for test account transactions. Simulator redirection and status lookup are not production or final settlement evidence; this page gives no specific live setup procedure. See raw lines 80–86 and 141–147.

## Detail locators

- Sessions prerequisites, base request and Swift initialization: raw lines 25–69.
- Sessions recurring qualification and TEST simulator: raw lines 72–86.
- Advanced prerequisites, mislinked Components URL and base request: raw lines 88–131.
- Repeated recurring qualification and TEST route: raw lines 133–147.

## Related

- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-rakutenpay]]
- [[adyen]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/rakutenpay/ios-component/2026-09-15|Adyen Rakuten Pay iOS Component snapshot]]
