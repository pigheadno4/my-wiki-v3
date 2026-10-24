---
title: "Adyen WeChat Pay overview"
type: source
date_ingested: 2026-10-24
original_format: webpage
canonical_url: "https://docs.adyen.com/payment-methods/wechat-pay"
raw_files:
  - "adyen/docs/payment-methods/wechat-pay/2026-09-15.md"
tags: [adyen, wechat-pay, wallets, online-payments, payment-methods]
---

## Overview

This [[adyen]] WeChat Pay overview, captured 2026-09-15, identifies website, mobile-app and point-of-sale acceptance routes and links separate integration guides. Its high-level matrix marks a wallet with an additional-action flow and specific refund/capture limitations. See [[adyen-online-payments]]. It is a historical capability/navigation snapshot, not proof of current merchant eligibility, enabled payment methods or a completed authorization, capture, refund or settlement. See raw lines 15–71.

## Key takeaways

- The page describes WeChat as an app used in China and says users with Chinese bank accounts can link those accounts to pay online or in person. Its matrix says countries `International` and currencies `Multiple`, without enumerating eligible countries, merchant entities or currencies. The historical “over 900 million” monthly-user figure has no measurement period on this page; do not treat it as a current count. See raw lines 23–25 and 37–39.
- The overview lists website, mobile-app and POS acceptance. For **mobile websites**, it expressly supports only payments initiated **from the WeChat app** and points to the in-app payments guide. This qualification must travel with the separate “Desktop QR and H5” link, whose label broadly describes desktop/mobile browsers; the overview alone does not explain or resolve the H5 journey. Desktop QR/H5, iOS/Android in-app, Pay by Link, POS QR-wallet and Mini Program are distinct linked routes; their setup, versions and transaction mechanics are in child guides. See raw lines 27–33 and 41–71.

> [!warning] Contradiction
> This overview was last modified 2023-03-09 and says **mobile websites only support payments initiated from the WeChat app** (its raw line 33). The linked [[source-adyen-docs-payment-methods-wechat-pay-wechat-pay-desktop-qr-payments]] H5 overview was last modified 2019-07-04 and describes a shopper starting in a **mobile browser**, redirecting to the WeChat Pay app and back, after Support enrolment of the web shop URL (that page's raw lines 19–27). The pages do not reconcile what “initiated” means or whether the older H5 route remains available. Do not treat the H5 description as current enablement or collapse it into the distinct merchant mobile-app flow.
- Most payments get an immediate success confirmation, but a small number do not; for those, the page requires a **webhook** to confirm success. A shopper handoff, QR scan, app return or immediate client response alone is therefore not universal final-outcome evidence. The overview gives no webhook event schema or reconciliation procedure. See raw line 35.
- The matrix calls the payment flow `Additional action`, countries `International`, currencies `Multiple`; marks recurring, separate/partial/multiple partial captures and chargebacks unavailable; and marks refunds, partial refunds and multiple partial refunds available in this snapshot. Capability marks do not provide the procedure, account enablement or actual payment/refund outcome. See raw lines 37–39.

## Detail locators

- **User/account context and claimed coverage:** raw lines 23–25.
- **Channels and mobile-web initiation condition:** raw lines 27–33.
- **Immediate versus webhook-confirmed result:** raw line 35.
- **Capability matrix:** raw lines 37–39.
- **Distinct integration-route links:** raw lines 41–71.

## Related

- [[adyen-online-payments]]
- [[adyen-webhooks]]

## Related raw API references

- [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-desktop-qr-payments/2026-09-15|WeChat Pay desktop QR and H5 guide]] — linked child route; implementation details require that guide.
- [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-in-app-payments/2026-09-15|WeChat Pay in-app guide]] — linked child route for app and mobile-web initiation context.
- [[raw/adyen/docs/payment-methods/wechat-pay/wechat-pay-mini-program/2026-09-15|WeChat Pay Mini Program guide]] — linked child route; separate flow.

## Raw Sources

- [[raw/adyen/docs/payment-methods/wechat-pay/2026-09-15|WeChat Pay overview — captured 2026-09-15]]
