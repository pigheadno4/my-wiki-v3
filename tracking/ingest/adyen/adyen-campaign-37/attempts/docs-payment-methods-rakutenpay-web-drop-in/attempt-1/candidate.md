---
title: "Rakuten Pay Web Drop-in"
type: source
date_ingested: 2026-10-25
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/rakutenpay/web-drop-in"
raw_files:
  - "adyen/docs/payment-methods/rakutenpay/web-drop-in/2026-09-15.md"
tags: [adyen, rakuten-pay, web, drop-in, redirect]
---

## Overview

Adyen's 2026-09-15 Rakuten Pay Web Drop-in page gives method-specific additions for existing Web Drop-in Sessions and Advanced flows. It routes a redirect action through the existing integration and separately qualifies Rakuten Pay's card-on-file/recurring use. It does not prove current merchant eligibility or a completed payment. See [[adyen]] and [[adyen-online-payments]].

## Key takeaways

- **Sessions:** Requires an existing Web Drop-in Sessions integration, Checkout API v68 or later, `action.type: redirect` handling, and Rakuten Pay added in Customer Area. The page says no extra method-specific `/sessions` parameters. Importing `Redirect` separately is **optional** for tree-shaken Adyen Web imports, not a universal integration prerequisite. [Raw lines 25–53]
- **Advanced:** Requires an existing Web Drop-in Advanced integration, redirect handling and Rakuten Pay added in Customer Area. The page says no extra method-specific ordinary `/payments` parameters. Its Advanced prerequisite URL contains an unresolved template expression in the `platform` query, while the surrounding label and action link say Web Drop-in; use the stated flow rather than that literal malformed URL as behavioral evidence. [Raw lines 76–104]
- **Conditional recurring/card-on-file:** The page says Rakuten Pay permits one-off card-on-file transactions **after review** for a business model based on subscription and unscheduled card-on-file payments. Without a periodic charging cadence, it says Rakuten Pay prohibits initiating the card-on-file Recurring Processing Model, which it says is primarily allowed for Food & Beverage. Merchants must apply for **every** Recurring Processing Model when requesting Rakuten Pay. The page points to general token creation and strongly recommends explicit shopper permission and transparency about schedule and amount; that recommendation is not phrased as a page-specific mandatory consent field. No token-created event or recurring payment outcome is documented here. [Raw lines 56–64, 106–114]
- **TEST:** The page names `DGFT_AcquirerAccount_RakutenPay_closedLoop` for TEST payments and says the shopper is redirected to a DGFT simulator rather than needing the Rakuten Pay app; test transaction status is checked in Customer Area. This is a test route, not a live setup rule or evidence of successful payment. [Raw lines 66–74, 116–124]

## Detail locators

- Both flows require redirect handling through the linked base guide. The page gives no Rakuten Pay-specific return, webhook, authorization, capture or settlement procedure; a simulator redirect or request does not establish any final status.
- No Japan country/currency discovery table, minimum Web SDK version, refund/cancellation route or live activation sequence is stated in this page. Apply those only from separately read authority.

## Related

- [[adyen-online-payments]]

## Raw Sources

- [[raw/adyen/docs/payment-methods/rakutenpay/web-drop-in/2026-09-15|Rakuten Pay Web Drop-in (2026-09-15)]]
