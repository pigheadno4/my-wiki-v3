---
title: "WeChat Pay Mini Program"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/wechat-pay/wechat-pay-mini-program"
raw_files:
  - "adyen/docs/payment-methods/wechat-pay/wechat-pay-mini-program/2026-09-15.md"
tags: [adyen, wechat-pay, mini-program, api-only, cny]
---

## Overview

This 2019-modified, 2026-09-15-captured [[adyen]] page is a short **WeChat Pay Mini Program** overview, routed through [[adyen-online-payments]]. It defines a Mini Program as a native app or website within the WeChat social-app platform, sketches a **typical** shopper journey and says the Mini Program is available for **API-only** integrations. It is separate from the in-app Components and desktop QR routes.

## Key takeaways

- In the page's typical sequence, the shopper opens WeChat and the Mini Program; the **merchant** sends a payment request with method type `wechatpayMiniProgram`; WeChat displays a payment screen; the shopper sees a **CNY** amount, chooses Pay Now, sees a conversion rate and chooses a funding source. The page says the shopper always pays from the WeChat Pay wallet in CNY **even if the amount is processed in another currency**. This distinguishes shopper payment currency from processing currency without specifying an allowed processing-currency list.
- The sequence ends with the shopper seeing “Payment successful” after funds are deducted from their balance. That is a **described typical experience**, not an observed transaction, server API response, authorization webhook, capture or settlement proof.
- This page gives no provider app registration, WeChat merchant ID, Adyen Customer Area setup, entity/country eligibility, API version, credentials, request body beyond method type, or callback/webhook instructions. The separate [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-mini-program-api-only]] is the route for API-only implementation detail; its presence as a link does not make this overview evidence for its behavior.

## Detail locators

- [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-mini-program/2026-09-15|Pinned raw]], lines 15–19: title, description and Mini Program definition.
- Same raw, lines 21–30: explicitly typical shopper journey, merchant method type, CNY/processing-currency distinction and UI outcome wording.
- Same raw, line 32: API-only scope.

## Related

- [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-mini-program-api-only]] — separate API-only implementation guide.
- [[source-adyen-docs-payment-methods-wechat-pay]] — wallet overview.

## Raw Sources

- [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-mini-program/2026-09-15|WeChat Pay Mini Program]]
