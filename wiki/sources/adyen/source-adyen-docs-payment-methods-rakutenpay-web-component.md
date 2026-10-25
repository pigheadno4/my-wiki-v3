---
title: "Adyen Rakuten Pay Web Component guide"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/rakutenpay/web-component"
raw_files:
  - "adyen/docs/payment-methods/rakutenpay/web-component/2026-09-15.md"
tags: [adyen, rakuten-pay, web, components, redirect, online-payments]
---

## Overview

This 2026-09-15 Adyen page describes **Rakuten Pay-specific additions** to an existing Web Components integration, separately for Sessions and Advanced flows. It gives Redirect Component use, exceptional recurring-model conditions and a TEST simulator route. It does not prove that a merchant is approved for any recurring model or that a transaction was authorized. [[adyen]] [[adyen-online-payments]]

## Key takeaways

- **Sessions prerequisites and base additions:** The page requires an existing Web Components Sessions integration, **Checkout API v68 or later**, redirect handling for `action.type: redirect`, and Rakuten Pay added in Customer Area. It states no extra Rakuten Pay `/sessions` parameters or configuration are needed for the ordinary flow. It imports `Redirect` from Adyen Web and initializes Rakuten Pay through that class. (raw lines 25–71)
- **Advanced prerequisites and base additions:** The Advanced section requires an existing Web Components Advanced integration, redirect handling and Customer Area addition, then imports/initializes `Redirect`. It says no extra ordinary `/payments` parameters are needed. This section does not separately state the Sessions-row API minimum. The no-extra wording does not waive base integration requirements or the distinct review/application conditions for recurring. (raw lines 90–128)
- **Recurring restrictions:** Both sections say that for business models based on subscription and unscheduled card-on-file, Rakuten Pay permits **one-off card-on-file transactions only after a review process**. They say that without a periodic charging cadence, Rakuten Pay **prohibits initiating the card-on-file Recurring Processing Model**, described as primarily allowed for Food & Beverage. The merchant **must apply for every Recurring Processing Model** when requesting Rakuten Pay. The page routes tokenization implementation to a separate Create tokens guide and **strongly recommends** explicit shopper permission for future recurring payments; this recommendation is not worded as a blanket source requirement. The paragraph's subscription/unscheduled/one-off wording is nuanced and does not establish general recurring availability for a merchant. (raw lines 74–80, 130–136)
- **Example qualification:** Both initialization snippets use `new Redirect(checkout, { type:rakutenpay })`, but this page does not define a `rakutenpay` variable. Treat it as an unresolved sample-value ambiguity and consult the matching Adyen Web API/base guide before implementing; the snippet does not prove the code runs as printed or a checkout completes. The page gives no explicit Adyen Web SDK minimum. (raw lines 48–71, 104–121)
- **TEST scope:** The page names `DGFT_AcquirerAccount_RakutenPay_closedLoop` for TEST and says the shopper is redirected to a DGFT simulator without needing the Rakuten Pay app. It directs status checks to Customer Area. Despite a “Test and go live” heading, this snapshot gives no separate LIVE enablement steps or a final payment webhook/status sequence. TEST simulator completion does not establish live merchant eligibility or settlement. (raw lines 82–88, 138–144)

## Detail locators

- Sessions API/redirect/Customer Area prerequisites and no-extra statements: raw lines 25–60.
- Redirect import/initialization and undefined sample identifier: raw lines 48–71, 104–121.
- Recurring review, cadence/category limits, per-model application and consent recommendation: raw lines 74–80, 130–136.
- Advanced base prerequisites, no-extra ordinary request fields: raw lines 90–128.
- TEST DGFT acquirer/simulator and status-list route: raw lines 82–88, 138–144.

## Related

- [[adyen]]
- [[adyen-online-payments]]
- [[adyen-tokenization]]
- [[source-adyen-docs-payment-methods-rakutenpay]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/rakutenpay/web-component/2026-09-15|Adyen Rakuten Pay Web Component, 2026-09-15 snapshot]]
